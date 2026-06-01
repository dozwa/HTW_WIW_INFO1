"""Generiert das Schaubild "Excel vs. Datenbank" fuer Foliensatz 20.

Erzeugt:
  Grafiken/20_excel_vs_datenbank.png  -- links: eine Datei, ein Nutzer, Sperre;
                                         rechts: DBMS als Vermittler zwischen
                                         vielen Nutzern und strukturierten Tabellen.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams.update({
    'font.size': 12,
    'figure.dpi': 150,
    'savefig.dpi': 150,
    'font.family': 'DejaVu Sans',
})

GRAFIKEN_DIR = 'Grafiken'
ROT = "#c0392b"
GRUEN = "#2e7d32"
BLAU = "#2a5d8f"
GRAU = "#555555"


def _person(ax, x, y, s=0.045, color=GRAU):
    ax.add_patch(mpatches.Circle((x, y + s * 1.5), s, facecolor=color, edgecolor='none'))
    ax.add_patch(mpatches.FancyBboxPatch((x - s * 1.1, y - s * 2.2), s * 2.2, s * 2.6,
                 boxstyle="round,pad=0.005,rounding_size=0.02", facecolor=color, edgecolor='none'))


def _table_icon(ax, x, y, w=0.16, h=0.13, ec=BLAU):
    rh = h / 4
    for i in range(4):
        fc = ec if i == 0 else 'white'
        ax.add_patch(mpatches.Rectangle((x, y + i * rh), w, rh, facecolor=fc, edgecolor=ec, lw=1.0))
    for j in range(1, 3):
        ax.plot([x + j * w / 3, x + j * w / 3], [y, y + h], color=ec, lw=0.8)


def generate():
    fig, ax = plt.subplots(figsize=(13, 6.4))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Trennlinie
    ax.plot([0.5, 0.5], [0.05, 0.92], color='#cccccc', lw=1.2, ls=(0, (4, 4)))

    # --- LINKS: Excel-Datei ---
    ax.text(0.25, 0.93, "Tabellenkalkulation (Excel)", ha='center', fontsize=14,
            fontweight='bold', color=ROT)
    # die eine Datei
    ax.add_patch(mpatches.FancyBboxPatch((0.16, 0.45), 0.18, 0.30,
                 boxstyle="round,pad=0.01,rounding_size=0.02", facecolor="#f7e4e1", edgecolor=ROT, lw=1.6))
    ax.text(0.25, 0.60, "daten.xlsx", ha='center', va='center', fontsize=11, fontweight='bold')
    # Schloss-Symbol
    ax.add_patch(mpatches.Circle((0.25, 0.78), 0.018, facecolor='none', edgecolor=ROT, lw=2))
    ax.add_patch(mpatches.Rectangle((0.235, 0.745), 0.03, 0.03, facecolor=ROT, edgecolor='none'))
    # ein Nutzer
    _person(ax, 0.25, 0.30, color=ROT)
    ax.annotate("", xy=(0.25, 0.44), xytext=(0.25, 0.37), arrowprops=dict(arrowstyle="-|>", color=ROT, lw=1.6))
    # andere Nutzer ausgesperrt
    _person(ax, 0.40, 0.30, color="#bbbbbb")
    _person(ax, 0.10, 0.30, color="#bbbbbb")
    ax.text(0.40, 0.20, "wartet", ha='center', fontsize=9, color="#999999")
    ax.text(0.10, 0.20, "wartet", ha='center', fontsize=9, color="#999999")
    ax.text(0.25, 0.10, "✗ ein Nutzer  ✗ keine Regeln  ✗ ein großer Klumpen",
            ha='center', fontsize=10.5, color=ROT)

    # --- RECHTS: Datenbank mit DBMS ---
    ax.text(0.75, 0.93, "Datenbank mit DBMS", ha='center', fontsize=14,
            fontweight='bold', color=GRUEN)
    # DBMS-Box
    ax.add_patch(mpatches.FancyBboxPatch((0.66, 0.50), 0.18, 0.14,
                 boxstyle="round,pad=0.01,rounding_size=0.02", facecolor="#e3f0e4", edgecolor=GRUEN, lw=1.8))
    ax.text(0.75, 0.57, "DBMS", ha='center', va='center', fontsize=12, fontweight='bold', color=GRUEN)
    ax.text(0.75, 0.665, "prüft Regeln · steuert Zugriffe · sichert Konsistenz",
            ha='center', fontsize=8.6, color=GRAU)
    # Tabellen unten
    _table_icon(ax, 0.60, 0.27, ec=GRUEN)
    _table_icon(ax, 0.71, 0.27, ec=GRUEN)
    _table_icon(ax, 0.82, 0.27, ec=GRUEN)
    ax.annotate("", xy=(0.75, 0.41), xytext=(0.75, 0.49), arrowprops=dict(arrowstyle="<|-|>", color=GRUEN, lw=1.6))
    # viele Nutzer oben
    for px in (0.62, 0.75, 0.88):
        _person(ax, px, 0.78, color=GRUEN)
        ax.annotate("", xy=(0.75, 0.645), xytext=(px, 0.745),
                    arrowprops=dict(arrowstyle="-|>", color=GRUEN, lw=1.4))
    ax.text(0.75, 0.10, "✓ viele Nutzer gleichzeitig  ✓ Constraints erzwungen  ✓ skaliert",
            ha='center', fontsize=10.5, color=GRUEN)

    fig.tight_layout()
    out = f"{GRAFIKEN_DIR}/20_excel_vs_datenbank.png"
    fig.savefig(out, bbox_inches='tight')
    plt.close(fig)
    print(f"→ geschrieben: {out}")


if __name__ == "__main__":
    generate()
