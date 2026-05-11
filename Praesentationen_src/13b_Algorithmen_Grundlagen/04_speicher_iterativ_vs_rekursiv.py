"""
13b -- Komplexitaet | Demo 4: Speicher-Komplexitaet -- iterativ vs. rekursiv.

Zeigt:
- iterative Variante (Schleife):  Zeit O(n), Speicher O(1)
- rekursive Variante (Selbstaufruf): Zeit O(n), Speicher O(n)
- den Unterschied im Speicherbedarf via `tracemalloc`

Story: Veggie Soles muss eine Bestellsumme aus n Posten berechnen.
"""

import tracemalloc


def summe_iterativ(liste):
    """O(1) Speicher: nur eine Akku-Variable."""
    summe = 0
    for x in liste:
        summe = summe + x
    return summe


def summe_rekursiv(liste):
    """O(n) Speicher: jeder Aufruf legt einen Stack-Frame an."""
    if len(liste) == 0:
        return 0
    return liste[0] + summe_rekursiv(liste[1:])


# 1) Bestellung mit n=200 Posten anlegen (klein genug fuer Rekursion).
posten = [1.99] * 200

# 2) Iterativ messen.
tracemalloc.start()
ergebnis_it = summe_iterativ(posten)
_, peak_it = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"iterativ:  Ergebnis = {ergebnis_it:.2f} EUR")
print(f"           Peak-Speicher waehrend des Aufrufs: {peak_it} Byte")

print()

# 3) Rekursiv messen.
tracemalloc.start()
ergebnis_re = summe_rekursiv(posten)
_, peak_re = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"rekursiv:  Ergebnis = {ergebnis_re:.2f} EUR")
print(f"           Peak-Speicher waehrend des Aufrufs: {peak_re} Byte")

# 4) Vergleich.
print()
print(">>> Beobachtung:")
if peak_it > 0:
    print(f"    Faktor: {peak_re / peak_it:.1f}x mehr Speicher fuer rekursive Variante.")
else:
    print(f"    iterativ alloziiert nichts neu (Peak nahe 0).")
    print(f"    rekursiv: {peak_re} Byte zusaetzlich.")
print("    (Stack-Frames + zwischengespeicherte Restlisten = O(n).)")

# 5) Variation als Kommentar -- noch groessere Listen kosten Stack:
# summe_rekursiv([1.0] * 5000)   # RecursionError!
