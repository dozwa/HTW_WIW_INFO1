"""Saubere Patterns: with-Statement (commit/rollback automatisch), Fehlerbehandlung
mit try/except, und Ergebnisse als benannte Zeilen (sqlite3.Row).

Wir kapseln die Datenbankzugriffe in kleinen Funktionen -- so wie man es in
echtem Code macht.
"""
import sqlite3

DB = ":memory:"   # in echt: 'veggie_soles.db'

# WICHTIG fuer dieses Demo: ':memory:' lebt nur waehrend EINER Verbindung.
# Damit alle Funktionen dieselbe DB sehen, halten wir EINE Verbindung offen.
_conn = sqlite3.connect(DB)
_conn.row_factory = sqlite3.Row          # Zeilen wie ein Dict ansprechbar: zeile["name"]

with _conn:                              # with -> am Ende automatisch commit (oder rollback bei Fehler)
    _conn.execute("""
        CREATE TABLE produkt (
            produkt_id INTEGER PRIMARY KEY,
            name  TEXT NOT NULL UNIQUE,   -- UNIQUE: kein Produktname darf doppelt sein
            preis REAL
        )
    """)


def produkt_hinzufuegen(name, preis):
    """Fuegt ein Produkt hinzu. Faengt den Fall ab, dass der Name schon existiert."""
    try:
        with _conn:
            _conn.execute("INSERT INTO produkt (name, preis) VALUES (?, ?)", (name, preis))
        print(f"OK: '{name}' hinzugefuegt.")
    except sqlite3.IntegrityError:
        print(f"Abgelehnt: '{name}' gibt es schon (UNIQUE-Verletzung).")
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")


def produkt_suchen(teiltext):
    """Sucht Produkte, deren Name den Teiltext enthaelt."""
    with _conn:
        zeilen = _conn.execute(
            "SELECT name, preis FROM produkt WHERE name LIKE ?", (f"%{teiltext}%",)
        ).fetchall()
    if zeilen:
        for z in zeilen:
            print(f"  {z['name']:14s} {z['preis']:7.2f} EUR")   # Zugriff per Spaltenname
    else:
        print(f"  (kein Produkt mit '{teiltext}' im Namen)")


# --- ausprobieren ---
produkt_hinzufuegen("Eco-Sneaker", 89.95)
produkt_hinzufuegen("Hemp-High", 109.00)
produkt_hinzufuegen("Eco-Sneaker", 79.95)     # Dublette -> wird abgelehnt
produkt_hinzufuegen("Bambus-Boot", 135.50)

print("\nSuche nach 'Eco':")
produkt_suchen("Eco")
print("Suche nach 'Boot':")
produkt_suchen("Boot")
print("Suche nach 'XYZ':")
produkt_suchen("XYZ")

_conn.close()
