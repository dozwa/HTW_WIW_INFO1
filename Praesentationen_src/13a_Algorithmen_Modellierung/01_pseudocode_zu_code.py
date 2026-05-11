"""
13a -- Algorithmen modellieren | Demo 1: Vom Pseudocode zum Python-Code.

Zeigt:
- wie ein Pseudocode-Block 1:1 in Python uebersetzt wird
- die GGT-Berechnung nach Euklid (Klassiker der Algorithmik)

Story: Veggie Soles -- vegane Sneaker. Wir nutzen GGT, um Bestellmengen
auf gemeinsame Verpackungseinheiten zu reduzieren.
"""


# 1) Hier steht der Pseudocode in Kommentar-Form:
#
#    ALGORITHMUS GGT(a, b)
#        SOLANGE b > 0:
#            rest ← a MOD b
#            a    ← b
#            b    ← rest
#        RÜCKGABE a
#
# 2) Zeile fuer Zeile in Python uebersetzt:

def ggt(a, b):
    while b > 0:
        rest = a % b
        a = b
        b = rest
    return a


# 3) Anwendung mit Veggie-Soles-Bestellmengen.
print(">>> GGT von 24 und 18 (Eco-Sneaker / Hemp-High-Bestellmengen):")
print(f"    ggt(24, 18) = {ggt(24, 18)}")

print(">>> GGT von 1080 und 252 (groesse Lagerstueckzahl):")
print(f"    ggt(1080, 252) = {ggt(1080, 252)}")

# 4) Variation als Kommentar -- der Lecturer kann live einkommentieren:
# print(f"    ggt(0, 5) = {ggt(0, 5)}  # Randfall: erste Zahl 0")
