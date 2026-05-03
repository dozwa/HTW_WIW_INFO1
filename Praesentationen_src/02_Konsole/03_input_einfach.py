"""
02 -- Konsole | Demo 3: Eingaben mit input()

Zeigt:
- input(...) zeigt eine Frage und wartet auf Enter
- Die Eingabe kommt als Text zurueck und kann sofort weiterverwendet werden
- Ohne Variablen muss die Eingabe direkt im print() landen

Story: Veggie Soles -- Begruessung des Kunden.
"""


# Variante 1 -- Frage stellen, Antwort sofort wieder ausgeben.
print(input("Wie heissen Sie? "))

# Variante 2 -- zweistufig: erst Frage, dann input + print.
print("Aus welcher Stadt kommen Sie?")
print(input())

# Variante 3 -- mehrere Fragen hintereinander.
# (Jeweils einzeln beantworten und Enter druecken.)
print(input("Was ist Ihre Lieblings-Sneakerfarbe? "))
print(input("Welche Schuhgroesse tragen Sie? "))

# Beobachtung beim Vorfuehren:
# - Solange input() laeuft, blinkt der Cursor und das Programm wartet.
# - Die Antwort verschwindet, wenn wir sie nicht sofort verwenden.
#   Variablen (Notebook 04) loesen genau dieses Problem.
