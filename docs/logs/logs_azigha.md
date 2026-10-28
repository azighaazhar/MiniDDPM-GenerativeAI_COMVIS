# Log Interaksi Ketua

LOG INTERAKSI LLM - KELOMPOK [ISI nama kelompok]
- Nama Sesi: 01_2026-10-24_perencanaan-prd
- Tanggal Sesi: [28/10/2026]
- Target Modul: Perencanaan dan PRD
- Tautan Sesi Chat: (https://claude.ai/share/b7b6fba3-43da-4edf-9064-a420d44c70ee)

KRONOLOGI PROMPT & RESPONS:
1. TAHAP INISIASI (Meminta Kode Awal)
   - Prompt Kelompok: "Halo, saya ketua Kelompok Mini DDPM dan ada 2 orang anggota lagi, untuk tugas besar mata kuliah ini. Terlampir PDF panduannya. Kami sudah memilih membangun Mini Diffusion Model (DDPM) dengan dataset MNIST ukuran 28x28, memakai Python dan PyTorch. Tolong baca PDF-nya dulu, lalu jelaskan dengan bahasa sederhana: (1) apa yang sebenarnya diminta, (2) apa saja aturan dan larangannya, (3) bagaimana tugas ini dinilai. Jangan buat kode, PRD, atau struktur folder dulu. Saya mau memastikan pemahaman kita sama."
   - Alasan Khusus: Meminta ringkasan dulu agar pemahaman tentang tugas sama sebelum merancang apa pun. Setelah itu meminta draft PRD yang memuat aturan, pembagian file, dan kontrak data antar modul.
   - Output Model: Ringkasan isi PDF (aturan, larangan, rubrik) dan draft PRD, lalu paket final berisi bagian umum dan jobdesk tiap anggota.

2. TAHAP PENANGANAN EROR / DEBUGGING
   - Pesan Eror dari Notebook: tidak ada error notebook karna belum inisialisasi apapun
   - Prompt Perbaikan ke LLM: "[ISI prompt koreksimu. Intinya: peran dibagi A dan B, buang tambahan di luar ruang lingkup, buat versi ringkas hanya teknis]"
   - Analisis & Solusi Kelompok: "Aman terkendali"

---

- Nama Sesi: 02_2026-10-24_config-utils-diffusion
- Tanggal Sesi: [28/10/2026]
- Target Modul: config.py, utils.py, diffusion.py
- Tautan Sesi Chat: (https://claude.ai/share/8fa3cc9e-67ea-469d-8869-1423e5cf25e9)

KRONOLOGI PROMPT & RESPONS:
1. TAHAP INISIASI (Meminta Kode Awal)
   - Prompt Kelompok: "Saya ketua kelompok 3 orang untuk tugas besar ini. Terlampir PDF panduan dan PRD kelompok. Peran saya: Ketua, memegang config.py, utils.py, model.py, diffusion.py. Tolong ikuti PRD.

Tugas sesi ini: config.py dan utils.py.

STRUKTUR: Repo sudah ada. Sesuai Bagian 6 PRD, kedua file diletakkan langsung di root repo, tanpa folder src/. Jangan membuat folder atau file lain. Uji kecil cukup di blok if __name__ == "__main__" di masing-masing file.

HARDWARE: Kode ditulis di MacBook M3 (8GB memori gabungan) hanya untuk uji alur. Training penuh dijalankan di laptop GPU NVIDIA GTX 1650 Ti (4GB VRAM), uji memorinya baru bisa dilakukan di sana.

config.py:
- Konstanta tingkat modul, dikelompokkan dengan komentar, tanpa dataclass. Satu-satunya tempat nilai disimpan.
- SEED = 42; LEARNING_RATE = 2e-4; T = 1000.
- BATCH_SIZE = 64 dan EPOCHS = 30 sebagai nilai SEMENTARA, beri komentar bahwa belum final (menunggu uji memori) dan jangan dipakai untuk eksperimen tuning.
- BETA_START = 1e-4 dan BETA_END = 0.02, komentar "acuan untuk T=1000". Keputusan penyesuaian beta saat T berubah ditunda ke sesi diffusion.py.
- MODEL_PARAMS sebagai dict (channel input 1, base channels 64, multiplier (1, 2, 2) untuk dua downsampling 28→14→7, dimensi time embedding 128), supaya bisa dipakai UNet(**MODEL_PARAMS) dan disimpan di checkpoint.
- NUM_WORKERS = 0.
- Smoke test: SMOKE_TEST flag, subset 512 gambar, SMOKE_EPOCHS = 2, SMOKE_SAMPLE_EVERY = 1.
- SAMPLE_EVERY_N_EPOCHS = 5 dan NUM_SAMPLE_IMAGES = 16.
- Path (DATA_DIR, CHECKPOINT_DIR, RESULTS_DIR, loss_curves, samples) dihitung dari lokasi config.py memakai Path(__file__).resolve().parent.

utils.py:
- set_seed(seed): random, numpy, torch.manual_seed. Tanpa mode deterministik penuh.
- get_device(): cuda, lalu mps, lalu cpu. Fungsi murni tanpa print, satu-satunya tempat device ditentukan.

Format: tulis kodenya modular, diberi komentar, tanpa menyalin dari tutorial. Jelaskan singkat rencananya dulu, lalu kodenya, lalu cara mengujinya."
   - Alasan Khusus: Meminta penjelasan konsep (noise schedule, alpha-bar, sampling) sebelum kode supaya kami paham dulu. Hardware disebutkan agar BATCH_SIZE dan EPOCHS dibuat nilai sementara, karena uji memori hanya bisa dilakukan di laptop training.
   - Output Model: config.py (nilai baseline, MODEL_PARAMS, path), utils.py (set_seed, get_device cuda lalu mps lalu cpu), diffusion.py (noise schedule dengan beta diskalakan 1000/T, add_noise, sample_timesteps, sample) beserta uji di blok main.

2. TAHAP PENANGANAN EROR / DEBUGGING
   - Pesan Eror dari Notebook: Tidak ada error. Semua uji di blok main lolos, namun ada kesalahan permintaan yang dimana seharusnya AI tidak memberikan BETA_REFERENCE_T = 1000 dan Image_SIZE = 28 ke diffusion.py karena saya meminta inisialisasinya di config.py
   - Prompt Perbaikan ke LLM: "Pindahkan BETA_REFERENCE_T = 1000 dan IMAGE_SIZE = 28 ke config.py, lalu ganti di diffusion.py dengan config.BETA_REFERENCE_T dan config.IMAGE_SIZE."
   - Analisis & Solusi Kelompok: dua angka itu dipindah karena PRD mewajibkan semua angka dibaca dari config.py, jadi cukup diubah di satu tempat dan tidak ada nilai ganda di dua file.

---

- Nama Sesi: 03_2026-10-24_model-unet
- Tanggal Sesi: [28/10/2026]
- Target Modul: model.py (timestep embedding sinusoidal dan U-Net)
- Tautan Sesi Chat: (https://claude.ai/share/ee1dfdad-008c-4ffa-b143-099369c60048)

KRONOLOGI PROMPT & RESPONS:
1. TAHAP INISIASI (Meminta Kode Awal)
   - Prompt Kelompok: "Saya ketua kelompok 3 orang untuk tugas besar ini. Terlampir PDF panduan, PRD, dan config.py, utils.py, diffusion.py yang sudah jadi dan lolos uji. Tolong ikuti PRD.

Tugas sesi ini: model.py di root repo, tanpa file lain.

Isi: timestep embedding sinusoidal, blok dasar U-Net, dan UNet lengkap dengan skip connection dan dua downsampling (28 → 14 → 7). Konstruktor UNet harus menerima argumen yang cocok dengan kunci MODEL_PARAMS di config.py (UNet(**MODEL_PARAMS)). Input (x, t): x berbentuk (B, 1, 28, 28), t berbentuk (B,) bertipe long. Output: prediksi noise (B, 1, 28, 28).

Sebelum kode, jelaskan dulu dengan bahasa sederhana: apa itu timestep embedding dan mengapa disuntikkan ke blok U-Net, serta fungsi skip connection.

Uji di blok if __name__ == "__main__": shape output sama dengan input, jumlah parameter dicetak, dan satu langkah backward berjalan tanpa error. Pakai input acak.

Komentar di kode seperlunya saja. Tampilkan kode langsung di chat, bukan file unduhan. Jangan menyalin dari tutorial."
   - Alasan Khusus: Konstruktor UNet harus cocok dengan kunci MODEL_PARAMS agar model bisa dibangun ulang dari checkpoint. Uji yang diminta: shape output, pengaruh t, dan satu langkah backward.
   - Output Model: SinusoidalTimeEmbedding, ResBlock, Downsample, Upsample, dan UNet dengan dua downsampling (28 → 14 → 7) dan skip connection. Jumlah parameter 2.933.953.

2. TAHAP PENANGANAN EROR / DEBUGGING
   - Pesan Eror dari Notebook: Tidak ada error. Hasil uji shape (4,1,28,28) ke (4,1,28,28), pengaruh t OK, backward OK, model.py OK.
   - Prompt Perbaikan ke LLM: -
   - Analisis & Solusi Kelompok: "Aman terkendali"