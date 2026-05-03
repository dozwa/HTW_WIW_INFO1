"""
09 -- Verzweigungen | Demo 1: einfaches if

Zeigt:
- if + Bedingung + Doppelpunkt + Einrueckung
- Block laeuft nur, wenn die Bedingung True ist
- Mehrere Anweisungen im selben Block

Story: Veggie Soles -- Lagerwarnung.
"""


bestand_eco    = 3
mindestbestand = 5

print("Bestand Eco-Sneaker:", bestand_eco)

if bestand_eco < mindestbestand:
    print(">>> Achtung: Bestand niedrig!")
    print(">>> Bitte Nachbestellung pruefen.")

print("Tagesreport zu Ende.")

# Variation:
# bestand_eco = 12   # auf einen unkritischen Wert setzen
# Dann laeuft der if-Block nicht -- nur "Tagesreport zu Ende." erscheint.

# Klassiker-Falle (auskommentiert lassen):
# if bestand_eco < mindestbestand
#     print("...")        # SyntaxError: Doppelpunkt fehlt
