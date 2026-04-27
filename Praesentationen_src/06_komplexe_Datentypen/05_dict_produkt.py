"""
06 -- Komplexe Datentypen | Demo 5: Dictionaries -- Schluessel/Wert

Zeigt:
- Dictionary mit { "key": value } erstellen
- Zugriff per Schluessel d["key"]
- Werte aendern, neue hinzufuegen, loeschen
- keys() / values() / items()
- Praxis: Veggie-Soles-Produktkatalog als Dict-of-Dicts
"""

# Ein Produkt als Dictionary
produkt = {
    "name":    "Eco-Sneaker",
    "preis":   89.95,
    "bestand": 42,
    "vegan":   True,
    "groessen": [38, 39, 40, 41, 42],
}

print(f"Name:     {produkt['name']}")
print(f"Preis:    {produkt['preis']} EUR")
print(f"Bestand:  {produkt['bestand']}")
print(f"Vegan:    {produkt['vegan']}")
print(f"Groessen: {produkt['groessen']}")

print()
# Werte aendern -- gleiche Syntax wie Lesen
produkt["preis"] = 79.95     # Sale!
produkt["bestand"] -= 1      # Verkauf
print(f"Nach Sale: Preis={produkt['preis']}, Bestand={produkt['bestand']}")

# Neuen Schluessel hinzufuegen
produkt["bewertung"] = 4.7
print(f"Mit Bewertung: {produkt['bewertung']} Sterne")

# Schluessel loeschen
del produkt["vegan"]
print(f"Schluessel jetzt: {list(produkt.keys())}")

print()
# .keys() / .values() / .items()
print("Alle Schluessel:")
for key in produkt.keys():
    print(f"  - {key}")

print("\nAlle Werte:")
for value in produkt.values():
    print(f"  - {value}")

print("\nKey-Value-Paare:")
for key, value in produkt.items():
    print(f"  {key}: {value}")

print()
# Praxis: kompletter Veggie-Soles-Katalog als Dict-of-Dicts
katalog = {
    "eco":    {"name": "Eco-Sneaker",  "preis":  89.95, "bestand": 42},
    "hemp":   {"name": "Hemp-High",    "preis": 109.00, "bestand": 15},
    "bambus": {"name": "Bambus-Boot",  "preis": 135.50, "bestand":  8},
}

print("Veggie Soles -- Katalog:")
for kuerzel, info in katalog.items():
    print(f"  [{kuerzel}] {info['name']:<14} {info['preis']:>7.2f} EUR  ({info['bestand']} auf Lager)")
