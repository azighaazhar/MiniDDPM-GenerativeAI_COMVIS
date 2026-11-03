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