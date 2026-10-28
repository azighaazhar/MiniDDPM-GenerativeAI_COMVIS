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