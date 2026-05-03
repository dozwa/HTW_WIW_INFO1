"""
09 -- Verzweigungen | Demo 3: elif-Stufen fuer Rabatt

Zeigt:
- Mehrstufige Pruefung mit if/elif/else
- Reihenfolge: spezifischste Bedingung zuerst, allgemeinste am Ende
- Genau einer der Bloecke laeuft

Story: Veggie Soles -- Mengenrabatt.
"""


bestellsumme = 137.50
print(f"Bestellsumme: {bestellsumme:.2f} EUR")

if bestellsumme >= 200:
    rabatt = 0.15
    stufe  = "Premium (15 Prozent)"
elif bestellsumme >= 100:
    rabatt = 0.10
    stufe  = "Gross (10 Prozent)"
elif bestellsumme >= 50:
    rabatt = 0.05
    stufe  = "Standard (5 Prozent)"
else:
    rabatt = 0.0
    stufe  = "kein Rabatt"

ersparnis = bestellsumme * rabatt
endpreis  = bestellsumme - ersparnis

print(f"Rabattstufe: {stufe}")
print(f"Ersparnis:   {ersparnis:.2f} EUR")
print(f"Endpreis:    {endpreis:.2f} EUR")

# Variation zum Vorfuehren:
# bestellsumme = 49.99    # nur kein-Rabatt
# bestellsumme = 250.0    # Premium-Rabatt

# Wichtig: die Reihenfolge ZAEHLT!
# Wuerde "elif >= 50" zuerst stehen, wuerde JEDE Bestellung >= 50
# direkt 5 Prozent bekommen -- die hoeheren Stufen kaemen nie zum Zug.
