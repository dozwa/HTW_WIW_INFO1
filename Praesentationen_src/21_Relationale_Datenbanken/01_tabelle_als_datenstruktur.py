"""Eine relationale Tabelle, mit Python-Mitteln nachgebaut.

Zeigt: Tabelle = Liste von Zeilen, Zeile = Dictionary {Spalte: Wert}.
       Primaerschluessel = eindeutig + nie None.  NULL = Python None.
Alles Konzepte aus den Notebooks 06/07/09/10 -- nichts Neues, nur neu zusammengesetzt.
"""

# Eine "Tabelle" kunde: jede Zeile ein Dict mit denselben Spalten.
kunde = [
    {"kunde_id": 1, "vorname": "Anna", "nachname": "Mueller", "email": "anna@example.de"},
    {"kunde_id": 2, "vorname": "Max",  "nachname": "Schmidt", "email": "max@example.de"},
    {"kunde_id": 3, "vorname": "Lena", "nachname": "Weber",   "email": None},  # email unbekannt -> NULL
]

print("Tabelle kunde:")
for zeile in kunde:
    print("  ", zeile)


def primaerschluessel_ok(tabelle, spalte):
    """Prueft, was ein DBMS automatisch garantieren wuerde: eindeutig und nicht NULL."""
    werte = [z[spalte] for z in tabelle]
    if None in werte:
        return False, f"Spalte '{spalte}' enthaelt NULL -- als PK verboten."
    if len(werte) != len(set(werte)):
        return False, f"Spalte '{spalte}' hat Dubletten -- als PK verboten."
    return True, f"Spalte '{spalte}' taugt als Primaerschluessel."


print()
print(primaerschluessel_ok(kunde, "kunde_id")[1])     # ok
print(primaerschluessel_ok(kunde, "nachname")[1])      # ok hier -- aber waere bei zwei "Weber" hin

# NULL ist NICHT 0 und NICHT "" -- und Vergleiche mit == liefern bei echten DBs nichts:
lena = kunde[2]
print()
print("lena['email'] ist None? ->", lena["email"] is None)        # so prueft man in Python ("IS NULL")
print("lena['email'] == '' ?   ->", lena["email"] == "")          # False -- NULL != leerer String

# --- Variante zum Live-Einkommentieren: was ein DBMS ablehnen wuerde -----------
# kunde.append({"kunde_id": 1, "vorname": "Tom", "nachname": "Fischer", "email": "tom@example.de"})
# print(primaerschluessel_ok(kunde, "kunde_id")[1])   # jetzt: Dublette bei kunde_id!
