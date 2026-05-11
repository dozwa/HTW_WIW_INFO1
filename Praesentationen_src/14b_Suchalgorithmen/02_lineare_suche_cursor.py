"""
14b -- Suchalgorithmen | Demo 2: Lineare Suche mit Cursor-Visualisierung.

Zeigt:
- Liste mit Cursor "^pos" unter dem aktuellen Index
- Vorbereitung auf die Drei-Zeiger-Visualisierung der Binaersuche

Story: Veggie Soles -- jede Position des Katalogs explizit ablaufen.
"""


def liste_mit_cursor(liste, pos):
    """
    Druckt die Liste in einer Zeile + eine zweite Zeile mit "^pos" unter
    der aktuellen Position. Ergibt eine ASCII-Cursor-Animation pro
    Iteration.
    """
    # Erste Zeile: Liste mit gleichmaessigen Spalten.
    spaltenbreite = max(len(str(x)) for x in liste) + 2
    werte_zeile = "".join(f"{str(x):^{spaltenbreite}}" for x in liste)

    # Zweite Zeile: Cursor-Marker unter aktuellem Index.
    cursor_zeile = ""
    for i in range(len(liste)):
        if i == pos:
            cursor_zeile += f"{'^pos':^{spaltenbreite}}"
        else:
            cursor_zeile += " " * spaltenbreite

    print(f"  {werte_zeile}")
    print(f"  {cursor_zeile}")


def lineare_suche_cursor(liste, ziel):
    """Lineare Suche mit Cursor-Animation."""
    print(f">>> Suche {ziel!r} in {liste}")
    print()
    for i in range(len(liste)):
        liste_mit_cursor(liste, i)
        if liste[i] == ziel:
            print(f"    -> Treffer an Index {i}!")
            print()
            return i
        print(f"    {liste[i]!r} != {ziel!r}, weiter")
        print()
    print(f"    -> Nicht gefunden.")
    return -1


# 1) Zahlen -- gut auf der Folie ablesbar.
zahlen = [10, 20, 30, 40, 50, 60, 70]
lineare_suche_cursor(zahlen, 50)

print("=" * 60)
print()

# 2) Veggie-Soles-Produkte.
katalog = ["Eco", "Hemp", "Bam", "Sock", "Schn"]
lineare_suche_cursor(katalog, "Bam")
