"""
04 -- Variablen | Demo 4: Mehrfachzuweisung

Zeigt:
- Mehrere Variablen in einer Zeile
- Allen denselben Wert zuweisen
- Werte tauschen ohne Zwischenspeicher

Verwendet nur Konzepte aus den Notebooks 01-04 (print, Variablen,
Mehrfachzuweisung). Keine Tupel/Listen -- die kommen in NB 06.
"""

# Mehrere Variablen in einer Zeile -- Veggie-Soles-Stammprodukt
name, preis, bestand = "Eco-Sneaker", 89.95, 42

print(name)
print(preis)
print(bestand)

print()
# Allen denselben Wert zuweisen -- praktisch bei Initialisierung
verkauft_montag = verkauft_dienstag = verkauft_mittwoch = 0

print("Mo:", verkauft_montag)
print("Di:", verkauft_dienstag)
print("Mi:", verkauft_mittwoch)

print()
# Werte tauschen -- in vielen Sprachen braucht man dafuer eine Hilfsvariable.
# Python kann das in einer Zeile.
preis_eco = 89.95
preis_hemp = 109.00

print("Vorher:")
print("  Eco:  ", preis_eco)
print("  Hemp: ", preis_hemp)

preis_eco, preis_hemp = preis_hemp, preis_eco

print("Nachher (getauscht):")
print("  Eco:  ", preis_eco)
print("  Hemp: ", preis_hemp)

print()
# Mehrere Werte direkt zuweisen -- Reihenfolge zaehlt
platz1, platz2, platz3 = "Eco-Sneaker", "Hemp-High", "Bambus-Boot"
print("Top 1:", platz1)
print("Top 2:", platz2)
print("Top 3:", platz3)
