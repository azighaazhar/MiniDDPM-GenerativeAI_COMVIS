"""diffusion.py - noise schedule, forward process, dan sampling (reverse process) DDPM."""

import torch

import config


def _extract(values, t, x):
    """Ambil values[t] lalu ubah ke (B,1,1,1) agar bisa dikalikan dengan x (B,C,H,W)."""
    out = values.to(x.device)[t.to(x.device)]
    return out.reshape(t.shape[0], *([1] * (x.dim() - 1)))


class Diffusion:
    def __init__(self, T, device=None,
                 beta_start=config.BETA_START, beta_end=config.BETA_END):
        # Skala BETA_REFERENCE_T/T (1000/T) menjaga total noise tetap sama saat T berubah.
        scale = config.BETA_REFERENCE_T / T
        if beta_end * scale >= 1.0:
            raise ValueError(f"T={T} terlalu kecil: beta akhir jadi >= 1")

        self.T = T
        self.betas = torch.linspace(beta_start * scale, beta_end * scale, T, device=device)
        self.alphas = 1.0 - self.betas
        self.alpha_bars = torch.cumprod(self.alphas, dim=0)

        self.sqrt_alpha_bars = self.alpha_bars.sqrt()
        self.sqrt_one_minus_alpha_bars = (1.0 - self.alpha_bars).sqrt()
        self.sqrt_recip_alphas = (1.0 / self.alphas).sqrt()
        self.sqrt_betas = self.betas.sqrt()  # simpangan baku noise tambahan saat sampling

    def add_noise(self, x0, t, noise):
        """Forward process: x_t = sqrt(a_bar_t) * x0 + sqrt(1 - a_bar_t) * noise."""
        return (_extract(self.sqrt_alpha_bars, t, x0) * x0
                + _extract(self.sqrt_one_minus_alpha_bars, t, x0) * noise)

    def sample_timesteps(self, batch_size, device):
        """t acak bertipe long, nilai 0 sampai T-1 (batas atas randint tidak ikut)."""
        return torch.randint(0, self.T, (batch_size,), device=device)

    @torch.no_grad()
    def sample(self, model, num_images, device):
        """Reverse process: dari noise murni ke gambar (N, C, 28, 28) dalam [-1, 1].

        Mode eval/train model diatur pemanggil (train.py), bukan di sini.
        """
        size = config.IMAGE_SIZE
        shape = (num_images, config.MODEL_PARAMS["in_channels"], size, size)
        x = torch.randn(shape, device=device)

        for i in reversed(range(self.T)):
            t = torch.full((num_images,), i, device=device, dtype=torch.long)
            pred_noise = model(x, t)

            # Buang bagian noise yang diprediksi -> rata-rata estimasi x_{t-1}
            coef = _extract(self.betas, t, x) / _extract(self.sqrt_one_minus_alpha_bars, t, x)
            mean = _extract(self.sqrt_recip_alphas, t, x) * (x - coef * pred_noise)

            # Noise baru di setiap langkah, kecuali langkah terakhir (t=0)
            if i > 0:
                x = mean + _extract(self.sqrt_betas, t, x) * torch.randn_like(x)
            else:
                x = mean

        return x.clamp(-1.0, 1.0)


if __name__ == "__main__":
    from utils import get_device, set_seed

    set_seed(config.SEED)
    device = get_device()
    C = config.MODEL_PARAMS["in_channels"]

    # 1. Noise schedule: shape, alpha-bar turun dari ~1 ke ~0, total beta konstan
    ref_beta_sum = Diffusion(config.BETA_REFERENCE_T).betas.sum().item()
    for T_test in (100, 500, 1000, 2000):
        d = Diffusion(T_test)
        ab = d.alpha_bars
        assert d.betas.shape == (T_test,) and ab.shape == (T_test,)
        assert ((d.betas > 0) & (d.betas < 1)).all()
        assert (ab[1:] < ab[:-1]).all(), "alpha-bar harus menurun"
        assert ab[0] > 0.99 and ab[-1] < 1e-3
        assert abs(d.betas.sum().item() - ref_beta_sum) < 1e-2, "total beta harus tetap"
        print(f"schedule OK  T={T_test:<5} alpha_bar[0]={ab[0]:.5f}  alpha_bar[-1]={ab[-1]:.2e}")

    try:
        Diffusion(10)
        raise AssertionError("T=10 seharusnya ditolak")
    except ValueError:
        print("T terlalu kecil ditolak OK")

    # 2. Forward process pada gambar sintetis (kotak putih di latar hitam)
    d = Diffusion(config.T, device)
    x0 = torch.full((8, C, config.IMAGE_SIZE, config.IMAGE_SIZE), -1.0, device=device)
    x0[:, :, 8:20, 8:20] = 1.0
    noise = torch.randn_like(x0)

    errors = []
    for t_val in (0, d.T // 4, d.T // 2, d.T - 1):
        t = torch.full((8,), t_val, device=device, dtype=torch.long)
        xt = d.add_noise(x0, t, noise)
        assert xt.shape == x0.shape
        errors.append(((xt - x0) ** 2).mean().item())
    assert all(a < b for a, b in zip(errors, errors[1:])), "gambar harus makin berisik"
    assert (xt - noise).abs().max().item() < 0.05, "t=T-1 harus ~ noise murni"
    print("forward process OK  MSE ke gambar asli:", [f"{e:.4f}" for e in errors])

    # 3. Bentuk tertutup sama dengan menambah noise langkah demi langkah (uji statistik)
    t_check = d.T // 3
    x = torch.ones(20000, device=device)
    for i in range(t_check + 1):
        x = d.alphas[i].sqrt() * x + d.betas[i].sqrt() * torch.randn_like(x)
    assert abs(x.mean().item() - d.sqrt_alpha_bars[t_check].item()) < 0.05
    assert abs(x.std().item() - d.sqrt_one_minus_alpha_bars[t_check].item()) < 0.05
    print("bentuk tertutup = langkah bertahap OK")

    # 4. Pengambilan t acak: tipe long, rentang 0..T-1, kedua ujung tercapai
    small = Diffusion(50, device)
    ts = small.sample_timesteps(2000, device)
    assert ts.shape == (2000,) and ts.dtype == torch.long
    assert ts.min().item() == 0 and ts.max().item() == 49
    print("sample_timesteps OK")

    # 5. Sampling dengan model tiruan: prediksi noise nol, mencatat t yang diterima
    class SpyModel:
        def __init__(self):
            self.t_seen = []

        def __call__(self, x, t):
            assert t.shape == (x.shape[0],) and t.dtype == torch.long
            self.t_seen.append(int(t[0]))
            return torch.zeros_like(x)

    N = 4
    spy = SpyModel()
    out = d.sample(spy, N, device)
    assert out.shape == (N, C, config.IMAGE_SIZE, config.IMAGE_SIZE)
    assert torch.isfinite(out).all() and out.min() >= -1 and out.max() <= 1
    assert not out.requires_grad and out.device.type == device.type
    assert spy.t_seen == list(range(d.T - 1, -1, -1)), "t harus T-1 turun ke 0"
    print("sampling (model tiruan) OK")

    # 6. Model oracle yang tahu gambar asli: hasil sampling harus kembali ke gambar itu.
    #    Gagal bila indeks t salah atau noise ikut ditambahkan di langkah terakhir.
    target = x0[:N]

    def oracle(x, t):
        ab = _extract(d.alpha_bars, t, x)
        return (x - ab.sqrt() * target) / (1 - ab).sqrt()

    out = d.sample(oracle, N, device)
    assert (out - target).abs().max().item() < 5e-3
    print("sampling (model oracle) OK")
    print("diffusion.py OK")