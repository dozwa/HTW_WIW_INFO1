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

# 04 - Variablen: Werte speichern und wiederverwenden

## Willkommen!

Herzlich willkommen zum vierten Notebook! In den vorherigen Notebooks haben Sie gelernt, wie Python-Programme funktionieren, wie Sie Text mit `print()` ausgeben und mit `input()` einlesen können, und wie Sie Ihren Code mit Kommentaren verständlicher machen.

Heute lernen Sie eines der wichtigsten Konzepte der Programmierung kennen: **Variablen**. Mit Variablen können Sie Informationen speichern und später wieder verwenden. Das ist wie ein Gedächtnis für Ihr Programm!


## Was Sie heute lernen:
- Was Variablen sind und wofür man sie braucht
- Wie Sie Werte in Variablen speichern (Wertzuweisung)
- Welche Regeln für Variablennamen gelten
- Wie Sie mehrere Variablen auf einmal erstellen können
- Wie Sie gespeicherte Werte wieder abrufen und nutzen

## Voraussetzungen
Was Sie schon können sollten:
- Grundverständnis von Python und Programmiersprachen (Notebook 01)
- Mit `print()` Text ausgeben (Notebook 02)
- Mit `input()` Eingaben vom Benutzer erhalten (Notebook 02)
- Kommentare schreiben mit `#` (Notebook 03)

+++

## Was ist eine Variable? - Die Schublade für Informationen

Stellen Sie sich vor, Sie räumen Ihr Zimmer auf. Sie haben verschiedene Gegenstände: Socken, Bücher, Stifte. Wohin damit? Sie nehmen Schubladen und kleben auf jede einen beschrifteten Zettel: "Socken", "Bücher", "Stifte". Jetzt wissen Sie immer, wo Sie was finden!

Genau so funktionieren **Variablen** in der Programmierung. Eine Variable ist wie eine beschriftete Schublade (oder Box, Behälter, Ordner), in der Sie Informationen aufbewahren können. Der Name auf dem Zettel ist der **Variablenname**, und der Inhalt der Schublade ist der **Wert** der Variable.

Warum brauchen wir Variablen? Stellen Sie sich vor, Sie schreiben ein Programm, das jemanden begrüßt. Ohne Variablen müssten Sie den Namen immer wieder neu eingeben. Mit Variablen speichern Sie den Namen einmal und können ihn dann beliebig oft verwenden. Das spart nicht nur Arbeit, sondern macht Programme auch flexibel und mächtig!

In der Programmierung ist eine Variable ein **Speicherort** für Daten. Sie können sich das wie einen Platz im Gedächtnis Ihres Computers vorstellen, wo eine Information abgelegt wird. Diese Information kann eine Zahl sein (z.B. 42), ein Text (z.B. "Hallo"), oder etwas anderes. Der große Vorteil: Sie können den Inhalt der Variable jederzeit abrufen, ändern oder in Berechnungen verwenden.

Das Besondere an Python: Sie müssen Python nicht im Voraus sagen, was für eine Art von Information Sie speichern möchten. Python erkennt das automatisch! Sie sagen einfach: "Hier ist eine Schublade mit dem Namen 'alter', und da kommt die Zahl 25 rein." Python versteht sofort, dass 25 eine Zahl ist.

Variablen sind das Fundament der Programmierung. Fast jedes Programm, das Sie jemals schreiben werden, nutzt Variablen. Sie ermöglichen es, mit Daten zu arbeiten, Berechnungen durchzuführen, Benutzereingaben zu verarbeiten und vieles mehr. Ohne Variablen wären Programme extrem starr und unbrauchbar.

+++

### Die Syntax: So erstellen Sie eine Variable

In Python wird eine Variable mit folgender **Syntax** erstellt:

```
variablenname = wert
```

- **Links** vom Gleichheitszeichen steht der **Name** der Variable (wie der Zettel auf der Schublade)
- **Rechts** vom Gleichheitszeichen steht der **Wert**, den Sie speichern möchten (was in die Schublade kommt)
- Das **Gleichheitszeichen `=`** bedeutet: "Speichere den Wert rechts in der Variable links"

**Wichtig:** Das `=` ist KEIN "ist gleich" wie in der Mathematik! Es ist eine **Zuweisung**. Die Information fließt von rechts nach links, wie ein Pfeil ←.

+++

### Erstes Beispiel: Eine Zahl speichern

Schauen wir uns das einfachste Beispiel an. Wir erstellen eine Variable mit dem Namen `antwort` und speichern darin die Zahl `42`:

```{code-cell}
# Wir erstellen eine Variable namens "antwort" und speichern die Zahl 42 darin
antwort = 42
```

**Was ist passiert?**

Python hat eine Schublade mit dem Namen `antwort` erstellt und die Zahl `42` hineingelegt. Die Variable existiert jetzt im Speicher Ihres Computers!

Sie können jetzt jederzeit auf diese Variable zugreifen. Probieren wir es aus:

```{code-cell}
# Wir geben den Inhalt der Variable "antwort" aus
print(antwort)
```

Super! Python zeigt uns `42` - den Wert, den wir gespeichert haben. Die Variable hat sich den Wert gemerkt!

+++

### Zweites Beispiel: Einen Text speichern

Variablen können nicht nur Zahlen speichern. Sie können auch Text speichern. In Python schreiben Sie Text in Anführungszeichen `"..."` oder `'...'`:

```{code-cell}
# Variable "begrüßung" speichert den Text "Hallo Welt"
begrüßung = "Hallo Welt"
```

```{code-cell}
# Wir geben den Text aus
print(begrüßung)
```

Perfekt! Die Variable `begrüßung` hat sich den Text "Hallo Welt" gemerkt.

+++

### Variablen-Explorer in Google Colab

**Tipp für Google Colab Nutzer:**  
Google Colab hat ein praktisches Werkzeug, den **Variablen-Explorer**. Damit können Sie alle Ihre Variablen und deren Werte sehen!

So finden Sie ihn:
- Schauen Sie in die **linke Seitenleiste**
- Klicken Sie auf das Symbol **{x}** (sieht aus wie eine geschweifte Klammer mit x)
- Dort sehen Sie alle Variablen, die Sie erstellt haben

Das ist besonders hilfreich, wenn Sie den Überblick über viele Variablen behalten möchten!

+++

### Sofort ausprobieren!

**Aufgabe 1:** Erstellen Sie eine Variable namens `lieblingsfarbe` und speichern Sie Ihre Lieblingsfarbe als Text darin. Geben Sie die Variable dann mit `print()` aus.

*Hinweis: Text muss in Anführungszeichen stehen, z.B. `"blau"`*

```{code-cell}
# Ihr Code hier:
```

**Aufgabe 2:** Erstellen Sie eine Variable namens `punktzahl` und speichern Sie die Zahl `100` darin. Geben Sie die Variable aus.

*Hinweis: Zahlen brauchen KEINE Anführungszeichen!*

```{code-cell}
# Ihr Code hier:
```

**Aufgabe 3:** Erstellen Sie zwei Variablen: `vorname` mit Ihrem Vornamen und `nachname` mit Ihrem Nachnamen. Geben Sie beide mit `print()` aus.

*Tipp: Sie können mehrere Dinge in print() schreiben, getrennt durch Kommas!*

```{code-cell}
# Ihr Code hier:
```

<details>
<summary>Lösungen anzeigen</summary>

```python
# Aufgabe 1:
lieblingsfarbe = "blau"
print(lieblingsfarbe)

# Aufgabe 2:
punktzahl = 100
print(punktzahl)

# Aufgabe 3:
vorname = "Anna"
nachname = "Schmidt"
print(vorname, nachname)
```
</details>

+++

## Wertzuweisung verstehen - Werte in Schubladen legen

Jetzt verstehen wir das Konzept der **Wertzuweisung** noch genauer. Wertzuweisung bedeutet: "Nimm einen Wert und lege ihn in eine Variable."

Denken Sie wieder an die Schublade: Die **Wertzuweisung** ist der Moment, in dem Sie etwas in die Schublade legen. Sie nehmen einen Gegenstand (den Wert) und platzieren ihn in der beschrifteten Schublade (der Variable). Von diesem Moment an liegt der Gegenstand dort und Sie können ihn jederzeit wieder herausholen.

Der Fachbegriff **Initialisierung** bedeutet, dass eine Variable zum **ersten Mal** einen Wert erhält. Das ist wie das erste Befüllen einer neuen Schublade. Danach können Sie den Inhalt jederzeit ändern - das wäre dann eine neue Wertzuweisung, aber keine Initialisierung mehr.

Der Vorgang läuft immer von **rechts nach links**:
1. Python schaut auf die rechte Seite des `=` und sieht den Wert
2. Python nimmt diesen Wert
3. Python legt ihn in die Variable auf der linken Seite

Das ist wichtig zu verstehen, denn später werden Sie auch Berechnungen auf der rechten Seite haben. Python berechnet ZUERST alles rechts vom `=`, und DANN wird das Ergebnis in die Variable links gespeichert.

+++

### Beispiel: Schritt für Schritt

Schauen wir uns eine Wertzuweisung in Zeitlupe an:

```{code-cell}
# Variable "alter" wird erstellt und erhält den Wert 25
alter = 25
```

**Was passiert hier?**

1. Python sieht: "Rechts vom = steht die Zahl 25"
2. Python sieht: "Links vom = steht der Name 'alter'"
3. Python erstellt eine Variable namens `alter`
4. Python legt die Zahl 25 in diese Variable
5. Fertig! Die Variable `alter` existiert jetzt und enthält 25

+++

### Variablen verwenden

Sobald eine Variable einen Wert hat, können Sie sie überall verwenden, wo Sie sonst den Wert direkt hinschreiben würden:

```{code-cell}
# Variable erstellen
name = "Alice"
```

```{code-cell}
# Variable in print() verwenden
print("Hallo")
print(name)
```

```{code-cell}
# Variable in einem F-String verwenden (F-Strings kennen Sie aus Notebook 02!)
print(f"Willkommen, {name}!")
```

Sehen Sie? Überall wo "Alice" stehen soll, können Sie einfach die Variable `name` verwenden. Praktisch!

+++

### Variablen ändern - Neue Werte zuweisen

Sie können den Wert einer Variable jederzeit ändern. Das ist wie das Umräumen einer Schublade: Sie nehmen den alten Inhalt heraus und legen etwas Neues hinein.

```{code-cell}
# Erste Zuweisung
punktzahl = 10
print(f"Punktzahl: {punktzahl}")
```

```{code-cell}
# Neue Zuweisung - der alte Wert wird überschrieben!
punktzahl = 20
print(f"Neue Punktzahl: {punktzahl}")
```

Die Zahl 10 ist jetzt weg. Die Variable `punktzahl` enthält nur noch die Zahl 20. Der alte Wert wurde ersetzt!

+++

### Das Gleichheitszeichen ist KEINE mathematische Gleichung!

**Wichtiger Hinweis:**  
In der Mathematik bedeutet `=` "ist gleich". In Python bedeutet `=` "speichere rechts in links"!

```python
x = 5    # Bedeutet: Speichere die Zahl 5 in der Variable x
```

Es ist ein **Zuweisungsoperator**, kein Vergleich. Sie weisen den Wert von rechts nach links zu.

+++

### Sofort ausprobieren!

**Aufgabe 1:** Erstellen Sie eine Variable `stadt` mit dem Wert `"Berlin"`. Geben Sie sie aus. Ändern Sie dann den Wert zu `"München"` und geben Sie die Variable erneut aus.

```{code-cell}
# Ihr Code hier:
```

**Aufgabe 2:** Erstellen Sie eine Variable `leben` mit dem Wert `3`. Geben Sie sie aus. Setzen Sie dann den Wert auf `2` und geben Sie sie wieder aus.

```{code-cell}
# Ihr Code hier:
```

**Aufgabe 3:** Erstellen Sie eine Variable `begrüßung` mit dem Text `"Guten Morgen"`. Verwenden Sie die Variable in einem F-String: `print(f"{begrüßung}, wie geht es Ihnen?")`

```{code-cell}
# Ihr Code hier:
```

<details>
<summary>Lösungen anzeigen</summary>

```python
# Aufgabe 1:
stadt = "Berlin"
print(stadt)
stadt = "München"
print(stadt)

# Aufgabe 2:
leben = 3
print(leben)
leben = 2
print(leben)

# Aufgabe 3:
begrüßung = "Guten Morgen"
print(f"{begrüßung}, wie geht es Ihnen?")
```
</details>

+++

## Variablennamen - Die Beschriftung der Schublade

Sie können Ihre Variablen fast beliebig benennen - aber es gibt ein paar wichtige Regeln! Der Variablenname ist wie die Beschriftung auf der Schublade: Sie sollte klar, verständlich und eindeutig sein.

Stellen Sie sich vor, Sie beschriften Schubladen in Ihrem Zimmer. Würden Sie eine Schublade mit "X1" beschriften? Oder mit "123abc"? Wahrscheinlich nicht! Sie würden sinnvolle Namen wählen wie "Socken", "T-Shirts" oder "Briefe". Genau so sollten Sie auch Variablennamen wählen.

**Gute Variablennamen** machen Ihren Code **lesbar** und **verständlich**. Wenn Sie oder jemand anderes Ihren Code später liest, sollte sofort klar sein, was in der Variable gespeichert ist. Ein Name wie `alter` ist viel besser als `x` oder `a1`.

In Python gibt es klare **Regeln**, was erlaubt ist und was nicht. Diese Regeln stellen sicher, dass Python Ihren Code richtig verstehen kann und es zu keinen Verwechslungen kommt.

+++

### Regeln für Variablennamen

**Erlaubt sind:**
- Buchstaben: `a-z`, `A-Z` (auch Umlaute wie `ä`, `ö`, `ü`)
- Ziffern: `0-9` (aber NICHT am Anfang!)
- Unterstrich: `_`

**Verboten sind:**
- Namen, die mit einer Ziffer beginnen: `1name` ❌
- Leerzeichen im Namen: `mein name` ❌
- Sonderzeichen wie `!`, `?`, `-`, `+`, etc.: `mein-name` ❌
- Python-Schlüsselwörter (reservierte Wörter wie `print`, `if`, `for`, etc.)

**Konventionen (Empfehlungen):**
- Verwenden Sie **aussagekräftige Namen**: `alter` statt `a`
- Für mehrere Wörter: Verwenden Sie Unterstriche: `mein_name` (nennt sich "snake_case")
- Beginnen Sie mit einem Kleinbuchstaben: `name` statt `Name`
- Groß-/Kleinschreibung ist wichtig: `Name` und `name` sind verschiedene Variablen!

+++

### Beispiele: Gut vs. Schlecht

Schauen wir uns gute und schlechte Variablennamen an:

```{code-cell}
# ✅ GUT: Aussagekräftige Namen
alter = 25
vorname = "Anna"
ist_student = "Ja"
```

```{code-cell}
# ❌ SCHLECHT: Unverständliche Namen
a = 25
x = "Anna"
y123 = "Ja"
```

Sehen Sie den Unterschied? Bei den guten Namen wissen Sie sofort, was gespeichert ist. Bei den schlechten Namen müssen Sie raten!

+++

### Was passiert bei falschen Namen?

Wenn Sie gegen die Regeln verstoßen, beschwert sich Python mit einer Fehlermeldung. Das ist gut! Python hilft Ihnen, Fehler zu vermeiden.

Probieren Sie mal aus (wird einen Fehler geben - das ist Absicht!):

```{code-cell}
# Dies wird einen Fehler verursachen - Name beginnt mit Zahl!
# 1name = "Max"
```

Python sagt: "SyntaxError: invalid syntax" - Das bedeutet: "Das verstehe ich nicht, das ist kein gültiger Variablenname!"

+++

### Sofort ausprobieren!

**Aufgabe 1:** Erstellen Sie drei Variablen mit **guten**, aussagekräftigen Namen für:
- Eine Temperatur (z.B. 22)
- Einen Wochentag (z.B. "Montag")
- Eine Hausnummer (z.B. 42)

Geben Sie alle drei Variablen aus.

```{code-cell}
# Ihr Code hier:
```

**Aufgabe 2:** Welche dieser Variablennamen sind ERLAUBT? Überlegen Sie erst, dann testen Sie es!
- `mein_name`
- `3punkt`
- `größe`
- `Lieblings Farbe`
- `alter_2024`

```{code-cell}
# Testen Sie hier:
```

<details>
<summary>Lösungen anzeigen</summary>

```python
# Aufgabe 1:
temperatur = 22
wochentag = "Montag"
hausnummer = 42
print(temperatur, wochentag, hausnummer)

# Aufgabe 2:
# ✅ mein_name - ERLAUBT (Unterstrich ist ok)
# ❌ 3punkt - VERBOTEN (beginnt mit Zahl)
# ✅ größe - ERLAUBT (Umlaute sind ok)
# ❌ Lieblings Farbe - VERBOTEN (Leerzeichen nicht erlaubt)
# ✅ alter_2024 - ERLAUBT (Zahlen sind ok, nur nicht am Anfang)
```
</details>

+++

## Mehrfachzuweisung - Mehrere Variablen auf einmal

Python bietet eine praktische Abkürzung: Sie können mehrere Variablen gleichzeitig erstellen! Das ist wie das gleichzeitige Befüllen mehrerer Schubladen in einem Arbeitsschritt.

Stellen Sie sich vor, Sie haben drei Schubladen nebeneinander und drei Gegenstände. Normalerweise würden Sie dreimal einzeln arbeiten: Gegenstand 1 in Schublade 1, Gegenstand 2 in Schublade 2, Gegenstand 3 in Schublade 3. Mit Mehrfachzuweisung machen Sie das alles in einem Rutsch!

Es gibt zwei Arten von Mehrfachzuweisung:
1. **Verschiedene Werte** an verschiedene Variablen
2. **Derselbe Wert** an mehrere Variablen

Diese Technik ist praktisch, wenn Sie mehrere zusammengehörige Werte haben und nicht für jeden eine extra Zeile schreiben möchten. Sie macht den Code kompakter und manchmal auch übersichtlicher.

+++

### Verschiedene Werte an verschiedene Variablen

Sie können mehrere Variablen in einer Zeile verschiedene Werte zuweisen. Die Syntax ist:

```python
variable1, variable2, variable3 = wert1, wert2, wert3
```

Python weist dabei zu:
- `wert1` → `variable1`
- `wert2` → `variable2`
- `wert3` → `variable3`

```{code-cell}
# Drei Variablen auf einmal erstellen
vorname, nachname, alter = "Anna", "Schmidt", 25
```

```{code-cell}
# Alle drei ausgeben
print(f"Name: {vorname} {nachname}")
print(f"Alter: {alter}")
```

Super! Alle drei Variablen wurden gleichzeitig erstellt und haben ihre Werte erhalten.

+++

### Derselbe Wert an mehrere Variablen

Manchmal möchten Sie mehreren Variablen denselben Wert geben. Das geht auch in einer Zeile:

```python
variable1 = variable2 = variable3 = wert
```

Alle drei Variablen bekommen dann den gleichen Wert.

```{code-cell}
# Drei Variablen mit dem gleichen Wert
x = y = z = 10
```

```{code-cell}
# Alle haben den Wert 10
print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}")
```

Perfekt! Alle drei Variablen enthalten die Zahl 10.

+++

### Wann ist Mehrfachzuweisung nützlich?

Mehrfachzuweisung ist besonders praktisch bei:
- Koordinaten: `x, y = 5, 10`
- Zusammengehörigen Daten: `tag, monat, jahr = 15, 3, 2024`
- Initialisierung mehrerer Zähler: `a = b = c = 0`

+++

### Sofort ausprobieren!

**Aufgabe 1:** Erstellen Sie mit Mehrfachzuweisung drei Variablen:
- `straße` mit dem Wert `"Hauptstraße"`
- `hausnummer` mit dem Wert `42`
- `stadt` mit dem Wert `"Berlin"`

Geben Sie alle drei in einem F-String aus: `"{straße} {hausnummer}, {stadt}"`

```{code-cell}
# Ihr Code hier:
```

**Aufgabe 2:** Erstellen Sie drei Variablen `start`, `mitte`, `ende`, die alle den Wert `0` haben. Verwenden Sie Mehrfachzuweisung mit demselben Wert.

```{code-cell}
# Ihr Code hier:
```

**Aufgabe 3:** Verwenden Sie `input()`, um den Benutzer nach Vorname und Nachname zu fragen. Speichern Sie die Antworten in Variablen und geben Sie dann eine Begrüßung aus.

```{code-cell}
# Ihr Code hier:
```

<details>
<summary>Lösungen anzeigen</summary>

```python
# Aufgabe 1:
straße, hausnummer, stadt = "Hauptstraße", 42, "Berlin"
print(f"{straße} {hausnummer}, {stadt}")

# Aufgabe 2:
start = mitte = ende = 0
print(f"Start: {start}, Mitte: {mitte}, Ende: {ende}")

# Aufgabe 3:
vorname = input("Wie ist Ihr Vorname? ")
nachname = input("Wie ist Ihr Nachname? ")
print(f"Herzlich willkommen, {vorname} {nachname}!")
```
</details>

+++

## Zusammenfassung

Herzlichen Glückwunsch! Sie haben das Konzept der Variablen verstanden - eines der wichtigsten Grundlagen der Programmierung!

### Was Sie gelernt haben:

✅ **Variablen sind wie beschriftete Schubladen** für Informationen  
✅ **Wertzuweisung** erfolgt mit `=` von rechts nach links: `name = wert`  
✅ **Variablennamen** müssen Regeln folgen (kein Start mit Zahl, keine Leerzeichen)  
✅ **Gute Namen** sind aussagekräftig: `alter` statt `x`  
✅ **Mehrfachzuweisung** ermöglicht das Erstellen mehrerer Variablen auf einmal  
✅ **Variablen können geändert werden** - neue Zuweisung überschreibt den alten Wert  
✅ **`=` ist KEINE Gleichung**, sondern eine Zuweisung  

### Wichtige Konzepte:

- **Initialisierung**: Erste Wertzuweisung an eine Variable
- **Zuweisung**: Speichern eines Wertes in einer Variable
- **Variablenname**: Die Beschriftung (Bezeichner) der Variable
- **Wert**: Das, was in der Variable gespeichert ist

Variablen sind das Fundament fast aller Programme. In den nächsten Notebooks lernen Sie, welche verschiedenen Arten von Werten es gibt und was Sie alles damit machen können!

+++

## Trainingsmaterial

Jetzt sind Sie dran! Testen Sie Ihr Wissen mit verschiedenen Aufgaben. Versuchen Sie zuerst, die Aufgaben selbst zu lösen, bevor Sie die Lösungen anschauen.

+++

### Einfache Aufgaben (zum Warmwerden)

**Aufgabe 1:** Erstellen Sie eine Variable `lieblingszahl` und speichern Sie Ihre Lieblingszahl darin. Geben Sie die Variable mit einem schönen Text aus, z.B. "Meine Lieblingszahl ist: ..."

```{code-cell}
# Ihr Code hier:
```

**Aufgabe 2:** Erstellen Sie zwei Variablen `tag` und `monat` für Ihren Geburtstag (z.B. 15 und 3). Geben Sie beide in einem Satz aus: "Ich habe am 15.3. Geburtstag."

```{code-cell}
# Ihr Code hier:
```

**Aufgabe 3:** Erstellen Sie eine Variable `nachricht` mit dem Text "Python macht Spaß!". Geben Sie diese Variable dreimal hintereinander aus.

```{code-cell}
# Ihr Code hier:
```

### Mittlere Aufgaben (schon besser!)

**Aufgabe 4:** Schreiben Sie ein Mini-Programm:
1. Fragen Sie mit `input()` nach dem Namen des Benutzers
2. Fragen Sie nach dem Alter
3. Fragen Sie nach der Lieblingsfarbe
4. Geben Sie alle drei Informationen in einem schönen Satz aus

Beispiel-Ausgabe: "Hallo Anna! Du bist 25 Jahre alt und deine Lieblingsfarbe ist blau."

```{code-cell}
# Ihr Code hier:
```

**Aufgabe 5:** Erstellen Sie Variablen für eine Adresse:
- `straße`, `hausnummer`, `plz`, `stadt`

Verwenden Sie Mehrfachzuweisung für straße und stadt. Geben Sie die komplette Adresse formatiert aus:
```
Hauptstraße 42
12345 Berlin
```

```{code-cell}
# Ihr Code hier:
```

### Herausforderungen (für Profis)

**Aufgabe 6:** Schreiben Sie ein Programm, das:
1. Nach Vorname und Nachname fragt (mit `input()`)
2. Die beiden Namen in den Variablen `vorname` und `nachname` speichert
3. Eine neue Variable `vollständiger_name` erstellt, die beide Namen kombiniert
4. Die Variable `vollständiger_name` ausgibt
5. Dann den Benutzer nach einem Spitznamen fragt
6. Die Variable `vorname` mit dem Spitznamen überschreibt
7. Wieder den vollständigen Namen ausgibt (jetzt mit Spitzname statt Vorname)

*Hinweis: Sie können zwei Textvariablen mit einem Leerzeichen kombinieren: `name1 + " " + name2`*

```{code-cell}
# Ihr Code hier:
```

### Musterlösungen

<details>
<summary>Lösungen anzeigen</summary>

```python
# --- Aufgabe 1 ---
lieblingszahl = 7
print(f"Meine Lieblingszahl ist: {lieblingszahl}")


# --- Aufgabe 2 ---
tag = 15
monat = 3
print(f"Ich habe am {tag}.{monat}. Geburtstag.")


# --- Aufgabe 3 ---
nachricht = "Python macht Spaß!"
print(nachricht)
print(nachricht)
print(nachricht)


# --- Aufgabe 4 ---
# Schritt 1: Daten abfragen
name = input("Wie heißt du? ")
alter = input("Wie alt bist du? ")
lieblingsfarbe = input("Was ist deine Lieblingsfarbe? ")

# Schritt 2: Ausgabe
print(f"Hallo {name}! Du bist {alter} Jahre alt und deine Lieblingsfarbe ist {lieblingsfarbe}.")


# --- Aufgabe 5 ---
# Mehrfachzuweisung für straße und stadt
straße, stadt = "Hauptstraße", "Berlin"
hausnummer = 42
plz = 12345

# Formatierte Ausgabe
print(f"{straße} {hausnummer}")
print(f"{plz} {stadt}")


# --- Aufgabe 6 ---
# Schritt 1-2: Namen abfragen
vorname = input("Wie ist Ihr Vorname? ")
nachname = input("Wie ist Ihr Nachname? ")

# Schritt 3-4: Vollständigen Namen erstellen und ausgeben
vollständiger_name = vorname + " " + nachname
print(f"Ihr vollständiger Name: {vollständiger_name}")

# Schritt 5-6: Spitznamen abfragen und vorname überschreiben
spitzname = input("Haben Sie einen Spitznamen? ")
vorname = spitzname

# Schritt 7: Neuen vollständigen Namen ausgeben
vollständiger_name = vorname + " " + nachname
print(f"Mit Spitzname: {vollständiger_name}")
```

**Erklärung zu Aufgabe 6:**

Diese Aufgabe zeigt ein wichtiges Konzept: Variablen können **überschrieben** werden. Wenn Sie `vorname = spitzname` schreiben, ist der alte Vorname weg und durch den Spitznamen ersetzt. Das ist wie beim Umräumen einer Schublade - der alte Inhalt wird durch den neuen ersetzt.

**Häufige Fehler:**
- Vergessen, Leerzeichen zwischen Namen einzufügen: `vorname + nachname` (ergibt "AnnaSchmidt" statt "Anna Schmidt")
- Anführungszeichen vergessen bei Text: `name = Anna` statt `name = "Anna"`
- Variablenname falsch geschrieben: `vollständiger_name` vs `vollstaendiger_name`

</details>

+++

---

**Glückwunsch!** Sie haben Notebook 04 abgeschlossen und verstehen jetzt Variablen!

Im nächsten Notebook lernen Sie, welche verschiedenen **Arten von Werten** (Datentypen) es in Python gibt: Zahlen, Text, Wahrheitswerte und mehr!
