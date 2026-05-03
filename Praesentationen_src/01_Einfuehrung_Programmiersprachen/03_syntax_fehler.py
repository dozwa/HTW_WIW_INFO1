"""
01 -- Einfuehrung | Demo 3: Syntaxfehler erkennen

Zeigt:
- Wie Python einen Syntaxfehler meldet
- Wie ein Tippfehler den ganzen Lauf verhindert
- Den Unterschied zu logischen Fehlern (Code laeuft, ist aber falsch)

Hinweis fuer den Lecturer: jeweils eine der unten auskommentierten Zeilen
einkommentieren und das Skript starten -- Python zeigt die Fehlermeldung.

Story: Veggie Soles -- Begruessung im Shop.
"""


# 1) Korrekt:
print("Willkommen bei Veggie Soles!")


# 2) Tippfehler -- Print mit grossem P. Aktivieren zum Vorfuehren:
# Print("Willkommen bei Veggie Soles!")
# -> NameError: name 'Print' is not defined


# 3) Klammer fehlt. Aktivieren zum Vorfuehren:
# print "Willkommen bei Veggie Soles!"
# -> SyntaxError: Missing parentheses in call to 'print'


# 4) Anfuehrungszeichen nicht geschlossen. Aktivieren zum Vorfuehren:
# print("Willkommen bei Veggie Soles!)
# -> SyntaxError: unterminated string literal


# 5) Logischer Fehler -- syntaktisch korrekt, aber falscher Preis:
print("Eco-Sneaker kostet 98.95 EUR")
# Programm laeuft. Python merkt nichts. Aber der Preis ist falsch
# (korrekt waere 89.95 EUR). Solche Fehler findet nur sorgfaeltiges Pruefen.
