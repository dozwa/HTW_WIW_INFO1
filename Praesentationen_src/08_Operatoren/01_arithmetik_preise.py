"""
08 -- Operatoren | Demo 1: Arithmetik fuer Preise

Zeigt:
- + - * / // % **
- Brutto/Netto, Mengenrabatt, Stueckpreis
- // und % gemeinsam fuer "Kartonierung"

Story: Veggie Soles -- Preisberechnung im Shop.
"""


netto = 89.95            # Eco-Sneaker, vor MwSt
mwst  = 0.19             # 19 Prozent

# Addition / Multiplikation
brutto = netto * (1 + mwst)
print(f"Eco-Sneaker netto:  {netto:.2f} EUR")
print(f"Eco-Sneaker brutto: {brutto:.2f} EUR")

# Subtraktion -- Rabatt
rabatt = 10.00
preis_mit_rabatt = brutto - rabatt
print(f"Mit 10 EUR Rabatt:  {preis_mit_rabatt:.2f} EUR")

# Division -- Stueckpreis pro Paar (1 Paar = 2 Schuhe)
stueck = 2
print(f"Pro Schuh ungefaehr: {brutto / stueck:.2f} EUR")

# // und % -- Kartonierung
artikel_pro_karton = 12
bestellte_artikel  = 47
volle_kartons   = bestellte_artikel // artikel_pro_karton
einzelartikel   = bestellte_artikel % artikel_pro_karton
print(f"{bestellte_artikel} Artikel = {volle_kartons} Kartons + {einzelartikel} einzeln")

# ** -- Potenz (selten in Preislogik, aber gut zu kennen)
print(f"2^10 = {2 ** 10}")

# Variation zum Vorfuehren:
# print(7 / 0)   # ZeroDivisionError -- Fehlerbehandlung erst NB 11
