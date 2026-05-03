"""
10 -- Schleifen | Demo 2: for ueber eine Liste

Zeigt:
- for VAR in SAMMLUNG: ...
- Schleife endet automatisch
- Mit if-Verzweigung in der Schleife (Bestandspruefung)

Story: Veggie Soles -- Warenkorbpruefung gegen Lagerbestand.
"""


warenkorb = ["Eco-Sneaker", "Hemp-High", "Bambus-Boot"]
lager     = {"Eco-Sneaker": 12, "Hemp-High": 0, "Bambus-Boot": 4}

for produkt in warenkorb:
    bestand = lager[produkt]
    if bestand > 0:
        print(f"{produkt}: lieferbar ({bestand} Stueck)")
    else:
        print(f"{produkt}: nicht verfuegbar")

# Beobachtung beim Vorfuehren:
# - In jedem Durchlauf zeigt 'produkt' auf den naechsten Listeneintrag.
# - Die Schleife endet, wenn die Liste durchlaufen ist -- ohne Zaehler.

# Variation: ueber einen String iterieren
print()
for buchstabe in "Veggie":
    print(buchstabe)
