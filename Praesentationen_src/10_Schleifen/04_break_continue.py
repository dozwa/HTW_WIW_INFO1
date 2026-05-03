"""
10 -- Schleifen | Demo 4: break und continue

Zeigt:
- break: Schleife komplett beenden (z. B. erstes Treffer-Element)
- continue: aktuellen Durchlauf abbrechen, weiter mit dem naechsten
- Praktische Filter-Logik

Story: Veggie Soles -- Suche im Sortiment, Filterung der Premium-Schuhe.
"""


sortiment = ["Eco-Sneaker", "Hemp-High", "Bambus-Boot", "Sandale"]
preise    = [89.95, 109.00, 135.50, 49.90]

# 1) break -- erstes Modell ueber 100 EUR finden, dann anhalten
print("Erstes Premium-Modell (>100 EUR):")
for name, preis in zip(sortiment, preise):
    if preis > 100:
        print(f"  Treffer: {name} ({preis:.2f} EUR)")
        break

# 2) continue -- Modelle <= 50 EUR ueberspringen
print("\nModelle ueber 50 EUR:")
for name, preis in zip(sortiment, preise):
    if preis <= 50:
        continue
    print(f"  - {name}: {preis:.2f} EUR")

# Faustregel:
# - "ich brauche das ERSTE, das passt" -> break
# - "ich will nur bestimmte Eintraege bearbeiten" -> continue
