LOG INTERAKSI LLM - KELOMPOK mini ddpm
Anggota: Mutiara Syaikha Husnaa (Teman A) - dataset dan visualize

---

## Sesi 1

- Tanggal Sesi: 02/11/2026
- Target Modul: Bagian 4 (dataset: get_dataloader) dan bagian 5 (visualize: save_image_grid, plot_loss), beserta sel uji
- Tautan Sesi Chat:
  - Kutipan percakapan: `docs/chat_exports/kutipan_sesi_teman_a.md` (giliran 72–157 dari chat "Notebook file location")
- Catatan sesi: Sesi dilakukan di chat yang sama dengan sesi Teman B, di akun Claude milik Gita. Permintaan kode awal (giliran 72–79) dikirim Gita dari akunnya. Saya melanjutkan mulai giliran 80 untuk setup environment, menjalankan notebook, debugging, dan push. Nomor giliran di bawah merujuk ke file kutipan.

KRONOLOGI PROMPT & RESPONS:

1. TAHAP INISIASI (Meminta Kode Awal)
   - Prompt Kelompok (giliran 72, dikirim Gita): "Hai, kamu tau tugasnya teman A? Tolong buatinnn". Di giliran 73 AI bertanya siapa yang mengetik; dijawab "bagian syaikha" (giliran 74).
   - Alasan Khusus:
     - Kode B (train, sample) sudah selesai dan memakai fungsi pengganti untuk bagian A. Karena itu, bagian A harus mengikuti bentuk yang sudah dipakai B:
       - `get_dataloader(cfg)` yang membaca `SMOKE_TEST` dan `SMOKE_SUBSET_SIZE` dari argumen;
       - `save_image_grid(images, path)`;
       - `plot_loss({label: [loss]}, path)`.
     - Chat yang sudah memuat konteks PRD, notebook ketua, dan kode B dipakai supaya kontrak antar-bagian tidak meleset.
   - Output Model (giliran 75):
     - LLM merakit `notebooks/A.ipynb` (23 sel; 7 sel salinan ketua berlabel SALINAN SEMENTARA). Isinya:
       - Kelas `ImagesOnly`: membungkus MNIST dan membuang label, sehingga tiap item hanya gambar.
       - `get_dataloader(cfg)`:
         - `datasets.MNIST(download=True)`;
         - `ToTensor()` lalu `Normalize((0.5,), (0.5,))` untuk rentang [-1, 1];
         - mode smoke memakai `Subset` berisi `SMOKE_SUBSET_SIZE` gambar pertama;
         - batch size dan num_workers dibaca dari `cfg`;
         - data tidak dipindah ke device.
       - `save_image_grid(images, path)`: detach, pindah ke CPU, clamp, ubah [-1, 1] ke [0, 1], `make_grid`, simpan PNG, tampilkan di notebook.
       - `plot_loss(series, path)`: menerima dict `{label: [loss]}` (bisa beberapa seri) atau list biasa, menyimpan grafik, lalu menampilkannya.
       - Sel uji:
         - shape (64, 1, 28, 28), float32, rentang [-1, 1], tanpa label, tetap di CPU, 60.000 gambar;
         - mode smoke 512 gambar dengan shape sama dan `config` tidak berubah;
         - contoh 8 digit;
         - uji `save_image_grid` dan `plot_loss` ke folder sementara.
     - Sebelum dikirim, LLM menguji notebook dengan file MNIST tiruan (format biner sama) karena jaringannya tidak bisa mengunduh MNIST. LLM juga menjalankan kode B memakai fungsi A asli: semua uji B lolos, jadi bentuk fungsi A dan B cocok.
     - Hasil di laptop saya (giliran 128–133; Windows, Python 3.14.10, torch 2.14.0+cpu): MNIST asli terunduh, 8 digit tampil, mode smoke 512 gambar / 8 batch, dan muncul `dataset OK`, `save_image_grid OK`, `plot_loss OK`, `visualize OK`.

2. TAHAP PENANGANAN EROR / DEBUGGING
   - Pesan Eror dari Notebook / Terminal:
     1. (giliran 84–95) Versi Python tidak sesuai PRD. Hasil `py -0` hanya menampilkan Python 3.13 dan 3.13t (free-threaded), padahal PRD mewajibkan 3.14.
     2. (giliran 100–103) Saat mengecek instalasi torch:
        ```
        SyntaxError: invalid syntax
        ```
        Penyebabnya ada teks `` `.git `` yang ikut tersalin di akhir perintah `python -c "..."`.
     3. (giliran 114–117) VS Code membuka folder dalam Restricted Mode, sehingga notebook tidak bisa dijalankan.
     4. (giliran 118–127) Pilihan "Python Environments" tidak muncul saat Select Kernel.
     5. (giliran 136–141) `git status` menampilkan `modified: notebooks/azigha_(ketua).ipynb`, padahal file milik ketua tidak sengaja diubah.
   - Prompt Perbaikan ke LLM: mengirim screenshot terminal / VS Code di setiap langkah dan bertanya "ini kenapa?", "yang mana?", atau "klo gini?".
   - Analisis & Solusi Kelompok:
     1. Menginstal Python 3.14.10 (64-bit, bukan free-threaded) dari python.org, lalu membuat venv dengan `py -3.14 -m venv venv`.
     2. Menjalankan ulang perintah cek tanpa teks tambahan. Hasilnya `2.14.0+cpu 0.29.0+cpu`. Pelajaran: torch sudah terpasang dengan benar; error-nya hanya salah salin perintah.
     3. Memilih Trust untuk folder repo.
     4. Menginstal extension Python dan Jupyter (Microsoft) di VS Code, lalu memilih kernel `venv (3.14.10)`.
     5. Menjalankan `git restore "notebooks/azigha_(ketua).ipynb"` supaya file ketua kembali seperti semula. Hanya `notebooks/A.ipynb` yang di-commit (output dikosongkan), dan folder `data/` tidak ikut karena sudah diabaikan `.gitignore`. Push ke branch `teman-a-syaikha` berhasil.
