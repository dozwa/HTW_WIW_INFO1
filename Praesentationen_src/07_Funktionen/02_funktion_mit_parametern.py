"""
07 -- Funktionen | Demo 2: Parameter und Argumente

Zeigt:
- Parameter in der Definition
- Positionale vs. benannte Argumente
- Mischung erlaubt: positional vor benannt
"""


def zeige_produkt(name, preis, kategorie):
    print(f"  {name:<14} | {preis:>7.2f} EUR | {kategorie}")


print("Veggie Soles -- aktuelle Produkte:")
print("-" * 50)

# 1) Positionale Argumente -- Reihenfolge zaehlt
zeige_produkt("Eco-Sneaker", 89.95, "Low-Cut")
zeige_produkt("Hemp-High",   109.00, "Mid-Cut")

# 2) Benannte Argumente -- Reihenfolge egal
zeige_produkt(name="Bambus-Boot", preis=135.50, kategorie="Winter")
zeige_produkt(kategorie="Slipper", name="Cork-Slipper", preis=64.90)

# 3) Mischung: erst positional, dann benannt
zeige_produkt("Jute-Runner", 79.95, kategorie="Sport")

# 4) Was passiert bei vertauschter Reihenfolge?
#    Auskommentieren zum Vorfuehren -- gibt unsinniges Ergebnis,
#    aber keinen Fehler, weil die Typen passen.
# zeige_produkt(89.95, "Eco-Sneaker", "Low-Cut")
