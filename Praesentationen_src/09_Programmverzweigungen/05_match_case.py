"""
09 -- Verzweigungen | Demo 5: match-case fuer Modellbeschreibung

Zeigt:
- match auf einer Variable mit mehreren exakten Werten
- case _: als Default-Fall
- Wann match-case besser passt als if/elif

Story: Veggie Soles -- Modellbeschreibung im Shop.
Voraussetzung: Python 3.10+ (an der HTW im Labor erfuellt).
"""


def beschreibung(modell):
    match modell:
        case "Eco-Sneaker":
            return "Klassiker -- recyceltes Polyester, 89.95 EUR."
        case "Hemp-High":
            return "Knoechelhoch, Obermaterial aus Hanf, 109.00 EUR."
        case "Bambus-Boot":
            return "Winterfest, Bambusfaser-Innenfutter, 135.50 EUR."
        case _:
            return "Modell nicht im Sortiment."


# Drei Sortiment-Treffer + ein Unbekanntes
print(beschreibung("Eco-Sneaker"))
print(beschreibung("Hemp-High"))
print(beschreibung("Bambus-Boot"))
print(beschreibung("Sandale"))

# Wann lieber if-elif?
# Bei BEREICHEN (z. B. bestellsumme >= 50) bringt match nichts, weil
# match auf exakte Werte zielt. Faustregel:
# - "ist gleich diesem konkreten Wert" -> match
# - "ist groesser als" / "passt zu Range" -> if/elif
