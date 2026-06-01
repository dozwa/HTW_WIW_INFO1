"""Zusammenfassen: Aggregatfunktionen (COUNT, SUM, AVG, MIN, MAX), GROUP BY
(ein Wert pro Gruppe) und HAVING (Gruppen NACH der Aggregation filtern).

Veggie-Soles-In-Memory-DB: produkt, kunde, bestellung.
Merke: WHERE filtert Zeilen VOR der Gruppierung, HAVING filtert Gruppen DANACH.
"""
import sqlite3


def shop_db():
    conn = sqlite3.connect(":memory:")
    conn.executescript("""
        CREATE TABLE produkt (produkt_id INTEGER PRIMARY KEY, name TEXT, preis REAL, kategorie TEXT);
        CREATE TABLE kunde   (kunde_id INTEGER PRIMARY KEY, name TEXT);
        CREATE TABLE bestellung (bestell_id INTEGER PRIMARY KEY, kunde_id INTEGER, betrag REAL);
    """)
    conn.executemany("INSERT INTO produkt (name, preis, kategorie) VALUES (?, ?, ?)", [
        ("Eco-Sneaker", 89.95, "Low-Cut"), ("Hemp-High", 109.00, "High-Cut"),
        ("Bambus-Boot", 135.50, "Boot"),   ("Kork-Slip", 74.90, "Low-Cut"),
        ("Algae-Runner", 99.95, "Low-Cut"),
    ])
    conn.executemany("INSERT INTO kunde (name) VALUES (?)",
                     [("Anna Mueller",), ("Max Schmidt",), ("Lena Weber",)])
    conn.executemany("INSERT INTO bestellung (kunde_id, betrag) VALUES (?, ?)",
                     [(1, 89.95), (1, 109.00), (1, 60.00),     # Anna: 3 Bestellungen
                      (2, 135.50), (2, 89.95),                  # Max: 2
                      (3, 75.00)])                              # Lena: 1
    conn.commit()
    return conn


conn = shop_db()


def zeig(titel, sql, params=()):
    print(f"\n{titel}")
    for zeile in conn.execute(sql, params).fetchall():
        print("  ", zeile)


# 1) Aggregatfunktionen ueber die ganze Tabelle (Ergebnis: eine Zeile)
zeig("Kennzahlen aller Produkte:",
     "SELECT COUNT(*), MIN(preis), MAX(preis), ROUND(AVG(preis), 2) FROM produkt")

# 2) GROUP BY: ein Wert PRO Gruppe -- Produkte je Kategorie
zeig("Produkte und Durchschnittspreis je Kategorie:", """
    SELECT kategorie, COUNT(*) AS anzahl, ROUND(AVG(preis), 2) AS schnitt
    FROM produkt
    GROUP BY kategorie
    ORDER BY anzahl DESC
""")

# 3) GROUP BY + JOIN: Umsatz und Anzahl Bestellungen je Kundin
zeig("Umsatz je Kundin:", """
    SELECT kunde.name, COUNT(*) AS bestellungen, ROUND(SUM(bestellung.betrag), 2) AS umsatz
    FROM kunde
    INNER JOIN bestellung ON kunde.kunde_id = bestellung.kunde_id
    GROUP BY kunde.kunde_id
    ORDER BY umsatz DESC
""")

# 4) HAVING: nur Gruppen, die NACH der Aggregation eine Bedingung erfuellen
zeig("Nur Kund:innen mit Umsatz ueber 200 EUR (HAVING):", """
    SELECT kunde.name, ROUND(SUM(bestellung.betrag), 2) AS umsatz
    FROM kunde
    INNER JOIN bestellung ON kunde.kunde_id = bestellung.kunde_id
    GROUP BY kunde.kunde_id
    HAVING umsatz > 200
    ORDER BY umsatz DESC
""")

# 5) WHERE vs. HAVING: WHERE wirkt VOR der Gruppierung (nur Bestellungen >= 80 EUR zaehlen)
zeig("Umsatz je Kundin, aber nur aus Bestellungen >= 80 EUR (WHERE + GROUP BY):", """
    SELECT kunde.name, COUNT(*) AS grosse_bestellungen, ROUND(SUM(bestellung.betrag), 2) AS umsatz
    FROM kunde
    INNER JOIN bestellung ON kunde.kunde_id = bestellung.kunde_id
    WHERE bestellung.betrag >= 80
    GROUP BY kunde.kunde_id
    ORDER BY umsatz DESC
""")

conn.close()
