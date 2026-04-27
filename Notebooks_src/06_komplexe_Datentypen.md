---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 06 - Komplexe Datentypen: Mehrere Werte geschickt verwalten

## Willkommen!

Schön, dass Sie wieder dabei sind! In den bisherigen Notebooks haben Sie gelernt, wie man einzelne Werte in Variablen speichert - eine Zahl, ein Text, ein Wahrheitswert. Doch was passiert, wenn Sie viele Werte verwalten möchten? Stellen Sie sich vor, Sie müssen die Namen von 100 Studierenden speichern. Würden Sie 100 verschiedene Variablen anlegen? Das wäre sehr unpraktisch!

Genau hier kommen die **komplexen Datentypen** ins Spiel. Sie ermöglichen es, mehrere Werte elegant in einer einzigen Variable zu organisieren. Das ist ein Meilenstein in Ihrer Programmier-Reise!


## Was Sie heute lernen:
- **Listen** - Mehrere Werte geordnet speichern und verändern
- **Tupel** - Werte speichern, die nicht verändert werden sollen
- **Sets** - Einzigartige Werte ohne Duplikate verwalten
- **Dictionaries** - Daten mit Schlüssel-Wert-Paaren organisieren

## Voraussetzungen
Was Sie schon können sollten:
- Mit `print()` Ausgaben erzeugen
- Mit `input()` Benutzereingaben entgegennehmen
- F-Strings zur Textformatierung nutzen
- Variablen definieren und Werte zuweisen
- Die einfachen Datentypen `int`, `float`, `str` und `bool` verwenden
- Mit `type()` den Typ einer Variable ermitteln

---

+++

## Überblick: Die vier komplexen Datentypen

Python bietet vier wichtige komplexe Datentypen, die jeweils unterschiedliche Stärken haben:

**1. Liste** - Eine geordnete, veränderbare Sammlung von Werten  
Wie ein Notizbuch, in dem Sie Einträge hinzufügen, streichen und umschreiben können.

**2. Tupel** - Eine geordnete, unveränderbare Sammlung von Werten  
Wie eine Liste, aber in Stein gemeißelt - einmal erstellt, bleibt sie so.

**3. Set** - Eine ungeordnete Sammlung von einzigartigen Werten  
Wie eine Sammlung von einzigartigen Briefmarken - jede gibt es nur einmal.

**4. Dictionary** - Eine Sammlung von Schlüssel-Wert-Paaren  
Wie ein echtes Wörterbuch: Zu jedem Begriff (Schlüssel) gehört eine Bedeutung (Wert).

Im Folgenden werden wir jeden dieser Datentypen detailliert kennenlernen!

---

+++

## 1. Listen - Ihre flexible Datensammlung

### Was ist eine Liste?

Stellen Sie sich eine Einkaufsliste vor, die Sie mit Bleistift auf Papier schreiben. Sie können jederzeit Produkte hinzufügen, durchstreichen oder die Reihenfolge ändern. Genau so funktioniert eine **Liste** in Python!

Eine Liste ist ein Container, der mehrere Werte aufnehmen kann - und zwar in einer bestimmten Reihenfolge. Das Besondere: Sie können die Liste jederzeit verändern. Neue Elemente hinzufügen? Kein Problem! Ein Element entfernen? Auch das geht! Ein Element durch ein anderes ersetzen? Natürlich!

Listen sind die am häufigsten verwendeten komplexen Datentypen in Python, weil sie so flexibel sind. Sie können Zahlen speichern, Texte, oder sogar beides gemischt. Python erlaubt das!

### Warum brauchen wir Listen?

Nehmen wir an, Sie möchten die Namen aller Früchte speichern, die Sie im Supermarkt kaufen wollen. Ohne Listen müssten Sie so vorgehen:

```python
frucht1 = "Apfel"
frucht2 = "Banane"
frucht3 = "Kirsche"
```

Das ist umständlich! Was, wenn Sie 10, 20 oder 100 Früchte haben? Mit einer Liste geht das viel eleganter:

```python
früchte = ["Apfel", "Banane", "Kirsche"]
```

Alle Werte sind schön zusammen in einer Variable organisiert!

### Wie funktioniert eine Liste?

Eine Liste wird mit **eckigen Klammern** `[]` erstellt. Die einzelnen Werte (auch "Elemente" genannt) werden durch Kommas getrennt. So sieht die Grundstruktur aus:

```python
meine_liste = [element1, element2, element3]
```

Die Reihenfolge ist wichtig! Python merkt sich genau, in welcher Reihenfolge Sie die Elemente eingefügt haben. Jedes Element bekommt automatisch eine Position (einen "Index"), beginnend bei 0.

### Wann sollten Sie Listen verwenden?

Listen sind perfekt, wenn Sie:
- Mehrere zusammengehörige Werte speichern wollen (z.B. Messwerte, Namen, Preise)
- Die Reihenfolge wichtig ist
- Werte später hinzufügen, entfernen oder ändern möchten
- Nicht sicher sind, wie viele Elemente Sie letztendlich haben werden

Beispiele aus dem Alltag: Einkaufslisten, To-Do-Listen, Teilnehmerlisten, Messwertsammlungen, Produktkataloge.

---

+++

### Ihre erste Liste erstellen

Lassen Sie uns eine einfache Liste mit Fruchtnamen erstellen und ausgeben:

```{code-cell}
# Eine Liste mit drei Früchten erstellen
früchte = ["Apfel", "Banane", "Kirsche"]

# Die ganze Liste ausgeben
print(früchte)
```

Sehen Sie die eckigen Klammern in der Ausgabe? Das zeigt Ihnen: Das ist eine Liste! Python gibt die Liste genau so aus, wie Sie sie definiert haben.

+++

### Den Typ einer Liste prüfen

Mit der `type()` Funktion können Sie überprüfen, dass es sich wirklich um eine Liste handelt:

```{code-cell}
früchte = ["Apfel", "Banane", "Kirsche"]

# Den Datentyp anzeigen
print(type(früchte))
```

Python sagt Ihnen: `<class 'list'>` - das ist eine Liste!

+++

### Auf einzelne Elemente zugreifen - Die Indexierung

Stellen Sie sich vor, Ihre Liste ist ein Regal mit nummerierten Fächern. Jedes Fach hat eine Nummer, mit der Sie darauf zugreifen können. In Python nennen wir diese Nummer **Index**.

**Wichtig:** Python beginnt bei 0 zu zählen! Das erste Element hat also den Index 0, das zweite den Index 1, und so weiter.

```
Liste:     ["Apfel",  "Banane",  "Kirsche"]
Index:         0          1           2
```

Um auf ein einzelnes Element zuzugreifen, schreiben Sie den Variablennamen gefolgt von eckigen Klammern mit dem Index: `liste[index]`

```{code-cell}
früchte = ["Apfel", "Banane", "Kirsche"]

# Das erste Element ausgeben (Index 0)
print(früchte[0])
```

```{code-cell}
früchte = ["Apfel", "Banane", "Kirsche"]

# Das zweite Element ausgeben (Index 1)
print(früchte[1])
```

```{code-cell}
früchte = ["Apfel", "Banane", "Kirsche"]

# Das dritte Element ausgeben (Index 2)
print(früchte[2])
```

### Mini-Übung: Listen erstellen und ausgeben

Jetzt sind Sie dran! Probieren Sie es selbst aus:

**Aufgabe 1:** Erstellen Sie eine Liste namens `städte` mit den Städten "Berlin", "Hamburg" und "München". Geben Sie die ganze Liste aus.

```{code-cell}
# Ihre Lösung hier:
```

**Aufgabe 2:** Erstellen Sie eine Liste namens `zahlen` mit den Zahlen 10, 20 und 30. Geben Sie nur das zweite Element aus (Index 1).

```{code-cell}
# Ihre Lösung hier:
```

**Aufgabe 3:** Erstellen Sie eine Liste namens `farben` mit "rot", "grün" und "blau". Geben Sie das erste und das letzte Element aus.

```{code-cell}
# Ihre Lösung hier:
```

<details>
<summary>Lösungen anzeigen</summary>

```python
# Aufgabe 1:
städte = ["Berlin", "Hamburg", "München"]
print(städte)

# Aufgabe 2:
zahlen = [10, 20, 30]
print(zahlen[1])

# Aufgabe 3:
farben = ["rot", "grün", "blau"]
print(farben[0])
print(farben[2])
```
</details>

---

+++

### Die Länge einer Liste ermitteln mit len()

Oft möchten Sie wissen: Wie viele Elemente hat meine Liste? Dafür gibt es die Funktion `len()` (kurz für "length" = Länge).

Die Funktion zählt für Sie automatisch alle Elemente in der Liste:

```{code-cell}
früchte = ["Apfel", "Banane", "Kirsche", "Orange"]

# Wie viele Früchte sind in der Liste?
anzahl = len(früchte)
print(f"Die Liste enthält {anzahl} Früchte")
```

Das ist sehr praktisch, denn Sie müssen nicht selbst zählen!

+++

### Elemente hinzufügen mit append()

Eine Liste wäre nicht sehr nützlich, wenn Sie sie nicht erweitern könnten. Mit der Methode `append()` können Sie neue Elemente **ans Ende** der Liste anhängen.

Stellen Sie sich vor, Sie kaufen im Supermarkt noch eine zusätzliche Frucht und schreiben sie auf Ihre Einkaufsliste unten dazu. Genau das macht `append()`:

```{code-cell}
früchte = ["Apfel", "Banane", "Kirsche"]
print("Vorher:", früchte)

# Eine neue Frucht hinzufügen
früchte.append("Orange")
print("Nachher:", früchte)
```

Die Orange wurde ans Ende der Liste angehängt! Die anderen Elemente bleiben unverändert.

+++

### Elemente entfernen mit remove()

Manchmal möchten Sie ein Element aus der Liste entfernen. Dafür gibt es die Methode `remove()`. Sie geben an, **welches** Element entfernt werden soll:

```{code-cell}
früchte = ["Apfel", "Banane", "Kirsche", "Orange"]
print("Vorher:", früchte)

# Die Banane entfernen
früchte.remove("Banane")
print("Nachher:", früchte)
```

Die Banane ist weg! Alle anderen Elemente rücken automatisch nach.

+++

### Mini-Übung: Listen manipulieren

Jetzt wird es praktisch! Testen Sie Ihr Wissen:

**Aufgabe 1:** Erstellen Sie eine Liste `werkzeuge` mit "Hammer" und "Schraubenzieher". Fügen Sie "Zange" hinzu und geben Sie die Liste aus.

```{code-cell}
# Ihre Lösung hier:
```

**Aufgabe 2:** Erstellen Sie eine Liste `tiere` mit "Hund", "Katze", "Maus". Entfernen Sie "Maus" und geben Sie die Länge der Liste aus.

```{code-cell}
# Ihre Lösung hier:
```

**Aufgabe 3:** Erstellen Sie eine leere Liste `einkauf = []`. Fügen Sie drei beliebige Produkte hinzu. Geben Sie dann die Liste und ihre Länge aus.

```{code-cell}
# Ihre Lösung hier:
```

<details>
<summary>Lösungen anzeigen</summary>

```python
# Aufgabe 1:
werkzeuge = ["Hammer", "Schraubenzieher"]
werkzeuge.append("Zange")
print(werkzeuge)

# Aufgabe 2:
tiere = ["Hund", "Katze", "Maus"]
tiere.remove("Maus")
print(len(tiere))

# Aufgabe 3:
einkauf = []
einkauf.append("Brot")
einkauf.append("Milch")
einkauf.append("Eier")
print(einkauf)
print(len(einkauf))
```
</details>

---

+++

### Listen mit Benutzereingaben füllen

Listen werden noch mächtiger, wenn Sie sie mit Benutzereingaben kombinieren. So können Anwender selbst bestimmen, welche Daten gespeichert werden:

```{code-cell}
# Eine leere Liste erstellen
meine_wörter = []

# Drei Wörter vom Benutzer eingeben lassen
wort1 = input("Geben Sie das erste Wort ein: ")
meine_wörter.append(wort1)

wort2 = input("Geben Sie das zweite Wort ein: ")
meine_wörter.append(wort2)

wort3 = input("Geben Sie das dritte Wort ein: ")
meine_wörter.append(wort3)

# Die fertige Liste anzeigen
print(f"Ihre Wörterliste: {meine_wörter}")
```

### Praktische Übung: Interaktive Wortliste

Jetzt eine etwas komplexere Aufgabe! Erstellen Sie ein kleines Programm:

1. Lassen Sie den Benutzer drei Wörter eingeben und speichern Sie diese in einer Liste
2. Lassen Sie den Benutzer eine Zahl zwischen 0 und 2 eingeben
3. Geben Sie das Element an dieser Position aus und entfernen Sie es dann aus der Liste
4. Lassen Sie den Benutzer ein neues Wort eingeben und fügen Sie es zur Liste hinzu
5. Geben Sie die finale Liste aus

```{code-cell}
# Ihre Lösung hier:
# Tipp: Verwenden Sie int() um die eingegebene Zahl in einen Integer zu konvertieren
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Leere Liste erstellen
wörter = []

# Drei Wörter eingeben lassen
wort1 = input("Geben Sie das erste Wort ein: ")
wörter.append(wort1)

wort2 = input("Geben Sie das zweite Wort ein: ")
wörter.append(wort2)

wort3 = input("Geben Sie das dritte Wort ein: ")
wörter.append(wort3)

print(f"Aktuelle Liste: {wörter}")

# Position eingeben lassen
position = int(input("Welches Element soll entfernt werden? (0, 1 oder 2): "))

# Element an dieser Position ausgeben und entfernen
entferntes_wort = wörter[position]
print(f"Entferntes Wort: {entferntes_wort}")
wörter.remove(entferntes_wort)

# Neues Wort hinzufügen
neues_wort = input("Geben Sie ein neues Wort ein: ")
wörter.append(neues_wort)

# Finale Liste anzeigen
print(f"Finale Liste: {wörter}")
```
</details>

---

+++

## 2. Tupel - Listen, die sich nicht ändern

### Was ist ein Tupel?

Ein **Tupel** ist wie eine Liste - mit einem entscheidenden Unterschied: Tupel sind **unveränderlich**. Einmal erstellt, können Sie keine Elemente mehr hinzufügen, entfernen oder ändern. Klingt das nach einer Einschränkung? Manchmal ist genau das gewollt!

Stellen Sie sich ein Tupel wie ein versiegeltes Dokument vor. Sie können es lesen, aber nicht mehr bearbeiten. Das ist sehr praktisch, wenn Sie sicherstellen möchten, dass bestimmte Daten nicht versehentlich geändert werden.

### Warum brauchen wir Tupel?

Manchmal haben Sie Daten, die einfach nicht verändert werden sollten. Beispiele:
- **Koordinaten**: Ein Punkt im Raum (x, y, z) sollte nicht plötzlich woanders sein
- **Geburtsdaten**: Ihr Geburtsdatum ist fest und ändert sich nie
- **Konstante Werte**: Physikalische Konstanten, Konfigurationswerte
- **Mehrsprachige Texte**: Übersetzungen eines Begriffs in verschiedenen Sprachen

In all diesen Fällen schützt Sie ein Tupel davor, versehentlich Daten zu ändern, die konstant bleiben sollen.

### Wie funktioniert ein Tupel?

Ein Tupel wird mit **runden Klammern** `()` erstellt - im Gegensatz zu Listen mit eckigen Klammern. Die Syntax ist ansonsten sehr ähnlich:

```python
mein_tupel = (element1, element2, element3)
```

Genau wie bei Listen können Sie mit einem Index auf einzelne Elemente zugreifen. Was Sie **nicht** können: Die Elemente nachträglich ändern!

### Wann sollten Sie Tupel verwenden?

Tupel sind perfekt, wenn Sie:
- Daten haben, die sich nicht ändern sollen
- Sicherstellen möchten, dass niemand (auch Sie selbst nicht) die Daten versehentlich ändert
- Mehrere zusammengehörige Werte als Einheit behandeln wollen
- Konstante Konfigurationsdaten speichern

Beispiele: Koordinaten, RGB-Farbwerte, Produktcodes, Konfigurationseinstellungen, mehrsprachige Begriffe.

---

+++

### Ihr erstes Tupel erstellen

Erstellen wir ein Tupel mit Farbnamen:

```{code-cell}
# Ein Tupel mit drei Farben erstellen
farben = ("rot", "grün", "blau")

# Das ganze Tupel ausgeben
print(farben)
```

Sehen Sie die runden Klammern? Das zeigt Ihnen: Das ist ein Tupel!

+++

### Den Typ eines Tupels prüfen

```{code-cell}
farben = ("rot", "grün", "blau")

# Den Datentyp anzeigen
print(type(farben))
```

Python bestätigt: `<class 'tuple'>` - das ist ein Tupel!

+++

### Auf Tupel-Elemente zugreifen

Der Zugriff funktioniert genau wie bei Listen - mit einem Index in eckigen Klammern:

```{code-cell}
farben = ("rot", "grün", "blau")

# Das erste Element ausgeben (Index 0)
print(farben[0])
```

```{code-cell}
farben = ("rot", "grün", "blau")

# Das zweite Element ausgeben (Index 1)
print(farben[1])
```

### Was passiert, wenn wir ein Tupel ändern wollen?

Schauen wir uns an, was passiert, wenn wir versuchen, ein Element zu ändern:

```{code-cell}
farben = ("rot", "grün", "blau")

# Versuch, das zweite Element zu ändern
# Das wird einen Fehler erzeugen!
farben[1] = "gelb"
```

Python sagt: **TypeError: 'tuple' object does not support item assignment**

Das ist keine schlechte Nachricht! Python schützt Ihr Tupel vor Veränderungen. Genau das wollten wir!

+++

### Die Länge eines Tupels ermitteln

Die `len()` Funktion funktioniert auch bei Tupeln:

```{code-cell}
koordinaten = (10, 20, 30)

# Anzahl der Koordinaten
anzahl = len(koordinaten)
print(f"Das Tupel hat {anzahl} Elemente")
```

### Mini-Übung: Tupel erstellen und verwenden

**Aufgabe 1:** Erstellen Sie ein Tupel `wochentage` mit "Montag", "Dienstag", "Mittwoch". Geben Sie den zweiten Wochentag aus.

```{code-cell}
# Ihre Lösung hier:
```

**Aufgabe 2:** Erstellen Sie ein Tupel `rgb` mit den Zahlen 255, 0, 128 (ein RGB-Farbwert). Geben Sie alle drei Werte einzeln mit beschreibendem Text aus.

```{code-cell}
# Ihre Lösung hier:
```

<details>
<summary>Lösungen anzeigen</summary>

```python
# Aufgabe 1:
wochentage = ("Montag", "Dienstag", "Mittwoch")
print(wochentage[1])

# Aufgabe 2:
rgb = (255, 0, 128)
print(f"Rot: {rgb[0]}")
print(f"Grün: {rgb[1]}")
print(f"Blau: {rgb[2]}")
```
</details>

---

+++

### Praktische Übung: Mehrsprachiges Programm

Erstellen Sie ein kleines mehrsprachiges Programm:

1. Definieren Sie ein Tupel `nummer_wort` mit "Nummer" auf Deutsch, "Number" auf Englisch und "Numéro" auf Französisch
2. Definieren Sie ein Tupel `summe_wort` mit "Summe" auf Deutsch, "Sum" auf Englisch und "Somme" auf Französisch
3. Definieren Sie eine Variable `sprache` mit Wert 0 für Deutsch (später können Sie 1 für Englisch oder 2 für Französisch testen)
4. Fragen Sie den Benutzer nach der ersten Zahl (verwenden Sie das entsprechende Wort aus `nummer_wort`)
5. Fragen Sie den Benutzer nach der zweiten Zahl
6. Berechnen Sie die Summe und geben Sie sie mit dem entsprechenden Wort aus

```{code-cell}
# Ihre Lösung hier:
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Tupel mit Übersetzungen definieren
nummer_wort = ("Nummer", "Number", "Numéro")
summe_wort = ("Summe", "Sum", "Somme")

# Sprache festlegen (0=Deutsch, 1=Englisch, 2=Französisch)
sprache = 0

# Erste Zahl abfragen
zahl1 = int(input(f"{nummer_wort[sprache]} 1: "))

# Zweite Zahl abfragen
zahl2 = int(input(f"{nummer_wort[sprache]} 2: "))

# Summe berechnen und ausgeben
ergebnis = zahl1 + zahl2
print(f"{summe_wort[sprache]}: {ergebnis}")
```

**Hinweis:** Wenn Sie `sprache = 1` setzen, läuft das Programm auf Englisch. Bei `sprache = 2` auf Französisch!
</details>

---

+++

## 3. Sets - Sammlungen ohne Duplikate

### Was ist ein Set?

Ein **Set** (englisch für "Menge") ist eine Sammlung von Werten mit einer besonderen Eigenschaft: **Jeder Wert kommt nur einmal vor!** Duplikate werden automatisch entfernt. Außerdem sind Sets **ungeordnet** - das heißt, Python merkt sich keine bestimmte Reihenfolge.

Stellen Sie sich ein Set wie eine Sammlung von einzigartigen Briefmarken vor. Jede Briefmarke gibt es nur einmal. Wenn Sie versuchen, dieselbe Briefmarke nochmal hinzuzufügen, wird sie einfach ignoriert.

### Warum brauchen wir Sets?

Sets sind extrem nützlich, wenn Sie:
- Duplikate aus Daten entfernen möchten
- Prüfen wollen, ob ein bestimmter Wert vorhanden ist (sehr schnell!)
- Mathematische Mengenoperationen durchführen möchten
- Eine Sammlung eindeutiger Werte benötigen

Praktische Beispiele: Liste aller unterschiedlichen Bauteile in einem Lager, alle verschiedenen Benutzer die eine Website besucht haben, eindeutige Produktkategorien.

### Wie funktioniert ein Set?

Ein Set wird mit **geschwungenen Klammern** `{}` erstellt:

```python
mein_set = {element1, element2, element3}
```

Wenn Sie dasselbe Element mehrfach hinzufügen, wird es automatisch nur einmal gespeichert. Das ist die Magie von Sets!

**Wichtig:** Da Sets ungeordnet sind, können Sie **nicht** mit einem Index darauf zugreifen wie bei Listen oder Tupeln.

### Wann sollten Sie Sets verwenden?

Sets sind perfekt, wenn Sie:
- Duplikate automatisch eliminieren möchten
- Die Reihenfolge unwichtig ist
- Sehr schnell prüfen möchten, ob ein Element vorhanden ist
- Mit einzigartigen Werten arbeiten

---

+++

### Ihr erstes Set erstellen

Schauen wir uns an, wie Sets Duplikate automatisch entfernen:

```{code-cell}
# Ein Set mit einigen doppelten Zahlen
zahlen = {1, 2, 3, 4, 4, 5, 5, 5}

# Set ausgeben - Duplikate sind weg!
print(zahlen)
```

Sehen Sie? Die doppelten 4er und 5er wurden automatisch entfernt. Jede Zahl kommt nur einmal vor!

+++

### Den Typ eines Sets prüfen

```{code-cell}
früchte = {"Apfel", "Banane", "Kirsche"}

# Den Datentyp anzeigen
print(type(früchte))
```

Python sagt: `<class 'set'>` - das ist ein Set!

+++

### Die Länge eines Sets ermitteln

Die `len()` Funktion zählt die eindeutigen Elemente:

```{code-cell}
früchte = {"Apfel", "Banane", "Kirsche", "Apfel"}  # "Apfel" kommt zweimal vor

# Anzahl der eindeutigen Früchte
anzahl = len(früchte)
print(f"Das Set enthält {anzahl} eindeutige Früchte")
print(früchte)
```

Obwohl wir "Apfel" zweimal angegeben haben, zählt `len()` nur 3, weil das Set nur eindeutige Werte speichert.

+++

### Elemente hinzufügen mit add()

Mit `add()` können Sie neue Elemente zu einem Set hinzufügen:

```{code-cell}
früchte = {"Apfel", "Banane", "Kirsche"}
print("Vorher:", früchte)

# Eine neue Frucht hinzufügen
früchte.add("Orange")
print("Nachher:", früchte)
```

### Was passiert bei doppelten Elementen?

Wenn Sie versuchen, ein Element hinzuzufügen, das schon existiert, passiert einfach nichts:

```{code-cell}
früchte = {"Apfel", "Banane", "Kirsche"}
print("Vorher:", früchte)

# Versuchen, "Apfel" nochmal hinzuzufügen
früchte.add("Apfel")
print("Nachher:", früchte)
```

Das Set bleibt unverändert! Python ignoriert das doppelte Element einfach.

+++

### Elemente entfernen mit remove()

Genau wie bei Listen können Sie Elemente mit `remove()` entfernen:

```{code-cell}
früchte = {"Apfel", "Banane", "Kirsche", "Orange"}
print("Vorher:", früchte)

# Die Banane entfernen
früchte.remove("Banane")
print("Nachher:", früchte)
```

### Mini-Übung: Sets verwenden

**Aufgabe 1:** Erstellen Sie ein Set `buchstaben` mit den Buchstaben "A", "B", "C", "A", "B". Geben Sie das Set aus und beobachten Sie, wie Duplikate entfernt werden.

```{code-cell}
# Ihre Lösung hier:
```

**Aufgabe 2:** Erstellen Sie ein leeres Set `meine_zahlen = set()`. Fügen Sie die Zahlen 10, 20, 30 und nochmal 10 hinzu. Geben Sie das Set und seine Länge aus.

```{code-cell}
# Ihre Lösung hier:
```

<details>
<summary>Lösungen anzeigen</summary>

```python
# Aufgabe 1:
buchstaben = {"A", "B", "C", "A", "B"}
print(buchstaben)  # Ausgabe: {'A', 'B', 'C'}

# Aufgabe 2:
meine_zahlen = set()
meine_zahlen.add(10)
meine_zahlen.add(20)
meine_zahlen.add(30)
meine_zahlen.add(10)  # wird ignoriert
print(meine_zahlen)
print(len(meine_zahlen))  # Ausgabe: 3
```
</details>

---

+++

### Listen in Sets umwandeln

Eine sehr praktische Anwendung: Sie können eine Liste mit Duplikaten in ein Set umwandeln, um automatisch alle Duplikate zu entfernen:

```{code-cell}
# Eine Liste mit vielen Duplikaten
zahlen_liste = [1, 2, 2, 3, 4, 4, 4, 5, 1, 2]
print("Original-Liste:", zahlen_liste)

# In ein Set umwandeln - Duplikate werden entfernt
zahlen_set = set(zahlen_liste)
print("Als Set:", zahlen_set)
```

### Sets zurück in Listen umwandeln

Wenn Sie wieder eine geordnete Liste brauchen, können Sie das Set mit `list()` zurückverwandeln:

```{code-cell}
zahlen_set = {1, 2, 3, 4, 5}
print("Als Set:", zahlen_set)

# Zurück in eine Liste umwandeln
zahlen_liste = list(zahlen_set)
print("Als Liste:", zahlen_liste)
```

### Praktische Übung: Duplikate aus Bauteilliste entfernen

Sie haben eine Liste von Bauteilnamen mit vielen Duplikaten. Ermitteln Sie, wie viele unterschiedliche Bauteile es gibt:

```{code-cell}
# Gegeben ist folgende Liste aus Bauteilen
bauteil_namen = [
    "Schraube",
    "Mutter",
    "Unterlegscheibe",
    "Dichtung",
    "Schraube",
    "Kabel",
    "Ventil",
    "Feder",
    "Achse",
    "Dichtung",
    "Bolzen",
    "Kabel",
    "Ventil",
    "Bolzen",
    "Zahnrad",
    "Unterlegscheibe"
]

# Ihre Aufgabe:
# 1. Erstellen Sie ein Set aus der Liste (um Duplikate zu entfernen)
# 2. Wandeln Sie das Set in eine Liste um
# 3. Ermitteln Sie die Anzahl unterschiedlicher Bauteile
# 4. Geben Sie die Anzahl und die Liste eindeutiger Bauteile aus

# Ihre Lösung hier:
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Set erstellen (Duplikate werden automatisch entfernt)
bauteil_set = set(bauteil_namen)

# Zurück in eine Liste umwandeln
eindeutige_bauteile = list(bauteil_set)

# Anzahl ermitteln
anzahl = len(eindeutige_bauteile)

# Ausgabe
print(f"Anzahl unterschiedlicher Bauteile: {anzahl}")
print(f"Liste: {eindeutige_bauteile}")
```
</details>

---

+++

## 4. Dictionaries - Daten mit Schlüsseln organisieren

### Was ist ein Dictionary?

Ein **Dictionary** (englisch für "Wörterbuch") ist eine Sammlung von **Schlüssel-Wert-Paaren**. Stellen Sie sich ein echtes Wörterbuch vor: Sie schlagen ein Wort nach (das ist der **Schlüssel**), und finden dazu eine Erklärung (das ist der **Wert**).

In Python können Sie mit Dictionaries jedem beliebigen Schlüssel einen Wert zuordnen. Zum Beispiel: Jedem Namen eine Telefonnummer, jedem Produkt einen Preis, jedem Bauteil eine Anzahl.

### Warum brauchen wir Dictionaries?

Dictionaries sind extrem mächtig, weil Sie Daten nicht über eine Position (Index) ansprechen, sondern über einen **aussagekräftigen Schlüssel**. Das macht den Code viel lesbarer und verständlicher!

Vergleichen Sie:
- Liste: `telefonnummern[0]` - welche Nummer ist das?
- Dictionary: `telefonnummern["Alice"]` - sofort klar, wessen Nummer das ist!

Dictionaries sind perfekt, wenn Daten logisch zusammengehören: Name und Telefonnummer, Produkt und Preis, Bauteil und Menge, Land und Hauptstadt.

### Wie funktioniert ein Dictionary?

Ein Dictionary wird mit **geschwungenen Klammern** `{}` erstellt. Jedes Element besteht aus einem Schlüssel-Wert-Paar, getrennt durch einen **Doppelpunkt** `:`:

```python
mein_dictionary = {
    "schlüssel1": "wert1",
    "schlüssel2": "wert2",
    "schlüssel3": "wert3"
}
```

Um auf einen Wert zuzugreifen, verwenden Sie den zugehörigen Schlüssel: `mein_dictionary["schlüssel1"]`

### Wann sollten Sie Dictionaries verwenden?

Dictionaries sind perfekt, wenn Sie:
- Daten mit einem aussagekräftigen Namen (Schlüssel) verknüpfen möchten
- Schnell auf Werte anhand eines Schlüssels zugreifen wollen
- Konfigurationen, Einstellungen oder Zuordnungen speichern
- Strukturierte Daten verwalten

Beispiele: Telefonbuch, Produktkatalog, Lagerbestand, Kontaktdaten, Konfigurationsdateien, Übersetzungstabellen.

---

+++

### Ihr erstes Dictionary erstellen

Erstellen wir ein einfaches Telefonbuch:

```{code-cell}
# Ein Dictionary mit Namen und Telefonnummern
telefonbuch = {
    "Alice": "1234",
    "Bob": "5678",
    "Charlie": "9101"
}

# Das ganze Dictionary ausgeben
print(telefonbuch)
```

Sehen Sie die Struktur? Jeder Name (Schlüssel) ist mit einer Telefonnummer (Wert) verbunden!

+++

### Den Typ eines Dictionaries prüfen

```{code-cell}
telefonbuch = {"Alice": "1234", "Bob": "5678"}

# Den Datentyp anzeigen
print(type(telefonbuch))
```

Python bestätigt: `<class 'dict'>` - das ist ein Dictionary!

+++

### Auf Werte zugreifen über den Schlüssel

Der große Vorteil von Dictionaries: Sie können über den aussagekräftigen Schlüssel auf Werte zugreifen:

```{code-cell}
telefonbuch = {
    "Alice": "1234",
    "Bob": "5678",
    "Charlie": "9101"
}

# Alices Telefonnummer abrufen
nummer = telefonbuch["Alice"]
print(f"Alices Telefonnummer: {nummer}")
```

```{code-cell}
telefonbuch = {
    "Alice": "1234",
    "Bob": "5678",
    "Charlie": "9101"
}

# Charlies Telefonnummer abrufen
nummer = telefonbuch["Charlie"]
print(f"Charlies Telefonnummer: {nummer}")
```

### Neue Einträge hinzufügen

Sie können jederzeit neue Schlüssel-Wert-Paare hinzufügen:

```{code-cell}
telefonbuch = {
    "Alice": "1234",
    "Bob": "5678"
}
print("Vorher:", telefonbuch)

# Einen neuen Eintrag hinzufügen
telefonbuch["David"] = "1122"
print("Nachher:", telefonbuch)
```

### Einträge ändern

Sie können auch bestehende Werte überschreiben:

```{code-cell}
telefonbuch = {
    "Alice": "1234",
    "Bob": "5678"
}
print("Vorher:", telefonbuch)

# Alices Nummer ändern
telefonbuch["Alice"] = "9999"
print("Nachher:", telefonbuch)
```

### Die Länge eines Dictionaries ermitteln

`len()` zählt die Anzahl der Schlüssel-Wert-Paare:

```{code-cell}
telefonbuch = {
    "Alice": "1234",
    "Bob": "5678",
    "Charlie": "9101"
}

anzahl = len(telefonbuch)
print(f"Das Telefonbuch hat {anzahl} Einträge")
```

### Alle Schlüssel abrufen mit keys()

Mit der Methode `keys()` können Sie alle Schlüssel ausgeben:

```{code-cell}
telefonbuch = {
    "Alice": "1234",
    "Bob": "5678",
    "Charlie": "9101"
}

# Alle Namen ausgeben
namen = telefonbuch.keys()
print("Alle Namen:", namen)
```

### Alle Werte abrufen mit values()

Mit der Methode `values()` können Sie alle Werte ausgeben:

```{code-cell}
telefonbuch = {
    "Alice": "1234",
    "Bob": "5678",
    "Charlie": "9101"
}

# Alle Telefonnummern ausgeben
nummern = telefonbuch.values()
print("Alle Nummern:", nummern)
```

### Einträge entfernen mit pop()

Mit `pop()` können Sie einen Eintrag über seinen Schlüssel entfernen. Die Methode gibt den entfernten Wert zurück:

```{code-cell}
telefonbuch = {
    "Alice": "1234",
    "Bob": "5678",
    "Charlie": "9101"
}
print("Vorher:", telefonbuch)

# Bob entfernen
entfernte_nummer = telefonbuch.pop("Bob")
print(f"Entfernte Nummer: {entfernte_nummer}")
print("Nachher:", telefonbuch)
```

### Mini-Übung: Dictionaries verwenden

**Aufgabe 1:** Erstellen Sie ein Dictionary `hauptstädte` mit drei Ländern und ihren Hauptstädten (z.B. "Deutschland": "Berlin"). Geben Sie die Hauptstadt von einem Land aus.

```{code-cell}
# Ihre Lösung hier:
```

**Aufgabe 2:** Erstellen Sie ein Dictionary `preise` mit drei Produkten und ihren Preisen (als Zahlen). Berechnen Sie den Gesamtpreis aller Produkte.

```{code-cell}
# Ihre Lösung hier:
```

<details>
<summary>Lösungen anzeigen</summary>

```python
# Aufgabe 1:
hauptstädte = {
    "Deutschland": "Berlin",
    "Frankreich": "Paris",
    "Italien": "Rom"
}
print(hauptstädte["Frankreich"])

# Aufgabe 2:
preise = {
    "Apfel": 1.50,
    "Banane": 0.80,
    "Orange": 1.20
}
# Werte als Liste abrufen und in int-Liste umwandeln
preis_liste = list(preise.values())
gesamtpreis = preis_liste[0] + preis_liste[1] + preis_liste[2]
print(f"Gesamtpreis: {gesamtpreis}")
```
</details>

---

+++

### Praktische Übung: Lagerbestand verwalten

Erstellen Sie ein kleines Programm zur Lagerverwaltung:

1. Definieren Sie ein Dictionary `bauteile` mit 4 verschiedenen Bauteilnamen und deren Anzahl
2. Geben Sie eine Liste aller Bauteilnamen aus (mit `keys()`)
3. Berechnen Sie die Gesamtanzahl aller Bauteile (addieren Sie alle Werte zusammen)
4. Geben Sie die Gesamtanzahl aus

```{code-cell}
# Ihre Lösung hier:
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Dictionary mit Bauteilen und Anzahl
bauteile = {
    "Schraube": 150,
    "Mutter": 120,
    "Unterlegscheibe": 200,
    "Dichtung": 80
}

# Alle Bauteilnamen ausgeben
namen = list(bauteile.keys())
print(f"Verfügbare Bauteile: {namen}")

# Gesamtanzahl berechnen
anzahl_liste = list(bauteile.values())
gesamt = anzahl_liste[0] + anzahl_liste[1] + anzahl_liste[2] + anzahl_liste[3]
print(f"Gesamtanzahl aller Bauteile: {gesamt}")
```
</details>

---

+++

### Praktische Übung: Interaktives Inventarsystem

Erstellen Sie ein interaktives Programm, das Bauteile vom Benutzer abfragt:

1. Erstellen Sie ein leeres Dictionary
2. Fragen Sie den Benutzer nach dem ersten Bauteilnamen
3. Fragen Sie nach der Anzahl dieses Bauteils (mit `int()` in eine Zahl umwandeln)
4. Speichern Sie das Bauteil im Dictionary
5. Wiederholen Sie Schritte 2-4 für zwei weitere Bauteile
6. Geben Sie am Ende eine Übersicht über alle Bauteile und deren Anzahl aus

```{code-cell}
# Ihre Lösung hier:
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Leeres Dictionary erstellen
inventar = {}

# Erstes Bauteil
name1 = input("Name des ersten Bauteils: ")
anzahl1 = int(input(f"Anzahl von {name1}: "))
inventar[name1] = anzahl1

# Zweites Bauteil
name2 = input("Name des zweiten Bauteils: ")
anzahl2 = int(input(f"Anzahl von {name2}: "))
inventar[name2] = anzahl2

# Drittes Bauteil
name3 = input("Name des dritten Bauteils: ")
anzahl3 = int(input(f"Anzahl von {name3}: "))
inventar[name3] = anzahl3

# Übersicht ausgeben
print("\n=== INVENTAR-ÜBERSICHT ===")
print(inventar)
print(f"\nAnzahl verschiedener Bauteile: {len(inventar)}")
```
</details>

---

+++

## Zusammenfassung

Herzlichen Glückwunsch! Sie haben die vier komplexen Datentypen von Python kennengelernt:

### Was Sie gelernt haben:

**Listen** - Flexible, veränderbare Sammlungen
- Erstellen mit `[]`
- Zugriff über Index: `liste[0]`
- Elemente hinzufügen: `liste.append(element)`
- Elemente entfernen: `liste.remove(element)`
- Länge ermitteln: `len(liste)`

**Tupel** - Unveränderliche, geordnete Sammlungen
- Erstellen mit `()`
- Zugriff über Index: `tupel[0]`
- Können nicht verändert werden
- Perfekt für konstante Daten

**Sets** - Sammlungen ohne Duplikate
- Erstellen mit `{}`
- Duplikate werden automatisch entfernt
- Ungeordnet (kein Index-Zugriff)
- Elemente hinzufügen: `set.add(element)`
- Umwandlung: `set(liste)` oder `list(set)`

**Dictionaries** - Schlüssel-Wert-Paare
- Erstellen mit `{schlüssel: wert}`
- Zugriff über Schlüssel: `dict[schlüssel]`
- Hinzufügen/Ändern: `dict[schlüssel] = wert`
- Entfernen: `dict.pop(schlüssel)`
- Schlüssel abrufen: `dict.keys()`
- Werte abrufen: `dict.values()`

### Die richtige Wahl treffen:

| Datentyp | Verwenden wenn... |
|----------|------------------|
| **Liste** | Reihenfolge wichtig ist und Daten sich ändern können |
| **Tupel** | Daten konstant bleiben sollen |
| **Set** | Duplikate vermieden werden sollen |
| **Dictionary** | Daten mit aussagekräftigen Schlüsseln verknüpft werden sollen |

---

+++

## Trainingsmaterial

Jetzt kommt der wichtigste Teil: Üben, üben, üben! Je mehr Sie mit diesen Datentypen arbeiten, desto selbstverständlicher wird ihre Verwendung.

### Einfache Aufgaben (zum Warmwerden)

**Aufgabe 1: Einkaufsliste**
- Erstellen Sie eine leere Liste `einkauf`
- Fügen Sie 5 Produkte hinzu
- Geben Sie das dritte Produkt aus
- Entfernen Sie das erste Produkt
- Geben Sie die finale Liste und ihre Länge aus

```{code-cell}
# Ihre Lösung hier:
```

**Aufgabe 2: Koordinaten**
- Erstellen Sie ein Tupel `punkt` mit drei Koordinaten (x=10, y=20, z=30)
- Geben Sie jede Koordinate einzeln mit Beschriftung aus
- Versuchen Sie, die y-Koordinate zu ändern (was passiert?)

```{code-cell}
# Ihre Lösung hier:
```

**Aufgabe 3: Eindeutige Zahlen**
- Erstellen Sie eine Liste mit den Zahlen: 5, 10, 5, 20, 10, 30, 5
- Wandeln Sie sie in ein Set um
- Geben Sie das Set aus
- Wie viele eindeutige Zahlen gibt es?

```{code-cell}
# Ihre Lösung hier:
```

### Mittlere Aufgaben (schon besser!)

**Aufgabe 4: Notenverwaltung**
- Erstellen Sie ein Dictionary `noten` mit 4 Fächern und ihren Noten (z.B. "Mathe": 1.7)
- Geben Sie alle Fächer aus
- Berechnen Sie die Durchschnittsnote (Summe aller Noten geteilt durch Anzahl)
- Ändern Sie die Note eines Fachs
- Geben Sie das aktualisierte Dictionary aus

```{code-cell}
# Ihre Lösung hier:
```

**Aufgabe 5: Mitgliederliste**
- Erstellen Sie eine Liste `mitglieder` mit 5 Namen
- Lassen Sie den Benutzer einen Namen eingeben, der hinzugefügt werden soll
- Lassen Sie den Benutzer einen Namen eingeben, der entfernt werden soll
- Geben Sie die finale Mitgliederliste und die Anzahl aus

```{code-cell}
# Ihre Lösung hier:
```

### Herausforderungen (für Profis)

**Aufgabe 6: Produktverwaltung**

Erstellen Sie ein umfassendes Produktverwaltungssystem:

1. Erstellen Sie ein leeres Dictionary `produkte`
2. Fragen Sie den Benutzer nach 3 Produkten (Name und Preis)
3. Speichern Sie alle Produkte im Dictionary
4. Geben Sie alle Produktnamen aus
5. Berechnen Sie den Gesamtwert aller Produkte
6. Finden Sie das teuerste Produkt (durchlaufen Sie alle Preise)
7. Lassen Sie den Benutzer ein Produkt zum Entfernen auswählen
8. Geben Sie eine finale Übersicht aus

```{code-cell}
# Ihre Lösung hier:
```

---

## Musterlösungen

+++

<details>
<summary>Lösung zu Aufgabe 1: Einkaufsliste</summary>

```python
# Überlegung:
# - Wir erstellen eine leere Liste
# - Mit append() fügen wir Elemente hinzu
# - Index 2 ist das dritte Element (weil wir bei 0 beginnen)
# - Mit remove() entfernen wir das erste Produkt

# Lösung:
einkauf = []
einkauf.append("Brot")
einkauf.append("Milch")
einkauf.append("Eier")
einkauf.append("Butter")
einkauf.append("Käse")

print(f"Drittes Produkt: {einkauf[2]}")

einkauf.remove("Brot")

print(f"Finale Liste: {einkauf}")
print(f"Anzahl Produkte: {len(einkauf)}")
```

**Häufige Fehler:**
- Index 3 statt 2 für das dritte Element (vergessen, dass wir bei 0 beginnen)
- Vergessen, das erste Element zu speichern, bevor man es entfernt
</details>

+++

<details>
<summary>Lösung zu Aufgabe 2: Koordinaten</summary>

```python
# Überlegung:
# - Tupel werden mit runden Klammern erstellt
# - Index 0, 1, 2 für x, y, z
# - Tupel sind unveränderlich - Änderungsversuch führt zu Fehler

# Lösung:
punkt = (10, 20, 30)

print(f"X-Koordinate: {punkt[0]}")
print(f"Y-Koordinate: {punkt[1]}")
print(f"Z-Koordinate: {punkt[2]}")

# Änderungsversuch - erzeugt einen Fehler:
# punkt[1] = 25  # TypeError: 'tuple' object does not support item assignment

print("Tupel können nicht geändert werden!")
```

**Häufige Fehler:**
- Eckige statt runde Klammern verwenden (erzeugt eine Liste statt Tupel)
</details>

+++

<details>
<summary>Lösung zu Aufgabe 3: Eindeutige Zahlen</summary>

```python
# Überlegung:
# - Liste erstellen mit Duplikaten
# - set() wandelt in Set um und entfernt Duplikate automatisch
# - len() zählt eindeutige Elemente

# Lösung:
zahlen_liste = [5, 10, 5, 20, 10, 30, 5]
print(f"Original-Liste: {zahlen_liste}")

zahlen_set = set(zahlen_liste)
print(f"Als Set: {zahlen_set}")

anzahl = len(zahlen_set)
print(f"Anzahl eindeutiger Zahlen: {anzahl}")
```

**Erklärung:**
Die Liste hat 7 Elemente, aber nur 4 sind eindeutig: 5, 10, 20, 30
</details>

+++

<details>
<summary>Lösung zu Aufgabe 4: Notenverwaltung</summary>

```python
# Überlegung:
# - Dictionary mit Fächern als Schlüssel und Noten als Werte
# - keys() gibt alle Schlüssel zurück
# - values() gibt alle Werte zurück, die wir für Durchschnitt brauchen
# - Durch Neuzuweisung können wir Werte ändern

# Lösung:
noten = {
    "Mathematik": 1.7,
    "Physik": 2.0,
    "Informatik": 1.3,
    "Chemie": 2.3
}

# Alle Fächer ausgeben
fächer = list(noten.keys())
print(f"Fächer: {fächer}")

# Durchschnitt berechnen
noten_liste = list(noten.values())
summe = noten_liste[0] + noten_liste[1] + noten_liste[2] + noten_liste[3]
durchschnitt = summe / len(noten_liste)
print(f"Durchschnittsnote: {durchschnitt}")

# Note ändern
noten["Physik"] = 1.7
print(f"\nAktualisiertes Dictionary: {noten}")
```
</details>

+++

<details>
<summary>Lösung zu Aufgabe 5: Mitgliederliste</summary>

```python
# Überlegung:
# - Liste mit anfänglichen Mitgliedern erstellen
# - input() für Benutzereingaben
# - append() zum Hinzufügen
# - remove() zum Entfernen

# Lösung:
mitglieder = ["Anna", "Bernd", "Clara", "David", "Emma"]
print(f"Aktuelle Mitglieder: {mitglieder}")

# Neues Mitglied hinzufügen
neues_mitglied = input("Name des neuen Mitglieds: ")
mitglieder.append(neues_mitglied)
print(f"Nach Hinzufügen: {mitglieder}")

# Mitglied entfernen
zu_entfernen = input("Welches Mitglied soll entfernt werden? ")
mitglieder.remove(zu_entfernen)

# Finale Ausgabe
print(f"\nFinale Mitgliederliste: {mitglieder}")
print(f"Anzahl Mitglieder: {len(mitglieder)}")
```
</details>

+++

<details>
<summary>Lösung zu Aufgabe 6: Produktverwaltung</summary>

```python
# Überlegung:
# - Dictionary für Produkt-Preis-Paare
# - Mehrere Eingaben nacheinander abfragen
# - values() für Preise, um Gesamtwert und Maximum zu finden
# - Alle Preise einzeln vergleichen für Maximum

# Lösung:
produkte = {}

# Drei Produkte abfragen
print("Bitte geben Sie drei Produkte ein:\n")

name1 = input("Produktname 1: ")
preis1 = float(input(f"Preis von {name1}: "))
produkte[name1] = preis1

name2 = input("Produktname 2: ")
preis2 = float(input(f"Preis von {name2}: "))
produkte[name2] = preis2

name3 = input("Produktname 3: ")
preis3 = float(input(f"Preis von {name3}: "))
produkte[name3] = preis3

# Produktnamen ausgeben
print(f"\nAlle Produkte: {list(produkte.keys())}")

# Gesamtwert berechnen
preise = list(produkte.values())
gesamtwert = preise[0] + preise[1] + preise[2]
print(f"Gesamtwert: {gesamtwert} Euro")

# Teuerstes Produkt finden
# Wir vergleichen alle drei Preise
max_preis = preise[0]
if preise[1] > max_preis:
    max_preis = preise[1]
if preise[2] > max_preis:
    max_preis = preise[2]

# Name des teuersten Produkts finden
produktnamen = list(produkte.keys())
if produkte[produktnamen[0]] == max_preis:
    teuerstes = produktnamen[0]
elif produkte[produktnamen[1]] == max_preis:
    teuerstes = produktnamen[1]
else:
    teuerstes = produktnamen[2]

print(f"Teuerstes Produkt: {teuerstes} mit {max_preis} Euro")

# Produkt entfernen
zu_entfernen = input("\nWelches Produkt soll entfernt werden? ")
produkte.pop(zu_entfernen)

# Finale Übersicht
print("\n=== FINALE ÜBERSICHT ===")
print(produkte)
print(f"Verbleibende Produkte: {len(produkte)}")
```

**Hinweis:** Diese Aufgabe ist anspruchsvoll! Es ist in Ordnung, wenn Sie Hilfe brauchen. Die Logik zum Finden des Maximums werden wir später mit Schleifen viel eleganter lösen können.
</details>

+++

---

## Ausblick

Im nächsten Notebook lernen Sie **Funktionen** kennen - eine Möglichkeit, Code wiederzuverwenden und Programme übersichtlicher zu gestalten. Funktionen werden oft mit Listen und Dictionaries kombiniert, um mächtige Programme zu erstellen!

Bis dahin: Üben Sie fleißig mit den komplexen Datentypen. Sie sind die Grundlage für fast alles, was noch kommt!

**Viel Erfolg!**
