"""
13a -- Algorithmen modellieren | Demo 2: Print-Trace eines Algorithmus.

Zeigt:
- wie man jeden Schritt einer Schleife sichtbar macht
- erste Stufe der Visualisierung -- wir bauen darauf in 13b/14a/14b auf

Story: Veggie Soles -- summiere die Tagesverkaeufe der ersten n Tage.
"""


def summe_bis_n(n):
    """Summiert 1 + 2 + ... + n und druckt den Trace pro Schritt."""
    summe = 0
    print(f">>> Start: summe = {summe}")
    for i in range(1, n + 1):
        summe = summe + i
        # Print-Trace: zeigt, wie sich die Variable in jedem Schritt entwickelt.
        print(f"    Schritt {i}: summe = summe + {i} -> {summe}")
    print(f">>> Ende:  summe = {summe}")
    return summe


# 1) Kleines Beispiel mit n=5 -- gut auf der Folie ablesbar.
print("Tagesverkaeufe summieren (n = 5):")
ergebnis = summe_bis_n(5)
print()
print(f"Endergebnis: {ergebnis}")

# 2) Variation als Kommentar -- ohne print, aber gleiches Ergebnis:
# def summe_bis_n_still(n):
#     return n * (n + 1) // 2     # mathematische Formel, O(1)
# print(summe_bis_n_still(5))     # 15
