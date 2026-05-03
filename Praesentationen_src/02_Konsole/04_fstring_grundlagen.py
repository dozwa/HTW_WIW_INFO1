"""
02 -- Konsole | Demo 4: F-Strings -- Text mit Platzhaltern

Zeigt:
- f vor dem Anfuehrungszeichen aktiviert die F-String-Formatierung
- {wert} wird beim Ausgeben durch den Wert ersetzt
- Ohne f bleibt {wert} einfach Text -- typische Anfaenger-Falle

Story: Veggie Soles -- personalisierte Begruessung.
"""


# Einfacher F-String mit einem Platzhalter.
print(f"Willkommen bei {'Veggie Soles'}!")

# Mehrere Platzhalter -- Reihenfolge im Text bleibt erhalten.
print(f"Hallo {'Anna'}, willkommen in {'Berlin'}!")

# Das gleiche fuer unsere Stamm-Kund:innen aus story.md:
print(f"Hallo {'Anna Mueller'} -- danke fuer Ihre Bestellung der {'Eco-Sneaker'}.")
print(f"Hallo {'Max Schmidt'} -- danke fuer Ihre Bestellung der {'Hemp-High'}.")

# Anti-Beispiel -- f vergessen. Der Platzhalter erscheint als Text:
print("Hallo {'Anna'}, willkommen!")

# Beobachtung beim Vorfuehren:
# - Mit f -> Anna erscheint
# - Ohne f -> {'Anna'} erscheint genauso, wie es da steht
# Echter Mehrwert kommt mit Variablen (Notebook 04): f"{name} kostet {preis} EUR".
