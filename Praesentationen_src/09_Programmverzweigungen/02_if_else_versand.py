"""
09 -- Verzweigungen | Demo 2: if/else fuer Versandkosten

Zeigt:
- Genau einer der beiden Bloecke laeuft
- Veggie-Soles-Logik: ab 50 EUR versandfrei
- else laeuft, wenn die if-Bedingung NICHT erfuellt ist

Story: Veggie Soles -- Versandkostenregel.
"""


bestellsumme = 62.50
print(f"Bestellsumme: {bestellsumme:.2f} EUR")

if bestellsumme >= 50:
    print(">>> versandfrei -- Sie sparen die Pauschale!")
else:
    print(">>> Versand 4.95 EUR")

# Variation zum Vorfuehren:
# bestellsumme = 19.90  # unter 50 -> der else-Block laeuft

# Faustregel: jede if-Bedingung hat ggf. einen "andernfalls"-Pfad.
# Wenn der else-Block nichts zu tun hat, weglassen -- Code wird kuerzer.
