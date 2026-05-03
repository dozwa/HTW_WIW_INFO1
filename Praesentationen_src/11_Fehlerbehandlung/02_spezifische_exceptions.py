"""
11 -- Fehlerbehandlung | Demo 2: spezifische Exception-Typen

Zeigt:
- Jeweils ein except-Block pro Fehlertyp
- ValueError, ZeroDivisionError, KeyError unterschieden
- "as e" -- Fehlermeldung lesen

Story: Veggie Soles -- Bestellung pruefen.
"""


preise = {
    "Eco-Sneaker": 89.95,
    "Hemp-High":   109.00,
    "Bambus-Boot": 135.50,
}


def stueckpreis(modell, anzahl_text):
    try:
        anzahl = int(anzahl_text)
        einzelpreis = preise[modell]
        return einzelpreis / anzahl    # Stueckpreis pro Schuh aus dem Paar etc.
    except ValueError as e:
        return f"Eingabe ist keine Zahl ({e})."
    except ZeroDivisionError:
        return "Anzahl darf nicht 0 sein."
    except KeyError:
        return f"Modell {modell!r} ist nicht im Sortiment."


# Vier Faelle vorfuehren:
print(stueckpreis("Eco-Sneaker", "2"))     # ok
print(stueckpreis("Eco-Sneaker", "abc"))   # ValueError
print(stueckpreis("Eco-Sneaker", "0"))     # ZeroDivisionError
print(stueckpreis("Sandale",     "1"))     # KeyError

# Beobachtung beim Vorfuehren:
# - Reihenfolge der except-Bloecke ist egal, solange die Typen disjunkt sind.
# - "as e" liefert die Original-Fehlermeldung, nuetzlich zum Debuggen.
