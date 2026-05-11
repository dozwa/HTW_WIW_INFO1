"""
13a -- Algorithmen modellieren | Demo 3: Primzahlpruefung schrittweise.

Zeigt:
- klassischen Algorithmus aus dem Notebook 13a, Kap. 5
- Print-Trace fuer jeden getesteten Teiler -- so sieht man, wo der
  Algorithmus abbricht (False) bzw. wann er bis zum Ende laeuft (True)

Story: Veggie Soles will eine Charge n Sneaker auf gleichgrosse Lager-
Einheiten verteilen. Geht das nur mit n selbst und 1? Dann ist n prim.
"""


def ist_primzahl(n):
    """Prueft, ob n eine Primzahl ist. Druckt den Pruefweg mit."""
    print(f">>> Pruefe n = {n}")

    # 1) Randfall: Zahlen unter 2 sind keine Primzahlen.
    if n < 2:
        print(f"    n < 2 -> KEINE Primzahl")
        return False

    # 2) Fuer jeden Kandidaten testen, ob er n teilt.
    for teiler in range(2, n):
        rest = n % teiler
        print(f"    teste Teiler {teiler}: {n} MOD {teiler} = {rest}")
        if rest == 0:
            print(f"    {teiler} teilt {n} -> KEINE Primzahl")
            return False

    # 3) Kein Teiler gefunden -> Primzahl.
    print(f"    kein Teiler gefunden -> {n} ist PRIM")
    return True


# 1) Erste Probe: 7 ist eine Primzahl.
print("=" * 50)
ist_primzahl(7)

# 2) Zweite Probe: 9 ist KEINE Primzahl.
print("=" * 50)
ist_primzahl(9)

# 3) Dritte Probe: Randfall 1.
print("=" * 50)
ist_primzahl(1)

# 4) Variation als Kommentar -- effizientere Variante:
# for teiler in range(2, int(n**0.5) + 1):  # nur bis sqrt(n) testen
#     ...
