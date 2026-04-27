"""
06 -- Komplexe Datentypen | Demo 4: Sets -- keine Duplikate

Zeigt:
- Set erstellen mit { } oder set()
- Duplikate werden automatisch entfernt
- add() / remove()
- 'in' fuer schnelle Pruefung

Verwendet nur Konzepte bis NB 06. Mengenoperationen (Schnitt, Vereinigung)
folgen in NB 08.
"""

# Bestellte Groessen vom heutigen Tag (mit vielen Duplikaten)
bestellte_groessen = [40, 41, 40, 42, 41, 41, 39, 40, 38, 42]

print("Alle Bestellungen:", bestellte_groessen)
print("Anzahl:           ", len(bestellte_groessen))

# Aus der Liste ein Set machen -> Duplikate weg
einzigartige = set(bestellte_groessen)
print()
print("Einzigartige Groessen:", einzigartige)
print("Anzahl:               ", len(einzigartige))

print()
# Set direkt definieren
verfuegbar = {38, 39, 40, 41, 42, 43}
print("Lager fuehrt:    ", verfuegbar)

# Hinzufuegen / entfernen
verfuegbar.add(44)
print("Nach add(44):    ", verfuegbar)

verfuegbar.remove(38)
print("Nach remove(38): ", verfuegbar)

print()
# 'in' ist sehr schnell auf Sets -- selbst bei Millionen Eintraegen
print("Ist 41 verfuegbar?", 41 in verfuegbar)
print("Ist 36 verfuegbar?", 36 in verfuegbar)

print()
# Klassischer Use-Case: doppelte Eintraege entfernen
roh = ["Anna", "Max", "Anna", "Lisa", "Max", "Anna"]
einzig = set(roh)
print("Roh-Liste:        ", roh)
print("Einzigartige Namen:", einzig)
