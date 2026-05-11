"""Generiert den Bubble-Sort-Schrittstreifen fuer Foliensatz 14a."""
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 12,
    'axes.titlesize': 13,
    'axes.labelsize': 11,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.dpi': 150,
    'savefig.dpi': 150,
})

GRAFIKEN_DIR = 'Grafiken'

DEFAULT_COLOR = "#5c87b8"
SWAP_COLOR = "#e07b3a"
SORTED_COLOR = "#7fa97f"


def bubble_sort_passes(daten):
    """Liefert Snapshots der Liste nach jedem Pass + Index der getauschten Paare."""
    daten = daten.copy()
    n = len(daten)
    snapshots = [(daten.copy(), None, n)]   # (state, swapped_pair, sortierter_suffix_start)
    sortiert_ab = n
    for i in range(n):
        getauscht_pair = None
        getauscht_in_pass = False
        for j in range(n - i - 1):
            if daten[j] > daten[j + 1]:
                daten[j], daten[j + 1] = daten[j + 1], daten[j]
                getauscht_pair = (j, j + 1)
                getauscht_in_pass = True
        sortiert_ab = n - i - 1
        snapshots.append((daten.copy(), getauscht_pair, sortiert_ab))
        if not getauscht_in_pass:
            break
    return snapshots


def generate_bubble_sort_schritte():
    daten = [5, 3, 8, 4, 2, 7]
    snapshots = bubble_sort_passes(daten)

    n_panel = min(5, len(snapshots))
    fig, axes = plt.subplots(1, n_panel, figsize=(13, 3.6), sharey=True)
    if n_panel == 1:
        axes = [axes]

    n = len(daten)
    xs = list(range(n))

    for panel_idx, (state, swap, sortiert_ab) in enumerate(snapshots[:n_panel]):
        ax = axes[panel_idx]
        farben = []
        for i in range(n):
            if i >= sortiert_ab:
                farben.append(SORTED_COLOR)
            elif swap and i in swap:
                farben.append(SWAP_COLOR)
            else:
                farben.append(DEFAULT_COLOR)

        ax.bar(xs, state, color=farben, edgecolor="white", linewidth=1.2)
        for i, wert in enumerate(state):
            ax.text(i, wert + 0.2, str(wert), ha="center", va="bottom", fontsize=10)

        if panel_idx == 0:
            titel = "Start"
        else:
            titel = f"nach Pass {panel_idx}"
        ax.set_title(titel, fontsize=11)

        ax.set_xticks(xs)
        ax.set_ylim(0, max(daten) + 2)
        ax.set_yticks([])
        for spine in ("top", "right", "left"):
            ax.spines[spine].set_visible(False)

    fig.suptitle("Bubble Sort -- Schrittstreifen (orange = getauscht, gruen = endgueltig)",
                 fontsize=12, y=1.02)
    fig.tight_layout()
    out = f"{GRAFIKEN_DIR}/14a_bubble_sort_schritte.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"  ✓ {out}")


if __name__ == '__main__':
    generate_bubble_sort_schritte()
