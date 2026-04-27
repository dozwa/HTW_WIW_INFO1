"""
07 -- Funktionen | Demo 5: Scope -- lokal vs. global

Zeigt:
- Lokale Variablen leben nur in der Funktion
- Globale Variablen sind ueberall lesbar
- Parameter sind lokal
- Schreibzugriff auf Globale braucht 'global'-Keyword (kurz erwaehnt)
"""


# Globale Konstante: kennzeichnen wir nach Konvention mit GROSSBUCHSTABEN
VERSANDPAUSCHALE = 4.95
VERSANDFREI_AB = 100.00


def berechne_versand(bestellsumme):
    # 'rabatt' ist lokal -- existiert nur in dieser Funktion
    rabatt = 0.0 if bestellsumme < VERSANDFREI_AB else VERSANDPAUSCHALE
    return VERSANDPAUSCHALE - rabatt


# 1) Globale Variablen lesen klappt von ueberall
print(f"Pauschale (global gelesen): {VERSANDPAUSCHALE} EUR")
print(f"Frei-ab-Schwelle (global):  {VERSANDFREI_AB} EUR")

# 2) Funktion nutzt die globalen Werte intern
print(f"\nVersand fuer 89.95 EUR Bestellung:  {berechne_versand(89.95):.2f} EUR")
print(f"Versand fuer 150.00 EUR Bestellung: {berechne_versand(150.00):.2f} EUR")

# 3) Lokale Variablen sind ausserhalb nicht sichtbar
# print(rabatt)   # NameError -- 'rabatt' existiert hier nicht

# 4) Parameter sind ebenfalls lokal
def begruessung(name):
    gruss = f"Hallo {name}!"     # lokal
    return gruss


print(f"\n{begruessung('Anna')}")
# print(name)    # NameError -- nur in der Funktion sichtbar
# print(gruss)   # NameError -- ebenfalls nur lokal


# 5) Wer eine globale Variable INNERHALB einer Funktion ueberschreiben
#    moechte, braucht das 'global'-Keyword. Selten noetig -- lieber per
#    return nach aussen geben:
def alte_pauschale_aendern(neuer_wert):
    global VERSANDPAUSCHALE
    VERSANDPAUSCHALE = neuer_wert


alte_pauschale_aendern(5.95)
print(f"\nNeue Pauschale (nach Funktionsaufruf): {VERSANDPAUSCHALE} EUR")
