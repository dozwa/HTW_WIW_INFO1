"""
08 -- Operatoren | Demo 3: Logische Operatoren

Zeigt:
- and / or / not
- Bedingungen kombinieren
- Klammern fuer Lesbarkeit

Story: Veggie Soles -- Versandkosten und Rabattlogik.
"""


bestellsumme   = 62.50
stammkunde     = True
gutschein      = False
storniert      = False

# AND -- beide Bedingungen muessen wahr sein
versandfrei = (bestellsumme >= 50) and (not storniert)
print(f"versandfrei (>=50 EUR und nicht storniert): {versandfrei}")

# OR -- mindestens eine Bedingung muss wahr sein
darf_rabatt_bekommen = stammkunde or gutschein
print(f"darf Rabatt (Stammkunde oder Gutschein):    {darf_rabatt_bekommen}")

# NOT -- Wert kippen
nicht_storniert = not storniert
print(f"nicht storniert: {nicht_storniert}")

# Kombiniert -- mit Klammern fuer Lesbarkeit
spezial_rabatt = (bestellsumme >= 100) or (stammkunde and gutschein)
print(f"Spezial-Rabatt: {spezial_rabatt}")

# Anti-Pattern: ohne Klammern wirkt's mehrdeutig
# Python wertet "and" vor "or" aus, aber wer liest das schon spontan?
unklar = bestellsumme >= 50 and stammkunde or gutschein
klar   = ((bestellsumme >= 50) and stammkunde) or gutschein
print(f"unklar == klar?  {unklar == klar}")
