import sqlite3 as s

conn = s.connect("produkt.db")

cursor = conn.cursor()

# cursor.execute("""
#         CREATE TABLE produkt (
#         produkt_id INTEGER PRIMARY KEY,
#         name       TEXT NOT NULL, 
#         preis      REAL,
#         kategorie  TEXT
#         )
#         """)

# sql = "INSERT INTO produkt (name, preis, kategorie) VALUES (?, ?, ?)"
# cursor.execute(sql, ("Eco-Sneaker", 89.95, "Low-Cut"))

# produkte = [("Test", 12.34, "Neu"), ("Test2", 42.24, "ALT")]

# cursor.executemany(sql, produkte)

# conn.commit()

sql = "SELECT * FROM produkt"

cursor.execute(sql)

print("Alle Produkte:")
cursor.execute("SELECT * FROM produkt")
for zeile in cursor.fetchall():
    print("  ", zeile) 

print("Nur Namen")
cursor.execute("SELECT name FROM produkt")
for zeile in cursor.fetchall():
    print("  ", zeile)

print("Mit Klausel")
grenze = 50.0
cursor.execute("SELECT name FROM produkt WHERE preis > ?", (grenze, ))
for zeile in cursor.fetchall():
    print("  ", zeile)

conn.close()