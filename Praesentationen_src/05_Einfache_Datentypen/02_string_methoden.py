"""
05 -- Einfache Datentypen | Demo 2: String-Methoden

Zeigt:
- .upper() / .lower() / .title()
- .strip() -- Leerzeichen weg
- .replace() -- ersetzen
- .startswith() / .endswith()
- Praxisbeispiel: E-Mail-Adresse aus Vor-/Nachname bauen
"""

produkt = "Eco-Sneaker"

# Gross-/Kleinschreibung
print(f"upper:  {produkt.upper()}")        # ECO-SNEAKER
print(f"lower:  {produkt.lower()}")        # eco-sneaker
print(f"title:  {produkt.title()}")        # Eco-Sneaker (jedes Wort gross)

print()
# Leerzeichen entfernen
roher_input = "  Anna Mueller  "
print(f"Eingabe roh:    '{roher_input}'")
print(f"strip:          '{roher_input.strip()}'")

print()
# Ersetzen
print(produkt.replace("-", " "))           # "Eco Sneaker"
print(produkt.replace("Sneaker", "Boot"))  # "Eco-Boot"

print()
# Pruefen ob ein Praefix/Suffix vorliegt -- liefert bool
print(produkt.startswith("Eco"))           # True
print(produkt.endswith(".pdf"))            # False

print()
# Praxis: E-Mail-Adresse aus Vor-/Nachname konstruieren
vorname = "Anna"
nachname = "Mueller"
domain = "example.de"

email = f"{vorname.lower()}.{nachname.lower()}@{domain}"
print(f"E-Mail: {email}")
