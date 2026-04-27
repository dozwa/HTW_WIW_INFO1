"""
06 -- Komplexe Datentypen | Demo 1: Listen -- Grundlagen

Zeigt:
- Liste mit eckigen Klammern erstellen
- Index-Zugriff (positiv und negativ)
- len() fuer die Anzahl
- in / not in fuer "ist drin?"
"""

# Veggie-Soles-Warenkorb
warenkorb = ["Eco-Sneaker", "Hemp-High", "Bambus-Boot"]

print("Warenkorb-Inhalt:")
print(warenkorb)
print(f"Anzahl Artikel: {len(warenkorb)}")

print()
# Index-Zugriff -- ZAEHLUNG BEGINNT BEI 0
print(f"Erster Artikel  (Index 0): {warenkorb[0]}")
print(f"Zweiter Artikel (Index 1): {warenkorb[1]}")
print(f"Dritter Artikel (Index 2): {warenkorb[2]}")

print()
# Negative Indizes -- vom Ende
print(f"Letzter Artikel (Index -1): {warenkorb[-1]}")
print(f"Vorletzter (Index -2):       {warenkorb[-2]}")

print()
# Pruefen ob ein Artikel drin ist
print(f"'Eco-Sneaker' im Warenkorb? {'Eco-Sneaker' in warenkorb}")
print(f"'Cork-Slipper' im Warenkorb? {'Cork-Slipper' in warenkorb}")

print()
# Listen koennen unterschiedliche Typen mischen (in der Praxis selten gut)
gemischt = ["Eco-Sneaker", 89.95, 42, True]
print(f"Gemischte Liste: {gemischt}")
