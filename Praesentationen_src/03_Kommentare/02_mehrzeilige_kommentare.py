"""
Veggie Soles -- Versandkosten-Kalkulation

Berechnet die Versandkosten fuer eine Bestellung nach den geltenden
Konditionen:

    - Pauschale: 4.95 EUR
    - Frei-ab-Schwelle: 100.00 EUR Warenwert

Stand: SoSe 2026
Autor: HTW WIW INFO1 -- Beispielcode
"""

# Modul-Docstring (oben) wird auch von help() angezeigt --
# das ist die offizielle Doku-Konvention in Python.

VERSANDPAUSCHALE = 4.95
VERSANDFREI_AB = 100.00

'''
Mehrzeiliger Kommentar mitten im Code:
Hier dokumentieren wir, warum wir 100.00 EUR als Schwelle nehmen --
naemlich weil das die Marketing-Vorgabe vom 12.04.2026 ist.
Ein einzeiliger Kommentar wuerde hier zu schmal werden.
'''

warenwert = 89.95

if warenwert >= VERSANDFREI_AB:
    versand = 0.0
else:
    versand = VERSANDPAUSCHALE

print(f"Warenwert: {warenwert:.2f} EUR")
print(f"Versand:   {versand:.2f} EUR")
print(f"Gesamt:    {warenwert + versand:.2f} EUR")
