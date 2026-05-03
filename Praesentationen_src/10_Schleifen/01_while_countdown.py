"""
10 -- Schleifen | Demo 1: while-Schleife

Zeigt:
- while + Bedingung + Doppelpunkt + Block
- Bedingung wird VOR jedem Durchlauf geprueft
- Schleife muss sich selbst beenden (Zaehler runter)

Story: Veggie Soles -- Restbestand-Countdown bis Lager leer.
"""


bestand_hemp = 5

while bestand_hemp > 0:
    print(f"Hemp-High auf Lager: {bestand_hemp}")
    bestand_hemp = bestand_hemp - 1     # auch: bestand_hemp -= 1

print("Lager leer -- Nachbestellung ausloesen!")

# Variation zum Vorfuehren:
# bestand_hemp = 0     # Schleife laeuft NIE -- Bedingung schon falsch
# bestand_hemp = 100   # 100 Durchlaeufe

# Klassiker-Falle (NICHT einkommentieren -- erzeugt Endlosschleife):
# while bestand_hemp > 0:
#     print(bestand_hemp)
#     # Zaehler vergessen! -> haengt sich auf, STRG+C noetig
