"""
05 -- Einfache Datentypen | Demo 4: Boolean -- True/False

Zeigt:
- Bool-Werte True/False
- Vergleichsoperatoren als Bool-Quelle
- Logische Verknuepfungen and / or / not
- 'in'-Operator fuer Strings
- Praxis: Versand-frei-Bedingung pruefen
"""

# Direkte Bool-Werte
auf_lager = True
ausverkauft = False
print(f"auf_lager:    {auf_lager}")
print(f"ausverkauft:  {ausverkauft}")

print()
# Bool aus Vergleichen
preis = 89.95
print(f"preis > 100   → {preis > 100}")        # False
print(f"preis < 100   → {preis < 100}")        # True
print(f"preis == 89.95 → {preis == 89.95}")    # True

print()
# Logische Verknuepfung
bestand = 5
versand_frei_grenze = 100
warenwert = 105

versand_gratis = warenwert >= versand_frei_grenze
verfuegbar = bestand > 0

print(f"versand_gratis: {versand_gratis}")
print(f"verfuegbar:     {verfuegbar}")
print(f"bestellbar:     {versand_gratis and verfuegbar}")

# Mehrere Bedingungen kombinieren
ist_premium_kunde = True
hat_gutschein = False
bekommt_rabatt = ist_premium_kunde or hat_gutschein
print(f"bekommt_rabatt: {bekommt_rabatt}")

print()
# 'in' funktioniert auf Strings (und auf Listen, kommt in NB 06)
produkt = "Eco-Sneaker"
print(f"'Eco' in '{produkt}': {'Eco' in produkt}")        # True
print(f"'Hemp' in '{produkt}': {'Hemp' in produkt}")      # False

# 'not' kehrt einen Bool um
print(f"not auf_lager: {not auf_lager}")                  # False
