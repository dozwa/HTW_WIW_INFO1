"""
15 -- Programme | Demo 1: Spaghetti-Code vs. strukturiertes Programm

Zeigt:
- Wie loser Code schnell unuebersichtlich wird
- Wie dasselbe Programm mit Funktionen klarer wird
- Das Hauptprogramm liest sich am Ende wie eine Anleitung
"""

# ============================================================
# Variante A -- "Spaghetti": alles lose hintereinander
# ============================================================
print("A) Spaghetti-Code")
print("-" * 40)

shop = {
    "Eco-Sneaker": 89.95,
    "Hemp-High": 109.00,
    "Bambus-Boot": 135.50,
}

# Bestand anzeigen
print("\nSortiment:")
for produkt, preis in shop.items():
    print(f"  {produkt}: {preis} EUR")

# Gesamtwert
gesamt = 0
for preis in shop.values():
    gesamt = gesamt + preis
print(f"\nLagerwert: {gesamt:.2f} EUR")

# Teure Artikel markieren
print("\nArtikel ueber 100 EUR:")
for produkt, preis in shop.items():
    if preis > 100:
        print(f"  -> {produkt}: {preis} EUR")

# Problem: Alle drei Aufgaben (Anzeige, Summe, Filter) stehen
# durcheinander. Keine ist wiederverwendbar -- will man die Summe
# noch einmal, muss man die Schleife kopieren.


# ============================================================
# Variante B -- mit Funktionen + main()
# ============================================================
print("\n\nB) Strukturiert mit Funktionen")
print("-" * 40)


def sortiment_anzeigen(shop):
    """Listet alle Produkte mit Preis."""
    print("\nSortiment:")
    for produkt, preis in shop.items():
        print(f"  {produkt}: {preis} EUR")


def lagerwert(shop):
    """Berechnet die Summe aller Preise."""
    gesamt = 0
    for preis in shop.values():
        gesamt = gesamt + preis
    return gesamt


def teure_artikel(shop, grenze):
    """Druckt Artikel, deren Preis > grenze ist."""
    print(f"\nArtikel ueber {grenze} EUR:")
    for produkt, preis in shop.items():
        if preis > grenze:
            print(f"  -> {produkt}: {preis} EUR")


def main():
    """Hauptprogramm: Veggie Soles Sortimentsuebersicht."""
    shop = {
        "Eco-Sneaker": 89.95,
        "Hemp-High": 109.00,
        "Bambus-Boot": 135.50,
    }
    sortiment_anzeigen(shop)
    print(f"\nLagerwert: {lagerwert(shop):.2f} EUR")
    teure_artikel(shop, 100)


main()

# Beobachtung fuer den Lecturer:
# main() liest sich wie eine Bedienungsanleitung -- jeder Schritt
# ein Funktionsname. Die "Wie?"-Details stecken in den Hilfsfunktionen.
