"""
12 -- File I/O | Demo 1: open / write / close

Zeigt:
- open(name, "w") legt eine Datei an (oder ueberschreibt)
- write() schreibt Strings (kein automatisches \\n!)
- close() ist Pflicht -- ohne es gehen Daten verloren

Story: Veggie Soles -- einfacher Tagesreport.
Hinweis: Demo legt eine Datei im aktuellen Verzeichnis an und loescht
sie am Ende wieder, damit der Repo-Ordner sauber bleibt.
"""

import os


pfad = "tagesreport_demo.txt"

# 1) Datei oeffnen, schreiben, schliessen.
f = open(pfad, "w")
f.write("Veggie Soles -- Tagesreport\n")
f.write("Eco-Sneaker 89.95 EUR\n")
f.write("Hemp-High   109.00 EUR\n")
f.write("Bambus-Boot 135.50 EUR\n")    # \n nicht vergessen
f.close()

print(f"Datei geschrieben: {pfad}")

# 2) Inhalt zur Kontrolle direkt zurueckgelesen
f = open(pfad, "r")
print("--- Datei-Inhalt ---")
print(f.read())
f.close()

# 3) Aufraeumen
os.remove(pfad)
print(f"Datei wieder geloescht: {pfad}")

# Variation zum Vorfuehren:
# - close() weglassen -> moeglicher Datenverlust
# - "w" durch "a" ersetzen -> jeweils anhaengen statt ueberschreiben
