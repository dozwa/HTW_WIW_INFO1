"""
11 -- Fehlerbehandlung | Demo 3: try / except / finally

Zeigt:
- finally laeuft IMMER -- mit oder ohne Fehler
- Klassischer Einsatz: Statusmeldung am Ende
- Reihenfolge der Bloecke: try -> except -> (else) -> finally

Story: Veggie Soles -- Bestellabschluss mit "Pruefung beendet".
"""


def buche_bestellung(eingabe):
    print(f"--- Bestellannahme: {eingabe!r} ---")
    try:
        anzahl = int(eingabe)
        if anzahl <= 0:
            raise ValueError("Anzahl muss positiv sein.")
        print(f"Buche {anzahl} Stueck.")
    except ValueError as e:
        print(f"Fehler: {e}")
    finally:
        print("Pruefung abgeschlossen.\n")


buche_bestellung("3")        # erfolgreich -> finally laeuft
buche_bestellung("abc")      # ValueError  -> except + finally laufen
buche_bestellung("-2")       # selbst geworfener ValueError -> except + finally

# Beobachtung beim Vorfuehren:
# - "Pruefung abgeschlossen." erscheint in allen drei Faellen.
# - finally eignet sich genau fuer Aufraeum-Aktionen, die NIE ausfallen duerfen
#   (Datei schliessen, Verbindung beenden, Status-Log).
