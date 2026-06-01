"""
15 -- Programme | Demo 2: Funktionen als Bausteine -- Funktionen rufen Funktionen

Zeigt:
- Single Responsibility: jede Funktion macht EINE Sache
- Eine "Berichts"-Funktion delegiert an mehrere Hilfsfunktionen
- Abstraktion: der Berichtschreiber weiss nicht, *wie* angezeigt wird
"""

# --- kleine Bausteine -- jede Funktion hat EINE Aufgabe ---

def sortiment_anzeigen(shop):
    """Listet alle Produkte mit Preis."""
    for produkt, preis in shop.items():
        print(f"  {produkt:<14} {preis:>7.2f} EUR")


def lagerwert(shop):
    """Berechnet die Summe aller Preise."""
    gesamt = 0
    for preis in shop.values():
        gesamt = gesamt + preis
    return gesamt


def teuerstes_produkt(shop):
    """Gibt (Name, Preis) des teuersten Produkts zurueck."""
    teuer_name = None
    teuer_preis = 0
    for produkt, preis in shop.items():
        if preis > teuer_preis:
            teuer_preis = preis
            teuer_name = produkt
    return teuer_name, teuer_preis


# --- groessere Funktion, die die Bausteine kombiniert ---

def bericht_drucken(shop):
    """Druckt einen vollstaendigen Lagerbericht.

    Diese Funktion sagt nur 'WAS' passieren soll -- 'WIE' steckt
    in den Hilfsfunktionen. Das nennt man Abstraktion.
    """
    print("=" * 40)
    print("     VEGGIE SOLES -- LAGERBERICHT")
    print("=" * 40)

    print("\nSortiment:")
    sortiment_anzeigen(shop)

    print(f"\nLagerwert gesamt: {lagerwert(shop):.2f} EUR")
    print(f"Produktanzahl:    {len(shop)}")

    name, preis = teuerstes_produkt(shop)
    print(f"Teuerstes Produkt: {name} ({preis:.2f} EUR)")

    print("=" * 40)


# --- main() ruft nur den Berichtschreiber auf ---

def main():
    shop = {
        "Eco-Sneaker": 89.95,
        "Hemp-High": 109.00,
        "Bambus-Boot": 135.50,
    }
    bericht_drucken(shop)


main()

# Variante zum Vorfuehren:
# bericht_drucken({"Cork-Slipper": 64.90})  # andere Daten, gleicher Code
