---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
kernelspec:
  display_name: base2
  language: python
  name: python3
---

# 09 - Programmverzweigungen: Entscheidungen im Code treffen 🚦

## Willkommen! 👋

Bisher haben Sie Programme geschrieben, die immer denselben Ablauf hatten – Zeile für Zeile von oben nach unten. Aber stellen Sie sich vor, Sie entwickeln ein Programm für eine Produktionsanlage: Wenn weniger als 100 Bauteile produziert wurden, soll eine Warnung ausgegeben werden. Wenn mehr als 100 Bauteile produziert wurden, soll eine Erfolgsmeldung erscheinen. Das Programm muss also **Entscheidungen treffen** können!

In diesem Notebook lernen Sie, wie Sie Ihren Programmen beibringen, unterschiedliche Wege zu gehen – je nachdem, welche Bedingungen erfüllt sind. Diese sogenannten **Programmverzweigungen** sind ein fundamentales Konzept der Programmierung und ermöglichen es Ihnen, flexible und intelligente Programme zu schreiben.


## Was Sie in diesem Notebook lernen:

- **if-Anweisungen**: Code nur unter bestimmten Bedingungen ausführen
- **if-else-Anweisungen**: Zwischen zwei Alternativen entscheiden
- **elif-Anweisungen**: Mehrere Bedingungen nacheinander prüfen
- **match-case-Anweisungen**: Elegante Fallunterscheidungen durchführen
- **Bedingungen formulieren**: Mit Vergleichsoperatoren arbeiten

## Voraussetzungen 📚

Was Sie bereits können sollten:
- **Variablen** definieren und verwenden (Notebook 04)
- **Datentypen** verstehen (int, float, str, bool) (Notebook 05)
- **Vergleichsoperatoren** kennen (==, !=, <, >, <=, >=) (Notebook 08)
- **Logische Operatoren** verwenden (and, or, not) (Notebook 08)
- **print()** und **input()** nutzen (Notebook 02)

+++

---

## 1. Was sind Programmverzweigungen? 🤔

### Die Idee hinter Verzweigungen

Stellen Sie sich vor, Sie fahren mit dem Auto und kommen an eine Kreuzung. Je nachdem, wohin Sie möchten, biegen Sie links, rechts ab oder fahren geradeaus weiter. Genau so funktionieren **Programmverzweigungen**: Ihr Programm kommt an einen Punkt, an dem es eine Entscheidung treffen muss – welcher Weg soll eingeschlagen werden?

In der Programmierung nennen wir solche Entscheidungspunkte **bedingte Anweisungen** oder **Programmverzweigungen**. Sie ermöglichen es, dass bestimmte Teile Ihres Codes nur dann ausgeführt werden, wenn eine bestimmte **Bedingung** erfüllt ist.

Ein einfaches Beispiel aus dem Alltag: "**Wenn** es regnet, **dann** nehme ich einen Regenschirm mit." Das "wenn" ist die Bedingung (es regnet), und das "dann" beschreibt die Aktion, die bei erfüllter Bedingung ausgeführt wird (Regenschirm mitnehmen).

In der Programmierung funktioniert das genauso: **Wenn** eine Bedingung wahr ist (z.B. eine Zahl ist größer als 100), **dann** wird ein bestimmter Codeblock ausgeführt (z.B. eine Warnung ausgeben).

### Warum brauchen wir Verzweigungen?

Ohne Programmverzweigungen wären unsere Programme extrem limitiert. Sie würden immer genau dasselbe tun, egal welche Eingaben Sie machen oder welche Situationen auftreten. Mit Verzweigungen können wir:

- **Auf Benutzereingaben reagieren**: Wenn der Benutzer "ja" eingibt, passiert etwas anderes als bei "nein"
- **Fehler abfangen**: Wenn eine ungültige Eingabe gemacht wird, können wir eine Fehlermeldung ausgeben
- **Komplexe Logik umsetzen**: Produktionsanlagen, Alarmsysteme, Berechnungen – all das benötigt Entscheidungslogik
- **Programme intelligent machen**: Ihr Code kann sich an verschiedene Situationen anpassen

### Die wichtigsten Konzepte

Bevor wir in die Details einsteigen, hier die wichtigsten Begriffe:

- **Bedingung**: Ein Ausdruck, der entweder wahr (`True`) oder falsch (`False`) ist. Zum Beispiel: `x > 10`
- **Anweisungsblock**: Eine oder mehrere Codezeilen, die zusammengehören und ausgeführt werden, wenn die Bedingung wahr ist
- **Einrückung**: In Python wird durch Einrückung (meist 4 Leerzeichen) gekennzeichnet, welche Zeilen zu einem Anweisungsblock gehören

+++

---

## 2. Die if-Anweisung: "Wenn... dann..." 🛤️

### Was ist eine if-Anweisung?

Die **if-Anweisung** ist die grundlegendste Form der Programmverzweigung in Python. Sie bedeutet wörtlich "**wenn**" und funktioniert nach einem einfachen Prinzip: **Wenn** eine Bedingung erfüllt ist, **dann** wird der nachfolgende Code ausgeführt. Wenn die Bedingung nicht erfüllt ist, wird dieser Code einfach übersprungen.

Denken Sie an eine automatische Tür im Supermarkt: **Wenn** jemand sich der Tür nähert (Bedingung erfüllt), **dann** öffnet sich die Tür (Aktion wird ausgeführt). Wenn niemand da ist (Bedingung nicht erfüllt), bleibt die Tür geschlossen (Aktion wird nicht ausgeführt).

### Wie schreibt man eine if-Anweisung?

Die Syntax (der Aufbau) einer if-Anweisung sieht in Python so aus:

```python
if Bedingung:
    # Anweisungsblock (wird nur ausgeführt, wenn Bedingung True ist)
    # Diese Zeilen müssen eingerückt sein!
```

Wichtige Elemente:
1. **`if`**: Das Schlüsselwort, das die Verzweigung einleitet
2. **Bedingung**: Ein Ausdruck, der zu `True` oder `False` ausgewertet wird
3. **Doppelpunkt `:`**: Markiert das Ende der Bedingung und den Beginn des Anweisungsblocks
4. **Einrückung**: Alle Zeilen, die zur if-Anweisung gehören, müssen eingerückt sein (normalerweise 4 Leerzeichen)

### Wann wird der Code ausgeführt?

Python prüft die Bedingung nach dem `if`. Wenn diese Bedingung **wahr** (`True`) ist, führt Python alle eingerückten Zeilen aus. Wenn die Bedingung **falsch** (`False`) ist, überspringt Python alle eingerückten Zeilen und macht mit dem Code nach der if-Anweisung weiter.

### Typische Einsatzgebiete

if-Anweisungen verwenden Sie überall dort, wo Sie Code nur unter bestimmten Umständen ausführen möchten:
- Warnung ausgeben, wenn ein Grenzwert überschritten wird
- Aktion ausführen, wenn eine bestimmte Eingabe gemacht wurde
- Berechnungen nur für positive Zahlen durchführen
- Zugriff nur gewähren, wenn ein Passwort korrekt ist

+++

### Beispiel 1: Einfache if-Anweisung mit positiver Zahl

```{code-cell} ipython3
# Eine Variable mit einer positiven Zahl
x = 0

# Prüfen, ob x größer als 0 ist
if x > 0:
    print("x ist positiv")
    print("Der Wert von x ist:", x)

# Dieser Code wird immer ausgeführt (nicht eingerückt)
print("Ende des Programms")
```

**Erklärung:**
- Die Variable `x` hat den Wert 10
- Die Bedingung `x > 0` wird geprüft: Ist 10 größer als 0? Ja! Also `True`
- Da die Bedingung wahr ist, werden die beiden eingerückten print-Anweisungen ausgeführt
- Die letzte print-Anweisung wird immer ausgeführt, da sie nicht eingerückt ist

+++

### Beispiel 2: if-Anweisung mit negativer Zahl

```{code-cell} ipython3
# Eine Variable mit einer negativen Zahl
x = -5

# Prüfen, ob x größer als 0 ist
if x > 0:
    print("x ist positiv")
    print("Der Wert von x ist:", x)

# Dieser Code wird immer ausgeführt (nicht eingerückt)
print("Ende des Programms")
```

**Erklärung:**
- Die Variable `x` hat den Wert -5
- Die Bedingung `x > 0` wird geprüft: Ist -5 größer als 0? Nein! Also `False`
- Da die Bedingung falsch ist, werden die eingerückten print-Anweisungen **übersprungen**
- Nur die letzte print-Anweisung wird ausgeführt, da sie nicht eingerückt ist

+++

### Beispiel 3: if-Anweisung mit Vergleich auf Gleichheit

```{code-cell} ipython3
# Passwort-Überprüfung (sehr vereinfacht!)
passwort = "geheim123"

if passwort == "geheim123" and True:
    print("Zugang gewährt!")
    print("Willkommen im System.")
```

**Erklärung:**
- Die Variable `passwort` enthält den String "geheim123"
- Mit dem Vergleichsoperator `==` prüfen wir, ob der Inhalt von `passwort` genau "geheim123" ist
- Da dies der Fall ist (`True`), werden beide print-Anweisungen ausgeführt

+++

---

### 🏃 Sofort ausprobieren: if-Anweisungen

**Aufgabe 1:** Schreiben Sie ein Programm, das prüft, ob eine Temperatur über 30 Grad liegt. Wenn ja, soll "Es ist heiß!" ausgegeben werden.

```{code-cell} ipython3
# Aufgabe 1: Ihr Code hier
temperatur = 20

# Ihre if-Anweisung:
if temperatur > 30:
    print("Es ist f**** heiß!")

if temperatur > 20 and temperatur <= 30 :
    print("Es ist zumindest nicht f**** heiß!")

if temperatur < 20:
    print("Es ist weniger als 20°C ...")
```

**Aufgabe 2:** Erstellen Sie eine Variable `alter` mit dem Wert 18. Prüfen Sie, ob die Person volljährig ist (>= 18) und geben Sie eine entsprechende Nachricht aus.

```{code-cell} ipython3
# Aufgabe 2: Ihr Code hier
alter = 18

# Ihre if-Anweisung:
```

**Aufgabe 3:** Schreiben Sie ein Programm, das prüft, ob eine Produktion (Variable `produzierte_teile = 150`) das Tagesziel von 100 Teilen erreicht hat.

```{code-cell} ipython3
# Aufgabe 3: Ihr Code hier
produzierte_teile = 150
tagesziel = 100

# Ihre if-Anweisung:
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1:
temperatur = 35

if temperatur > 30:
    print("Es ist heiß!")

# Aufgabe 2:
alter = 18

if alter >= 18:
    print("Die Person ist volljährig.")

# Aufgabe 3:
produzierte_teile = 150
tagesziel = 100

if produzierte_teile >= tagesziel:
    print("Tagesziel erreicht!")
    print(f"Es wurden {produzierte_teile} Teile produziert.")
```
</details>

+++

---

## 3. Die if-else-Anweisung: Entweder... oder... ⚖️

### Was ist eine if-else-Anweisung?

Oft reicht eine einfache if-Anweisung nicht aus. Manchmal möchten wir nicht nur etwas tun, **wenn** eine Bedingung erfüllt ist, sondern auch etwas **anderes** tun, wenn sie **nicht** erfüllt ist. Genau dafür gibt es die **if-else-Anweisung**.

Stellen Sie sich einen Lichtschalter vor: **Wenn** Sie ihn drücken und das Licht ist aus, **dann** geht es an. **Ansonsten** (also wenn das Licht schon an ist) geht es aus. Es gibt also immer zwei Möglichkeiten – entweder die eine Aktion oder die andere.

In der Programmierung bedeutet `else` genau das: "ansonsten" oder "in allen anderen Fällen". Der Code im else-Block wird immer dann ausgeführt, wenn die if-Bedingung **nicht** erfüllt ist.

### Wie schreibt man eine if-else-Anweisung?

Die Syntax sieht so aus:

```python
if Bedingung:
    # Anweisungsblock 1 (wird ausgeführt, wenn Bedingung True ist)
else:
    # Anweisungsblock 2 (wird ausgeführt, wenn Bedingung False ist)
```

Wichtige Punkte:
- Das `else` steht auf derselben Einrückungsebene wie das `if`
- Nach `else` kommt auch ein Doppelpunkt `:`
- Der Code nach `else` muss ebenfalls eingerückt sein
- **Genau einer** der beiden Blöcke wird ausgeführt – nie beide, nie keiner

### Warum ist if-else nützlich?

Mit if-else können Sie **garantieren**, dass Ihr Programm in jeder Situation eine Antwort hat. Es gibt keine "Lücke" mehr – entweder trifft die Bedingung zu, oder sie trifft nicht zu. In beiden Fällen passiert etwas.

Typische Anwendungsfälle:
- Benutzereingabe prüfen: Entweder korrekt oder inkorrekt
- Zugriff gewähren: Entweder Zugang oder Ablehnung
- Klassifizierung: Entweder positiv oder negativ/null
- Ampelsteuerung: Entweder grün (fahren) oder rot (stoppen)

### Der Unterschied zu einfachem if

Bei einem einfachen `if` kann es passieren, dass **kein** Code ausgeführt wird (wenn die Bedingung falsch ist). Bei `if-else` wird **immer** einer der beiden Blöcke ausgeführt – garantiert!

+++

### Beispiel 1: Positive oder nicht-positive Zahl

```{code-cell} ipython3
# Eine Variable mit einer negativen Zahl
x = 10

# Prüfen und entsprechend reagieren
if x > 0:
    print("x ist positiv")
else:
    print("x ist nicht positiv (null oder negativ)")
```

**Erklärung:**
- Die Variable `x` hat den Wert -10
- Die Bedingung `x > 0` ist falsch (`False`), da -10 nicht größer als 0 ist
- Daher wird der if-Block übersprungen
- Stattdessen wird der else-Block ausgeführt
- Ausgabe: "x ist nicht positiv (null oder negativ)"

+++

### Beispiel 2: Produktionsziel erreicht oder nicht

```{code-cell} ipython3
# Produktionsdaten
produzierte_teile = 85
tagesziel = 100

# Überprüfung
if produzierte_teile >= tagesziel:
    print(f"Tagesziel erreicht! {produzierte_teile} Teile produziert.")
else:
    fehlende_teile = tagesziel - produzierte_teile
    print(f"Tagesziel nicht erreicht. Noch {fehlende_teile} Teile fehlen.")
```

**Erklärung:**
- Es wurden 85 Teile produziert, das Ziel liegt bei 100
- Die Bedingung `produzierte_teile >= tagesziel` ist falsch (85 ist nicht >= 100)
- Der else-Block wird ausgeführt
- Im else-Block wird berechnet, wie viele Teile fehlen (100 - 85 = 15)
- Eine informative Nachricht wird ausgegeben

+++

### Beispiel 3: Volljährigkeit prüfen

```{code-cell} ipython3
# Altersüberprüfung
alter = 16

if alter >= 18:
    print("Zugang gewährt – Sie sind volljährig.")
else:
    print("Zugang verweigert – Sie müssen mindestens 18 Jahre alt sein.")
```

**Erklärung:**
- Das Alter ist 16 Jahre
- Die Bedingung `alter >= 18` ist falsch
- Der else-Block wird ausgeführt und eine Ablehnungsmeldung ausgegeben

+++

---

### 🏃 Sofort ausprobieren: if-else-Anweisungen

**Aufgabe 1:** Schreiben Sie ein Programm, das prüft, ob eine Zahl gerade oder ungerade ist. Nutzen Sie den Modulo-Operator `%` aus Notebook 08.

```{code-cell} ipython3
# Aufgabe 1: Ihr Code hier
zahl = 7

# Ihre if-else-Anweisung:
# Hinweis: Eine Zahl ist gerade, wenn zahl % 2 == 0
```

**Aufgabe 2:** Erstellen Sie ein Programm, das eine Temperatur klassifiziert: Über 25°C ist "warm", ansonsten "kühl".

```{code-cell} ipython3
# Aufgabe 2: Ihr Code hier
temperatur = 22

# Ihre if-else-Anweisung:
```

**Aufgabe 3:** Schreiben Sie ein Passwort-Prüfprogramm. Wenn das Passwort "Python123" ist, gewähren Sie Zugang, ansonsten verweigern Sie ihn.

```{code-cell} ipython3
# Aufgabe 3: Ihr Code hier
passwort = "Test123"

# Ihre if-else-Anweisung:
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1:
zahl = 7

if zahl % 2 == 0:
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")

# Aufgabe 2:
temperatur = 22

if temperatur > 25:
    print("Es ist warm.")
else:
    print("Es ist kühl.")

# Aufgabe 3:
passwort = "Test123"

if passwort == "Python123":
    print("Zugang gewährt!")
else:
    print("Zugang verweigert – falsches Passwort!")
```
</details>

+++

---

## 4. Die elif-Anweisung: Mehrere Bedingungen prüfen 🔀

### Was ist eine elif-Anweisung?

Manchmal gibt es nicht nur zwei Möglichkeiten (entweder-oder), sondern **mehrere verschiedene Fälle**, die Sie unterscheiden möchten. Zum Beispiel: Eine Zahl kann positiv, negativ **oder** null sein – das sind drei verschiedene Fälle!

Für solche Situationen gibt es **elif** (eine Abkürzung für "**else if**", also "ansonsten wenn"). Mit elif können Sie mehrere Bedingungen nacheinander überprüfen, bis eine davon zutrifft.

Stellen Sie sich ein Ampelsystem vor: **Wenn** die Ampel grün ist, fahren Sie. **Ansonsten wenn** (elif) die Ampel gelb ist, werden Sie langsamer. **Ansonsten** (else) – also bei rot – halten Sie an. Drei verschiedene Zustände, drei verschiedene Aktionen.

### Wie funktioniert elif?

Python geht die Bedingungen von oben nach unten durch:
1. Zuerst wird die if-Bedingung geprüft
2. Wenn diese falsch ist, wird die erste elif-Bedingung geprüft
3. Wenn auch diese falsch ist, wird die nächste elif-Bedingung geprüft
4. Dieser Prozess geht so weiter, bis eine Bedingung wahr ist
5. **Sobald eine Bedingung wahr ist**, wird der zugehörige Block ausgeführt und **alle weiteren Bedingungen werden übersprungen**
6. Wenn keine Bedingung zutrifft und ein else vorhanden ist, wird der else-Block ausgeführt

### Die Syntax

```python
if Bedingung1:
    # Code für Fall 1
elif Bedingung2:
    # Code für Fall 2
elif Bedingung3:
    # Code für Fall 3
else:
    # Code für alle anderen Fälle
```

Wichtige Hinweise:
- Sie können beliebig viele elif-Zweige haben (einen, zwei, zehn, ...)
- Das `else` am Ende ist optional – Sie müssen es nicht verwenden
- Alle Schlüsselwörter (if, elif, else) stehen auf derselben Einrückungsebene
- **Nur einer** der Blöcke wird ausgeführt, niemals mehrere!

### Warum ist elif besser als mehrere if?

Sie könnten versucht sein, mehrere if-Anweisungen hintereinander zu schreiben. **Aber:** Bei mehreren if würde Python **alle** Bedingungen prüfen, auch wenn bereits eine erfüllt war. Mit elif stoppt Python, sobald eine Bedingung zutrifft. Das ist effizienter und oft genau das, was Sie wollen.

### Typische Anwendungsfälle

- Notenberechnung: A, B, C, D, F je nach Punktzahl
- Altersgruppen: Kind, Jugendlicher, Erwachsener, Senior
- Produktionsauslastung: Niedrig, Normal, Hoch, Kritisch
- Temperaturklassifizierung: Kalt, Kühl, Warm, Heiß

+++

### Beispiel 1: Zahl klassifizieren (positiv, negativ, null)

```{code-cell} ipython3
# Eine Zahl
x = 0

# Klassifizierung
if x > 0:
    print("x ist positiv")
elif x < 0:
    print("x ist negativ")
else:
    print("x ist null")
```

**Erklärung:**
- Die Variable `x` hat den Wert 0
- Erste Prüfung: `x > 0`? Nein (0 ist nicht größer als 0) → if-Block wird übersprungen
- Zweite Prüfung: `x < 0`? Nein (0 ist nicht kleiner als 0) → elif-Block wird übersprungen
- Da beide Bedingungen falsch sind, wird der else-Block ausgeführt
- Ausgabe: "x ist null"

+++

### Beispiel 2: Produktionsauslastung bewerten

```{code-cell} ipython3
# Produktionsdaten
produzierte_teile = 95
kapazitaet = 120  # Maximale Tageskapazität

# Auslastung berechnen (in Prozent)
auslastung = (produzierte_teile / kapazitaet) * 100

# Bewertung der Auslastung
if auslastung >= 90:
    print(f"Auslastung: {auslastung:.1f}% - Ausgezeichnet!")
elif auslastung >= 75:
    print(f"Auslastung: {auslastung:.1f}% - Gut")
elif auslastung >= 50:
    print(f"Auslastung: {auslastung:.1f}% - Befriedigend")
else:
    print(f"Auslastung: {auslastung:.1f}% - Zu niedrig!")
```

**Erklärung:**
- Es wurden 95 von 120 möglichen Teilen produziert
- Auslastung wird berechnet: (95/120) * 100 = 79,2%
- Erste Bedingung: `auslastung >= 90`? Nein (79,2 ist nicht >= 90)
- Zweite Bedingung: `auslastung >= 75`? Ja! (79,2 ist >= 75)
- Der elif-Block wird ausgeführt, alle weiteren Bedingungen werden übersprungen
- Ausgabe: "Auslastung: 79.2% - Gut"

+++

### Beispiel 3: Altersklassifizierung

```{code-cell} ipython3
# Alter einer Person
alter = 25

# Klassifizierung nach Altersgruppen
if alter < 12:
    print("Kind")
elif alter < 18:
    print("Jugendlicher")
elif alter < 65:
    print("Erwachsener")
else:
    print("Senior")
```

**Erklärung:**
- Das Alter ist 25 Jahre
- Erste Bedingung: `alter < 12`? Nein
- Zweite Bedingung: `alter < 18`? Nein
- Dritte Bedingung: `alter < 65`? Ja! (25 ist kleiner als 65)
- Der zweite elif-Block wird ausgeführt
- Ausgabe: "Erwachsener"

+++

---

### 🏃 Sofort ausprobieren: elif-Anweisungen

**Aufgabe 1:** Erstellen Sie ein Notensystem. Punkte >= 90: "Sehr gut", >= 75: "Gut", >= 60: "Befriedigend", >= 50: "Ausreichend", sonst: "Nicht bestanden".

```{code-cell} ipython3
# Aufgabe 1: Ihr Code hier
punkte = 82

# Ihre if-elif-else-Kette:
```

**Aufgabe 2:** Klassifizieren Sie eine Temperatur: < 0: "Gefrierend", < 15: "Kalt", < 25: "Angenehm", >= 25: "Warm".

```{code-cell} ipython3
# Aufgabe 2: Ihr Code hier
temperatur = 12

# Ihre if-elif-else-Kette:
```

**Aufgabe 3:** Bewerten Sie eine Fehlerquote (in Prozent): < 1%: "Ausgezeichnet", < 3%: "Akzeptabel", < 5%: "Grenzwertig", >= 5%: "Inakzeptabel".

```{code-cell} ipython3
# Aufgabe 3: Ihr Code hier
fehlerquote = 2.5  # in Prozent

# Ihre if-elif-else-Kette:
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1:
punkte = 82

if punkte >= 90:
    print("Sehr gut")
elif punkte >= 75:
    print("Gut")
elif punkte >= 60:
    print("Befriedigend")
elif punkte >= 50:
    print("Ausreichend")
else:
    print("Nicht bestanden")

# Aufgabe 2:
temperatur = 12

if temperatur < 0:
    print("Gefrierend")
elif temperatur < 15:
    print("Kalt")
elif temperatur < 25:
    print("Angenehm")
else:
    print("Warm")

# Aufgabe 3:
fehlerquote = 2.5

if fehlerquote < 1:
    print("Ausgezeichnet")
elif fehlerquote < 3:
    print("Akzeptabel")
elif fehlerquote < 5:
    print("Grenzwertig")
else:
    print("Inakzeptabel")
```
</details>

+++

---

## 5. Praktische Übung: Maschinenauslastung berechnen 🏭

### Aufgabenstellung

Sie arbeiten in einer Produktionshalle mit einer CNC-Fräse. Diese Maschine kann maximal **120 Bauteile pro Tag** fräsen. Ihre Aufgabe ist es, ein Programm zu schreiben, das:

1. Den Benutzer fragt, wie viele Bauteile heute gefräst wurden
2. Die prozentuale Auslastung berechnet
3. Die Auslastung ausgibt
4. Eine Bewertung der Auslastung ausgibt:
   - >= 90%: "Ausgezeichnete Auslastung!"
   - >= 75%: "Gute Auslastung"
   - >= 50%: "Durchschnittliche Auslastung"
   - < 50%: "Auslastung zu niedrig!"

```{code-cell} ipython3
# Praktische Übung: Maschinenauslastung

# Schritt 1: Benutzereingabe
count = int(input("Wie viele Bauteile wurden heute gefräst? "))

# Schritt 2: Auslastung berechnen (Ihr Code hier)
# Tipp: auslastung = (count / 120) * 100


# Schritt 3: Auslastung ausgeben (Ihr Code hier)


# Schritt 4: Bewertung ausgeben (Ihr Code hier - nutzen Sie if-elif-else)
```

<details>
<summary>🔍 Musterlösung anzeigen</summary>

```python
# Benutzereingabe
count = int(input("Wie viele Bauteile wurden heute gefräst? "))

# Auslastung berechnen
kapazitaet = 120
auslastung = (count / kapazitaet) * 100

# Auslastung ausgeben
print(f"Die Auslastung beträgt: {auslastung:.1f}%")

# Bewertung
if auslastung >= 90:
    print("Ausgezeichnete Auslastung!")
elif auslastung >= 75:
    print("Gute Auslastung")
elif auslastung >= 50:
    print("Durchschnittliche Auslastung")
else:
    print("Auslastung zu niedrig!")
```
</details>

+++

---

## 6. Die match-case-Anweisung: Elegante Fallunterscheidung 🎯

### Was ist match-case?

Ab Python 3.10 gibt es eine neue, elegante Möglichkeit, verschiedene Fälle zu unterscheiden: die **match-case-Anweisung**. Sie ist besonders nützlich, wenn Sie eine Variable mit **vielen verschiedenen konkreten Werten** vergleichen möchten.

Stellen Sie sich ein Menü in einem Restaurant vor: Je nachdem, welches Gericht Sie bestellen ("Pizza", "Pasta", "Salat"), passiert etwas anderes (verschiedene Zutaten werden vorbereitet). Mit match-case können Sie solche Fälle sehr übersichtlich programmieren.

### Wann verwendet man match-case statt if-elif?

**match-case ist ideal, wenn:**
- Sie eine Variable mit vielen spezifischen Werten vergleichen ("A", "B", "C", "D")
- Sie exakte Übereinstimmungen prüfen (Gleichheit)
- Sie viele Fälle haben und der Code übersichtlich bleiben soll

**if-elif ist besser, wenn:**
- Sie Bereiche prüfen (z.B. `alter < 18`, `alter >= 65`)
- Sie komplexe Bedingungen haben (z.B. `alter > 18 and punkte >= 50`)
- Sie mit älteren Python-Versionen (< 3.10) arbeiten müssen

### Die Syntax von match-case

```python
match variable:
    case Wert1:
        # Code für Wert1
    case Wert2:
        # Code für Wert2
    case _:
        # Code für alle anderen Werte (Standard-Fall)
```

Wichtige Elemente:
- **`match variable:`**: Gibt an, welche Variable geprüft werden soll
- **`case Wert:`**: Definiert einen Fall – wenn `variable` diesem Wert entspricht, wird der Code darunter ausgeführt
- **`case _:`**: Der Unterstrich `_` ist ein Platzhalter für "alle anderen Fälle" (wie `else` bei if)
- Die case-Blöcke müssen eingerückt sein

### Wie funktioniert match-case?

Python vergleicht den Wert der Variable nacheinander mit jedem case. Sobald eine Übereinstimmung gefunden wird, wird der zugehörige Code ausgeführt und die match-Anweisung beendet. Wenn keine Übereinstimmung gefunden wird, wird der `case _:`-Block ausgeführt (falls vorhanden).

### Vorteile von match-case

- **Übersichtlicher Code**: Besonders bei vielen Fällen leichter zu lesen als lange if-elif-Ketten
- **Klarere Struktur**: Man sieht sofort, dass es um verschiedene Fälle derselben Variable geht
- **Weniger Wiederholung**: Man muss die Variable nicht in jeder Bedingung neu schreiben

+++

### Beispiel 1: Fruchtauswahl

```{code-cell} ipython3
# Eine Variable mit einer Frucht
frucht = "Apfel"

# Match-Case-Anweisung
match frucht:
    case "Apfel":
        print("Ein Apfel hat etwa 95 Kalorien.")
    case "Banane":
        print("Eine Banane hat etwa 105 Kalorien.")
    case "Orange":
        print("Eine Orange hat etwa 62 Kalorien.")
    case _:
        print("Kalorienwert unbekannt.")
```

**Erklärung:**
- Die Variable `frucht` enthält den String "Apfel"
- Python prüft nacheinander: Ist `frucht` gleich "Apfel"? Ja!
- Der erste case-Block wird ausgeführt
- Ausgabe: "Ein Apfel hat etwa 95 Kalorien."
- Alle weiteren cases werden übersprungen

+++

### Beispiel 2: Wochentage klassifizieren

```{code-cell} ipython3
# Wochentag
tag = "Samstag"

# Klassifizierung
match tag:
    case "Montag":
        print("Wochenstart – viel Energie!")
    case "Freitag":
        print("Fast Wochenende!")
    case "Samstag":
        print("Wochenende – Zeit zum Entspannen!")
    case "Sonntag":
        print("Letzter freier Tag!")
    case _:
        print("Ein normaler Arbeitstag.")
```

**Erklärung:**
- Die Variable `tag` hat den Wert "Samstag"
- Python prüft nacheinander die cases
- Beim dritten case gibt es eine Übereinstimmung: "Samstag" == "Samstag"
- Ausgabe: "Wochenende – Zeit zum Entspannen!"

+++

### Beispiel 3: Mehrere Werte in einem case (mit |)

```{code-cell} ipython3
# Alter einer Person
alter = 2

# Altersklassifizierung mit match-case
match alter:
    case 0:
        print("Neugeborenes")
    case 1 | 2 | 3:
        print("Kleinkind")
    case 4 | 5 | 6:
        print("Vorschulkind")
    case _:
        print("Älteres Kind oder Erwachsener")
```

**Erklärung:**
- Die Variable `alter` hat den Wert 2
- Der erste case (0) passt nicht
- Der zweite case prüft: Ist `alter` gleich 1 **ODER** 2 **ODER** 3?
- Ja! `alter` ist 2, also wird dieser Block ausgeführt
- Der vertikale Strich `|` bedeutet "ODER" (eine von mehreren Möglichkeiten)
- Ausgabe: "Kleinkind"

+++

### Beispiel 4: match-case mit zusätzlichen Bedingungen (guards)

```{code-cell} ipython3
# Alter mit zusätzlichen Bedingungen
alter = 15

match alter:
    case 0:
        print("Gerade geboren")
    case _ if alter < 12:
        print("Kind")
    case _ if alter < 18:
        print("Jugendlicher")
    case _ if alter < 65:
        print("Erwachsener")
    case _:
        print("Senior")
```

**Erklärung:**
- Hier kombinieren wir match-case mit Bedingungen (guards)
- `case _ if bedingung:` bedeutet: "Alle Werte, **wenn** die Bedingung erfüllt ist"
- Das Alter ist 15
- Der erste case (0) passt nicht
- Der zweite case: `_ if alter < 12`? Nein (15 ist nicht < 12)
- Der dritte case: `_ if alter < 18`? Ja! (15 ist < 18)
- Ausgabe: "Jugendlicher"

**Hinweis:** In diesem Fall wäre eine if-elif-Kette eigentlich übersichtlicher. match-case mit guards ist eher für spezielle Situationen gedacht.

+++

---

### 🏃 Sofort ausprobieren: match-case-Anweisungen

**Aufgabe 1:** Erstellen Sie ein Programm, das basierend auf einem Monatsnamen (z.B. "Januar") die Jahreszeit ausgibt.

```{code-cell} ipython3
# Aufgabe 1: Ihr Code hier
monat = "März"

# Ihre match-case-Anweisung:
# Tipp: Dezember/Januar/Februar = Winter, März/April/Mai = Frühling, etc.
```

**Aufgabe 2:** Schreiben Sie ein Programm, das basierend auf einer Notenzahl (1, 2, 3, 4, 5) eine textuelle Note ausgibt ("Sehr gut", "Gut", etc.).

```{code-cell} ipython3
# Aufgabe 2: Ihr Code hier
note = 2

# Ihre match-case-Anweisung:
```

**Aufgabe 3:** Erstellen Sie ein Programm für eine Verkehrsampel. Bei "rot" → "Stopp", "gelb" → "Achtung", "grün" → "Fahren".

```{code-cell} ipython3
# Aufgabe 3: Ihr Code hier
ampel = "grün"

# Ihre match-case-Anweisung:
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1:
monat = "März"

match monat:
    case "Dezember" | "Januar" | "Februar":
        print("Winter")
    case "März" | "April" | "Mai":
        print("Frühling")
    case "Juni" | "Juli" | "August":
        print("Sommer")
    case "September" | "Oktober" | "November":
        print("Herbst")
    case _:
        print("Unbekannter Monat")

# Aufgabe 2:
note = 2

match note:
    case 1:
        print("Sehr gut")
    case 2:
        print("Gut")
    case 3:
        print("Befriedigend")
    case 4:
        print("Ausreichend")
    case 5:
        print("Mangelhaft")
    case _:
        print("Ungültige Note")

# Aufgabe 3:
ampel = "grün"

match ampel:
    case "rot":
        print("Stopp")
    case "gelb":
        print("Achtung – bald rot!")
    case "grün":
        print("Fahren")
    case _:
        print("Unbekannter Ampelzustand")
```
</details>

+++

---

## 7. Praktische Übung: Maschinenauslastung für verschiedene Maschinen 🏭

### Aufgabenstellung

In Ihrer Produktionshalle stehen nun mehrere Maschinen mit unterschiedlichen Kapazitäten:

- **Maschine A**: 100 Stück pro Tag
- **Maschine B**: 120 Stück pro Tag
- **Maschine C**: 50 Stück pro Tag
- **Maschine D**: 200 Stück pro Tag

Ihre Aufgabe:
1. Fragen Sie den Benutzer, für welche Maschine (A, B, C oder D) die Auslastung ermittelt werden soll
2. Fragen Sie, wie viele Stück produziert wurden
3. Berechnen Sie die Auslastung für die gewählte Maschine (nutzen Sie match-case!)
4. Geben Sie die Auslastung aus

```{code-cell} ipython3
# Praktische Übung: Maschinenauslastung mit match-case

# Schritt 1: Benutzereingaben
machine = input("Für welche Maschine soll die Auslastung ermittelt werden? (A/B/C/D) ")
count = int(input("Wie viele Stück wurden heute produziert? "))

# Schritt 2: Kapazität ermitteln mit match-case (Ihr Code hier)
# Tipp: Definieren Sie eine Variable 'kapazitaet' basierend auf 'machine'


# Schritt 3: Auslastung berechnen (Ihr Code hier)


# Schritt 4: Ausgabe (Ihr Code hier)
```

<details>
<summary>🔍 Musterlösung anzeigen</summary>

```python
# Benutzereingaben
machine = input("Für welche Maschine soll die Auslastung ermittelt werden? (A/B/C/D) ")
count = int(input("Wie viele Stück wurden heute produziert? "))

# Kapazität ermitteln mit match-case
match machine:
    case "A":
        kapazitaet = 100
    case "B":
        kapazitaet = 120
    case "C":
        kapazitaet = 50
    case "D":
        kapazitaet = 200
    case _:
        print("Ungültige Maschine!")
        kapazitaet = 0

# Auslastung berechnen (nur wenn Kapazität > 0)
if kapazitaet > 0:
    auslastung = (count / kapazitaet) * 100
    print(f"Die Auslastung für Maschine {machine} beträgt {auslastung:.1f}%")
```

**Alternative mit F-String:**
```python
print(f"Die Auslastung für Maschine {machine} beträgt {auslastung:.1f}%")
```

**Alternative ohne F-String:**
```python
print("Die Auslastung für Maschine", machine, "beträgt", round(auslastung, 1), "%")
```
</details>

+++

---

## Zusammenfassung 🎓

### Was Sie in diesem Notebook gelernt haben:

- ✅ **if-Anweisungen**: Code nur unter bestimmten Bedingungen ausführen
  - Syntax: `if Bedingung:` gefolgt von eingerücktem Code
  - Wird nur ausgeführt, wenn die Bedingung `True` ist

- ✅ **if-else-Anweisungen**: Zwischen zwei Alternativen entscheiden
  - Entweder if-Block oder else-Block wird ausgeführt (nie beide, nie keiner)
  - Garantiert, dass immer eine Aktion stattfindet

- ✅ **elif-Anweisungen**: Mehrere Bedingungen nacheinander prüfen
  - Beliebig viele elif-Blöcke zwischen if und else
  - Sobald eine Bedingung erfüllt ist, werden alle weiteren übersprungen
  - Effizienter als mehrere separate if-Anweisungen

- ✅ **match-case-Anweisungen**: Elegante Fallunterscheidungen
  - Ideal für Vergleiche mit vielen spezifischen Werten
  - Mit `|` können mehrere Werte in einem case kombiniert werden
  - `case _:` fungiert als Standard-Fall (wie else)

- ✅ **Bedingungen formulieren**: Mit Vergleichsoperatoren arbeiten
  - `>`, `<`, `>=`, `<=`, `==`, `!=` für Vergleiche
  - Bedingungen ergeben immer `True` oder `False`

### Wichtige Konzepte:

| Konzept | Verwendung | Beispiel |
|---------|------------|----------|
| **if** | Eine Bedingung prüfen | `if x > 0:` |
| **if-else** | Zwei Alternativen | `if x > 0: ... else: ...` |
| **elif** | Mehrere Bedingungen | `if ... elif ... else:` |
| **match-case** | Viele spezifische Werte | `match x: case "A": ...` |

### Wann verwende ich was?

- **Einfaches if**: Wenn Sie nur prüfen möchten, ob etwas zutrifft (optional eine Aktion ausführen)
- **if-else**: Wenn es zwei klare Alternativen gibt (entweder-oder)
- **if-elif-else**: Wenn Sie Bereiche oder komplexe Bedingungen prüfen (z.B. Notenberechnung)
- **match-case**: Wenn Sie eine Variable mit vielen konkreten Werten vergleichen (z.B. Buchstaben, Wochentage)

+++

---

## Trainingsmaterial 💪

Jetzt sind Sie dran! Testen Sie Ihr Wissen mit diesen Aufgaben. Sie werden nach Schwierigkeitsgrad geordnet präsentiert.

+++

### 🟢 Einfache Aufgaben (zum Warmwerden)

**Aufgabe 1:** Schreiben Sie ein Programm, das prüft, ob eine Zahl positiv ist. Wenn ja, geben Sie "Positiv" aus.

```{code-cell} ipython3
# 🟢 Aufgabe 1: Ihr Code hier
zahl = 42

# Ihre Lösung:
```

**Aufgabe 2:** Erstellen Sie ein Programm, das prüft, ob eine Person mindestens 16 Jahre alt ist. Geben Sie "Fahrradführerschein möglich" oder "Noch zu jung" aus.

```{code-cell} ipython3
# 🟢 Aufgabe 2: Ihr Code hier
alter = 14

# Ihre Lösung:
```

**Aufgabe 3:** Schreiben Sie ein Programm, das basierend auf einer Farbe ("rot", "grün", "blau") eine Nachricht ausgibt. Verwenden Sie match-case.

```{code-cell} ipython3
# 🟢 Aufgabe 3: Ihr Code hier
farbe = "rot"

# Ihre Lösung:
```

### 🟡 Mittlere Aufgaben (schon anspruchsvoller!)

**Aufgabe 4:** Erstellen Sie ein BMI-Bewertungsprogramm. BMI < 18.5: "Untergewicht", 18.5-24.9: "Normalgewicht", 25-29.9: "Übergewicht", >= 30: "Adipositas".

```{code-cell} ipython3
# 🟡 Aufgabe 4: Ihr Code hier
bmi = 22.5

# Ihre Lösung:
```

**Aufgabe 5:** Schreiben Sie ein Rabatt-Programm für einen Online-Shop:
- Einkaufswert < 50€: Kein Rabatt
- 50€ - 99.99€: 5% Rabatt
- 100€ - 199.99€: 10% Rabatt
- >= 200€: 15% Rabatt

Berechnen Sie den Endpreis und geben Sie ihn aus.

```{code-cell} ipython3
# 🟡 Aufgabe 5: Ihr Code hier
einkaufswert = 125.50

# Ihre Lösung:
```

**Aufgabe 6:** Erstellen Sie ein Programm, das basierend auf einer Temperatur und einem Wettercode eine Aktivitätsempfehlung gibt:
- "sonnig" und Temperatur > 20°C: "Perfekt für Outdoor-Aktivitäten!"
- "sonnig" und Temperatur <= 20°C: "Jacke mitnehmen für Spaziergang"
- "regnerisch": "Zuhause bleiben oder Regenschirm mitnehmen"
- Alles andere: "Wetter prüfen"

```{code-cell} ipython3
# 🟡 Aufgabe 6: Ihr Code hier
wetter = "sonnig"
temperatur = 25

# Ihre Lösung:
```

### 🔴 Herausforderungen (für Profis!)

**Aufgabe 7:** Erstellen Sie ein umfassendes Qualitätskontroll-Programm für eine Produktion:
- Fragen Sie nach der Anzahl produzierter Teile
- Fragen Sie nach der Anzahl fehlerhafter Teile
- Berechnen Sie die Fehlerquote in Prozent
- Bewerten Sie:
  - < 1%: "Exzellente Qualität – Weiter so!"
  - 1-2.9%: "Gute Qualität"
  - 3-4.9%: "Akzeptable Qualität – Optimierung empfohlen"
  - >= 5%: "Kritisch – Sofortige Maßnahmen erforderlich!"
- Wenn >= 5%: Berechnen Sie, wie viele fehlerhafte Teile maximal sein dürften (< 5%)

```{code-cell} ipython3
# 🔴 Aufgabe 7: Ihr Code hier

# Ihre umfassende Lösung:
```

**Aufgabe 8:** Entwickeln Sie ein Schichtplanungs-Programm:
- Fragen Sie nach dem Wochentag (als Zahl: 1=Montag, ..., 7=Sonntag)
- Fragen Sie nach der Uhrzeit (als Zahl: 0-23)
- Bestimmen Sie die Schicht:
  - Montag-Freitag, 6-14 Uhr: "Frühschicht"
  - Montag-Freitag, 14-22 Uhr: "Spätschicht"
  - Montag-Freitag, 22-6 Uhr: "Nachtschicht"
  - Samstag-Sonntag: "Wochenendschicht"
- Geben Sie zusätzlich einen Zuschlag aus:
  - Nachtschicht: +20%
  - Wochenendschicht: +25%
  - Andere: +0%

```{code-cell} ipython3
# 🔴 Aufgabe 8: Ihr Code hier

# Ihre umfassende Lösung:
```

---

### 📝 Musterlösungen

<details>
<summary>🔍 Lösungen für 🟢 Einfache Aufgaben</summary>

```python
# Aufgabe 1:
zahl = 42

if zahl > 0:
    print("Positiv")

# Aufgabe 2:
alter = 14

if alter >= 16:
    print("Fahrradführerschein möglich")
else:
    print("Noch zu jung")

# Aufgabe 3:
farbe = "rot"

match farbe:
    case "rot":
        print("Die Farbe symbolisiert Energie und Leidenschaft.")
    case "grün":
        print("Die Farbe symbolisiert Natur und Wachstum.")
    case "blau":
        print("Die Farbe symbolisiert Ruhe und Vertrauen.")
    case _:
        print("Unbekannte Farbe.")
```
</details>

<details>
<summary>🔍 Lösungen für 🟡 Mittlere Aufgaben</summary>

```python
# Aufgabe 4:
bmi = 22.5

if bmi < 18.5:
    print("Untergewicht")
elif bmi < 25:
    print("Normalgewicht")
elif bmi < 30:
    print("Übergewicht")
else:
    print("Adipositas")

# Aufgabe 5:
einkaufswert = 125.50

if einkaufswert < 50:
    rabatt = 0
elif einkaufswert < 100:
    rabatt = 5
elif einkaufswert < 200:
    rabatt = 10
else:
    rabatt = 15

rabattbetrag = einkaufswert * (rabatt / 100)
endpreis = einkaufswert - rabattbetrag

print(f"Einkaufswert: {einkaufswert:.2f}€")
print(f"Rabatt: {rabatt}% ({rabattbetrag:.2f}€)")
print(f"Endpreis: {endpreis:.2f}€")

# Aufgabe 6:
wetter = "sonnig"
temperatur = 25

if wetter == "sonnig" and temperatur > 20:
    print("Perfekt für Outdoor-Aktivitäten!")
elif wetter == "sonnig" and temperatur <= 20:
    print("Jacke mitnehmen für Spaziergang")
elif wetter == "regnerisch":
    print("Zuhause bleiben oder Regenschirm mitnehmen")
else:
    print("Wetter prüfen")
```
</details>

<details>
<summary>🔍 Lösungen für 🔴 Herausforderungen</summary>

```python
# Aufgabe 7:
produzierte_teile = int(input("Wie viele Teile wurden produziert? "))
fehlerhafte_teile = int(input("Wie viele Teile waren fehlerhaft? "))

# Fehlerquote berechnen
fehlerquote = (fehlerhafte_teile / produzierte_teile) * 100

print(f"\nFehlerquote: {fehlerquote:.2f}%")

# Bewertung
if fehlerquote < 1:
    print("Exzellente Qualität – Weiter so!")
elif fehlerquote < 3:
    print("Gute Qualität")
elif fehlerquote < 5:
    print("Akzeptable Qualität – Optimierung empfohlen")
else:
    print("Kritisch – Sofortige Maßnahmen erforderlich!")
    max_fehlerhafte = (produzierte_teile * 5) / 100
    print(f"Maximal zulässig wären {max_fehlerhafte:.0f} fehlerhafte Teile (< 5%).")

# Aufgabe 8:
wochentag = int(input("Wochentag (1=Montag, ..., 7=Sonntag): "))
uhrzeit = int(input("Uhrzeit (0-23): "))

# Schicht und Zuschlag bestimmen
if wochentag >= 6:  # Samstag oder Sonntag
    schicht = "Wochenendschicht"
    zuschlag = 25
elif uhrzeit >= 6 and uhrzeit < 14:
    schicht = "Frühschicht"
    zuschlag = 0
elif uhrzeit >= 14 and uhrzeit < 22:
    schicht = "Spätschicht"
    zuschlag = 0
else:  # 22-6 Uhr (Nachtschicht)
    schicht = "Nachtschicht"
    zuschlag = 20

print(f"\nSchicht: {schicht}")
print(f"Zuschlag: +{zuschlag}%")
```
</details>

+++

---

## Herzlichen Glückwunsch! 🎉

Sie haben erfolgreich gelernt, wie Programme Entscheidungen treffen können! Mit if, elif, else und match-case können Sie nun flexible und intelligente Programme schreiben, die auf unterschiedliche Situationen reagieren.

**Im nächsten Notebook (10_Schleifen.ipynb)** lernen Sie, wie Sie Aktionen automatisch wiederholen können – ein weiteres fundamentales Konzept der Programmierung!
