"""
10 -- Schleifen | Demo 5: for ueber Dictionary + Comprehensions

Zeigt:
- for k, v in d.items(): -- elegante Iteration
- Sammeln in einem neuen Dict / einer neuen Liste
- List Comprehension als Kurzform fuer Filter+Transformation

Story: Veggie Soles -- Warenkorb auswerten und Brutto-Preisliste bauen.
"""


warenkorb = {
    "Eco-Sneaker": 1,
    "Hemp-High":   2,
    "Bambus-Boot": 1,
}

preise = {
    "Eco-Sneaker": 89.95,
    "Hemp-High":   109.00,
    "Bambus-Boot": 135.50,
}

# Dict iterieren mit items()
gesamt = 0.0
for produkt, anzahl in warenkorb.items():
    teilsumme = preise[produkt] * anzahl
    gesamt = gesamt + teilsumme
    print(f"{produkt:13s} x {anzahl}  ->  {teilsumme:7.2f} EUR")

print(f"{'GESAMT':17s}  ->  {gesamt:7.2f} EUR")

# List Comprehension: nur Produkte ueber 100 EUR auflisten
premium = [name for name, p in preise.items() if p > 100]
print(f"\nPremium-Modelle: {premium}")

# Brutto-Preise als neue Liste mit Comprehension
mwst = 0.19
brutto = [round(p * (1 + mwst), 2) for p in preise.values()]
print(f"Brutto-Liste:    {brutto}")
