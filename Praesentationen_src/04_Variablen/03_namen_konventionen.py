"""
04 -- Variablen | Demo 3: Variablennamen -- erlaubt, verboten, konventionell

Zeigt:
- snake_case fuer normale Variablen
- GROSSBUCHSTABEN fuer Konstanten
- Aussagekraeftige Namen statt Kuerzel
- Verbotene Namen (auskommentiert -- waeren SyntaxError)
"""

# Konventionell: snake_case fuer Variablen
produkt_name = "Eco-Sneaker"
auf_lager = True
anzahl_bewertungen = 47

# Konventionell: GROSSBUCHSTABEN fuer Konstanten (aendern sich nicht)
MWST_SATZ = 0.19
VERSANDPAUSCHALE = 4.95
WAEHRUNG = "EUR"

# Aussagekraeftig statt kryptisch
# schlecht (auskommentiert)
# x = 89.95
# n = "Eco-Sneaker"
# k = "anna@example.de"

# gut
preis_eco_sneaker = 89.95
produkt_titel = "Eco-Sneaker"
kunden_email = "anna@example.de"

print(f"{produkt_titel}: {preis_eco_sneaker} {WAEHRUNG}")
print(f"MwSt-Satz: {MWST_SATZ * 100:.0f}%")
print(f"Kunden-E-Mail: {kunden_email}")

# ============================================================
# Folgende Zeilen wuerden SyntaxError ausloesen.
# Zum Vorfuehren bitte einkommentieren -- fuehren zu Fehlern!
# ============================================================

# 1produkt = "Eco-Sneaker"     # Variable darf nicht mit Zahl beginnen
# produkt-name = "Eco-Sneaker" # Bindestrich = Minus, kein gueltiger Name
# class = "sneaker"            # 'class' ist reserviert (Python-Schluesselwort)
# mein produkt = "Eco-Sneaker" # Leerzeichen nicht erlaubt
