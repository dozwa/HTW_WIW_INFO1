"""
05 -- Einfache Datentypen | Demo 4: Boolean -- True/False

Zeigt:
- Bool-Werte True/False
- Vergleichsoperatoren als Bool-Quelle
- 'in'-Operator auf Strings
- bool() zur Typumwandlung

Verwendet nur Konzepte bis NB 05. Logik-Verknuepfungen (and/or/not)
folgen in NB 08.
"""

# Direkte Bool-Werte
auf_lager = True
ausverkauft = False

print("auf_lager:    ", auf_lager)
print("ausverkauft:  ", ausverkauft)
print("type:         ", type(auf_lager).__name__)

print()
# Bool aus Vergleichen -- die Hauptquelle fuer Bool-Werte
preis = 89.95

print("preis > 100   →", preis > 100)        # False
print("preis < 100   →", preis < 100)        # True
print("preis == 89.95 →", preis == 89.95)    # True
print("preis != 0    →", preis != 0)         # True
print("preis >= 50   →", preis >= 50)        # True
print("preis <= 50   →", preis <= 50)        # False

print()
# 'in' funktioniert auf Strings (und auf Listen, kommt in NB 06)
produkt = "Eco-Sneaker"
print("'Eco' in produkt:  ", "Eco" in produkt)        # True
print("'Hemp' in produkt: ", "Hemp" in produkt)       # False

print()
# bool() hat eine Falle: nicht-leerer String wird True
print("bool('False') =", bool('False'))      # True (!) -- nicht-leer
print("bool('')      =", bool(''))           # False -- leerer String
print("bool(0)       =", bool(0))            # False -- 0
print("bool(0.0)     =", bool(0.0))          # False -- 0.0
print("bool(42)      =", bool(42))           # True

print()
# Bool als Ergebnis einer Pruefung speichern
warenwert = 105.00
versand_frei_grenze = 100.00
versand_gratis = warenwert >= versand_frei_grenze

print("warenwert:        ", warenwert)
print("Schwelle:         ", versand_frei_grenze)
print("versand_gratis:   ", versand_gratis)
