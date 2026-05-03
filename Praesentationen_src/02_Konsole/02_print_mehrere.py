"""
02 -- Konsole | Demo 2: Mehrere Werte und Leerzeilen

Zeigt:
- Mehrere Werte in einem print, kommagetrennt -> Leerzeichen dazwischen
- print("") oder print() erzeugt eine leere Zeile
- Strukturierte Listenausgaben fuer den Tagesreport

Story: Veggie Soles -- Tagesreport.
"""


# Komma-getrennte Werte: Python setzt jeweils ein Leerzeichen dazwischen.
print("Eco-Sneaker", "89.95", "EUR")
print("Hemp-High", "109.00", "EUR")
print("Bambus-Boot", "135.50", "EUR")

# Leerzeile zur Trennung.
print("")

# Strukturierte Mini-Tabelle als Ausgabe:
print("====== Veggie Soles -- Tagesreport ======")
print("Produkt", "       ", "Preis")
print("Eco-Sneaker", "    ", "89.95 EUR")
print("Hemp-High", "      ", "109.00 EUR")
print("Bambus-Boot", "    ", "135.50 EUR")
print("=========================================")

# Variation zum Vorfuehren (auskommentieren bzw. einkommentieren):
# print()                         # gleiches wie print("")
# print("a", "b", "c", sep="--")  # andere Trennzeichen -- spaeter im Kurs.
