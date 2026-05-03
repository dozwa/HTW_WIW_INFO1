"""
11 -- Fehlerbehandlung | Demo 4: robuste Eingabeschleife

Zeigt:
- while True + try/except + break
- Bei jeder ungueltigen Eingabe nochmal fragen
- Erst die erste GUELTIGE Eingabe verlaesst die Schleife

Story: Veggie Soles -- Stueckzahl beim Kunden abfragen.
Hinweis fuer den Lecturer: live mit input() vorfuehren. Hier eine
nicht-interaktive Variante, die eine Liste simulierter Eingaben durchgeht.
"""


simulierte_eingaben = ["abc", "0", "-3", "2"]


def naechste_eingabe(quelle):
    """Liefert eine Eingabe -- entweder von input() oder aus der Liste."""
    if quelle:
        return quelle.pop(0)
    return input("Stueckzahl? ")


def hole_anzahl():
    while True:
        roh = naechste_eingabe(simulierte_eingaben)
        print(f"-> Versuch: {roh!r}")
        try:
            anzahl = int(roh)
            if anzahl <= 0:
                print("   ungueltig: Anzahl muss positiv sein.")
                continue
            return anzahl
        except ValueError:
            print("   ungueltig: bitte eine ganze Zahl.")


anzahl = hole_anzahl()
print(f"\nOK: {anzahl} Stueck gebucht.")

# Beobachtung beim Vorfuehren:
# - Drei Fehleingaben werden nacheinander abgewiesen.
# - Erst "2" verlaesst die Schleife mit return.
# - In der echten Welt ersetzen wir simulierte_eingaben durch input(...).
