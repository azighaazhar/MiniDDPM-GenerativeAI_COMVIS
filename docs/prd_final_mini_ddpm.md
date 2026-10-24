# PRD Final: Mini DDPM pada MNIST

**Cara pakai:** Tempel bagian umum + jobdesk milikmu ke AI-mu. Bagian orang lain boleh dibaca, tapi tidak perlu ditempel.

Label: **[PDF]** = dari panduan dosen, **[Keputusan]** = disepakati kelompok, **[Asumsi]** = usulan teknis yang dipakai sampai ada keputusan lain.

Urutan ketergantungan: data dan model dikerjakan paralel, training dilakukan setelah keduanya jadi.

---

# BAGIAN UMUM (semua anggota)

## 1. Tujuan
Membangun model difusi Mini DDPM dari nol, dilatih pada MNIST 28x28 (1 channel), menggunakan Python dan PyTorch. Model menghasilkan digit tulisan tangan dari noise murni. Seluruh kode dibuat lewat kolaborasi dengan LLM (vibe coding) **[PDF]**.

## 2. Aturan proyek
- Dilarang menyalin kode dari GitHub atau blog tutorial **[PDF]**.
- Boleh memakai layer dasar `torch.nn` **[Keputusan]**.
- Dilarang memakai library difusi jadi (misalnya `diffusers`) dan bobot pretrained **[Asumsi]**.
- U-Net, noise schedule, dan timestep embedding disusun sendiri **[Keputusan]**.
- Tidak ada conditional generation, classifier evaluasi, atau fine-tuning dalam arti melanjutkan model pretrained **[Keputusan]**.

## 3. Keputusan teknis
- Model: Mini DDPM. Dataset: MNIST 28x28 **[Keputusan]**.
- U-Net maksimal dua level downsampling: 28 → 14 → 7 **[Keputusan]**.
- Normalisasi data ke [-1, 1] **[Asumsi]**. Timestep embedding sinusoidal **[Asumsi]**. Loss MSE antara noise asli dan noise prediksi **[Asumsi]**.
- Dua variabel tuning: **learning rate** dan **jumlah timestep T**. Batch size dikunci; nilainya dan jumlah epoch ditentukan setelah uji memori dan disimpan di `config.py` **[Keputusan]**.
- `config.py` hanya berisi nilai baseline. `experiments.py` (milik Teman B) berisi daftar konfigurasi eksperimen bernama yang menimpa learning rate dan T. `train.py` memilih konfigurasi berdasarkan nama **[Keputusan]**.
- DataLoader hanya mengembalikan gambar (tanpa label). `dataset.py` memakai `download=True` **[Keputusan]**.
- Checkpoint berisi: bobot model, T, parameter pembentuk model, epoch, dan optimizer. Dengan isi ini `sample.py` dapat membangun ulang model dengan benar **[Keputusan]**.
- `train.py` menyimpan grid gambar sampel setiap N epoch; N diatur di `config.py` **[Keputusan]**.
- Checkpoint tidak di-commit. Grafik loss dan gambar sampel di-commit **[Keputusan]**.
- Satu seed dan satu `config.py` dipakai semua anggota **[Keputusan]**.

## 4. Device dan versi Python
- `utils.py` memilih device berurutan: cuda, lalu mps, lalu cpu. Tidak ada device tetap di kode; semua file memakai hasil fungsi itu **[Keputusan]**.
- Versi Python: **3.14** (ketua memakai 3.14.6). Semua anggota memakai versi yang sama. Dicatat di README dan sebagai baris komentar di `requirements.txt`: `WAJIB: Python 3.14, lihat README` **[Keputusan]**.

## 5. Kontrak data antar-modul

| Antarmuka | Bentuk |
|---|---|
| Batch dari DataLoader | satu tensor float (B, 1, 28, 28), nilai dalam [-1, 1] |
| Timestep `t` | tensor bilangan bulat (B,), nilai 0 sampai T-1 |
| Input model | gambar ber-noise (B, 1, 28, 28) dan `t` (B,) |
| Output model | prediksi noise, shape (B, 1, 28, 28) |
| Hasil sampling | tensor (N, 1, 28, 28), nilai dalam [-1, 1] |

Nilai parameter dibaca dari `config.py` (baseline) dan, untuk learning rate dan T, dari konfigurasi eksperimen yang dipilih. Tidak ada angka tetap di file lain.

## 6. Struktur folder dan pemilik file (satu file satu pemilik) **[Keputusan]**

```
mini-ddpm-mnist/
├── README.md              (Ketua)   versi Python, cara instal dan menjalankan
├── requirements.txt       (Ketua)   versi PyTorch dan library pendukung
├── .gitignore             (Ketua)   abaikan data/ dan checkpoints/
├── config.py              (Ketua)   nilai baseline
├── model.py               (Ketua)
├── diffusion.py           (Ketua)
├── utils.py               (Ketua)
├── experiments.py         (Teman B)
├── train.py               (Teman B)
├── sample.py              (Teman B)
├── dataset.py             (Teman A)
├── visualize.py           (Teman A)
├── scripts/
│   └── check_data.py      (Teman A)
├── data/                  (tidak di-commit) unduhan MNIST
├── checkpoints/           (tidak di-commit)
├── results/               (di-commit)
│   ├── loss_curves/       (Teman B)
│   ├── samples/           (Teman B)
│   └── experiments.md     (Teman B) tabel hasil tuning
└── docs/
    ├── logs/
    │   ├── log_ketua.md   (Ketua)
    │   ├── log_teman_a.md (Teman A)
    │   └── log_teman_b.md (Teman B)
    ├── LOG_INTERAKSI_GABUNGAN.md  (Teman A)
    └── chat_exports/      (tiap anggota untuk chat miliknya)
```

Semua perintah dijalankan dari root repo.

## 7. Aturan kerja
- **Log per anggota [PDF]:** setiap sesi LLM untuk membuat modul baru atau memperbaiki bug dicatat di `docs/logs/log_<nama>.md` pada akhir sesi, memakai templat berikut. Teman A hanya merapikan dan menggabungkan log menjadi `docs/LOG_INTERAKSI_GABUNGAN.md`.

```
LOG INTERAKSI LLM - KELOMPOK [Nama Kelompok]
- Tanggal Sesi: [DD/MM/YYYY]
- Target Modul: [mis. Timestep embedding / Debugging shape U-Net]
- Tautan Sesi Chat: [share link]

KRONOLOGI PROMPT & RESPONS:
1. TAHAP INISIASI (Meminta Kode Awal)
   - Prompt Kelompok: "[prompt spesifik]"
   - Alasan Khusus: [mengapa pendekatan/instruksi ini]
   - Output Model: [ringkasan skrip atau cuplikan kode krusial]

2. TAHAP PENANGANAN EROR / DEBUGGING
   - Pesan Eror dari Notebook: [pesan eror utuh]
   - Prompt Perbaikan ke LLM: "[cara menanyakan solusi]"
   - Analisis & Solusi Kelompok: [bagaimana AI membantu dan pelajaran yang diambil]
```

- **Ekspor chat [PDF]:** setiap sesi punya share link aktif atau ekspor Markdown/PDF di `docs/chat_exports/`.
- **Git [Keputusan]:** tiap anggota commit ke branch sendiri; ketua menggabungkan ke `main`. Setiap anggota hanya mengubah file miliknya.
- **Debugging [Keputusan]:** tiap orang men-debug modulnya sendiri. Error lintas modul ditangani pemilik modul yang menerima input. Penemu error mencatatnya di log miliknya. Salin pesan error utuh, tanyakan ke LLM, analisis solusinya, lalu catat di log **[PDF]**.

---

# JOBDESK KETUA: Model, Diffusion, Config, Utils, Integrasi

Peran **[PDF]**: Prompt Engineer & LLM Navigator (merancang system prompt awal, mengomunikasikan arsitektur ke LLM, menjaga konsistensi logika coding).

**File milik:** `model.py`, `diffusion.py`, `config.py`, `utils.py`, `README.md`, `requirements.txt`, `.gitignore`, `docs/logs/log_ketua.md`.

## Modul

| File | Isi |
|---|---|
| `config.py` | Hanya nilai baseline: seed, batch size, jumlah epoch, learning rate baseline, T baseline, parameter pembentuk model, flag smoke test (subset data kecil, 1-2 epoch), N (interval grid sampel), jumlah gambar sampel, path |
| `diffusion.py` | Noise schedule (beta, alpha, alpha-bar dan turunannya); forward process; fungsi sampling (reverse process). Menerima T sebagai parameter agar T hasil timpaan eksperimen dapat dipakai |
| `model.py` | Timestep embedding sinusoidal; blok dasar U-Net; U-Net lengkap dengan skip connection, dua level downsampling (28 → 14 → 7). Dibangun dari parameter pembentuk model yang diteruskan sebagai argumen |
| `utils.py` | Pengaturan seed; fungsi pemilihan device (cuda, lalu mps, lalu cpu) |
| `README.md` | Python 3.14 (ketua 3.14.6), cara instal dari `requirements.txt`, cara menjalankan |
| `requirements.txt` | Versi PyTorch dan library pendukung (termasuk `torchvision` dan `matplotlib`); baris komentar `WAJIB: Python 3.14, lihat README` |

## Input dan output

| Modul | Input | Output |
|---|---|---|
| Forward process | gambar bersih (B,1,28,28) dalam [-1,1], `t` (B,), noise (B,1,28,28) | gambar ber-noise (B,1,28,28) |
| U-Net | gambar ber-noise (B,1,28,28), `t` (B,) | prediksi noise (B,1,28,28) |
| Fungsi sampling | model, jumlah gambar N, device | gambar (N,1,28,28) dalam [-1,1] |
| Pemilihan device | - | device pertama yang tersedia: cuda, mps, cpu |

## Kontrak dengan modul lain
- **Ke Teman B (`train.py`):** `config.py` menyediakan baseline; `train.py` menimpa learning rate dan T dengan konfigurasi dari `experiments.py`, lalu membangun `diffusion.py` dengan T efektif dan model dengan parameter pembentuk dari `config.py`. `diffusion.py` menyediakan forward process dan pengambilan `t` acak yang valid (0 sampai T-1). Loss MSE dihitung di `train.py`. Untuk grid selama training, `train.py` memanggil fungsi sampling di `diffusion.py`.
- **Ke Teman B (`sample.py`):** `sample.py` membangun ulang model dengan `model.py` dan `diffusion.py` memakai parameter model dan T dari checkpoint, lalu memanggil fungsi sampling. `sample.py` tidak memuat logika reverse process.
- **Dari Teman A (`dataset.py`):** menerima satu tensor (B,1,28,28) dalam [-1,1], tanpa label.
- Hanya ketua yang mengubah `config.py`.

## Integrasi
- Menggabungkan branch anggota ke `main`.
- Memastikan satu seed dan satu `config.py` dipakai semua orang.
- Memastikan tidak ada device tetap di seluruh kode.
- Menguji simpan-muat checkpoint dan menjalankan smoke test setelah penggabungan.

## Uji mandiri sebelum diserahkan ke Teman B
- Forward process divisualisasikan pada beberapa nilai `t`; gambar makin berisik ke arah T.
- U-Net diuji dengan input acak: shape output sama dengan input.
- Fungsi sampling diuji berjalan end-to-end dengan model yang belum dilatih (yang diuji hanya alurnya).

## Harus bisa dijelaskan saat presentasi
- Mengapa noise ditambahkan bertahap dan apa fungsi noise schedule.
- Arti alpha-bar dan mengapa gambar pada timestep `t` dapat dihitung langsung dari gambar bersih.
- Mengapa model memprediksi noise, bukan gambar.
- Fungsi skip connection dan alur ukuran 28 → 14 → 7 → 14 → 28.
- Mengapa timestep disuntikkan ke U-Net dan cara kerja embedding sinusoidal.
- Apa yang terjadi di setiap langkah sampling.
- Mengapa T harus tersimpan di checkpoint.
- Mengapa seed dan config dipusatkan, dan mengapa device tidak ditulis tetap.

---

# JOBDESK TEMAN A: Dataset, Visualisasi, Check Data, Kompilasi Log

Peran **[PDF]**: Data Pipeline & Preprocessing Engineer; Lead Documentarian (kompilasi Log Interaksi LLM).

**File milik:** `dataset.py`, `visualize.py`, `scripts/check_data.py`, `docs/LOG_INTERAKSI_GABUNGAN.md`, `docs/logs/log_teman_a.md`.

## Modul

| File | Isi |
|---|---|
| `dataset.py` | Memuat MNIST dengan `download=True`; normalisasi ke [-1,1]; DataLoader dengan batch size dari `config.py`; mendukung mode smoke test (subset kecil sesuai `config.py`). DataLoader hanya mengembalikan gambar: label dibuang di dalam `dataset.py`. Tidak memindahkan data ke device; itu dilakukan `train.py` |
| `visualize.py` | (1) Fungsi menyimpan grid gambar dari tensor (N,1,28,28) dalam [-1,1], termasuk konversi ke rentang tampilan; (2) fungsi membuat grafik loss dari catatan loss per epoch dan menyimpannya ke file. Tensor dapat berada di device mana pun; fungsi memindahkannya ke CPU sebelum menyimpan |
| `scripts/check_data.py` | Memeriksa shape batch, rentang nilai (min/maks), dan tipe data; menyimpan contoh gambar memakai fungsi grid di `visualize.py` |

Cara menjalankan dari root repo **[Asumsi]**: `python -m scripts.check_data` (memakai `-m` agar `check_data.py` dapat mengimpor `dataset.py`, `config.py`, dan `visualize.py` di root). Jalankan pertama kali dengan koneksi internet karena `download=True` mengunduh MNIST ke `data/`.

## Input dan output

| Modul | Input | Output |
|---|---|---|
| `dataset.py` | MNIST (diunduh otomatis); `config.py` (batch size, flag smoke test, path data) | DataLoader yang menghasilkan satu tensor float (B,1,28,28) dalam [-1,1] per batch |
| `visualize.py` (grid) | tensor (N,1,28,28) dalam [-1,1], path tujuan | file gambar grid |
| `visualize.py` (grafik loss) | catatan loss per epoch, path tujuan | file grafik loss |
| `check_data.py` | DataLoader dari `dataset.py` | laporan shape dan rentang; gambar contoh |

## Kontrak dengan modul lain
- **Ke Teman B (`train.py`):** fungsi pembuat DataLoader; tiap batch adalah satu tensor (B,1,28,28), float, rentang [-1,1], tanpa label.
- **Ke Teman B (`train.py` dan `sample.py`):** `visualize.py` menyediakan fungsi grafik loss (dipanggil `train.py`) dan fungsi simpan grid gambar (dipanggil `train.py` tiap N epoch dan `sample.py`).
- **Dari Ketua (`config.py`):** batch size, flag smoke test, ukuran subset, dan path data diambil dari config; tidak ada angka tetap di `dataset.py`.
- Tidak ada device tetap di kode.
- Masalah shape atau rentang nilai dari DataLoader, serta kegagalan fungsi `visualize.py`, ditangani Teman A.

## Kompilasi log
Menggabungkan `log_ketua.md`, `log_teman_a.md`, dan `log_teman_b.md` menjadi `docs/LOG_INTERAKSI_GABUNGAN.md` dengan format templat dosen; memastikan setiap tautan chat aktif dan kronologi setiap sesi mengikuti inisiasi → debugging → optimasi. Log mentah ditulis tiap anggota sendiri; Teman A hanya merapikan dan menggabungkan.

## Uji mandiri
- Satu batch dari DataLoader: shape (B,1,28,28), tipe float, nilai min/maks dalam [-1,1].
- Mode smoke test menghasilkan subset kecil dengan shape yang sama.
- `visualize.py` menyimpan grid dari tensor acak berbentuk (N,1,28,28) dan grafik loss dari daftar angka contoh.
- `python -m scripts.check_data` berjalan dari root repo dan menampilkan laporan serta contoh gambar yang benar.

## Harus bisa dijelaskan saat presentasi
- Mengapa data dinormalisasi ke [-1,1] dan bedanya dengan [0,1].
- Mengapa DataLoader hanya mengembalikan gambar (model unconditional) dan di mana label dibuang.
- Bagaimana shape data mengalir dari dataset ke model.
- Cara kerja mode smoke test pada data.
- Mengapa `visualize.py` mengonversi rentang [-1,1] sebelum menyimpan gambar.
- Garis besar cara kerja noise dan alur seluruh proyek (penguasaan individu dinilai).

---

# JOBDESK TEMAN B: Training, Sampling, Eksperimen Tuning

Peran **[PDF]**: Training Loop & Hyperparameter Tuning Engineer.

**File milik:** `train.py`, `sample.py`, `experiments.py`, `results/` (grafik loss, gambar sampel, `experiments.md`), `docs/logs/log_teman_b.md`.

## Modul

| File | Isi |
|---|---|
| `experiments.py` | Daftar konfigurasi eksperimen bernama. Tiap konfigurasi hanya menimpa learning rate dan/atau T (tidak batch size, epoch, atau seed). Menyertakan konfigurasi `baseline` (tanpa timpaan) **[Asumsi]** |
| `train.py` | Memilih konfigurasi berdasarkan nama (argumen saat dijalankan; jika tanpa nama, dipakai `baseline`) **[Asumsi]**; training loop; loss MSE antara noise asli dan prediksi; optimizer; pencatatan loss per epoch; checkpoint berkala dan akhir; grafik loss lewat `visualize.py`; grid gambar sampel tiap N epoch (N dari `config.py`) dengan memanggil fungsi sampling di `diffusion.py` lalu fungsi grid di `visualize.py`. Saat membuat grid, model dialihkan ke mode evaluasi tanpa gradien lalu dikembalikan ke mode training **[Asumsi]**. Memindahkan batch dan model ke device dari `utils.py` |
| `sample.py` | Memuat checkpoint ke device dari `utils.py`; membangun ulang model dan `diffusion.py` dari isi checkpoint; memanggil fungsi sampling dari `diffusion.py`; menyimpan grid lewat `visualize.py`. Tidak berisi logika reverse process |
| Eksperimen tuning | Variasi learning rate dan T, satu variabel diubah dalam satu waktu **[Asumsi]**; hasil dicatat di `results/experiments.md` dan grafik per konfigurasi |

**Isi checkpoint:** bobot model, T, parameter pembentuk model, epoch, dan optimizer. Nama file memuat nama konfigurasi agar tidak saling menimpa **[Asumsi]**.

## Input dan output

| Modul | Input | Output |
|---|---|---|
| `train.py` | DataLoader dari `dataset.py` (satu tensor per batch); model dari `model.py`; forward process dan fungsi sampling dari `diffusion.py`; baseline dari `config.py` (termasuk N); nama konfigurasi dari `experiments.py`; device dari `utils.py` | checkpoint di `checkpoints/`; catatan loss; grafik loss dan grid sampel tiap N epoch di `results/` |
| `sample.py` | checkpoint; `config.py` (jumlah gambar sampel); device dari `utils.py` | grid gambar sampel di `results/samples/` |

## Kontrak dengan modul lain
- **Dari Teman A (`dataset.py`):** tiap batch adalah satu tensor (B,1,28,28) dalam [-1,1], tanpa label. `train.py` memakainya langsung sebagai gambar.
- **Dari Teman A (`visualize.py`):** fungsi grafik loss dan fungsi simpan grid gambar.
- **Dari Ketua (`diffusion.py`):** forward process untuk membuat gambar ber-noise pada `t` acak; fungsi sampling. `diffusion.py` menerima T sebagai parameter, jadi `train.py` meneruskan T efektif (baseline atau hasil timpaan).
- **Dari Ketua (`model.py`):** U-Net menerima `(x_t, t)` dan mengeluarkan prediksi noise (B,1,28,28). Model dibangun dari parameter pembentuk model; `train.py` menyimpannya di checkpoint.
- **Dari Ketua (`utils.py`, `config.py`):** fungsi pemilihan device; nilai baseline (seed, batch size, epoch, learning rate, T, parameter model, flag smoke test, N, jumlah gambar sampel, path).
- Tidak ada device tetap di kode. `experiments.py` milik Teman B sendiri; perubahan `config.py` tetap lewat ketua.
- Jika shape output model salah, itu ditangani ketua. Jika `train.py` salah memakai input, itu ditangani Teman B.

## Uji mandiri
- Sebelum modul asli siap, alur `train.py` dapat diuji dengan tensor acak berbentuk (B,1,28,28) dalam [-1,1] dan model tiruan sederhana; setelah modul asli siap, bagian sementara dihapus.
- Training berjalan di mode smoke test; loss tercatat per epoch dan grid tersimpan minimal satu kali (N pada smoke test tidak lebih besar dari jumlah epoch smoke).
- Uji simpan-muat: checkpoint yang disimpan `train.py` dapat dimuat `sample.py` dan menghasilkan gambar dengan shape (N,1,28,28).
- `train.py` dengan nama konfigurasi eksperimen memakai learning rate dan T hasil timpaan, dan T itu tersimpan di checkpoint.

## Harus bisa dijelaskan saat presentasi
- Mengapa loss berupa MSE antara noise asli dan noise prediksi.
- Apa yang terjadi pada tiap iterasi training (pilih `t` acak, tambah noise, prediksi, hitung loss).
- Apa yang terjadi di tiap langkah sampling dan mengapa grid dibuat tiap N epoch.
- Bagaimana konfigurasi eksperimen menimpa baseline dan mengapa hanya learning rate dan T.
- Mengapa learning rate dan T memengaruhi hasil, serta temuan eksperimen.
- Mengapa batch size dikunci.
- Isi checkpoint dan mengapa semuanya dibutuhkan agar `sample.py` dapat membangun ulang model.
