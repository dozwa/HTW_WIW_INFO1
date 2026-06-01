"""Tabellen verbinden mit INNER JOIN: nur Zeilen, die in BEIDEN Tabellen einen
Treffer haben. Inklusive 3-Tabellen-JOIN ueber die Zwischentabelle bestellposition.

Veggie-Soles-In-Memory-DB: kunde, produkt, bestellung, bestellposition.
"""
import sqlite3


def shop_db():
    conn = sqlite3.connect(":memory:")
    conn.executescript("""
        CREATE TABLE kunde   (kunde_id INTEGER PRIMARY KEY, name TEXT, land TEXT);
        CREATE TABLE produkt (produkt_id INTEGER PRIMARY KEY, name TEXT, preis REAL);
        CREATE TABLE bestellung (bestell_id INTEGER PRIMARY KEY, kunde_id INTEGER, datum TEXT, betrag REAL);
        CREATE TABLE bestellposition (position_id INTEGER PRIMARY KEY, bestell_id INTEGER, produkt_id INTEGER, anzahl INTEGER);
    """)
    conn.executemany("INSERT INTO kunde (name, land) VALUES (?, ?)",
                     [("Anna Mueller", "Deutschland"), ("Max Schmidt", "Deutschland"),
                      ("Lena Weber", "Oesterreich"),  ("Tom Fischer", "Deutschland")])  # Tom ohne Bestellung
    conn.executemany("INSERT INTO produkt (name, preis) VALUES (?, ?)",
                     [("Eco-Sneaker", 89.95), ("Hemp-High", 109.00), ("Bambus-Boot", 135.50)])
    conn.executemany("INSERT INTO bestellung (kunde_id, datum, betrag) VALUES (?, ?, ?)",
                     [(1, "2026-05-03", 198.95), (1, "2026-05-09", 271.00),
                      (2, "2026-05-10", 89.95),  (3, "2026-05-11", 135.50)])
    conn.executemany("INSERT INTO bestellposition (bestell_id, produkt_id, anzahl) VALUES (?, ?, ?)",
                     [(1, 1, 1), (1, 2, 1), (2, 3, 2), (3, 1, 1), (4, 3, 1)])
    conn.commit()
    return conn


conn = shop_db()


def zeig(titel, sql, params=()):
    print(f"\n{titel}")
    for zeile in conn.execute(sql, params).fetchall():
        print("  ", zeile)


# 1) Welche Bestellung gehoert zu welcher Kundin? -> kunde JOIN bestellung ueber kunde_id
zeig("Bestellungen mit Kundennamen (INNER JOIN):", """
    SELECT kunde.name, bestellung.datum, bestellung.betrag
    FROM bestellung
    INNER JOIN kunde ON bestellung.kunde_id = kunde.kunde_id
""")
# -> Tom Fischer taucht NICHT auf: er hat keine Bestellung (kein Treffer in beiden Tabellen).

# 2) JOIN + WHERE: nur Bestellungen von Anna
zeig("Nur Annas Bestellungen:", """
    SELECT kunde.name, bestellung.datum, bestellung.betrag
    FROM bestellung
    INNER JOIN kunde ON bestellung.kunde_id = kunde.kunde_id
    WHERE kunde.name = ?
""", ("Anna Mueller",))

# 3) Drei Tabellen verbinden: was steckt in Bestellung 1?
zeig("Inhalt von Bestellung 1 (kunde + bestellposition + produkt):", """
    SELECT kunde.name, produkt.name, bestellposition.anzahl, produkt.preis
    FROM bestellposition
    INNER JOIN bestellung ON bestellposition.bestell_id = bestellung.bestell_id
    INNER JOIN kunde      ON bestellung.kunde_id        = kunde.kunde_id
    INNER JOIN produkt    ON bestellposition.produkt_id = produkt.produkt_id
    WHERE bestellung.bestell_id = 1
""")

conn.close()
