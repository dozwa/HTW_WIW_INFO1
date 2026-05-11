"""
14a -- Sortieralgorithmen | Demo 4: Quicksort mit Rekursionsbaum.

Zeigt:
- Quicksort-Implementierung (List Comprehension, simple Variante)
- jeden rekursiven Aufruf indentiert ausgegeben
- Pivot-Wahl, kleiner-Teilliste, groesser-Teilliste, Ergebnis pro Aufruf

Story: Veggie Soles -- 8 zufaellig gewuerfelte Bestellgroessen sortieren.
"""


def quicksort_debug(liste, tiefe=0):
    """Quicksort mit Trace pro rekursivem Aufruf."""
    einzug = "  " * tiefe

    # 1) Aufruf zeigen.
    print(f"{einzug}quicksort({liste})")

    # 2) Basisfall: leer oder einelementig -> bereits sortiert.
    if len(liste) <= 1:
        print(f"{einzug}  -> Basisfall, gebe {liste} zurueck")
        return liste

    # 3) Pivot waehlen, in zwei Listen partitionieren.
    pivot = liste[0]
    kleiner = [x for x in liste[1:] if x < pivot]
    groesser = [x for x in liste[1:] if x >= pivot]
    print(f"{einzug}  pivot = {pivot}")
    print(f"{einzug}  kleiner  = {kleiner}")
    print(f"{einzug}  groesser = {groesser}")

    # 4) Rekursiv sortieren und kombinieren.
    sort_kleiner = quicksort_debug(kleiner, tiefe + 1)
    sort_groesser = quicksort_debug(groesser, tiefe + 1)
    ergebnis = sort_kleiner + [pivot] + sort_groesser
    print(f"{einzug}  -> kombiniert: {ergebnis}")
    return ergebnis


# 1) Klassisches Beispiel.
print("Quicksort der Liste [5, 3, 8, 4, 2, 7, 1, 6]:")
print("-" * 60)
ergebnis = quicksort_debug([5, 3, 8, 4, 2, 7, 1, 6])
print()
print(f"Endergebnis: {ergebnis}")

print()
print("=" * 60)
print()

# 2) Worst-case-Andeutung: bereits sortierte Liste -> Rekursionstiefe = n.
print("Worst-Case-Andeutung mit sortierter Liste [1, 2, 3, 4, 5]:")
print("-> jeder Pivot ist das kleinste Element, Tiefe waechst linear")
print("-" * 60)
quicksort_debug([1, 2, 3, 4, 5])
