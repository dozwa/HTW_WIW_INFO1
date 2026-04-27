---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
kernelspec:
  display_name: base
  language: python
  name: python3
---

# 02 - Konsole: Ihre erste Unterhaltung mit dem Computer 💬

## Willkommen! 👋

Herzlich willkommen zu Ihrem zweiten Notebook! Heute lernen Sie, wie Sie mit dem Computer "sprechen" können. Stellen Sie sich vor, Sie hätten einen unsichtbaren Gesprächspartner, dem Sie Fragen stellen und der Ihnen antwortet - genau das werden Sie heute programmieren!

+++

## Was Sie heute lernen:

- Was die Konsole ist und warum sie wichtig ist
- Wie Sie mit `print()` Nachrichten ausgeben
- Wie Sie mit `input()` Benutzereingaben empfangen
- Wie Sie mit F-Strings elegante Ausgaben erstellen

## Voraussetzungen 📚

Was Sie schon können sollten:
- Grundverständnis von Programmiersprachen (aus Notebook 01)
- Wissen, was Python ist und wie ein Interpreter funktioniert
- Jupyter Notebooks bedienen können

**WICHTIG:** In diesem Notebook lernen wir NUR die Grundlagen der Konsolenkommunikation. Variablen, Datentypen und andere Konzepte kommen in späteren Notebooks!

+++

---

## 1. Was ist die Konsole? 🖥️

### Die Konsole als Kommunikationskanal

Stellen Sie sich vor, Sie sitzen in einem Raum mit einem Computer. Der Computer kann denken und rechnen, aber er kann nicht sprechen. Die einzige Möglichkeit, mit ihm zu kommunizieren, ist ein Textfeld auf dem Bildschirm - das ist die **Konsole**.

Die Konsole ist wie ein Chat-Fenster zwischen Ihnen und dem Computer. Sie können dort:
- **Nachrichten hineinschreiben** (das macht Ihr Programm mit Ausgaben)
- **Nachrichten herauslesen** (das machen Sie, wenn Sie die Ausgaben sehen)
- **Fragen stellen** (das macht Ihr Programm, wenn es Eingaben braucht)
- **Antworten geben** (das machen Sie, wenn Sie etwas eintippen)

### Warum ist die Konsole so wichtig?

Ohne die Konsole wäre ein Programm wie ein stummes Radio - es würde funktionieren, aber niemand könnte hören, was es zu sagen hat! Die Konsole ist das Sprachrohr Ihres Programms.

In der Praxis wird die Konsole verwendet für:
- **Testen von Code:** Sie können sehen, was Ihr Programm gerade macht
- **Fehlermeldungen:** Der Computer teilt Ihnen mit, wenn etwas nicht funktioniert
- **Benutzerinteraktion:** Einfache Programme können Fragen stellen und Antworten verarbeiten
- **Debugging:** Sie können Zwischenergebnisse anzeigen lassen

### Die Konsole in Python

Python bietet zwei grundlegende Funktionen für die Konsolenkommunikation:
1. `print()` - zum Ausgeben von Informationen
2. `input()` - zum Empfangen von Benutzereingaben

Diese beiden Funktionen sind Ihre ersten Werkzeuge, um mit dem Computer zu "sprechen". In den nächsten Abschnitten lernen Sie beide im Detail kennen.

+++

---

## 2. Ausgabe mit print() 🖨️

### Die print() Funktion verstehen

Stellen Sie sich vor, Sie möchten einem Freund etwas mitteilen. Sie öffnen Ihren Mund und sagen es laut - Ihr Freund hört es. Genau das macht die `print()` Funktion in Python: Sie ist wie der Mund Ihres Programms, der Nachrichten "ausspricht"!

Aber warum brauchen wir so etwas? Computer sind von Natur aus stumm. Sie rechnen im Hintergrund, denken, verarbeiten Daten - aber ohne `print()` würden wir nie erfahren, was sie dabei denken oder berechnen. Es wäre wie ein Taschenrechner ohne Display: Er rechnet vielleicht richtig, aber das Ergebnis bleibt unsichtbar.

Die `print()` Funktion nimmt das, was Sie ihr geben (Text, später auch Zahlen oder andere Dinge), und zeigt es auf dem Bildschirm an. Sie ist Ihre Kommunikationsbrücke zum Computer. Ohne sie wäre Programmieren wie ein Selbstgespräch im Dunkeln.

### Wie funktioniert print() technisch?

Wenn Sie `print()` verwenden, passiert Folgendes:
1. Python nimmt den Inhalt zwischen den Klammern `( )`
2. Es wandelt diesen Inhalt in Text um (falls nötig)
3. Es schreibt diesen Text in die Konsole
4. Es macht einen Zeilenumbruch (die nächste Ausgabe erscheint in einer neuen Zeile)

### Wann benutzt man print() in der Praxis?

Programmierer nutzen `print()` ständig:
- **Während der Entwicklung:** "Läuft mein Code überhaupt?"
- **Bei Fehlern:** "Welchen Wert hat diese Berechnung gerade?"
- **Für Benutzer:** "Hallo! Das Programm ist bereit."
- **Zur Bestätigung:** "Die Datei wurde erfolgreich gespeichert."

Es ist das wichtigste Werkzeug für die Kommunikation zwischen Programm und Mensch!

+++

### Beispiel 1: Die erste print()-Ausgabe

Beginnen wir mit dem absolut einfachsten Beispiel. Wir geben einen einzigen Satz aus:

```{code-cell} ipython3
# Unser erstes Programm: Eine einfache Begrüßung
print("Hallo, Welt!")
```

**Was ist hier passiert?**
- `print` ist der Name der Funktion (das Werkzeug)
- Die Klammern `()` sagen Python: "Führe diese Funktion aus!"
- `"Hallo, Welt!"` ist der Text (in Anführungszeichen!), der ausgegeben werden soll
- Python zeigt diesen Text in der Konsole an

**Wichtig:** Text muss IMMER in Anführungszeichen stehen! Sie können `"` oder `'` verwenden.

+++

### Beispiel 2: Mehrere Ausgaben hintereinander

Sie können `print()` so oft aufrufen, wie Sie möchten. Jeder Aufruf erzeugt eine neue Zeile:

```{code-cell} ipython3
# Mehrere Zeilen ausgeben
print("Willkommen bei Python!")
print("Dies ist Ihr erstes Programm.")
print("Jeder print()-Aufruf erzeugt eine neue Zeile.")
```

**Beobachtung:** Jede `print()`-Anweisung erscheint in einer neuen Zeile. Das ist das Standard-Verhalten.

+++

### Beispiel 3: Mehrere Texte in einer Ausgabe

Sie können auch mehrere Texte in einem einzigen `print()` ausgeben, indem Sie sie mit Kommas trennen:

```{code-cell} ipython3
# Mehrere Texte mit Komma getrennt
print("Guten", "Morgen", "zusammen!")
```

**Was passiert?** Python fügt automatisch Leerzeichen zwischen die Texte ein. Das Ergebnis: `Guten Morgen zusammen!`

+++

### Beispiel 4: Leere Zeilen für bessere Lesbarkeit

Manchmal möchten Sie Leerzeilen einfügen, um die Ausgabe übersichtlicher zu machen:

```{code-cell} ipython3
# Ausgabe mit Leerzeilen
print("Erste Zeile")
print("")  # Eine leere Zeile
print("Dritte Zeile")
```

**Trick:** `print("")` oder `print()` erzeugt eine leere Zeile.

+++

### 🏃 Mini-Übung: print() ausprobieren!

Jetzt sind Sie dran! Probieren Sie die `print()` Funktion selbst aus.

**Aufgabe 1:** Geben Sie Ihren Namen aus

```{code-cell} ipython3
# Ihr Code hier:
```

**Aufgabe 2:** Geben Sie drei verschiedene Begrüßungen aus (jede in einer eigenen Zeile)

```{code-cell} ipython3
# Ihr Code hier:
```

**Aufgabe 3:** Geben Sie einen Satz aus, der aus drei Teilen besteht (mit Kommas getrennt)

```{code-cell} ipython3
# Ihr Code hier:
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1:
print("Max Mustermann")

# Aufgabe 2:
print("Guten Morgen!")
print("Hallo!")
print("Willkommen!")

# Aufgabe 3:
print("Ich", "lerne", "Python!")
```
</details>

+++

---

## 3. Eingabe mit input() ⌨️

### Die input() Funktion verstehen

Sie haben gelernt, wie Ihr Programm "sprechen" kann mit `print()`. Aber was, wenn das Programm auch "zuhören" soll? Hier kommt `input()` ins Spiel!

Stellen Sie sich ein Gespräch vor. Sie fragen: "Wie heißen Sie?" - und dann warten Sie auf eine Antwort. Genau das macht `input()`: Es stellt eine Frage, wartet geduldig, bis der Benutzer etwas eintippt und Enter drückt, und nimmt dann diese Eingabe entgegen.

### Warum brauchen wir input()?

Programme, die nur ausgeben, sind wie einseitige Gespräche - der Computer redet, aber hört nicht zu. Das ist für viele Anwendungen zu starr. Wir wollen Programme, die:
- **Flexibel** sind: Unterschiedliche Benutzer, unterschiedliche Eingaben
- **Interaktiv** sind: Der Benutzer kann Entscheidungen treffen
- **Persönlich** sind: Das Programm kann auf den Benutzer eingehen

Beispiele aus dem echten Leben:
- Ein Login-System fragt nach Benutzername und Passwort
- Ein Taschenrechner fragt nach den Zahlen, die berechnet werden sollen
- Ein Bestellsystem fragt nach der gewünschten Pizza-Größe

### Wie funktioniert input() technisch?

Wenn Python auf `input()` stößt:
1. Es zeigt die Nachricht in den Klammern an (falls vorhanden)
2. Es wartet, bis der Benutzer etwas eintippt und Enter drückt
3. Es nimmt alles, was getippt wurde, als Text entgegen
4. Es gibt diesen Text zurück (mehr dazu in späteren Notebooks!)

**Wichtig für später:** `input()` liefert IMMER Text zurück, auch wenn Sie eine Zahl eingeben! (Das lernen wir in Notebook 05 genauer.)

+++

### Beispiel 1: Einfache Eingabe mit sofortiger Ausgabe

Das einfachste Beispiel: Wir fragen nach etwas und geben die Antwort direkt aus:

```{code-cell} ipython3
# Frage nach dem Namen und gebe die Antwort direkt aus
print(input("Wie heißen Sie? "))
```

**Was passiert hier?**
1. `input("Wie heißen Sie? ")` zeigt die Frage an und wartet
2. Sie tippen etwas ein (z.B. "Anna") und drücken Enter
3. `print()` gibt aus, was Sie eingegeben haben

**Achtung:** Dies ist ein verschachtelter Aufruf - `input()` ist INNERHALB von `print()`. Das ist für Anfänger verwirrend, deshalb zeigen wir gleich eine klarere Methode!

+++

### Beispiel 2: Eingabe mit Begrüßung

Oft möchten wir die Eingabe in eine freundliche Nachricht einbauen:

```{code-cell} ipython3
# Frage nach dem Namen
print("Wie heißen Sie?")
# Hinweis: Die Antwort können wir erst in Notebook 04 (Variablen) speichern!
# Für jetzt geben wir sie nur direkt aus:
print(input())
```

**Limitation:** Wir können die Eingabe hier nicht weiterverarbeiten, weil wir noch keine Variablen kennen. Das kommt in Notebook 04!

+++

### Beispiel 3: Mehrere Eingaben nacheinander

Sie können mehrere Fragen hintereinander stellen:

```{code-cell} ipython3
# Erste Frage
print("Frage 1: Wie heißen Sie?")
print(input())

# Zweite Frage
print("Frage 2: Woher kommen Sie?")
print(input())
```

**Beobachtung:** Jede Eingabe wird sofort ausgegeben, aber nicht gespeichert. Das Speichern lernen wir mit Variablen!

+++

### 🏃 Mini-Übung: input() ausprobieren!

Probieren Sie `input()` selbst aus!

**Aufgabe 1:** Fragen Sie nach einer Lieblingsfarbe und geben Sie die Antwort aus

```{code-cell} ipython3
# Ihr Code hier:
```

**Aufgabe 2:** Stellen Sie zwei Fragen nacheinander (z.B. Name und Alter)

```{code-cell} ipython3
# Ihr Code hier:
```

**Aufgabe 3:** Erstellen Sie einen "Mini-Dialog" mit drei Fragen

```{code-cell} ipython3
# Ihr Code hier:
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1:
print("Was ist Ihre Lieblingsfarbe?")
print(input())

# Aufgabe 2:
print("Wie heißen Sie?")
print(input())
print("Wie alt sind Sie?")
print(input())

# Aufgabe 3:
print("Wie heißen Sie?")
print(input())
print("Woher kommen Sie?")
print(input())
print("Was studieren Sie?")
print(input())
```
</details>

+++

---

## 4. F-String-Formatierung ✨

### Was sind F-Strings?

Sie haben gelernt, wie man Text ausgibt und Eingaben empfängt. Aber was, wenn Sie beides elegant kombinieren möchten? Hier kommen **F-Strings** (Formatted Strings) ins Spiel!

Stellen Sie sich vor, Sie schreiben einen Brief. Sie haben eine Vorlage: "Guten Tag, [NAME]!" - und Sie möchten [NAME] durch einen echten Namen ersetzen. Genau das machen F-Strings in Python: Sie erstellen Textvorlagen mit Platzhaltern, die dann durch echte Werte ersetzt werden.

### Warum sind F-Strings so praktisch?

Ohne F-Strings müssten wir Text umständlich zusammensetzen. Mit F-Strings können wir elegante, lesbare Ausgaben erstellen, die sich natürlich anfühlen. Vergleichen Sie:

**Ohne F-String (umständlich):**
```python
print("Hallo", "Max", "willkommen!")
```

**Mit F-String (elegant):**
```python
print(f"Hallo Max, willkommen!")
```

### Die Anatomie eines F-Strings

Ein F-String besteht aus:
1. Dem Buchstaben `f` oder `F` VOR den Anführungszeichen
2. Normalem Text
3. Geschweiften Klammern `{}` für Platzhalter
4. Inhalten innerhalb der geschweiften Klammern (das, was eingefügt werden soll)

Syntax: `f"Text {Platzhalter} mehr Text"`

### Wann benutzt man F-Strings?

F-Strings sind perfekt, wenn Sie:
- **Personalisierte Nachrichten** erstellen möchten
- **Mehrere Werte** in einem Text einbauen wollen
- **Lesbare Ausgaben** bevorzugen
- **Professionell wirkenden Code** schreiben möchten

**Wichtig:** Für die Beispiele hier nutzen wir F-Strings direkt mit Text. Die wahre Kraft zeigen F-Strings erst mit Variablen (Notebook 04)!

+++

### Beispiel 1: Einfacher F-String mit direktem Text

Der einfachste Fall - wir setzen einen Wert direkt in den Text ein:

```{code-cell} ipython3
# F-String mit einem Platzhalter
print(f"Willkommen bei {'Python'}!")
```

**Was passiert?**
- `f` vor dem String aktiviert die F-String-Formatierung
- `{'Python'}` wird durch das Wort Python ersetzt
- Ergebnis: `Willkommen bei Python!`

**Hinweis:** Dies ist noch nicht sehr nützlich, aber es zeigt das Grundprinzip!

+++

### Beispiel 2: F-String mit mehreren Platzhaltern

Sie können mehrere Platzhalter in einem F-String verwenden:

```{code-cell} ipython3
# F-String mit mehreren Platzhaltern
print(f"Hallo {'Anna'}, willkommen in {'München'}!")
```

**Beobachtung:** Jeder Platzhalter `{}` wird durch seinen Inhalt ersetzt. Der Rest bleibt unverändert.

+++

### Beispiel 3: F-String mit input() kombinieren

Jetzt wird es interessant! Wir kombinieren `input()` mit F-Strings für eine personalisierte Ausgabe:

```{code-cell} ipython3
# Eingabe direkt in F-String einbauen
print(f"Hallo {input('Wie heißen Sie? ')}, schön Sie kennenzulernen!")
```

**Das ist clever!**
- `input('Wie heißen Sie? ')` fragt nach dem Namen
- Die Antwort wird direkt in den F-String eingefügt
- `print()` gibt die komplette, personalisierte Nachricht aus

**Beispiel:**
- Eingabe: "Max"
- Ausgabe: "Hallo Max, schön Sie kennenzulernen!"

+++

### Beispiel 4: Komplexerer Dialog mit F-Strings

Lassen Sie uns einen kleinen Dialog erstellen:

```{code-cell} ipython3
# Dialog mit mehreren F-Strings
print(f"Guten Tag {input('Wie ist Ihr Vorname? ')}!")
print(f"Interessant, und Sie kommen aus {input('Aus welcher Stadt kommen Sie? ')}!")
print(f"Ah, {input('Was studieren Sie? ')} - ein spannendes Fach!")
```

**Beobachtung:** Jede Zeile:
1. Stellt eine Frage mit `input()`
2. Baut die Antwort in einen F-String ein
3. Gibt eine personalisierte Nachricht aus

Das fühlt sich schon wie ein echtes Gespräch an!

+++

### 🏃 Mini-Übung: F-Strings meistern!

Jetzt probieren Sie F-Strings aus!

**Aufgabe 1:** Erstellen Sie einen F-String, der nach Ihrer Lieblingsspeise fragt und diese in einen Satz einbaut

```{code-cell} ipython3
# Ihr Code hier:
```

**Aufgabe 2:** Erstellen Sie einen Dialog mit drei Fragen, die alle mit F-Strings personalisierte Antworten geben

```{code-cell} ipython3
# Ihr Code hier:
```

**Aufgabe 3:** Erstellen Sie eine "Vorstellungsrunde", die nach Name, Wohnort und Hobby fragt und alles in einem großen Satz zusammenfasst

```{code-cell} ipython3
# Ihr Code hier:
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1:
print(f"Mmh, {input('Was ist Ihre Lieblingsspeise? ')} klingt lecker!")

# Aufgabe 2:
print(f"Hallo {input('Wie heißen Sie? ')}!")
print(f"Aha, Sie sind also {input('Wie alt sind Sie? ')} Jahre alt!")
print(f"Und Sie arbeiten als {input('Was ist Ihr Beruf? ')} - interessant!")

# Aufgabe 3:
print(f"Also, {input('Wie heißen Sie? ')} aus {input('Woher kommen Sie? ')} hat als Hobby {input('Was ist Ihr Hobby? ')} - super!")
```
</details>

+++

---

## 5. Zusammenfassung 🎓

### Was Sie gelernt haben:

- ✅ **Die Konsole** ist Ihr Kommunikationskanal zum Computer
- ✅ **print()** gibt Nachrichten in der Konsole aus (der "Mund" des Programms)
- ✅ **input()** empfängt Benutzereingaben (das "Ohr" des Programms)
- ✅ **F-Strings** (`f"...{...}..."`) ermöglichen elegante, formatierte Ausgaben
- ✅ Sie können Ausgaben und Eingaben kombinieren für interaktive Programme

### Die wichtigsten Konzepte:

```python
# Ausgabe
print("Hallo")

# Eingabe
input("Frage? ")

# F-String
print(f"Text {wert} mehr Text")

# Kombination
print(f"Hallo {input('Name? ')}!")
```

### Wichtige Einschränkung:

In diesem Notebook konnten wir Eingaben noch nicht **speichern** und **weiterverarbeiten**. Dafür brauchen wir **Variablen**, die Sie in Notebook 04 lernen werden. Dann werden die Möglichkeiten noch viel größer!

### Nächste Schritte:

Im nächsten Notebook (03 - Kommentare) lernen Sie, wie Sie Ihren Code dokumentieren und für andere (und für sich selbst!) verständlicher machen.

+++

---

## 6. Trainingsmaterial 💪

Zeit, Ihr neues Wissen zu festigen! Die Aufgaben sind in drei Schwierigkeitsstufen unterteilt.

+++

### 🟢 Einfache Aufgaben (zum Warmwerden)

**Aufgabe 1:** Begrüßungsprogramm

Erstellen Sie ein Programm, das "Guten Morgen!", "Wie geht es Ihnen?" und "Schön, Sie zu sehen!" in drei separaten Zeilen ausgibt.

```{code-cell} ipython3
# Aufgabe 1: Ihr Code hier
```

**Aufgabe 2:** Echo-Programm

Schreiben Sie ein Programm, das Sie nach einem Wort fragt und dieses Wort dann ausgibt.

```{code-cell} ipython3
# Aufgabe 2: Ihr Code hier
```

**Aufgabe 3:** Personalisierte Begrüßung

Erstellen Sie ein Programm, das nach Ihrem Namen fragt und dann sagt: "Hallo [NAME], herzlich willkommen!"

```{code-cell} ipython3
# Aufgabe 3: Ihr Code hier
```

### 🟡 Mittlere Aufgaben (schon besser!)

**Aufgabe 4:** Mini-Interview

Erstellen Sie ein Programm, das nacheinander nach drei Dingen fragt:
1. Name
2. Lieblingsfarbe
3. Lieblingsjahreszeit

Geben Sie nach jeder Eingabe eine passende Reaktion aus (z.B. "Schöner Name!", "Tolle Farbe!", "Mag ich auch!").

```{code-cell} ipython3
# Aufgabe 4: Ihr Code hier
```

**Aufgabe 5:** Restaurant-Bestellung

Simulieren Sie eine Restaurant-Bestellung:
1. Fragen Sie nach dem Namen des Gastes
2. Fragen Sie nach der gewünschten Vorspeise
3. Fragen Sie nach dem Hauptgericht
4. Fragen Sie nach dem Getränk

Geben Sie am Ende eine Zusammenfassung aus: "Alles klar, [NAME]! Sie bekommen [VORSPEISE], [HAUPTGERICHT] und [GETRÄNK]. Guten Appetit!"

```{code-cell} ipython3
# Aufgabe 5: Ihr Code hier
```

### 🔴 Herausforderungen (für Profis)

**Aufgabe 6:** Kreative Geschichte

Erstellen Sie ein Programm, das eine kleine Geschichte erzählt und dabei den Benutzer nach fehlenden Wörtern fragt. Zum Beispiel:

```
Es war einmal ein [Adjektiv] [Tier], das in [Ort] lebte.
Eines Tages fand es einen [Gegenstand] und war sehr [Emotion].
Das [Tier] beschloss, [Aktivität] zu gehen.
Und wenn sie nicht gestorben sind, dann [Aktivität] sie noch heute!
```

Hinweise:
- Fragen Sie nacheinander nach allen benötigten Wörtern
- Verwenden Sie F-Strings, um die Geschichte zusammenzusetzen
- Seien Sie kreativ mit der Geschichte!

```{code-cell} ipython3
# Aufgabe 6: Ihr Code hier
```

---

## Musterlösungen

Versuchen Sie erst selbst, die Aufgaben zu lösen! Die Lösungen finden Sie unten.

+++

<details>
<summary>🔍 Lösung Aufgabe 1: Begrüßungsprogramm</summary>

```python
# 📝 Aufgabe: Drei Begrüßungen ausgeben

# 💭 Überlegung:
# - Wir brauchen drei separate print()-Aufrufe
# - Jeder print()-Aufruf erzeugt eine neue Zeile

# 💻 Lösung:
print("Guten Morgen!")
print("Wie geht es Ihnen?")
print("Schön, Sie zu sehen!")

# 🎯 Erklärung:
# Zeile 1: Gibt "Guten Morgen!" aus
# Zeile 2: Gibt "Wie geht es Ihnen?" in neuer Zeile aus
# Zeile 3: Gibt "Schön, Sie zu sehen!" in neuer Zeile aus

# ⚠️ Häufige Fehler:
# - Anführungszeichen vergessen → SyntaxError
# - Alles in einem print() → erscheint in einer Zeile
```
</details>

+++

<details>
<summary>🔍 Lösung Aufgabe 2: Echo-Programm</summary>

```python
# 📝 Aufgabe: Nach einem Wort fragen und es ausgeben

# 💭 Überlegung:
# - input() fragt nach Eingabe
# - print() gibt die Eingabe direkt aus

# 💻 Lösung:
print("Sagen Sie ein Wort:")
print(input())

# Alternative (kürzer):
print(input("Sagen Sie ein Wort: "))

# 🎯 Erklärung:
# Version 1: Zwei separate Schritte - erst Frage, dann Eingabe und Ausgabe
# Version 2: Alles in einer Zeile - input() ist in print() verschachtelt

# ⚠️ Häufige Fehler:
# - input() ohne print() → Eingabe verschwindet
# - Verschachtelung verwirrt Anfänger
```
</details>

+++

<details>
<summary>🔍 Lösung Aufgabe 3: Personalisierte Begrüßung</summary>

```python
# 📝 Aufgabe: Nach Namen fragen und personalisiert begrüßen

# 💭 Überlegung:
# - Wir brauchen input() für den Namen
# - Wir brauchen einen F-String für die personalisierte Ausgabe
# - Der Name soll direkt in den Text eingebaut werden

# 💻 Lösung:
print(f"Hallo {input('Wie heißen Sie? ')}, herzlich willkommen!")

# 🎯 Erklärung:
# - input('Wie heißen Sie? ') zeigt die Frage und wartet auf Eingabe
# - Die Eingabe wird in die geschweiften Klammern {} eingefügt
# - print() gibt den kompletten, personalisierten Text aus

# Beispiel-Ablauf:
# Eingabe: "Anna"
# Ausgabe: "Hallo Anna, herzlich willkommen!"

# ⚠️ Häufige Fehler:
# - Das 'f' vor dem String vergessen → {} wird nicht ersetzt
# - Geschweifte Klammern vergessen → input() erscheint als Text
```
</details>

+++

<details>
<summary>🔍 Lösung Aufgabe 4: Mini-Interview</summary>

```python
# 📝 Aufgabe: Drei Fragen stellen mit passenden Reaktionen

# 💭 Überlegung:
# - Wir brauchen drei separate Eingaben
# - Nach jeder Eingabe eine positive Reaktion
# - F-Strings für personalisierte Reaktionen

# 💻 Lösung:
print(f"Hallo {input('Wie heißen Sie? ')} - schöner Name!")
print(f"{input('Was ist Ihre Lieblingsfarbe? ')} ist eine tolle Farbe!")
print(f"{input('Was ist Ihre Lieblingsjahreszeit? ')} mag ich auch sehr!")

# 🎯 Erklärung:
# Zeile 1: Fragt nach Namen, baut ihn in Begrüßung ein
# Zeile 2: Fragt nach Farbe, reagiert positiv
# Zeile 3: Fragt nach Jahreszeit, stimmt zu

# Beispiel-Ablauf:
# Eingabe 1: "Max"
# Ausgabe 1: "Hallo Max - schöner Name!"
# Eingabe 2: "Blau"
# Ausgabe 2: "Blau ist eine tolle Farbe!"
# Eingabe 3: "Sommer"
# Ausgabe 3: "Sommer mag ich auch sehr!"

# ⚠️ Häufige Fehler:
# - Vergessen, jede Zeile als F-String zu markieren (f"...")
# - input() außerhalb der geschweiften Klammern platzieren
```
</details>

+++

<details>
<summary>🔍 Lösung Aufgabe 5: Restaurant-Bestellung</summary>

```python
# 📝 Aufgabe: Restaurant-Bestellung simulieren

# 💭 Überlegung:
# - Vier Eingaben nacheinander (Name, Vorspeise, Hauptgericht, Getränk)
# - Alle Eingaben in einer Abschluss-Nachricht zusammenfassen
# - Problem: Wir können die Eingaben nicht speichern (keine Variablen!)
# - Lösung: Alles in einer langen Zeile mit verschachtelten input()-Aufrufen

# 💻 Lösung:
print("Willkommen im Restaurant Python!")
print("")
print(f"Alles klar, {input('Wie ist Ihr Name? ')}! Sie bekommen {input('Welche Vorspeise möchten Sie? ')}, {input('Welches Hauptgericht möchten Sie? ')} und {input('Was möchten Sie trinken? ')}. Guten Appetit!")

# 🎯 Erklärung:
# Zeile 1-2: Begrüßung mit Leerzeile
# Zeile 3: Komplexer F-String mit vier verschachtelten input()-Aufrufen
#   - Erster input(): Name
#   - Zweiter input(): Vorspeise
#   - Dritter input(): Hauptgericht
#   - Vierter input(): Getränk
#   - Alle werden direkt in den Text eingefügt

# Beispiel-Ablauf:
# "Wie ist Ihr Name?" → "Anna"
# "Welche Vorspeise möchten Sie?" → "Salat"
# "Welches Hauptgericht möchten Sie?" → "Pizza"
# "Was möchten Sie trinken?" → "Wasser"
# Ausgabe: "Alles klar, Anna! Sie bekommen Salat, Pizza und Wasser. Guten Appetit!"

# ⚠️ Häufige Fehler:
# - Zu viele Klammern vergessen zu schließen
# - Kommas zwischen den Teilen vergessen
# - Das 'f' vor dem String vergessen

# 💡 Hinweis:
# Diese Lösung ist kompliziert, weil wir keine Variablen verwenden können!
# Ab Notebook 04 wird das viel einfacher und lesbarer!
```
</details>

+++

<details>
<summary>🔍 Lösung Aufgabe 6: Kreative Geschichte</summary>

```python
# 📝 Aufgabe: Interaktive Geschichte erstellen

# 💭 Überlegung:
# - Geschichte hat mehrere Platzhalter
# - Wir brauchen viele input()-Aufrufe
# - Ohne Variablen müssen alle inputs in einem F-String sein
# - Das wird lang, aber es funktioniert!

# 💻 Lösung:
print("Willkommen beim Geschichten-Generator!")
print("Beantworten Sie die Fragen und erleben Sie Ihre eigene Geschichte.")
print("")

print(f"Es war einmal ein {input('Adjektiv (z.B. mutiger, kleiner, lustiger): ')} {input('Tier (z.B. Hund, Katze, Drache): ')}, das in {input('Ort (z.B. einem Wald, einer Stadt, einem Schloss): ')} lebte. Eines Tages fand es einen {input('Gegenstand (z.B. Schatz, Schlüssel, Zauberstab): ')} und war sehr {input('Emotion (z.B. glücklich, überrascht, ängstlich): ')}. Das Tier beschloss, {input('Aktivität (z.B. tanzen, singen, springen): ')} zu gehen. Und wenn sie nicht gestorben sind, dann {input('Aktivität (z.B. tanzen, lachen, schlafen): ')} sie noch heute!")

print("")
print("Ende der Geschichte. Danke fürs Mitmachen!")

# 🎯 Erklärung:
# Zeile 1-3: Einleitung und Erklärung
# Zeile 5: Komplexer F-String mit 8 verschachtelten input()-Aufrufen:
#   1. Adjektiv für das Tier
#   2. Tierart
#   3. Wohnort
#   4. Gefundener Gegenstand
#   5. Emotion beim Finden
#   6. Erste Aktivität
#   7. Zweite Aktivität (für das Ende)
# Zeile 7-8: Abschluss

# Beispiel-Ablauf:
# Adjektiv: "mutiger"
# Tier: "Drache"
# Ort: "einem Schloss"
# Gegenstand: "Schatz"
# Emotion: "glücklich"
# Aktivität 1: "tanzen"
# Aktivität 2: "feiern"
#
# Ausgabe:
# "Es war einmal ein mutiger Drache, das in einem Schloss lebte. 
#  Eines Tages fand es einen Schatz und war sehr glücklich. 
#  Das Tier beschloss, tanzen zu gehen. 
#  Und wenn sie nicht gestorben sind, dann feiern sie noch heute!"

# ⚠️ Häufige Fehler:
# - Zu viele verschachtelte Klammern → schnell den Überblick verlieren
# - Anführungszeichen nicht richtig geschlossen
# - Das 'f' vergessen → Geschichte wird nicht zusammengesetzt

# 💡 Hinweis:
# Dies ist eine fortgeschrittene Übung! 
# Wenn Sie das hinbekommen, verstehen Sie print(), input() und F-Strings sehr gut!
# Ab Notebook 04 (Variablen) wird so etwas viel übersichtlicher.
```
</details>

+++

---

## Glückwunsch! 🎉

Sie haben Notebook 02 erfolgreich abgeschlossen! Sie können jetzt:
- Mit dem Computer über die Konsole kommunizieren
- Ausgaben mit `print()` erstellen
- Eingaben mit `input()` empfangen
- Elegante Texte mit F-Strings formatieren

Im nächsten Notebook lernen Sie, wie Sie Ihren Code mit **Kommentaren** dokumentieren und verständlicher machen. Bis bald! 👋
