"""
13b -- Komplexitaet | Demo 3: ASCII-Balken-Diagramm im Terminal.

Zeigt:
- eine kleine Bibliotheksfunktion `print_balken`, die wir in 14a
  fuer Sortier-Visualisierungen wiederverwenden
- Wachstum von O(n) vs. O(n^2) als Balken (statt nur Zahlen)

Story: Veggie Soles -- Shop mit wachsender Produktzahl. Wir machen
das Wachstum SICHTBAR, nicht nur ablesbar.
"""


def print_balken(werte, beschriftungen=None, maxbreite=40, zeichen="#"):
    """
    Druckt einen horizontalen Balken pro Wert in `werte`.
    Der laengste Balken hat `maxbreite` Zeichen.

    Diese Funktion taucht in 14a wieder auf, um Listen-Zustaende beim
    Sortieren zu visualisieren.
    """
    if not werte:
        return
    skala = max(werte) / maxbreite
    if skala == 0:
        skala = 1
    if beschriftungen is None:
        beschriftungen = [str(w) for w in werte]
    label_breite = max(len(s) for s in beschriftungen)
    for label, wert in zip(beschriftungen, werte):
        balken_laenge = int(round(wert / skala))
        balken = zeichen * balken_laenge
        print(f"  {label:>{label_breite}} | {balken} {wert}")


# 1) Ein kleines Beispiel -- Veggie-Soles-Tagesumsatz pro Wochentag.
print("Tagesumsatz Veggie Soles (EUR):")
tage = ["Mo", "Di", "Mi", "Do", "Fr", "Sa"]
umsaetze = [320, 250, 180, 410, 590, 720]
print_balken(umsaetze, tage)

# 2) O(n) vs. O(n^2): Wachstum sichtbar machen.
print()
print("O(n) -- linear:")
n_werte = [1, 2, 4, 8, 16, 32, 64]
print_balken(n_werte, [f"n={n}" for n in n_werte])

print()
print("O(n^2) -- quadratisch:")
quadrate = [n * n for n in n_werte]
print_balken(quadrate, [f"n={n}" for n in n_werte])

# 3) Aha-Effekt -- der letzte Balken bei n=64 ist 4096-mal so gross.
print()
print(">>> O(n^2) waechst sehr viel schneller -- bei groesseren n unbenutzbar.")
