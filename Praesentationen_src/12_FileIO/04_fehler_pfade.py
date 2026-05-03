"""
12 -- File I/O | Demo 4: Pfade + Fehlerbehandlung

Zeigt:
- Relative vs. absolute Pfade
- FileNotFoundError abfangen
- Sinnvoller Fallback statt Crash

Story: Veggie Soles -- Preisliste laden, falls vorhanden.
"""

import os


# 1) Relative vs. absolute Pfade
print(f"Aktuelles Arbeitsverzeichnis: {os.getcwd()}")
print(f"Beispiel relativer Pfad:      preise.txt")
print(f"Beispiel absoluter Pfad:      {os.path.abspath('preise.txt')}")
print()

# 2) Versuch, eine nicht existierende Datei zu lesen
def lade_preise(pfad):
    try:
        with open(pfad, "r") as f:
            zeilen = f.read().splitlines()
        print(f"OK: {len(zeilen)} Zeile(n) aus {pfad} geladen.")
        return zeilen
    except FileNotFoundError:
        print(f"Datei {pfad!r} nicht gefunden -- starte mit Standardliste.")
        return ["Eco-Sneaker", "Hemp-High", "Bambus-Boot"]


# Erster Versuch: Datei existiert nicht
liste1 = lade_preise("nicht_vorhanden.txt")
print("Liste 1:", liste1)
print()

# Zweiter Versuch: kurz eine Datei anlegen, dann lesen
pfad = "preise_demo.txt"
with open(pfad, "w") as f:
    f.write("Eco-Sneaker\nHemp-High\nBambus-Boot\nSandale\n")

liste2 = lade_preise(pfad)
print("Liste 2:", liste2)

# Aufraeumen
os.remove(pfad)

# Beobachtung beim Vorfuehren:
# - Erster Aufruf: FileNotFoundError -> Fallback wird genutzt.
# - Zweiter Aufruf: Datei existiert -> Inhalt wird gelesen.
# - Standard-Muster fuer "Datei lesen mit Default".
