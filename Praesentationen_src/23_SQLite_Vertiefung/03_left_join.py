"""LEFT JOIN: ALLE Zeilen der linken Tabelle -- auch ohne Treffer rechts.
Wo es keinen Treffer gibt, stehen NULL-Werte. Damit findet man auch "die ohne".

Veggie-Soles-In-Memory-DB: kunde, bestellung (Tom Fischer hat keine Bestellung).
"""
import sqlite3


def shop_db():
    conn = sqlite3.connect(":memory:")
    conn.executescript("""
        CREATE TABLE kunde (kunde_id INTEGER PRIMARY KEY, name TEXT);
        CREATE TABLE bestellung (bestell_id INTEGER PRIMARY KEY, kunde_id INTEGER, betrag REAL);
    """)
    conn.executemany("INSERT INTO kunde (name) VALUES (?)",
                     [("Anna Mueller",), ("Max Schmidt",), ("Lena Weber",), ("Tom Fischer",)])
    conn.executemany("INSERT INTO bestellung (kunde_id, betrag) VALUES (?, ?)",
                     [(1, 198.95), (1, 271.00), (2, 89.95), (3, 135.50)])
    conn.commit()
    return conn


conn = shop_db()


def zeig(titel, sql):
    print(f"\n{titel}")
    for zeile in conn.execute(sql).fetchall():
        print("  ", zeile)


# INNER JOIN: Tom fehlt -- er hat keine Bestellung
zeig("INNER JOIN -- nur Kund:innen MIT Bestellung:", """
    SELECT kunde.name, bestellung.betrag
    FROM kunde
    INNER JOIN bestellung ON kunde.kunde_id = bestellung.kunde_id
""")

# LEFT JOIN: ALLE Kund:innen, Tom mit NULL beim Betrag
zeig("LEFT JOIN -- ALLE Kund:innen (Tom: NULL):", """
    SELECT kunde.name, bestellung.betrag
    FROM kunde
    LEFT JOIN bestellung ON kunde.kunde_id = bestellung.kunde_id
""")

# LEFT JOIN + WHERE ... IS NULL: gezielt "die OHNE" finden
zeig("Kund:innen, die noch nie bestellt haben:", """
    SELECT kunde.name
    FROM kunde
    LEFT JOIN bestellung ON kunde.kunde_id = bestellung.kunde_id
    WHERE bestellung.bestell_id IS NULL
""")

conn.close()
