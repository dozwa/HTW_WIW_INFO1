"""
15 -- Programme | Demo 5: Komplettes Veggie-Soles-Programm mit allen 5 Bausteinen

Zeigt:
- Die ideale .py-Struktur in einer einzigen Datei
- Imports -> Konstanten -> Hilfsfunktionen -> main() -> if __name__
- Fehlerbehandlung im Hauptablauf

So vorfuehren:
  python3 05_veggie_soles_komplett.py
"""

# ============================================================
# 1. Imports
# ============================================================
from datetime import date


# ============================================================
# 2. Konstanten -- aendern sich nie waehrend der Laufzeit
# ============================================================
SHOP_NAME = "Veggie Soles"
VERSANDPAUSCHALE = 4.95
VERSANDFREI_AB = 100.00
MINDESTBESTELLWERT = 25.00


# ============================================================
# 3. Hilfsfunktionen -- jede hat genau EINE Aufgabe
# ============================================================
def katalog_erstellen():
    """Liefert den aktuellen Produktkatalog."""
    return {
        "Eco-Sneaker": 89.95,
        "Hemp-High":   109.00,
        "Bambus-Boot": 135.50,
    }


def zwischensumme_berechnen(bestellung, katalog):
    """Summiert die Preise einer Bestellung (Liste von Produktnamen)."""
    summe = 0
    for produkt in bestellung:
        if produkt in katalog:
            summe = summe + katalog[produkt]
    return summe


def versand_berechnen(summe):
    """Versandpauschale -- frei ab VERSANDFREI_AB."""
    if summe >= VERSANDFREI_AB:
        return 0.0
    return VERSANDPAUSCHALE


def bestellung_pruefen(summe):
    """Prueft, ob Mindestbestellwert erreicht ist.

    Wirft ValueError, wenn nicht -- main() faengt das ab.
    """
    if summe < MINDESTBESTELLWERT:
        raise ValueError(
            f"Mindestbestellwert {MINDESTBESTELLWERT} EUR nicht erreicht."
        )


def rechnung_drucken(kunde, bestellung, katalog, summe, versand):
    """Druckt eine formatierte Rechnung."""
    print(f"=== {SHOP_NAME} -- Rechnung vom {date.today()} ===")
    print(f"Kunde: {kunde}\n")
    for produkt in bestellung:
        preis = katalog[produkt]
        print(f"  {produkt:<14} {preis:>7.2f} EUR")
    print("  " + "-" * 24)
    print(f"  {'Zwischensumme':<14} {summe:>7.2f} EUR")
    print(f"  {'Versand':<14} {versand:>7.2f} EUR")
    print(f"  {'GESAMT':<14} {summe + versand:>7.2f} EUR")


# ============================================================
# 4. main() -- der Dirigent
# ============================================================
def main():
    """Bestellabwicklung fuer eine Beispielbestellung."""
    katalog = katalog_erstellen()
    kunde = "Anna Mueller"
    bestellung = ["Eco-Sneaker", "Hemp-High"]

    summe = zwischensumme_berechnen(bestellung, katalog)

    try:
        bestellung_pruefen(summe)
    except ValueError as e:
        print(f"Bestellung abgelehnt: {e}")
        return

    versand = versand_berechnen(summe)
    rechnung_drucken(kunde, bestellung, katalog, summe, versand)


# ============================================================
# 5. Einstiegspunkt
# ============================================================
if __name__ == "__main__":
    main()
