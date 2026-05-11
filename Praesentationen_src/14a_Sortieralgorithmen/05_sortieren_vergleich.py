"""
14a -- Sortieralgorithmen | Demo 5: Bubble vs. Insertion vs. Pythons sorted().

Zeigt:
- echten Zeitvergleich auf einer mittelgrossen Zufallsliste
- warum man in der Praxis IMMER `sorted()` nimmt

Story: Veggie Soles -- 2000 Bestellsummen aus einer Woche sortieren.
"""

import random
import time


def bubble_sort(liste):
    n = len(liste)
    for i in range(n):
        getauscht = False
        for j in range(n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
                getauscht = True
        if not getauscht:
            break
    return liste


def insertion_sort(liste):
    for i in range(1, len(liste)):
        schluessel = liste[i]
        j = i - 1
        while j >= 0 and liste[j] > schluessel:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = schluessel
    return liste


def messen(funktion, daten, name):
    """Misst, wie lange die Sortierfunktion braucht."""
    kopie = daten.copy()
    start = time.perf_counter()
    funktion(kopie)
    dauer_ms = (time.perf_counter() - start) * 1000
    print(f"  {name:<22}: {dauer_ms:>10.2f} ms")
    return dauer_ms


# 1) Reproduzierbare Zufallsdaten.
random.seed(42)
daten = [round(random.uniform(10.0, 200.0), 2) for _ in range(2000)]
print(f"Sortieren von {len(daten)} zufaelligen Bestellsummen:")
print()

# 2) Drei Algorithmen messen.
t_bubble = messen(bubble_sort, daten, "Bubble Sort")
t_insert = messen(insertion_sort, daten, "Insertion Sort")
t_python = messen(sorted, daten, "Pythons sorted()")

# 3) Verhaeltnis ausrechnen.
print()
print(">>> Beobachtung:")
if t_python > 0:
    print(f"    Bubble    ist ca. {t_bubble / t_python:>6.0f}x langsamer als sorted().")
    print(f"    Insertion ist ca. {t_insert / t_python:>6.0f}x langsamer als sorted().")
print()
print("    sorted() = TimSort, O(n log n) -- in der Praxis fast immer richtig.")

# 4) Variation als Kommentar -- groesseres n probieren:
# daten = [round(random.uniform(10.0, 200.0), 2) for _ in range(10_000)]
# Bubble/Insertion werden ab hier sehr langsam (~Sekunden).
