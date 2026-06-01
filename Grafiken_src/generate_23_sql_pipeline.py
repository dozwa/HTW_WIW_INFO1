"""Generiert das SELECT-Pipeline-Diagramm fuer Foliensatz 23.

Erzeugt:
  Grafiken/23_sql_pipeline.png  -- in welcher Reihenfolge eine SELECT-Abfrage
                                   abgearbeitet wird: FROM/JOIN → WHERE → GROUP BY
                                   → HAVING → SELECT → ORDER BY → LIMIT.
                                   Hinweis: geschrieben wird sie in anderer Reihenfolge.
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
BLAUFUELL = "#dbe6f2"
ORANGE = "#e07b3a"
ORANGEFUELL = "#fdecdd"
GRAU = "#444444"

STAGES = [
    ("FROM / JOIN", "Tabellen holen\n& verknüpfen", BLAUFUELL),
    ("WHERE", "einzelne Zeilen\nfiltern", BLAUFUELL),
    ("GROUP BY", "Zeilen zu Gruppen\nzusammenfassen", ORANGEFUELL),
    ("HAVING", "Gruppen\nfiltern", ORANGEFUELL),
    ("SELECT", "Spalten / Aggregate\nberechnen", BLAUFUELL),
    ("ORDER BY", "Ergebnis\nsortieren", BLAUFUELL),
    ("LIMIT", "abschneiden", BLAUFUELL),
]


def generate():
    fig, ax = plt.subplots(figsize=(16, 6.6))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title("Wie SQL eine Abfrage abarbeitet — und warum die Reihenfolge zählt",
                 fontsize=15, fontweight='bold', color=BLAU)

    n = len(STAGES)
    bw = 0.122
    gap = (1.0 - n * bw) / (n + 1)
    y, bh = 0.56, 0.20
    centers = []
    for i, (name, desc, fc) in enumerate(STAGES):
        x = gap + i * (bw + gap)
        cx = x + bw / 2
        centers.append(cx)
        ax.add_patch(mpatches.FancyBboxPatch((x, y), bw, bh,
                     boxstyle="round,pad=0.006,rounding_size=0.02",
                     facecolor=fc, edgecolor=BLAU, lw=1.6))
        ax.text(cx, y + bh - 0.045, name, ha='center', va='center', fontsize=10.5,
                family='monospace', fontweight='bold')
        ax.text(cx, y + 0.055, desc, ha='center', va='center', fontsize=8.2, color=GRAU)
        if i > 0:
            ax.annotate("", xy=(x, y + bh / 2), xytext=(centers[i - 1] + bw / 2, y + bh / 2),
                        arrowprops=dict(arrowstyle="-|>", color=BLAU, lw=1.6))

    # "ausgefuehrt in dieser Reihenfolge"
    ax.text(0.5, 0.83, "▶ so wird sie ausgeführt", ha='center', fontsize=11, color=BLAU, fontweight='bold')
    # "geschrieben in anderer Reihenfolge"
    ax.text(0.5, 0.40, "✎ so wird sie geschrieben:", ha='center', fontsize=11, color=ORANGE, fontweight='bold')
    code = ("SELECT   kunde.name, SUM(bestellung.betrag) AS umsatz\n"
            "FROM     kunde  JOIN  bestellung  ON kunde.kunde_id = bestellung.kunde_id\n"
            "WHERE    bestellung.betrag > 50\n"
            "GROUP BY kunde.kunde_id\n"
            "HAVING   umsatz > 200\n"
            "ORDER BY umsatz DESC\n"
            "LIMIT    10;")
    ax.text(0.5, 0.20, code, ha='center', va='center', fontsize=10, family='monospace',
            color=GRAU, bbox=dict(boxstyle="round,pad=0.5", facecolor="#f6f6f6", edgecolor="#cccccc"))
    ax.text(0.5, 0.015, "blau = arbeitet auf Zeilen   ·   orange = arbeitet auf Gruppen",
            ha='center', fontsize=9.5, color=GRAU, style='italic')

    fig.tight_layout()
    out = f"{GRAFIKEN_DIR}/23_sql_pipeline.png"
    fig.savefig(out, bbox_inches='tight')
    plt.close(fig)
    print(f"→ geschrieben: {out}")


if __name__ == "__main__":
    generate()
