# Log Interaksi Teman B

LOG INTERAKSI LLM - KELOMPOK Mini DDPM
- Nama Sesi: 01_2026-11-01_experiments-train-sample
- Tanggal Sesi: 01/11/2026
- Target Modul: Bagian 8-13 notebook (EXPERIMENTS, train, sample, eksekusi baseline, eksperimen dan hasil)
- Tautan Sesi Chat: (https://claude.ai/share/b089d29b-705f-4587-ac27-99a77ee326bf)

KRONOLOGI PROMPT & RESPONS:
1. TAHAP INISIASI (Meminta Kode Awal)
   - Prompt Kelompok: "Halo, saya Gita, Teman B dalam kelompok 3 orang untuk tugas besar Mini DDPM pada MNIST. Terlampir PRD kelompok (acuan utama; kalau berbeda dengan file lain, ikuti PRD) dan notebook ketua (contoh gaya sel, berisi config, utils, model, dan diffusion).

Tolong kerjakan hanya jobdesk Teman B di PRD: experiments (EXPERIMENTS), train, sample, eksekusi baseline (bagian 12), serta eksperimen dan hasil (bagian 13), masing-masing dengan sel ujinya.

Konteks: laptop saya hanya untuk smoke test (CPU atau Colab). Training penuh dijalankan ketua di GPU. Jadi kode harus:
- jalan di device apa pun lewat get_device(), tanpa device tetap;
- lolos uji dalam mode smoke test, yaitu SMOKE_TEST, SMOKE_SUBSET_SIZE, SMOKE_EPOCHS, SMOKE_SAMPLE_EVERY dari config;
- bisa dijalankan orang lain cukup dengan train("nama_konfigurasi") dan sample(path_checkpoint);
- mencetak waktu per epoch supaya durasi training penuh bisa diperkirakan.

Aturan:
- Semua kode di sel notebook, tanpa file .py dan tanpa import antar-file.
- Satu sel kode maksimal sekitar 30 baris, isinya satu fungsi, satu kelas, atau satu langkah.
- Sel markdown 1-3 kalimat, bahasa santai seperti mahasiswa menjelaskan ke teman.
- Nama fungsi, bentuk data, dan atribut config harus persis seperti PRD. Tidak ada angka tetap di luar config dan EXPERIMENTS.
- Konfigurasi di EXPERIMENTS hanya boleh menimpa learning rate dan/atau T, satu variabel per eksperimen. Nilai T harus lebih dari 20 karena Diffusion menolak T yang terlalu kecil.
- Nilai efektif dipakai sebagai salinan lokal. config tidak boleh berubah setelah train dijalankan.
- Checkpoint hanya berisi tipe yang aman untuk torch.load(weights_only=True): state_dict model, T, MODEL_PARAMS, epoch, dan state_dict optimizer. Jangan simpan objek config atau Path. Nama file checkpoint memuat nama konfigurasi.
- Selain grafik, train menyimpan catatan loss per epoch ke file JSON di results/loss_curves/, supaya bagian 13 bisa membandingkan hasil tanpa melatih ulang.

Untuk uji, salin sementara semua sel ketua yang dibutuhkan beserta helper-nya: BASE_DIR, config, set_seed, get_device, _group_norm, SinusoidalTimeEmbedding, ResBlock, Downsample, Upsample, UNet, _extract, Diffusion. Bagian Teman A belum jadi, jadi buat pengganti sederhana:
- get_dataloader yang menghasilkan tensor acak (B,1,28,28) dalam [-1,1] tanpa label;
- save_image_grid dan plot_loss versi minimal.
Semua sel salinan dan pengganti diberi label "SALINAN SEMENTARA, jangan dimasukkan ke notebook final".

Jangan tulis kode dulu. Tampilkan daftar sel (nomor, jenis, judul, isi satu kalimat, dan total sel), lalu tunggu persetujuan saya. Setelah saya setujui, tampilkan semua kode di chat sebagai blok kode per kelompok sel, tanpa file atau artifact."
   - Alasan Khusus:
     - Laptop saya hanya CPU, jadi kode harus lolos smoke test di device apa pun. Training penuh dijalankan ketua di GPU.
     - Bagian Teman A belum jadi, jadi get_dataloader, save_image_grid, dan plot_loss diganti versi data acak berlabel SALINAN SEMENTARA.
     - Isi checkpoint dibatasi ke tipe sederhana supaya bisa dimuat dengan weights_only=True.
     - Loss disimpan ke JSON supaya bagian 13 bisa membandingkan eksperimen tanpa melatih ulang.
     - Daftar sel diminta dulu supaya strukturnya bisa dicek sebelum kode ditulis.
   - Output Model:
     - Daftar 50 sel. LLM juga menandai masalah desain: sel uji train bisa memicu training penuh dua kali di notebook final. Solusinya `train(name="baseline", smoke=None)`, dan sel uji selalu memanggil `smoke=True`.
     - Usulan yang saya setujui (dengan tambahan saya):
       - EXPERIMENTS: baseline, lr_1e-4, lr_5e-4, T_250, T_500 (satu variabel per eksperimen).
       - Satu checkpoint per konfigurasi (`ddpm_<nama>.pt`).
       - Akhiran `_smoke` untuk output uji.
       - Override CPU: `SMOKE_TEST=True`, `NUM_SAMPLE_IMAGES=4`, `T=50`.
     - Kode utama:
       - `_resolve_run` membuat salinan lokal config dengan timpaan LR/T, sehingga config asli tidak berubah.
       - `train` menjalankan loop: t acak, add_noise, prediksi noise, MSE, Adam. Fungsi ini menyimpan checkpoint dengan 5 kunci dan JSON loss tiap epoch, serta membuat grid tiap N epoch.
       - `sample(path_checkpoint)` membangun ulang UNet dan Diffusion dari isi checkpoint.

2. TAHAP PENANGANAN EROR / DEBUGGING
   - Pesan Eror dari Notebook: "The Kernel crashed while executing code in the current cell or a previous cell." Log Jupyter: `Disposing session as kernel process died ExitCode: 3221225477`. Terjadi saat Run All pertama di laptop (Windows, CPU, Python 3.14.10, torch 2.14.0+cpu), sekitar 16 detik setelah kernel start, saat sel uji train mulai jalan.
   - Prompt Perbaikan ke LLM: "Waktu Run All pertama, kernel sempat crash [...] ExitCode: 3221225477 [...] Aku pasang faulthandler lalu jalankan sel satu per satu, dan crash-nya tidak muncul lagi. 1. Exit code itu artinya apa dan kemungkinan penyebabnya? 2. Apakah ada yang perlu diubah di kode B? 3. Kalau crash lagi di laptop ketua (GPU), apa yang sebaiknya dicek?"
   - Analisis & Solusi Kelompok:
     - Exit code 3221225477 = 0xC0000005 (access violation). Proses mati di kode native (torch/numpy/OpenMP), bukan karena error di logika Python.
     - Setelah faulthandler dipasang dan sel dijalankan satu per satu, crash tidak terulang. Run All berikutnya lolos sampai "eksperimen OK".
     - Penyebab tidak teridentifikasi karena crash tidak bisa direproduksi, jadi kode tidak diubah. Workaround seperti `KMP_DUPLICATE_LIB_OK=TRUE` juga tidak dipakai karena bisa menyembunyikan masalah.
     - Catatan untuk ketua: `train` belum bisa resume. Kalau crash di tengah run penuh, eksperimen harus diulang dari awal.
