"""
06 -- Komplexe Datentypen | Demo 4: Sets -- keine Duplikate

Zeigt:
- Set erstellen mit { } oder set()
- Duplikate werden automatisch entfernt
- add() / remove()
- Mengenoperationen: Schnitt, Vereinigung, Differenz
- Praxis: einzigartige Schuhgroessen aus Bestellungen
"""

# Bestellte Groessen vom heutigen Tag (mit vielen Duplikaten)
bestellte_groessen = [40, 41, 40, 42, 41, 41, 39, 40, 38, 42]

print(f"Alle Bestellungen ({len(bestellte_groessen)}): {bestellte_groessen}")

# Aus der Liste ein Set machen -> Duplikate weg
einzigartige = set(bestellte_groessen)
print(f"Einzigartige Groessen ({len(einzigartige)}): {einzigartige}")

print()
# Set direkt definieren
verfuegbar = {38, 39, 40, 41, 42, 43}
print(f"Lager fuehrt:  {verfuegbar}")

# Hinzufuegen / entfernen
verfuegbar.add(44)
print(f"Nach add(44):  {verfuegbar}")

verfuegbar.remove(38)
print(f"Nach remove(38): {verfuegbar}")

print()
# Mengenoperationen -- der Witz von Sets
gewuenscht = {39, 40, 41, 42}
auf_lager = {40, 41, 42, 43, 44}

# Welche Groessen sind sowohl gewuenscht ALS AUCH auf Lager?
schnitt = gewuenscht & auf_lager
print(f"Verfuegbar von gewuenscht: {schnitt}")

# Welche Groessen brauchen wir, die noch nicht auf Lager sind?
fehlend = gewuenscht - auf_lager
print(f"Nachbestellen:             {fehlend}")

# Komplette Auswahl
alle = gewuenscht | auf_lager
print(f"Komplette Auswahl:         {alle}")

print()
# 'in' ist sehr schnell auf Sets -- selbst bei Millionen Eintraegen
print(f"Ist 41 verfuegbar? {41 in auf_lager}")
print(f"Ist 36 verfuegbar? {36 in auf_lager}")
