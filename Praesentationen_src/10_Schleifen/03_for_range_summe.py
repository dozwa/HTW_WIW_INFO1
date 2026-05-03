"""
10 -- Schleifen | Demo 3: range() und Sammelvariable

Zeigt:
- range(stop), range(start, stop), range(start, stop, step)
- Klassisches Sammel-Muster: Summe / Mittelwert
- "Obere Grenze ist exklusiv" als typische Falle

Story: Veggie Soles -- Tagesumsatz aus Einzelpreisen.
"""


# 1) range Grundformen
print("range(5):", list(range(5)))            # 0..4
print("range(1,6):", list(range(1, 6)))       # 1..5
print("range(0,21,5):", list(range(0, 21, 5)))  # 0,5,10,15,20

# 2) Sammelvariable: Tagesumsatz aufsummieren
preise = [89.95, 109.00, 135.50, 89.95, 109.00]
gesamt = 0.0
for p in preise:
    gesamt = gesamt + p

mittel = gesamt / len(preise)
print(f"\nGesamtumsatz: {gesamt:.2f} EUR")
print(f"Durchschnittspreis: {mittel:.2f} EUR")

# 3) range + Liste kombiniert: Index UND Wert
for i in range(len(preise)):
    print(f"Position {i}: {preise[i]:.2f} EUR")

# Variation: idiomatischer ginge das mit enumerate (kommt in Vertiefung)
# for i, p in enumerate(preise): ...
