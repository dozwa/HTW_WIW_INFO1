"""
14b -- Suchalgorithmen | Demo 4: Linear vs. Binaer auf 1 Million Werten.

Zeigt:
- gemessene Laufzeit auf einer grossen sortierten Liste
- Schrittzahl pro Algorithmus
- den drastischen Unterschied O(n) vs. O(log n)

Story: Veggie Soles wird mit 1 000 000 Bestell-IDs Spielzeug-Daten
generieren -- wir suchen eine ID linear vs. binaer.
"""

import time


def lineare_suche(liste, ziel):
    """Lineare Suche, zaehlt Schritte als Nebenprodukt."""
    schritte = 0
    for i in range(len(liste)):
        schritte += 1
        if liste[i] == ziel:
            return i, schritte
    return -1, schritte


def binaere_suche(liste, ziel):
    """Binaere Suche, zaehlt Schritte als Nebenprodukt."""
    lo, hi = 0, len(liste) - 1
    schritte = 0
    while lo <= hi:
        schritte += 1
        mid = (lo + hi) // 2
        if liste[mid] == ziel:
            return mid, schritte
        elif liste[mid] < ziel:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, schritte


# 1) Sortierte Eingabe-Liste mit n=1 000 000.
n = 1_000_000
print(f"Erzeuge sortierte Liste mit {n:,} Werten ...")
daten = list(range(n))   # [0, 1, 2, ..., 999_999]
ziel = n - 7             # liegt am Ende -> Worst Case fuer linear

print(f"Suche Wert {ziel:,} ...")
print()

# 2) Lineare Suche messen.
start = time.perf_counter()
pos_l, schritte_l = lineare_suche(daten, ziel)
dauer_l = (time.perf_counter() - start) * 1000

# 3) Binaere Suche messen.
start = time.perf_counter()
pos_b, schritte_b = binaere_suche(daten, ziel)
dauer_b = (time.perf_counter() - start) * 1000

# 4) Ergebnis-Tabelle.
print(f"{'Algorithmus':<18} | {'Schritte':>10} | {'Dauer (ms)':>12} | Ergebnis")
print("-" * 65)
print(f"{'Lineare Suche':<18} | {schritte_l:>10,} | {dauer_l:>12.2f} | Index {pos_l}")
print(f"{'Binaere Suche':<18} | {schritte_b:>10,} | {dauer_b:>12.2f} | Index {pos_b}")

# 5) Speedup berechnen.
print()
if dauer_b > 0:
    print(f">>> Binaere Suche braucht ca. {schritte_l / max(schritte_b, 1):>10.0f}x weniger Schritte.")
    print(f">>> Binaere Suche ist ca.    {dauer_l / dauer_b:>10.0f}x schneller (Wallclock).")
print()
print("    Voraussetzung: die Liste muss sortiert sein -- siehe NB 14a.")
