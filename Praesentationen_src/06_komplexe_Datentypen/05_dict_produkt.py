"""
06 -- Komplexe Datentypen | Demo 5: Dictionaries -- Schluessel/Wert

Zeigt:
- Dictionary mit { "key": value } erstellen
- Zugriff per Schluessel d["key"]
- Werte aendern, neue hinzufuegen, loeschen
- keys() / values() / items() liefern Listen-aehnliche Sichten
- Praxis: Veggie-Soles-Produktkatalog als Dict-of-Dicts

Verwendet nur Konzepte bis NB 06. Iteration (for-Loop) folgt in NB 10.
"""

# Ein Produkt als Dictionary
produkt = {
    "name":    "Eco-Sneaker",
    "preis":   89.95,
    "bestand": 42,
    "vegan":   True,
    "groessen": [38, 39, 40, 41, 42],
}

print("Name:    ", produkt["name"])
print("Preis:   ", produkt["preis"], "EUR")
print("Bestand: ", produkt["bestand"])
print("Vegan:   ", produkt["vegan"])
print("Groessen:", produkt["groessen"])

print()
# Werte aendern -- gleiche Syntax wie Lesen
produkt["preis"] = 79.95     # Sale!
produkt["bestand"] = produkt["bestand"] - 1   # Verkauf

print("Nach Sale:")
print("  Preis:  ", produkt["preis"])
print("  Bestand:", produkt["bestand"])

# Neuen Schluessel hinzufuegen
produkt["bewertung"] = 4.7
print("Mit Bewertung:", produkt["bewertung"], "Sterne")

# Schluessel loeschen
del produkt["vegan"]
print("Schluessel jetzt:", list(produkt.keys()))

print()
# .keys() / .values() / .items() -- liefern Sichten auf Daten
print("Alle Schluessel:", list(produkt.keys()))
print("Alle Werte:    ", list(produkt.values()))
print("Erstes item:   ", list(produkt.items())[0])

print()
# Praxis: kompletter Veggie-Soles-Katalog als Dict-of-Dicts
katalog = {
    "eco":    {"name": "Eco-Sneaker",  "preis":  89.95, "bestand": 42},
    "hemp":   {"name": "Hemp-High",    "preis": 109.00, "bestand": 15},
    "bambus": {"name": "Bambus-Boot",  "preis": 135.50, "bestand":  8},
}

print("Veggie Soles -- Katalog:")
print("  [eco]    ", katalog["eco"]["name"], "->", katalog["eco"]["preis"], "EUR")
print("  [hemp]   ", katalog["hemp"]["name"], "->", katalog["hemp"]["preis"], "EUR")
print("  [bambus] ", katalog["bambus"]["name"], "->", katalog["bambus"]["preis"], "EUR")

# Pruefung mit 'in' -- gibt's einen Schluessel?
print()
print("'eco' im Katalog?  ", "eco" in katalog)
print("'jute' im Katalog? ", "jute" in katalog)
