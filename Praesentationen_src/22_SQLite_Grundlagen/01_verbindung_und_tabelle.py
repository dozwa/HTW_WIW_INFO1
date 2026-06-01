"""SQLite-Einstieg: Verbindung, Cursor, CREATE TABLE, commit, close.

Wir nutzen eine In-Memory-Datenbank (':memory:') -- die existiert nur waehrend
das Programm laeuft, ideal zum Vorfuehren. Mit einem Dateinamen statt ':memory:'
(z. B. 'veggie_soles.db') waere die DB dauerhaft auf der Platte.
"""
import sqlite3

print(f"SQLite-Version: {sqlite3.sqlite_version}")

# 1) Verbindung herstellen (Datei wuerde hier angelegt; ':memory:' = nur im RAM)
conn = sqlite3.connect(":memory:")

# 2) Cursor holen -- das Werkzeug, mit dem wir SQL-Befehle abschicken
cursor = conn.cursor()

# 3) SQL ausfuehren: eine Tabelle fuer die Veggie-Soles-Produkte anlegen.
#    SQLite kennt nur fuenf Datentypen: INTEGER, REAL, TEXT, BLOB, NULL.
cursor.execute("""
    CREATE TABLE produkt (
        produkt_id INTEGER PRIMARY KEY,   -- Primaerschluessel, zaehlt automatisch hoch
        name       TEXT NOT NULL,         -- Pflichtfeld
        preis      REAL,                  -- Geldbetrag
        kategorie  TEXT
    )
""")

# 4) Aenderungen sichern
conn.commit()
print("Tabelle 'produkt' angelegt.")

# Kontrolle: welche Tabellen gibt es? (steht im Systemkatalog sqlite_master)
cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
print("Tabellen in der Datenbank:", cursor.fetchall())

# 5) Verbindung schliessen -- gibt Ressourcen frei
conn.close()
print("Verbindung geschlossen.")

# --- Variante zum Live-Einkommentieren: dieselbe Tabelle nochmal anlegen -------
# conn = sqlite3.connect(":memory:")
# conn.execute("CREATE TABLE produkt (produkt_id INTEGER PRIMARY KEY)")
# conn.execute("CREATE TABLE produkt (produkt_id INTEGER PRIMARY KEY)")  # -> OperationalError: table produkt already exists
# # Abhilfe: CREATE TABLE IF NOT EXISTS produkt (...)
