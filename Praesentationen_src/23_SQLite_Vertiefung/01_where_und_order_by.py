"""Gezielt filtern und sortieren: WHERE (=, <, AND/OR mit Klammern, BETWEEN, IN,
LIKE, IS NULL) und ORDER BY (ASC/DESC, mehrere Spalten).

Wir arbeiten auf der produkt-Tabelle des Veggie-Soles-Shops (eine In-Memory-DB).
"""
import sqlite3


def shop_db():
    conn = sqlite3.connect(":memory:")
    conn.execute("""CREATE TABLE produkt (
        produkt_id INTEGER PRIMARY KEY, name TEXT, preis REAL, kategorie TEXT)""")
    conn.executemany("INSERT INTO produkt (name, preis, kategorie) VALUES (?, ?, ?)", [
        ("Eco-Sneaker", 89.95, "Low-Cut"), ("Hemp-High", 109.00, "High-Cut"),
        ("Bambus-Boot", 135.50, "Boot"),   ("Kork-Slip", 74.90, "Low-Cut"),
        ("Algae-Runner", 99.95, "Low-Cut"), ("Pilz-Pump", 119.00, None),  # kategorie noch offen -> NULL
    ])
    conn.commit()
    return conn


conn = shop_db()


def zeig(titel, sql, params=()):
    print(f"\n{titel}")
    for zeile in conn.execute(sql, params).fetchall():
        print("  ", zeile)


zeig("Genau 89.95 EUR:", "SELECT name, preis FROM produkt WHERE preis = ?", (89.95,))
zeig("Nicht in Kategorie 'Low-Cut':", "SELECT name, kategorie FROM produkt WHERE kategorie != 'Low-Cut'")

# AND / OR -- Klammern entscheiden! (Low-Cut ODER High-Cut) UND guenstiger als 100
zeig("(Low-Cut oder High-Cut) und < 100 EUR:",
     "SELECT name, kategorie, preis FROM produkt WHERE (kategorie = 'Low-Cut' OR kategorie = 'High-Cut') AND preis < ?",
     (100.0,))

zeig("Preis zwischen 90 und 120 (BETWEEN, inklusiv):",
     "SELECT name, preis FROM produkt WHERE preis BETWEEN 90 AND 120")

zeig("Kategorie in einer Liste (IN):",
     "SELECT name, kategorie FROM produkt WHERE kategorie IN ('Boot', 'High-Cut')")

zeig("Name enthaelt 'er' (LIKE, % = beliebig viele Zeichen):",
     "SELECT name FROM produkt WHERE name LIKE '%er%'")

# NULL: NICHT mit = pruefen, sondern IS NULL / IS NOT NULL
zeig("Kategorie noch nicht gesetzt (IS NULL):", "SELECT name, kategorie FROM produkt WHERE kategorie IS NULL")

# ORDER BY -- sortieren (Standard ASC); mehrere Spalten: erste hat Vorrang
zeig("Nach Preis aufsteigend:", "SELECT name, preis FROM produkt ORDER BY preis ASC")
zeig("Nach Kategorie, dann Preis absteigend:",
     "SELECT kategorie, name, preis FROM produkt ORDER BY kategorie, preis DESC")

conn.close()

# --- Variante zum Live-Einkommentieren: WHERE kategorie = NULL liefert NICHTS ---
# print(conn.execute("SELECT name FROM produkt WHERE kategorie = NULL").fetchall())   # -> []
