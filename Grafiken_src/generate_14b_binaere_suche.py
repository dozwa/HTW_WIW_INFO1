"""Generiert die Binaere-Suche-Intervall-Visualisierung fuer Foliensatz 14b."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams.update({
    'font.size': 12,
    'axes.titlesize': 13,
    'axes.labelsize': 11,
    'figure.dpi': 150,
    'savefig.dpi': 150,
})

GRAFIKEN_DIR = 'Grafiken'

OUT_OF_RANGE_COLOR = "#dddddd"
ACTIVE_COLOR = "#5c87b8"
MID_COLOR = "#e07b3a"
HIT_COLOR = "#7fa97f"


def binaere_suche_schritte(daten, ziel):
    """Liefert (lo, mid, hi, hit) pro Schritt."""
    lo, hi = 0, len(daten) - 1
    schritte = []
    while lo <= hi:
        mid = (lo + hi) // 2
        hit = daten[mid] == ziel
        schritte.append((lo, mid, hi, hit))
        if hit:
            break
        elif daten[mid] < ziel:
            lo = mid + 1
        else:
            hi = mid - 1
    return schritte


def generate_binaere_suche():
    daten = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
    ziel = 23
    schritte = binaere_suche_schritte(daten, ziel)
    n = len(daten)
    n_panel = len(schritte)

    fig, axes = plt.subplots(n_panel, 1, figsize=(11, 1.0 + 1.0 * n_panel))
    if n_panel == 1:
        axes = [axes]

    for panel_idx, (lo, mid, hi, hit) in enumerate(schritte):
        ax = axes[panel_idx]
        farben = []
        for i in range(n):
            if i < lo or i > hi:
                farben.append(OUT_OF_RANGE_COLOR)
            elif i == mid:
                farben.append(HIT_COLOR if hit else MID_COLOR)
            else:
                farben.append(ACTIVE_COLOR)

        ax.bar(range(n), [1] * n, color=farben, edgecolor="white", linewidth=1.2)
        for i, wert in enumerate(daten):
            farbe = "white" if i == mid else "black"
            ax.text(i, 0.5, str(wert), ha="center", va="center", fontsize=10, color=farbe)

        # Marker-Beschriftung darunter.
        for i, label in [(lo, "lo"), (mid, "mid"), (hi, "hi")]:
            ax.text(i, -0.25, label, ha="center", va="top", fontsize=9,
                    color=MID_COLOR if label == "mid" else "black",
                    fontweight="bold" if label == "mid" else "normal")

        if hit:
            titel = f"Schritt {panel_idx + 1}: liste[{mid}] = {daten[mid]} -- TREFFER"
        elif daten[mid] < ziel:
            titel = f"Schritt {panel_idx + 1}: liste[{mid}] = {daten[mid]} < {ziel} -> rechts"
        else:
            titel = f"Schritt {panel_idx + 1}: liste[{mid}] = {daten[mid]} > {ziel} -> links"
        ax.set_title(titel, fontsize=11, loc="left")

        ax.set_xlim(-0.6, n - 0.4)
        ax.set_ylim(-0.6, 1.2)
        ax.axis("off")

    legend_patches = [
        mpatches.Patch(color=ACTIVE_COLOR, label="Suchintervall"),
        mpatches.Patch(color=MID_COLOR, label="aktuelles mid"),
        mpatches.Patch(color=HIT_COLOR, label="Treffer"),
        mpatches.Patch(color=OUT_OF_RANGE_COLOR, label="ausgeschlossen"),
    ]
    fig.legend(handles=legend_patches, loc="lower center", ncol=4, frameon=False,
               bbox_to_anchor=(0.5, -0.02))

    fig.suptitle(f"Binaere Suche nach {ziel} -- Intervall halbieren",
                 fontsize=12, y=1.0)
    fig.tight_layout()
    out = f"{GRAFIKEN_DIR}/14b_binaere_suche_schritte.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"  ✓ {out}")


if __name__ == '__main__':
    generate_binaere_suche()
