"""
13a -- Algorithmen modellieren | Demo 4: Versandkosten als Algorithmus.

Zeigt:
- wie eine kleine Geschaeftsregel als Pseudocode formuliert wird
- die direkte Uebersetzung nach Python
- Print-Trace fuer jede Bestellung -- wir sehen jede Entscheidung

Story: Veggie Soles -- ab 100 EUR Bestellsumme ist der Versand frei,
darunter kostet er 4.95 EUR Pauschale.
"""


# 1) Pseudocode (Kommentar):
#
#    ALGORITHMUS Versand(bestellsumme)
#        EINGABE:  Bestellsumme in EUR
#        AUSGABE:  Versandkosten in EUR
#
#        WENN bestellsumme >= 100 DANN
#            RÜCKGABE 0.00
#        SONST
#            RÜCKGABE 4.95
#
# 2) Python-Uebersetzung:

def versand(bestellsumme):
    if bestellsumme >= 100:
        kosten = 0.00
        print(f"    Bestellsumme {bestellsumme:>6.2f} EUR >= 100 -> Versand FREI")
    else:
        kosten = 4.95
        print(f"    Bestellsumme {bestellsumme:>6.2f} EUR <  100 -> Versand {kosten:.2f} EUR")
    return kosten


# 3) Mehrere Beispielbestellungen aus der Veggie-Soles-Welt.
bestellungen = [
    ("Anna Mueller -- 1x Eco-Sneaker",        89.95),
    ("Max Schmidt -- 1x Hemp-High",          109.00),
    ("Anna Mueller -- 1x Eco-Sneaker, 1x Hemp-High", 198.95),
    ("Max Schmidt -- nur Socken",             19.95),
]

print("Versandkosten-Algorithmus (Veggie Soles):")
print("-" * 60)
gesamt_versand = 0.0
for label, summe in bestellungen:
    print(f"{label}")
    kosten = versand(summe)
    gesamt_versand = gesamt_versand + kosten
print("-" * 60)
print(f"Gesamtversand des Tages: {gesamt_versand:.2f} EUR")
