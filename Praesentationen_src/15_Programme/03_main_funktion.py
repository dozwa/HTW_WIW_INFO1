"""
15 -- Programme | Demo 3: Die main()-Funktion als Dirigent

Zeigt:
- main() steuert den Ablauf, enthaelt selbst kaum Logik
- main() liest sich wie eine Zusammenfassung des Programms
- Was gehoert in main() -- und was nicht?
"""

# --- Hilfsfunktionen: die "Instrumente" ---

def bestellung_erstellen():
    """Liefert eine Beispiel-Bestellung von Anna Mueller."""
    return [
        ("Eco-Sneaker", 89.95),
        ("Hemp-High", 109.00),
    ]


def zwischensumme(bestellung):
    """Summiert die Preise einer Bestellung."""
    summe = 0
    for _, preis in bestellung:
        summe = summe + preis
    return summe


def versand_berechnen(summe):
    """Versandkosten -- frei ab 100 EUR."""
    if summe >= 100:
        return 0.0
    return 4.95


def rechnung_drucken(kunde, bestellung, summe, versand):
    """Druckt eine formatierte Rechnung."""
    print(f"=== Rechnung fuer {kunde} ===")
    for name, preis in bestellung:
        print(f"  {name:<14} {preis:>7.2f} EUR")
    print(f"  {'Zwischensumme':<14} {summe:>7.2f} EUR")
    print(f"  {'Versand':<14} {versand:>7.2f} EUR")
    print(f"  {'GESAMT':<14} {summe + versand:>7.2f} EUR")


# --- main() als Dirigent: ruft die Hilfsfunktionen in Reihenfolge auf ---

def main():
    """Hauptprogramm: Eine Bestellung bei Veggie Soles abwickeln."""
    kunde = "Anna Mueller"
    bestellung = bestellung_erstellen()
    summe = zwischensumme(bestellung)
    versand = versand_berechnen(summe)
    rechnung_drucken(kunde, bestellung, summe, versand)


main()

# Beobachtung fuer den Lecturer:
# - main() hat keine Schleifen, keine if/else, keine arithmetische Logik.
# - Wer nur main() liest, versteht den kompletten Ablauf:
#     "Kunde -> Bestellung -> Zwischensumme -> Versand -> Rechnung."
# - Die Details ("WIE wird Versand berechnet?") stehen woanders.
