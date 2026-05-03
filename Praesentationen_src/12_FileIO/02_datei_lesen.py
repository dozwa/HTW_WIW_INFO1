"""
12 -- File I/O | Demo 2: lesen mit read / readline / Iteration

Zeigt:
- read() laed alles auf einmal als String
- readline() liest die naechste Zeile (mit \\n am Ende)
- for zeile in f: streamt Zeile fuer Zeile

Story: Veggie Soles -- Tagesreport zur Auswertung lesen.
"""

import os


pfad = "tagesreport_demo2.txt"

# Hilfs-Setup: erst eine Datei mit Demo-Inhalten anlegen.
with open(pfad, "w") as f:
    f.write("Eco-Sneaker;89.95\n")
    f.write("Hemp-High;109.00\n")
    f.write("Bambus-Boot;135.50\n")

# 1) read() -- alles auf einmal
f = open(pfad, "r")
inhalt = f.read()
f.close()
print("--- read() ---")
print(inhalt)

# 2) readline() -- erste Zeile getrennt
f = open(pfad, "r")
print("--- readline() ---")
print("Zeile 1:", f.readline().rstrip("\n"))
print("Zeile 2:", f.readline().rstrip("\n"))
f.close()

# 3) for zeile in f -- streamend, ressourcen-schonend bei grossen Dateien
print("--- for zeile in f ---")
with open(pfad, "r") as f:
    for zeile in f:
        name, preis = zeile.rstrip("\n").split(";")
        print(f"{name:13s} -> {preis} EUR")

# Aufraeumen
os.remove(pfad)
