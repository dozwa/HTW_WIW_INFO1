"""
06 -- Komplexe Datentypen | Demo 2: Listen -- Operationen

Zeigt:
- append() -- hinten anfuegen
- insert() -- an Position einfuegen
- remove() -- nach Wert entfernen
- pop() -- nach Index entfernen, gibt Wert zurueck
- sort() / reverse() -- in-place sortieren
- + und * fuer Listen
"""

warenkorb = ["Eco-Sneaker", "Hemp-High"]
print(f"Start: {warenkorb}")

# Hinten anfuegen
warenkorb.append("Bambus-Boot")
print(f"Nach append: {warenkorb}")

# An Position einfuegen
warenkorb.insert(1, "Cork-Slipper")
print(f"Nach insert(1, ...): {warenkorb}")

# Nach Wert entfernen
warenkorb.remove("Hemp-High")
print(f"Nach remove('Hemp-High'): {warenkorb}")

# Nach Index entfernen -- pop liefert den entfernten Wert zurueck
weg = warenkorb.pop(0)
print(f"Nach pop(0): {warenkorb}, entfernt: '{weg}'")

# Element ueberschreiben
warenkorb[0] = "Jute-Runner"
print(f"Nach Ueberschreiben [0]: {warenkorb}")

print()
# Sortieren -- alphabetisch
sortiert_kopie = sorted(warenkorb)        # neue Liste, Original bleibt
print(f"sorted() (neue Liste): {sortiert_kopie}")
print(f"Original unveraendert: {warenkorb}")

warenkorb.sort()                            # in-place
print(f".sort() (in-place):    {warenkorb}")

print()
# Listen verbinden mit +
top_drei = ["Eco-Sneaker", "Hemp-High", "Bambus-Boot"]
neu = ["Cork-Slipper", "Jute-Runner"]
sortiment = top_drei + neu
print(f"Verbundene Liste: {sortiment}")

# Vervielfaeltigen mit *
trenner = ["---"] * 5
print(f"Trenner-Liste: {trenner}")
