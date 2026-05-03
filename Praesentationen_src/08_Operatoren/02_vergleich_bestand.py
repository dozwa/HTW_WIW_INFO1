"""
08 -- Operatoren | Demo 2: Vergleichsoperatoren

Zeigt:
- ==, !=, <, >, <=, >=
- Vergleiche liefern bool
- = (Zuweisung) vs. == (Vergleich)

Story: Veggie Soles -- Lagerbestand.
"""


bestand_eco    = 12
bestand_hemp   = 0
mindestbestand = 5

print("Eco-Sneaker bestand:", bestand_eco)
print("Hemp-High bestand:  ", bestand_hemp)
print("Mindestbestand:     ", mindestbestand)
print()

# Vergleiche -- Ergebnis ist immer True/False
print("ist Eco knapp?     bestand_eco < mindestbestand  ->", bestand_eco < mindestbestand)
print("ist Hemp leer?     bestand_hemp == 0            ->", bestand_hemp == 0)
print("noch lieferbar?    bestand_eco != 0             ->", bestand_eco != 0)
print("genug Eco da?      bestand_eco >= mindestbestand ->", bestand_eco >= mindestbestand)

# Klassische Anfaenger-Falle: = vs. ==
# bestand_eco = mindestbestand   # ZUWEISUNG -- ueberschreibt den Bestand!
# print(bestand_eco == mindestbestand)  # VERGLEICH -- liefert True/False

# Variation: Vergleichsergebnis in Variable speichern
ist_knapp = bestand_eco < mindestbestand
print(f"\nFlag 'ist_knapp' (bool): {ist_knapp}, Typ: {type(ist_knapp).__name__}")
