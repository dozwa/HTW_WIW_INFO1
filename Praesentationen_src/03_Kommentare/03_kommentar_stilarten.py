"""
03 -- Kommentare | Demo 3: Gute vs. schlechte Kommentare

Zeigt mit Veggie-Soles-Beispielen, welche Kommentare hilfreich sind und
welche besser weggelassen werden sollten.
"""

# ============================================================
# SCHLECHT: Kommentar wiederholt nur den Code
# ============================================================

i = 0
i = i + 1     # i um eins erhoehen   <- ueberfluessig

# ============================================================
# GUT: Kommentar erklaert das WARUM
# ============================================================

bestellnummer = i   # nur fuer Demo -- normalerweise aus DB

mwst_satz = 0.19    # gesetzliche MwSt fuer physische Ware in DE

# ============================================================
# SCHLECHT: auskommentierter alter Code, der nie geloescht wurde
# ============================================================

# Frueher hatten wir 7% MwSt fuer Buecher:
# mwst_satz = 0.07
# preis_brutto = preis * (1 + mwst_satz)

# (Seit 2024 nicht mehr relevant -- bitte loeschen, Git merkt sich's)

# ============================================================
# GUT: TODO / FIXME als markierte Aufgabe
# ============================================================

# TODO: Stammkunden-Rabatt einrechnen, sobald die Kundenliste verfuegbar ist
# FIXME: Float-Arithmetik bei sehr grossen Summen ungenau -- Decimal pruefen


# ============================================================
# Praxis: was waere hier ein guter Kommentar?
# ============================================================

# Versandkosten Eco-Sneaker
warenwert = 89.95

# Pauschale 4.95 EUR -- gratis ab 100 (Marketing-Vorgabe 12.04.2026)
versand = 0.0 if warenwert >= 100 else 4.95

print(f"Warenwert: {warenwert} EUR, Versand: {versand} EUR")
