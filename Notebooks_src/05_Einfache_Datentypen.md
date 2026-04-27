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

# 05 - Einfache Datentypen: Die Sprache der Daten verstehen 🎯

## Willkommen! 👋

Herzlich willkommen zu Ihrer fünften Lerneinheit! Bisher haben Sie gelernt, wie Sie mit der Konsole kommunizieren, Ihren Code dokumentieren und Informationen in Variablen speichern können. Aber was genau können wir in diesen "Schubladen" (Variablen) eigentlich ablegen?

In diesem Notebook lernen Sie die grundlegenden **Datentypen** kennen - die verschiedenen "Arten" von Informationen, mit denen Python arbeiten kann. Dies ist ein fundamentaler Baustein der Programmierung!

## Was Sie heute lernen:
- Was Datentypen sind und warum sie wichtig sind
- Wie Sie mit Texten (Strings) arbeiten
- Wie Sie ganze Zahlen (Integer) verwenden
- Wie Sie Zahlen mit Dezimalstellen (Float) einsetzen
- Wie Sie Wahrheitswerte (Boolean) nutzen
- Wie Sie zwischen verschiedenen Datentypen umwandeln

## Voraussetzungen 📚
Was Sie bereits können sollten:
- Mit `print()` Ausgaben auf der Konsole erzeugen (Notebook 02)
- Mit `input()` Benutzereingaben entgegennehmen (Notebook 02)
- Kommentare schreiben mit `#` (Notebook 03)
- Variablen erstellen und Werte zuweisen (Notebook 04)

---

+++

## 1. Daten und Datentypen verstehen 🧩

### Was sind Daten überhaupt?

Stellen Sie sich vor, Sie organisieren Ihr Büro. Sie haben verschiedene Arten von Gegenständen: Dokumente, Ordner, Stifte, Taschenrechner. Jeder Gegenstand hat einen bestimmten Zweck und wird auf eine spezielle Art verwendet. Genau so verhält es sich mit Daten in der Programmierung!

In der Welt der Programmierung sind **Daten die Grundbausteine**, mit denen wir arbeiten. Sie repräsentieren Informationen, die in einem Computerprogramm verarbeitet, manipuliert und gespeichert werden. Daten können vielfältige Formen annehmen - von einfachen Zahlen und Texten bis hin zu komplexeren Informationen.

+++

### Was sind Datentypen?

Nun stellen Sie sich vor, Sie sortieren Ihre Post: Briefe kommen in einen Ordner, Rechnungen in einen anderen, Zeitschriften auf einen Stapel. Sie behandeln jeden Typ unterschiedlich, weil sie verschiedene Eigenschaften haben.

**Datentypen** sind genau das - sie definieren die **Art der Daten**, die in einer Programmiersprache verwendet werden können. Sie bestimmen:
- Welche Werte eine Variable annehmen kann
- Wie viel Speicherplatz benötigt wird
- Welche Operationen damit durchgeführt werden können

Python kennt verschiedene grundlegende Datentypen:
- **String** (Zeichenketten): Für Texte wie "Hallo Welt"
- **Integer** (Ganzzahlen): Für ganze Zahlen wie 42 oder -7
- **Float** (Gleitkommazahlen): Für Zahlen mit Dezimalstellen wie 3.14 oder -0.5
- **Boolean** (Wahrheitswerte): Für wahr (True) oder falsch (False)

+++

### Warum ist die Unterscheidung von Datentypen wichtig?

Die Frage ist berechtigt: Warum kann Python nicht einfach alles als "Daten" behandeln? Die Antwort liegt in mehreren wichtigen Gründen:

**1. Speicherverwaltung:** Stellen Sie sich vor, Sie packen für eine Reise. Ein T-Shirt braucht weniger Platz als ein dicker Wintermantel. Genauso benötigen unterschiedliche Datentypen unterschiedliche Mengen an Speicherplatz. Eine einzelne Zahl braucht weniger Speicher als ein ganzer Roman. Die Kenntnis des Datentyps ermöglicht es dem Computer, Speicher effizient zu verwalten.

**2. Fehlervermeidung:** Würden Sie versuchen, Äpfel mit Kilometern zu addieren? Natürlich nicht - das ergibt keinen Sinn! Genauso verhindert die Unterscheidung von Datentypen unsinnige Operationen. Wenn Sie versuchen, einen Text mit einer Zahl zu "multiplizieren", warnt Sie Python, dass das nicht funktioniert.

**3. Klarheit und Verständlichkeit:** Wenn Sie in Ihrem Code sehen, dass eine Variable ein String ist, wissen Sie sofort: "Hier arbeite ich mit Text". Das macht Programme leichter verständlich und wartbar - besonders wenn andere Personen Ihren Code lesen oder Sie nach einigen Monaten zurückkehren.

**4. Korrekte Verarbeitung:** Denken Sie an das Pluszeichen (+). Bei Zahlen bedeutet es "addieren" (2 + 3 = 5), bei Texten bedeutet es "aneinanderhängen" ("Hallo" + "Welt" = "HalloWelt"). Python muss wissen, mit welchem Datentyp es arbeitet, um die richtige Operation auszuführen!

+++

### Ein häufiger Fehler: Zahlen als Text

Schauen wir uns ein typisches Problem an, das entsteht, wenn man Datentypen nicht beachtet. Im folgenden Beispiel sehen Sie, was passieren kann:

```{code-cell} ipython3
# Beispiel: Was passiert, wenn Zahlen als Text gespeichert werden?
zahl1 = "5"  # Dies ist KEIN Zahl, sondern Text!
zahl2 = "3"  # Auch dies ist Text!

# Was erwarten Sie als Ergebnis?
print(zahl1)
print(zahl2)
```

**Erklärung:** Sieht aus wie Zahlen, oder? Aber die Anführungszeichen machen daraus Text! Python behandelt "5" wie jeden anderen Text, etwa wie "Hallo".

+++

### Die type() Funktion - Ihr Datentyp-Detektor 🔍

Python bietet eine eingebaute Funktion, mit der Sie jederzeit herausfinden können, welchen Datentyp eine Variable oder ein Wert hat: die `type()` Funktion.

Stellen Sie sich `type()` wie ein Etikettenlesegerät vor: Sie zeigen darauf, und es sagt Ihnen, was Sie in der Hand halten.

```{code-cell} ipython3
# Die type() Funktion zeigt uns den Datentyp
zahl_als_text = "5"
echte_zahl = 5

# Lassen Sie uns den Datentyp überprüfen
print(type(zahl_als_text))  # Was wird hier angezeigt?
print(type(echte_zahl))     # Und hier?
```

**Erklärung:** Die Ausgabe zeigt:
- `<class 'str'>` bedeutet: Dies ist ein String (Text)
- `<class 'int'>` bedeutet: Dies ist ein Integer (Ganzzahl)

Das Wort "class" können Sie vorerst ignorieren - wichtig ist der Teil danach (str, int, etc.).

+++

### 🏃 Sofort ausprobieren!

**Aufgabe 1:** Erstellen Sie eine Variable mit Ihrem Namen und überprüfen Sie den Datentyp

```{code-cell} ipython3
# Ihr Code hier:
# Erstellen Sie eine Variable "mein_name" mit Ihrem Namen


# Geben Sie den Datentyp mit type() aus
```

**Aufgabe 2:** Erstellen Sie eine Variable mit einer Zahl und überprüfen Sie den Datentyp

```{code-cell} ipython3
# Ihr Code hier:
# Erstellen Sie eine Variable "mein_alter" mit einer Zahl


# Geben Sie den Datentyp mit type() aus
```

**Aufgabe 3:** Experimentieren Sie - was ist der Datentyp von "123"?

```{code-cell} ipython3
# Ihr Code hier:
# Überprüfen Sie den Datentyp von "123" (mit Anführungszeichen)
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1:
mein_name = "Anna Müller"
print(type(mein_name))  # Ergebnis: <class 'str'>

# Aufgabe 2:
mein_alter = 25
print(type(mein_alter))  # Ergebnis: <class 'int'>

# Aufgabe 3:
print(type("123"))  # Ergebnis: <class 'str'> - Es ist Text, keine Zahl!
```
</details>

+++

---

## 2. String - Arbeiten mit Text 📝

### Was ist ein String?

Stellen Sie sich einen String wie eine Perlenkette vor: Jede Perle ist ein Buchstabe, eine Ziffer oder ein Sonderzeichen. Aufgereiht ergeben sie ein Wort, einen Satz oder einen ganzen Text.

Ein **String** (auf Deutsch: Zeichenkette) ist eine Folge von Zeichen, die als Text interpretiert wird. Strings können enthalten:
- Buchstaben: "Hallo"
- Zahlen als Text: "12345" (Achtung: Das sind keine Zahlen zum Rechnen!)
- Sonderzeichen: "!@#$%"
- Leerzeichen: "Ein ganzer Satz mit Leerzeichen"
- Sogar nichts: "" (ein leerer String)

+++

### Wie erstellt man einen String?

In Python wird ein String erstellt, indem man Text in Anführungszeichen setzt. Sie können dabei entweder einfache Anführungszeichen (`'`) oder doppelte Anführungszeichen (`"`) verwenden - beide funktionieren gleich!

**Wichtig:** Die Anführungszeichen am Anfang und am Ende müssen vom gleichen Typ sein. Sie können nicht mit `'` beginnen und mit `"` enden.

**Warum gibt es zwei Arten von Anführungszeichen?** Das ist praktisch, wenn Ihr Text selbst Anführungszeichen enthalten soll:
- "Er sagte: 'Hallo!'" funktioniert
- 'Sie antwortete: "Guten Tag!"' funktioniert auch

```{code-cell} ipython3
# Strings mit doppelten Anführungszeichen
name = "Alice"
print(name)
```

```{code-cell} ipython3
# Strings mit einfachen Anführungszeichen
gruss = 'Hallo, wie geht es Ihnen?'
print(gruss)
```

```{code-cell} ipython3
# Strings können Anführungszeichen enthalten
zitat = "Er sagte: 'Das ist interessant!'"
print(zitat)
```

```{code-cell} ipython3
# Ein leerer String (enthält nichts)
leer = ""
print(leer)
print("Der String ist leer!")
```

### ACHTUNG: Zahlen in Anführungszeichen sind Text!

Dies ist eine der häufigsten Fehlerquellen für Programmieranfänger: Wenn Sie eine Zahl in Anführungszeichen setzen, wird sie zu Text und kann nicht mehr für Berechnungen verwendet werden!

```{code-cell} ipython3
# Dies ist KEINE Zahl, sondern Text!
nummer = "123"
print(nummer)
print(type(nummer))  # Zeigt: <class 'str'>
```

### 🏃 Sofort ausprobieren!

**Aufgabe 1:** Erstellen Sie einen String mit Ihrer Lieblingsfarbe und geben Sie ihn aus

```{code-cell} ipython3
# Ihr Code hier:
# Erstellen Sie eine Variable "lieblingsfarbe"


# Geben Sie sie aus
```

**Aufgabe 2:** Erstellen Sie einen String mit einem Satz, der Anführungszeichen enthält

```{code-cell} ipython3
# Ihr Code hier:
# Erstellen Sie einen String wie: Sie sagte: "Guten Morgen!"
```

**Aufgabe 3:** Überprüfen Sie den Datentyp der Zahl "999" in Anführungszeichen

```{code-cell} ipython3
# Ihr Code hier:
# Speichern Sie "999" in einer Variable und prüfen Sie den Typ
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1:
lieblingsfarbe = "Blau"
print(lieblingsfarbe)

# Aufgabe 2:
satz = "Sie sagte: 'Guten Morgen!'"
print(satz)
# Alternative:
satz2 = 'Er antwortete: "Guten Tag!"'
print(satz2)

# Aufgabe 3:
zahl_als_text = "999"
print(type(zahl_als_text))  # Ergebnis: <class 'str'>
```
</details>

+++

### Strings mit input() verwenden

Sie erinnern sich an die `input()` Funktion aus Notebook 02? Eine wichtige Information: `input()` liefert **immer** einen String zurück, egal was der Benutzer eingibt!

Selbst wenn der Benutzer eine Zahl eintippt, behandelt Python sie als Text. Das werden wir später mit der Typkonvertierung lösen.

```{code-cell} ipython3
# input() gibt immer einen String zurück
eingabe = input("Geben Sie etwas ein: ")
print("Sie haben eingegeben:")
print(eingabe)
print("Der Datentyp ist:")
print(type(eingabe))
```

### Umwandeln in einen String: Die str() Funktion

Manchmal haben Sie einen Wert, der kein String ist (zum Beispiel eine Zahl), und möchten ihn in Text umwandeln. Dafür gibt es die `str()` Funktion.

Stellen Sie sich `str()` wie einen Übersetzer vor: Sie geben ihm etwas, und er macht Text daraus.

```{code-cell} ipython3
# Eine Zahl in einen String umwandeln
zahl = 42
print("Vor der Umwandlung:")
print(type(zahl))
```

```{code-cell} ipython3
# Jetzt wandeln wir sie um
zahl = 42
zahl_als_text = str(zahl)
print("Nach der Umwandlung:")
print(type(zahl_als_text))
```

```{code-cell} ipython3
# Die Variable sieht gleich aus, ist aber jetzt Text
zahl = 42
zahl_als_text = str(zahl)
print(zahl_als_text)  # Sieht aus wie eine Zahl, ist aber Text!
```

### 🏃 Sofort ausprobieren!

**Aufgabe 1:** Wandeln Sie die Zahl 2025 in einen String um

```{code-cell} ipython3
# Ihr Code hier:
jahr = 2025
# Wandeln Sie jahr in einen String um und speichern Sie es in jahr_text


# Überprüfen Sie den Datentyp
```

**Aufgabe 2:** Fragen Sie den Benutzer nach seinem Namen und geben Sie eine Begrüßung aus

```{code-cell} ipython3
# Ihr Code hier:
# Fragen Sie nach dem Namen mit input()


# Geben Sie eine Begrüßung aus
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1:
jahr = 2025
jahr_text = str(jahr)
print(type(jahr_text))  # <class 'str'>
print(jahr_text)

# Aufgabe 2:
name = input("Wie ist Ihr Name? ")
print("Hallo")
print(name)
print("Willkommen!")
```
</details>

+++

---

## 3. Integer - Ganze Zahlen 🔢

### Was ist ein Integer?

Stellen Sie sich vor, Sie zählen Äpfel in einem Korb. Sie können 1, 2, 3 oder 10 Äpfel haben - aber niemals 2,5 Äpfel (es sei denn, Sie schneiden einen durch). Genau solche ganzen Zahlen sind Integer!

Ein **Integer** (auf Deutsch: Ganzzahl) ist ein Datentyp, der ganze Zahlen ohne Dezimalstellen repräsentiert. Integer können sein:
- Positive Zahlen: 1, 42, 1000
- Negative Zahlen: -5, -100, -999
- Die Null: 0

+++

### Wann verwendet man Integer?

Integer verwenden wir für Dinge, die nur in ganzen Einheiten existieren:
- Alter von Personen (25 Jahre, nicht 25,3 Jahre)
- Anzahl von Gegenständen (7 Bücher, nicht 7,2 Bücher)
- Hausnummern (Hausnummer 42, nicht 42,5)
- Jahre (2025, nicht 2025,3)

**Wichtig:** In Python schreiben Sie Integer OHNE Anführungszeichen und OHNE Dezimalpunkt. Sobald Sie einen Punkt schreiben (z.B. 5.0), wird daraus ein Float (dazu später mehr).

```{code-cell} ipython3
# Ein einfacher Integer
alter = 25
print(alter)
print(type(alter))
```

```{code-cell} ipython3
# Negative Integer sind auch erlaubt
temperatur = -5
print(temperatur)
print("Grad Celsius")
```

```{code-cell} ipython3
# Die Null ist auch ein Integer
kontostand = 0
print(kontostand)
print(type(kontostand))
```

### Umwandeln in einen Integer: Die int() Funktion

Erinnern Sie sich: `input()` gibt immer einen String zurück. Wenn Sie eine Zahl vom Benutzer abfragen wollen, mit der Sie später arbeiten möchten, müssen Sie den String in einen Integer umwandeln.

Dafür gibt es die `int()` Funktion. Sie versucht, einen String in eine Ganzzahl umzuwandeln.

**Wichtig:** Der String muss eine gültige Ganzzahl enthalten, sonst gibt es einen Fehler!
- `int("25")` funktioniert ✓
- `int("Hallo")` funktioniert NICHT ✗
- `int("25.5")` funktioniert NICHT ✗ (Dezimalzahlen sind keine Integer)

```{code-cell} ipython3
# String in Integer umwandeln
zahl_als_text = "42"
print("Vor der Umwandlung:")
print(type(zahl_als_text))
```

```{code-cell} ipython3
# Jetzt wandeln wir um
zahl_als_text = "42"
zahl = int(zahl_als_text)
print("Nach der Umwandlung:")
print(type(zahl))
```

```{code-cell} ipython3
# Praktisches Beispiel: Benutzereingabe in Integer umwandeln
alter_text = input("Wie alt sind Sie? ")
print("Vor der Umwandlung ist es ein:")
print(type(alter_text))
```

```{code-cell} ipython3
# Fortsetzung des Beispiels
alter_text = input("Wie alt sind Sie? ")
alter = int(alter_text)
print("Nach der Umwandlung ist es ein:")
print(type(alter))
print("Sie sind")
print(alter)
print("Jahre alt")
```

### 🏃 Sofort ausprobieren!

**Aufgabe 1:** Erstellen Sie eine Variable mit der Anzahl Ihrer Geschwister

```{code-cell} ipython3
# Ihr Code hier:
# Erstellen Sie eine Variable "anzahl_geschwister"


# Geben Sie sie aus


# Überprüfen Sie den Datentyp
```

**Aufgabe 2:** Wandeln Sie den String "100" in einen Integer um

```{code-cell} ipython3
# Ihr Code hier:
zahl_text = "100"
# Wandeln Sie zahl_text in einen Integer um


# Überprüfen Sie den neuen Datentyp
```

**Aufgabe 3:** Fragen Sie den Benutzer nach seinem Geburtsjahr und wandeln Sie die Eingabe in einen Integer um

```{code-cell} ipython3
# Ihr Code hier:
# Fragen Sie nach dem Geburtsjahr


# Wandeln Sie die Eingabe in einen Integer um


# Geben Sie das Ergebnis aus
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1:
anzahl_geschwister = 2
print(anzahl_geschwister)
print(type(anzahl_geschwister))  # <class 'int'>

# Aufgabe 2:
zahl_text = "100"
zahl = int(zahl_text)
print(type(zahl))  # <class 'int'>

# Aufgabe 3:
geburtsjahr_text = input("In welchem Jahr wurden Sie geboren? ")
geburtsjahr = int(geburtsjahr_text)
print("Sie wurden geboren im Jahr:")
print(geburtsjahr)
print(type(geburtsjahr))  # <class 'int'>
```
</details>

+++

---

## 4. Float - Gleitkommazahlen 🎯

### Was ist ein Float?

Stellen Sie sich vor, Sie messen Ihre Körpergröße: 1,75 Meter. Oder Sie tanken Benzin: 45,8 Liter. Oder Sie berechnen einen Durchschnitt: 3,14. All diese Zahlen haben Dezimalstellen - und genau dafür sind Floats da!

Ein **Float** (auf Deutsch: Gleitkommazahl oder Fließkommazahl) stellt Zahlen mit Dezimalstellen dar. Der Name "Gleitkomma" kommt daher, dass der Dezimalpunkt "gleiten" kann - die Zahl kann sehr groß oder sehr klein sein.

**Wichtig in Python:** Während wir in Deutschland das Komma verwenden (3,14), verwendet Python wie in der englischen Sprache einen **Punkt** als Dezimaltrennzeichen (3.14)!

+++

### Wann verwendet man Float?

Floats verwenden wir für Messungen und Berechnungen, die Genauigkeit erfordern:
- Körpergröße: 1.75 (Meter)
- Gewicht: 68.5 (Kilogramm)
- Temperatur: 22.3 (Grad Celsius)
- Preise: 19.99 (Euro)
- Mathematische Konstanten: 3.14159 (Pi)

**Wichtig:** Sobald eine Zahl einen Punkt hat, ist sie ein Float - selbst 5.0 ist ein Float, nicht ein Integer!

```{code-cell} ipython3
# Ein einfacher Float
koerpergroesse = 1.75
print(koerpergroesse)
print(type(koerpergroesse))
```

```{code-cell} ipython3
# Auch negative Floats sind möglich
temperatur = -3.5
print(temperatur)
print("Grad Celsius")
```

```{code-cell} ipython3
# Selbst mit .0 ist es ein Float, kein Integer!
zahl = 5.0
print(zahl)
print(type(zahl))  # Zeigt <class 'float'> nicht <class 'int'>!
```

```{code-cell} ipython3
# Die Zahl Pi mit vielen Dezimalstellen
pi = 3.14159265359
print(pi)
```

### Umwandeln in einen Float: Die float() Funktion

Genau wie bei Integer gibt es auch für Float eine Umwandlungsfunktion: `float()`. Sie kann:
- Strings in Floats umwandeln: `float("3.14")`
- Integer in Floats umwandeln: `float(5)` wird zu 5.0

**Wichtig:** Der String muss im englischen Format sein (mit Punkt, nicht Komma)!
- `float("3.14")` funktioniert ✓
- `float("3,14")` funktioniert NICHT ✗

```{code-cell} ipython3
# String in Float umwandeln
zahl_text = "3.14"
print("Vor der Umwandlung:")
print(type(zahl_text))
```

```{code-cell} ipython3
# Jetzt wandeln wir um
zahl_text = "3.14"
zahl = float(zahl_text)
print("Nach der Umwandlung:")
print(type(zahl))
```

```{code-cell} ipython3
# Integer in Float umwandeln
ganzzahl = 5
gleitkomma = float(ganzzahl)
print(gleitkomma)  # Zeigt: 5.0
print(type(gleitkomma))
```

```{code-cell} ipython3
# Praktisches Beispiel: Benutzereingabe in Float umwandeln
groesse_text = input("Wie groß sind Sie in Metern? (z.B. 1.75) ")
groesse = float(groesse_text)
print("Ihre Größe ist:")
print(groesse)
print("Meter")
```

### Achtung: Rundungsfehler bei Floats!

Computer speichern Floats auf eine spezielle Art im Speicher. Das kann manchmal zu winzigen Rundungsfehlern führen. Schauen Sie sich dieses Beispiel an:

```{code-cell} ipython3
# Manchmal gibt es kleine Rundungsfehler
zahl = 0.1
print(zahl)
# Dies kann manchmal zu unerwarteten Ergebnissen führen
```

**Erklärung:** Diese Rundungsfehler sind normalerweise so klein (viele Stellen nach dem Komma), dass sie in den meisten Programmen keine Rolle spielen. Aber es ist gut zu wissen, dass sie existieren!

+++

### 🏃 Sofort ausprobieren!

**Aufgabe 1:** Erstellen Sie eine Variable mit einer Temperatur (z.B. 23.5 Grad)

```{code-cell} ipython3
# Ihr Code hier:
# Erstellen Sie eine Variable "temperatur"


# Geben Sie sie aus


# Überprüfen Sie den Datentyp
```

**Aufgabe 2:** Wandeln Sie den String "99.99" in einen Float um

```{code-cell} ipython3
# Ihr Code hier:
preis_text = "99.99"
# Wandeln Sie preis_text in einen Float um


# Geben Sie das Ergebnis aus
```

**Aufgabe 3:** Wandeln Sie den Integer 42 in einen Float um

```{code-cell} ipython3
# Ihr Code hier:
ganzzahl = 42
# Wandeln Sie ganzzahl in einen Float um


# Geben Sie das Ergebnis aus und prüfen Sie den Typ
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1:
temperatur = 23.5
print(temperatur)
print(type(temperatur))  # <class 'float'>

# Aufgabe 2:
preis_text = "99.99"
preis = float(preis_text)
print(preis)
print(type(preis))  # <class 'float'>

# Aufgabe 3:
ganzzahl = 42
gleitkomma = float(ganzzahl)
print(gleitkomma)  # Zeigt: 42.0
print(type(gleitkomma))  # <class 'float'>
```
</details>

+++

---

## 5. Boolean - Wahrheitswerte ✓✗

### Was ist ein Boolean?

Stellen Sie sich einen Lichtschalter vor: Er kann nur zwei Zustände haben - an oder aus. Oder denken Sie an eine Ja/Nein-Frage: Die Antwort kann nur Ja oder Nein sein. Genau das ist ein Boolean!

Ein **Boolean** (auch "boolescher Wert" oder "Wahrheitswert" genannt) ist ein Datentyp, der nur zwei mögliche Werte besitzt:
- `True` (wahr, ja, ein, aktiviert)
- `False` (falsch, nein, aus, deaktiviert)

**Wichtig:** In Python werden `True` und `False` IMMER mit großem Anfangsbuchstaben geschrieben!

+++

### Wann verwendet man Boolean?

Booleans verwenden wir für Zustände, die nur zwei Möglichkeiten haben:
- Ist der Benutzer eingeloggt? True oder False
- Regnet es? True oder False
- Ist die Aufgabe erledigt? True oder False
- Hat der Benutzer einen Führerschein? True oder False
- Ist das Konto leer? True oder False

Später im Kurs (ab Notebook 09) werden Booleans noch viel wichtiger, wenn wir lernen, wie Programme Entscheidungen treffen können. Dann werden wir Fragen stellen wie: "Wenn alter größer als 18 ist (True), dann erlaube Zugang".

```{code-cell} ipython3
# Ein Boolean mit dem Wert True
ist_student = True
print(ist_student)
print(type(ist_student))
```

```{code-cell} ipython3
# Ein Boolean mit dem Wert False
hat_fuehrerschein = False
print(hat_fuehrerschein)
print(type(hat_fuehrerschein))
```

```{code-cell} ipython3
# Mehrere Beispiele für Boolean-Variablen
ist_sommer = True
regnet_es = False
ist_wochenende = True

print("Ist Sommer:")
print(ist_sommer)
print("Regnet es:")
print(regnet_es)
print("Ist Wochenende:")
print(ist_wochenende)
```

### Umwandeln in einen Boolean: Die bool() Funktion

Die `bool()` Funktion kann verschiedene Werte in einen Boolean umwandeln. Python hat dabei interessante Regeln:

**Werte, die als False interpretiert werden:**
- Die Zahl 0 (sowohl Integer als auch Float)
- Ein leerer String: ""
- Natürlich False selbst

**Werte, die als True interpretiert werden:**
- Alle Zahlen außer 0 (auch negative!)
- Alle Strings außer dem leeren String
- Natürlich True selbst

```{code-cell} ipython3
# Die Zahl 1 wird zu True
ergebnis = bool(1)
print(ergebnis)
```

```{code-cell} ipython3
# Die Zahl 0 wird zu False
ergebnis = bool(0)
print(ergebnis)
```

```{code-cell} ipython3
# Negative Zahlen werden zu True!
ergebnis = bool(-5)
print(ergebnis)
```

```{code-cell} ipython3
# Ein leerer String wird zu False
ergebnis = bool("")
print(ergebnis)
```

```{code-cell} ipython3
# Jeder nicht-leere String wird zu True
ergebnis = bool("Hallo")
print(ergebnis)
```

```{code-cell} ipython3
# Sogar der String "False" wird zu True!
# (Weil es ein nicht-leerer String ist)
ergebnis = bool("False")
print(ergebnis)
```

```{code-cell} ipython3
# Der String "0" wird auch zu True!
# (Es ist Text, nicht die Zahl 0)
ergebnis = bool("0")
print(ergebnis)
```

### 🏃 Sofort ausprobieren!

**Aufgabe 1:** Erstellen Sie eine Variable, die speichert, ob heute die Sonne scheint

```{code-cell} ipython3
# Ihr Code hier:
# Erstellen Sie eine Variable "sonne_scheint" mit True oder False


# Geben Sie sie aus
```

**Aufgabe 2:** Testen Sie die bool() Funktion mit verschiedenen Zahlen

```{code-cell} ipython3
# Ihr Code hier:
# Testen Sie: bool(100), bool(0), bool(-1)
# Was erhalten Sie jeweils?
```

**Aufgabe 3:** Testen Sie die bool() Funktion mit verschiedenen Strings

```{code-cell} ipython3
# Ihr Code hier:
# Testen Sie: bool("Python"), bool(""), bool(" ")
# Was erhalten Sie jeweils? Warum?
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1:
sonne_scheint = True
print(sonne_scheint)
print(type(sonne_scheint))  # <class 'bool'>

# Aufgabe 2:
print(bool(100))   # True - alle Zahlen außer 0 sind True
print(bool(0))     # False - nur 0 ist False
print(bool(-1))    # True - auch negative Zahlen sind True

# Aufgabe 3:
print(bool("Python"))  # True - nicht-leerer String
print(bool(""))        # False - leerer String
print(bool(" "))       # True - String mit Leerzeichen ist nicht leer!
```
</details>

+++

---

## Zusammenfassung 🎓

### Was Sie gelernt haben:

✅ **Datentypen verstehen:** Datentypen definieren die Art der Daten und bestimmen, wie sie gespeichert und verwendet werden können

✅ **String (Zeichenketten):** 
- Für Texte und Zeichen
- Werden in Anführungszeichen gesetzt: "Text" oder 'Text'
- `input()` gibt immer einen String zurück
- Umwandlung mit `str()`

✅ **Integer (Ganzzahlen):**
- Für ganze Zahlen ohne Dezimalstellen
- Positive, negative oder Null
- Umwandlung mit `int()`

✅ **Float (Gleitkommazahlen):**
- Für Zahlen mit Dezimalstellen
- Verwendet Punkt statt Komma (3.14 statt 3,14)
- Kann kleine Rundungsfehler haben
- Umwandlung mit `float()`

✅ **Boolean (Wahrheitswerte):**
- Nur zwei Werte: True oder False
- Für Ja/Nein-Zustände
- Umwandlung mit `bool()`

✅ **Die type() Funktion:** Zeigt den Datentyp einer Variable oder eines Werts

✅ **Typkonvertierung:** Werte können zwischen Datentypen umgewandelt werden mit `str()`, `int()`, `float()`, `bool()`

### Wichtige Konzepte:
- Jeder Datentyp hat spezifische Eigenschaften und Verwendungszwecke
- Die Wahl des richtigen Datentyps hilft, Fehler zu vermeiden
- Typkonvertierung ist wichtig, um mit Benutzereingaben zu arbeiten
- Python ist flexibel, aber Sie müssen verstehen, mit welchem Typ Sie arbeiten

+++

---

## Trainingsmaterial 💪

Jetzt ist es Zeit, Ihr Wissen zu festigen! Bearbeiten Sie die folgenden Aufgaben, um sicherzustellen, dass Sie die Datentypen wirklich verstanden haben.

+++

### 🟢 Einfache Aufgaben (zum Warmwerden)

Diese Aufgaben helfen Ihnen, die Grundlagen zu festigen.

+++

#### Aufgabe 1: Persönliche Daten

Erstellen Sie Variablen für:
- Ihren Namen (String)
- Ihr Alter (Integer)
- Ihre Körpergröße in Metern (Float)
- Ob Sie Student sind (Boolean)

Geben Sie alle Variablen mit beschreibendem Text aus.

```{code-cell} ipython3
# Ihr Code hier:
```

#### Aufgabe 2: Datentypen erkennen

Überprüfen Sie mit `type()` den Datentyp von:
- "100"
- 100
- 100.0
- True

```{code-cell} ipython3
# Ihr Code hier:
```

#### Aufgabe 3: Typkonvertierung üben

Gegeben ist: `zahl = "42"`

Wandeln Sie diese Variable in:
- Einen Integer um
- Einen Float um
- Einen Boolean um

Geben Sie jeweils das Ergebnis und den Typ aus.

```{code-cell} ipython3
# Ihr Code hier:
zahl = "42"
```

### 🟡 Mittlere Aufgaben (schon besser!)

Diese Aufgaben kombinieren mehrere Konzepte.

+++

#### Aufgabe 4: Benutzerdaten erfassen

Erstellen Sie ein kleines Programm, das:
1. Den Benutzer nach seinem Namen fragt
2. Den Benutzer nach seinem Alter fragt (und in Integer umwandelt)
3. Den Benutzer nach seiner Körpergröße fragt (und in Float umwandelt)
4. Alle Informationen schön formatiert ausgibt

```{code-cell} ipython3
# Ihr Code hier:
```

#### Aufgabe 5: Boolean-Logik erforschen

Testen Sie, welche der folgenden Werte zu True oder False werden, wenn Sie sie mit `bool()` umwandeln:
- 999
- -1
- 0.0
- "0"
- " " (ein Leerzeichen)
- "False"

Geben Sie jeweils den Wert und das Ergebnis der bool()-Konvertierung aus.

```{code-cell} ipython3
# Ihr Code hier:
```

### 🔴 Herausforderungen (für Profis)

Diese Aufgabe erfordert kreatives Denken!

+++

#### Aufgabe 6: Datentyp-Übersetzer

Erstellen Sie ein Programm, das:
1. Den Benutzer nach einer Eingabe fragt
2. Den Datentyp der Eingabe überprüft (wird immer String sein)
3. Versucht, die Eingabe in Integer umzuwandeln und das Ergebnis ausgibt
4. Versucht, die Eingabe in Float umzuwandeln und das Ergebnis ausgibt
5. Versucht, die Eingabe in Boolean umzuwandeln und das Ergebnis ausgibt
6. Die ursprüngliche Eingabe als String beibehält und ausgibt

**Hinweis:** Manche Umwandlungen werden funktionieren, manche nicht - das ist in Ordnung! Testen Sie mit verschiedenen Eingaben wie "42", "3.14", "Hallo".

```{code-cell} ipython3
# Ihr Code hier:
```

---

## Musterlösungen

Hier finden Sie ausführliche Lösungen zu allen Übungsaufgaben.

+++

### Lösung zu Aufgabe 1: Persönliche Daten

```{code-cell} ipython3
# Musterlösung Aufgabe 1

# Variablen erstellen
name = "Max Mustermann"
alter = 25
koerpergroesse = 1.80
ist_student = True

# Ausgabe mit beschreibendem Text
print("Name:")
print(name)
print("Alter:")
print(alter)
print("Jahre")
print("Körpergröße:")
print(koerpergroesse)
print("Meter")
print("Student:")
print(ist_student)
```

**Erklärung:**
- Wir erstellen vier Variablen mit unterschiedlichen Datentypen
- String für Namen (Text in Anführungszeichen)
- Integer für Alter (ganze Zahl ohne Punkt)
- Float für Körpergröße (Dezimalzahl mit Punkt)
- Boolean für Studentenstatus (True oder False)
- Jede Ausgabe wird mit beschreibendem Text versehen

+++

### Lösung zu Aufgabe 2: Datentypen erkennen

```{code-cell} ipython3
# Musterlösung Aufgabe 2

print("Typ von \"100\":")
print(type("100"))  # <class 'str'> - String wegen Anführungszeichen

print("Typ von 100:")
print(type(100))    # <class 'int'> - Integer, ganze Zahl

print("Typ von 100.0:")
print(type(100.0))  # <class 'float'> - Float wegen Dezimalpunkt

print("Typ von True:")
print(type(True))   # <class 'bool'> - Boolean
```

**Erklärung:**
- "100" ist ein String, erkennbar an den Anführungszeichen
- 100 ist ein Integer, eine ganze Zahl ohne Dezimalpunkt
- 100.0 ist ein Float - sobald ein Punkt vorhanden ist, wird es ein Float
- True ist ein Boolean, einer der beiden Wahrheitswerte

+++

### Lösung zu Aufgabe 3: Typkonvertierung üben

```{code-cell} ipython3
# Musterlösung Aufgabe 3

zahl = "42"

# In Integer umwandeln
als_integer = int(zahl)
print("Als Integer:")
print(als_integer)
print(type(als_integer))  # <class 'int'>

# In Float umwandeln
als_float = float(zahl)
print("Als Float:")
print(als_float)  # Zeigt 42.0
print(type(als_float))    # <class 'float'>

# In Boolean umwandeln
als_boolean = bool(zahl)
print("Als Boolean:")
print(als_boolean)  # True, weil nicht-leerer String
print(type(als_boolean))  # <class 'bool'>
```

**Erklärung:**
- `int("42")` wandelt den String in die Ganzzahl 42 um
- `float("42")` wandelt den String in die Gleitkommazahl 42.0 um
- `bool("42")` ergibt True, weil "42" ein nicht-leerer String ist
- Jede Umwandlung ändert den Datentyp, aber nicht unbedingt das Aussehen

+++

### Lösung zu Aufgabe 4: Benutzerdaten erfassen

```{code-cell} ipython3
# Musterlösung Aufgabe 4

# Daten vom Benutzer abfragen
name = input("Wie ist Ihr Name? ")

alter_text = input("Wie alt sind Sie? ")
alter = int(alter_text)  # In Integer umwandeln

groesse_text = input("Wie groß sind Sie in Metern? (z.B. 1.75) ")
groesse = float(groesse_text)  # In Float umwandeln

# Formatierte Ausgabe
print("")
print("Ihre Daten:")
print("Name:")
print(name)
print("Alter:")
print(alter)
print("Jahre")
print("Körpergröße:")
print(groesse)
print("Meter")
```

**Erklärung:**
- `input()` gibt immer einen String zurück
- Für das Alter wandeln wir den String mit `int()` in eine Ganzzahl um
- Für die Größe wandeln wir den String mit `float()` in eine Gleitkommazahl um
- Den Namen lassen wir als String, da er Text ist
- Wir geben alle Informationen formatiert aus

+++

### Lösung zu Aufgabe 5: Boolean-Logik erforschen

```{code-cell} ipython3
# Musterlösung Aufgabe 5

# Test 1: Positive Zahl
wert = 999
print("Wert:")
print(wert)
print("Als Boolean:")
print(bool(wert))  # True - alle Zahlen außer 0 sind True
print("")

# Test 2: Negative Zahl
wert = -1
print("Wert:")
print(wert)
print("Als Boolean:")
print(bool(wert))  # True - auch negative Zahlen sind True!
print("")

# Test 3: Float 0.0
wert = 0.0
print("Wert:")
print(wert)
print("Als Boolean:")
print(bool(wert))  # False - 0 ist immer False, auch als Float
print("")

# Test 4: String "0"
wert = "0"
print("Wert:")
print(wert)
print("Als Boolean:")
print(bool(wert))  # True - nicht-leerer String!
print("")

# Test 5: String mit Leerzeichen
wert = " "
print("Wert: (ein Leerzeichen)")
print("Als Boolean:")
print(bool(wert))  # True - String ist nicht leer!
print("")

# Test 6: String "False"
wert = "False"
print("Wert:")
print(wert)
print("Als Boolean:")
print(bool(wert))  # True - es ist ein nicht-leerer String!
```

**Erklärung:**
- **999 → True:** Alle Zahlen außer 0 werden zu True
- **-1 → True:** Auch negative Zahlen sind True
- **0.0 → False:** Die Zahl 0 ist immer False, egal ob Integer oder Float
- **"0" → True:** Dies ist ein String, nicht die Zahl 0! Nicht-leere Strings sind immer True
- **" " → True:** Ein Leerzeichen ist ein Zeichen, der String ist also nicht leer
- **"False" → True:** Der String "False" ist nicht das Boolean False, sondern ein Text mit 5 Buchstaben!

+++

### Lösung zu Aufgabe 6: Datentyp-Übersetzer

```{code-cell} ipython3
# Musterlösung Aufgabe 6

# Benutzereingabe
eingabe = input("Geben Sie etwas ein: ")

# Originaltyp anzeigen
print("")
print("Original:")
print(eingabe)
print("Typ:")
print(type(eingabe))
print("")

# Versuche Integer-Umwandlung
print("Als Integer:")
als_integer = int(eingabe)
print(als_integer)
print(type(als_integer))
print("")

# Versuche Float-Umwandlung
print("Als Float:")
als_float = float(eingabe)
print(als_float)
print(type(als_float))
print("")

# Boolean-Umwandlung (funktioniert immer)
print("Als Boolean:")
als_boolean = bool(eingabe)
print(als_boolean)
print(type(als_boolean))
print("")

# String bleibt String
print("Als String:")
als_string = str(eingabe)
print(als_string)
print(type(als_string))
```

**Erklärung:**
- Das Programm nimmt eine Benutzereingabe entgegen (immer ein String)
- Es versucht, die Eingabe in verschiedene Datentypen umzuwandeln
- Bei der Eingabe "42":
  - Integer-Umwandlung funktioniert → 42
  - Float-Umwandlung funktioniert → 42.0
  - Boolean-Umwandlung funktioniert → True (nicht-leer)
- Bei der Eingabe "3.14":
  - Integer-Umwandlung würde scheitern (Dezimalzahl)
  - Float-Umwandlung funktioniert → 3.14
  - Boolean-Umwandlung funktioniert → True
- Bei der Eingabe "Hallo":
  - Integer-Umwandlung würde scheitern (kein Text)
  - Float-Umwandlung würde scheitern
  - Boolean-Umwandlung funktioniert → True

**Hinweis:** Wenn Sie eine ungültige Umwandlung versuchen (z.B. int("Hallo")), wird Python einen Fehler ausgeben. Das ist normal und zeigt, dass nicht jede Umwandlung möglich ist!

+++

---

## Herzlichen Glückwunsch! 🎉

Sie haben Notebook 05 erfolgreich abgeschlossen! Sie verstehen nun:
- Was Datentypen sind und warum sie wichtig sind
- Wie Sie mit den vier grundlegenden Datentypen arbeiten (String, Integer, Float, Boolean)
- Wie Sie zwischen Datentypen umwandeln können
- Wie Sie den Datentyp einer Variable überprüfen

Diese Kenntnisse sind fundamental für alles, was noch kommt. Jedes Python-Programm arbeitet mit diesen Datentypen!

**Nächster Schritt:** In Notebook 06 lernen Sie komplexe Datentypen kennen - Listen, Tupel, Sets und Dictionaries. Damit können Sie nicht nur einzelne Werte, sondern ganze Sammlungen von Daten verwalten!

### Ihr Fortschritt:
- ✅ Start  
- ✅ Datentypen verstehen
- ✅ String (Zeichenketten) beherrschen
- ✅ Integer (Ganzzahlen) kennenlernen
- ✅ Float (Gleitkommazahlen) verstehen
- ✅ Boolean (Wahrheitswerte) einsetzen
- ✅ Fertig!

**Weiter so! Sie machen großartige Fortschritte!** 🚀
