"""
11 -- Fehlerbehandlung | Demo 1: try / except Grundform

Zeigt:
- Ohne Behandlung crasht das Programm
- try/except fangen den Fehler ab
- Das Programm laeuft danach weiter

Story: Veggie Soles -- Stueckzahl-Eingabe absichern.
"""


# Hinweis: Eingabe ist hardcoded, damit das Skript ohne Tippen laeuft.
# Im Live-Demo bitte input() einkommentieren.
# eingabe = input("Stueckzahl Eco-Sneaker? ")
eingabe = "drei"   # absichtlich falsch, um den Fehler zu provozieren

print(f"Eingabe vom Kunden: {eingabe!r}")

# 1) Ohne Schutz -- waere ein Crash:
# anzahl = int(eingabe)             # ValueError
# print(f"Bestellung: {anzahl}")

# 2) Mit try/except:
try:
    anzahl = int(eingabe)
    print(f"Bestellung: {anzahl} Stueck Eco-Sneaker")
except ValueError:
    print("Konnte die Eingabe nicht in eine Zahl wandeln.")
    print("Bitte eine ganze Zahl wie 3 eingeben.")

print("Programm laeuft weiter -- kein Crash.")

# Variation: eingabe = "3" -> kein Fehler, der except-Block wird uebersprungen.
