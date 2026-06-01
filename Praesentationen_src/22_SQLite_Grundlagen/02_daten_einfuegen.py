"""Daten einfuegen: INSERT mit festen Werten, sicher mit Platzhaltern (?), und
viele Zeilen auf einmal mit executemany().

Wichtigste Regel: Werte NIE per String-Bastelei in den SQL-Befehl kleben --
immer ? als Platzhalter. Das schuetzt vor SQL-Injection (und vor Tippfehlern).
"""
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE produkt (
        produkt_id INTEGER PRIMARY KEY,
        name       TEXT NOT NULL,
        preis      REAL,
        kategorie  TEXT
    )
""")

# 1) Ein Datensatz mit festen Werten direkt im Befehl
cursor.execute("""
    INSERT INTO produkt (name, preis, kategorie)
    VALUES ('Eco-Sneaker', 89.95, 'Low-Cut')
""")
conn.commit()
print("Eco-Sneaker eingefuegt, neue ID:", cursor.lastrowid)

# 2) SICHER: Werte als Platzhalter (?) -- Python setzt sie korrekt ein
neues_produkt = ("Hemp-High", 109.00, "High-Cut")
cursor.execute("INSERT INTO produkt (name, preis, kategorie) VALUES (?, ?, ?)", neues_produkt)
conn.commit()
print(f"'{neues_produkt[0]}' sicher eingefuegt, neue ID:", cursor.lastrowid)

# 3) Viele Datensaetze auf einmal: executemany() mit einer Liste von Tupeln
weitere = [
    ("Bambus-Boot", 135.50, "Boot"),
    ("Kork-Slip", 74.90, "Low-Cut"),
    ("Algae-Runner", 99.95, "Low-Cut"),
]
cursor.executemany("INSERT INTO produkt (name, preis, kategorie) VALUES (?, ?, ?)", weitere)
conn.commit()
print(f"{cursor.rowcount} weitere Produkte eingefuegt.")

# Kontrolle
cursor.execute("SELECT produkt_id, name, preis FROM produkt")
for zeile in cursor.fetchall():
    print("  ", zeile)

conn.close()

# --- Variante zum Live-Einkommentieren: warum NICHT mit String-Bastelei -------
# eingabe = "Eco-Sneaker'); DROP TABLE produkt; --"     # boeser Input
# cursor.execute(f"INSERT INTO produkt (name) VALUES ('{eingabe}')")   # NIEMALS so!
# # Mit ? waere derselbe Input einfach ein harmloser (langer) Produktname.
