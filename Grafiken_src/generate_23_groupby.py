"""Generiert die GROUP-BY-/Aggregations-Visualisierung fuer Foliensatz 23.

Erzeugt:
  Grafiken/23_groupby_aggregation.png  -- links: Einzelzeilen (bestellung), nach kunde
                                          eingefaerbt → Mitte: Gruppen → rechts:
                                          ein aggregierter Wert pro Gruppe (COUNT, SUM).
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
GRAU = "#444444"
GRP = {"Anna": "#cfe3f5", "Max": "#fde2c8", "Lena": "#d9ecd2"}
GRP_EDGE = {"Anna": "#2a5d8f", "Max": "#d2691e", "Lena": "#3a7d2f"}


def _row(ax, x, y, w, h, cells, fc, ec):
    ax.add_patch(mpatches.Rectangle((x, y), w, h, facecolor=fc, edgecolor=ec, lw=1.1))
    n = len(cells)
    for j, c in enumerate(cells):
        ax.text(x + (j + 0.5) * w / n, y + h / 2, c, ha='center', va='center', fontsize=8.6)


def generate():
    fig, ax = plt.subplots(figsize=(15, 7.4))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title("GROUP BY — viele Zeilen werden zu einem Wert pro Gruppe", fontsize=15,
                 fontweight='bold', color=BLAU)

    # --- Links: Rohdaten bestellung ---
    daten = [  # (kunde, bestell_id, betrag)
        ("Anna", "10", "89.95"), ("Max", "12", "135.50"), ("Anna", "11", "109.00"),
        ("Lena", "13", "75.00"), ("Anna", "14", "60.00"), ("Max", "15", "89.95"),
    ]
    x0, w, h = 0.04, 0.22, 0.082
    ax.text(x0 + w / 2, 0.90, "bestellung  (Rohdaten)", ha='center', fontsize=10.5, fontweight='bold', color=BLAU)
    ax.text(x0 + w / 2, 0.855, "kunde · bestell_id · betrag", ha='center', fontsize=8.2, color=GRAU)
    for i, (k, bid, bet) in enumerate(daten):
        yy = 0.82 - (i + 1) * h
        _row(ax, x0, yy, w, h, [k, bid, bet], GRP[k], GRP_EDGE[k])

    # --- Mitte: Gruppen ---
    ax.annotate("", xy=(0.36, 0.42), xytext=(0.27, 0.42), arrowprops=dict(arrowstyle="-|>", color=GRAU, lw=2))
    ax.text(0.315, 0.46, "GROUP BY\nkunde", ha='center', fontsize=9.5, color=GRAU)
    gx = 0.38
    groups = {"Anna": [d for d in daten if d[0] == "Anna"],
              "Max": [d for d in daten if d[0] == "Max"],
              "Lena": [d for d in daten if d[0] == "Lena"]}
    gy = 0.80
    for k, rows in groups.items():
        gh = len(rows) * 0.05 + 0.05
        ax.add_patch(mpatches.FancyBboxPatch((gx, gy - gh), 0.20, gh,
                     boxstyle="round,pad=0.004,rounding_size=0.012",
                     facecolor=GRP[k], edgecolor=GRP_EDGE[k], lw=1.6))
        ax.text(gx + 0.10, gy - 0.025, f"Gruppe: {k}", ha='center', fontsize=8.8, fontweight='bold',
                color=GRP_EDGE[k])
        for i, (_, bid, bet) in enumerate(rows):
            ax.text(gx + 0.10, gy - 0.06 - i * 0.05, f"{bid} · {bet}", ha='center', va='center', fontsize=8.2)
        gy = gy - gh - 0.04

    # --- Rechts: aggregiertes Ergebnis ---
    ax.annotate("", xy=(0.66, 0.42), xytext=(0.59, 0.42), arrowprops=dict(arrowstyle="-|>", color=GRAU, lw=2))
    ax.text(0.625, 0.49, "COUNT(*)\nSUM(betrag)", ha='center', fontsize=9.0, color=GRAU)
    rx, rw, rh = 0.68, 0.27, 0.082
    ax.text(rx + rw / 2, 0.70, "Ergebnis: eine Zeile pro Kund:in", ha='center', fontsize=10.5,
            fontweight='bold', color=BLAU)
    head = ["kunde", "anzahl", "summe"]
    for j, c in enumerate(head):
        ax.add_patch(mpatches.Rectangle((rx + j * rw / 3, 0.61), rw / 3, rh, facecolor=BLAU,
                     edgecolor='white', lw=1))
        ax.text(rx + (j + 0.5) * rw / 3, 0.61 + rh / 2, c, ha='center', va='center', color='white',
                fontsize=8.8, fontweight='bold')
    erg = [("Anna", "3", "218.95"), ("Max", "2", "225.45"), ("Lena", "1", "75.00")]
    for i, (k, n, s) in enumerate(erg):
        yy = 0.61 - (i + 1) * rh
        _row(ax, rx, yy, rw, rh, [k, n, s], GRP[k], GRP_EDGE[k])

    ax.text(0.5, 0.06, "Faustregel: jede Spalte hinter SELECT steht entweder im GROUP BY — "
                       "oder steckt in einer Aggregatfunktion (COUNT/SUM/AVG/MIN/MAX).",
            ha='center', fontsize=9.8, color=GRAU)
    ax.text(0.5, 0.015, "WHERE filtert Zeilen VOR der Gruppierung · HAVING filtert Gruppen DANACH",
            ha='center', fontsize=9.8, color="#c0392b")

    fig.tight_layout()
    out = f"{GRAFIKEN_DIR}/23_groupby_aggregation.png"
    fig.savefig(out, bbox_inches='tight')
    plt.close(fig)
    print(f"→ geschrieben: {out}")


if __name__ == "__main__":
    generate()
