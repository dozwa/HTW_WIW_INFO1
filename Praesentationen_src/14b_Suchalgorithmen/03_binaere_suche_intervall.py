"""
14b -- Suchalgorithmen | Demo 3: Binaere Suche mit Drei-Zeiger-Animation.

Zeigt:
- die Halbierungs-Idee: Intervall [lo, hi] schrumpft pro Schritt
- drei Zeiger lo / mid / hi unter den Indizes der Liste
- maximal log2(n) Schritte -- bei 16 Elementen also 4

Story: Veggie Soles -- 16 sortierte Bestell-IDs durchsuchen.
"""


def liste_mit_drei_zeigern(liste, lo, mid, hi):
    """Druckt Liste + Zeiger-Zeile mit ^lo, ^mid, ^hi unter den Indizes."""
    spaltenbreite = max(len(str(x)) for x in liste) + 2
    werte_zeile = "".join(f"{str(x):^{spaltenbreite}}" for x in liste)

    # Drei Marker einsammeln (mehrere Marker am gleichen Index zusammenfuegen).
    marker = {}
    for idx, label in [(lo, "lo"), (mid, "mid"), (hi, "hi")]:
        if 0 <= idx < len(liste):
            marker.setdefault(idx, []).append(label)

    zeiger_zeile = ""
    for i in range(len(liste)):
        if i in marker:
            text = "^" + "/".join(marker[i])
            zeiger_zeile += f"{text:^{spaltenbreite}}"
        else:
            zeiger_zeile += " " * spaltenbreite

    print(f"  {werte_zeile}")
    print(f"  {zeiger_zeile}")


def binaere_suche_intervall(liste, ziel):
    """Binaere Suche mit Visualisierung des Intervalls."""
    print(f">>> Suche {ziel} in sortierter Liste {liste}")
    print()
    lo, hi = 0, len(liste) - 1
    schritt = 0

    while lo <= hi:
        schritt += 1
        mid = (lo + hi) // 2
        print(f"--- Schritt {schritt}: lo={lo}, mid={mid}, hi={hi} ---")
        liste_mit_drei_zeigern(liste, lo, mid, hi)

        wert = liste[mid]
        if wert == ziel:
            print(f"    liste[{mid}] = {wert} == {ziel}  -> Treffer!")
            print()
            return mid
        elif wert < ziel:
            print(f"    liste[{mid}] = {wert} < {ziel}  -> rechts weitersuchen")
            lo = mid + 1
        else:
            print(f"    liste[{mid}] = {wert} > {ziel}  -> links weitersuchen")
            hi = mid - 1
        print()

    print(f"    -> Nicht gefunden.")
    return -1


# 1) Klassisches Beispiel mit 16 sortierten Werten.
zahlen = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
binaere_suche_intervall(zahlen, 23)

print("=" * 60)
print()

# 2) Worst-case: nicht enthalten.
binaere_suche_intervall(zahlen, 4)

print("=" * 60)
print()

# 3) Zugriff sehr schnell -- ein Element direkt am Pivot.
binaere_suche_intervall(zahlen, 17)
