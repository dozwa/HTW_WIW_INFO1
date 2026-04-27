"""
05 -- Einfache Datentypen | Demo 3: Integer und Float

Zeigt:
- int (ganze Zahlen) vs. float (Kommazahlen)
- Operatoren: + - * / // % **
- Float-Ungenauigkeit (klassische Falle)
- Formatierung mit f-string :.2f
"""

# Integer fuer Stueckzahlen
bestand = 42
verkauft = 7
neuer_bestand = bestand - verkauft
print(f"Bestand vorher: {bestand}, verkauft: {verkauft}, jetzt: {neuer_bestand}")

# Float fuer Preise
preis = 89.95
mwst_satz = 0.19
brutto = preis * (1 + mwst_satz)
print(f"Netto:  {preis:.2f} EUR")
print(f"Brutto: {brutto:.2f} EUR")

print()
# Division: / liefert IMMER float, // liefert int (abrundend)
gesamtumsatz = 1000.00
preis_pro_paar = 89.95

paare_kontinuierlich = gesamtumsatz / preis_pro_paar    # 11.11...
paare_ganz = gesamtumsatz // preis_pro_paar             # 11.0 (abgerundet, aber float)

print(f"Mathematisch:    {paare_kontinuierlich:.2f} Paare")
print(f"Ganzzahl-Division: {int(paare_ganz)} Paare")

print()
# Modulo (Rest) -- praktisch fuer Verpackungs-Logik
total_paare = 100
karton_groesse = 12
volle_kartons = total_paare // karton_groesse
einzelpaare = total_paare % karton_groesse

print(f"{total_paare} Paare = {volle_kartons} Karton(s) + {einzelpaare} einzelne")

print()
# KLASSISCHE FALLE: Float ist nicht exakt
print("0.1 + 0.2 =", 0.1 + 0.2)      # 0.30000000000000004 (!)
print("Vorsicht bei == Vergleichen mit Floats.")
