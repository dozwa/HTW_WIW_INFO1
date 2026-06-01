"""Generiert das Venn-Diagramm der vier Mengenoperationen fuer Foliensatz 08.

Erzeugt:
  Grafiken/08_mengenoperationen_venn.png   -- 1x4-Streifen: Vereinigung, Schnitt,
                                              Differenz, symmetrische Differenz
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams.update({
    'font.size': 13,
    'figure.dpi': 150,
    'savefig.dpi': 150,
    'font.family': 'DejaVu Sans',
})

GRAFIKEN_DIR = 'Grafiken'

# Geometrie der beiden Kreise (A links, B rechts, ueberlappend)
AX, AY = -0.42, 0.0
BX, BY = 0.42, 0.0
R = 0.78

FILL = "#e07b3a"   # Orange (passend zu den exercisebox-Folien)
EDGE_A = "#2a5d8f"
EDGE_B = "#7a3b9c"


def _masks(res=900):
    x = np.linspace(-1.7, 1.7, res)
    y = np.linspace(-1.15, 1.15, res)
    X, Y = np.meshgrid(x, y)
    in_a = (X - AX) ** 2 + (Y - AY) ** 2 <= R ** 2
    in_b = (X - BX) ** 2 + (Y - BY) ** 2 <= R ** 2
    extent = (x[0], x[-1], y[0], y[-1])
    return in_a, in_b, extent


def _draw_panel(ax, region, titel, mengen_notation, py_operator):
    in_a, in_b, extent = _masks()

    # gefuellte Region als halbtransparentes RGBA-Bild
    rgba = np.zeros(region.shape + (4,))
    r, g, b = (int(FILL[1:3], 16) / 255, int(FILL[3:5], 16) / 255,
               int(FILL[5:7], 16) / 255)
    rgba[..., 0] = r
    rgba[..., 1] = g
    rgba[..., 2] = b
    rgba[..., 3] = np.where(region, 0.55, 0.0)
    ax.imshow(rgba, extent=extent, origin='lower', interpolation='nearest',
              aspect='auto', zorder=1)

    # Kreis-Umrandungen
    ax.add_patch(mpatches.Circle((AX, AY), R, fill=False, lw=2.2,
                                 edgecolor=EDGE_A, zorder=3))
    ax.add_patch(mpatches.Circle((BX, BY), R, fill=False, lw=2.2,
                                 edgecolor=EDGE_B, zorder=3))

    # Mengen-Labels A und B
    ax.text(AX - R * 0.62, R * 0.78, "A", fontsize=18, fontweight='bold',
            color=EDGE_A, ha='center', va='center', zorder=4)
    ax.text(BX + R * 0.62, R * 0.78, "B", fontsize=18, fontweight='bold',
            color=EDGE_B, ha='center', va='center', zorder=4)

    ax.set_xlim(-1.7, 1.7)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    ax.set_title(titel, fontsize=15, fontweight='bold', pad=4)
    # Mengennotation unter dem Diagramm
    ax.text(0, -1.32, mengen_notation, fontsize=16, ha='center', va='center')


def generate_venn():
    in_a, in_b, _ = _masks()

    fig, axes = plt.subplots(1, 4, figsize=(16, 4.6))

    _draw_panel(axes[0], in_a | in_b,
                "Vereinigung  ·  A | B", r"$A \cup B$", "A | B")
    _draw_panel(axes[1], in_a & in_b,
                "Schnittmenge  ·  A & B", r"$A \cap B$", "A & B")
    _draw_panel(axes[2], in_a & ~in_b,
                "Differenz  ·  A - B", r"$A \setminus B$", "A - B")
    _draw_panel(axes[3], in_a ^ in_b,
                "Symm. Differenz  ·  A ^ B", r"$A \,\triangle\, B$", "A ^ B")

    fig.tight_layout()
    out = f"{GRAFIKEN_DIR}/08_mengenoperationen_venn.png"
    fig.savefig(out, bbox_inches='tight')
    plt.close(fig)
    print(f"→ geschrieben: {out}")


if __name__ == "__main__":
    generate_venn()
