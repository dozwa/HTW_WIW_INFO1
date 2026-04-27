"""
07 -- Funktionen | Demo 4: Mehrere Rueckgabewerte

Zeigt:
- Funktion gibt mehrere Werte zurueck (als Tupel)
- Beim Aufruf in mehrere Variablen "entpacken"

Story: Warenkorb-Zusammenfassung bei Veggie Soles.
"""


def warenkorb_zusammenfassung(preise):
    """Liefert Anzahl der Artikel und Gesamtpreis zurueck."""
    anzahl = len(preise)
    gesamtpreis = sum(preise)
    return anzahl, gesamtpreis


# 1) Anna Mueller bestellt drei Paar Sneaker
annas_warenkorb = [89.95, 109.00, 135.50]

n, total = warenkorb_zusammenfassung(annas_warenkorb)
print(f"Annas Warenkorb: {n} Artikel, {total:.2f} EUR")

# 2) Max Schmidt bestellt nur ein Paar
max_warenkorb = [109.00]

n, total = warenkorb_zusammenfassung(max_warenkorb)
print(f"Max Warenkorb:   {n} Artikel, {total:.2f} EUR")

# 3) Tupel-Rueckgabe ohne Entpacken
ergebnis = warenkorb_zusammenfassung(annas_warenkorb)
print(f"\nRueckgabewert ist ein Tupel: {ergebnis}")
print(f"Typ: {type(ergebnis).__name__}")

# 4) Praxis: gleich mit Versand kombinieren
def berechne_versand(summe):
    return 0.0 if summe >= 100 else 4.95


anzahl, summe = warenkorb_zusammenfassung(annas_warenkorb)
versand = berechne_versand(summe)
print(f"\nRechnung Anna: {anzahl} Artikel = {summe:.2f} EUR + {versand:.2f} EUR Versand")
