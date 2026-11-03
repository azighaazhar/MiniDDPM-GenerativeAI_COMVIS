# Hasil eksperimen

Loss = rata-rata MSE noise per epoch. Kolom catatan visual diisi manual dari grid akhir.

| Konfigurasi | Learning rate | T | Epoch | Loss akhir | Loss minimum | Rata-rata detik/epoch | Catatan visual |
|---|---|---|---|---|---|---|---|
| baseline | 0.0002 | 1000 | 20 | 0.0222 | 0.0221 | 85.8 | Sebagian besar digit jelas, 1 sampai 2 gambar bentuknya aneh |
| lr_1e-4 | 0.0001 | 1000 | 20 | 0.0224 | 0.0223 | 86.7 | Mirip baseline, ada 1 gambar berbentuk gumpalan |
| lr_5e-4 | 0.0005 | 1000 | 20 | 0.0221 | 0.0221 | 86.9 | Mirip baseline, 1 gambar berbentuk tanda plus |
| T_250 | 0.0002 | 250 | 20 | 0.0218 | 0.0218 | 86.3 | Digit jelas dan agak tebal, goresan bersih |
| T_500 | 0.0002 | 500 | 20 | 0.0219 | 0.0219 | 86.5 | Sebagian besar digit jelas, 2 gambar bentuknya aneh |