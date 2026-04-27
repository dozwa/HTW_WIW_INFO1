"""
04 -- Variablen | Demo 2: Werte ueberschreiben

Zeigt:
- Eine Variable kann mehrfach neu zugewiesen werden
- Berechnung mit dem alten Wert: x = x - 1
- Reihenfolge der Zuweisungen ist wichtig
"""

# Bestand an Eco-Sneakern im Tagesverlauf
bestand = 42
print(f"Morgens:       {bestand} Paar")

# Mittags: 5 Verkaeufe
bestand = bestand - 5
print(f"Nach Mittag:   {bestand} Paar")

# Nachschub: 20 Paar werden geliefert
bestand = bestand + 20
print(f"Nach Lieferung: {bestand} Paar")

# Abend: 8 Verkaeufe
bestand = bestand - 8
print(f"Abend:         {bestand} Paar")

# Kurzform mit erweiterter Zuweisung -- macht dasselbe
bestand -= 3        # gleichbedeutend mit: bestand = bestand - 3
print(f"Vor Schliessung: {bestand} Paar")

print()
# Variable kann auch ihren TYP wechseln (in Python erlaubt, aber selten gut)
status = bestand            # int
print(f"status (int):  {status}")
status = "ausverkauft"      # gleiche Variable, jetzt str
print(f"status (str):  {status}")
