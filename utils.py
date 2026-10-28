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