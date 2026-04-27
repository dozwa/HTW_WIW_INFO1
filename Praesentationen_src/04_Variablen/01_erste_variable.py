"""
04 -- Variablen | Demo 1: Werte in Variablen speichern

Zeigt:
- Variable definieren mit name = wert
- Variablen in Texten einsetzen (f-string)
- Verschiedene Datentypen: str, float, int
"""

# Variablen mit Veggie-Soles-Stammdaten
produktname = "Eco-Sneaker"
preis = 89.95
bestand = 42

# Werte ueber den Variablennamen ansprechen
print(f"Produkt:  {produktname}")
print(f"Preis:    {preis} EUR")
print(f"Bestand:  {bestand} Paar")

print()  # Leerzeile zur Trennung

# Mehrere Stamm-Kund:innen
kunde_1 = "Anna Mueller"
kunde_2 = "Max Schmidt"

print(f"Stammkund:innen: {kunde_1}, {kunde_2}")
