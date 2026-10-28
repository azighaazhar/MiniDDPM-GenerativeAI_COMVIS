"""model.py - U-Net penebak noise untuk Mini DDPM.

Berisi: timestep embedding sinusoidal, blok dasar (ResBlock), dan UNet.
Alur ukuran: 28 -> 14 -> 7 -> 14 -> 28. Dibuat dengan UNet(**config.MODEL_PARAMS).
"""

import math

import torch
import torch.nn as nn

import config


def _group_norm(channels):
    # Jumlah grup terbesar dari (8, 4, 2, 1) yang habis membagi jumlah channel
    for groups in (8, 4, 2, 1):
        if channels % groups == 0:
            return nn.GroupNorm(groups, channels)


class SinusoidalTimeEmbedding(nn.Module):
    """t (B,) bertipe long -> vektor (B, dim) berisi sin dan cos berbagai frekuensi."""

    def __init__(self, dim):
        super().__init__()
        if dim % 2 != 0:
            raise ValueError("time_emb_dim harus genap")
        self.dim = dim

    def forward(self, t):
        half = self.dim // 2
        # Frekuensi turun geometris dari 1 ke 1/10000
        exponent = -math.log(10000.0) * torch.arange(half, device=t.device, dtype=torch.float32) / half
        freqs = torch.exp(exponent)                      # (half,)
        args = t.float()[:, None] * freqs[None, :]       # (B, half)
        return torch.cat([args.sin(), args.cos()], dim=1)  # (B, dim)


class ResBlock(nn.Module):
    """Dua konvolusi 3x3; embedding waktu ditambahkan di antaranya."""

    def __init__(self, in_ch, out_ch, time_emb_dim):
        super().__init__()
        self.norm1 = _group_norm(in_ch)
        self.conv1 = nn.Conv2d(in_ch, out_ch, 3, padding=1)
        self.time_proj = nn.Sequential(nn.SiLU(), nn.Linear(time_emb_dim, out_ch))
        self.norm2 = _group_norm(out_ch)
        self.conv2 = nn.Conv2d(out_ch, out_ch, 3, padding=1)
        self.act = nn.SiLU()
        # Jalan pintas residual; 1x1 conv bila jumlah channel berubah
        self.shortcut = nn.Conv2d(in_ch, out_ch, 1) if in_ch != out_ch else nn.Identity()

    def forward(self, x, t_emb):
        h = self.conv1(self.act(self.norm1(x)))
        h = h + self.time_proj(t_emb)[:, :, None, None]  # (B,C) -> (B,C,1,1), disiarkan ke semua piksel
        h = self.conv2(self.act(self.norm2(h)))
        return h + self.shortcut(x)


class Downsample(nn.Module):
    def __init__(self, ch):
        super().__init__()
        self.conv = nn.Conv2d(ch, ch, 3, stride=2, padding=1)  # 28->14, 14->7

    def forward(self, x):
        return self.conv(x)


class Upsample(nn.Module):
    def __init__(self, ch):
        super().__init__()
        self.up = nn.Upsample(scale_factor=2, mode="nearest")  # 7->14, 14->28
        self.conv = nn.Conv2d(ch, ch, 3, padding=1)

    def forward(self, x):
        return self.conv(self.up(x))


class UNet(nn.Module):
    def __init__(self, in_channels, base_channels, channel_mults, time_emb_dim):
        super().__init__()
        n = len(channel_mults)
        if not 1 <= n <= 3:
            raise ValueError("channel_mults harus berisi 1 sampai 3 level (maks. dua downsampling)")
        chs = [base_channels * m for m in channel_mults]

        self.time_mlp = nn.Sequential(
            SinusoidalTimeEmbedding(time_emb_dim),
            nn.Linear(time_emb_dim, time_emb_dim),
            nn.SiLU(),
            nn.Linear(time_emb_dim, time_emb_dim),
        )
        self.init_conv = nn.Conv2d(in_channels, chs[0], 3, padding=1)

        # Jalur turun: level i menerima channel dari level sebelumnya
        self.down_blocks = nn.ModuleList(
            [ResBlock(chs[max(i - 1, 0)], chs[i], time_emb_dim) for i in range(n)]
        )
        self.downsamples = nn.ModuleList([Downsample(chs[i]) for i in range(n - 1)])

        self.mid1 = ResBlock(chs[-1], chs[-1], time_emb_dim)
        self.mid2 = ResBlock(chs[-1], chs[-1], time_emb_dim)

        # Jalur naik, dari level terdalam ke terluar. Input = hasil level di bawahnya + skip.
        self.up_blocks = nn.ModuleList()
        for k in range(n):
            i = n - 1 - k
            self.up_blocks.append(
                ResBlock(chs[i] + chs[min(i + 1, n - 1)], chs[i], time_emb_dim)
            )
        self.upsamples = nn.ModuleList([Upsample(chs[n - 1 - k]) for k in range(n - 1)])

        self.out_norm = _group_norm(chs[0])
        self.out_conv = nn.Conv2d(chs[0], in_channels, 3, padding=1)
        self.act = nn.SiLU()

    def forward(self, x, t):
        t_emb = self.time_mlp(t)
        h = self.init_conv(x)

        skips = []
        for i, block in enumerate(self.down_blocks):
            h = block(h, t_emb)
            skips.append(h)
            if i < len(self.downsamples):
                h = self.downsamples[i](h)

        h = self.mid2(self.mid1(h, t_emb), t_emb)

        for k, block in enumerate(self.up_blocks):
            h = torch.cat([h, skips.pop()], dim=1)  # skip dari level dengan ukuran sama
            h = block(h, t_emb)
            if k < len(self.upsamples):
                h = self.upsamples[k](h)

        return self.out_conv(self.act(self.out_norm(h)))


if __name__ == "__main__":
    from utils import get_device, set_seed

    set_seed(config.SEED)
    device = get_device()
    model = UNet(**config.MODEL_PARAMS).to(device)

    n_params = sum(p.numel() for p in model.parameters())
    print(f"device: {device} | jumlah parameter: {n_params:,}")

    # 1. Shape output sama dengan input
    B, C, S = 4, config.MODEL_PARAMS["in_channels"], config.IMAGE_SIZE
    x = torch.randn(B, C, S, S, device=device)
    t = torch.randint(0, config.T, (B,), device=device)  # long, 0..T-1
    out = model(x, t)
    assert out.shape == x.shape, f"shape salah: {tuple(out.shape)}"
    assert torch.isfinite(out).all()
    print(f"shape OK: {tuple(x.shape)} -> {tuple(out.shape)}")

    # 2. Embedding waktu benar-benar berpengaruh: t berbeda -> output berbeda
    with torch.no_grad():
        o0 = model(x, torch.zeros(B, dtype=torch.long, device=device))
        o1 = model(x, torch.full((B,), config.T - 1, dtype=torch.long, device=device))
    assert (o0 - o1).abs().max().item() > 0
    print("pengaruh t OK")

    # 3. Satu langkah backward: semua parameter mendapat gradien yang valid
    loss = nn.functional.mse_loss(model(x, t), torch.randn_like(x))
    loss.backward()
    missing = [n for n, p in model.named_parameters() if p.grad is None]
    assert not missing, f"tanpa gradien: {missing}"
    assert all(torch.isfinite(p.grad).all() for p in model.parameters())
    print(f"backward OK, loss={loss.item():.4f}")
    print("model.py OK")