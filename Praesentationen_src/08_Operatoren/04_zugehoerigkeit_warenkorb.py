"""
08 -- Operatoren | Demo 4: in / not in

Zeigt:
- Zugehoerigkeit auf Listen, Sets, Dicts, Strings
- Praktische Pruefung im Warenkorb
- Case-Sensitivitaet bei Strings

Story: Veggie Soles -- Warenkorb und Sortimentspruefung.
"""


warenkorb = ["Eco-Sneaker", "Hemp-High"]
sortiment = {"Eco-Sneaker", "Hemp-High", "Bambus-Boot"}

# in -- ist ein Element in der Sammlung?
print("Eco-Sneaker im Warenkorb? ", "Eco-Sneaker" in warenkorb)
print("Bambus-Boot im Warenkorb?", "Bambus-Boot" in warenkorb)

# not in -- Negation
print("Bambus-Boot fehlt? ", "Bambus-Boot" not in warenkorb)

# Auch auf Sets
print("Hemp-High im Sortiment? ", "Hemp-High" in sortiment)

# Auf Dictionaries: prueft die Schluessel
preise = {"Eco-Sneaker": 89.95, "Hemp-High": 109.00, "Bambus-Boot": 135.50}
print("Preis fuer 'Hemp-High' bekannt?", "Hemp-High" in preise)
print("Preis fuer 'Sandale' bekannt?  ", "Sandale" in preise)

# Auf Strings: Teilstring-Pruefung
suchbegriff = "sneaker"
treffer     = suchbegriff in "Eco-Sneaker".lower()
print(f"'{suchbegriff}' in 'Eco-Sneaker' (lower): {treffer}")

# Variation: Case-Sensitivitaet -- ohne .lower() schlaegt das oft fehl
print(f"'sneaker' in 'Eco-Sneaker' (ohne lower): {'sneaker' in 'Eco-Sneaker'}")
