"""
06 -- Komplexe Datentypen | Demo 3: Tupel -- unveraenderlich

Zeigt:
- Tupel mit runden Klammern (oder ganz ohne!)
- Index-Zugriff wie bei Listen
- Aenderung loest TypeError aus
- Tupel-Entpacken in einzelne Variablen
- Praxis: Produkt-Stammdaten als Tupel (Name, Preis, ID)
"""

# Veggie-Soles-Produkt als Tupel: (Name, Preis, ID)
produkt = ("Eco-Sneaker", 89.95, 1001)

print(f"Produkt: {produkt}")
print(f"Name:    {produkt[0]}")
print(f"Preis:   {produkt[1]} EUR")
print(f"ID:      {produkt[2]}")

# Tupel-Entpacken (kommt in NB 07 wieder)
name, preis, prod_id = produkt
print(f"\nEntpackt: name={name}, preis={preis}, id={prod_id}")

print()
# Tupel ohne Klammern -- in Python erlaubt
koord_lager = 52.508, 13.471      # Berlin
print(f"Lager-Koordinaten: {koord_lager}")
print(f"Typ: {type(koord_lager).__name__}")

print()
# Aenderungs-Versuch loest TypeError aus -- daher auskommentiert
# produkt[1] = 79.95     # TypeError: 'tuple' object does not support item assignment

# Stattdessen: neues Tupel erstellen
produkt_reduziert = (produkt[0], 79.95, produkt[2])
print(f"Reduziert: {produkt_reduziert}")

print()
# Liste von Tupeln -- klassisch fuer Stammdaten
katalog = [
    ("Eco-Sneaker",   89.95, 1001),
    ("Hemp-High",    109.00, 1002),
    ("Bambus-Boot",  135.50, 1003),
]
print("Veggie Soles -- Katalog:")
for produkt in katalog:
    print(f"  {produkt[0]:<14} {produkt[1]:>7.2f} EUR  (ID {produkt[2]})")
