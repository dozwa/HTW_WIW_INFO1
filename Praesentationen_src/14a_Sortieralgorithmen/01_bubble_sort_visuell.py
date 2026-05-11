"""
14a -- Sortieralgorithmen | Demo 1: Bubble Sort mit State-Snapshot.

Zeigt:
- Bubble-Sort-Implementierung
- Visualisierung pro Schritt: Liste komplett, getauschtes Paar in [ ]
- nach jedem Pass eine Trennlinie

Story: Veggie-Soles-Bestseller-Preise [109.00, 89.95, 135.50] sortieren.
"""


def array_mit_markern(arr, marker_idx):
    """
    Druckt die Liste so, dass die Indices in `marker_idx` mit [ ] markiert
    sind. Beispiel: [89.95, [109.00], [135.50]]
    """
    teile = []
    for i, wert in enumerate(arr):
        if i in marker_idx:
            teile.append(f"[{wert}]")
        else:
            teile.append(f" {wert} ")
    return "  " + ", ".join(teile)


def bubble_sort_visuell(liste):
    """Bubble Sort mit Trace pro Vergleich."""
    n = len(liste)
    print(f">>> Start: {liste}")
    print()
    for i in range(n):
        getauscht_in_pass = False
        print(f"--- Pass {i + 1} ---")
        for j in range(n - i - 1):
            if liste[j] > liste[j + 1]:
                # Tauschen + Snapshot
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
                getauscht_in_pass = True
                print(array_mit_markern(liste, {j, j + 1}) + "  <- getauscht")
            else:
                print(array_mit_markern(liste, {j, j + 1}) + "  ok")
        if not getauscht_in_pass:
            print("    (kein Tausch mehr -- Liste ist sortiert)")
            break
        print()
    print()
    print(f">>> Ende:  {liste}")
    return liste


# 1) Veggie-Soles-Preise sortieren.
preise = [109.00, 89.95, 135.50]
print("Bubble Sort der Veggie-Soles-Preise (Hemp-High, Eco-Sneaker, Bambus-Boot):")
bubble_sort_visuell(preise.copy())

print()
print("=" * 60)
print()

# 2) Etwas groesseres Beispiel zur Demonstration mehrerer Passes.
zahlen = [5, 3, 8, 4, 2]
print(f"Bubble Sort der Liste {zahlen}:")
bubble_sort_visuell(zahlen.copy())
