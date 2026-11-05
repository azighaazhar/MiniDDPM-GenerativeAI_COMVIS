haloo

Halo! 👋 Ada yang bisa saya bantu hari ini?

Halo, saya ketua Kelompok Mini DDPM dan ada 2 orang anggota lagi, untuk tugas besar mata kuliah ini. Terlampir PDF panduannya. Kami sudah memilih membangun Mini Diffusion Model (DDPM) dengan dataset MNIST ukuran 28x28, memakai Python dan PyTorch. Tolong baca PDF-nya dulu, lalu jelaskan dengan bahasa sederhana: (1) apa yang sebenarnya diminta, (2) apa saja aturan dan larangannya, (3) bagaimana tugas ini dinilai. Jangan buat kode, PRD, atau struktur folder dulu. Saya mau memastikan pemahaman kita sama.

Menyusun draf PRD singkat berdasarkan asumsi dan risiko.
Asumsi kalian wajar dan bisa dipertanggungjawabkan, selama dituliskan secara eksplisit di laporan.

Penilaian asumsi dan risikonya
1. Tiga anggota, peran Anggota 4 digabung ke ketua. Ini masuk akal karena kelompok kalian memang kurang satu orang. Risikonya:

Beban ketua menjadi berat (Prompt Engineer, Documentarian, dan Error Handler sekaligus). Dokumentasi bernilai 25%, jadi log yang bolong akan langsung mengurangi nilai.
Penilaian kerja sama melihat Git commit atau log kerja, dan penguasaan individu dinilai saat presentasi. Jika semua dokumentasi dan debugging hanya tampak dikerjakan ketua, anggota lain bisa terlihat kurang berkontribusi.
Mitigasi: ketua tetap mengompilasi log, tetapi tiap anggota mengisi log untuk sesi LLM miliknya sendiri. Semua anggota juga ikut meng-commit ke Git.
2. Boleh memakai torch.nn, tetapi U-Net, noise schedule, dan timestep embedding disusun sendiri. Ini batas yang paling masuk akal, karena PDF sendiri mengizinkan dokumentasi PyTorch sebagai referensi fungsi dasar. Risikonya adalah dosen atau penilai punya tafsir “from scratch” yang lebih ketat. Mitigasi:

Jangan memakai library difusi jadi (misalnya diffusers atau paket DDPM siap pakai) maupun bobot pretrained.
Tulis batas ini di laporan, misalnya “Komponen yang kami bangun sendiri vs. yang memakai torch.nn”.
Pastikan semua anggota bisa menjelaskan isi U-Net dan rumus noise schedule tanpa membuka kode.
3. “Fine-tuning” = eksperimen tuning learning rate, batch size, dan jumlah timestep. Ini tafsir yang paling logis untuk model yang dilatih dari nol. Risikonya, penilai mungkin mengharapkan fine-tuning dalam arti sebenarnya (melanjutkan model yang sudah dilatih). Mitigasi: jika waktu dan tenaga cukup, tambahkan satu eksperimen kecil opsional, misalnya melanjutkan pelatihan model pada subset tertentu. Itu menutup kedua tafsir tanpa menambah banyak pekerjaan.

Saran umum: karena dosen tidak bisa ditanya lagi, simpan keputusan ini sebagai bagian laporan bernama “Asumsi & Batasan Proyek”, lengkap dengan alasannya. Itu menunjukkan kalian sadar akan ambiguitasnya dan memilih secara rasional.

Draft PRD: Mini DDPM pada MNIST
1. Tujuan
Membangun model difusi (DDPM) skala kecil dari nol yang mampu menghasilkan digit tulisan tangan 28x28 dari noise murni, menggunakan Python dan PyTorch, dengan seluruh proses dikerjakan lewat vibe coding dan terdokumentasi lengkap.

2. Ruang lingkup

Termasuk:

Data pipeline MNIST (normalisasi ke rentang [-1, 1], DataLoader).
Noise schedule (forward process) dan timestep embedding buatan sendiri.
Arsitektur U-Net kecil untuk memprediksi noise.
Training loop dengan loss MSE antara noise asli dan noise prediksi.
Sampling (reverse process) untuk menghasilkan gambar.
Eksperimen tuning: learning rate, batch size, jumlah timestep.
Log interaksi LLM, grafik metrik, laporan akhir, dan presentasi.
Tidak termasuk:

Library difusi jadi atau bobot pretrained.
Dataset selain MNIST (kecuali fine-tuning opsional).
Conditional generation (opsional, jika waktu tersisa).
3. Kebutuhan fungsional

F1: Dataset termuat dengan shape dan rentang nilai yang benar.
F2: Forward process dapat menambahkan noise pada timestep t sembarang, dan hasilnya bisa divisualisasikan.
F3: U-Net menerima gambar ber-noise dan timestep, lalu mengeluarkan prediksi noise dengan shape yang sama.
F4: Training berjalan tanpa error dan mencatat loss per epoch.
F5: Sampling menghasilkan grid gambar dari noise acak.
F6: Checkpoint model dapat disimpan dan dimuat ulang.
4. Eksperimen tuning

Variabel	Contoh variasi
Learning rate	3 nilai (mis. kecil, sedang, besar)
Batch size	2–3 nilai
Jumlah timestep (T)	2–3 nilai
Setiap eksperimen mengubah satu variabel dalam satu waktu, dan hasilnya dicatat dalam tabel dan grafik.

5. Metrik dan bukti keberhasilan

Kurva training loss yang menurun dan stabil.
Grid sampel gambar dari tiap konfigurasi, dibandingkan secara visual.
Tambahan opsional: akurasi klasifikator MNIST sederhana terhadap gambar hasil generate sebagai ukuran kualitas kasar.
6. Pembagian peran (3 orang)

Peran	Tanggung jawab
Ketua	Prompt engineer, arsitektur, kompilasi log, laporan akhir
Anggota 2	Data pipeline dan preprocessing, evaluasi visual sampel
Anggota 3	Training loop, tuning hyperparameter, pencatatan metrik, bersama ketua menangani debugging
Semua anggota mengisi log untuk sesi LLM masing-masing dan melakukan commit Git.

7. Deliverables

Kode (repositori Git dengan riwayat commit dari semua anggota).
Log Interaksi LLM (format templat dosen) dan tautan atau ekspor chat.
Grafik metrik dan hasil sampling.
Laporan akhir, termasuk bagian “Asumsi & Batasan”.
Presentasi.
8. Tahapan kerja

Persiapan: finalisasi PRD dan setup lingkungan.
Data pipeline dan forward process.
U-Net dan timestep embedding.
Training loop dan sampling.
Eksperimen tuning.
Dokumentasi, laporan, dan latihan presentasi.
9. Risiko utama

Risiko	Mitigasi
Training lambat atau tanpa GPU	Model kecil, subset data untuk uji awal, Google Colab/Kaggle
Hasil sampel berupa noise	Cek forward process dan normalisasi dulu, lalu timestep embedding dan skala learning rate
Log tidak lengkap	Isi log di akhir setiap sesi, bukan di akhir proyek
Anggota tidak menguasai seluruh kode	Sesi saling menjelaskan sebelum presentasi
10. Kriteria selesai
Model menghasilkan digit yang dapat dikenali, eksperimen tuning terdokumentasi dengan grafik, log LLM lengkap dengan kronologi inisiasi → debugging → optimasi, dan semua anggota dapat menjelaskan seluruh alur.

Kalau PRD ini sudah sesuai, langkah berikutnya bisa berupa penyusunan system prompt awal untuk LLM, atau strategi tahapan prompt per modul agar variasi prompt kalian baik untuk penilaian vibe coding. Mana yang ingin kalian kerjakan dulu?

PRD-nya hampir sesuai, tapi ada beberapa koreksi. (1) Peran Anggota 4 tidak digabung ke saya. Teman A memegang dataset dan mengompilasi log semua anggota. Teman B memegang training, sampling, dan eksperimen tuning. Saya memegang model, noise schedule, dan integrasi. Tiap orang men-debug modulnya sendiri. (2) Ukuran gambar 28x28, jadi U-Net maksimal dua level downsampling (28→14→7). (3) Hapus fine-tuning opsional, classifier, dan conditional generation dari ruang lingkup. (4) Batasi eksperimen jadi dua variabel saja supaya muat di GPU kami. Tolong revisi PRD-nya dan tandai bagian mana yang berasal dari PDF dan mana yang asumsi. Nah setelah ini kita jangan generate prd dlu, Kita rencanakan detail dulu bagian saya (ketua) apa teman A apa dan teman B sebagai apa.

Revisi PRD: Mini DDPM pada MNIST
Label: [PDF] = berasal dari panduan, [Keputusan] = keputusan kelompok kalian, [Asumsi] = usulan saya yang belum kalian konfirmasi.

1. Tujuan

Membangun model generatif dari nol, dikerjakan lewat vibe coding dan terdokumentasi [PDF].
Model yang dipilih adalah Mini DDPM, dengan tantangan noise schedule dan timestep embedding [PDF].
Dataset MNIST 28x28, Python, PyTorch [Keputusan].
2. Ruang lingkup

Termasuk:

Data pipeline dan preprocessing [PDF]. Normalisasi ke rentang [-1, 1] [Asumsi].
Noise schedule dan timestep embedding buatan sendiri [PDF + Keputusan]. Bentuk sinusoidal untuk embedding [Asumsi].
U-Net dengan maksimal dua level downsampling (28→14→7) [Keputusan].
Training loop dengan loss MSE antara noise asli dan noise prediksi [Asumsi], berdasarkan rumus DDPM standar.
Sampling (reverse process) untuk menghasilkan gambar [Asumsi].
Eksperimen tuning dengan dua variabel [Keputusan].
Log interaksi LLM, grafik metrik, laporan, dan presentasi [PDF].
Tidak termasuk [Keputusan]:

Fine-tuning opsional.
Classifier evaluasi.
Conditional generation.
Library difusi jadi dan bobot pretrained [Asumsi].
3. Aturan dan batasan

Dilarang copy-paste tutorial atau GitHub orang lain [PDF].
Riwayat chat dilampirkan sebagai share link atau ekspor [PDF].
Error wajib dikonsultasikan ke LLM dan dicatat di log [PDF].
Boleh memakai torch.nn, tetapi U-Net, noise schedule, dan timestep embedding disusun sendiri [Keputusan].
“Fine-tuning” ditafsirkan sebagai eksperimen tuning hyperparameter [Keputusan].
Keduanya dicatat di bagian “Asumsi & Batasan” laporan [Asumsi].
4. Pembagian peran [Keputusan]

Orang	Cakupan
Ketua	Model (U-Net), noise schedule, timestep embedding, integrasi
Teman A	Dataset dan kompilasi log semua anggota
Teman B	Training, sampling, eksperimen tuning
Tiap orang men-debug modulnya sendiri [Keputusan]. Semua anggota commit ke Git [PDF: dinilai lewat commit/log kerja].

5. Eksperimen tuning

Jumlah variabel dibatasi dua [Keputusan].
Usulan saya: learning rate dan jumlah timestep (T), dengan batch size dikunci satu nilai yang aman di GPU [Asumsi]. Alasannya, batch size paling langsung memengaruhi memori GPU, sehingga mengunci batch size paling menghemat risiko.
Satu variabel diubah dalam satu waktu [Asumsi].
Karena kalian awalnya mendefinisikan tuning dengan tiga variabel, tulis di laporan bahwa batch size dikunci karena keterbatasan GPU.
6. Bukti keberhasilan

Grafik metrik training yang valid [PDF].
Luaran model logis dan model berjalan tanpa error [PDF].
Grid sampel per konfigurasi untuk perbandingan visual [Asumsi].
7. Deliverables

Kode di Git, Log Interaksi (templat dosen), tautan atau ekspor chat, grafik metrik, laporan, presentasi [PDF].
Bagian “Asumsi & Batasan” di laporan [Asumsi].
8. Kriteria selesai
Mengikuti rubrik: vibe coding 30%, log 25%, fungsionalitas 25%, kerja tim 20% [PDF]. Tambahan: semua anggota bisa menjelaskan seluruh alur [PDF: penguasaan individu saat presentasi].

Perencanaan detail peran
Satu catatan dulu: PDF menaruh peran Prompt Engineer & LLM Navigator pada ketua. Saya asumsikan itu tetap kalian, jadi selain model dan integrasi, kalian juga menjaga konsistensi arahan ke LLM. Ini beban terberat secara teknis, jadi rencana di bawah sengaja membuat A dan B bisa mulai lebih dulu tanpa menunggu kalian.

Kontrak antarmuka (disepakati bertiga sebelum mulai)
Ini kunci supaya integrasi tidak macet [Asumsi]:

Data → Training: batch gambar berbentuk (B, 1, 28, 28), nilai di [-1, 1].
Schedule → Training/Sampling: objek yang menyediakan koefisien (beta, alpha, alpha-bar, dst.) dan fungsi penambah noise pada timestep tertentu.
Model → Training/Sampling: menerima gambar ber-noise dan timestep (tensor bilangan bulat, satu per gambar), mengeluarkan prediksi noise dengan shape sama dengan input.
Titik serah-terima yang perlu diputuskan: reverse step di sampling memakai koefisien dari schedule. Usul saya, kalian menyediakan koefisiennya dan B menulis loop sampling-nya.
Ketua: Model, schedule, integrasi
Modul: noise schedule, timestep embedding, U-Net (28→14→7, ukuran kecil agar muat GPU), dan penggabungan semuanya.
Peran PDF yang melekat: system prompt awal, strategi arsitektur ke LLM, menjaga konsistensi logika.
Rencana sesi LLM: (1) schedule dan rumus forward, (2) timestep embedding, (3) blok dasar U-Net, (4) skip connection dan penyusunan U-Net utuh, (5) uji shape dan integrasi. Variasikan jenis prompt: minta penjelasan konsep dulu, lalu kode, lalu minta LLM mengkritik kode sendiri.
Pengujian mandiri sebelum serah ke B: forward process divisualisasikan pada beberapa t, model diuji dengan input acak untuk memastikan shape output benar.
Harus bisa dijelaskan saat presentasi: mengapa noise ditambahkan seperti itu, apa itu alpha-bar, fungsi skip connection, alasan timestep disuntikkan ke U-Net.
Teman A: Dataset dan log
Modul: pemuatan MNIST, normalisasi, DataLoader, pemeriksaan shape dan rentang nilai, visualisasi contoh data.
Kompilasi log: mengumpulkan log dari semua anggota ke satu dokumen berformat templat dosen, memastikan setiap tautan chat aktif, dan menjaga kronologi inisiasi → debugging → optimasi.
Rencana sesi LLM: (1) data loader dan normalisasi, (2) verifikasi shape dan visualisasi. Sesi data akan sedikit, jadi A sebaiknya juga mengambil porsi evaluasi visual sampel dan penyusunan kerangka laporan agar beban seimbang [Asumsi].
Aturan kerja log: tiap anggota menulis log mentah sendiri di akhir setiap sesi, lalu A hanya merapikan dan menggabungkan. Tanpa aturan ini, A akan menjadi sumber kemacetan.
Harus bisa dijelaskan: mengapa normalisasi ke [-1, 1], bagaimana shape mengalir ke model.
Teman B: Training, sampling, tuning
Modul: training loop (loss, optimizer, pencatatan metrik, checkpoint), loop sampling, eksperimen tuning, grafik metrik.
Bisa mulai lebih awal: B dapat menyusun training loop memakai model tiruan sederhana (hanya untuk menguji alurnya) selagi kalian mengerjakan U-Net, lalu diganti model asli saat siap.
Rencana sesi LLM: (1) training loop, (2) pencatatan dan grafik metrik, (3) sampling, (4) desain dan eksekusi eksperimen tuning.
Harus bisa dijelaskan: mengapa loss-nya MSE terhadap noise, apa yang terjadi di tiap langkah sampling, mengapa learning rate dan T memengaruhi hasil.
Urutan kerja dan ketergantungan
Bertiga: sepakati kontrak antarmuka dan aturan log.
Paralel: A mengerjakan data, kalian mengerjakan schedule dan U-Net, B mengerjakan training loop dengan model tiruan.
Integrasi (dipimpin kalian): pasang model asli ke training B, uji pada data kecil (sekitar satu epoch pada subset) untuk memastikan loss turun.
B: sampling dan eksperimen tuning.
Bertiga: saling menjelaskan modul sebelum presentasi.
Hal yang perlu diputuskan
Dua variabel tuning (usul saya learning rate dan T) dan siapa yang menulis loop sampling (usul saya B).
Aturan debugging: karena tiap orang men-debug modulnya sendiri, error lintas modul (misalnya shape tidak cocok) sebaiknya ditangani oleh pemilik modul yang menerima input. Ini perlu kalian sepakati.
Untuk melanjutkan, apakah dua variabel tuning (learning rate dan T, dengan batch size dikunci) sudah sesuai dengan keinginan kelompok, atau kalian lebih memilih pasangan lain?

Revisi PRD-nya sudah sesuai. Saya kunci beberapa keputusan tambahan, lalu tolong buatkan paket final.

KEPUTUSAN KELOMPOK
1. Pembagian file, satu file satu pemilik:
   - Saya (ketua): model.py, diffusion.py, config.py, utils.py, dan integrasi. diffusion.py sepenuhnya milik saya, berisi noise schedule, forward process, dan fungsi sampling (reverse process).
   - Teman A: dataset.py, scripts/check_data.py, dan mengompilasi Log Interaksi semua anggota.
   - Teman B: train.py, sample.py, eksperimen tuning, dan grafik metrik. sample.py hanya memuat checkpoint, memanggil fungsi sampling dari diffusion.py, lalu menyimpan gambar.
2. Debugging: tiap orang men-debug modulnya sendiri. Error lintas modul ditangani pemilik modul yang menerima input, dan penemu error mencatatnya di log miliknya.
3. Training penuh dijalankan di laptop NVIDIA milik salah satu anggota (ditentukan nanti). Batch size dan jumlah epoch disimpan di config.py dan ditentukan setelah uji memori.
4. train.py menyimpan checkpoint berkala dan di akhir training. Hasil training (grafik loss dan gambar sampel) di-commit ke repo. Checkpoint tidak di-commit dan hanya dibagikan jika dibutuhkan.
5. Semua anggota memakai satu seed dan satu config.py yang dipegang saya. Versi Python dan PyTorch diseragamkan di requirements.txt.
6. Git: tiap anggota commit ke branch sendiri, saya yang menggabungkan ke main.
7. Tersedia mode smoke test di config.py (subset data kecil, satu atau dua epoch) untuk uji cepat tanpa GPU.
8. Dataset MNIST 28x28, U-Net maksimal dua level downsampling (28→14→7), dua variabel tuning (learning rate dan jumlah timestep, batch size dikunci).

YANG SAYA MINTA
Buat paket final dalam Markdown yang tidak bergantung pada satu LLM:
(a) PRD final dengan keputusan terkunci dan label [PDF], [Keputusan], [Asumsi].
(b) Struktur folder repo lengkap, dengan pemilik tiap file.
(c) Jobdesk per orang: modul, input dan output, kontrak antarmuka dengan modul lain, dan apa yang harus bisa dijelaskan saat presentasi.
(d) Aturan kerja: log per anggota, commit Git, debugging, ekspor chat.

Pisahkan bagian per orang supaya tiap anggota bisa menempelkan bagiannya sendiri. Jangan menambah fitur di luar ruang lingkup, dan tandai jika ada yang kamu tambahkan sebagai asumsi.

Paket final sudah jadi di paket_final_mini_ddpm.md. Bagian C1, C2, dan C3 berdiri sendiri, jadi tiap anggota bisa menempelkan bagiannya sendiri bersama Bagian 0 (konteks bersama).

Ada beberapa hal yang saya tambahkan di luar keputusan kalian. Semuanya saya tandai [Asumsi] di berkas:

requirements.txt, README.md, dan .gitignore saya taruh di bawah kepemilikan kalian sebagai ketua.
utils.py saya isi seperlunya, yaitu pengaturan seed dan pemilihan device.
train.py yang menghitung loss MSE, sedangkan diffusion.py hanya menyediakan forward process dan sampling.
Folder results/ dan docs/chat_exports/, plus aturan penamaan ekspor chat.
Aturan kecil di Git: nama branch dan kebiasaan kalian bekerja lewat branch juga, supaya commit kalian terlihat setara dengan anggota lain.
Ada tujuh hal yang belum diputuskan, semuanya di Bagian E. Dua yang paling penting:

Laporan akhir dan presentasi belum punya penanggung jawab. Di PDF, peran Lead Documentarian mencakup laporan akhir, sedangkan keputusan kalian baru menetapkan kompilasi log untuk Teman A.
Cara Teman B mengubah learning rate dan T. config.py hanya kalian yang memegang, jadi B perlu jalur yang jelas untuk meminta perubahan. Usul saya: kalian menyediakan daftar konfigurasi eksperimen bernama di config.py, lalu train.py memilihnya berdasarkan nama.
Sebelum dibagikan ke Teman A dan B, sebaiknya kalian bertiga membaca Bagian E bersama dan memutuskan kedua poin itu. Mau kita bahas dulu, atau lanjut ke penyusunan system prompt awal untuk sesi LLM kalian?

Paketnya hampir final. Tolong revisi dengan keputusan berikut, dan tandai bagian yang berubah.

Eksperimen tuning: config.py milik saya hanya berisi nilai baseline. Teman B punya file sendiri (experiments.py) berisi daftar konfigurasi eksperimen bernama yang menimpa learning rate dan T. train.py memilih konfigurasi berdasarkan nama. Perbarui struktur folder, jobdesk B, dan Bagian E.
Checkpoint menyimpan bobot model, T, parameter pembentuk model, epoch, dan optimizer, supaya sample.py bisa membangun ulang model dengan benar.
DataLoader mengembalikan gambar saja (bukan pasangan gambar dan label). dataset.py memakai download=True.
[Laporan akhir: A menyusun kerangka, tiap anggota menulis bagian modulnya.] [Pemilik laptop training: ... / belum ditentukan.]
Tambahkan visualize.py milik Teman A: fungsi menyimpan grid gambar dan membuat grafik loss, dipanggil oleh train.py dan sample.py. Perbarui jobdesk A dan B.
Tambahkan bagian jadwal: tenggat [tanggal], dengan tahapan dan tanggal target per modul.
Beri label [Asumsi] pada larangan library difusi dan bobot pretrained di Bagian 0. Catat versi Python di README, bukan di requirements.txt. Sebutkan cara menjalankan scripts/check_data.py dari root repo.
Jangan menambah fitur di luar ruang lingkup.

Paket sudah direvisi di paket_final_mini_ddpm.md. Tabel “Ringkasan Perubahan” di bagian atas berkas memetakan tiap keputusan ke bagian yang terdampak. Perubahan di dalam isi ditandai [REVISI] dan [BARU].

Ada empat hal yang perlu kalian ketahui:

Tenggat dan tanggal target jadwal masih kosong. Kalian menulis [tanggal] tanpa isi, jadi saya tidak mengarang tanggal. Bagian F sudah berisi tahapan, pemilik, dan ketergantungannya. Kalian tinggal mengisi kolom tanggal.
Pemilik laptop training masih “belum ditentukan” di A3, D7, dan Bagian E. Versi Python juga masih kosong dan menunggu kalian mengisinya di README.
Perintah check_data.py saya tulis python -m scripts.check_data. Jika dijalankan dengan python scripts/check_data.py, file itu tidak bisa mengimpor dataset.py dan config.py di root. Perintah ini perlu Teman A cek di mesinnya sebelum masuk README.
Saya menambahkan beberapa butir kecil sebagai [Asumsi], semuanya terkait keputusan baru:
diffusion.py menerima T sebagai parameter, bukan membacanya langsung dari config.py, supaya T hasil timpaan experiments.py bisa dipakai.
Konfigurasi baseline selalu tersedia dan dipakai bila train.py dijalankan tanpa nama konfigurasi.
Nama file checkpoint memuat nama konfigurasi agar tidak saling menimpa.
torchvision dan matplotlib masuk requirements.txt, karena dibutuhkan untuk download MNIST dan grafik.
Folder docs/laporan/, dengan satu file bagian per anggota.
Satu hal lagi yang masih terbuka di Bagian E: apakah train.py juga boleh menyimpan grid sampel selama training. Usul saya tidak, supaya ruang lingkup tidak melebar, tetapi itu keputusan kalian.

Sebelum membagikan ke Teman A dan B, isi dulu tenggat dan tanggal target di Bagian F, lalu tentukan pemilik laptop.

Revisinya sudah sesuai. Keputusan saya untuk butir yang terbuka:
1. Butir E6: ya, train.py memanggil fungsi grid gambar tiap N epoch, N diatur di config.py.
2. Tenggat proyek: 1 November 2026. Hari ini 24 Oktober 2026. Isi Bagian F dengan tanggal target yang dihitung mundur dari tenggat, tahap 1a, 1b, dan 1c dimulai hari ini, dan sisakan waktu terpisah untuk laporan dan log.
3. Butir E4: tiap anggota menyiapkan slide untuk modulnya sendiri, dikerjakan di akhir.
4. Di Bagian F, Tahap 1c juga bergantung pada Tahap 1b. Teman B memakai data acak dan fungsi sementara sampai bagian A selesai.
5. Versi Python belum ditentukan. Ketua akan mengisinya di README. Di requirements.txt tambahkan baris komentar "WAJIB: Python [versi], lihat README" sebagai pengingat. Semua anggota wajib memakai versi yang sama.
6. Training penuh dan semua eksperimen dijalankan oleh Teman B di laptop miliknya (laptop training dengan GPU). Ini belum dikonfirmasi, jadi tulis sebagai butir terbuka dengan tenggat konfirmasi sebelum Tahap 4. Hapus penyebutan merek GPU di seluruh paket dan ganti dengan "laptop training".
7. Saya hanya menjalankan pengujian ringan di MacBook arm64 (CPU). Kode tidak boleh memakai device tetap, dan utils.py memilih device berurutan: cuda, mps, lalu cpu.
Tandai perubahan dengan [REVISI], dan jangan menambah fitur baru.

Paket sudah direvisi di paket_final_mini_ddpm.md. Tabel “Ringkasan Perubahan Revisi Ini” di bagian atas memetakan ketujuh keputusan ke bagian yang terdampak, dan tiap perubahan di dalam isi bertanda [REVISI]. Penyebutan merek GPU sudah dihapus dari seluruh paket dan diganti “laptop training”.

Ada empat hal yang perlu kalian tahu:

Device di MacBook kalian akan jadi mps, bukan cpu. Urutan cuda → mps → cpu di utils.py membuat MacBook arm64 yang mendukung mps memilih mps. Karena itu saya menaruhnya sebagai butir terbuka di Bagian E (butir 5). Kalau ada operasi yang tidak didukung mps, kelompok perlu memutuskan cara memaksa cpu. Saya tidak menambahkan fitur untuk itu.
Jadwal padat dan punya satu titik kritis. Hanya ada delapan hari, dan 28 Oktober memuat Tahap 3a, 3b, dan 4 sekaligus. Training dan eksperimen hanya punya dua hari (29–30 Oktober), jadi ukuran model, epoch, dan jumlah konfigurasi eksperimen harus disesuaikan setelah uji memori. Laporan dan log punya baris terpisah dari training. Kalian dan Teman A menulis bagian laporan dan log selagi Teman B menjalankan training, sedangkan bagian B ditulis 31 Oktober.
Konfirmasi laptop training Teman B jatuh 27 Oktober. Tahap 5 dan 6 tidak bisa mulai tanpa itu. Butir ini ada di Bagian E dan di jadwal.
Beberapa butir kecil saya tandai [Asumsi] karena turunan dari keputusan baru:
train.py mengalihkan model ke mode evaluasi sebelum membuat grid, lalu mengembalikannya.
visualize.py memindahkan tensor ke CPU sebelum menyimpan.
Checkpoint dimuat ke device hasil utils.py, supaya checkpoint dari laptop training bisa dibuka di MacBook.
Nilai N pada smoke test tidak boleh melebihi jumlah epoch smoke.
Latihan presentasi diasumsikan 1 November. Tanggal presentasi sebenarnya perlu kalian konfirmasi (Bagian E, butir 6).
Versi Python dan baris [versi] di requirements.txt masih kosong. Usul saya, kalian mengisinya hari ini di Tahap 0, supaya semua anggota memakai versi yang sama sejak awal.
Paketnya terlalu rumit. Tolong buat PRD final yang ringkas, bersih, dan hanya berisi hal teknis yang wajib. Dokumen ini akan saya kirim ke dua teman saya, yang masing-masing akan menempelkannya ke AI mereka dan berperan sebagai Teman A atau Teman B.

FORMAT
- Judul: "PRD Final: Mini DDPM pada MNIST". Jangan ada kata "revisi", nomor versi, atau tag [REVISI]/[BARU]. Dokumen harus terbaca seperti dokumen baru yang bersih.
- Paragraf pendek di paling atas tentang cara pakai: "Tempel bagian umum + jobdesk milikmu ke AI-mu. Bagian orang lain boleh dibaca, tapi tidak perlu ditempel."
- Bagian umum dan tiap jobdesk (ketua, Teman A, Teman B) harus berdiri sendiri, dengan judul yang jelas supaya mudah dipilih.
- Label [PDF], [Keputusan], [Asumsi] dipakai seperlunya dan singkat.

HAPUS
Jadwal, tanggal, tahapan per hari, butir belum diputuskan, semua penyebutan MacBook, laptop training, pemilik laptop, tanggal presentasi, slide, tabel risiko, dan checklist. Jangan membuat batasan waktu. Kerjakan secepat bisa selesai. Cukup satu kalimat urutan ketergantungan: data dan model dikerjakan paralel, training setelah keduanya jadi.

PERTAHANKAN
1. Konteks bersama: aturan proyek dan kontrak data antar modul.
2. Keputusan teknis: Mini DDPM, MNIST 28x28, U-Net maksimal dua level downsampling (28→14→7), dua variabel tuning (learning rate dan T), checkpoint berisi bobot, T, parameter model, epoch, dan optimizer, DataLoader hanya gambar dengan download=True, config.py hanya baseline dengan experiments.py milik Teman B, train.py menyimpan grid sampel tiap N epoch.
3. Struktur folder repo dan pemilik tiap file (satu file satu pemilik).
4. Jobdesk per orang: modul, input dan output, kontrak dengan modul lain, uji mandiri (misalnya uji shape dengan tensor acak), dan apa yang harus bisa dijelaskan saat presentasi.
5. Aturan kerja singkat: log per anggota (templat PDF), ekspor chat (link atau PDF), Git (branch sendiri, ketua menggabungkan ke main), debugging (pemilik modul yang menerima input).
6. Satu baris aturan device: utils.py memilih cuda, lalu mps, lalu cpu, dan tidak ada device tetap di kode.
7. Versi Python: 3.14 (ketua memakai 3.14.6). Semua anggota memakai versi yang sama, dicatat di README dan sebagai baris komentar di requirements.txt: "WAJIB: Python 3.14, lihat README".

Setelah ini, keluarkan versi akhirnya. Jangan menambah fitur, usulan, atau pertanyaan baru.

PRD final yang ringkas sudah jadi di prd_final_mini_ddpm.md, dengan struktur: Bagian Umum, lalu Jobdesk Ketua, Jobdesk Teman A, dan Jobdesk Teman B. Semua yang masuk daftar HAPUS sudah dibuang, dan semua yang masuk daftar PERTAHANKAN ada, termasuk Python 3.14 (ketua 3.14.6) dan baris komentar WAJIB: Python 3.14, lihat README.

Tiga hal yang perlu kalian ketahui:

Laporan akhir dan folder docs/laporan/ tidak masuk karena tidak ada di daftar PERTAHANKAN. Kalau kerangka laporan oleh Teman A masih berlaku, tambahkan sendiri satu baris di jobdesk A.
Smoke test tetap ada sebagai satu flag di config.py dan satu butir di uji mandiri A dan B. Itu keputusan teknis lama yang dipakai di dua jobdesk tersebut.
Perintah python -m scripts.check_data tetap ada di jobdesk Teman A (ditandai [Asumsi]), karena tanpa -m skrip itu tidak bisa mengimpor dataset.py di root.
Folder outputs juga masih berisi paket lama paket_final_mini_ddpm.md. Jangan kirim berkas itu ke teman kalian.

Repo GitHub kelompok sudah saya buat dan akan berisi struktur folder di PRD. Saya mau membuat file .gitignore. Tolong berikan isi .gitignore yang sesuai dengan proyek ini (Python, PyTorch, MNIST, dikerjakan di macOS dan Windows), dan jelaskan alasan tiap baris.

Pastikan sesuai keputusan PRD: data/ dan checkpoints/ tidak di-commit, sedangkan results/ (grafik loss dan gambar sampel) dan docs/ tetap di-commit. Jangan mengabaikan file yang harus ada di repo.

Ini isi .gitignore yang sesuai PRD:

# Data dan checkpoint (keputusan PRD: tidak di-commit)
/data/
/checkpoints/
*.pt
*.pth

# Python
__pycache__/
*.py[cod]
.venv/
venv/

# Jupyter/Colab
.ipynb_checkpoints/

# Editor
.vscode/
.idea/

# macOS
.DS_Store
._*

# Windows
Thumbs.db
desktop.ini
Alasan tiap baris
Baris	Alasan
/data/	Folder unduhan MNIST (download=True). Datanya bisa diunduh ulang dan ukurannya besar. Tanda / di depan membuat aturan hanya berlaku untuk folder data/ di root repo.
/checkpoints/	Checkpoint tidak di-commit, hanya dibagikan bila perlu (keputusan PRD). Ukurannya besar dan berubah tiap training.
*.pt, *.pth	Jaring pengaman: kalau ada yang menyimpan checkpoint di luar checkpoints/, file itu tetap tidak ikut ter-commit.
__pycache__/, *.py[cod]	Cache bytecode Python. Dibuat otomatis di setiap mesin dan berbeda antar versi Python.
.venv/, venv/	Virtual environment berisi paket terpasang. Yang dibagikan cukup requirements.txt.
.ipynb_checkpoints/	Salinan otomatis Jupyter. File .ipynb sendiri tidak diabaikan.
.vscode/, .idea/	Pengaturan pribadi editor, berbeda untuk tiap anggota.
.DS_Store, ._*	File metadata yang dibuat macOS di folder dan di drive eksternal.
Thumbs.db, desktop.ini	File metadata yang dibuat Windows.
Yang sengaja tidak diabaikan
results/ (grafik loss, gambar sampel, experiments.md) dan docs/ (log, chat export) tetap ter-commit. Karena itu tidak ada pola untuk *.png, *.jpg, *.md, atau *.pdf.
config.py, experiments.py, requirements.txt, dan semua kode tetap ter-commit.
Hal yang perlu diperhatikan
Path di config.py harus data/ dan checkpoints/ di root repo, supaya cocok dengan aturan di atas. Kalau path-nya beda, folder itu tidak terabaikan.
Folder yang diabaikan tidak ada setelah clone. torchvision membuat data/ sendiri saat mengunduh, tetapi train.py perlu membuat checkpoints/ bila belum ada. Informasikan ini ke Teman B.
Folder kosong tidak dilacak Git. results/loss_curves/ dan results/samples/ baru muncul di repo setelah ada file di dalamnya.
.gitignore tidak berlaku untuk file yang sudah terlanjur di-commit. Kalau data/ atau checkpoints/ sudah masuk, lepaskan dengan git rm -r --cached data checkpoints, lalu commit.
Untuk memeriksa hasilnya, jalankan:

git check-ignore -v data/MNIST checkpoints/model.pt results/samples/contoh.png
Dua path pertama akan tercetak beserta aturan yang mengabaikannya. Path ketiga tidak boleh tercetak, karena artinya results/ aman.

Coba cek, ini isi dari git ignorenya. Setelah ini apakah kita lanjut ke config dan utils.py yaa. Tpi anda jangan generate code dlu disini kita masi brainstorming, tepat ga klo saya build config dan utils.py tpi saya build di chat baruu dengan menambahkan prd dan docs perintah tugas yg pdf itu. Iya ga?

.gitignore kamu sudah benar. Isinya sama persis dengan yang saya berikan, 26 baris, tanpa ada yang terpotong. Pastikan saja file itu ada di root repo dengan nama persis .gitignore, lalu jalankan perintah git check-ignore tadi sekali untuk memastikan results/ tidak ikut terabaikan.

Soal membangun config.py dan utils.py di chat baru: tepat, dan malah menguntungkan. Alasannya:

Penilaian vibe coding melihat variasi prompt, dan log meminta satu “Target Modul” per sesi. Satu chat per modul membuat log dan share link jadi rapi.
Chat baru yang berisi PRD dan PDF tugas membuat LLM bekerja dari keputusan yang sudah dikunci, bukan dari ingatan percakapan panjang yang bisa kabur.
Kamu tidak perlu menempelkan seluruh PRD. Sesuai petunjuk di PRD, cukup Bagian Umum + Jobdesk Ketua. PDF tugas tetap berguna dilampirkan supaya LLM paham aturan larangan copy-paste dan format log.
Hal yang perlu kamu siapkan sebelum mulai:

Chat ini tidak terbawa ke chat baru. Memori Claude kamu tidak aktif, jadi semua keputusan hanya hidup di PRD. Kalau ada keputusan yang belum tertulis di PRD, tambahkan dulu.
Beberapa isi config.py belum punya nilai. Learning rate dan T baseline belum ditentukan, sedangkan batch size dan epoch baru ditentukan setelah uji memori. Putuskan sebelum sesi apakah LLM boleh mengusulkan nilai awal sementara. Kalau boleh, minta nilai itu ditandai sementara.
Parameter pembentuk model (misalnya jumlah channel dasar dan dimensi embedding) bergantung pada model.py, yang belum ditulis. Di sesi config.py bagian itu hampir pasti perlu ditambah atau diubah nanti. Jadi anggap config.py dokumen yang tumbuh, dan catat tiap perubahannya di log.
Dalam prompt, tegaskan bahwa LLM tidak boleh menambah fitur di luar PRD dan tidak boleh memakai device tetap. Dua hal itu paling sering terlanggar oleh LLM.
Simpan share link chat baru segera dan isi log di akhir sesi, sebelum lanjut ke sesi berikutnya.
Soal urutan, config.py dan utils.py memang titik mulai yang wajar. Keduanya dipakai semua anggota, dan keduanya kecil sehingga mudah diuji. Teman A dan Teman B bisa langsung bergantung pada config.py begitu selesai.

kalau uji memori gitu berati dari device yang nantinya untuk run training yaa? saya devicenya untuk running nanti menggunakan Grafis (GPU): NVIDIA GeForce GTX 1650 Ti 4GB GDDR6  memori 16gb gitu. aman ga? Klo gasalah itu sih.

Ya, uji memori dilakukan di perangkat yang nanti dipakai untuk training. Batas memorinya ditentukan oleh GPU itu. Pengujian di perangkat lain, misalnya MacBook, hanya untuk memeriksa alur dan shape, bukan untuk menentukan batch size.

Soal spesifikasimu: angka 4GB itu VRAM (memori GPU), sedangkan 16GB itu RAM biasa. Untuk training, yang menentukan adalah VRAM.

Aman atau tidak: untuk Mini DDPM pada MNIST 28x28 dengan U-Net kecil (28→14→7), 4GB VRAM umumnya cukup. Gambarnya sangat kecil dan modelnya tidak besar. Dua hal yang paling memengaruhi pemakaian memori adalah batch size dan lebar channel U-Net. Sebagian VRAM juga dipakai Windows untuk tampilan, jadi ruang efektifnya sedikit di bawah 4GB. Angka pastinya baru ketahuan setelah model.py ditulis, dan itulah gunanya uji memori. Karena batch size dikunci dan bukan variabel eksperimen, kalian bisa memilih nilai yang konservatif tanpa merusak desain eksperimen.

Yang lebih mungkin jadi kendala adalah waktu, bukan memori:

GTX 1650 Ti tidak punya tensor core, jadi mixed precision tidak banyak mempercepat. Anggap training akan berjalan di kecepatan biasa.
Sampling DDPM butuh T langkah per gambar. Grid yang dibuat tiap N epoch dan eksperimen dengan T besar akan terasa lambat. Karena itu N dan jumlah gambar sampel sebaiknya kecil.
Satu hal teknis yang sering terlewat: PyTorch harus versi CUDA, bukan versi CPU. Indeks default PyPI hanya menyediakan PyTorch versi CPU, sehingga pip install biasa di Windows akan memasang versi yang tidak memakai GPU (PyPI’s default index only has CPU-only PyTorch). Indeks resmi PyTorch sendiri menyediakan wheel Windows untuk Python 3.14 dengan CUDA 12.8 pada torch 2.9 sampai 2.11 (torch-2.10.0+cu128-cp314-cp314-win_amd64.whl adalah salah satunya), jadi kombinasi Python 3.14 kalian tersedia. Setelah instal, pastikan torch.cuda.is_available() bernilai benar dan nama GPU-nya terbaca. Driver NVIDIA juga perlu cukup baru. Saya belum memverifikasi apakah build CUDA 12.8 itu mendukung arsitektur kartumu, jadi pengecekan itu penting. 
pypi
pytorch

Karena instal PyTorch CUDA berbeda dari instal biasa, catatan cara instalnya sebaiknya masuk README, yang memang jatah ketua. Teman yang memakai Mac tidak perlu build CUDA. utils.py akan memilih device yang tersedia di mesin masing-masing.

masalahnya klo misal kan uji ram gitu sekarang sekarang, pasti ke detect nya laptop yang ini. Saat ini saya menggunakan macbook pro m3 8gb ram karna asusnya sedang di perbaiki, tapi bisa digunakan beberapa hari lagi. Nah anda juga jangan pesimis, laptop asus saya udah sering training dan hasilnya cepat dan lancar kok aman aja jangan pesimis 4 gb vram itu kecil. GImana tuh berati?

Koreksimu valid. Kamu sudah sering training di laptop ASUS itu dan hasilnya lancar, jadi pengalaman itu lebih bisa dipercaya daripada perkiraan saya dari spesifikasi. Maksud saya tadi bukan bahwa 4GB tidak cukup. Hanya saja angka batch size yang pasti baru bisa ditentukan lewat uji di perangkat sebenarnya.

Soal uji memori di MacBook sekarang: hasilnya tidak bisa dipakai untuk laptop ASUS. M3 memakai memori gabungan, yaitu 8GB yang dibagi dengan sistem, dan pengelolaannya berbeda dari VRAM terpisah di GPU NVIDIA. Angka dari satu mesin tidak berlaku untuk mesin lain. Jadi uji memori memang harus menunggu ASUS kembali.

Tapi itu tidak menghambat pekerjaan sekarang. PRD kita sudah memisahkan keduanya:

Sekarang, di MacBook: tulis config.py dan utils.py, lalu uji alur, shape, dan smoke test. Itu semua tidak bergantung pada ukuran memori. Kalau ada operasi yang tidak didukung mps, itu juga akan ketahuan sekarang.
Saat ASUS sudah kembali: lakukan uji memori di sana, tentukan batch size dan jumlah epoch, lalu masukkan ke config.py.
Selama menunggu: isi batch size dan epoch di config.py dengan nilai kecil sementara, supaya kode bisa jalan. Tandai dengan komentar bahwa nilai itu sementara, dan jangan dipakai untuk eksperimen tuning.
Karena config.py memang tempat satu-satunya nilai itu disimpan, mengganti angka nanti hanya mengubah satu file dan tidak menyentuh kode lain. Catat di log sesi config.py bahwa nilai batch size dan epoch masih sementara, supaya kronologinya jelas saat dikompilasi.

oya tpi disitu pesan error notebook. Mksdnya error ipynb? disuru ipynb apa gimana? karna sama aja kan intinya bahasa python?

Tidak, kamu tidak harus memakai .ipynb. Kamu benar bahwa intinya sama-sama Python.

Di templat log dosen, tulisan lengkapnya “Pesan Eror dari Notebook: [Salin pesan eror konsol secara utuh]”. Isi kurung siku itu menjelaskan maksudnya: yang diminta adalah pesan error utuh dari konsol. Kata “Notebook” kemungkinan hanya kebiasaan templat, karena banyak tugas seperti ini dikerjakan di Colab. Panduan tidak mewajibkan format notebook di bagian mana pun. Yang dinilai adalah kode yang bersih dan modular, model yang berjalan tanpa error, dan log yang lengkap, dan .py terpisah per modul justru cocok dengan itu.

Jadi untuk kelompokmu:

Tetap pakai label “Pesan Eror dari Notebook” persis seperti di templat, supaya formatnya sama dengan yang diminta dosen.
Isi dengan pesan error dari terminal tempat kamu menjalankan skrip. Salin utuh dari baris Traceback sampai baris terakhir, jangan diringkas.
Kalau ingin aman, tambahkan satu kalimat di bagian atas log gabungan, misalnya “Proyek dikerjakan sebagai skrip .py sehingga pesan error berasal dari terminal”. Itu cukup untuk menjelaskan kenapa tidak ada notebook.
Folder .ipynb_checkpoints/ di .gitignore tidak mengganggu apa pun. Aturan itu hanya aktif kalau ada yang memakai Jupyter, dan file .ipynb sendiri tidak diabaikan.

Dosen meminta hasil akhir proyek berupa satu file .ipynb yang berdiri sendiri (boleh berisi fungsi dan kelas). Kata dosen: "sebaiknya file yang modular tersebut dijadikan 1 file dalam .ipynb, bisa dibuat fungsi atau yang lainnya". Tenggat sekarang 7 November 2026. Saya lampirkan ulang PDF panduan dan PRD lama.

Buat PRD versi notebook. Dokumen ini berupa Markdown biasa, bukan kode. Jangan menulis kode atau file .py apa pun.

PERTAHANKAN semua keputusan lama: Mini DDPM, MNIST 28x28, U-Net dua level downsampling (28→14→7), dua variabel tuning (learning rate dan T), isi checkpoint, DataLoader hanya gambar, kontrak data, pembagian peran, aturan log dan Git, label [PDF]/[Keputusan]/[Asumsi]. Nama fungsi dan kelas yang sudah ada di PRD lama dipakai apa adanya. Kalau ada yang belum punya nama di PRD lama, tandai [Asumsi], jangan mengarang diam-diam.

UBAH hanya hal berikut:

ATURAN UTAMA
Seluruh kode ada di sel notebook. Tidak ada file .py baru. File .py lama tetap di repo sebagai riwayat commit dan tidak dipakai atau diimpor. Tidak ada import antar-file, yang di-import hanya library (torch, numpy, matplotlib, torchvision).

STRUKTUR REPO
notebooks/ketua.ipynb (Ketua), notebooks/A.ipynb (Teman A), notebooks/B.ipynb (Teman B). Tiap anggota hanya mengubah notebook miliknya, di branch sendiri.
MiniDDPM.ipynb di root repo: notebook final, dirakit Ketua dari tiga notebook di atas.
data/, checkpoints/, results/ tetap di root repo, aturan commit sama seperti sebelumnya.
BASE_DIR ditentukan satu kali di sel config: Path.cwd(), dan kalau nama foldernya "notebooks" pakai folder induknya, supaya data/, checkpoints/, results/ selalu di root repo.

ISI TIAP NOTEBOOK (urutan sel)
Notebook final dan notebook tiap anggota mengikuti urutan bagian ini; tiap anggota hanya mengisi bagiannya:
0. Judul dan ringkasan proyek (markdown)
Import library (satu sel)
config: nilai baseline sebagai SimpleNamespace bernama config, sehingga config.X tetap berlaku (Ketua)
utils: set_seed dan get_device (Ketua)
dataset: DataLoader MNIST (Teman A)
visualize: grid gambar dan grafik loss (Teman A)
model: timestep embedding, blok dasar, U-Net (Ketua)
diffusion: kelas Diffusion (Ketua)
experiments: daftar konfigurasi eksperimen (Teman B)
train: fungsi training (Teman B)
sample: fungsi sampling dari checkpoint (Teman B)
Uji: satu sel uji per bagian di atas
Eksekusi: jalankan training baseline, tampilkan grafik loss dan grid gambar di notebook (juga disimpan ke results/), lalu sampling dari checkpoint
Eksperimen dan hasil: jalankan konfigurasi eksperimen, tampilkan perbandingan

ATURAN SEL
Satu sel berisi satu fungsi, satu kelas, atau satu langkah.
Tiap bagian diawali sel markdown berisi judul dan nama pemilik, dan diakhiri sel uji.
Urutan sel dari yang diandalkan ke yang memakai (config sebelum utils, model dan diffusion sebelum train).
Blok if __name__ == "__main__" dan python -m diganti sel uji. Argparse dan perintah terminal diganti pemanggilan fungsi, misalnya train("baseline") dan sample(path_checkpoint).
Notebook A dan B boleh memuat salinan sementara sel milik Ketua yang mereka butuhkan untuk uji, diberi label "SALINAN SEMENTARA, jangan dimasukkan ke notebook final".

KONTRAK ANTAR-BAGIAN
Tabel: nama fungsi atau kelas publik tiap bagian, pemilik, input, dan output.

Hapus bagian jadwal. Jobdesk tetap per orang (Ketua, Teman A, Teman B), berdiri sendiri, dan menyebut notebook milik masing-masing.

Judul: "PRD Final: Mini DDPM pada MNIST (Notebook)". Tanpa kata "revisi". Jangan menambah fitur atau butir baru.

PRD versi notebook sudah jadi di prd_final_mini_ddpm_notebook.md. Tidak ada lampiran baru yang terbaca di pesan ini, jadi saya bekerja dari PRD lama dan isi PDF yang sudah ada di percakapan ini. Jadwal dan tenggat tidak dimasukkan, sesuai instruksi.

Yang berubah hanya enam hal yang kamu minta. Tiga hal terkait penamaan perlu kamu cek:

Nama yang ditetapkan di pesanmu saya tandai [Keputusan]: config, set_seed, get_device, Diffusion, train, dan sample(path_checkpoint). Nama-nama ini tidak ada di PRD lama, jadi asalnya dari pesan ini.
Nama yang belum ada saya tandai [Asumsi]: get_dataloader, save_image_grid, plot_loss, SinusoidalTimeEmbedding, Block, UNet, Diffusion.q_sample, Diffusion.sample_timesteps, Diffusion.generate, dan EXPERIMENTS. PRD lama hanya menyebut fungsinya, bukan namanya. Kalau kelompok sudah punya nama lain, ganti di tabel Bagian 10 (Kontrak antar-bagian) lalu tempel ulang ke teman-temanmu.
Pemilik sel 0, 1, 12, dan 13 tidak kamu sebut. Saya isi Ketua untuk sel 0 dan 1 (judul dan import), dan Teman B untuk sel 12 dan 13 (eksekusi dan eksperimen), semuanya [Asumsi]. Teman B dipilih karena dia yang menjalankan training dan eksperimen.
Dua hal kecil yang juga saya tandai [Asumsi]: train memakai nilai efektif sebagai salinan lokal supaya config tidak berubah antar-eksperimen, dan Ketua menjalankan notebook final dari sel pertama pada kernel yang bersih sebelum dikumpulkan.

Satu hal di luar dokumen: daftar library yang boleh di-import tidak mencakup Jupyter. Untuk menjalankan .ipynb, kalian tetap butuh Jupyter atau ekstensi notebook di VS Code. Itu alat pemakaian, bukan import di kode, jadi saya tidak memasukkannya ke PRD.

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

02
Haloo

Halo! 👋 Ada yang bisa saya bantu hari ini?

[CAK4KBB3 2026-1] Panduan Proyek 1 - Vibe Coding (1).pdf
pdf

prd_final_mini_ddpm.md
prd_final_mini_ddpm.md
MD
Saya ketua kelompok 3 orang untuk tugas besar ini. Terlampir PDF panduan dan PRD kelompok. Peran saya: Ketua, memegang config.py, utils.py, model.py, diffusion.py. Tolong ikuti PRD.

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

Format: tulis kodenya modular, diberi komentar, tanpa menyalin dari tutorial. Jelaskan singkat rencananya dulu, lalu kodenya, lalu cara mengujinya.

Meninjau PDF panduan dan PRD kelompok.
Saya baca PRD-nya dulu supaya kodenya sesuai.

Rencana singkat
PRD sudah saya baca (Bagian 3, 4, 5, 6 dan jobdesk Ketua). Hasilnya dua file di root repo, config.py dan utils.py, tanpa folder atau file lain.

config.py: konstanta tingkat modul yang dikelompokkan dengan komentar (seed, training, diffusion, model, sampling, smoke test, path), sesuai spesifikasimu.
utils.py: set_seed(seed) dan get_device(). get_device() tidak mencetak apa pun, dan hanya __main__ yang boleh print.
Kodenya
Kedua file ada di config.py dan utils.py (lihat kartu file). Beberapa keputusan yang perlu kamu tahu:

Nama kunci MODEL_PARAMS: in_channels, base_channels, channel_mults, time_emb_dim. Spesifikasimu tidak menyebut nama kuncinya, jadi ini pilihan saya. Konstruktor UNet di sesi model.py harus memakai nama yang sama persis.
Nama path: LOSS_CURVES_DIR dan SAMPLES_DIR (keduanya di bawah RESULTS_DIR). Saya juga menambah BASE_DIR karena dipakai untuk menghitung semua path lainnya.
SMOKE_SUBSET_SIZE = 512: nama ini saya pilih untuk “subset 512 gambar”.
Import config.py tidak membuat folder. checkpoints/ dan results/... harus dibuat dengan mkdir(parents=True, exist_ok=True) oleh kode yang menulis ke sana (train.py, sample.py). Ini sengaja, sesuai larangan membuat folder lain.
channel_mults berupa tuple, jadi torch.save aman. Kalau suatu saat checkpoint disimpan lewat JSON, tuple akan menjadi list. Ini perlu diperhatikan Teman B.
set_seed memakai torch.manual_seed, yang juga menyemai CUDA dan MPS. Karena mode deterministik penuh tidak dipakai, hasil di GPU bisa sedikit berbeda antar-run walau seed sama.
Cara menguji
Jalankan dari root repo:

python config.py
python utils.py
Hasil yang diharapkan:

config.py mencetak path absolut dan nilai-nilai, lalu config.py OK. Blok ujinya memeriksa:
semua path berada di bawah root repo
0 < BETA_START < BETA_END < 1
SMOKE_SAMPLE_EVERY <= SMOKE_EPOCHS
SMOKE_SUBSET_SIZE >= BATCH_SIZE
channel_mults benar-benar menghasilkan 28 → 14 → 7
utils.py mencetak set_seed OK dan get_device OK: mps di MacBook M3 (atau cuda di laptop GTX 1650 Ti). Tes set_seed membuktikan seed sama menghasilkan angka sama dan seed beda menghasilkan angka beda. Tes get_device membuat tensor di device itu dan menghitungnya.
Status uji di sandbox saya
config.py sudah saya jalankan di sandbox dan lolos semua pemeriksaan.
utils.py hanya lolos cek sintaks. Instalasi PyTorch di sandbox kehabisan waktu, jadi blok ujinya belum pernah dijalankan. Tolong jalankan python utils.py di Mac-mu. Kalau ada error, salin pesannya utuh untuk log debugging.
Sandbox memakai Python 3.12, sedangkan proyekmu 3.14. Tidak ada sintaks khusus versi di kedua file, tapi uji di 3.14.6-mu tetap yang berlaku.
Jangan lupa mengisi docs/logs/log_ketua.md untuk sesi ini sesuai templat. Kalau siap, lanjut ke sesi diffusion.py (di sana juga keputusan beta saat T berubah) atau model.py.

Tolong tampilkan kode langsung di dalam chat sebagai blok kode, satu blok per file (config.py dan utils.py). Jangan membuat file atau artifact yang harus diunduh. Saya akan menyalinnya sendiri ke repo.

Ini kodenya, satu blok per file. Isinya sama dengan versi final yang sudah saya jalankan (config.py) dan cek sintaksnya (utils.py).

config.py

python
"""config.py - satu-satunya tempat nilai baseline proyek Mini DDPM disimpan.

Aturan (PRD Bagian 3, 5, 6):
- Hanya ketua yang mengubah file ini.
- File lain tidak boleh menulis angka tetap; semuanya dibaca dari sini.
- experiments.py (Teman B) hanya boleh menimpa LEARNING_RATE dan T,
  dan penimpaan dilakukan di sisi experiments.py/train.py, bukan di sini.
- Import file ini tidak membuat folder apa pun. Pembuatan folder
  (checkpoints/, results/...) dilakukan oleh kode yang menulis ke sana.
"""

from pathlib import Path

# ---------------------------------------------------------------------------
# Reproducibility
# ---------------------------------------------------------------------------
SEED = 42  # dipakai utils.set_seed(); satu seed untuk semua anggota

# ---------------------------------------------------------------------------
# Training (baseline)
# ---------------------------------------------------------------------------
LEARNING_RATE = 2e-4  # baseline; boleh ditimpa oleh experiments.py

# SEMENTARA, BELUM FINAL: menunggu uji memori di laptop GTX 1650 Ti (4GB).
# Jangan dipakai untuk eksperimen tuning sampai nilai final ditetapkan.
BATCH_SIZE = 64
EPOCHS = 30

NUM_WORKERS = 0  # DataLoader tanpa proses worker (aman di macOS dan Windows)

# ---------------------------------------------------------------------------
# Diffusion (baseline)
# ---------------------------------------------------------------------------
T = 1000  # jumlah timestep baseline; boleh ditimpa oleh experiments.py

# Acuan untuk T=1000. Penyesuaian beta saat T berubah diputuskan
# di sesi diffusion.py.
BETA_START = 1e-4
BETA_END = 0.02

# ---------------------------------------------------------------------------
# Model (parameter pembentuk U-Net)
# ---------------------------------------------------------------------------
# Dipakai sebagai UNet(**MODEL_PARAMS) dan disimpan di checkpoint.
# Nama kunci harus cocok dengan argumen konstruktor UNet di model.py.
# channel_mults (1, 2, 2) = dua downsampling: 28 -> 14 -> 7.
MODEL_PARAMS = {
    "in_channels": 1,
    "base_channels": 64,
    "channel_mults": (1, 2, 2),
    "time_emb_dim": 128,
}

# ---------------------------------------------------------------------------
# Sampling selama training
# ---------------------------------------------------------------------------
SAMPLE_EVERY_N_EPOCHS = 5  # grid sampel disimpan tiap N epoch
NUM_SAMPLE_IMAGES = 16     # jumlah gambar per grid

# ---------------------------------------------------------------------------
# Smoke test (uji alur cepat, bukan untuk hasil)
# ---------------------------------------------------------------------------
SMOKE_TEST = False       # True = pakai subset kecil dan epoch pendek
SMOKE_SUBSET_SIZE = 512  # jumlah gambar pada mode smoke test
SMOKE_EPOCHS = 2         # jumlah epoch pada mode smoke test
SMOKE_SAMPLE_EVERY = 1   # interval grid pada smoke test (harus <= SMOKE_EPOCHS)

# ---------------------------------------------------------------------------
# Path (dihitung dari lokasi file ini, jadi tidak bergantung pada
# direktori tempat perintah dijalankan)
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"                  # unduhan MNIST (tidak di-commit)
CHECKPOINT_DIR = BASE_DIR / "checkpoints"     # checkpoint (tidak di-commit)
RESULTS_DIR = BASE_DIR / "results"            # hasil (di-commit)
LOSS_CURVES_DIR = RESULTS_DIR / "loss_curves"
SAMPLES_DIR = RESULTS_DIR / "samples"


if __name__ == "__main__":
    # Uji kecil: cek konsistensi nilai dan path. Tidak membuat folder.
    print(f"BASE_DIR       : {BASE_DIR}")
    for name, path in [
        ("DATA_DIR", DATA_DIR),
        ("CHECKPOINT_DIR", CHECKPOINT_DIR),
        ("RESULTS_DIR", RESULTS_DIR),
        ("LOSS_CURVES_DIR", LOSS_CURVES_DIR),
        ("SAMPLES_DIR", SAMPLES_DIR),
    ]:
        assert path.is_absolute(), f"{name} harus absolut"
        assert BASE_DIR in path.parents, f"{name} harus berada di bawah BASE_DIR"
        print(f"{name:<15}: {path}")

    assert (BASE_DIR / "config.py").exists(), \
        "config.py harus berada langsung di root repo (BASE_DIR)"

    # Konsistensi nilai
    assert 0 < BETA_START < BETA_END < 1, "beta harus 0 < start < end < 1"
    assert T > 0 and BATCH_SIZE > 0 and EPOCHS > 0
    assert SMOKE_SAMPLE_EVERY <= SMOKE_EPOCHS, "smoke: N harus <= jumlah epoch"
    assert SMOKE_SUBSET_SIZE >= BATCH_SIZE, "subset smoke harus >= batch size"

    # Dua downsampling dari 28: 28 -> 14 -> 7
    n_down = len(MODEL_PARAMS["channel_mults"]) - 1
    size = 28
    for _ in range(n_down):
        size //= 2
    assert n_down == 2 and size == 7, "U-Net harus 28 -> 14 -> 7"

    print(f"SEED={SEED}  LR={LEARNING_RATE}  T={T}  "
          f"BATCH_SIZE={BATCH_SIZE}(sementara)  EPOCHS={EPOCHS}(sementara)")
    print(f"MODEL_PARAMS   : {MODEL_PARAMS}")
    print("config.py OK")
utils.py

python
"""utils.py - fungsi pendukung umum: pengaturan seed dan pemilihan device.

Aturan (PRD Bagian 4):
- get_device() adalah SATU-SATUNYA tempat device ditentukan. File lain
  tidak boleh menulis "cuda"/"mps"/"cpu" secara langsung.
- Fungsi di sini tidak mencetak apa pun; pencetakan hanya di blok uji.
"""

import random

import numpy as np
import torch


def set_seed(seed):
    """Mengatur seed random, numpy, dan torch agar hasil bisa diulang.

    Sengaja TIDAK mengaktifkan mode deterministik penuh
    (torch.use_deterministic_algorithms / cudnn.deterministic), supaya
    kecepatan training tidak turun. Akibatnya hasil di GPU bisa sedikit
    berbeda antar-run walau seed sama.
    """
    random.seed(seed)
    np.random.seed(seed)
    # torch.manual_seed juga menyemai generator di semua device
    # (CPU, CUDA, MPS).
    torch.manual_seed(seed)


def get_device():
    """Mengembalikan torch.device pertama yang tersedia: cuda, mps, cpu.

    Fungsi murni: tidak ada print dan tidak ada efek samping.
    """
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


if __name__ == "__main__":
    # --- Uji set_seed: seed sama -> angka sama, seed beda -> angka beda ---
    def draw():
        """Mengambil satu angka dari tiap generator."""
        return (random.random(), float(np.random.rand()), float(torch.rand(1)))

    set_seed(42)
    a = draw()
    set_seed(42)
    b = draw()
    set_seed(7)
    c = draw()
    assert a == b, "seed sama harus menghasilkan angka sama"
    assert a != c, "seed beda harus menghasilkan angka beda"
    print("set_seed OK: reproducible untuk random, numpy, torch")

    # --- Uji get_device: tipe benar, urutan prioritas, bisa dipakai ---
    device = get_device()
    assert isinstance(device, torch.device)
    assert device.type in ("cuda", "mps", "cpu")

    if torch.cuda.is_available():
        expected = "cuda"
    elif torch.backends.mps.is_available():
        expected = "mps"
    else:
        expected = "cpu"
    assert device.type == expected, "urutan prioritas harus cuda > mps > cpu"

    # Pastikan tensor benar-benar bisa dibuat dan dihitung di device itu
    x = torch.ones(2, 2, device=device)
    assert float((x + x).sum().cpu()) == 8.0
    print(f"get_device OK: {device}")
Setelah menyalin ke root repo, jalankan python config.py lalu python utils.py. Di Mac M3-mu, hasil yang diharapkan adalah config.py OK dan get_device OK: mps. Ingat bahwa utils.py belum pernah saya jalankan penuh karena PyTorch tidak terpasang di sandbox saya, jadi hasil uji di Mac-mu yang menentukan.

1793176383692_image.png
okayy sudah berhasil, config.py dan utils.py sudah jadi dan lolos uji. Kita lanjut ke diffusion.py, di root repo, tanpa file lain.

Sebelum kode, jelaskan dulu dengan bahasa sederhana: noise schedule (beta, alpha, alpha-bar), mengapa gambar di timestep t bisa dihitung langsung dari gambar bersih, dan apa yang terjadi di tiap langkah sampling.

Lalu tulis diffusion.py sesuai PRD: noise schedule, forward process, pengambilan t acak yang valid (0 sampai T-1), dan fungsi sampling. T diterima sebagai parameter. Untuk beta saat T berubah: skalakan dengan 1000/T supaya langkah terakhir tetap noise murni. Jelaskan alasannya.

Uji di blok if __name__ == "__main__": cek shape, cek alpha-bar menurun dari mendekati 1 ke mendekati 0, dan uji sampling dengan model tiruan sederhana. Pakai gambar sintetis, bukan MNIST.

Komentar di kode seperlunya saja: singkat dan hanya untuk bagian penting. Tampilkan kode langsung di chat, bukan file unduhan.

Saya coba memasang PyTorch di sandbox lewat proses latar belakang supaya diffusion.py bisa saya uji sebelum saya tampilkan. File uji hanya di folder sementara, bukan file yang perlu kamu unduh.

Instalasi PyTorch di sandbox mati sebelum selesai. Sebagai gantinya, saya verifikasi rumusnya dengan numpy supaya matematikanya terbukti, meskipun kode torch-nya sendiri tetap perlu kamu jalankan.

Penjelasan sederhana
Noise schedule. Forward process mengubah gambar bersih menjadi noise murni lewat T langkah kecil. Di setiap langkah t ada tiga angka:

beta_t adalah porsi noise yang ditambahkan di langkah itu. Nilainya kecil di awal (1e-4) lalu naik linear sampai 0.02.
alpha_t = 1 - beta_t adalah porsi gambar yang dipertahankan di langkah itu.
alpha-bar_t adalah hasil kali semua alpha dari langkah 0 sampai t, yaitu seberapa banyak gambar asli yang masih tersisa. Nilainya mulai dari hampir 1 (hampir bersih) dan turun sampai hampir 0 (tinggal noise).
Noise ditambahkan bertahap karena model hanya perlu belajar membuang sedikit noise di tiap langkah, yang jauh lebih mudah daripada mengubah noise menjadi gambar sekaligus.

Mengapa gambar di timestep t bisa dihitung langsung dari gambar bersih. Satu langkah noise berbentuk x_t = sqrt(alpha_t)·x_(t-1) + sqrt(beta_t)·noise. Kalau dua langkah digabung:

x_2 = sqrt(a1·a2)·x0 + sqrt(a2·b1)·n1 + sqrt(b2)·n2
Dua noise Gaussian yang saling bebas bisa digabung menjadi satu noise Gaussian dengan varians dijumlahkan: a2·b1 + b2 = a2(1-a1) + (1-a2) = 1 - a1·a2. Pola ini berlanjut untuk semua langkah:

x_t = sqrt(alpha_bar_t)·x0 + sqrt(1 - alpha_bar_t)·noise
Jadi satu rumus dan satu noise sudah cukup. Saat training, kita cukup memilih t acak tanpa perlu mengulang t langkah. Uji nomor 3 di kode membuktikan kesetaraan ini secara statistik.

Apa yang terjadi di tiap langkah sampling. Mulai dari noise murni, lalu untuk t dari T-1 turun ke 0:

Model memprediksi noise yang ada di x_t.
Bagian noise itu dikurangkan (dengan koefisien beta_t / sqrt(1 - alpha_bar_t)), lalu dibagi sqrt(alpha_t) untuk mengembalikan skala. Hasilnya estimasi x_(t-1) yang sedikit lebih bersih.
Ditambahkan noise acak kecil sqrt(beta_t). Model hanya memberi rata-rata dari distribusi x_(t-1), dan noise inilah yang membuat hasil beragam. Pada t=0 noise tidak ditambahkan agar hasil akhir bersih.
Setelah loop selesai, nilai di-clamp ke [-1, 1] sesuai kontrak PRD.

Mengapa beta diskalakan 1000/T. Total noise kira-kira sama dengan jumlah semua beta, karena alpha_bar_T ≈ exp(-jumlah beta). Pada jadwal linear, jumlah beta = T × rata-rata beta.

Tanpa skala: dengan T=100, jumlah beta hanya sekitar 1 dan alpha_bar_T sekitar 0.36, jadi di langkah terakhir masih tersisa sinyal (sekitar 60%). Training tidak pernah melihat noise murni, padahal sampling selalu mulai dari noise murni. Akibatnya hasil sampling rusak.
Dengan skala: jumlah beta tetap 10.05 untuk semua T, sehingga alpha_bar_T selalu sekitar 4e-5 dan langkah terakhir benar-benar noise murni. Kurva alpha-bar terhadap t/T juga hampir sama untuk semua T. Jadi eksperimen T hanya mengubah jumlah langkah (resolusi), bukan jumlah noise totalnya, dan itulah yang ingin diukur Teman B.
Batas bawah T: beta akhir menjadi 0.02·1000/T, jadi harus < 1, artinya T minimal 21. Kode melempar ValueError jika T lebih kecil.
Kode
diffusion.py

python
"""diffusion.py - noise schedule, forward process, dan sampling (reverse process) DDPM."""

import torch

import config

# Beta di config.py adalah acuan untuk T=1000; dipakai sebagai pembagi skala.
BETA_REFERENCE_T = 1000
# Sisi gambar (28x28). Jumlah channel diambil dari config.MODEL_PARAMS.
IMAGE_SIZE = 28


def _extract(values, t, x):
    """Ambil values[t] lalu ubah ke (B,1,1,1) agar bisa dikalikan dengan x (B,C,H,W)."""
    out = values.to(x.device)[t.to(x.device)]
    return out.reshape(t.shape[0], *([1] * (x.dim() - 1)))


class Diffusion:
    def __init__(self, T, device=None,
                 beta_start=config.BETA_START, beta_end=config.BETA_END):
        # Skala 1000/T menjaga total noise tetap sama saat T berubah.
        scale = BETA_REFERENCE_T / T
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
        shape = (num_images, config.MODEL_PARAMS["in_channels"], IMAGE_SIZE, IMAGE_SIZE)
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
    ref_beta_sum = Diffusion(BETA_REFERENCE_T).betas.sum().item()
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
    x0 = torch.full((8, C, IMAGE_SIZE, IMAGE_SIZE), -1.0, device=device)
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
    assert out.shape == (N, C, IMAGE_SIZE, IMAGE_SIZE)
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
Cara menguji
Dari root repo, dengan venv aktif:

python diffusion.py
Hasil yang diharapkan: empat baris schedule OK (nilai alpha_bar[-1] sekitar 2e-05 sampai 4e-05), lalu T terlalu kecil ditolak OK, forward process OK (MSE naik dari sekitar 0.0001 ke sekitar 2), bentuk tertutup = langkah bertahap OK, sample_timesteps OK, dua baris sampling ... OK, dan terakhir diffusion.py OK. Pengujian sampling berjalan 1000 langkah dengan model tiruan, jadi di M3 mungkin butuh beberapa detik.

Dua model tiruan menguji hal yang berbeda:

Model nol memeriksa bentuk, rentang nilai, dan bahwa t yang diterima model berurutan dari T-1 ke 0 dengan tipe long.
Model oracle (tahu gambar aslinya) harus menghasilkan gambar aslinya kembali. Tes ini akan gagal jika indeks t salah atau noise ikut ditambahkan di langkah terakhir.
Catatan integrasi
Dua angka di luar config. BETA_REFERENCE_T = 1000 dan IMAGE_SIZE = 28 masih ditulis di diffusion.py, padahal PRD menyatakan tidak ada angka tetap di file lain. Saya tidak mengubah config.py tanpa persetujuanmu. Kalau mau dipindah, cukup tambah dua baris di config.py (mis. BETA_REFERENCE_T = 1000 dan IMAGE_SIZE = 28), lalu ganti dua konstanta itu dengan config.BETA_REFERENCE_T dan config.IMAGE_SIZE.
Kontrak untuk Teman B:
Buat Diffusion(T, device).
add_noise(x0, t, noise) mewajibkan noise diberikan dari luar, supaya train.py memakai noise yang sama sebagai target loss.
sample_timesteps(batch_size, device) mengembalikan t bertipe long.
sample(model, num_images, device) tidak mengubah mode model. train.py yang harus memakai model.eval() sebelum sampling dan model.train() sesudahnya.
Biaya sampling. Sampling butuh T kali forward U-Net, jadi eksperimen T=2000 membuat grid sampel dua kali lebih lama daripada T=1000.
Varians noise. Saya memakai sigma_t² = beta_t karena paling sederhana untuk dijelaskan. Alternatifnya adalah varians posterior, yang hasilnya mirip.
Status uji
PyTorch gagal terpasang di sandbox saya, jadi kode torch di diffusion.py belum pernah saya jalankan, dan hasil python diffusion.py di Mac-mu yang menentukan. Yang sudah saya verifikasi dengan numpy adalah rumus-rumusnya:

alpha_bar[-1] sekitar 2e-05 sampai 4e-05 untuk T = 100, 500, 1000, dan 2000, dengan jumlah beta selalu 10.05.
Tanpa skala, T=100 menyisakan alpha_bar[-1] sekitar 0.36.
Bentuk tertutup cocok dengan langkah bertahap: rata-rata 0.560 vs 0.564, simpangan baku 0.827 vs 0.825.
Sampling dengan model oracle menghasilkan error maksimum sekitar 1e-5.
Sampling dengan model nol tetap berhingga.
Kalau ada error saat dijalankan, salin pesannya utuh untuk log debugging. Jangan lupa mengisi docs/logs/log_ketua.md untuk sesi ini. Lanjut ke model.py (U-Net dan timestep embedding)?

Menurut saya Varians noise sigma_t² = beta_t saya setujui karena paling sederhana dijelaskan.

Satu perubahan menurut saya: pindahkan BETA_REFERENCE_T = 1000 dan IMAGE_SIZE = 28 ke config.py, lalu di diffusion.py ganti dengan config.BETA_REFERENCE_T dan config.IMAGE_SIZE. Tampilkan config.py dan diffusion.py yang sudah diperbarui, utuh, langsung di chat.

Setelah itu saya akan menjalankan python config.py dan python diffusion.py, lalu melaporkan hasilnya.

config.py dan diffusion.py sudah diperbarui sesuai permintaanmu. Perubahannya:

config.py

Menambah BETA_REFERENCE_T = 1000 di grup Diffusion, di bawah BETA_START dan BETA_END.
Menambah IMAGE_SIZE = 28 di grup Model.
Komentar beta saya perbarui: keputusan penyesuaian beta sudah diambil (skala BETA_REFERENCE_T / T), jadi catatan “ditunda ke sesi diffusion.py” tidak lagi relevan.
Blok uji bertambah dua pemeriksaan. Beta akhir setelah skala untuk T baseline harus < 1, dan ukuran gambar harus habis dibagi 2 di tiap downsampling (jalur 28 → 14 → 7 sekarang dihitung dari IMAGE_SIZE).
diffusion.py

Dua konstanta lokal dihapus.
Semua pemakaian diganti dengan config.BETA_REFERENCE_T dan config.IMAGE_SIZE, termasuk di blok uji.
Satu baris panjang di sample() saya pecah supaya mudah dibaca.
config.py

python
"""config.py - satu-satunya tempat nilai baseline proyek Mini DDPM disimpan.

Aturan (PRD Bagian 3, 5, 6):
- Hanya ketua yang mengubah file ini.
- File lain tidak boleh menulis angka tetap; semuanya dibaca dari sini.
- experiments.py (Teman B) hanya boleh menimpa LEARNING_RATE dan T,
  dan penimpaan dilakukan di sisi experiments.py/train.py, bukan di sini.
- Import file ini tidak membuat folder apa pun. Pembuatan folder
  (checkpoints/, results/...) dilakukan oleh kode yang menulis ke sana.
"""

from pathlib import Path

# ---------------------------------------------------------------------------
# Reproducibility
# ---------------------------------------------------------------------------
SEED = 42  # dipakai utils.set_seed(); satu seed untuk semua anggota

# ---------------------------------------------------------------------------
# Training (baseline)
# ---------------------------------------------------------------------------
LEARNING_RATE = 2e-4  # baseline; boleh ditimpa oleh experiments.py

# SEMENTARA, BELUM FINAL: menunggu uji memori di laptop GTX 1650 Ti (4GB).
# Jangan dipakai untuk eksperimen tuning sampai nilai final ditetapkan.
BATCH_SIZE = 64
EPOCHS = 30

NUM_WORKERS = 0  # DataLoader tanpa proses worker (aman di macOS dan Windows)

# ---------------------------------------------------------------------------
# Diffusion (baseline)
# ---------------------------------------------------------------------------
T = 1000  # jumlah timestep baseline; boleh ditimpa oleh experiments.py

# Acuan untuk T=1000. Saat T berubah, diffusion.py menskalakan beta
# dengan BETA_REFERENCE_T / T agar total noise tetap sama.
BETA_START = 1e-4
BETA_END = 0.02
BETA_REFERENCE_T = 1000  # T tempat BETA_START dan BETA_END berlaku apa adanya

# ---------------------------------------------------------------------------
# Model (parameter pembentuk U-Net)
# ---------------------------------------------------------------------------
IMAGE_SIZE = 28  # sisi gambar MNIST (28x28); channel ada di MODEL_PARAMS

# Dipakai sebagai UNet(**MODEL_PARAMS) dan disimpan di checkpoint.
# Nama kunci harus cocok dengan argumen konstruktor UNet di model.py.
# channel_mults (1, 2, 2) = dua downsampling: 28 -> 14 -> 7.
MODEL_PARAMS = {
    "in_channels": 1,
    "base_channels": 64,
    "channel_mults": (1, 2, 2),
    "time_emb_dim": 128,
}

# ---------------------------------------------------------------------------
# Sampling selama training
# ---------------------------------------------------------------------------
SAMPLE_EVERY_N_EPOCHS = 5  # grid sampel disimpan tiap N epoch
NUM_SAMPLE_IMAGES = 16     # jumlah gambar per grid

# ---------------------------------------------------------------------------
# Smoke test (uji alur cepat, bukan untuk hasil)
# ---------------------------------------------------------------------------
SMOKE_TEST = False       # True = pakai subset kecil dan epoch pendek
SMOKE_SUBSET_SIZE = 512  # jumlah gambar pada mode smoke test
SMOKE_EPOCHS = 2         # jumlah epoch pada mode smoke test
SMOKE_SAMPLE_EVERY = 1   # interval grid pada smoke test (harus <= SMOKE_EPOCHS)

# ---------------------------------------------------------------------------
# Path (dihitung dari lokasi file ini, jadi tidak bergantung pada
# direktori tempat perintah dijalankan)
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"                  # unduhan MNIST (tidak di-commit)
CHECKPOINT_DIR = BASE_DIR / "checkpoints"     # checkpoint (tidak di-commit)
RESULTS_DIR = BASE_DIR / "results"            # hasil (di-commit)
LOSS_CURVES_DIR = RESULTS_DIR / "loss_curves"
SAMPLES_DIR = RESULTS_DIR / "samples"


if __name__ == "__main__":
    # Uji kecil: cek konsistensi nilai dan path. Tidak membuat folder.
    print(f"BASE_DIR       : {BASE_DIR}")
    for name, path in [
        ("DATA_DIR", DATA_DIR),
        ("CHECKPOINT_DIR", CHECKPOINT_DIR),
        ("RESULTS_DIR", RESULTS_DIR),
        ("LOSS_CURVES_DIR", LOSS_CURVES_DIR),
        ("SAMPLES_DIR", SAMPLES_DIR),
    ]:
        assert path.is_absolute(), f"{name} harus absolut"
        assert BASE_DIR in path.parents, f"{name} harus berada di bawah BASE_DIR"
        print(f"{name:<15}: {path}")

    assert (BASE_DIR / "config.py").exists(), \
        "config.py harus berada langsung di root repo (BASE_DIR)"

    # Konsistensi nilai
    assert 0 < BETA_START < BETA_END < 1, "beta harus 0 < start < end < 1"
    assert T > 0 and BATCH_SIZE > 0 and EPOCHS > 0
    assert BETA_REFERENCE_T > 0 and IMAGE_SIZE > 0
    assert BETA_END * BETA_REFERENCE_T / T < 1, "beta akhir (setelah skala) harus < 1"
    assert SMOKE_SAMPLE_EVERY <= SMOKE_EPOCHS, "smoke: N harus <= jumlah epoch"
    assert SMOKE_SUBSET_SIZE >= BATCH_SIZE, "subset smoke harus >= batch size"

    # Dua downsampling dari IMAGE_SIZE: 28 -> 14 -> 7
    n_down = len(MODEL_PARAMS["channel_mults"]) - 1
    size = IMAGE_SIZE
    for _ in range(n_down):
        assert size % 2 == 0, "ukuran gambar harus habis dibagi 2 di tiap downsampling"
        size //= 2
    assert n_down == 2 and size == 7, "U-Net harus 28 -> 14 -> 7"

    print(f"SEED={SEED}  LR={LEARNING_RATE}  T={T}  "
          f"BATCH_SIZE={BATCH_SIZE}(sementara)  EPOCHS={EPOCHS}(sementara)")
    print(f"BETA_REFERENCE_T={BETA_REFERENCE_T}  IMAGE_SIZE={IMAGE_SIZE}")
    print(f"MODEL_PARAMS   : {MODEL_PARAMS}")
    print("config.py OK")
diffusion.py

python
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
Status uji di sisi saya
config.py versi baru sudah saya jalankan di sandbox dan lolos semua pemeriksaan, termasuk dua yang baru. Di komputermu path-nya tentu akan menunjuk ke folder repo.
diffusion.py hanya saya cek sintaksnya. Karena PyTorch belum terpasang di sandbox, kode torch-nya belum dijalankan. Pemeriksaan teks memastikan tidak ada lagi angka 28 atau 1000 sebagai nilai di kode diffusion.py. Satu-satunya 1000 yang tersisa adalah salah satu nilai T pada daftar uji (100, 500, 1000, 2000), dan itu memang nilai uji, bukan duplikasi config.
Silakan jalankan python config.py lalu python diffusion.py dari root repo. Kalau ada baris yang gagal, kirim seluruh output beserta pesan error utuhnya, dan salin juga ke log debugging di docs/logs/log_ketua.md.

1793179167271_image.png
1793179178201_image.png
udah bisa yaa.

Semua lolos, dan angkanya cocok dengan yang saya harapkan.

Schedule: alpha_bar[-1] berada di 2e-05 sampai 4e-05 untuk T = 100, 500, 1000, dan 2000. Angkanya sama persis dengan hitungan numpy saya, jadi skala 1000/T bekerja seperti yang direncanakan.
Forward process: MSE ke gambar asli naik dari 0.0001 (t=0) ke 2.0021 (t=T-1). Nilai akhir sekitar 2 memang benar: gambar sintetis bernilai ±1 (kuadratnya 1) dan noise murni bervarians 1, jadi jaraknya 1 + 1 = 2. Artinya di langkah terakhir gambar asli sudah hilang sepenuhnya.
Bentuk tertutup dan model oracle: dua tes ini yang paling penting. Yang pertama membuktikan x_t bisa dihitung langsung dari x0, sedangkan yang kedua membuktikan indeks t di loop sampling benar dan langkah terakhir tidak menambah noise.
Dua hal yang masih tersisa:

Uji di GPU belum ada. Semua hasil di atas dari MPS. Saat kode dipindah ke laptop GTX 1650 Ti, jalankan lagi python utils.py dan python diffusion.py. get_device() seharusnya mencetak cuda, dan semua tes seharusnya tetap lolos.
Dokumentasi. Catat sesi config.py, utils.py, dan diffusion.py di docs/logs/log_ketua.md, lalu commit ke branch-mu. Jangan lupa menyimpan ekspor chat sesi ini di docs/chat_exports/.
Sesi berikutnya adalah model.py: timestep embedding sinusoidal, blok dasar, dan U-Net dengan skip connection (28 → 14 → 7 → 14 → 28). Konstruktornya harus menerima in_channels, base_channels, channel_mults, dan time_emb_dim, sesuai MODEL_PARAMS. Setelah U-Net jadi, kita bisa mengukur memorinya di GTX 1650 Ti untuk menentukan BATCH_SIZE dan EPOCHS final. Mau lanjut ke sana?

okee akan saya lanjutkan sendiri di chat lain untuk model-unet

Siap. Supaya sesi model.py di chat baru konsisten dengan yang sudah jadi, sertakan hal-hal berikut:

PRD dan bagian jobdesk Ketua.
Kunci MODEL_PARAMS (in_channels, base_channels, channel_mults, time_emb_dim). Konstruktor UNet harus memakai nama yang sama persis, karena akan dipanggil sebagai UNet(**MODEL_PARAMS).
Kontrak input dan output: forward(x_t, t) dengan x_t berbentuk (B, 1, 28, 28) dan t bertipe long berbentuk (B,), mengeluarkan prediksi noise berbentuk (B, 1, 28, 28).
Aturan bahwa tidak ada device tetap di kode dan tidak ada angka tetap di luar config.py. Kalau U-Net butuh nilai lain yang belum ada di config, kabari dulu supaya ditambahkan di sana.
Selamat mengerjakan, dan semoga lancar sampai uji memori di GTX 1650 Ti.

Terlampir PRD notebook baru. Ubah config, utils, dan diffusion (kode yang sudah kita buat di chat ini) jadi sel notebook untuk ketua.ipynb, tanpa mengubah logika.

Aturan: sel kode pendek (maksimal sekitar 30 baris, satu fungsi, kelas, atau langkah); banyak sel tidak apa-apa. Sebelum tiap bagian, satu sel markdown singkat (1-3 kalimat, bahasa sederhana, tidak kaku seperti AI). Hapus import antar-file. config jadi SimpleNamespace dengan nama atribut persis sama, BASE_DIR sesuai PRD. Blok main jadi sel uji.

Jangan menulis kode dulu. Tampilkan daftar sel (nomor, judul, isi satu kalimat, total sel). Setelah saya setujui, kirim isinya per kelompok sel.

Saya baca PRD notebook-nya dulu supaya daftar sel sesuai aturannya.

PRD notebook sudah saya baca (Bagian 2, 8, 9, 10 dan jobdesk Ketua). Berikut daftar sel untuk ketua.ipynb, tanpa kode dulu.

Daftar sel
No	Jenis	Judul	Isi (satu kalimat)
1	markdown	Import library	Pengantar singkat bahwa semua import library dikumpulkan di satu sel.
2	kode	Import library	random, numpy, torch, Path, SimpleNamespace, dan matplotlib (yang terakhir hanya jika sel 18 diambil).
3	markdown	2. Config (Ketua)	Menjelaskan bahwa config adalah satu-satunya tempat nilai baseline, dibuat sebagai SimpleNamespace.
4	kode	Config: BASE_DIR	Menentukan root repo dari Path.cwd(), dan memakai folder induk kalau nama foldernya notebooks.
5	kode	Config: nilai baseline	config = SimpleNamespace(...) berisi seed, training (BATCH_SIZE dan EPOCHS bertanda sementara), diffusion, IMAGE_SIZE, dan MODEL_PARAMS.
6	kode	Config: sampling, smoke test, path	Menambahkan atribut sampling, smoke test, dan semua path turunan BASE_DIR ke config yang sama.
7	kode (uji)	Uji config	Memeriksa path absolut dan di bawah root repo, konsistensi nilai (beta, smoke), serta jalur 28 → 14 → 7.
8	markdown	3. Utils (Ketua)	Pengantar singkat tentang seed dan pemilihan device.
9	kode	set_seed	Mengatur seed random, numpy, dan torch tanpa mode deterministik penuh.
10	kode	get_device	Memilih cuda, lalu mps, lalu cpu, tanpa print.
11	kode (uji)	Uji utils	Seed sama menghasilkan angka sama, seed beda menghasilkan angka beda, dan device terpilih bisa menghitung tensor.
12	markdown	7. Diffusion (Ketua)	Pengantar noise schedule, forward process, dan sampling dalam bahasa sederhana.
13	kode	_extract	Fungsi bantu pengambil nilai schedule per t, dibentuk ulang agar cocok dengan batch gambar.
14	kode	Kelas Diffusion: schedule dan forward	__init__ (beta, alpha, alpha-bar dengan skala BETA_REFERENCE_T / T), add_noise, dan sample_timesteps.
15	kode	Diffusion.sample	Reverse process dari noise murni ke gambar, dipasang ke kelas yang sama.
16	kode (uji)	Uji 1: noise schedule	Seed dan device, lalu shape, alpha-bar menurun dari ~1 ke ~0, total beta tetap untuk T = 100 sampai 2000, dan T=10 ditolak.
17	kode (uji)	Uji 2: forward process	Gambar sintetis (kotak putih) makin berisik ke arah T, dan t=T-1 sudah noise murni.
18	kode (uji, tambahan)	Visualisasi forward process	Menampilkan gambar sintetis pada beberapa nilai t dengan matplotlib.
19	kode (uji)	Uji 3: bentuk tertutup	Menambah noise langkah demi langkah menghasilkan statistik yang sama dengan rumus langsung.
20	kode (uji)	Uji 4: sample_timesteps	Tipe long, rentang 0 sampai T-1, dan kedua ujung tercapai.
21	kode (uji)	Uji 5: sampling model tiruan	Shape, rentang [-1, 1], dan t yang diterima model berurutan dari T-1 ke 0.
22	kode (uji)	Uji 6: sampling model oracle	Model yang tahu gambar asli harus menghasilkan gambar itu kembali.
Total: 22 sel (4 markdown dan 18 kode). Tanpa sel 18, totalnya 21.

Yang perlu kamu putuskan
Sel 18 (visualisasi) adalah tambahan. PRD meminta forward process divisualisasikan di uji mandiri Ketua, sedangkan kode kita sekarang hanya mengecek angka MSE. Karena ini kode baru (bukan konversi), saya minta persetujuanmu. Kalau ditolak, sel 18 dan import matplotlib dihapus.
Kelas Diffusion dipecah jadi dua sel (14 dan 15). Satu kelas utuh sekitar 50 baris, melewati batas 30 baris. Saya pecah dengan mendefinisikan sample di sel terpisah, lalu memasangnya ke kelas (Diffusion.sample = ...). Logikanya sama, tapi polanya agak tidak lazim. Alternatifnya satu sel kelas sekitar 50 baris. Saya sarankan pecah.
config dipecah jadi tiga sel (4, 5, 6). Dua puluhan atribut plus komentar tidak muat di satu sel. Hasilnya tetap satu SimpleNamespace dengan nama atribut persis sama.
Perubahan yang tidak bisa dihindari
Perubahan ini bukan perubahan logika, tapi akibat pindah ke notebook:

Import antar-file hilang. import config dan from utils import ... dihapus. Akses seperti config.T tetap sama persis karena config sekarang adalah namespace.
BASE_DIR tidak lagi memakai __file__. Sesuai PRD, nilainya dari Path.cwd(). Pemeriksaan “config.py ada di root” saya ganti dengan pemeriksaan bahwa BASE_DIR bukan folder notebooks.
Uji config. Daftar path di uji config diubah jadi loop getattr supaya muat 30 baris, dan nama telanjang seperti BETA_START menjadi config.BETA_START.
Uji diffusion. Uji diffusion dipecah jadi enam sel yang berbagi variabel (device, d, x0), jadi harus dijalankan berurutan.
Default beta dibaca saat sel kelas dijalankan. Kalau sel config diubah, kamu perlu menjalankan ulang sel kelas juga (atau Restart and Run All, yang memang aturan PRD).
Yang tidak termasuk
Section 0 (judul) tidak termasuk karena kamu hanya meminta tiga bagian. Bisa ditambah saat perakitan.
Section 6 (model/U-Net) dikerjakan di chat lain dan nanti disisipkan antara utils dan diffusion. Uji diffusion tidak bergantung padanya.
Uji end-to-end Diffusion.sample dengan U-Net asli yang belum dilatih, sesuai PRD, baru bisa dibuat setelah UNet ada. Sementara ini sampling diuji dengan model tiruan dan oracle.
Kalau daftar ini sudah oke dan ketiga keputusan di atas sudah kamu putuskan, saya kirim isinya per kelompok:

Kelompok 1: sel 1-7 (import dan config)
Kelompok 2: sel 8-11 (utils)
Kelompok 3: sel 12-15 (diffusion)
Kelompok 4: sel 16-22 (uji diffusion)
Daftar sel saya setujui dengan tiga catatan:
1. Sel 18 (visualisasi forward process) boleh masuk, jadi matplotlib tetap diimpor.
2. Kelas Diffusion jangan dipecah dengan Diffusion.sample = .... Jadikan satu sel kelas utuh dan ringkas komentarnya sampai sekitar 40 baris. Penjelasannya taruh di sel markdown.
3. Config dalam tiga sel boleh, tapi sel itu harus aman dijalankan berurutan dari atas.

Sel markdown: 1-3 kalimat, bahasa sederhana seperti mahasiswa menjelaskan ke teman, tidak kaku, tanpa kalimat pembuka seperti "Berikut adalah".

Logika dan nama tidak boleh berubah. Jangan menambah fitur selain yang sudah disebut.

Kirim kelompok 1 dulu (sel 1-7). Kelompok berikutnya saya minta setelah saya jalankan dan lolos.

Tampilkan semua kode langsung di chat sebagai blok kode, satu blok per sel dengan label "Sel 1", "Sel 2", dan seterusnya. Jangan membuat file, artifact, atau notebook yang harus diunduh. Saya yang menyalinnya sendiri.

Sebelum saya kirim, saya jalankan dulu sel 4-7 di sandbox, dari root dan dari folder notebooks.

Sel 4-7 sudah saya jalankan di sandbox dari root repo dan dari folder notebooks/ (hasilnya sama, BASE_DIR selalu root repo), dan dua kali berturut-turut tanpa error. Sel 2 tidak bisa saya jalankan karena PyTorch tidak terpasang di sandbox.

Sel 1 (markdown)

markdown
## 1. Import library (Ketua)
Semua import dikumpulkan di satu sel ini supaya gampang dicek. Yang dipakai cuma library, tidak ada import antar-file.
Sel 2 (kode)

python
import random
from pathlib import Path
from types import SimpleNamespace

import matplotlib.pyplot as plt
import numpy as np
import torch
Sel 3 (markdown)

markdown
## 2. Config (Ketua)
Semua angka dan path proyek disimpan di sini, jadi sel lain cukup membaca `config.X` tanpa menulis angka sendiri. Isinya dibagi tiga sel (root repo, nilai baseline, lalu sisanya) dan harus dijalankan berurutan dari atas. `BATCH_SIZE` dan `EPOCHS` masih sementara sampai uji memori di GTX 1650 Ti.
Sel 4 (kode)

python
# Root repo: folder kerja saat ini, atau folder induknya kalau dijalankan dari notebooks/
BASE_DIR = Path.cwd()
if BASE_DIR.name == "notebooks":
    BASE_DIR = BASE_DIR.parent
Sel 5 (kode)

python
config = SimpleNamespace(
    # Reproducibility
    SEED=42,  # dipakai set_seed(); satu seed untuk semua anggota
    # Training (baseline)
    LEARNING_RATE=2e-4,  # baseline; boleh ditimpa konfigurasi di EXPERIMENTS
    # SEMENTARA, BELUM FINAL: menunggu uji memori di GTX 1650 Ti (4GB).
    # Jangan dipakai untuk eksperimen tuning sebelum nilai final ditetapkan.
    BATCH_SIZE=64,
    EPOCHS=30,
    NUM_WORKERS=0,  # DataLoader tanpa proses worker (aman di macOS dan Windows)
    # Diffusion (baseline)
    T=1000,  # jumlah timestep baseline; boleh ditimpa konfigurasi di EXPERIMENTS
    # Acuan untuk T=1000; Diffusion menskalakan beta dengan BETA_REFERENCE_T / T
    BETA_START=1e-4,
    BETA_END=0.02,
    BETA_REFERENCE_T=1000,
    # Model
    IMAGE_SIZE=28,  # sisi gambar MNIST; channel ada di MODEL_PARAMS
    # Dipakai sebagai UNet(**config.MODEL_PARAMS) dan disimpan di checkpoint.
    # channel_mults (1, 2, 2) = dua downsampling: 28 -> 14 -> 7
    MODEL_PARAMS={
        "in_channels": 1,
        "base_channels": 64,
        "channel_mults": (1, 2, 2),
        "time_emb_dim": 128,
    },
)
Sel 6 (kode)

python
# Sampling selama training
config.SAMPLE_EVERY_N_EPOCHS = 5  # grid sampel disimpan tiap N epoch
config.NUM_SAMPLE_IMAGES = 16     # jumlah gambar per grid

# Smoke test (uji alur cepat, bukan untuk hasil)
config.SMOKE_TEST = False         # True = subset kecil dan epoch pendek
config.SMOKE_SUBSET_SIZE = 512    # jumlah gambar pada mode smoke test
config.SMOKE_EPOCHS = 2           # jumlah epoch pada mode smoke test
config.SMOKE_SAMPLE_EVERY = 1     # interval grid smoke test (harus <= SMOKE_EPOCHS)

# Path: semuanya diturunkan dari BASE_DIR (sel sebelumnya)
config.BASE_DIR = BASE_DIR
config.DATA_DIR = BASE_DIR / "data"               # unduhan MNIST (tidak di-commit)
config.CHECKPOINT_DIR = BASE_DIR / "checkpoints"  # checkpoint (tidak di-commit)
config.RESULTS_DIR = BASE_DIR / "results"         # hasil (di-commit)
config.LOSS_CURVES_DIR = config.RESULTS_DIR / "loss_curves"
config.SAMPLES_DIR = config.RESULTS_DIR / "samples"
Sel 7 (kode, uji)

python
# Uji config: konsistensi nilai dan path. Tidak membuat folder.
print(f"BASE_DIR       : {config.BASE_DIR}")
for name in ("DATA_DIR", "CHECKPOINT_DIR", "RESULTS_DIR", "LOSS_CURVES_DIR", "SAMPLES_DIR"):
    path = getattr(config, name)
    assert path.is_absolute(), f"{name} harus absolut"
    assert config.BASE_DIR in path.parents, f"{name} harus berada di bawah BASE_DIR"
    print(f"{name:<15}: {path}")

assert config.BASE_DIR.name != "notebooks", "BASE_DIR harus root repo, bukan folder notebooks"

assert 0 < config.BETA_START < config.BETA_END < 1, "beta harus 0 < start < end < 1"
assert config.T > 0 and config.BATCH_SIZE > 0 and config.EPOCHS > 0
assert config.BETA_REFERENCE_T > 0 and config.IMAGE_SIZE > 0
assert config.BETA_END * config.BETA_REFERENCE_T / config.T < 1, "beta akhir (setelah skala) harus < 1"
assert config.SMOKE_SAMPLE_EVERY <= config.SMOKE_EPOCHS, "smoke: N harus <= jumlah epoch"
assert config.SMOKE_SUBSET_SIZE >= config.BATCH_SIZE, "subset smoke harus >= batch size"

# Dua downsampling dari IMAGE_SIZE: 28 -> 14 -> 7
n_down = len(config.MODEL_PARAMS["channel_mults"]) - 1
size = config.IMAGE_SIZE
for _ in range(n_down):
    assert size % 2 == 0, "ukuran gambar harus habis dibagi 2 di tiap downsampling"
    size //= 2
assert n_down == 2 and size == 7, "U-Net harus 28 -> 14 -> 7"

print(f"SEED={config.SEED}  LR={config.LEARNING_RATE}  T={config.T}  "
      f"BATCH_SIZE={config.BATCH_SIZE}(sementara)  EPOCHS={config.EPOCHS}(sementara)")
print(f"BETA_REFERENCE_T={config.BETA_REFERENCE_T}  IMAGE_SIZE={config.IMAGE_SIZE}")
print(f"MODEL_PARAMS   : {config.MODEL_PARAMS}")
print("config OK")
Catatan
Aman dijalankan berurutan.
Sel 4 selalu menghitung BASE_DIR dari Path.cwd(), bukan dari nilai sebelumnya, jadi aman diulang.
Sel 5 membuat config dari nol.
Sel 6 menambahkan atribut dengan penugasan satu per satu (LOSS_CURVES_DIR dihitung dari config.RESULTS_DIR, sama seperti di config.py), jadi aman diulang.
Kalau kamu menjalankan ulang hanya sel 5, atribut dari sel 6 hilang sampai sel 6 dijalankan lagi. Karena itu urutannya selalu 4 → 5 → 6.
Komentar yang berubah. Komentar di sel 5 menyebut EXPERIMENTS (menggantikan “experiments.py”) dan Diffusion menskalakan beta, karena file .py sudah tidak ada. Nilai dan nama atribut tidak berubah.
Sel 7 tepat 30 baris. Satu-satunya perubahan dari uji lama: pemeriksaan “config.py ada di root” diganti pemeriksaan bahwa BASE_DIR bukan folder notebooks. Output terakhirnya sekarang config OK.
Penomoran bergeser setelah sel 14. Karena kelas Diffusion jadi satu sel, Sel 14 menjadi kelas utuh dan uji-ujinya menjadi Sel 15-20. Total sekarang 21 sel. Kelompok 2 (utils, Sel 8-11) tidak terpengaruh.
Silakan jalankan Sel 1-7 berurutan. Kalau lolos (output terakhir config OK), kabari saya dan kita lanjut ke kelompok 2.

Sel 1-7 lolos, output terakhir "config OK". Lanjut kelompok 2 (utils, sel 8-11). Format sama: blok kode di chat per sel, tanpa file. Command di kode dirapihkan jangan terlalu banyak command kecuali memang penting

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

03
haloo

Halo! Ada yang bisa saya bantu hari ini?

prd_final_mini_ddpm.md
prd_final_mini_ddpm.md
MD
[CAK4KBB3 2026-1] Panduan Proyek 1 - Vibe Coding (1).pdf
pdf

config.py
config.py
120 baris
PY
diffusion.py
diffusion.py
155 baris
PY
utils.py
utils.py
74 baris
PY
Saya ketua kelompok 3 orang untuk tugas besar ini. Terlampir PDF panduan, PRD, dan config.py, utils.py, diffusion.py yang sudah jadi dan lolos uji. Tolong ikuti PRD.

Tugas sesi ini: model.py di root repo, tanpa file lain.

Isi: timestep embedding sinusoidal, blok dasar U-Net, dan UNet lengkap dengan skip connection dan dua downsampling (28 → 14 → 7). Konstruktor UNet harus menerima argumen yang cocok dengan kunci MODEL_PARAMS di config.py (UNet(**MODEL_PARAMS)). Input (x, t): x berbentuk (B, 1, 28, 28), t berbentuk (B,) bertipe long. Output: prediksi noise (B, 1, 28, 28).

Sebelum kode, jelaskan dulu dengan bahasa sederhana: apa itu timestep embedding dan mengapa disuntikkan ke blok U-Net, serta fungsi skip connection.

Uji di blok if __name__ == "__main__": shape output sama dengan input, jumlah parameter dicetak, dan satu langkah backward berjalan tanpa error. Pakai input acak.

Komentar di kode seperlunya saja. Tampilkan kode langsung di chat, bukan file unduhan. Jangan menyalin dari tutorial.

Locating the requirements document among uploaded files.
Saya baca PRD-nya dulu supaya model.py sesuai ketentuan.

Penjelasan singkat
Timestep embedding. t hanyalah satu bilangan bulat, misalnya 37 atau 850, dan jaringan saraf sulit memakai bilangan mentah seperti itu. Embedding sinusoidal mengubahnya menjadi vektor panjang (di sini 128 angka) berisi gelombang sin dan cos dengan frekuensi berbeda-beda. Prinsipnya mirip jam: jarum detik, menit, dan jam bersama-sama menandai satu waktu secara unik. Frekuensi rendah membedakan t yang jauh (50 vs 900), dan frekuensi tinggi membedakan t yang berdekatan (50 vs 51). Dua t yang berdekatan menghasilkan vektor yang mirip, jadi model bisa menggeneralisasi antar-timestep.

Mengapa disuntikkan ke blok U-Net. Gambar masukan hanya berisi piksel, tanpa penanda seberapa berisik gambar itu. Padahal tugasnya berbeda jauh: pada t kecil noise sedikit dan model hanya merapikan detail halus, sedangkan pada t besar gambar hampir noise murni dan model harus menebak struktur digit. Satu jaringan dengan bobot yang sama melayani semua t, jadi ia harus diberi tahu t berapa yang sedang ditangani. Karena itu embedding dimasukkan ke setiap blok (ditambahkan ke feature map di tengah blok), supaya informasi t tidak hilang di lapisan yang dalam.

Skip connection. Di jalur turun (28 → 14 → 7) gambar diperkecil, dan detail halus seperti tepi dan lengkung goresan ikut hilang. Skip connection menyimpan feature map tiap level dan menempelkannya (concatenate) ke level yang ukurannya sama di jalur naik (7 → 14 → 28). Jalur naik jadi punya dua sumber: gambaran global dari bagian dalam dan detail spasial dari jalur turun. Ini penting karena noise yang diprediksi harus sejajar piksel demi piksel dengan inputnya. Tanpa skip, hasil upsampling cenderung buram. Skip juga memudahkan aliran gradien saat training.

Kode model.py
python
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
Catatan
Belum dijalankan. PyTorch tidak bisa dipasang di lingkungan saya, jadi kode ini belum saya jalankan. Saya hanya menelusuri shape dan channel secara manual: skip 28×28 (64 ch), 14×14 (128 ch), dan 7×7 (128 ch) cocok dengan concat di jalur naik (masing-masing 256, 256, 192 channel masuk). Tolong jalankan python model.py dari root repo. Kalau ada error, salin pesannya utuh ke log, seperti aturan PRD.
Argumen konstruktor (in_channels, base_channels, channel_mults, time_emb_dim) sengaja tanpa nilai default, supaya tidak ada angka tetap di luar config.py.
import config dipakai di model.py hanya untuk blok uji. Jika ingin model.py tidak bergantung pada config.py sama sekali, impor itu bisa dipindah ke dalam blok __main__.
Satu ResBlock per level. Ini menjaga memori dan kecepatan di GTX 1650 Ti 4 GB. Jumlah parameter akan tercetak saat uji, jadi bisa kamu bandingkan dengan hasil uji memori batch size.
Log. Sesi ini sebaiknya dicatat di docs/logs/log_ketua.md dengan target modul “Timestep embedding + U-Net”.

Tolong tulis ulang README.md dan requirements.txt sesuai PRD, di root repo, tampilkan langsung di chat. Jangan memakai placeholder <ISI>.

train.py dan sample.py belum jadi. Di bagian "Cara menjalankan", tulis perintah sesuai PRD: python train.py (memakai baseline) dan python train.py <nama_konfigurasi> untuk eksperimen, serta python sample.py. Beri catatan singkat "(disesuaikan setelah train.py dan sample.py jadi)" di dua tempat itu saja.

Bagian lainnya sama seperti sebelumnya.

Versi sebelumnya tidak ada di percakapan ini, jadi saya menyusun keduanya langsung dari PRD. Kalau versi lama punya bagian tambahan, tempel saja ke sini dan saya sesuaikan.

requirements.txt
text
# WAJIB: Python 3.14, lihat README
torch==2.14.0
torchvision==0.29.0
numpy>=2.3.2
matplotlib>=3.10.7
README.md
markdown
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
Catatan
Versi PyTorch. Saya memakai torch==2.14.0 dan torchvision==0.29.0, pasangan yang disebut di pengumuman resmi PyTorch. Menurut dokumentasi torchvision, rilis PyTorch 2.9 ke atas mendukung Python 3.14. PyTorch 2.15 dijadwalkan rilis hari ini, tetapi saya belum memastikan pasangan torchvision-nya, jadi saya tidak memakainya. Cek sekali di halaman get-started PyTorch sebelum kalian semua memasang.
numpy dan matplotlib memakai batas bawah (>=), bukan versi persis. Versi 2.3.2 dan 3.10.7 adalah rilis pertama yang saya ketahui menyediakan wheel Python 3.14. Kalau ingin hasil instal identik antar anggota, jalankan pip freeze di laptop ketua setelah semuanya terpasang dan ganti baris ini dengan versi persis.
Catatan “(disesuaikan setelah train.py dan sample.py jadi)” hanya ada di dua tempat: judul bagian Training dan judul bagian Sampling.
<nama_konfigurasi> saya biarkan karena itu bentuk perintah yang kamu minta. README menjelaskan bahwa namanya diambil dari experiments.py.

Terlampir PRD notebook baru. Ubah model (kode U-Net di chat ini) jadi sel notebook untuk ketua.ipynb tanpa mengubah logika. Sel-sel ini nanti disisipkan di antara bagian utils dan bagian diffusion. Di notebook sudah ada: config (SimpleNamespace dengan atribut huruf besar seperti config.MODEL_PARAMS, config.IMAGE_SIZE, config.T, config.SEED), set_seed, dan get_device. Import library sudah ada di Sel 2, termasuk math dan torch.nn as nn. Jangan membuat sel import baru dan jangan menulis ulang Sel 2.

Aturan: sel kode maksimal sekitar 30 baris, satu kelas atau satu langkah. Sel markdown 1-3 kalimat, bahasa sederhana seperti mahasiswa menjelaskan ke teman, tidak kaku, tanpa kalimat pembuka seperti "Berikut adalah". Hapus semua import antar-file. Blok if __name__ == "__main__" diubah jadi sel uji. Nama kelas dan fungsi tidak boleh berubah (SinusoidalTimeEmbedding, ResBlock, Downsample, Upsample, UNet). Jangan menambah fitur.

Jangan menulis kode dulu. Tampilkan daftar sel dulu (nomor, jenis, judul, isi satu kalimat, dan total sel), lalu tunggu saya setujui. Setelah itu tampilkan semua kode langsung di chat sebagai blok kode, satu blok per sel dengan label "Sel 1", "Sel 2", dan seterusnya. Jangan membuat file, artifact, atau notebook yang harus diunduh.

Ini rencana sel untuk bagian model (bagian 6 di PRD notebook). Belum ada kode.

No	Jenis	Judul	Isi
1	Markdown	Model (Ketua)	Judul bagian dan pemilik, plus satu kalimat bahwa isinya timestep embedding, blok dasar, dan U-Net.
2	Kode	_group_norm	Fungsi kecil pembuat GroupNorm dengan jumlah grup terbesar dari (8, 4, 2, 1) yang habis membagi jumlah channel.
3	Markdown	Timestep embedding	Penjelasan sederhana kenapa t diubah jadi vektor sin dan cos, dan kenapa model perlu tahu t.
4	Kode	SinusoidalTimeEmbedding	Mengubah t (B,) menjadi vektor (B, dim) berisi sin dan cos berbagai frekuensi.
5	Markdown	ResBlock	Penjelasan bahwa blok ini dua konvolusi dengan embedding waktu ditambahkan di tengah, plus jalan pintas residual.
6	Kode	ResBlock	Blok dasar U-Net: norm, konvolusi 3x3, tambah embedding waktu, norm, konvolusi, lalu jumlahkan dengan shortcut.
7	Markdown	Downsample dan Upsample	Penjelasan cara gambar diperkecil (28→14→7) dan dibesarkan lagi (7→14→28).
8	Kode	Downsample	Konvolusi stride 2 yang menyusutkan ukuran gambar setengahnya.
9	Kode	Upsample	Perbesar 2x dengan nearest, lalu konvolusi 3x3.
10	Markdown	UNet	Penjelasan jalur turun, tengah, jalur naik, dan fungsi skip connection.
11	Kode	UNet (kelas, __init__)	Menyusun semua lapisan dari in_channels, base_channels, channel_mults, time_emb_dim.
12	Kode	UNet.forward	Alur maju: embedding waktu, turun sambil menyimpan skip, tengah, naik sambil menempel skip, keluaran noise.
13	Markdown	Uji model	Satu-dua kalimat tentang tiga hal yang diuji: shape, pengaruh t, dan backward.
14	Kode	Uji shape dan jumlah parameter	Bangun UNet(**config.MODEL_PARAMS), cetak jumlah parameter, cek shape output sama dengan input.
15	Kode	Uji pengaruh t	Cek output berbeda untuk t=0 dan t=T-1.
16	Kode	Uji backward	Satu langkah backward, semua parameter harus dapat gradien yang valid.
Total: 16 sel (6 markdown, 10 kode). Import config, utils, dan __main__ hilang, dan semua nama kelas dan fungsi tetap.

Satu hal perlu keputusanmu. Kelas UNet panjangnya sekitar 55 baris (__init__ sekitar 33, forward sekitar 20), jadi tidak muat di batas 30 baris. Saya mengusulkan dua cara:

A (usulan saya): dipecah jadi sel 11 dan 12 seperti di tabel. Sel 11 berisi kelas dengan __init__. Sel 12 mendefinisikan forward(self, x, t) yang isinya persis sama, lalu menempelkannya dengan UNet.forward = forward dan del forward. Logika tidak berubah, hanya ada dua baris perekat tambahan.
B: UNet utuh dalam satu sel sekitar 55 baris. Rapi, tapi melanggar aturan maksimal sekitar 30 baris. Rencananya jadi 15 sel (sel 12 hilang).
Kalau kamu setuju rencana ini dan memilih A atau B, saya tampilkan semua kodenya.

Rencana sel saya setujui, pilih B: kelas UNet utuh dalam satu sel (tanpa UNet.forward = forward). Ringkas komentar di dalamnya supaya sekitar 45-50 baris; penjelasannya taruh di sel markdown. Jadi totalnya 15 sel, sel 12 hilang dan penomoran bergeser.

Tampilkan semua kodenya sekarang, per kelompok sel: kelompok 1 sel 1-9, kelompok 2 sel 10-15. Blok kode di chat, tanpa file. Logika dan nama tidak boleh berubah.

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

okee aman sampe cell terakhir

Memeriksa keluaran dan kehilangan model.
Mantap, sel uji terakhir lolos. Loss 1,1063 untuk output acak melawan noise acak memang wajar: dua tensor acak independen menghasilkan MSE sekitar 1, ditambah sedikit karena output model belum dilatih.

Sebelum lanjut, ada beberapa hal yang sebaiknya dilakukan:

Cek juga output Sel 13 (jumlah parameter, shape) dan Sel 14 (pengaruh t). Kalau semuanya sudah muncul tanpa error, bagian model selesai.
Catat sesi ini di docs/logs/log_ketua.md dengan target modul “Model (timestep embedding, ResBlock, U-Net)”, dan simpan share link chat-nya.
Sebelum commit ketua.ipynb, jalankan Clear All Outputs sesuai PRD.
Berikutnya bagian diffusion (bagian 7). Kalau mau, saya ubah Diffusion jadi sel notebook dengan cara yang sama: daftar sel dulu, tunggu persetujuanmu, baru kodenya.


04
haloo

Halo! Ada yang bisa aku bantu hari ini?

prd_final_miniddpm_notebook.md
prd_final_miniddpm_notebook.md
MD
azigha_(ketua).ipynb
azigha_(ketua).ipynb
IPYNB
A.ipynb
A.ipynb
IPYNB
B.ipynb
B.ipynb
IPYNB
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

Planning the file-reading stage before any changes.
Aku baca dulu isi kelima file supaya angka sel yang dibuang akurat.

Tahap 1: pemahaman

Aku sudah membaca PRD dan membuka ketiga notebook untuk menghitung selnya.

Tujuan. Dosen minta hasil akhir berupa satu file .ipynb yang berdiri sendiri. Tugasku merakit pekerjaan Ketua, Teman A, dan Teman B menjadi MiniDDPM.ipynb di root repo. Isi kodenya tidak boleh berubah, hanya urutan, label, komentar, dan sel markdown tertentu yang dirapikan. Hasilnya harus bersih dari output dan nomor eksekusi.

Isi tiap notebook dan bagian yang masuk.

azigha_(ketua).ipynb punya 36 sel dan semuanya masuk. Isinya bagian 1 (import), 2 (config), 3 (utils), 6 (model), dan 7 (diffusion), lengkap dengan sel uji masing-masing.
A.ipynb punya 23 sel. Yang masuk bagian 4 (dataset) dan bagian 5 (visualize), termasuk sel uji dan sel markdown penjelasnya.
B.ipynb punya 50 sel. Yang masuk bagian 8 (experiments), 9 (train), 10 (sample), 12 (eksekusi baseline), dan 13 (eksperimen dan hasil), termasuk sel uji.
Urutan final mengikuti nomor bagian: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13. Tidak ada bagian 11 karena sel uji sudah menempel di tiap bagian.
Sel yang dibuang.

Di A.ipynb ada 8 sel yang dibuang:
6 sel kode berlabel “SALINAN SEMENTARA” (milik Ketua yang disalin untuk uji).
1 sel “# Import Teman A”.
1 sel markdown judul “# Notebook kerja Syaikha A”.
Sisa 15 sel masuk.
Di B.ipynb ada 20 sel yang dibuang:
18 sel kode berlabel “SALINAN SEMENTARA”, termasuk pengganti get_dataloader dan model tiruan.
1 sel “# Import Teman B”.
1 sel markdown judul “# Notebook kerja Teman B”.
Sisa 30 sel masuk.
Di notebook Ketua tidak ada yang dibuang. Sel import Ketua diperluas jadi sel import utama yang memuat gabungan semua library. Dari A menambah copy, tempfile, DataLoader, Dataset, Subset, datasets, transforms, dan make_grid. Dari B menambah json dan time, sementara copy sudah ada dari A. Aku sudah cek bahwa tidak ada import tersembunyi di sel kode lain yang dipertahankan.
Perkiraan total sel final: 1 judul proyek + 36 + 15 + 30 = 82.
Yang dikurangi.

Di kode, komentar yang hanya mengulang isi barisnya dihapus. Komentar yang menjelaskan hal tidak jelas dipertahankan, sekitar satu sampai dua per sel. Docstring multi-baris jadi satu baris. Pemisahan komentar memakai tokenize agar # di dalam string aman. Skrip membandingkan ast.dump sebelum dan sesudah, docstring diabaikan, lalu mencetak jumlah sel yang strukturnya berubah, yang harus 0.
Di markdown, aku sudah memeriksa semua sel. Yang melanggar aturan 8 (lebih dari tiga kalimat atau memakai titik koma) kutemukan di bagian 2 Config dan bagian 7 Diffusion, dan akan kutampilkan teks sebelum dan sesudahnya di Tahap 2. Judul bagian juga disamakan menjadi Ketua, Teman A, dan Teman B, jadi “Syaikha A” di judul bagian 4 berubah menjadi “Teman A”. Tidak ada markdown yang kuubah tanpa persetujuanmu.
Yang sengaja tidak diubah. Semua baris kode, nama variabel dan fungsi, urutan logika, isi sel uji, serta sel markdown penjelas yang sudah memenuhi aturan. Panah “→” di beberapa markdown bukan em dash atau en dash, jadi kubiarkan. Teks bebas seperti “ketua” huruf kecil di badan markdown juga tidak kuubah. Hanya label pemilik di judul bagian yang disamakan.

Hal yang ingin kukonfirmasi.

Sel markdown berjudul “## 2. Config (Ketua)” dan sel-sel yang punya judul bagian akan dirapikan hanya sebatas aturan 8. Setujukah kamu kalau kalimat yang menyebut “GTX 1650 Ti” dan “masih sementara” tetap dipertahankan, atau mau dibuang karena bisa membingungkan dosen?
Metadata notebook: Ketua memakai kernel “venv (3.14.6)”, A dan B memakai “3.14.10”. Aku berencana memakai metadata Ketua untuk file final. Setuju?
Kata “Syaikha” muncul di judul A dan B kerja yang dibuang, jadi tidak akan ada di notebook final. Kalau ada kata itu di sel lain yang masuk, akan kutandai di Tahap 2.
Beberapa sel kode di notebook Ketua melebihi batas sekitar 30 baris menurut PRD (misalnya UNet 50 baris, train 26 baris masih aman). Karena kamu minta kode tidak diubah, aku tidak akan memecahnya. Aman?
Silakan koreksi atau setujui, lalu aku lanjut ke Tahap 2.
Pemahaman Tahap 1 saya setujui. Ini jawaban untuk empat pertanyaanmu dan beberapa tambahan. Pesan ini menggantikan semua balasan saya sebelumnya.

Kalimat dan komentar yang menyebut GTX 1650 Ti jangan kamu ubah. Saya akan menghapusnya sendiri di notebook final.
Pakai metadata notebook Ketua untuk file final.
Kata Syaikha tidak boleh muncul di notebook final. Kalau ada di sel lain yang masuk, tandai di Tahap 2.
Jangan memecah sel yang lebih dari sekitar 30 baris. UNet dan Diffusion tetap satu sel utuh.
Tambahan: notebook final tidak memuat sel uji karena tiap bagian sudah diuji di notebook kerja masing-masing. Buang semua sel kode yang berisi assert, dan buang sel markdown yang hanya menjelaskan sel uji (misalnya yang diawali "Sel uji ini gantinya" dan "Tiga hal yang dicek"). Mode smoke di config dan di dalam fungsi tetap dipertahankan, jangan diubah.

Setelah sel uji dibuang, dua sel akan rusak karena memakai variabel dari sel uji. Pertama sel "Contoh gambar dari satu batch" di bagian Dataset yang memakai variabel batch. Kedua sel "Visualisasi forward process" di bagian Diffusion yang memakai variabel d, x0, noise, dan device. Buat keduanya berdiri sendiri dengan menambah beberapa baris di awal sel itu untuk membuat variabel yang dibutuhkan, tanpa mengubah baris lainnya. Catat keduanya sebagai dua sel yang sengaja berubah, terpisah dari pengecekan ast.dump.

Tahap 3 tetap berupa skrip Python seperti rencana semula, bukan mengirim sel satu per satu.

Sekarang lanjut ke Tahap 2: tampilkan tabel daftar sel notebook final, total sel (perkiraan saya sekitar 58), teks sebelum dan sesudah untuk sel markdown yang berubah, dan teks sebelum dan sesudah untuk dua sel yang berdiri sendiri. Lalu berhenti dan tunggu persetujuan saya.

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