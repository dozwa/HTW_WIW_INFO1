"""Daten abfragen mit SELECT: alle Spalten, bestimmte Spalten, mit WHERE filtern,
fetchall() vs. fetchone().

Wichtig: execute() schickt nur den Befehl ab -- die Ergebnisse holt man danach
mit fetchone() (eine Zeile), fetchall() (alle) oder fetchmany(n) (n Zeilen).
"""
import sqlite3

# kleine Hilfsfunktion, damit jede Demo dieselben Produkte hat
def shop_db():
    conn = sqlite3.connect(":memory:")
    conn.execute("""
        CREATE TABLE produkt (
            produkt_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL, preis REAL, kategorie TEXT
        )
    """)
    conn.executemany(
        "INSERT INTO produkt (name, preis, kategorie) VALUES (?, ?, ?)",
        [("Eco-Sneaker", 89.95, "Low-Cut"), ("Hemp-High", 109.00, "High-Cut"),
         ("Bambus-Boot", 135.50, "Boot"), ("Kork-Slip", 74.90, "Low-Cut"),
         ("Algae-Runner", 99.95, "Low-Cut")],
    )
    conn.commit()
    return conn

conn = shop_db()
cursor = conn.cursor()

# 1) Alle Spalten, alle Zeilen
print("Alle Produkte:")
cursor.execute("SELECT * FROM produkt")
for zeile in cursor.fetchall():
    print("  ", zeile)            # (produkt_id, name, preis, kategorie)

# 2) Nur bestimmte Spalten -- und gleich beim Auspacken benennen
print("\nName + Preis:")
cursor.execute("SELECT name, preis FROM produkt")
for name, preis in cursor.fetchall():
    print(f"  {name:14s} {preis:7.2f} EUR")

# 3) Mit WHERE filtern -- der Vergleichswert kommt als Platzhalter (?)
preisgrenze = 100.0
cursor.execute("SELECT name, preis FROM produkt WHERE preis < ?", (preisgrenze,))
print(f"\nGuenstiger als {preisgrenze:.2f} EUR:")
for name, preis in cursor.fetchall():
    print(f"  - {name} ({preis:.2f} EUR)")

# 4) Genau eine Zeile erwartet -> fetchone() (gibt None, wenn nichts passt)
cursor.execute("SELECT * FROM produkt WHERE name = ?", ("Hemp-High",))
treffer = cursor.fetchone()
print("\nGesucht 'Hemp-High':", treffer if treffer else "nicht gefunden")

conn.close()

# --- Variante zum Live-Einkommentieren: ORDER BY ist erst NB 23 -- hier mit Python ---
# cursor.execute("SELECT name, preis FROM produkt")
# for name, preis in sorted(cursor.fetchall(), key=lambda t: t[1]):
#     print(name, preis)
