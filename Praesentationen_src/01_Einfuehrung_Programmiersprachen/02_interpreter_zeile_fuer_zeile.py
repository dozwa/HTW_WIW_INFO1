"""
01 -- Einfuehrung | Demo 2: Interpreter -- Zeile fuer Zeile

Zeigt:
- Python-Interpreter arbeitet sequentiell, Zeile fuer Zeile
- Reihenfolge der Ausgaben entspricht der Reihenfolge im Quelltext
- Kein Vorab-Build noetig -- direkt ausfuehrbar

Story: Veggie Soles -- Tagesreport.
"""


# Drei aufeinanderfolgende Anweisungen -- so liest sie der Interpreter.
print("Tagesreport Veggie Soles")
print("Top-Produkt 1: Eco-Sneaker")
print("Top-Produkt 2: Hemp-High")
print("Top-Produkt 3: Bambus-Boot")
print("Ende des Reports.")

# Didaktischer Punkt fuer die Vorlesung:
# Wuerde Zeile 2 weiter unten stehen, erschiene "Top-Produkt 1" auch erst spaeter.
# Der Interpreter rechnet keine Reihenfolge "schlau" um -- er arbeitet stumpf von oben nach unten.
