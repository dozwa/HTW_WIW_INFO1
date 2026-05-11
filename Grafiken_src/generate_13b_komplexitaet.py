"""Generiert die Big-O-Wachstumskurven fuer Foliensatz 13b."""
import math

import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 12,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 150,
    'savefig.dpi': 150,
})

GRAFIKEN_DIR = 'Grafiken'


def generate_komplexitaet_kurven():
    fig, ax = plt.subplots(figsize=(10, 5))

    # n von 1 bis 50 -- gross genug, dass O(2^n) sichtbar explodiert.
    n_max = 30
    xs = list(range(1, n_max + 1))

    o_1 = [1 for _ in xs]
    o_log = [math.log2(n) for n in xs]
    o_n = [n for n in xs]
    o_nlogn = [n * math.log2(n) for n in xs]
    o_n2 = [n * n for n in xs]
    o_2n = [2 ** n for n in xs]

    ax.plot(xs, o_1, label="O(1)", linewidth=2)
    ax.plot(xs, o_log, label="O(log n)", linewidth=2)
    ax.plot(xs, o_n, label="O(n)", linewidth=2)
    ax.plot(xs, o_nlogn, label="O(n log n)", linewidth=2)
    ax.plot(xs, o_n2, label="O(n^2)", linewidth=2)
    ax.plot(xs, o_2n, label="O(2^n)", linewidth=2, linestyle="--")

    ax.set_xlabel("Eingabegroesse n")
    ax.set_ylabel("Anzahl Operationen")
    ax.set_title("Wachstum der Komplexitaetsklassen (logarithmische Skala)")
    ax.set_yscale("log")
    ax.set_ylim(0.5, 1e10)
    ax.set_xlim(1, n_max)
    ax.grid(True, which="both", alpha=0.3)
    ax.legend(loc="upper left", ncol=2, frameon=True)

    fig.tight_layout()
    out = f"{GRAFIKEN_DIR}/13b_komplexitaet_kurven.png"
    fig.savefig(out)
    plt.close(fig)
    print(f"  ✓ {out}")


if __name__ == '__main__':
    generate_komplexitaet_kurven()
