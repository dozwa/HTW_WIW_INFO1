"""
12 -- File I/O | Demo 3: with-Block fuer sicheres Schliessen

Zeigt:
- with open(...) as f: ... -- close() automatisch
- Auch bei Exception im Block wird die Datei geschlossen
- Der idiomatische Stil in Python

Story: Veggie Soles -- mehrere Tagesreports schreiben und lesen.
"""

import os


pfad = "tagesreport_demo3.txt"

# 1) Schreiben mit with -- close() braucht's nicht
with open(pfad, "w") as f:
    f.write("Veggie Soles\n")
    f.write("=================\n")
    for produkt, preis in [("Eco-Sneaker", 89.95), ("Hemp-High", 109.00)]:
        f.write(f"{produkt}: {preis:.2f} EUR\n")

print("Datei geschrieben.")

# 2) Lesen mit with
with open(pfad, "r") as f:
    print("--- Inhalt ---")
    print(f.read())

# 3) Selbst nach Exception waere die Datei zu -- Demo:
try:
    with open(pfad, "r") as f:
        text = f.read()
        raise ValueError("Beispiel-Fehler im with-Block")
except ValueError as e:
    print(f"Exception abgefangen: {e}")
    # 'f' ist hier garantiert geschlossen, obwohl der Block mit Fehler endete

# Aufraeumen
os.remove(pfad)
print("Aufraeumen erledigt.")

# Faustregel:
# In allem produktiven Code IMMER with verwenden.
# open + close ist nur Lehr-Schritt -- in der Klausur reicht with.
