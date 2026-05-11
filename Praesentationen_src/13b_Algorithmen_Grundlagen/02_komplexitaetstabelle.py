"""
13b -- Komplexitaet | Demo 2: Tabelle der Operationen pro Komplexitaetsklasse.

Zeigt:
- Wie unterschiedlich Algorithmen mit n skalieren
- O(1), O(log n), O(n), O(n log n), O(n^2), O(2^n) im direkten Vergleich

Story: Veggie Soles betreibt einen Online-Shop. Wie viele "Operationen"
braucht ein Algorithmus, wenn der Shop 10, 100, 1000, 10 000 Produkte hat?
"""

import math


def vergleichstabelle(n_werte):
    """Druckt eine Tabelle: n und Operationen pro Komplexitaetsklasse."""
    kopf = f"{'n':>10} | {'O(1)':>8} | {'O(log n)':>10} | {'O(n)':>10} | {'O(n log n)':>12} | {'O(n^2)':>14}"
    print(kopf)
    print("-" * len(kopf))

    for n in n_werte:
        op_1 = 1
        op_log = int(math.log2(n))
        op_n = n
        op_nlogn = int(n * math.log2(n))
        op_n2 = n * n
        zeile = f"{n:>10} | {op_1:>8} | {op_log:>10} | {op_n:>10} | {op_nlogn:>12} | {op_n2:>14}"
        print(zeile)


# 1) Tabelle fuer typische Shop-Groessen.
print("Wachstumsverhalten (Anzahl Operationen):")
vergleichstabelle([10, 100, 1000, 10_000])

# 2) Den Schock von O(2^n) als Extra-Tabelle -- nur kleine n moeglich!
print()
print("Exponentielles Wachstum O(2^n) -- nur kleine n:")
print(f"{'n':>4} | {'2^n':>20}")
print("-" * 28)
for n in [10, 20, 30, 40, 50]:
    print(f"{n:>4} | {2 ** n:>20}")

# 3) Variation als Kommentar:
# vergleichstabelle([100_000, 1_000_000])   # O(n^2) wird unbenutzbar
