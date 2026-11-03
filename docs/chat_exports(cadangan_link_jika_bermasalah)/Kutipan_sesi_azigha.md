haloo

PRD notebook terakhir perlu diselaraskan dengan kode yang sudah jadi (terlampir: config.py, utils.py, model.py, diffusion.py). Keluarkan PRD utuh versi baru. Ubah HANYA hal berikut, jangan menyentuh bagian lain:

Nama di PRD disamakan dengan kode asli:
Diffusion.q_sample diganti Diffusion.add_noise(x0, t, noise)
Diffusion.generate diganti Diffusion.sample(model, num_images, device)
Block diganti ResBlock
Diffusion.sample_timesteps menerima (batch_size, device); perbarui input di tabel kontrak Perbarui semua tempat yang menyebut nama-nama itu (tabel kontrak, jobdesk Ketua, jobdesk Teman B, catatan kontrak). Label yang tadinya [Asumsi] untuk nama-nama ini diganti [Keputusan], karena sudah sesuai kode.
Nama atribut config sama persis dengan config.py (huruf besar: SEED, LEARNING_RATE, BATCH_SIZE, EPOCHS, NUM_WORKERS, T, BETA_START, BETA_END, BETA_REFERENCE_T, IMAGE_SIZE, MODEL_PARAMS, SAMPLE_EVERY_N_EPOCHS, NUM_SAMPLE_IMAGES, SMOKE_TEST, SMOKE_SUBSET_SIZE, SMOKE_EPOCHS, SMOKE_SAMPLE_EVERY, BASE_DIR, DATA_DIR, CHECKPOINT_DIR, RESULTS_DIR, LOSS_CURVES_DIR, SAMPLES_DIR). Tulis daftar ini di Bagian Umum. Tambahkan aturan: anggota melampirkan config.py, model.py, dan diffusion.py ke chat AI mereka supaya nama cocok.
Tambahkan aturan output sel: notebook kerja (ketua.ipynb, A.ipynb, B.ipynb) dikosongkan outputnya sebelum commit (Clear All Outputs); MiniDDPM.ipynb final dijalankan dengan Restart and Run All di mesin ber-GPU lalu disimpan dengan output lengkap.
Tambahkan catatan: jika memakai Colab, versi Python bawaan Colab diterima; yang dijaga adalah tidak memakai fitur khusus Python 3.14.
Catat di Bagian Umum bahwa di notebook ada method Diffusion.sample dan fungsi sample(path_checkpoint) milik Teman B keduanya berbeda.
Di bawah dokumen, di luar PRD, tulis daftar singkat perubahan yang kamu lakukan. Jangan menambah fitur atau butir baru.

Ran a command, shared files
PRD utuh yang baru sudah ada di prd_final_mini_ddpm_notebook.md (menggantikan berkas sebelumnya dengan nama yang sama).

Catatan penting: lampiran config.py, utils.py, model.py, dan diffusion.py tidak terbaca di pesan ini. Saya bekerja dari daftar nama di pesanmu, jadi saya tidak bisa mencocokkannya dengan kode aslinya. Silakan cek sendiri, terutama tanda tangan Diffusion.sample_timesteps(batch_size, device) dan 23 nama atribut config, sebelum PRD dikirim ke Teman A dan B.

Daftar perubahan
Nama disamakan dengan kode.
Diffusion.q_sample menjadi Diffusion.add_noise(x0, t, noise).
Diffusion.generate menjadi Diffusion.sample(model, num_images, device).
Block menjadi ResBlock.
Input Diffusion.sample_timesteps di tabel kontrak menjadi batch_size dan device.
Semua penyebutan nama lama diperbarui di tabel kontrak, catatan kontrak, jobdesk Ketua, dan jobdesk Teman B.
Label keempat nama itu diganti [Keputusan]. SinusoidalTimeEmbedding dan UNet tetap [Asumsi] karena tidak ada dalam daftarmu.
Nama atribut config. Daftar 23 atribut dengan huruf besar ditulis di Bagian Umum, butir 4 (Keputusan teknis). Aturan melampirkan config.py, model.py, dan diffusion.py ke chat AI ditambahkan di butir yang sama, dengan catatan bahwa file itu hanya acuan dan tidak diimpor. Dua baris yang memuat isi config ikut diselaraskan (baris config di tabel kontrak dan baris config di jobdesk Ketua). Satu baris uji Teman B juga ditulis ulang memakai SMOKE_SAMPLE_EVERY dan SMOKE_EPOCHS. Penyebutan config yang bersifat deskriptif di tempat lain, misalnya “batch size” atau “N”, tidak saya ubah.
Aturan output sel. Ditambahkan di Bagian Umum, butir 9 (Aturan sel): notebook kerja dikosongkan outputnya sebelum commit, dan MiniDDPM.ipynb dijalankan dengan Restart and Run All di mesin ber-GPU lalu disimpan dengan output lengkap. Langkah “menjalankan notebook final” di perakitan Ketua disamakan dengan aturan ini dan labelnya menjadi [Keputusan].
Catatan Colab. Ditambahkan di Bagian Umum, butir 5 (Device dan versi Python).
Catatan dua sample. Ditambahkan di catatan kontrak, Bagian Umum butir 10. Penjelasan singkat juga muncul di jobdesk Ketua dan Teman B.
Bagian lain tidak diubah.


Prd final mini ddpm notebook
Document · MD 
Kami memutuskan file .py tidak dipakai sebagai bahan kerja anggota. PRD harus jadi satu-satunya acuan untuk AI Teman A dan Teman B. Keluarkan PRD notebook utuh versi baru. Ubah HANYA ini:

Aturan utama: file .py lama bukan bagian proyek, Saya (Ketua) menghapusnya dari repo setelah ketua.ipynb selesai (riwayat tetap di Git). Anggota tidak memakai dan tidak melampirkan file .py. Acuan nama dan antarmuka hanya PRD ini, jadi anggota melampirkan PRD, bukan file kode. Hapus semua kalimat yang menyuruh melampirkan config.py, model.py, atau diffusion.py, dan hapus baris "*.py lama" dari struktur folder.
Tabel kontrak: tambahkan cara membuat objek dan tanda tangan fungsi publik Ketua: set_seed(seed); get_device(); Diffusion(T, device=None); Diffusion.add_noise(x0, t, noise); Diffusion.sample_timesteps(batch_size, device); Diffusion.sample(model, num_images, device); UNet(in_channels, base_channels, channel_mults, time_emb_dim) dibuat dengan UNet(**config.MODEL_PARAMS) dan dipanggil model(x, t).
Aturan sel: satu sel kode maksimal sekitar 30 baris dan hanya satu fungsi, kelas, atau langkah (pecah yang panjang). Sel markdown pendek, 1-3 kalimat, bahasa sederhana dan natural, tidak kaku.
Di bawah dokumen, di luar PRD, tulis daftar singkat perubahan. Jangan mengubah bagian lain dan jangan menambah butir baru.

Ran a command, shared files
PRD notebook utuh yang baru ada di prd_final_mini_ddpm_notebook.md (menggantikan berkas sebelumnya dengan nama yang sama).

Daftar perubahan
Aturan utama (Bagian Umum, butir 2).
Bullet “file .py lama tetap disimpan sebagai riwayat” diganti dua bullet baru. Pertama, file .py lama bukan bagian proyek dan Ketua menghapusnya dari repo setelah ketua.ipynb selesai (riwayat tetap di Git). Kedua, anggota tidak memakai dan tidak melampirkan file .py, acuan nama dan antarmuka hanya PRD ini, jadi yang dilampirkan adalah PRD, bukan file kode.
Kalimat yang menyuruh melampirkan config.py, model.py, dan diffusion.py dihapus dari butir 4.
Baris *.py lama dihapus dari struktur folder.
Di butir 4, frasa “sama persis dengan config.py” saya hapus dari kalimat daftar atribut config. Alasannya, file itu akan dihapus dan acuannya sekarang PRD. Daftar atributnya sendiri tidak berubah.
Tabel kontrak (butir 10).
Tanda tangan ditambahkan: set_seed(seed), get_device(), Diffusion(T, device=None), Diffusion.add_noise(x0, t, noise), Diffusion.sample_timesteps(batch_size, device), Diffusion.sample(model, num_images, device), dan UNet(in_channels, base_channels, channel_mults, time_emb_dim).
Cara membuat dan memanggil UNet ditulis di baris yang sama: dibuat dengan UNet(**config.MODEL_PARAMS) dan dipanggil model(x, t).
Baris model dipecah menjadi dua: SinusoidalTimeEmbedding dan ResBlock sebagai komponen, serta UNet sendiri.
Label UNet dan Diffusion(T, device=None) menjadi [Keputusan] karena tanda tangannya kamu berikan dari kode. SinusoidalTimeEmbedding tetap [Asumsi].
Di jobdesk Ketua, label UNet pada baris model juga disesuaikan menjadi [Keputusan].
Aturan sel (butir 9).
Bullet “satu sel berisi satu fungsi, satu kelas, atau satu langkah” diganti: satu sel kode maksimal sekitar 30 baris dan hanya satu fungsi, kelas, atau langkah; yang panjang dipecah.
Bullet baru ditambahkan: sel markdown pendek, 1-3 kalimat, bahasa sederhana dan natural, tidak kaku.
Bagian lain tidak diubah. Dua penyebutan python -m scripts.check_data (butir 7 dan jobdesk Teman A) tetap ada, karena fungsinya hanya menjelaskan bahwa perintah itu digantikan sel uji.

Haloo

Ran a command
Kelompok 4 (uji diffusion) adalah Sel 15-21, tujuh sel. Sebelumnya saya menulis “Sel 15-20”, dan itu keliru: totalnya tetap 21 sel, dan penomorannya sekarang konsisten.

Strukturnya saya bandingkan dengan blok main lama: 41 pernyataan, semuanya identik, kecuali pesan terakhir (diffusion.py OK menjadi diffusion OK). Sel 17 adalah sel baru (visualisasi yang sudah kamu setujui), jadi hanya sintaksnya yang saya cek. Komentar sudah dikurangi, tiap sel hanya punya satu baris judul uji.

Sel 15 (kode, uji)

python
# Uji 1: noise schedule
set_seed(config.SEED)
device = get_device()
C = config.MODEL_PARAMS["in_channels"]

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
Sel 16 (kode, uji)

python
# Uji 2: forward process pada gambar sintetis (kotak putih di latar hitam)
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
Sel 17 (kode, uji, visualisasi)

python
# Visualisasi forward process: makin besar t, makin berisik
ts = [0, d.T // 4, d.T // 2, 3 * d.T // 4, d.T - 1]
fig, axes = plt.subplots(1, len(ts), figsize=(2.2 * len(ts), 2.6))
for ax, t_val in zip(axes, ts):
    t = torch.full((1,), t_val, device=device, dtype=torch.long)
    xt = d.add_noise(x0[:1], t, noise[:1])
    ax.imshow(xt[0, 0].cpu().numpy(), cmap="gray", vmin=-1, vmax=1)
    ax.set_title(f"t={t_val}")
    ax.axis("off")
plt.show()
Sel 18 (kode, uji)

python
# Uji 3: bentuk tertutup = menambah noise langkah demi langkah (uji statistik)
t_check = d.T // 3
x = torch.ones(20000, device=device)
for i in range(t_check + 1):
    x = d.alphas[i].sqrt() * x + d.betas[i].sqrt() * torch.randn_like(x)
assert abs(x.mean().item() - d.sqrt_alpha_bars[t_check].item()) < 0.05
assert abs(x.std().item() - d.sqrt_one_minus_alpha_bars[t_check].item()) < 0.05
print("bentuk tertutup = langkah bertahap OK")
Sel 19 (kode, uji)

python
# Uji 4: t acak bertipe long, 0..T-1, kedua ujung tercapai
small = Diffusion(50, device)
ts = small.sample_timesteps(2000, device)
assert ts.shape == (2000,) and ts.dtype == torch.long
assert ts.min().item() == 0 and ts.max().item() == 49
print("sample_timesteps OK")
Sel 20 (kode, uji)

python
# Uji 5: sampling dengan model tiruan (prediksi noise nol) yang mencatat t
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
Sel 21 (kode, uji)

python
# Uji 6: model oracle (tahu gambar asli) -> hasil sampling harus kembali ke gambar itu
target = x0[:N]

def oracle(x, t):
    ab = _extract(d.alpha_bars, t, x)
    return (x - ab.sqrt() * target) / (1 - ab).sqrt()

out = d.sample(oracle, N, device)
assert (out - target).abs().max().item() < 5e-3
print("sampling (model oracle) OK")
print("diffusion OK")
Output yang diharapkan
Sel 15: empat baris schedule OK (nilai alpha_bar[-1] sama seperti uji diffusion.py tadi), lalu T terlalu kecil ditolak OK.
Sel 16: forward process OK dengan MSE sekitar ['0.0001', '0.5645', '1.4570', '2.0021']. Seed di-reset di Sel 15, jadi angkanya seharusnya hampir sama seperti sebelumnya.
Sel 17: satu baris lima gambar. Kotak putih jelas di t=0, makin kabur di tengah, dan tinggal bintik noise di t=999.
Sel 18-21: bentuk tertutup = langkah bertahap OK, sample_timesteps OK, sampling (model tiruan) OK, sampling (model oracle) OK, dan terakhir diffusion OK.
Catatan
Jalankan berurutan: Sel 15 mengisi device dan C, Sel 16 mengisi d, x0, dan noise, lalu Sel 17-21 memakainya. N dari Sel 20 dipakai Sel 21.
Sel 20 dan 21 menjalankan 1000 langkah sampling, jadi mungkin butuh beberapa detik di M3.
Sel 17 meng-override variabel t dan xt dari Sel 16 dan ts dari Sel 19 meng-override ts dari Sel 17. Itu tidak mengganggu karena tiap sel mengisi ulang yang dipakainya.
Kalau Sel 15-21 lolos, bagian config, utils, dan diffusion di ketua.ipynb selesai (21 sel). Sisanya tinggal bagian model (U-Net) dari chat lain, yang nanti disisipkan antara utils dan diffusion. Sebelum commit, jalankan Clear All Outputs dan isi docs/logs/log_ketua.md untuk sesi ini.

1793351245872_image.png
1793351264202_image.png
1793351285800_image.png
1793351314775_image.png
1793351330474_image.png
1793351350640_image.png
1793351366707_image.png
untuk output seperti ini, berhasil

Listing the remaining steps before committing
Semua uji lolos, dan hasilnya cocok dengan yang diharapkan.

Schedule (Sel 15): nilai alpha_bar[-1] sama persis dengan uji diffusion.py tadi (2.04e-05 sampai 4.18e-05), dan T=10 ditolak.
Forward process (Sel 16): MSE-nya 0.0001 → 0.5645 → 1.4570 → 2.0021, juga sama persis, jadi seed-nya konsisten.
Visualisasi (Sel 17): kotak putih jelas di t=0, masih samar terlihat di t=250, dan di t=999 sudah tidak terbaca (noise murni). Ini gambaran yang pas untuk dijelaskan saat presentasi bahwa noise ditambahkan bertahap.
Sel 18-21: bentuk tertutup, sample_timesteps, model tiruan, dan model oracle semuanya OK, dan diffusion OK muncul di akhir.
Bagian config, utils, dan diffusion di ketua.ipynb (21 sel) sudah selesai dan teruji di MPS.

Yang masih tersisa untukmu:

Clear All Outputs sebelum commit ketua.ipynb, sesuai aturan PRD.
Log sesi di docs/logs/log_ketua.md: tiga target modul (config, utils, diffusion) dan konversi ke notebook, plus ekspor chat ke docs/chat_exports/.
Bagian model (U-Net) dari chat lain nanti disisipkan antara utils (Sel 11) dan diffusion (Sel 12). Satu uji yang masih tertunda adalah Diffusion.sample dengan U-Net asli yang belum dilatih, karena PRD memintanya di uji mandiri Ketua. Uji itu bisa ditambahkan setelah UNet jadi.
Uji di CUDA (laptop GTX 1650 Ti) baru terjadi saat Restart and Run All pada MiniDDPM.ipynb final. Semua sel memakai get_device(), jadi seharusnya langsung jalan.
Kalau sesi model.py di chat lain sudah selesai dan kamu butuh bantuan menyisipkannya ke notebook atau merakit MiniDDPM.ipynb, kabari saja.

haloo

Menguji backward dan gradien seluruh parameter
Kelompok 1 (Sel 1-9)
Sel 1 (markdown)

markdown
## Model (Ketua)
Di bagian ini kita bikin otak DDPM-nya: timestep embedding, blok dasar, dan U-Net yang menebak noise di gambar.
Sel 2 (kode)

python
def _group_norm(channels):
    # Jumlah grup terbesar dari (8, 4, 2, 1) yang habis membagi jumlah channel
    for groups in (8, 4, 2, 1):
        if channels % groups == 0:
            return nn.GroupNorm(groups, channels)
Sel 3 (markdown)

markdown
Angka `t` mentah susah dipakai jaringan, jadi diubah jadi vektor berisi gelombang sin dan cos dengan frekuensi berbeda-beda, mirip jarum jam, menit, dan detik yang bareng-bareng menunjuk satu waktu. Model perlu tahu `t` karena kerjanya beda: di `t` kecil cuma merapikan detail, di `t` besar harus menebak bentuk digit dari noise.
Sel 4 (kode)

python
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
Sel 5 (markdown)

markdown
`ResBlock` itu dua konvolusi 3x3 yang di tengahnya ditambah embedding waktu, supaya tiap blok tahu lagi di `t` berapa. Inputnya juga dijumlahkan ke keluaran (jalan pintas residual) biar training lebih stabil.
Sel 6 (kode)

python
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
Sel 7 (markdown)

markdown
`Downsample` memperkecil gambar jadi setengahnya (28 → 14 → 7) pakai konvolusi stride 2. `Upsample` kebalikannya: ukuran gambar digandakan (7 → 14 → 28), lalu dihaluskan dengan satu konvolusi.
Sel 8 (kode)

python
class Downsample(nn.Module):
    def __init__(self, ch):
        super().__init__()
        self.conv = nn.Conv2d(ch, ch, 3, stride=2, padding=1)  # 28->14, 14->7

    def forward(self, x):
        return self.conv(x)
Sel 9 (kode)

python
class Upsample(nn.Module):
    def __init__(self, ch):
        super().__init__()
        self.up = nn.Upsample(scale_factor=2, mode="nearest")  # 7->14, 14->28
        self.conv = nn.Conv2d(ch, ch, 3, padding=1)

    def forward(self, x):
        return self.conv(self.up(x))
Kelompok 2 (Sel 10-15)
Sel 10 (markdown)

markdown
`UNet` punya jalur turun (28 → 14 → 7), satu bagian tengah di 7x7, lalu jalur naik (7 → 14 → 28). Hasil tiap level di jalur turun disimpan, lalu ditempel (skip connection) ke level naik yang ukurannya sama, supaya detail halus yang hilang waktu diperkecil tetap kebawa. Keluarannya prediksi noise berukuran sama dengan input, yaitu (B, 1, 28, 28).
Sel 11 (kode)

python
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
        self.down_blocks = nn.ModuleList(
            [ResBlock(chs[max(i - 1, 0)], chs[i], time_emb_dim) for i in range(n)]
        )
        self.downsamples = nn.ModuleList([Downsample(chs[i]) for i in range(n - 1)])
        self.mid1 = ResBlock(chs[-1], chs[-1], time_emb_dim)
        self.mid2 = ResBlock(chs[-1], chs[-1], time_emb_dim)

        # Jalur naik dari level terdalam: input = hasil level bawah + skip
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
            h = torch.cat([h, skips.pop()], dim=1)  # skip dari level seukuran
            h = block(h, t_emb)
            if k < len(self.upsamples):
                h = self.upsamples[k](h)
        return self.out_conv(self.act(self.out_norm(h)))
Sel 12 (markdown)

markdown
Tiga hal yang dicek: shape keluaran harus sama dengan input, `t` yang beda harus ngasih keluaran yang beda, dan satu langkah backward harus jalan buat semua parameter.
Sel 13 (kode)

python
set_seed(config.SEED)
device = get_device()
model = UNet(**config.MODEL_PARAMS).to(device)

n_params = sum(p.numel() for p in model.parameters())
print(f"device: {device} | jumlah parameter: {n_params:,}")

B, C, S = 4, config.MODEL_PARAMS["in_channels"], config.IMAGE_SIZE
x = torch.randn(B, C, S, S, device=device)
t = torch.randint(0, config.T, (B,), device=device)  # long, 0..T-1
out = model(x, t)
assert out.shape == x.shape, f"shape salah: {tuple(out.shape)}"
assert torch.isfinite(out).all()
print(f"shape OK: {tuple(x.shape)} -> {tuple(out.shape)}")
Sel 14 (kode)

python
with torch.no_grad():
    o0 = model(x, torch.zeros(B, dtype=torch.long, device=device))
    o1 = model(x, torch.full((B,), config.T - 1, dtype=torch.long, device=device))
assert (o0 - o1).abs().max().item() > 0
print("pengaruh t OK")
Sel 15 (kode)

python
loss = nn.functional.mse_loss(model(x, t), torch.randn_like(x))
loss.backward()
missing = [n for n, p in model.named_parameters() if p.grad is None]
assert not missing, f"tanpa gradien: {missing}"
assert all(torch.isfinite(p.grad).all() for p in model.parameters())
print(f"backward OK, loss={loss.item():.4f}")
print("model OK")
Catatan
Belum dijalankan. PyTorch tidak bisa dipasang di lingkungan saya, jadi logikanya hanya saya telusuri manual. Jalankan Sel 13-15 sebagai uji pertama.
Perubahan dari model.py. Tidak ada perubahan logika. Selain import dan __main__ yang dihapus, saya menghapus beberapa baris kosong dan komentar di UNet supaya sekitar 50 baris. Teks print terakhir diubah dari "model.py OK" menjadi "model OK".
Variabel global. Sel uji meninggalkan variabel model, x, t, loss, dan device di notebook. Ini tidak masalah selama sel train milik Teman B mendefinisikan variabelnya sendiri di dalam fungsi.
Log. Sesi ini bisa dicatat di docs/logs/log_ketua.md dengan target modul “Model (timestep embedding, ResBlock, U-Net)”.
1793352846700_image.png
okee aman sampe cell terakhir

Memeriksa keluaran dan kehilangan model.
Memeriksa keluaran dan kehilangan model.
Mantap, sel uji terakhir lolos. Loss 1,1063 untuk output acak melawan noise acak memang wajar: dua tensor acak independen menghasilkan MSE sekitar 1, ditambah sedikit karena output model belum dilatih.

Sebelum lanjut, ada beberapa hal yang sebaiknya dilakukan:

Cek juga output Sel 13 (jumlah parameter, shape) dan Sel 14 (pengaruh t). Kalau semuanya sudah muncul tanpa error, bagian model selesai.
Catat sesi ini di docs/logs/log_ketua.md dengan target modul “Model (timestep embedding, ResBlock, U-Net)”, dan simpan share link chat-nya.
Sebelum commit ketua.ipynb, jalankan Clear All Outputs sesuai PRD.
Berikutnya bagian diffusion (bagian 7). Kalau mau, saya ubah Diffusion jadi sel notebook dengan cara yang sama: daftar sel dulu, tunggu persetujuanmu, baru kodenya.

Dosen meminta seluruh kode kelompok dijadikan satu file .ipynb yang berdiri sendiri. Terlampir PRD notebook dan tiga notebook kerja: azigha_(ketua).ipynb, A.ipynb, dan B.ipynb. Tugasmu merakit ketiganya menjadi satu notebook bernama MiniDDPM.ipynb tanpa mengubah logika kode apa pun.

Pembagian isi tiga notebook itu:
- azigha_(ketua).ipynb berisi bagian 1 Import, 2 Config, 3 Utils, 6 Model, dan 7 Diffusion.
- A.ipynb berisi bagian 4 Dataset dan 5 Visualize.
- B.ipynb berisi bagian 8 Experiments, 9 Train, 10 Sample, 12 Eksekusi baseline, dan 13 Eksperimen dan hasil.

Urutan di notebook final mengikuti nomor bagian di PRD: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13. Tambahkan satu sel markdown judul proyek di paling atas.

Aturan perakitan:
1. Buang semua sel kode yang baris pertamanya "# SALINAN SEMENTARA", karena itu salinan sementara dari bagian milik orang lain.
2. Buang sel markdown judul notebook kerja, yaitu yang diawali "# Notebook kerja".
3. Buang sel import tambahan milik A dan B yang baris pertamanya "# Import Teman". Gabungkan semua import yang dipakai ketiga notebook ke satu sel import utama di bagian 1 tanpa duplikat.
4. Samakan label pemilik di judul bagian menjadi Ketua, Teman A, dan Teman B.
5. Kosongkan output dan nomor eksekusi semua sel.
6. Jangan menambah atau mengubah kode selain yang disebut di aturan 7 dan 8.
7. Kurangi komentar di kode supaya sel tidak penuh. Hapus komentar yang hanya mengulang apa yang sudah jelas dari barisnya. Pertahankan komentar yang menjelaskan hal yang tidak jelas dari kodenya, dengan batas sekitar satu sampai dua komentar per sel. Docstring yang lebih dari satu baris dipendekkan menjadi satu baris. Hanya teks komentar dan docstring yang boleh berubah, baris kode tidak boleh disentuh. Gunakan modul tokenize supaya tanda # di dalam string tidak ikut terhapus. Skrip harus membuktikan kodenya sama dengan membandingkan ast.dump sebelum dan sesudah (docstring diabaikan pada perbandingan), lalu mencetak jumlah sel yang strukturnya berubah. Angkanya harus 0.
8. Sel markdown harus pendek, maksimal tiga kalimat pendek. Jangan memakai tanda titik koma dan jangan memakai tanda pisah panjang seperti em dash atau en dash. Jangan mengubah sel markdown diam-diam. Untuk sel markdown yang perlu diubah, tampilkan teks sebelum dan sesudahnya di Tahap 2 supaya saya setujui dulu.

Kerjakan dalam tiga tahap. Berhenti di akhir tiap tahap dan tunggu saya setujui sebelum lanjut. Jangan membuat file.

Tahap 1, pemahaman. Jangan menulis kode dan jangan membuat tabel. Jelaskan dengan kalimat biasa di chat apa yang kamu pahami dari tugas ini: apa tujuan perakitannya, apa isi tiap notebook dan bagian mana yang masuk ke notebook final, sel apa saja yang dibuang dan berapa jumlahnya di A.ipynb dan di B.ipynb, apa yang dikurangi di komentar kode dan sel markdown, apa yang sengaja tidak diubah, dan hal yang kamu ragukan atau butuh saya konfirmasi. Setelah itu berhenti.

Tahap 2, daftar sel. Setelah saya setujui pemahamanmu, tampilkan daftar lengkap sel notebook final dalam bentuk tabel berurutan dengan kolom nomor sel, jenis (markdown atau kode), judul atau baris pertama sel, dan asal notebook (ketua, A, atau B). Semua sel markdown dari tiga notebook tetap dipertahankan di tempatnya. Satu-satunya sel baru adalah sel markdown judul proyek di paling atas dan sel import gabungan. Sebutkan total sel di bawah tabel. Tampilkan juga teks sebelum dan sesudah untuk tiap sel markdown yang perlu diubah menurut aturan 8. Setelah itu berhenti.

Tahap 3, skrip. Setelah saya setujui daftar sel, tampilkan satu skrip Python pendek memakai nbformat langsung di chat sebagai blok kode. Skrip itu membaca tiga notebook dan menulis MiniDDPM.ipynb di folder root repo. Letakkan path tiga file input sebagai variabel di bagian paling atas skrip, dengan nilai awal notebooks/azigha_(ketua).ipynb, notebooks/A.ipynb, dan notebooks/B.ipynb. Cari awal tiap bagian lewat judul markdown seperti "## 4." dan "## 8.", jangan lewat nomor sel. Setelah skrip, jelaskan singkat cara menjalankannya dari terminal.

Ran 4 commands
Tahap 2: daftar sel

Sebelum tabel, satu koreksi untuk Tahap 1. Aku menyebut sel markdown Config punya empat kalimat. Setelah kuperiksa ulang, ternyata hitungannya ikut menghitung “2.” di judul. Isinya hanya tiga kalimat, jadi Config tidak perlu diubah. Dari seluruh markdown yang masuk, hanya sel judul bagian 7 yang melanggar aturan 8 (ada titik koma).

Aku juga mengecek semua sel yang masuk memakai analisis nama (pyflakes). Setelah sel uji dibuang, hanya dua sel yang rusak, persis seperti perkiraanmu: contoh gambar di Dataset dan visualisasi forward process di Diffusion.

No	Jenis	Judul atau baris pertama	Asal
0	markdown	# Mini DDPM pada MNIST (judul proyek)	baru
1	markdown	## 1. Import library (Ketua)	ketua
2	kode	import gabungan (baris pertama import math)	baru
3	markdown	## 2. Config (Ketua)	ketua
4	kode	# Root repo: folder kerja saat ini, atau folder induknya...	ketua
5	kode	config = SimpleNamespace(	ketua
6	kode	# Sampling selama training	ketua
7	markdown	## 3. Utils (Ketua)	ketua
8	kode	def set_seed(seed):	ketua
9	kode	def get_device():	ketua
10	markdown	## 4. Dataset (Syaikha A), label akan jadi Teman A	A
11	kode	class ImagesOnly(Dataset):	A
12	markdown	get_dataloader membaca semua pengaturan dari argumen cfg...	A
13	kode	def get_dataloader(cfg):	A
14	kode	# Contoh gambar dari satu batch (berubah, lihat di bawah)	A
15	markdown	## 5. Visualize (Teman A)	A
16	markdown	Gambar dari model ada di rentang [-1, 1], sedangkan file PNG...	A
17	kode	def save_image_grid(images, path):	A
18	markdown	plot_loss menerima dict {label: [loss per epoch]}...	A
19	kode	def plot_loss(series, path):	A
20	markdown	## 6. Model (Ketua)	ketua
21	kode	def _group_norm(channels):	ketua
22	markdown	Angka t mentah susah dipakai jaringan...	ketua
23	kode	class SinusoidalTimeEmbedding(nn.Module):	ketua
24	markdown	ResBlock itu dua konvolusi 3x3...	ketua
25	kode	class ResBlock(nn.Module):	ketua
26	markdown	Downsample memperkecil gambar jadi setengahnya...	ketua
27	kode	class Downsample(nn.Module):	ketua
28	kode	class Upsample(nn.Module):	ketua
29	markdown	UNet punya jalur turun (28 → 14 → 7)...	ketua
30	kode	class UNet(nn.Module):	ketua
31	markdown	## 7. Diffusion (Ketua)	ketua
32	kode	def _extract(values, t, x):	ketua
33	kode	class Diffusion:	ketua
34	kode	# Visualisasi forward process (berubah, lihat di bawah)	ketua
35	markdown	## 8. Experiments (Teman B)	B
36	kode	EXPERIMENTS = {	B
37	markdown	_resolve_run menggabungkan baseline dengan timpaan eksperimen...	B
38	kode	def _resolve_run(name, smoke=None):	B
39	markdown	## 9. Train (Teman B)	B
40	kode	def _train_one_epoch(model, loader, diffusion, optimizer, device):	B
41	markdown	Checkpoint cuma berisi tensor, angka, dan dict biasa...	B
42	kode	def _save_checkpoint(path, model, optimizer, T, model_params, epoch):	B
43	kode	def _save_loss_record(run, losses, epoch_seconds):	B
44	kode	def _save_training_grid(model, diffusion, run, epoch, device):	B
45	kode	def _log_epoch(run, epoch, loss, train_s, sample_s, elapsed_s):	B
46	kode	def train(name="baseline", smoke=None):	B
47	markdown	## 10. Sample (Teman B)	B
48	kode	def sample(path_checkpoint):	B
49	markdown	## 12. Eksekusi baseline (Teman B)	B
50	kode	path_baseline, losses_baseline = train(“baseline”)	B
51	kode	images_baseline = sample(path_baseline)	B
52	markdown	## 13. Eksperimen dan hasil (Teman B)	B
53	kode	snapshot_13 = copy.deepcopy(vars(config)) # dipakai sel uji...	B
54	kode	def _load_loss_records(names):	B
55	kode	# Grafik perbandingan: tiap kelompok berisi baseline + eksperimen...	B
56	kode	# Grid akhir tiap eksperimen dari checkpoint-nya...	B
57	kode	# Tabel hasil ke results/experiments.md (smoke: experiments_smoke.md)	B
Total: 58 sel (1 judul baru, 1 import gabungan baru, 56 sel dari notebook kerja). Sesuai perkiraanmu. Rinciannya: 24 dari ketua, 10 dari A, 23 dari B, ditambah dua sel baru. Sel uji yang dibuang ada 22 sel kode berisi assert (11 di ketua, 4 di A, 7 di B) dan 2 sel markdown (“Tiga hal yang dicek” dan “Sel uji ini gantinya”).

Sel markdown yang berubah

Judul bagian 4 (label pemilik, aturan 4 dan 3). Isi lainnya sama.
Sebelum: ## 4. Dataset (Syaikha A) lalu “MNIST diunduh otomatis ke data/, lalu tiap gambar diubah ke rentang [-1, 1] supaya sama dengan skala noise Gaussian yang dipakai diffusion. Model kita unconditional (nggak dikasih tahu digit berapa), jadi labelnya dibuang di sini dan tiap batch cuma berisi gambar.”
Sesudah: ## 4. Dataset (Teman A) dan paragraf di bawahnya sama persis.
Judul bagian 7 (titik koma, aturan 8). Perubahannya hanya ; jadi , lalu, jadi tetap tiga kalimat.
Sebelum: “...supaya langkah terakhir tetap noise murni; sampling lalu membalik prosesnya dari noise murni, langkah T-1 sampai 0.”
Sesudah: “...supaya langkah terakhir tetap noise murni, lalu sampling membalik prosesnya dari noise murni, langkah T-1 sampai 0.”
Kalimat sebelumnya di sel itu tidak berubah.
Sel judul proyek baru (sel 0):
   # Mini DDPM pada MNIST
   Model difusi Mini DDPM yang dibangun dari nol dengan PyTorch dan dilatih pada MNIST 28x28. Notebook ini berdiri sendiri dan menghasilkan digit tulisan tangan dari noise murni.
Sel markdown lain tidak diubah, termasuk Config yang memuat kalimat GTX 1650 Ti.

Dua sel yang berdiri sendiri (dicatat terpisah dari pengecekan ast.dump). Baris baru kutaruh tepat setelah komentar pembuka, baris lainnya tidak disentuh.

Sel 14, Contoh gambar dari satu batch.
Sebelum:

python
# Contoh gambar dari satu batch (dikembalikan ke [0, 1] hanya untuk ditampilkan)
fig, axes = plt.subplots(1, 8, figsize=(12, 1.8))
for ax, img in zip(axes, batch[:8]):
    ax.imshow(((img[0] + 1) / 2).numpy(), cmap="gray", vmin=0, vmax=1)
    ax.axis("off")
plt.show()
print("dataset OK")
Sesudah (tiga baris baru, memakai pola sel uji aslinya: mode penuh):

python
# Contoh gambar dari satu batch (dikembalikan ke [0, 1] hanya untuk ditampilkan)
cfg_full = SimpleNamespace(**copy.deepcopy(vars(config)))
cfg_full.SMOKE_TEST = False
batch = next(iter(get_dataloader(cfg_full)))
fig, axes = plt.subplots(1, 8, figsize=(12, 1.8))
... (baris lain sama persis)
Sel 34, Visualisasi forward process.
Sebelum:

python
# Visualisasi forward process: makin besar t, makin berisik
ts = [0, d.T // 4, d.T // 2, 3 * d.T // 4, d.T - 1]
fig, axes = plt.subplots(1, len(ts), figsize=(2.2 * len(ts), 2.6))
for ax, t_val in zip(axes, ts):
    t = torch.full((1,), t_val, device=device, dtype=torch.long)
    xt = d.add_noise(x0[:1], t, noise[:1])
    ax.imshow(xt[0, 0].cpu().numpy(), cmap="gray", vmin=-1, vmax=1)
    ax.set_title(f"t={t_val}")
    ax.axis("off")
plt.show()
Sesudah (enam baris baru, dari sel uji aslinya tanpa assert; C kuganti config.MODEL_PARAMS["in_channels"] supaya tidak perlu variabel tambahan):

python
# Visualisasi forward process: makin besar t, makin berisik
set_seed(config.SEED)
device = get_device()
d = Diffusion(config.T, device)
x0 = torch.full((8, config.MODEL_PARAMS["in_channels"], config.IMAGE_SIZE, config.IMAGE_SIZE), -1.0, device=device)
x0[:, :, 8:20, 8:20] = 1.0
noise = torch.randn_like(x0)
ts = [0, d.T // 4, ...
... (baris lain sama persis)
set_seed kutambahkan supaya gambarnya konsisten antar-run, seperti sel uji aslinya. Kalau tidak mau, tinggal bilang.

Yang butuh keputusanmu

import tempfile dari A.ipynb hanya dipakai sel uji yang dibuang, jadi di notebook final tidak terpakai lagi. Usulku tidak dimasukkan ke import gabungan. Jadi import gabungan berisi math, random, copy, json, time, Path, SimpleNamespace, plt, np, torch, nn, DataLoader, Dataset, Subset, datasets, transforms, make_grid. Setuju?
Sel 53 (snapshot_13 = copy.deepcopy(vars(config))) variabelnya hanya dipakai sel uji bagian 13 yang dibuang, dan komentarnya menyebut “sel uji di akhir bagian ini”. Barisnya kubiarkan karena kode tidak boleh disentuh. Usulku komentar itu dihapus lewat aturan 7 karena sudah menyesatkan. Setuju, atau komentarnya dibiarkan?
Aku berhenti di sini dan menunggu persetujuanmu sebelum ke Tahap 3.

Tahap 2 saya setujui dengan jawaban berikut.
1. import tempfile tidak dimasukkan ke import gabungan. Setuju.
2. Di sel snapshot_13, hapus komentar yang menyebut sel uji lewat aturan 7. Barisnya tetap.
3. set_seed di sel visualisasi forward process tetap dipakai.

Koreksi kecil: rincian jumlah sel di jawabanmu keliru. Yang benar sesuai tabel adalah 23 dari ketua, 10 dari A, 23 dari B, dan 2 sel baru, total 58.

Lanjut ke Tahap 3, yaitu satu skrip Python pendek memakai nbformat, sesuai yang sudah saya tulis di prompt awal. Tambahan untuk skrip. Pakai tanda kutip lurus biasa di semua kode, jangan tanda kutip melengkung. Skrip hanya menulis MiniDDPM.ipynb dan tidak boleh mengubah tiga notebook input. Di akhir, skrip mencetak total sel (harus 58), urutan judul bagian, jumlah sel berisi assert (harus 0), dan jumlah sel yang strukturnya berubah di luar dua sel yang sengaja berubah (harus 0). Setelah skrip, jelaskan singkat cara menjalankannya dari terminal.
Tambahan untuk Tahap 3: jangan membuat file, artifact, atau notebook yang harus diunduh, termasuk file skrip. Tampilkan seluruh skrip langsung di chat sebagai satu blok kode python, lengkap dari baris import sampai baris terakhir, supaya saya salin sendiri ke file rakit.py. Jangan memotong skrip dengan komentar seperti "sisanya sama". Setelah blok kode, jelaskan singkat cara menjalankannya dari terminal.

Ran 4 commands
Terima kasih atas koreksinya. Rincian yang benar memang 23 dari ketua (sel import kode Ketua digantikan sel import gabungan), 10 dari A, 23 dari B, dan 2 sel baru, total 58.

Skrip di bawah sudah kujalankan di sandbox pada salinan ketiga notebook. Hasil uji ditulis ke folder sementara dan sudah kuhapus, jadi tidak ada file yang kuserahkan. Outputnya sesuai target: 58 sel, 0 sel berisi assert, 0 sel berubah struktur di luar dua sel sengaja, dan kode asli kedua sel itu utuh di bawah baris baru. Hasilnya juga lolos validasi nbformat dan bersih dari output, nomor eksekusi, kata “Syaikha”, label “SALINAN”, serta tanda kutip melengkung.

python
# Path input (relatif terhadap folder skrip ini, yaitu root repo)
KETUA_PATH = "notebooks/azigha_(ketua).ipynb"
A_PATH = "notebooks/A.ipynb"
B_PATH = "notebooks/B.ipynb"
OUT_PATH = "MiniDDPM.ipynb"

import ast
import io
import re
import sys
import tokenize
from pathlib import Path

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

ROOT = Path(__file__).resolve().parent
PLAN = [(1, "K"), (2, "K"), (3, "K"), (4, "A"), (5, "A"), (6, "K"), (7, "K"),
        (8, "B"), (9, "B"), (10, "B"), (12, "B"), (13, "B")]
EXCLUDE_IMPORTS = {"tempfile"}  # hanya dipakai sel uji yang dibuang
TITLE = ("# Mini DDPM pada MNIST\n"
         "Model difusi Mini DDPM yang dibangun dari nol dengan PyTorch dan dilatih pada MNIST 28x28. "
         "Notebook ini berdiri sendiri dan menghasilkan digit tulisan tangan dari noise murni.")
MD_FIXES = [
    ("## 4. Dataset (Syaikha A)", "## 4. Dataset (Teman A)"),
    ("tetap noise murni; sampling lalu membalik", "tetap noise murni, lalu sampling membalik"),
]
# Dua sel yang sengaja berubah: baris ini disisipkan tepat setelah komentar pembuka sel
PATCHES = {
    "# Contoh gambar dari satu batch": [
        "cfg_full = SimpleNamespace(**copy.deepcopy(vars(config)))",
        "cfg_full.SMOKE_TEST = False",
        "batch = next(iter(get_dataloader(cfg_full)))",
    ],
    "# Visualisasi forward process": [
        "set_seed(config.SEED)",
        "device = get_device()",
        "d = Diffusion(config.T, device)",
        'x0 = torch.full((8, config.MODEL_PARAMS["in_channels"], config.IMAGE_SIZE, config.IMAGE_SIZE), -1.0, device=device)',
        "x0[:, :, 8:20, 8:20] = 1.0",
        "noise = torch.randn_like(x0)",
    ],
}
# Komentar yang dipertahankan (cocok sebagian teks). Komentar lain dihapus.
# Baris komentar berurutan dihitung satu blok dan dipertahankan utuh.
KEEP = (
    "Root repo:", "SEMENTARA, BELUM FINAL", "Acuan untuk T=1000", "interval grid smoke test",
    "Path: semuanya diturunkan", "sekaligus menyemai", "Jumlah grup terbesar",
    "Frekuensi turun geometris", "Jalan pintas residual", "(B,C) -> (B,C,1,1)",
    "Jalur naik dari level terdalam", "Beta diskalakan", "Reverse process; mode eval/train",
    "label dibuang di sini", "piksel 0..255", "(x - 0.5) / 0.5", "grid sepersegi",
    "semua nilai dari config", "salinan; config asli", "tiap batch: satu tensor",
    "tetap di device", "waktu training per epoch", "sudah tanpa gradien",
    "inisialisasi dan urutan data", "checkpoint berkala", "T dari checkpoint", "noise awal sama",
    "Baseline sudah dilatih", "Visualisasi forward process", "Contoh gambar dari satu batch",
    "Grafik perbandingan", "Grid akhir tiap", "Tabel hasil ke",
)
HEAD = re.compile(r"^## (\d+)\.")


def section(cells, n):
    """Sel dari judul '## n.' sampai sebelum judul bagian berikutnya."""
    is_head = lambda c: c.cell_type == "markdown" and HEAD.match(c.source)
    start = next(i for i, c in enumerate(cells) if is_head(c) and int(HEAD.match(c.source).group(1)) == n)
    end = next((i for i in range(start + 1, len(cells)) if is_head(cells[i])), len(cells))
    return cells[start:end]


def is_dropped(c):
    s = c.source
    if c.cell_type == "markdown":
        return s.startswith(("# Notebook kerja", "Sel uji ini gantinya", "Tiga hal yang dicek"))
    if s.startswith(("# SALINAN SEMENTARA", "# Import Teman")):
        return True
    return any(isinstance(x, ast.Assert) for x in ast.walk(ast.parse(s)))


def merge_imports(sources):
    plain, froms = set(), {}
    for src in sources:
        for node in ast.parse(src).body:
            if isinstance(node, ast.Import):
                plain.update((a.name, a.asname) for a in node.names if a.name not in EXCLUDE_IMPORTS)
            elif isinstance(node, ast.ImportFrom) and node.module not in EXCLUDE_IMPORTS:
                froms.setdefault(node.module, set()).update((a.name, a.asname) for a in node.names)
    fmt = lambda name, asn: name + (f" as {asn}" if asn else "")
    groups = {True: [], False: []}
    for name, asn in sorted(plain):
        groups[name.split(".")[0] in sys.stdlib_module_names].append("import " + fmt(name, asn))
    for mod, names in sorted(froms.items()):
        line = f"from {mod} import " + ", ".join(fmt(n, a) for n, a in sorted(names))
        groups[mod.split(".")[0] in sys.stdlib_module_names].append(line)
    return "\n".join(groups[True]) + "\n\n" + "\n".join(groups[False])


def prune(code):
    """Hapus komentar yang tidak ada di KEEP dan pendekkan docstring multibaris. Kode tidak disentuh."""
    lines = code.split("\n")
    for n in ast.walk(ast.parse(code)):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            d = n.body[0]
            if (isinstance(d, ast.Expr) and isinstance(d.value, ast.Constant)
                    and isinstance(d.value.value, str) and d.end_lineno > d.lineno):
                first = d.value.value.strip().split("\n")[0].strip()
                lines[d.lineno - 1] = " " * d.col_offset + '"""' + first + '"""'
                for r in range(d.lineno, d.end_lineno):
                    lines[r] = None
    items = [(t.start[0], t.start[1], t.string, not t.line[:t.start[1]].strip())
             for t in tokenize.generate_tokens(io.StringIO(code).readline) if t.type == tokenize.COMMENT]
    blocks = []
    for it in items:
        if blocks and it[3] and blocks[-1][-1][3] and blocks[-1][-1][0] == it[0] - 1:
            blocks[-1].append(it)
        else:
            blocks.append([it])
    for blk in blocks:
        if any(k in text for _, _, text, _ in blk for k in KEEP):
            continue
        for row, col, _, standalone in blk:
            lines[row - 1] = None if standalone else lines[row - 1][:col].rstrip()
    return "\n".join(l for l in lines if l is not None)


def norm(code, skip=0):
    """ast.dump tiap statement, docstring diabaikan. skip = jumlah statement awal yang dilewati."""
    tree = ast.parse(code)
    for n in ast.walk(tree):
        if isinstance(n, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            b = n.body
            if b and isinstance(b[0], ast.Expr) and isinstance(b[0].value, ast.Constant) \
                    and isinstance(b[0].value.value, str):
                n.body = b[1:] or [ast.Pass()]
    return [ast.dump(n) for n in tree.body[skip:]]


nbs = {k: nbformat.read(ROOT / p, as_version=4) for k, p in (("K", KETUA_PATH), ("A", A_PATH), ("B", B_PATH))}
import_srcs = [c.source for c in section(nbs["K"].cells, 1) if c.cell_type == "code"]
import_srcs += [c.source for k in "AB" for c in nbs[k].cells
                 if c.cell_type == "code" and c.source.startswith("# Import Teman")]

cells, pairs, patched = [new_markdown_cell(TITLE)], [], []
fix_hits = [0] * len(MD_FIXES)
for n, k in PLAN:
    for c in section(nbs[k].cells, n):
        if is_dropped(c):
            continue
        if c.cell_type == "markdown":
            text = c.source
            for i, (old, new) in enumerate(MD_FIXES):
                if old in text:
                    text, fix_hits[i] = text.replace(old, new), fix_hits[i] + 1
            cells.append(new_markdown_cell(text))
        elif n == 1:
            cells.append(new_code_cell(merge_imports(import_srcs)))
        else:
            final = prune(c.source)
            key = next((p for p in PATCHES if c.source.startswith(p)), None)
            if key:
                head, *rest = final.split("\n")
                final = "\n".join([head] + PATCHES[key] + rest)
                patched.append((c.source, final, len(ast.parse("\n".join(PATCHES[key])).body)))
            else:
                pairs.append((c.source, final))
            cells.append(new_code_cell(final))
assert fix_hits == [1] * len(MD_FIXES), f"perbaikan markdown tidak tepat satu kali: {fix_hits}"

nb = new_notebook(cells=cells, metadata=dict(nbs["K"].metadata))  # metadata notebook Ketua
nbformat.validate(nb)
nbformat.write(nb, ROOT / OUT_PATH)

code_cells = [c for c in nb.cells if c.cell_type == "code"]
n_assert = sum(any(isinstance(x, ast.Assert) for x in ast.walk(ast.parse(c.source))) for c in code_cells)
changed = sum(norm(a) != norm(b) for a, b in pairs)
patched_ok = all(norm(a) == norm(b, k) for a, b, k in patched)
print("Ditulis ke:", ROOT / OUT_PATH)
print("Total sel:", len(nb.cells), "(harus 58)")
print("Urutan judul:")
for c in nb.cells:
    if c.cell_type == "markdown" and c.source.startswith(("# ", "## ")):
        print("  ", c.source.split("\n")[0])
print("Sel berisi assert:", n_assert, "(harus 0)")
print("Sel berubah struktur di luar dua sel sengaja:", changed, "(harus 0)")
print("Sel sengaja berubah:", len(patched), "| kode aslinya utuh di bawah baris baru:", patched_ok)
Cara menjalankan

Simpan skrip di atas sebagai rakit.py di root repo, sejajar dengan folder notebooks/.
Pastikan Python 3.10 atau lebih baru dan nbformat terpasang: pip install nbformat.
Jalankan dari terminal: python rakit.py.
Skrip hanya membaca tiga notebook di notebooks/ dan menulis MiniDDPM.ipynb di root, lewat path relatif terhadap lokasi rakit.py. Output terminal harus menunjukkan 58 sel, 0 sel assert, dan 0 sel berubah struktur.

Hal yang perlu kamu tahu

Komentar yang dipertahankan ditentukan daftar KEEP di atas skrip, yang kupilih manual dari 72 komentar di sel yang masuk. Sisanya 34 baris komentar. Kalau ada komentar yang mau kamu ganti, cukup edit daftar itu.
Sel config (bagian 2) berisi dua blok komentar, yaitu blok GTX 1650 Ti dua baris yang tetap utuh sesuai permintaanmu dan satu komentar acuan T=1000. Jadi sel itu tiga baris komentar, sedikit di atas batas dua.
Docstring dua baris di get_dataloader dan train dipendekkan dengan mengambil baris pertamanya. Docstring lain yang sudah satu baris tidak disentuh.
Komentar “dipakai sel uji di akhir bagian ini” di sel snapshot_13 sudah terhapus dan barisnya tetap. Variabel snapshot_13 sekarang tidak terpakai di mana pun, tapi kubiarkan karena kode tidak boleh diubah.