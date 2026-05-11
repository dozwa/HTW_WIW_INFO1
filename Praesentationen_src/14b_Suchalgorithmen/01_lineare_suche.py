"""
14b -- Suchalgorithmen | Demo 1: Lineare Suche im Veggie-Soles-Katalog.

Zeigt:
- die einfachste Suchimplementierung: jeden Index pruefen
- Print-Trace pro Vergleich

Story: Veggie Soles -- finde "Hemp-High" im Produktkatalog.
"""


def lineare_suche(liste, ziel):
    """Lineare Suche mit Print-Trace pro Schritt."""
    for index in range(len(liste)):
        wert = liste[index]
        print(f"    Pruefe Index {index}: {wert!r}", end="")
        if wert == ziel:
            print("   <- Treffer!")
            return index
        else:
            print()
    print(f"    -> Element {ziel!r} nicht gefunden")
    return -1


# 1) Klein und uebersichtlich -- man sieht jeden Schritt.
katalog = ["Eco-Sneaker", "Hemp-High", "Bambus-Boot", "Socken", "Schnuersenkel"]
print(f"Suche 'Hemp-High' in {katalog}:")
pos = lineare_suche(katalog, "Hemp-High")
print(f">>> gefunden an Index {pos}")

print()
print("=" * 60)
print()

# 2) Worst-Case: Element nicht im Katalog.
print("Suche 'Adidas' (nicht im Katalog):")
pos = lineare_suche(katalog, "Adidas")
print(f">>> Ergebnis-Index: {pos}  (-1 = nicht gefunden)")

print()
print("=" * 60)
print()

# 3) Zahlen-Beispiel.
ids = [101, 207, 314, 422, 555]
print(f"Suche Bestell-ID 422 in {ids}:")
pos = lineare_suche(ids, 422)
print(f">>> gefunden an Index {pos}")
