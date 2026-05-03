"""
08 -- Operatoren | Demo 5: is vs. ==

Zeigt:
- == prueft Gleichheit der Werte
- is prueft Identitaet (gleiches Objekt im Speicher)
- Praktischer Einsatz: is None / is not None

Story: Veggie Soles -- zwei Bestelllisten vergleichen.
"""


# Zwei Listen mit gleichem Inhalt -- aber verschiedene Objekte
bestellung_anna = ["Eco-Sneaker", "Hemp-High"]
bestellung_max  = ["Eco-Sneaker", "Hemp-High"]

print("== prueft Inhalt:")
print(" Anna == Max:", bestellung_anna == bestellung_max)   # True

print("is prueft Objekt:")
print(" Anna is Max:", bestellung_anna is bestellung_max)   # False

# Wenn wir die gleiche Liste TEILEN
gemeinsame_liste = bestellung_anna   # gleicher "Briefumschlag"
print("\nNach 'gemeinsame_liste = bestellung_anna':")
print(" gemeinsame_liste is bestellung_anna:", gemeinsame_liste is bestellung_anna)
gemeinsame_liste.append("Bambus-Boot")
print(" Annas Liste danach:", bestellung_anna)
print(" Max' Liste:        ", bestellung_max)

# Praktischer Einsatz von is: gegen None testen
keine_lieferadresse = None
print("\nLieferadresse fehlt?  ", keine_lieferadresse is None)
print("Lieferadresse vorhanden?", keine_lieferadresse is not None)

# Faustregel:
# - Werte vergleichen  -> immer ==
# - None / True / False testen -> is / is not
