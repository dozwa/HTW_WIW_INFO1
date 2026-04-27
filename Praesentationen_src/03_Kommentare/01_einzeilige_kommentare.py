"""
03 -- Kommentare | Demo 1: Einzeilige Kommentare mit #

Zeigt:
- Eigene Zeile vs. Zeilenende
- Code temporaer auskommentieren
- Konvention: Leerzeichen nach #
"""

# Veggie Soles -- aktueller Bestand der Top-Produkte
print("Bestandsuebersicht")

bestand_eco = 42        # Eco-Sneaker -- guter Verkaufsschlager
bestand_hemp = 15       # Hemp-High -- Nachschub bestellt
# bestand_bambus = 8    # Bambus-Boot -- aktuell ausgeblendet
bestand_jute = 23       # Jute-Runner -- Sommer-Hit

print(f"  Eco-Sneaker:  {bestand_eco}")
print(f"  Hemp-High:    {bestand_hemp}")
# print(f"  Bambus-Boot:  {bestand_bambus}")  # auskommentiert -> nicht ausgeben
print(f"  Jute-Runner:  {bestand_jute}")

# TODO: ab Lagerbestand < 10 automatisch Nachbestellung ausloesen
