# Mini DDPM pada MNIST

Model difusi Mini DDPM yang dibangun dari nol dengan Python dan PyTorch. Model dilatih pada MNIST (28x28, 1 channel) dan menghasilkan digit tulisan tangan dari noise murni. Seluruh kode dibuat lewat kolaborasi dengan LLM (vibe coding) untuk tugas besar kelompok.

## Versi Python

**Wajib Python 3.14** (ketua memakai 3.14.6). Semua anggota memakai versi yang sama. Cek dengan:

```
python --version
```

## Instalasi

Semua perintah dijalankan dari root repo.

1. Buat dan aktifkan virtual environment.

   Windows:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```

   macOS / Linux:
   ```
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Pasang dependensi:
   ```
   pip install -r requirements.txt
   ```

3. Cek device yang terdeteksi:
   ```
   python utils.py
   ```
   Device dipilih otomatis dengan urutan cuda, lalu mps, lalu cpu. Tidak ada device yang ditulis tetap di kode.

   **Catatan Windows dengan GPU NVIDIA:** paket `torch` dari PyPI untuk Windows adalah versi CPU saja. Jika `python utils.py` menampilkan `cpu` padahal ada GPU NVIDIA, pasang ulang `torch==2.14.0` dan `torchvision==0.29.0` dengan perintah dari https://pytorch.org/get-started/locally/ (pilih Pip, Windows, dan versi CUDA yang sesuai).

## Konfigurasi

Semua nilai baseline (seed, batch size, epoch, learning rate, T, parameter model, smoke test, interval grid sampel, path) ada di `config.py`. Hanya ketua yang mengubah file ini. File lain membaca nilainya dari sana dan tidak menulis angka tetap.

## Cara menjalankan

### Uji mandiri modul milik ketua

```
python config.py
python utils.py
python diffusion.py
python model.py
```

### Memeriksa data

Jalankan pertama kali dengan koneksi internet karena MNIST diunduh otomatis ke `data/`.

```
python -m scripts.check_data
```

### Training (disesuaikan setelah train.py dan sample.py jadi)

Training dengan baseline:

```
python train.py
```

Eksperimen dengan konfigurasi bernama (nama diambil dari `experiments.py`, yang hanya menimpa learning rate dan/atau T):

```
python train.py <nama_konfigurasi>
```

Checkpoint disimpan di `checkpoints/`. Grafik loss dan grid sampel disimpan di `results/`.

### Sampling (disesuaikan setelah train.py dan sample.py jadi)

```
python sample.py
```

Hasil grid gambar disimpan di `results/samples/`.

## Struktur folder

```
mini-ddpm-mnist/
├── README.md
├── requirements.txt
├── .gitignore
├── config.py              nilai baseline
├── model.py               timestep embedding, blok dasar, U-Net
├── diffusion.py           noise schedule, forward process, sampling
├── utils.py               seed dan pemilihan device
├── experiments.py         konfigurasi eksperimen (learning rate, T)
├── train.py               training loop
├── sample.py              sampling dari checkpoint
├── dataset.py             DataLoader MNIST
├── visualize.py           grid gambar dan grafik loss
├── scripts/
│   └── check_data.py      pemeriksaan data
├── data/                  unduhan MNIST (tidak di-commit)
├── checkpoints/           checkpoint (tidak di-commit)
├── results/               hasil (di-commit)
│   ├── loss_curves/
│   ├── samples/
│   └── experiments.md
└── docs/
    ├── logs/              log LLM per anggota
    ├── LOG_INTERAKSI_GABUNGAN.md
    └── chat_exports/      ekspor chat tiap anggota
```

## Aturan kerja

- Satu file satu pemilik; setiap anggota hanya mengubah file miliknya.
- Tiap anggota commit ke branch sendiri; ketua menggabungkan ke `main`.
- Dilarang menyalin kode dari GitHub atau blog tutorial.
- Setiap sesi LLM dicatat di `docs/logs/` dan chat-nya disimpan sebagai share link atau ekspor di `docs/chat_exports/`.