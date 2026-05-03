"""
09 -- Verzweigungen | Demo 4: Bedingungen mit and / or / not

Zeigt:
- Bedingungen aus NB 08 in if-Statements einsetzen
- Klammern fuer Lesbarkeit
- VIP-/Standard-/Normal-Versand-Logik

Story: Veggie Soles -- Versandklassen je nach Status und Summe.
"""


def versandhinweis(bestellsumme, stammkunde, premium, storniert):
    if storniert:
        return "Bestellung storniert -- kein Versand."

    if stammkunde and bestellsumme >= 50:
        return "VIP-Versand (frei + Geschenk)."

    if (bestellsumme >= 50) or premium:
        return "Standard-Versand kostenlos."

    return "Versand 4.95 EUR."


# Vier Beispielfaelle
print(versandhinweis(89.95, stammkunde=True,  premium=False, storniert=False))
print(versandhinweis(19.90, stammkunde=False, premium=True,  storniert=False))
print(versandhinweis(19.90, stammkunde=False, premium=False, storniert=False))
print(versandhinweis(89.95, stammkunde=True,  premium=False, storniert=True))

# Beobachtung beim Vorfuehren:
# - Mehrere if-Statements, ABER jedes mit "return": nach erstem Match endet die Funktion.
# - Das ersetzt die Verschachtelung -- bleibt gut lesbar.
# - Klammern um (bestellsumme >= 50) sind nicht noetig, machen die Lesart aber leichter.
