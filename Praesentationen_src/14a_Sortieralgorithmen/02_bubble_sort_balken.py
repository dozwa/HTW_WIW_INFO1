"""
14a -- Sortieralgorithmen | Demo 2: Bubble Sort als ASCII-Balken pro Pass.

Zeigt:
- Wiederverwendung der `print_balken`-Idee aus 13b/03_ascii_balken.py
- Liste nach jedem Pass als horizontaler Balken-Streifen
- man SIEHT, wie das groesste Element pro Pass nach rechts wandert

Story: Veggie Soles -- Stueckzahlen pro Sneaker-Modell. Welches Modell
verkaufen wir am meisten? Bubble Sort macht das Wachstum sichtbar.
"""


def print_balken(werte, beschriftungen=None, maxbreite=30, zeichen="#"):
    """Horizontaler Balken pro Wert. Aus 13b/03 wiederverwendet."""
    if not werte:
        return
    skala = max(werte) / maxbreite
    if skala == 0:
        skala = 1
    if beschriftungen is None:
        beschriftungen = [str(w) for w in werte]
    label_breite = max(len(s) for s in beschriftungen)
    for label, wert in zip(beschriftungen, werte):
        balken = zeichen * int(round(wert / skala))
        print(f"  {label:>{label_breite}} | {balken} {wert}")


def bubble_sort_mit_balken(werte, labels):
    """Bubble Sort, druckt nach jedem Pass alle Balken neu."""
    n = len(werte)
    werte = werte.copy()
    labels = labels.copy()

    print(">>> Start:")
    print_balken(werte, labels)
    print()

    for i in range(n):
        getauscht = False
        for j in range(n - i - 1):
            if werte[j] > werte[j + 1]:
                werte[j], werte[j + 1] = werte[j + 1], werte[j]
                labels[j], labels[j + 1] = labels[j + 1], labels[j]
                getauscht = True
        if not getauscht:
            break
        print(f"--- nach Pass {i + 1} ---")
        print_balken(werte, labels)
        print()

    print(">>> Ende -- sortiert:")
    print_balken(werte, labels)


# 1) Beispiel: verkaufte Stueckzahlen pro Modell.
modelle = ["Eco-Sneaker", "Hemp-High", "Bambus-Boot", "Socken", "Schnuersenkel"]
stueck = [42, 17, 28, 9, 35]

print("Bubble Sort der verkauften Stueckzahlen:")
print()
bubble_sort_mit_balken(stueck, modelle)

# 2) Aha: Reihenfolge der Modell-Labels passt sich mit -- so sieht man,
#        WELCHES Modell wandert.
