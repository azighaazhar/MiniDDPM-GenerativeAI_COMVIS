# PRD Final: Mini DDPM pada MNIST (Notebook)

**Cara pakai:** Tempel bagian umum + jobdesk milikmu ke AI-mu. Bagian orang lain boleh dibaca, tapi tidak perlu ditempel.

Label: **[PDF]** = dari panduan dosen, **[Keputusan]** = disepakati kelompok, **[Asumsi]** = usulan yang dipakai sampai ada keputusan lain.

Urutan ketergantungan: data dan model dikerjakan paralel, training dilakukan setelah keduanya jadi.

---

# BAGIAN UMUM (semua anggota)

## 1. Tujuan
Membangun model difusi Mini DDPM dari nol, dilatih pada MNIST 28x28 (1 channel), menggunakan Python dan PyTorch. Model menghasilkan digit tulisan tangan dari noise murni. Seluruh kode dibuat lewat kolaborasi dengan LLM (vibe coding) **[PDF]**.

Hasil akhir proyek adalah **satu file `.ipynb` yang berdiri sendiri** (boleh berisi fungsi dan kelas), sesuai arahan dosen **[Keputusan]**.

## 2. Aturan utama
- Seluruh kode ada di sel notebook. Tidak ada file `.py` baru **[Keputusan]**.
- File `.py` lama bukan bagian proyek. Ketua menghapusnya dari repo setelah `ketua.ipynb` selesai; riwayatnya tetap ada di Git **[Keputusan]**.
- Anggota tidak memakai dan tidak melampirkan file `.py`. Acuan nama dan antarmuka hanya PRD ini, jadi anggota melampirkan PRD, bukan file kode **[Keputusan]**.
- Tidak ada import antar-file. Yang di-import hanya library: `torch`, `numpy`, `matplotlib`, `torchvision` **[Keputusan]**.

## 3. Aturan proyek
- Dilarang menyalin kode dari GitHub atau blog tutorial **[PDF]**.
- Boleh memakai layer dasar `torch.nn` **[Keputusan]**.
- Dilarang memakai library difusi jadi (misalnya `diffusers`) dan bobot pretrained **[Asumsi]**.
- U-Net, noise schedule, dan timestep embedding disusun sendiri **[Keputusan]**.
- Tidak ada conditional generation, classifier evaluasi, atau fine-tuning dalam arti melanjutkan model pretrained **[Keputusan]**.

## 4. Keputusan teknis
- Model: Mini DDPM. Dataset: MNIST 28x28 **[Keputusan]**.
- U-Net maksimal dua level downsampling: 28 → 14 → 7 **[Keputusan]**.
- Normalisasi data ke [-1, 1] **[Asumsi]**. Timestep embedding sinusoidal **[Asumsi]**. Loss MSE antara noise asli dan noise prediksi **[Asumsi]**.
- Dua variabel tuning: **learning rate** dan **jumlah timestep T**. Batch size dikunci; nilainya dan jumlah epoch ditentukan setelah uji memori dan disimpan di sel config **[Keputusan]**.
- Sel config hanya berisi nilai baseline. Bagian experiments (milik Teman B) berisi daftar konfigurasi eksperimen bernama yang menimpa learning rate dan T. Fungsi `train` memilih konfigurasi berdasarkan nama **[Keputusan]**.
- DataLoader hanya mengembalikan gambar (tanpa label), memakai `download=True` **[Keputusan]**.
- Checkpoint berisi: bobot model, T, parameter pembentuk model, epoch, dan optimizer. Dengan isi ini fungsi `sample` dapat membangun ulang model dengan benar **[Keputusan]**.
- Fungsi `train` menyimpan grid gambar sampel setiap N epoch; N diatur di sel config **[Keputusan]**.
- Checkpoint tidak di-commit. Grafik loss dan gambar sampel di-commit **[Keputusan]**.
- Satu seed dan satu config dipakai semua anggota **[Keputusan]**.
- Nama atribut `config` (huruf besar) **[Keputusan]**: `SEED`, `LEARNING_RATE`, `BATCH_SIZE`, `EPOCHS`, `NUM_WORKERS`, `T`, `BETA_START`, `BETA_END`, `BETA_REFERENCE_T`, `IMAGE_SIZE`, `MODEL_PARAMS`, `SAMPLE_EVERY_N_EPOCHS`, `NUM_SAMPLE_IMAGES`, `SMOKE_TEST`, `SMOKE_SUBSET_SIZE`, `SMOKE_EPOCHS`, `SMOKE_SAMPLE_EVERY`, `BASE_DIR`, `DATA_DIR`, `CHECKPOINT_DIR`, `RESULTS_DIR`, `LOSS_CURVES_DIR`, `SAMPLES_DIR`.

## 5. Device dan versi Python
- `get_device` memilih device berurutan: cuda, lalu mps, lalu cpu. Tidak ada device tetap di kode; semua sel memakai hasil fungsi itu **[Keputusan]**.
- Versi Python: **3.14** (ketua memakai 3.14.6). Semua anggota memakai versi yang sama. Dicatat di README dan sebagai baris komentar di `requirements.txt`: `WAJIB: Python 3.14, lihat README` **[Keputusan]**.
- Jika memakai Colab, versi Python bawaan Colab diterima; yang dijaga adalah tidak memakai fitur khusus Python 3.14 **[Keputusan]**.

## 6. Kontrak data antar-bagian

| Antarmuka | Bentuk |
|---|---|
| Batch dari DataLoader | satu tensor float (B, 1, 28, 28), nilai dalam [-1, 1] |
| Timestep `t` | tensor bilangan bulat (B,), nilai 0 sampai T-1 |
| Input model | gambar ber-noise (B, 1, 28, 28) dan `t` (B,) |
| Output model | prediksi noise, shape (B, 1, 28, 28) |
| Hasil sampling | tensor (N, 1, 28, 28), nilai dalam [-1, 1] |

Nilai parameter dibaca dari `config` (baseline) dan, untuk learning rate dan T, dari konfigurasi eksperimen yang dipilih. Tidak ada angka tetap di sel lain.

## 7. Struktur repo dan pemilik file (satu file satu pemilik) **[Keputusan]**

```
mini-ddpm-mnist/
├── README.md              (Ketua)   versi Python, cara instal dan menjalankan
├── requirements.txt       (Ketua)   versi PyTorch dan library pendukung
├── .gitignore             (Ketua)   abaikan data/ dan checkpoints/
├── MiniDDPM.ipynb         (Ketua)   notebook final, dirakit dari tiga notebook di bawah
├── notebooks/
│   ├── ketua.ipynb        (Ketua)
│   ├── A.ipynb            (Teman A)
│   └── B.ipynb            (Teman B)
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

- Tiap anggota hanya mengubah notebook miliknya, di branch sendiri.
- `MiniDDPM.ipynb` dirakit Ketua dari `ketua.ipynb`, `A.ipynb`, dan `B.ipynb`.
- `BASE_DIR` ditentukan satu kali di sel config: folder kerja saat ini (`Path.cwd()`), dan jika nama foldernya `notebooks`, dipakai folder induknya. Dengan begitu `data/`, `checkpoints/`, dan `results/` selalu berada di root repo, baik notebook dijalankan dari root maupun dari `notebooks/`.
- Perintah `python -m scripts.check_data` digantikan sel uji pada bagian dataset.

## 8. Isi notebook (urutan sel)
Notebook final dan notebook tiap anggota mengikuti urutan bagian yang sama. Tiap anggota hanya mengisi bagiannya.

| No | Bagian | Pemilik |
|---|---|---|
| 0 | Judul dan ringkasan proyek (markdown) | Ketua **[Asumsi]** |
| 1 | Import library (satu sel) | Ketua **[Asumsi]**; di notebook anggota, tiap orang mengimpor yang dipakai bagiannya, lalu Ketua menyatukannya saat merakit |
| 2 | config: nilai baseline sebagai `SimpleNamespace` bernama `config`, sehingga `config.X` tetap berlaku | Ketua |
| 3 | utils: `set_seed` dan `get_device` | Ketua |
| 4 | dataset: DataLoader MNIST | Teman A |
| 5 | visualize: grid gambar dan grafik loss | Teman A |
| 6 | model: timestep embedding, blok dasar, U-Net | Ketua |
| 7 | diffusion: kelas `Diffusion` | Ketua |
| 8 | experiments: daftar konfigurasi eksperimen | Teman B |
| 9 | train: fungsi training | Teman B |
| 10 | sample: fungsi sampling dari checkpoint | Teman B |
| 11 | Uji: satu sel uji per bagian di atas | Pemilik bagian masing-masing |
| 12 | Eksekusi: jalankan training baseline, tampilkan grafik loss dan grid gambar di notebook (juga disimpan ke `results/`), lalu sampling dari checkpoint | Teman B **[Asumsi]** |
| 13 | Eksperimen dan hasil: jalankan konfigurasi eksperimen, tampilkan perbandingan | Teman B **[Asumsi]** |

## 9. Aturan sel
- Satu sel kode maksimal sekitar 30 baris dan hanya berisi satu fungsi, satu kelas, atau satu langkah; yang panjang dipecah **[Keputusan]**.
- Sel markdown pendek, 1-3 kalimat, dengan bahasa sederhana dan natural, tidak kaku **[Keputusan]**.
- Tiap bagian diawali sel markdown berisi judul dan nama pemilik, dan diakhiri sel uji.
- Urutan sel dari yang diandalkan ke yang memakai: config sebelum utils, model dan diffusion sebelum train.
- Blok `if __name__ == "__main__"` dan `python -m` diganti sel uji. Argparse dan perintah terminal diganti pemanggilan fungsi, misalnya `train("baseline")` dan `sample(path_checkpoint)`.
- Notebook A dan B boleh memuat salinan sementara sel milik Ketua yang mereka butuhkan untuk uji, diberi label **"SALINAN SEMENTARA, jangan dimasukkan ke notebook final"**.
- Notebook kerja (`ketua.ipynb`, `A.ipynb`, `B.ipynb`) dikosongkan outputnya sebelum commit (Clear All Outputs) **[Keputusan]**.
- `MiniDDPM.ipynb` final dijalankan dengan Restart and Run All di mesin ber-GPU, lalu disimpan dengan output lengkap **[Keputusan]**.

## 10. Kontrak antar-bagian
Nama bertanda **[Keputusan]** sudah ditetapkan kelompok dan sesuai kode. Nama bertanda **[Asumsi]** adalah usulan penamaan yang dipakai sampai kelompok menetapkan nama lain.

| Bagian | Nama publik | Pemilik | Input | Output |
|---|---|---|---|---|
| config | `config` (`SimpleNamespace`) **[Keputusan]**, `BASE_DIR` **[Keputusan]** | Ketua | - | semua atribut `config` (daftar lengkap di Bagian Umum, butir 4: Keputusan teknis), termasuk path yang diturunkan dari `BASE_DIR` |
| utils | `set_seed(seed)` **[Keputusan]** | Ketua | seed | - (mengatur seed) |
| utils | `get_device()` **[Keputusan]** | Ketua | - | device pertama yang tersedia: cuda, mps, cpu |
| dataset | `get_dataloader` **[Asumsi]** | Teman A | `config` (batch size, flag smoke test, path data) | DataLoader yang menghasilkan satu tensor float (B,1,28,28) dalam [-1,1] per batch, tanpa label |
| visualize | `save_image_grid` **[Asumsi]** | Teman A | tensor (N,1,28,28) dalam [-1,1], path tujuan | file gambar grid (juga dapat ditampilkan di notebook) |
| visualize | `plot_loss` **[Asumsi]** | Teman A | catatan loss per epoch (satu atau beberapa seri berlabel), path tujuan | file grafik loss (juga dapat ditampilkan di notebook) |
| model | `SinusoidalTimeEmbedding` **[Asumsi]**, `ResBlock` **[Keputusan]** | Ketua | - | komponen penyusun `UNet` |
| model | `UNet(in_channels, base_channels, channel_mults, time_emb_dim)` **[Keputusan]**; dibuat dengan `UNet(**config.MODEL_PARAMS)`; dipanggil `model(x, t)` | Ketua | `x`: gambar ber-noise (B,1,28,28), `t` (B,) | prediksi noise (B,1,28,28) |
| diffusion | `Diffusion(T, device=None)` **[Keputusan]** | Ketua | `T`; `device` (opsional) | objek yang memuat noise schedule |
| diffusion | `Diffusion.add_noise(x0, t, noise)` (forward process) **[Keputusan]** | Ketua | `x0`: gambar bersih (B,1,28,28) dalam [-1,1], `t` (B,), `noise` (B,1,28,28) | gambar ber-noise (B,1,28,28) |
| diffusion | `Diffusion.sample_timesteps(batch_size, device)` (pengambilan `t` acak) **[Keputusan]** | Ketua | `batch_size`, `device` | `t` (B,) bilangan bulat 0 sampai T-1 |
| diffusion | `Diffusion.sample(model, num_images, device)` (reverse process) **[Keputusan]** | Ketua | `model`, `num_images` (jumlah gambar), `device` | gambar (N,1,28,28) dalam [-1,1] |
| experiments | `EXPERIMENTS` **[Asumsi]** | Teman B | - | daftar konfigurasi bernama; tiap konfigurasi hanya menimpa learning rate dan/atau T; memuat `baseline` (tanpa timpaan) |
| train | `train` **[Keputusan]**, parameter nama konfigurasi **[Asumsi]** | Teman B | nama konfigurasi (tanpa nama dipakai `baseline`) **[Asumsi]**; DataLoader dari `get_dataloader`; `UNet`; `Diffusion`; `config`; `EXPERIMENTS`; device dari `get_device` | checkpoint di `checkpoints/`; catatan loss; grafik loss; grid sampel tiap N epoch di `results/` |
| sample | `sample` **[Keputusan]**, parameter `path_checkpoint` **[Keputusan]** | Teman B | `path_checkpoint`; `config` (jumlah gambar sampel); device dari `get_device` | grid sampel di `results/samples/` dan tensor (N,1,28,28) |

Catatan kontrak:
- Di notebook ada dua hal bernama `sample` yang berbeda: method `Diffusion.sample(model, num_images, device)` milik Ketua (reverse process) dan fungsi `sample(path_checkpoint)` milik Teman B (memuat checkpoint lalu memanggil `Diffusion.sample`) **[Keputusan]**.
- `train` menghitung loss MSE sendiri **[Asumsi]**. Nilai efektif (baseline + timpaan) dipakai sebagai salinan lokal dan tidak mengubah `config` **[Asumsi]**.
- Untuk grid selama training, `train` memanggil `Diffusion.sample` dengan model yang sedang dilatih, lalu `save_image_grid`. Model dialihkan ke mode evaluasi tanpa gradien lalu dikembalikan ke mode training **[Asumsi]**.
- Fungsi `sample` membangun ulang `UNet` dan `Diffusion` memakai parameter model dan T dari checkpoint, memuat checkpoint ke device dari `get_device`, lalu memanggil `Diffusion.sample`. Fungsi `sample` tidak memuat logika reverse process.
- Nama file checkpoint memuat nama konfigurasi agar tidak saling menimpa **[Asumsi]**.
- Dataset tidak memindahkan data ke device; `train` memindahkan batch dan model.

## 11. Aturan kerja
- **Log per anggota [PDF]:** setiap sesi LLM untuk membuat bagian baru atau memperbaiki bug dicatat di `docs/logs/log_<nama>.md` pada akhir sesi, memakai templat berikut. "Target Modul" diisi nama bagian notebook. Teman A hanya merapikan dan menggabungkan log menjadi `docs/LOG_INTERAKSI_GABUNGAN.md`.

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
- **Git [Keputusan]:** tiap anggota commit ke branch sendiri; Ketua menggabungkan ke `main`. Setiap anggota hanya mengubah notebook miliknya.
- **Debugging [Keputusan]:** tiap orang men-debug bagiannya sendiri. Error lintas bagian ditangani pemilik bagian yang menerima input. Penemu error mencatatnya di log miliknya. Salin pesan error utuh dari output sel notebook, tanyakan ke LLM, analisis solusinya, lalu catat di log **[PDF]**.

---

# JOBDESK KETUA: config, utils, model, diffusion, perakitan notebook final

Peran **[PDF]**: Prompt Engineer & LLM Navigator (merancang system prompt awal, mengomunikasikan arsitektur ke LLM, menjaga konsistensi logika coding).

**File milik:** `notebooks/ketua.ipynb`, `MiniDDPM.ipynb`, `README.md`, `requirements.txt`, `.gitignore`, `docs/logs/log_ketua.md`.

**Bagian di notebook:** 0 (judul), 1 (import, saat perakitan), 2 (config), 3 (utils), 6 (model), 7 (diffusion), serta sel uji bagian-bagian itu.

## Bagian dan isi

| Bagian | Isi |
|---|---|
| config | `config` sebagai `SimpleNamespace`, hanya nilai baseline, dengan atribut persis seperti daftar di Bagian Umum (butir 4: Keputusan teknis), termasuk `MODEL_PARAMS` (parameter pembentuk model), `SMOKE_TEST` beserta `SMOKE_SUBSET_SIZE`, `SMOKE_EPOCHS`, `SMOKE_SAMPLE_EVERY` (mode smoke test), `SAMPLE_EVERY_N_EPOCHS` (N interval grid sampel), dan `NUM_SAMPLE_IMAGES` (jumlah gambar sampel). `BASE_DIR` ditentukan satu kali di sel ini (lihat Bagian Umum, butir 7); path (`DATA_DIR`, `CHECKPOINT_DIR`, `RESULTS_DIR`, `LOSS_CURVES_DIR`, `SAMPLES_DIR`) diturunkan dari `BASE_DIR` |
| utils | `set_seed` dan `get_device` (cuda, lalu mps, lalu cpu) |
| model | `SinusoidalTimeEmbedding` **[Asumsi]**, `ResBlock` **[Keputusan]**, `UNet` **[Keputusan]**: timestep embedding sinusoidal; blok dasar; U-Net lengkap dengan skip connection dan dua level downsampling (28 → 14 → 7). Dibangun dari parameter pembentuk model yang diteruskan sebagai argumen |
| diffusion | Kelas `Diffusion`, dibangun dengan T sebagai parameter agar T hasil timpaan eksperimen dapat dipakai. Memuat noise schedule (beta, alpha, alpha-bar dan turunannya) serta `add_noise`, `sample_timesteps`, dan `sample` **[Keputusan]** |
| README | Python 3.14 (ketua 3.14.6), cara instal dari `requirements.txt`, cara menjalankan notebook |
| requirements.txt | Versi PyTorch dan library pendukung (`torch`, `torchvision`, `numpy`, `matplotlib`); baris komentar `WAJIB: Python 3.14, lihat README` |

## Input dan output

| Bagian | Input | Output |
|---|---|---|
| `Diffusion.add_noise(x0, t, noise)` | `x0`: gambar bersih (B,1,28,28) dalam [-1,1], `t` (B,), `noise` (B,1,28,28) | gambar ber-noise (B,1,28,28) |
| `UNet` | gambar ber-noise (B,1,28,28), `t` (B,) | prediksi noise (B,1,28,28) |
| `Diffusion.sample(model, num_images, device)` | `model`, `num_images` (jumlah gambar), `device` | gambar (N,1,28,28) dalam [-1,1] |
| `get_device` | - | device pertama yang tersedia: cuda, mps, cpu |

## Kontrak dengan bagian lain
- **Ke Teman B (`train`):** `config` menyediakan baseline; `train` menimpa learning rate dan T dengan konfigurasi dari `EXPERIMENTS` yang dipilih berdasarkan nama, lalu membuat `Diffusion` dengan T efektif dan `UNet` dengan parameter pembentuk dari `config`. `Diffusion` menyediakan `add_noise` dan `sample_timesteps(batch_size, device)` (nilai `t` 0 sampai T-1). Loss MSE dihitung di `train`. Untuk grid selama training, `train` memanggil `Diffusion.sample`.
- **Ke Teman B (fungsi `sample`):** fungsi `sample` membangun ulang `UNet` dan `Diffusion` memakai parameter model dan T dari checkpoint, lalu memanggil `Diffusion.sample`. Fungsi `sample` tidak memuat logika reverse process. Method `Diffusion.sample` dan fungsi `sample(path_checkpoint)` milik Teman B adalah dua hal yang berbeda.
- **Dari Teman A (`get_dataloader`):** menerima satu tensor (B,1,28,28) dalam [-1,1], tanpa label.
- Hanya Ketua yang mengubah isi config baseline.
- Tidak ada device tetap di kode.

## Perakitan notebook final
- Menyalin sel dari `ketua.ipynb`, `A.ipynb`, dan `B.ipynb` mengikuti urutan bagian 0 sampai 13.
- Menghapus semua sel berlabel "SALINAN SEMENTARA".
- Menyatukan sel import menjadi satu sel dan memastikan `BASE_DIR` hanya ditentukan sekali.
- Memeriksa urutan sel: yang diandalkan ada sebelum yang memakai.
- Memastikan tidak ada import antar-file dan tidak ada device tetap.
- Menjalankan `MiniDDPM.ipynb` dengan Restart and Run All di mesin ber-GPU, lalu menyimpannya dengan output lengkap **[Keputusan]**.
- Menggabungkan branch anggota ke `main`.

## Uji mandiri (sel uji)
- `get_device` menampilkan device terpilih; `set_seed` menghasilkan angka acak yang sama pada dua kali pemanggilan dengan seed sama.
- Forward process divisualisasikan pada beberapa nilai `t`; gambar makin berisik ke arah T.
- `UNet` diuji dengan input acak: shape output sama dengan input.
- `Diffusion.sample` diuji berjalan end-to-end dengan model yang belum dilatih (yang diuji hanya alurnya).

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

# JOBDESK TEMAN A: dataset dan visualize

Peran **[PDF]**: Data Pipeline & Preprocessing Engineer; Lead Documentarian (kompilasi Log Interaksi LLM).

**File milik:** `notebooks/A.ipynb`, `docs/LOG_INTERAKSI_GABUNGAN.md`, `docs/logs/log_teman_a.md`.

**Bagian di notebook:** 4 (dataset), 5 (visualize), serta sel uji kedua bagian itu. Bagian lain di `A.ipynb` dibiarkan kosong, atau berisi salinan sementara sel milik Ketua yang dibutuhkan untuk uji (diberi label "SALINAN SEMENTARA, jangan dimasukkan ke notebook final").

## Bagian dan isi

| Bagian | Isi |
|---|---|
| dataset | `get_dataloader` **[Asumsi]**: memuat MNIST dengan `download=True`; normalisasi ke [-1,1]; DataLoader dengan batch size dari `config`; mendukung mode smoke test (subset kecil sesuai `config`). DataLoader hanya mengembalikan gambar: label dibuang di dalam fungsi ini. Tidak memindahkan data ke device; itu dilakukan `train` |
| visualize | (1) `save_image_grid` **[Asumsi]**: menyimpan grid gambar dari tensor (N,1,28,28) dalam [-1,1], termasuk konversi ke rentang tampilan, dan dapat menampilkannya di notebook; (2) `plot_loss` **[Asumsi]**: membuat grafik loss dari catatan loss per epoch dan menyimpannya ke file, dan dapat menampilkannya di notebook. Tensor dapat berada di device mana pun; fungsi memindahkannya ke CPU sebelum menyimpan |

## Input dan output

| Bagian | Input | Output |
|---|---|---|
| `get_dataloader` | MNIST (diunduh otomatis); `config` (batch size, flag smoke test, path data) | DataLoader yang menghasilkan satu tensor float (B,1,28,28) dalam [-1,1] per batch |
| `save_image_grid` | tensor (N,1,28,28) dalam [-1,1], path tujuan | file gambar grid |
| `plot_loss` | catatan loss per epoch (satu atau beberapa seri berlabel), path tujuan | file grafik loss |

## Kontrak dengan bagian lain
- **Ke Teman B (`train`):** `get_dataloader` menghasilkan batch berupa satu tensor (B,1,28,28), float, rentang [-1,1], tanpa label.
- **Ke Teman B (`train` dan fungsi `sample`):** `save_image_grid` dipanggil `train` tiap N epoch dan oleh fungsi `sample`; `plot_loss` dipanggil `train`. Teman B tidak menulis ulang logika menggambar.
- **Dari Ketua (`config`):** batch size, flag smoke test, ukuran subset, dan path data diambil dari `config`; tidak ada angka tetap di bagian dataset. `get_device` dipakai untuk device; tidak ada device tetap di kode.
- Masalah shape atau rentang nilai dari DataLoader, serta kegagalan fungsi di bagian visualize, ditangani Teman A.

## Kompilasi log
Menggabungkan `log_ketua.md`, `log_teman_a.md`, dan `log_teman_b.md` menjadi `docs/LOG_INTERAKSI_GABUNGAN.md` dengan format templat dosen (Bagian Umum, butir 11); memastikan setiap tautan chat aktif dan kronologi setiap sesi mengikuti inisiasi → debugging → optimasi. Log mentah ditulis tiap anggota sendiri; Teman A hanya merapikan dan menggabungkan.

## Uji mandiri (sel uji)
- Satu batch dari DataLoader: shape (B,1,28,28), tipe float, nilai min/maks dalam [-1,1].
- Mode smoke test menghasilkan subset kecil dengan shape yang sama.
- `save_image_grid` menyimpan dan menampilkan grid dari tensor acak berbentuk (N,1,28,28); `plot_loss` menyimpan dan menampilkan grafik dari daftar angka contoh.
- Sel uji bagian dataset menampilkan laporan shape dan rentang serta contoh gambar (menggantikan `python -m scripts.check_data`).

## Harus bisa dijelaskan saat presentasi
- Mengapa data dinormalisasi ke [-1,1] dan bedanya dengan [0,1].
- Mengapa DataLoader hanya mengembalikan gambar (model unconditional) dan di mana label dibuang.
- Bagaimana shape data mengalir dari dataset ke model.
- Cara kerja mode smoke test pada data.
- Mengapa `save_image_grid` mengonversi rentang [-1,1] sebelum menyimpan gambar.
- Garis besar cara kerja noise dan alur seluruh proyek (penguasaan individu dinilai).

---

# JOBDESK TEMAN B: experiments, train, sample

Peran **[PDF]**: Training Loop & Hyperparameter Tuning Engineer.

**File milik:** `notebooks/B.ipynb`, `results/` (grafik loss, gambar sampel, `experiments.md`), `docs/logs/log_teman_b.md`.

**Bagian di notebook:** 8 (experiments), 9 (train), 10 (sample), 12 (eksekusi), 13 (eksperimen dan hasil), serta sel uji bagian-bagian itu **[Asumsi untuk 12 dan 13]**. Bagian lain di `B.ipynb` dibiarkan kosong, atau berisi salinan sementara sel milik Ketua dan Teman A yang dibutuhkan untuk uji (diberi label "SALINAN SEMENTARA, jangan dimasukkan ke notebook final").

## Bagian dan isi

| Bagian | Isi |
|---|---|
| experiments | `EXPERIMENTS` **[Asumsi]**: daftar konfigurasi eksperimen bernama. Tiap konfigurasi hanya menimpa learning rate dan/atau T (tidak batch size, epoch, atau seed). Memuat konfigurasi `baseline` (tanpa timpaan) **[Asumsi]** |
| train | `train` (parameter nama konfigurasi **[Asumsi]**; tanpa nama dipakai `baseline` **[Asumsi]**): memilih konfigurasi berdasarkan nama dan menggabungkannya dengan baseline `config` sebagai salinan lokal; training loop; loss MSE antara noise asli dan prediksi; optimizer; pencatatan loss per epoch; checkpoint berkala dan akhir; grafik loss lewat `plot_loss`; grid gambar sampel tiap N epoch (N dari `config`) dengan memanggil `Diffusion.sample` lalu `save_image_grid`. Saat membuat grid, model dialihkan ke mode evaluasi tanpa gradien lalu dikembalikan ke mode training **[Asumsi]**. Memindahkan batch dan model ke device dari `get_device` |
| sample | `sample(path_checkpoint)`: memuat checkpoint ke device dari `get_device`; membangun ulang `UNet` dan `Diffusion` dari isi checkpoint; memanggil `Diffusion.sample`; menyimpan grid lewat `save_image_grid`. Tidak berisi logika reverse process. Fungsi ini berbeda dari method `Diffusion.sample` milik Ketua |
| eksekusi | Menjalankan `train("baseline")`, menampilkan grafik loss dan grid gambar di notebook (juga disimpan ke `results/`), lalu menjalankan `sample` dari checkpoint |
| eksperimen dan hasil | Menjalankan konfigurasi eksperimen (variasi learning rate dan T, satu variabel diubah dalam satu waktu **[Asumsi]**), menampilkan perbandingan, dan mencatat hasil di `results/experiments.md` |

**Isi checkpoint:** bobot model, T, parameter pembentuk model, epoch, dan optimizer. Nama file memuat nama konfigurasi agar tidak saling menimpa **[Asumsi]**.

## Input dan output

| Bagian | Input | Output |
|---|---|---|
| `train` | nama konfigurasi; DataLoader dari `get_dataloader` (satu tensor per batch); `UNet`; `Diffusion` (`add_noise`, `sample_timesteps`, `sample`); baseline dari `config` (termasuk N); `EXPERIMENTS`; device dari `get_device` | checkpoint di `checkpoints/`; catatan loss; grafik loss dan grid sampel tiap N epoch di `results/` |
| `sample` | `path_checkpoint`; `config` (jumlah gambar sampel); device dari `get_device` | grid sampel di `results/samples/` dan tensor (N,1,28,28) |

## Kontrak dengan bagian lain
- **Dari Teman A (`get_dataloader`):** tiap batch adalah satu tensor (B,1,28,28) dalam [-1,1], tanpa label. `train` memakainya langsung sebagai gambar.
- **Dari Teman A (`save_image_grid`, `plot_loss`):** fungsi simpan grid gambar dan fungsi grafik loss.
- **Dari Ketua (`Diffusion`):** `add_noise(x0, t, noise)` untuk membuat gambar ber-noise pada `t` acak, `sample_timesteps(batch_size, device)` untuk `t`, dan `sample(model, num_images, device)` untuk sampling. `Diffusion` dibangun dengan T sebagai parameter, jadi `train` meneruskan T efektif (baseline atau hasil timpaan).
- **Dari Ketua (`UNet`):** menerima `(x_t, t)` dan mengeluarkan prediksi noise (B,1,28,28). `UNet` dibangun dari parameter pembentuk model; `train` menyimpannya di checkpoint.
- **Dari Ketua (`config`, `get_device`, `set_seed`):** nilai baseline (atribut `config` sesuai daftar di Bagian Umum); pemilihan device (cuda, mps, cpu).
- Tidak ada device tetap di kode. `EXPERIMENTS` milik Teman B sendiri; perubahan nilai baseline di `config` tetap lewat Ketua.
- Jika shape output model salah, itu ditangani Ketua. Jika `train` salah memakai input, itu ditangani Teman B.

## Uji mandiri (sel uji)
- Sebelum bagian lain siap, alur `train` dapat diuji dengan tensor acak berbentuk (B,1,28,28) dalam [-1,1] dan model tiruan sederhana (diberi label "SALINAN SEMENTARA, jangan dimasukkan ke notebook final"); setelah bagian asli siap, bagian sementara dihapus.
- `train` berjalan di mode smoke test; loss tercatat per epoch dan grid tersimpan minimal satu kali (`SMOKE_SAMPLE_EVERY` tidak lebih besar dari `SMOKE_EPOCHS`).
- Uji simpan-muat: checkpoint yang disimpan `train` dapat dimuat `sample` dan menghasilkan gambar dengan shape (N,1,28,28).
- `train` dengan nama konfigurasi eksperimen memakai learning rate dan T hasil timpaan, T itu tersimpan di checkpoint, dan `config` tidak berubah setelah training.

## Harus bisa dijelaskan saat presentasi
- Mengapa loss berupa MSE antara noise asli dan noise prediksi.
- Apa yang terjadi pada tiap iterasi training (pilih `t` acak, tambah noise, prediksi, hitung loss).
- Apa yang terjadi di tiap langkah sampling dan mengapa grid dibuat tiap N epoch.
- Bagaimana konfigurasi eksperimen menimpa baseline dan mengapa hanya learning rate dan T.
- Mengapa learning rate dan T memengaruhi hasil, serta temuan eksperimen.
- Mengapa batch size dikunci.
- Isi checkpoint dan mengapa semuanya dibutuhkan agar `sample` dapat membangun ulang model.
