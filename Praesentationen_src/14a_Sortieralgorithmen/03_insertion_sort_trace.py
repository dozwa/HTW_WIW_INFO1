"""
14a -- Sortieralgorithmen | Demo 3: Insertion Sort mit "sortiertem Praefix".

Zeigt:
- Insertion Sort als "Karten-in-der-Hand"-Algorithmus
- nach jedem Einfuegen wird der bereits sortierte Bereich in <>-Klammern
  hervorgehoben
- man sieht, wie der sortierte Bereich von links nach rechts waechst

Story: Veggie Soles -- Liste der heute eingegangenen Bestellsummen
sortieren, sobald sie eintreffen.
"""


def array_mit_praefix(arr, praefix_laenge):
    """
    Druckt die Liste so, dass die ersten `praefix_laenge` Elemente
    in <>-Klammern stehen (sortierter Bereich).
    """
    teile = []
    for i, wert in enumerate(arr):
        teile.append(str(wert))
    sortierter_teil = ", ".join(teile[:praefix_laenge])
    rest = ", ".join(teile[praefix_laenge:])
    if rest:
        return f"  <{sortierter_teil}>  {rest}"
    return f"  <{sortierter_teil}>"


def insertion_sort_trace(liste):
    """Insertion Sort mit Trace pro Einfuegevorgang."""
    print(f">>> Start: {liste}")
    print(array_mit_praefix(liste, 1))
    print()

    for i in range(1, len(liste)):
        schluessel = liste[i]
        print(f"--- Schritt {i}: nimm Element {schluessel} ---")

        # Schluessel an seiner alten Stelle entfernen, dann links suchen.
        j = i - 1
        while j >= 0 and liste[j] > schluessel:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = schluessel

        print(array_mit_praefix(liste, i + 1))
        print()

    print(f">>> Ende:  {liste}")
    return liste


# 1) Beispiel aus dem Notebook: [5, 3, 8, 4, 2]
zahlen = [5, 3, 8, 4, 2]
print(f"Insertion Sort der Liste {zahlen}:")
insertion_sort_trace(zahlen.copy())

print()
print("=" * 60)
print()

# 2) Veggie-Soles-Bestellsummen.
bestellungen = [109.00, 89.95, 135.50, 19.95, 89.95]
print(f"Insertion Sort der Bestellsummen {bestellungen}:")
insertion_sort_trace(bestellungen.copy())
