"""Generiert das SQLite-Workflow-Diagramm fuer Foliensatz 22.

Erzeugt:
  Grafiken/22_sqlite_workflow.png  -- Ablauf: connect → cursor → execute(SQL)
                                      → commit / fetch* → close, mit dem Hinweis,
                                      wo Python aufhoert und SQL anfaengt.
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


def _step(ax, cx, cy, w, h, code, beschr, fc):
    ax.add_patch(mpatches.FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                 boxstyle="round,pad=0.006,rounding_size=0.02",
                 facecolor=fc, edgecolor=BLAU, lw=1.6, zorder=3))
    ax.text(cx, cy + 0.022, code, ha='center', va='center', fontsize=10,
            family='monospace', fontweight='bold', zorder=4)
    ax.text(cx, cy - 0.032, beschr, ha='center', va='center', fontsize=8.4, color=GRAU, zorder=4)


def _arrow(ax, x1, y, x2):
    ax.annotate("", xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle="-|>", color=BLAU, lw=1.8))


def generate():
    fig, ax = plt.subplots(figsize=(15, 6.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title("SQLite mit Python — der immer gleiche Ablauf", fontsize=15,
                 fontweight='bold', color=BLAU)

    h, y = 0.18, 0.62
    steps = [
        (0.105, 0.17, "connect('shop.db')", "DB öffnen / anlegen", BLAUFUELL),
        (0.305, 0.15, ".cursor()", "Werkzeug holen", BLAUFUELL),
        (0.505, 0.18, ".execute(sql, daten)", "SQL ausführen", ORANGEFUELL),
        (0.725, 0.22, ".commit() / .fetchall()", "sichern / lesen", BLAUFUELL),
        (0.915, 0.13, ".close()", "schließen", BLAUFUELL),
    ]
    for cx, w, code, beschr, fc in steps:
        _step(ax, cx, y, w, h, code, beschr, fc)
    for i in range(len(steps) - 1):
        x1 = steps[i][0] + steps[i][1] / 2
        x2 = steps[i + 1][0] - steps[i + 1][1] / 2
        _arrow(ax, x1, y, x2)

    # Hinweis: der SQL-Befehl ist ein String
    ax.add_patch(mpatches.FancyBboxPatch((0.40, 0.40), 0.21, 0.07,
                 boxstyle="round,pad=0.004,rounding_size=0.01", facecolor=ORANGEFUELL,
                 edgecolor=ORANGE, lw=1.4))
    ax.text(0.505, 0.435, "der SQL-Befehl ist ein String", ha='center', fontsize=9.2, color=ORANGE)
    ax.annotate("", xy=(0.505, y - h / 2), xytext=(0.505, 0.47),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.4))

    # Sicherheits- und Best-Practice-Hinweise
    ax.text(0.5, 0.25, "Benutzereingaben NIE in den String kleben — immer Platzhalter:  "
                       "execute(\"... VALUES (?, ?)\", (name, preis))",
            ha='center', fontsize=10, color="#c0392b")
    ax.text(0.5, 0.16, "Noch besser:  with sqlite3.connect('shop.db') as conn:  →  schließt automatisch, "
                       "auch bei Fehlern",
            ha='center', fontsize=10, color=GRAU)
    ax.text(0.5, 0.07, "blau = reines Python   ·   orange = hier steckt SQL drin", ha='center',
            fontsize=9.5, color=GRAU, style='italic')

    fig.tight_layout()
    out = f"{GRAFIKEN_DIR}/22_sqlite_workflow.png"
    fig.savefig(out, bbox_inches='tight')
    plt.close(fig)
    print(f"→ geschrieben: {out}")


if __name__ == "__main__":
    generate()
