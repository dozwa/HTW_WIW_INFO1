"""Generiert die JOIN-Visualisierungen fuer Foliensatz 23.

Erzeugt:
  Grafiken/23_joins_mengen.png     -- Mengen-/Venn-Darstellung: INNER JOIN vs. LEFT JOIN.
  Grafiken/23_joins_tabellen.png   -- konkretes Beispiel: kunde + bestellung →
                                      INNER-JOIN-Ergebnis vs. LEFT-JOIN-Ergebnis (mit NULL).
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams.update({
    'font.size': 12,
    'figure.dpi': 150,
    'savefig.dpi': 150,
    'font.family': 'DejaVu Sans',
})

GRAFIKEN_DIR = 'Grafiken'
BLAU = "#2a5d8f"
LILA = "#7a3b9c"
ORANGE = "#e07b3a"
GRAU = "#444444"

AX, AY = -0.45, 0.0
BX, BY = 0.45, 0.0
R = 0.85


def _masks(res=900):
    x = np.linspace(-1.8, 1.8, res)
    y = np.linspace(-1.1, 1.1, res)
    X, Y = np.meshgrid(x, y)
    in_a = (X - AX) ** 2 + (Y - AY) ** 2 <= R ** 2
    in_b = (X - BX) ** 2 + (Y - BY) ** 2 <= R ** 2
    return in_a, in_b, (x[0], x[-1], y[0], y[-1])


def _venn_panel(ax, region, titel, sql):
    in_a, in_b, extent = _masks()
    rgba = np.zeros(region.shape + (4,))
    r, g, b = (int(ORANGE[1:3], 16) / 255, int(ORANGE[3:5], 16) / 255, int(ORANGE[5:7], 16) / 255)
    rgba[..., 0], rgba[..., 1], rgba[..., 2] = r, g, b
    rgba[..., 3] = np.where(region, 0.55, 0.0)
    ax.imshow(rgba, extent=extent, origin='lower', interpolation='nearest', aspect='auto', zorder=1)
    ax.add_patch(mpatches.Circle((AX, AY), R, fill=False, lw=2.4, edgecolor=BLAU, zorder=3))
    ax.add_patch(mpatches.Circle((BX, BY), R, fill=False, lw=2.4, edgecolor=LILA, zorder=3))
    ax.text(AX - R * 0.45, R * 0.85, "kunde", fontsize=13, fontweight='bold', color=BLAU,
            ha='center', zorder=4)
    ax.text(BX + R * 0.45, R * 0.85, "bestellung", fontsize=13, fontweight='bold', color=LILA,
            ha='center', zorder=4)
    ax.text(0, -R * 0.55, "ON kunde.kunde_id\n= bestellung.kunde_id", fontsize=8.5, ha='center',
            color=GRAU, zorder=4)
    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-1.55, 1.45)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(titel, fontsize=14, fontweight='bold', color=ORANGE, pad=6)
    ax.text(0, -1.42, sql, fontsize=9.5, ha='center', family='monospace', color=GRAU)


def generate_mengen():
    in_a, in_b, _ = _masks()
    fig, axes = plt.subplots(1, 2, figsize=(15, 6.4))
    _venn_panel(axes[0], in_a & in_b, "INNER JOIN — nur Treffer in BEIDEN",
                "FROM kunde JOIN bestellung ON ...")
    _venn_panel(axes[1], in_a, "LEFT JOIN — ALLE links, passende rechts",
                "FROM kunde LEFT JOIN bestellung ON ...")
    fig.suptitle("JOIN als Mengenoperation: welche Zeilen landen im Ergebnis?",
                 fontsize=15, fontweight='bold')
    fig.text(0.5, 0.02, "Orange = diese Zeilen stehen im Ergebnis.   Bei LEFT JOIN bekommen "
                        "Kund:innen ohne Bestellung NULL in den bestellung-Spalten.",
             ha='center', fontsize=10, color=GRAU)
    fig.tight_layout(rect=(0, 0.05, 1, 0.95))
    out = f"{GRAFIKEN_DIR}/23_joins_mengen.png"
    fig.savefig(out, bbox_inches='tight')
    plt.close(fig)
    print(f"→ geschrieben: {out}")


# ----------------------------------------------------------------------------

def _table(ax, x, y, title, cols, rows, cw=0.115, rh=0.072, null_cells=()):
    n = len(cols)
    ax.text(x + n * cw / 2, y + rh + 0.012, title, ha='center', fontsize=10.5, fontweight='bold',
            color=BLAU)
    for j, c in enumerate(cols):
        ax.add_patch(mpatches.Rectangle((x + j * cw, y), cw, rh, facecolor=BLAU, edgecolor='white', lw=1))
        ax.text(x + j * cw + cw / 2, y + rh / 2, c, ha='center', va='center', color='white',
                fontsize=8.6, fontweight='bold')
    for i, r in enumerate(rows):
        yy = y - (i + 1) * rh
        for j, val in enumerate(r):
            isnull = (i, j) in null_cells
            ax.add_patch(mpatches.Rectangle((x + j * cw, yy), cw, rh,
                         facecolor=("#f3e6e6" if isnull else 'white'), edgecolor=BLAU, lw=0.8))
            ax.text(x + j * cw + cw / 2, yy + rh / 2, val, ha='center', va='center', fontsize=8.4,
                    color=(ORANGE if isnull else 'black'), fontweight=('bold' if isnull else 'normal'))
    return (x, y - len(rows) * rh, n * cw, (len(rows) + 1) * rh)


def generate_tabellen():
    fig, ax = plt.subplots(figsize=(15, 8.0))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title("Derselbe JOIN, konkret: kunde + bestellung", fontsize=15, fontweight='bold', color=BLAU)

    # Quelltabellen oben
    _table(ax, 0.04, 0.80, "kunde", ["kunde_id", "name"],
           [["1", "Anna"], ["2", "Max"], ["3", "Lena"]], cw=0.10)
    _table(ax, 0.30, 0.80, "bestellung", ["bestell_id", "kunde_id", "betrag"],
           [["10", "1", "89.95"], ["11", "1", "109.00"], ["12", "2", "135.50"]], cw=0.10)
    ax.text(0.17, 0.50, "Lena (3) hat keine Bestellung.", ha='center', fontsize=9.5, color=ORANGE)

    # Pfeile nach unten
    ax.annotate("", xy=(0.30, 0.30), xytext=(0.22, 0.62), arrowprops=dict(arrowstyle="-|>", color=BLAU, lw=1.8))
    ax.annotate("", xy=(0.70, 0.30), xytext=(0.40, 0.62), arrowprops=dict(arrowstyle="-|>", color=BLAU, lw=1.8))
    ax.text(0.18, 0.40, "INNER JOIN", fontsize=11, fontweight='bold', color=ORANGE, rotation=20)
    ax.text(0.56, 0.42, "LEFT JOIN", fontsize=11, fontweight='bold', color=ORANGE, rotation=-20)

    # Ergebnisse unten
    _table(ax, 0.06, 0.27, "INNER JOIN — nur passende Paare", ["name", "bestell_id", "betrag"],
           [["Anna", "10", "89.95"], ["Anna", "11", "109.00"], ["Max", "12", "135.50"]], cw=0.105)
    _table(ax, 0.50, 0.27, "LEFT JOIN — alle Kund:innen", ["name", "bestell_id", "betrag"],
           [["Anna", "10", "89.95"], ["Anna", "11", "109.00"], ["Max", "12", "135.50"],
            ["Lena", "NULL", "NULL"]], cw=0.105, null_cells=((3, 1), (3, 2)))

    ax.text(0.5, 0.02, "INNER JOIN \"vergisst\" Lena — sie hat keinen Treffer.   LEFT JOIN behält sie und "
                       "füllt die fehlenden Werte mit NULL.", ha='center', fontsize=10, color=GRAU)
    fig.tight_layout()
    out = f"{GRAFIKEN_DIR}/23_joins_tabellen.png"
    fig.savefig(out, bbox_inches='tight')
    plt.close(fig)
    print(f"→ geschrieben: {out}")


if __name__ == "__main__":
    generate_mengen()
    generate_tabellen()
