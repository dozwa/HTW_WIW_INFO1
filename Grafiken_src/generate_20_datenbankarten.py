"""Generiert die Datenbankarten-Uebersicht fuer Foliensatz 20.

Erzeugt:
  Grafiken/20_datenbankarten_uebersicht.png  -- 2x2-Raster mit Mini-Schema-Skizzen
                                                der vier wichtigsten DB-Typen:
                                                relational, Key-Value, Dokument, Graph.
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

BLAU_RAHMEN = "#2a5d8f"
BLAU_FUELL = "#dbe6f2"
ORANGE = "#e07b3a"
GRAU = "#555555"


def _box(ax, x, y, w, h, fc=BLAU_FUELL, ec=BLAU_RAHMEN, lw=1.4, **kw):
    ax.add_patch(mpatches.FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.04",
        linewidth=lw, edgecolor=ec, facecolor=fc, **kw))


def _panel_relational(ax):
    ax.set_title("Relational  ·  Tabellen", fontweight='bold', color=BLAU_RAHMEN)
    # kleine Tabelle: 1 Kopfzeile + 3 Datenzeilen, 3 Spalten
    cols = ["id", "name", "preis"]
    rows = [["1", "Eco-Sneaker", "89.95"],
            ["2", "Hemp-High", "109.00"],
            ["3", "Bambus-Boot", "135.50"]]
    x0, y0, cw, rh = 0.06, 0.62, 0.30, 0.13
    for j, c in enumerate(cols):
        _box(ax, x0 + j * cw, y0, cw, rh, fc=BLAU_RAHMEN, ec=BLAU_RAHMEN)
        ax.text(x0 + j * cw + cw / 2, y0 + rh / 2, c, ha='center', va='center',
                color='white', fontsize=10.5, fontweight='bold')
    for i, r in enumerate(rows):
        yy = y0 - (i + 1) * rh
        for j, val in enumerate(r):
            _box(ax, x0 + j * cw, yy, cw, rh, fc='white', ec=BLAU_RAHMEN)
            ax.text(x0 + j * cw + cw / 2, yy + rh / 2, val, ha='center', va='center',
                    fontsize=9.5)
    ax.text(0.5, 0.16, "feste Spalten, SQL, ACID", ha='center', fontsize=10.5, color=GRAU)
    ax.text(0.5, 0.06, "z. B. PostgreSQL, MySQL, SQLite", ha='center', fontsize=10,
            style='italic', color=ORANGE)


def _panel_keyvalue(ax):
    ax.set_title("Key-Value  ·  Schluessel → Wert", fontweight='bold', color=BLAU_RAHMEN)
    paare = [("session:42", "{user: anna}"),
             ("cart:7", "[eco, hemp]"),
             ("views:eco", "1287")]
    y0 = 0.74
    for i, (k, v) in enumerate(paare):
        yy = y0 - i * 0.18
        _box(ax, 0.06, yy, 0.34, 0.13, fc=BLAU_FUELL)
        ax.text(0.23, yy + 0.065, k, ha='center', va='center', fontsize=10, fontweight='bold')
        ax.annotate("", xy=(0.56, yy + 0.065), xytext=(0.40, yy + 0.065),
                    arrowprops=dict(arrowstyle="-|>", color=BLAU_RAHMEN, lw=1.6))
        _box(ax, 0.56, yy, 0.36, 0.13, fc='white')
        ax.text(0.74, yy + 0.065, v, ha='center', va='center', fontsize=9.5)
    ax.text(0.5, 0.16, "extrem schnell bei einfachen Lookups", ha='center', fontsize=10.5, color=GRAU)
    ax.text(0.5, 0.06, "z. B. Redis, DynamoDB", ha='center', fontsize=10,
            style='italic', color=ORANGE)


def _panel_dokument(ax):
    ax.set_title("Dokument  ·  flexible JSON-Dokumente", fontweight='bold', color=BLAU_RAHMEN)
    _box(ax, 0.10, 0.30, 0.46, 0.50, fc='white')
    txt = ('{\n  "id": 1,\n  "name": "Eco-Sneaker",\n  "tags": ["vegan",\n           "recycled"],\n'
           '  "lager": {"berlin": 12}\n}')
    ax.text(0.13, 0.55, txt, ha='left', va='center', fontsize=9, family='monospace')
    _box(ax, 0.60, 0.40, 0.32, 0.32, fc=BLAU_FUELL)
    ax.text(0.76, 0.62, '{\n "id": 2,\n "name":\n  "Hemp-High"\n}', ha='left', va='center',
            fontsize=8.5, family='monospace')
    ax.text(0.5, 0.16, "jedes Dokument darf andere Felder haben", ha='center', fontsize=10.5, color=GRAU)
    ax.text(0.5, 0.06, "z. B. MongoDB, CouchDB", ha='center', fontsize=10,
            style='italic', color=ORANGE)


def _panel_graph(ax):
    ax.set_title("Graph  ·  Knoten & Kanten", fontweight='bold', color=BLAU_RAHMEN)
    knoten = {"Anna": (0.20, 0.70), "Max": (0.72, 0.74), "Lena": (0.52, 0.42),
              "Eco-Sneaker": (0.78, 0.40)}
    kanten = [("Anna", "Max", "ist befreundet mit"), ("Max", "Lena", "folgt"),
              ("Anna", "Lena", "folgt"), ("Lena", "Eco-Sneaker", "hat gekauft")]
    for a, b, label in kanten:
        (xa, ya), (xb, yb) = knoten[a], knoten[b]
        ax.plot([xa, xb], [ya, yb], color=GRAU, lw=1.3, zorder=1)
    for name, (x, y) in knoten.items():
        c = ORANGE if "-" in name else BLAU_RAHMEN
        ax.add_patch(mpatches.Circle((x, y), 0.075, facecolor=c, edgecolor='white', lw=1.5, zorder=3))
        ax.text(x, y - 0.135, name, ha='center', va='center', fontsize=8.8, zorder=4)
    ax.text(0.5, 0.16, "effizient bei Beziehungsanalysen", ha='center', fontsize=10.5, color=GRAU)
    ax.text(0.5, 0.06, "z. B. Neo4j, Amazon Neptune", ha='center', fontsize=10,
            style='italic', color=ORANGE)


def generate():
    fig, axes = plt.subplots(2, 2, figsize=(13, 8.6))
    for ax in axes.flat:
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
    _panel_relational(axes[0, 0])
    _panel_keyvalue(axes[0, 1])
    _panel_dokument(axes[1, 0])
    _panel_graph(axes[1, 1])
    fig.suptitle("Die vier wichtigsten Datenbankarten — ein Typ pro Anwendungsfall",
                 fontsize=15, fontweight='bold')
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    out = f"{GRAFIKEN_DIR}/20_datenbankarten_uebersicht.png"
    fig.savefig(out, bbox_inches='tight')
    plt.close(fig)
    print(f"→ geschrieben: {out}")


if __name__ == "__main__":
    generate()
