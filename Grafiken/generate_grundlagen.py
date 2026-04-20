import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Beamer-optimierte Einstellungen
plt.rcParams.update({
    'font.size': 12,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.figsize': (10, 5),
    'figure.dpi': 150,
    'savefig.dpi': 150,
})

GRAFIKEN_DIR = 'Grafiken'


def generate_programmierprozess():
    """Programmierprozess in 6 Schritten als Flussdiagramm."""
    fig, ax = plt.subplots(figsize=(14, 4.5))

    schritte = [
        ("1. Verstehen", "Aufgabe lesen,\nEVA identifizieren"),
        ("2. Beispiel", "Konkreten Fall\nvon Hand lösen"),
        ("3. Aufschreiben", "Schritte als\nPseudocode"),
        ("4. Verallgemeinern", "Variablen einsetzen,\nauf Papier testen"),
        ("5. Coden", "Pseudocode in\nPython übersetzen"),
        ("6. Testen", "Testfälle prüfen,\ndebuggen"),
    ]

    # Farben: Haberfellner-Phasen zugeordnet
    farben = [
        "#4CAF50",  # Anstoß (grün)
        "#2196F3",  # Zielsuche (blau)
        "#2196F3",  # Zielsuche (blau)
        "#FF9800",  # Lösungssuche (orange)
        "#FF9800",  # Lösungssuche (orange)
        "#9C27B0",  # Auswahl/Ergebnis (lila)
    ]

    box_w = 1.7
    box_h = 1.8
    gap = 0.45
    y_center = 2.0

    for i, (titel, beschreibung) in enumerate(schritte):
        x = i * (box_w + gap)

        # Box
        rect = mpatches.FancyBboxPatch(
            (x, y_center - box_h / 2), box_w, box_h,
            boxstyle="round,pad=0.1",
            facecolor=farben[i], edgecolor="white", linewidth=2, alpha=0.9
        )
        ax.add_patch(rect)

        # Titel
        ax.text(x + box_w / 2, y_center + 0.35, titel,
                ha='center', va='center', fontsize=11, fontweight='bold',
                color='white')

        # Beschreibung
        ax.text(x + box_w / 2, y_center - 0.3, beschreibung,
                ha='center', va='center', fontsize=9, color='white')

        # Pfeil
        if i < len(schritte) - 1:
            ax.annotate('', xy=(x + box_w + gap * 0.15, y_center),
                        xytext=(x + box_w + 0.02, y_center),
                        arrowprops=dict(arrowstyle='->', color='#555555',
                                        lw=2.5))

    # Legende: Haberfellner-Phasen
    legend_patches = [
        mpatches.Patch(color="#4CAF50", label="Anstoß"),
        mpatches.Patch(color="#2196F3", label="Zielsuche"),
        mpatches.Patch(color="#FF9800", label="Lösungssuche"),
        mpatches.Patch(color="#9C27B0", label="Auswahl / Ergebnis"),
    ]
    ax.legend(handles=legend_patches, loc='upper center',
              ncol=4, fontsize=9, frameon=False,
              bbox_to_anchor=(0.5, 0.08))

    total_w = len(schritte) * (box_w + gap) - gap
    ax.set_xlim(-0.3, total_w + 0.3)
    ax.set_ylim(0.2, 3.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Programmierprozess: Von Haberfellner zum Code', fontsize=14,
                 fontweight='bold', pad=15)

    fig.savefig(f'{GRAFIKEN_DIR}/01_problemloesung_programmierprozess.png')
    plt.close(fig)
    print(f'  ✓ {GRAFIKEN_DIR}/01_problemloesung_programmierprozess.png')


if __name__ == '__main__':
    generate_programmierprozess()
