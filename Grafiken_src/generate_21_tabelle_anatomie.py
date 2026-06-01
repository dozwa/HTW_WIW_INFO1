"""Generiert die "Anatomie einer Tabelle" fuer Foliensatz 21.

Erzeugt:
  Grafiken/21_tabelle_anatomie.png  -- eine Beispieltabelle (kunde) mit Annotationen:
                                       Spalte/Attribut, Zeile/Datensatz, Primaerschluessel,
                                       NULL-Wert, Datentyp.
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
BLAU = "#2a5d8f"
ORANGE = "#e07b3a"
GELB = "#fdf3d8"
GRAU = "#555555"


def generate():
    fig, ax = plt.subplots(figsize=(13, 7.0))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title("Anatomie einer Tabelle  ·  kunde", fontsize=15, fontweight='bold', color=BLAU)

    cols = ["kunde_id", "vorname", "nachname", "email", "newsletter"]
    types = ["INTEGER", "TEXT", "TEXT", "TEXT", "BOOLEAN"]
    rows = [
        ["1", "Anna", "Müller", "anna@example.de", "1"],
        ["2", "Max", "Schmidt", "max@example.de", "0"],
        ["3", "Lena", "Weber", "NULL", "1"],
    ]
    nx = len(cols)
    x0, y0 = 0.22, 0.60
    cw, rh = 0.118, 0.085

    # Datentyp-Zeile (klein, ueber den Spaltennamen)
    for j, t in enumerate(types):
        ax.text(x0 + j * cw + cw / 2, y0 + rh + 0.028, t, ha='center', va='center',
                fontsize=8.5, color=GRAU, style='italic')
    # Kopfzeile
    for j, c in enumerate(cols):
        ax.add_patch(mpatches.Rectangle((x0 + j * cw, y0), cw, rh, facecolor=BLAU, edgecolor='white', lw=1.2))
        ax.text(x0 + j * cw + cw / 2, y0 + rh / 2, c, ha='center', va='center',
                color='white', fontsize=9.5, fontweight='bold')
    # Datenzeilen
    for i, r in enumerate(rows):
        yy = y0 - (i + 1) * rh
        for j, val in enumerate(r):
            fc = 'white'
            if j == 0:
                fc = GELB  # Primaerschluessel-Spalte hervorheben
            if val == "NULL":
                fc = "#f3e6e6"
            ax.add_patch(mpatches.Rectangle((x0 + j * cw, yy), cw, rh, facecolor=fc, edgecolor=BLAU, lw=0.9))
            ax.text(x0 + j * cw + cw / 2, yy + rh / 2, val, ha='center', va='center', fontsize=9,
                    color=(ORANGE if val == "NULL" else "black"),
                    fontweight=('bold' if val == "NULL" else 'normal'))

    table_left, table_right = x0, x0 + nx * cw
    table_top, table_bot = y0 + rh, y0 - 3 * rh

    # --- Annotationen ---
    # Spalte / Attribut
    ax.annotate("Spalte = Attribut\n(ein fester Datentyp)", xy=(x0 + 1.5 * cw, y0 - 2.5 * rh),
                xytext=(0.50, 0.18), fontsize=11, ha='center', color=BLAU,
                arrowprops=dict(arrowstyle="-|>", color=BLAU, lw=1.6))
    # Zeile / Datensatz
    ax.annotate("Zeile = Datensatz / Tupel\n(genau eine Kundin)", xy=(table_right, y0 - 0.5 * rh),
                xytext=(0.86, 0.50), fontsize=11, ha='center', color=BLAU,
                arrowprops=dict(arrowstyle="-|>", color=BLAU, lw=1.6))
    # Primaerschluessel
    ax.annotate("Primärschlüssel (PK)\neindeutig, nie NULL, unveränderlich",
                xy=(x0 + 0.5 * cw, table_top), xytext=(0.18, 0.90), fontsize=11, ha='center',
                color="#b8860b", fontweight='bold',
                arrowprops=dict(arrowstyle="-|>", color="#b8860b", lw=1.8))
    # NULL
    ax.annotate("NULL ≠ 0 ≠ \"\" — Wert fehlt / unbekannt\n(prüfen mit IS NULL)",
                xy=(x0 + 3.5 * cw, y0 - 2.5 * rh), xytext=(0.74, 0.86), fontsize=11, ha='center',
                color=ORANGE, arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.6))

    # Rahmen um ganze Tabelle
    ax.add_patch(mpatches.Rectangle((table_left, table_bot), nx * cw, 4 * rh,
                 fill=False, edgecolor=BLAU, lw=2.2))

    fig.tight_layout()
    out = f"{GRAFIKEN_DIR}/21_tabelle_anatomie.png"
    fig.savefig(out, bbox_inches='tight')
    plt.close(fig)
    print(f"→ geschrieben: {out}")


if __name__ == "__main__":
    generate()
