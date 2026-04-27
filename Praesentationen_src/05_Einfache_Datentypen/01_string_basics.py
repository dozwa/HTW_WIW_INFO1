"""
05 -- Einfache Datentypen | Demo 1: Strings (Text) -- Grundlagen

Zeigt:
- Anfuehrungszeichen: einfach, doppelt, dreifach
- Konkatenation mit +
- Wiederholung mit *
- Laenge mit len()
- f-string fuer Formatierung
"""

# Drei Schreibweisen fuer denselben String
produkt_a = "Eco-Sneaker"
produkt_b = 'Hemp-High'
beschreibung = """
Klassischer Low-Cut, recyceltes Polyester
Groessen 36-46
"""

print(produkt_a)
print(produkt_b)
print(beschreibung)

# Konkatenation mit +
satz = produkt_a + " kostet " + "89.95 EUR"
print(satz)

# Wiederholung mit *
trenner = "=" * 40
print(trenner)
print("Veggie Soles -- Tagesreport")
print(trenner)

# Laenge mit len()
print(f"'{produkt_a}' hat {len(produkt_a)} Zeichen")

# f-string -- moderner und lesbarer
preis = 89.95
print(f"{produkt_a}: {preis} EUR")
