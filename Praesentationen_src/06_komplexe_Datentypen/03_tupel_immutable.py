"""
06 -- Komplexe Datentypen | Demo 3: Tupel -- unveraenderlich

Zeigt:
- Tupel mit runden Klammern (oder ganz ohne!)
- Index-Zugriff wie bei Listen
- Aenderungs-Versuch loest TypeError aus
- Tupel-Entpacken in einzelne Variablen
- Praxis: Produkt-Stammdaten als Tupel (Name, Preis, ID)

Verwendet nur Konzepte bis NB 06. Iteration (for-Loop) folgt in NB 10.
"""

# Veggie-Soles-Produkt als Tupel: (Name, Preis, ID)
produkt = ("Eco-Sneaker", 89.95, 1001)

print("Produkt:", produkt)
print("Name:   ", produkt[0])
print("Preis:  ", produkt[1], "EUR")
print("ID:     ", produkt[2])

# Tupel-Entpacken
name, preis, prod_id = produkt
print()
print("Entpackt:")
print("  name:    ", name)
print("  preis:   ", preis)
print("  prod_id: ", prod_id)

print()
# Tupel ohne Klammern -- in Python erlaubt
koord_lager = 52.508, 13.471      # Berlin
print("Lager-Koordinaten:", koord_lager)
print("Typ:              ", type(koord_lager).__name__)

print()
# Aenderungs-Versuch loest TypeError aus -- daher auskommentiert
# produkt[1] = 79.95     # TypeError: 'tuple' object does not support item assignment

# Stattdessen: neues Tupel erstellen
produkt_reduziert = (produkt[0], 79.95, produkt[2])
print("Original:    ", produkt)
print("Reduziert:   ", produkt_reduziert)

print()
# Liste von Tupeln -- klassisch fuer Stammdaten
katalog = [
    ("Eco-Sneaker",   89.95, 1001),
    ("Hemp-High",    109.00, 1002),
    ("Bambus-Boot",  135.50, 1003),
]

print("Veggie Soles -- Katalog (Liste von Tupeln):")
print(" ", katalog[0])
print(" ", katalog[1])
print(" ", katalog[2])

# Index-Zugriff geht bis ins innere Tupel hinein
print()
print("Erstes Produkt im Katalog:")
print("  Name: ", katalog[0][0])
print("  Preis:", katalog[0][1])
