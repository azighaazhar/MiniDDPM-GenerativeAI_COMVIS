# Mini DDPM pada MNIST

Model difusi (DDPM) kecil yang dibangun dari nol dengan PyTorch. Modelnya dilatih pada MNIST (28x28, satu channel) dan bisa membuat digit tulisan tangan dari noise murni. Seluruh kode dibuat lewat vibe coding bersama Claude, untuk Proyek 1 mata kuliah Generative AI (CAK4KBB3), Universitas Telkom.

## Isi repo

| Lokasi | Isi |
|---|---|
| `MiniDDPM.ipynb` | Notebook final, semua kode ada di sini |
| `notebooks/` | Notebook kerja tiap anggota (ketua, Teman A, Teman B) |
| `results/` | Grafik loss, grid gambar, dan tabel hasil eksperimen |
| `docs/prd_final_miniddpm_notebook.md` | PRD kelompok |
| `docs/logs_template/` | Log interaksi LLM tiap anggota, mengikuti template di panduan |
| `docs/chat_exports(cadangan_link_jika_bermasalah)/` | Salinan teks chat sebagai cadangan share link |
| `rakit.py` | Skrip penggabung sel, penjelasannya di bawah |

Folder `data/` (unduhan MNIST) dan `checkpoints/` dibuat saat notebook dijalankan dan tidak ikut Git.

## Cara menjalankan

1. Siapkan Python 3.12 atau 3.14, lalu buat virtual environment:

   ```
   python -m venv venv
   venv\Scripts\activate
   ```

   Di macOS atau Linux, aktifkan dengan `source venv/bin/activate`.

2. Pasang paket.

   Windows dengan GPU NVIDIA: pasang PyTorch versi CUDA dulu. Kami memakai CUDA 12.6, perintah terbaru ada di pytorch.org/get-started/locally.

   ```
   pip install torch torchvision --index-url https://download.pytorch.org/whl/cu126
   pip install -r requirements.txt
   ```

   macOS atau tanpa GPU NVIDIA:

   ```
   pip install -r requirements.txt
   ```

3. Buka `MiniDDPM.ipynb` di VS Code, pilih kernel `venv`, lalu klik Run All. Saat pertama kali, MNIST diunduh otomatis ke `data/`, jadi perlu internet.

Perangkat dipilih otomatis dengan urutan cuda, mps, lalu cpu. Tanpa GPU NVIDIA notebook tetap jalan, tetapi training penuh jauh lebih lama.

## Uji cepat (smoke test)

Di bagian 2 Config, pada sel kode kedua, ubah `config.SMOKE_TEST = True`. Notebook hanya memakai 512 gambar dan 2 epoch, jadi seluruh alur bisa dicek dalam beberapa menit. Kembalikan ke `False` untuk training sungguhan. File hasil uji ini bernama `*_smoke*` dan tidak ikut Git.

## Hasil

- Training penuh dijalankan di laptop dengan GPU GTX 1650 (4 GB), Windows, Python 3.12.4, PyTorch 2.14.1 dengan CUDA 12.6.
- 20 epoch per konfigurasi, batch size 64, sekitar 86 detik per epoch. Kelima konfigurasi selesai dalam sekitar 2,5 jam.
- Lima konfigurasi: baseline (learning rate 2e-4, T 1000), learning rate 1e-4, learning rate 5e-4, T 250, dan T 500.
- Loss akhir kelimanya berada di 0,0218 sampai 0,0224. Tabel lengkap ada di `results/experiments.md`.

## Isi notebook

Bagian 1 Import, 2 Config, dan 3 Utils (ketua). Bagian 4 Dataset dan 5 Visualize (Teman A). Bagian 6 Model U-Net dan 7 Diffusion (ketua). Bagian 8 Experiments, 9 Train, 10 Sample, 12 Eksekusi baseline, dan 13 Eksperimen dan hasil (Teman B). Bagian 14 adalah ringkasan hasil. Nomor 11 tidak dipakai karena sel uji hanya ada di notebook kerja.

## Pembagian kerja

| Anggota | Peran | Bagian |
|---|---|---|
| Muhammad Azigha Azhar | Ketua, Prompt Engineer dan LLM Navigator | config, utils, model, diffusion, perakitan notebook, training penuh |
| Mutiara Syaikha Husnaa | Teman A, Data Pipeline dan Preprocessing | dataset, visualize |
| Lilia Gita Savitri | Teman B, Training Loop dan Hyperparameter Tuning | experiments, train, sample, eksperimen |

## Tentang rakit.py

Kode awalnya ditulis sebagai file `.py`, lalu atas arahan dosen dipindah ke notebook. `rakit.py` adalah skrip hasil LLM (chat sesi 04) yang menggabungkan sel dari tiga notebook kerja menjadi `MiniDDPM.ipynb`. Skrip ini dijalankan sekali, tidak dipakai untuk menjalankan model, dan disimpan sebagai bukti proses perakitan.