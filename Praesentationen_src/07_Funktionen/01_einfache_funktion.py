"""
07 -- Funktionen | Demo 1: Einfache Funktion ohne Parameter

Zeigt:
- Definition mit `def`
- Aufruf mit ()
- Definieren ungleich Aufrufen

Story: Veggie Soles -- vegane Sneaker.
"""


def zeige_shop_info():
    print("=" * 40)
    print("  Willkommen bei Veggie Soles!")
    print("  Vegane Sneaker, fair produziert.")
    print("=" * 40)


# 1) Bis hier hin: nur Definition. Es passiert noch nichts.
print(">>> Vor dem ersten Aufruf passiert nichts auf dem Bildschirm.")

# 2) Erst der Aufruf führt den Code aus.
zeige_shop_info()

# 3) Beliebig oft wiederholbar.
print(">>> Zweiter Aufruf:")
zeige_shop_info()
