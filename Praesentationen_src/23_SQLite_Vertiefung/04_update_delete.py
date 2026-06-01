"""Daten aendern (UPDATE) und loeschen (DELETE) -- beides DESTRUKTIV.
Wichtigste Regel: IMMER eine WHERE-Klausel. Ohne WHERE trifft es ALLE Zeilen.

Best Practice: erst mit SELECT pruefen, was die WHERE-Bedingung trifft, dann erst
UPDATE/DELETE ausfuehren.
"""
import sqlite3


def shop_db():
    conn = sqlite3.connect(":memory:")
    conn.execute("""CREATE TABLE produkt (
        produkt_id INTEGER PRIMARY KEY, name TEXT, preis REAL, kategorie TEXT, aktiv INTEGER)""")
    conn.executemany("INSERT INTO produkt (name, preis, kategorie, aktiv) VALUES (?, ?, ?, ?)", [
        ("Eco-Sneaker", 89.95, "Low-Cut", 1), ("Hemp-High", 109.00, "High-Cut", 1),
        ("Bambus-Boot", 135.50, "Boot", 1),   ("Kork-Slip", 74.90, "Low-Cut", 1),
        ("Pilz-Pump", 119.00, None, 1),        # Kategorie noch offen
        ("Algae-Runner", 99.95, "Low-Cut", 0),  # Auslaufmodell -> wird geloescht
    ])
    conn.commit()
    return conn


conn = shop_db()


def zeig(titel, sql="SELECT name, preis, kategorie, aktiv FROM produkt", params=()):
    print(f"\n{titel}")
    for zeile in conn.execute(sql, params).fetchall():
        print("  ", zeile)


zeig("Ausgangslage:")

# --- UPDATE: einzelnen Datensatz aendern ---------------------------------------
# Best Practice: erst SELECT -- was wuerde getroffen?
zeig("Vorab-Check (was trifft die WHERE-Bedingung?):",
     "SELECT name, preis FROM produkt WHERE name = ?", ("Kork-Slip",))
conn.execute("UPDATE produkt SET preis = ? WHERE name = ?", (79.90, "Kork-Slip"))
conn.commit()
zeig("Nach Preisanpassung Kork-Slip:")

# Mehrere Spalten auf einmal -- hier: fehlende Kategorie nachtragen
conn.execute("UPDATE produkt SET kategorie = ? WHERE kategorie IS NULL", ("Low-Cut",))
conn.commit()
zeig("Nach Nachtragen der Kategorie (Pilz-Pump):")

# --- DELETE: Datensatz loeschen ------------------------------------------------
zeig("Vorab-Check (was wuerde geloescht?):", "SELECT name FROM produkt WHERE aktiv = 0")
geloescht = conn.execute("DELETE FROM produkt WHERE aktiv = 0").rowcount
conn.commit()
print(f"\n{geloescht} Zeile(n) geloescht.")
zeig("Bestand nach dem Loeschen:")

conn.close()

# --- Variante zum Live-Einkommentieren: das WHERE WEGLASSEN -- bitte NICHT! -----
# conn.execute("UPDATE produkt SET preis = 0")    # setzt ALLE Preise auf 0
# conn.execute("DELETE FROM produkt")             # leert die GANZE Tabelle
# # Beides ist nicht rueckgaengig zu machen (ausser man hat ein Backup).
