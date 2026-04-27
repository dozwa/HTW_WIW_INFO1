"""
03 -- Kommentare | Demo 3: Gute vs. schlechte Kommentare

Zeigt mit Veggie-Soles-Beispielen, welche Kommentare hilfreich sind und
welche besser weggelassen werden sollten.

Verwendet nur Konzepte aus den Notebooks 01-03 (print() + Kommentare).
"""

# ============================================================
# SCHLECHT: Kommentar wiederholt nur den Code
# ============================================================

print("Hallo")          # gibt Hallo aus    <- ueberfluessig

# ============================================================
# GUT: Kommentar erklaert das WARUM
# ============================================================

# Kopfzeile fuer den Tagesreport (Marketing-Vorgabe 12.04.2026)
print("Veggie Soles -- Tagesreport")

# ============================================================
# SCHLECHT: auskommentierter alter Code, der nie geloescht wurde
# ============================================================

# Frueher hatten wir einen Werbeslogan oben:
# print("Vegan. Fair. Nachhaltig.")
# print("Seit 2024.")

# (Aktuell nicht mehr -- bitte loeschen, Git merkt sich's)

# ============================================================
# GUT: TODO / FIXME als markierte Aufgabe
# ============================================================

# TODO: Datum dynamisch einsetzen, sobald wir das in NB 04 lernen
# FIXME: Trennlinie ist unten breiter als oben

print("---------------------------")
print("Top 1: Eco-Sneaker")
print("Top 2: Hemp-High")
print("Top 3: Bambus-Boot")
print("=============================")
