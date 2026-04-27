"""
04 -- Variablen | Demo 4: Mehrfachzuweisung

Zeigt:
- Mehrere Variablen in einer Zeile
- Tupel-Entpacken (kommt spaeter bei Funktionen wieder)
- Werte tauschen ohne Zwischenspeicher
- Allen denselben Wert zuweisen
"""

# Mehrere Variablen in einer Zeile -- Veggie-Soles-Stammprodukt
name, preis, bestand = "Eco-Sneaker", 89.95, 42

print(f"{name}: {preis} EUR, {bestand} Paar auf Lager")

print()
# Allen denselben Wert zuweisen -- praktisch bei Initialisierung
verkauft_montag = verkauft_dienstag = verkauft_mittwoch = 0

print(f"Mo: {verkauft_montag}, Di: {verkauft_dienstag}, Mi: {verkauft_mittwoch}")

print()
# Werte tauschen -- in vielen Sprachen braucht man dafuer eine Hilfsvariable.
# Python kann das in einer Zeile.
preis_eco = 89.95
preis_hemp = 109.00

print(f"Vorher: Eco={preis_eco}, Hemp={preis_hemp}")

preis_eco, preis_hemp = preis_hemp, preis_eco

print(f"Nachher (getauscht): Eco={preis_eco}, Hemp={preis_hemp}")

print()
# Achtung: Anzahl Variablen muss zur Anzahl Werte passen
# Funktioniert
top_drei = ("Eco-Sneaker", "Hemp-High", "Bambus-Boot")
platz1, platz2, platz3 = top_drei
print(f"Top 3: {platz1}, {platz2}, {platz3}")

# Wuerde Fehler ausloesen (auskommentiert):
# a, b = 1, 2, 3   # ValueError: too many values to unpack
