"""
05 -- Einfache Datentypen | Demo 5: Typumwandlung

Zeigt:
- input() liefert IMMER str
- int() / float() / str() / bool() zur Umwandlung
- Typischer Fehler: Strings + Zahlen gemischt
- Praxis: Bestellungs-Eingabe verarbeiten
"""

# input() liefert IMMER str -- auch wenn der User "42" eingibt
# Hier hardcodieren wir die Eingaben, damit das Skript ohne User-Input laeuft.
print(">>> Simulation: User gibt '3' und '89.95' ein")

eingabe_anzahl = "3"          # so kaeme es von input("Anzahl: ")
eingabe_preis = "89.95"       # so kaeme es von input("Preis: ")

print(f"Typ von eingabe_anzahl: {type(eingabe_anzahl).__name__}")
print(f"Typ von eingabe_preis:  {type(eingabe_preis).__name__}")

# Wuerde NICHT funktionieren -- str * str geht nicht
# total = eingabe_anzahl * eingabe_preis    # TypeError

# Erst umwandeln, dann rechnen
anzahl = int(eingabe_anzahl)
preis = float(eingabe_preis)

print(f"\nNach Umwandlung:")
print(f"  anzahl: {anzahl} (Typ: {type(anzahl).__name__})")
print(f"  preis:  {preis} (Typ: {type(preis).__name__})")

total = anzahl * preis
print(f"  total:  {total:.2f} EUR")

print()
# Andersherum: Zahl in String -- braucht man fuer Konkatenation mit +
# (Mit f-string nicht noetig, aber zur Demo:)
ausgabe = "Gesamt: " + str(total) + " EUR"
print(ausgabe)

print()
# bool() hat eine Falle: nicht-leerer String wird True
print(f"bool('False') = {bool('False')}")      # True (!) -- nicht-leer
print(f"bool('')      = {bool('')}")           # False -- leerer String
print(f"bool(0)       = {bool(0)}")            # False -- 0
print(f"bool(0.0)     = {bool(0.0)}")          # False -- 0.0
print(f"bool(42)      = {bool(42)}")           # True

print()
print("Faustregel: bei input() mit Zahlen IMMER int() oder float() drumherum.")
