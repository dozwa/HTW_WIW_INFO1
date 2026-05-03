"""
02 -- Konsole | Demo 5: Echter Dialog -- input() + F-String

Zeigt:
- input(...) im Inneren eines F-String-Platzhalters
- Mehrere Eingaben in einer Begruessungs-/Bestellsequenz
- Wie sich aus print + input + F-String ein "Gespraech" anfuehlt

Story: Veggie Soles -- Bestellannahme im Shop.

Hinweis fuer den Lecturer: das Skript wartet bei jedem input() auf Enter.
Hier reicht eine Antwort pro Frage -- alles weitere kommt mit Variablen
ab Notebook 04.
"""


# Begruessung mit Namen.
print(f"Hallo {input('Wie heissen Sie? ')}, willkommen bei Veggie Soles!")

# Mini-Beratung -- vier Fragen in vier Zeilen.
print(f"Schoen, Sie kommen aus {input('Aus welcher Stadt kommen Sie? ')}!")
print(f"Sie tragen also {input('Welche Schuhgroesse? ')} -- gut zu wissen.")
print(f"Wir notieren {input('Welches Modell interessiert Sie? ')} fuer Ihre Probebestellung.")

# Verabschiedung in einer einzigen Mega-Zeile.
print(
    f"Vielen Dank, {input('Wie ist Ihr Vorname (zur Bestaetigung)? ')}! "
    f"Wir senden eine Bestaetigung an {input('An welche E-Mail? ')}."
)

# Beobachtung beim Vorfuehren:
# - Jede Frage erscheint, bevor die naechste Zeile verarbeitet wird.
# - Wir muessen die Antwort jeweils direkt verwenden -- speichern geht erst
#   mit Variablen (Notebook 04).
