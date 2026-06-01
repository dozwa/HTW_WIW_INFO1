"""Generiert das 5-Bausteine-Diagramm einer .py-Datei fuer Foliensatz 15."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams.update({
    'font.size': 12,
    'figure.dpi': 150,
    'savefig.dpi': 150,
    'font.family': 'DejaVu Sans',
})

GRAFIKEN_DIR = 'Grafiken'

# Farbpalette: vom blassen Blau (Vorbereitung) zu kraeftigem Orange (Start)
BAUSTEINE = [
    ("1. Imports",                       "Was brauche ich?",            "#dbe6f0"),
    ("2. Konstanten",                    "Was aendert sich nie?",       "#c8d9e8"),
    ("3. Hilfsfunktionen",               "Was sind die Einzelschritte?", "#b1c7dd"),
    ("4. main()",                        "Was ist der Gesamtablauf?",    "#7fa2c2"),
    ('5. if __name__ == "__main__":',    "Wer startet das Ganze?",       "#e07b3a"),
]


def generate_bausteine():
    n = len(BAUSTEINE)
    fig, ax = plt.subplots(figsize=(10, 5.5))

    block_height = 1.0
    block_width = 7.5
    x0 = 0.0

    for i, (titel, frage, farbe) in enumerate(BAUSTEINE):
        # Reihenfolge: Imports oben, if __name__ unten
        y = (n - 1 - i) * block_height

        # Block-Rechteck
        rect = mpatches.FancyBboxPatch(
            (x0, y + 0.05), block_width, block_height - 0.1,
            boxstyle="round,pad=0.0,rounding_size=0.06",
            linewidth=1.5, edgecolor="#333333", facecolor=farbe,
        )
        ax.add_patch(rect)

        # Linker Titel-Bereich (fett, monospaced fuer Code-Anteile)
        ax.text(
            x0 + 0.25, y + block_height / 2,
            titel,
            ha="left", va="center", fontsize=13, fontweight="bold",
            family="DejaVu Sans Mono" if "__name__" in titel else "DejaVu Sans",
        )

        # Rechter Frage-Bereich (kursiv, dezent)
        ax.text(
            x0 + block_width - 0.25, y + block_height / 2,
            frage,
            ha="right", va="center", fontsize=11, style="italic",
            color="#444444",
        )

    # Pfeil rechts: zeigt Lese-/Ausfuehrungsrichtung von oben nach unten
    arrow_x = x0 + block_width + 0.4
    ax.annotate(
        "",
        xy=(arrow_x, 0.2), xytext=(arrow_x, n * block_height - 0.2),
        arrowprops=dict(arrowstyle="->", color="#555555", lw=2),
    )
    ax.text(
        arrow_x + 0.15, n * block_height / 2,
        "Lese-\nreihenfolge",
        ha="left", va="center", fontsize=10, color="#555555",
    )

    # Zweiter, schmaler Hinweis: was ist Definition, was Start
    bracket_x = x0 - 0.2
    # Vorbereitung: oberste 4 Bloecke
    ax.annotate(
        "", xy=(bracket_x, (n - 4) * block_height + 0.1),
        xytext=(bracket_x, n * block_height - 0.1),
        arrowprops=dict(arrowstyle="-", color="#7fa2c2", lw=3),
    )
    ax.text(
        bracket_x - 0.15, (n * block_height + (n - 4) * block_height) / 2,
        "Definition",
        ha="right", va="center", fontsize=10, color="#7fa2c2",
        fontweight="bold", rotation=90,
    )
    # Start: nur unterster Block
    ax.annotate(
        "", xy=(bracket_x, 0.1),
        xytext=(bracket_x, block_height - 0.1),
        arrowprops=dict(arrowstyle="-", color="#e07b3a", lw=3),
    )
    ax.text(
        bracket_x - 0.15, block_height / 2,
        "Start",
        ha="right", va="center", fontsize=10, color="#e07b3a",
        fontweight="bold", rotation=90,
    )

    ax.set_xlim(x0 - 1.2, x0 + block_width + 2.5)
    ax.set_ylim(-0.2, n * block_height + 0.2)
    ax.set_aspect("equal")
    ax.axis("off")

    fig.tight_layout()
    out = f"{GRAFIKEN_DIR}/15_programme_bausteine.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"  OK {out}")


if __name__ == '__main__':
    generate_bausteine()
