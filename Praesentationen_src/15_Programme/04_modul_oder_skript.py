"""
15 -- Programme | Demo 4: Skript oder Modul? Das __name__-Idiom

Zeigt:
- Was __name__ ist und welche Werte es annehmen kann
- Wozu if __name__ == "__main__": gut ist
- Wie eine Datei beides sein kann: Skript UND importierbares Modul

So vorfuehren:
  1) python3 04_modul_oder_skript.py     -> main() laeuft (Skript)
  2) python3 -c "import importlib.util as u, sys; \
       spec=u.spec_from_file_location('m','04_modul_oder_skript.py'); \
       m=u.module_from_spec(spec); spec.loader.exec_module(m); \
       print('Nach Import: __name__ war', m.__name__)"
     -> main() laeuft NICHT, nur die Funktionen sind geladen.
"""


def begruessung(kunde):
    """Liefert eine Begruessung -- als Modul-Funktion wiederverwendbar."""
    return f"Willkommen bei Veggie Soles, {kunde}!"


def main():
    """Hauptprogramm -- nur bei direkter Ausfuehrung."""
    print("(Skript-Modus aktiv -- main() wird ausgefuehrt)")
    print(begruessung("Anna Mueller"))
    print(begruessung("Max Schmidt"))


# Diese Pruefung ist der Kern des heutigen Themas:
print(f"__name__ in dieser Datei ist gerade: '{__name__}'")

if __name__ == "__main__":
    # Wird ausgefuehrt, wenn die Datei direkt mit `python3 04_...py`
    # gestartet wird.
    main()
else:
    # Wird ausgefuehrt, wenn jemand `import 04_modul_oder_skript` macht.
    # Dann waere __name__ z.B. "04_modul_oder_skript".
    print("(Modul-Modus aktiv -- main() wird NICHT ausgefuehrt)")
    print("  Nur die Funktion 'begruessung' ist jetzt importiert.")
