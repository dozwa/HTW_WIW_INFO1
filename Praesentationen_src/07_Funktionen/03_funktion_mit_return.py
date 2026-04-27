"""
07 -- Funktionen | Demo 3: Rueckgabewerte mit return

Zeigt:
- Unterschied print() vs. return
- Rueckgabewerte weiterverwenden
- return beendet die Funktion sofort

Story: Versandkosten bei Veggie Soles
       4.95 EUR Pauschale, gratis ab 100 EUR.
"""


def berechne_versand(bestellsumme):
    """Versand 0 EUR ab 100 EUR Bestellwert, sonst 4.95 EUR."""
    if bestellsumme >= 100:
        return 0.0
    return 4.95


# 1) Rueckgabewert in Variable speichern
versand = berechne_versand(89.95)
print(f"Versand fuer 89.95 EUR Bestellung: {versand} EUR")

versand = berechne_versand(150.00)
print(f"Versand fuer 150.00 EUR Bestellung: {versand} EUR")

# 2) Rueckgabewert direkt weiter verrechnen
warenwert = 109.00
gesamt = warenwert + berechne_versand(warenwert)
print(f"\nWarenwert {warenwert} EUR + Versand = {gesamt} EUR Gesamt")

# 3) Funktionen verschachteln
def formatiere_eur(betrag):
    return f"{betrag:.2f} EUR"


print(f"\nGesamt schoen formatiert: {formatiere_eur(gesamt)}")
print(f"Versand fuer 50 EUR Bestellung: {formatiere_eur(berechne_versand(50))}")
