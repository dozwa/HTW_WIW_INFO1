"""
13b -- Komplexitaet | Demo 1: O(1) vs. O(n) im Zeit-Vergleich.

Zeigt:
- konstanten Listenzugriff (O(1)) vs. Listendurchlauf (O(n))
- gemessene Laufzeit auf grossen Listen ueber das `time`-Modul
- dass O(1) unabhaengig von n ist

Story: Veggie-Soles-Lager mit n Bestellungen. "Erste Bestellung ansehen"
ist O(1), "Gesamtumsatz berechnen" ist O(n).
"""

import time


def erste_bestellung(bestellungen):
    """O(1): Zugriff per Index ist immer gleich schnell."""
    return bestellungen[0]


def gesamtumsatz(bestellungen):
    """O(n): muss jede Bestellung anschauen."""
    summe = 0.0
    for preis in bestellungen:
        summe = summe + preis
    return summe


# 1) Zwei verschieden grosse "Lager" aus Veggie-Soles-Preisen aufbauen.
preise_template = [89.95, 109.00, 135.50]

lager_klein = preise_template * 1000        #   3 000 Eintraege
lager_gross = preise_template * 1_000_000   # 3 000 000 Eintraege

print(f"Lager klein:  {len(lager_klein):>10} Bestellungen")
print(f"Lager gross:  {len(lager_gross):>10} Bestellungen")
print()

# 2) O(1)-Funktion auf beiden Lagern messen.
print("=== O(1): erste_bestellung() ===")
for name, lager in [("klein", lager_klein), ("gross", lager_gross)]:
    start = time.perf_counter()
    for _ in range(1000):                    # 1000-mal ausfuehren, sonst zu kurz
        erste_bestellung(lager)
    dauer = (time.perf_counter() - start) * 1000
    print(f"  {name:<5}: {dauer:.3f} ms (fuer 1000 Aufrufe)")

# 3) O(n)-Funktion auf beiden Lagern messen.
print()
print("=== O(n): gesamtumsatz() ===")
for name, lager in [("klein", lager_klein), ("gross", lager_gross)]:
    start = time.perf_counter()
    gesamtumsatz(lager)
    dauer = (time.perf_counter() - start) * 1000
    print(f"  {name:<5}: {dauer:.3f} ms")

# 4) Beobachtung kommentieren:
print()
print(">>> Beobachtung:")
print("    O(1): Lagergroesse egal -- Dauer praktisch konstant.")
print("    O(n): Lager 1000x groesser -> Dauer ca. 1000x laenger.")
