---
title: "Übungseinheit: Einfache Datentypen"
subtitle: "Praktische Anwendung von Strings, Integer, Float und Boolean in Python"
author: "Dorian Zwanzig, Claude"
date: "2025-01-10"
lang: de-DE
documentclass: article
geometry:
  - margin=2.5cm
  - a4paper
header-includes:
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhead[L]{\leftmark}
  - \fancyhead[R]{Informatik 1 - WiSe 2024-2025}
  - \fancyfoot[C]{\thepage}
  - \usepackage{titlesec}
  - \titleformat{\section}{\normalfont\Large\bfseries}{\thesection}{1em}{}
  - \titleformat{\subsection}{\normalfont\large\bfseries}{\thesubsection}{1em}{}
  - \usepackage{listings}
  - \lstset{basicstyle=\ttfamily\small, breaklines=true}
  - \usepackage{lastpage}
  - \fancyfoot[C]{Seite \thepage\ von \pageref{LastPage}}
toc: true
toc-title: "Inhaltsverzeichnis"
toc-depth: 2
numbersections: true
colorlinks: true
linkcolor: blue
urlcolor: blue
tags:
  - übung
  - python
  - datentypen
  - anfänger
---

\newpage

# Über diese Übung

## Lernziele

Nach Abschluss dieser Übung können Sie:
- Variablen vom Typ String erstellen und mit Textinhalten arbeiten
- Integer-Variablen für ganzzahlige Werte verwenden
- Float-Variablen für Dezimalzahlen einsetzen
- Boolean-Variablen für Wahrheitswerte nutzen
- Den passenden Datentyp für verschiedene Anwendungsfälle auswählen
- Typumwandlungen zwischen verschiedenen Datentypen durchführen
- Die Funktion `type()` zur Überprüfung von Datentypen anwenden

**Zeitbedarf**: ca. 90 Minuten
**Schwierigkeitsgrad**: * (Einsteiger)

---

## Voraussetzungen

Für diese Übung sollten Sie folgende Konzepte sicher beherrschen:
- **Grundlagen der Programmierung** (Notebook 01)
- **Konsolenausgabe mit print()** (Notebook 02)
- **Kommentare in Python** (Notebook 03)
- **Variablen und Wertzuweisung** (Notebook 04)

Falls Sie unsicher sind, wiederholen Sie bitte die entsprechenden Notebooks.

---

## Hinweis

Legen Sie mindestens für jeden Übungsblock eine eigene Datei an, idealerweise für jede Übung. Das hilft Ihnen die Übersicht zu behalten - nicht nur heute, sondern auch während der Klausurvorbereitung.

\newpage

# Vorbereitung (ca. 10 Min)

**Ziel:** VS Code öffnen, das Programm kennenlernen, Dateien anlegen, speichern und ausführen.

## Schritt-für-Schritt Anleitung

1. **VS Code starten** (Zenworks -- VSCode)

2. **Neues Projektverzeichnis erstellen:**
   - Datei -- Ordner öffnen...
   - Ordner z. B. `python_grundlagen` nennen

3. **Neue Datei erstellen:**
   - Im Explorer links: Rechtsklick -- Neue Datei
   - Dateiname: `hello_world.py`

4. **Code eingeben:**

```python
print("Hello World!")
```

5. **Datei speichern:**
   - Windows/Linux: `Strg + S`
   - macOS: `Cmd + S`

6. **Terminal öffnen:**
   - Windows: `Strg + ö`
   - Alternativ: _Terminal -- Neues Terminal_

7. **Datei ausführen:**

```bash
python hello_world.py        # Windows
python3 hello_world.py       # macOS/Linux
```

8. **Erwartete Ausgabe überprüfen:**

```
Hello World!
```

9. **Terminal-Ausgabe löschen:**

```bash
cls     # Windows
clear   # macOS/Linux
```

## Erfolgskontrolle

- [x] VS Code ist geöffnet
- [x] Projektordner wurde erstellt
- [x] Erste Python-Datei läuft
- [x] "Hello World!" wird ausgegeben

\newpage

# Einführung in Datentypen (ca. 15 Min)

## Die vier grundlegenden Datentypen

Python kennt verschiedene Arten von Daten. Die wichtigsten für den Anfang sind:

| Datentyp | Beschreibung | Beispiel |
|:---------|:-------------|:---------|
| **String** | Text, in Anführungszeichen | `"Hallo"`, `'Welt'` |
| **Integer** | Ganze Zahl | `42`, `-17`, `0` |
| **Float** | Kommazahl (mit Punkt!) | `3.14`, `-2.5`, `0.0` |
| **Boolean** | Wahrheitswert | `True`, `False` |

: Die vier grundlegenden Datentypen in Python {#tbl:datentypen}

## Warum verschiedene Datentypen?

- **Effizienz**: Zahlen brauchen weniger Speicher als Text
- **Operationen**: Mit Zahlen kann man rechnen, mit Text nicht
- **Klarheit**: Der Code wird verständlicher
- **Fehlerprävention**: Python warnt bei falscher Verwendung

## In dieser Übung lernen Sie:

- Variablen mit verschiedenen Datentypen erstellen
- Mit den Datentypen arbeiten
- Zwischen Typen umwandeln
- Typische Fehler vermeiden

\newpage

# Übungsblock A – Strings (ca. 20 Min)

## Vorbereitung

1. Neue Datei erstellen: `strings_uebung.py`
2. Datei im Editor öffnen

---

## Aufgabe 1: Namen speichern und ausgeben

<div class="keep-together">

### Aufgabenstellung
Erstellen Sie eine Variable mit dem Namen `name` und weisen Sie ihr Ihren Vornamen als Text zu. Geben Sie den Inhalt der Variable auf dem Bildschirm aus.

### Hilfestellungen

<details>
<summary>Problemanalyse</summary>

- Was soll gespeichert werden? -- Ein Textinhalt (Ihr Vorname)
- Welcher Datentyp wird benötigt? -- String (Text in Anführungszeichen)
- Wie gibt man etwas aus? -- Mit der `print()`-Funktion
</details>

<details>
<summary>Lösungsschritte</summary>

1. Eine Variable mit dem Namen `name` erstellen
2. Der Variable einen String-Wert zuweisen (Ihren Vornamen in Anführungszeichen)
3. Die Variable mit `print()` ausgeben
</details>

<details>
<summary>Pseudocode</summary>

```python
ERSTELLE Variable name MIT Wert "IhrVorname"
AUSGABE name
```
</details>

### Erwartete Ausgabe
```
Lina
```

</div>

---

## Aufgabe 2: Zeichenketten verknüpfen

<div class="keep-together">

### Aufgabenstellung
Erstellen Sie zwei Variablen `vorname` und `nachname` mit entsprechenden Texten. Verknüpfen Sie beide zu einem vollständigen Namen (mit Leerzeichen dazwischen) und speichern Sie das Ergebnis in einer neuen Variable `voller_name`. Geben Sie das Ergebnis aus.

### Hilfestellungen

<details>
<summary>Problemanalyse</summary>

- Was soll erreicht werden? -- Zwei separate Texte zu einem kombinieren
- Welche Daten werden benötigt? -- Vorname und Nachname als separate Variablen
- Was fehlt zwischen den Namen? -- Ein Leerzeichen als Trennung
</details>

<details>
<summary>Lösungsschritte</summary>

1. Variable `vorname` mit Ihrem Vornamen erstellen
2. Variable `nachname` mit Ihrem Nachnamen erstellen
3. Beide Strings mit `+` verknüpfen, Leerzeichen `" "` dazwischen einfügen
4. Das Ergebnis in einer neuen Variable `voller_name` speichern
5. Das Ergebnis ausgeben
</details>

<details>
<summary>Pseudocode</summary>

```python
ERSTELLE Variable vorname MIT Wert "Lina"
ERSTELLE Variable nachname MIT Wert "Schmidt"
ERSTELLE Variable voller_name MIT vorname + " " + nachname
AUSGABE voller_name
```
</details>

### Erwartete Ausgabe
```
Lina Schmidt
```

</div>

---

## Aufgabe 3: Länge eines Strings ermitteln

::: {.callout-note}
# Neue Funktion: `len()`

Die Funktion `len()` (von "length" = Länge) gibt die Anzahl der Zeichen in einem String zurück.

**Syntax:** `len(text)`

**Beispiel:**
```python
name = "Anna"
laenge = len(name)
print(laenge)  # Ausgabe: 4
```

**Wichtig:** Leerzeichen, Zahlen und Sonderzeichen werden mitgezählt!
:::

<div class="keep-together">

### Aufgabenstellung
Finden Sie heraus, wie viele Zeichen der vollständige Name (inklusive Leerzeichen) enthält und geben Sie diese Zahl aus.

### Hilfestellungen

<details>
<summary>Problemanalyse</summary>

- Was soll ermittelt werden? -- Die Anzahl der Zeichen in einem String
- Welche Funktion hilft dabei? -- Die Funktion `len()` zählt Zeichen
- Was wird mitgezählt? -- Alle Zeichen inklusive Leerzeichen
</details>

<details>
<summary>Lösungsschritte</summary>

1. Die Variable `voller_name` aus der vorherigen Aufgabe verwenden
2. Die Funktion `len()` auf die Variable anwenden
3. Das Ergebnis mit `print()` ausgeben
</details>

<details>
<summary>Pseudocode</summary>

```python
anzahl_zeichen = LÄNGE VON voller_name
AUSGABE anzahl_zeichen
```
</details>

### Erwartete Ausgabe
```
12
```

</div>

---

## Aufgabe 4: Zeichen ersetzen

::: {.callout-note}
# Neue Methode: `.replace()`

Die Methode `.replace()` ersetzt Textstellen in einem String.

**Syntax:** `text.replace("alt", "neu")`

**Beispiel:**
```python
satz = "Ich mag Äpfel"
neuer_satz = satz.replace("Äpfel", "Birnen")
print(neuer_satz)  # Ausgabe: Ich mag Birnen
print(satz)        # Ausgabe: Ich mag Äpfel (Original unverändert!)
```

**Wichtig:** Der ursprüngliche String bleibt unverändert. Das Ergebnis wird zurückgegeben.
:::

<div class="keep-together">

### Aufgabenstellung
Ersetzen Sie im vollständigen Namen "Lina" durch "Mara" und geben Sie das Ergebnis aus.

### Hilfestellungen

<details>
<summary>Problemanalyse</summary>

- Was soll passieren? -- Ein Textbestandteil soll durch einen anderen ersetzt werden
- Welche Methode hilft dabei? -- Die Methode `.replace()` ersetzt Textstellen
- Was passiert mit dem Original? -- Es bleibt unverändert, das Ergebnis muss ausgegeben werden
</details>

<details>
<summary>Lösungsschritte</summary>

1. Die Variable `voller_name` aus der vorherigen Aufgabe verwenden
2. Die Methode `.replace()` aufrufen mit "Lina" als altem und "Mara" als neuem Wert
3. Das Ergebnis direkt ausgeben oder in einer neuen Variable speichern
</details>

<details>
<summary>Pseudocode</summary>

```python
neuer_name = voller_name MIT ERSETZUNG "Lina" DURCH "Mara"
AUSGABE neuer_name
```
</details>

### Erwartete Ausgabe
```
Mara Schmidt
```

</div>

---

## Aufgabe 5: f-Strings verwenden

::: {.callout-note}
# Neues Konzept: f-Strings (formatierte Strings)

f-Strings ermöglichen es, Variablen direkt in Texte einzufügen.

**Syntax:** `f"Text {variable} mehr Text"`

**Beispiel:**
```python
name = "Max"
alter = 25
print(f"Hallo {name}, du bist {alter} Jahre alt.")
# Ausgabe: Hallo Max, du bist 25 Jahre alt.
```

**Mit Berechnungen:**
```python
preis = 10
print(f"Der doppelte Preis ist {preis * 2} Euro.")
# Ausgabe: Der doppelte Preis ist 20 Euro.
```

**Wichtig:** Das `f` vor dem String nicht vergessen!
:::

<div class="keep-together">

### Aufgabenstellung
Geben Sie einen Satz aus, der den Vornamen und die Anzahl seiner Buchstaben enthält. Nutzen Sie dafür f-Strings.

Beispiel: "Hallo Lina, dein Name hat 4 Buchstaben."

### Hilfestellungen

<details>
<summary>Problemanalyse</summary>

- Was soll ausgegeben werden? -- Ein Satz mit eingebetteten Variablen und Berechnungen
- Wie fügt man Variablen in Text ein? -- Mit f-Strings: `f"Text {variable}"`
- Wie berechnet man die Buchstabenanzahl? -- Mit `len(vorname)` direkt im f-String
</details>

<details>
<summary>Lösungsschritte</summary>

1. Einen f-String erstellen (beginnt mit `f` vor den Anführungszeichen)
2. Den Text mit Platzhaltern `{}` für Variable und Berechnung schreiben
3. In die erste Klammer `{vorname}` einfügen
4. In die zweite Klammer `{len(vorname)}` einfügen
5. Mit `print()` ausgeben
</details>

<details>
<summary>Pseudocode</summary>

```python
AUSGABE f"Hallo {vorname}, dein Name hat {LÄNGE VON vorname} Buchstaben."
```
</details>

### Erwartete Ausgabe
```
Hallo Lina, dein Name hat 4 Buchstaben.
```

</div>

---

## Aufgabe 6 (Erweitert): Mit Benutzereingabe arbeiten

**Schwierigkeit:** Mittel

<div class="keep-together">

### Aufgabenstellung
Ändern Sie das Programm so, dass der Benutzer seinen Vor- und Nachnamen selbst eingeben kann. Das Programm soll dann:
- Eine persönliche Begrüßung ausgeben
- Die Gesamtzahl der Zeichen (inklusive Leerzeichen) anzeigen

### Hilfestellungen

<details>
<summary>Problemanalyse</summary>

- Woher kommen die Daten? -- Vom Benutzer über die Konsole
- Welche Funktion liest Eingaben? -- `input("Frage")`
- Was wird dann mit den Eingaben gemacht? -- Verknüpfen, Länge berechnen, ausgeben
</details>

<details>
<summary>Lösungsschritte</summary>

1. Trennlinie ausgeben mit `print("\n--- Jetzt mit Eingabe ---")`
2. Benutzer nach Vornamen fragen und in Variable speichern
3. Benutzer nach Nachnamen fragen und in Variable speichern
4. Vor- und Nachname zu `voller_name` verknüpfen
5. Persönliche Begrüßung mit f-String ausgeben
6. Zeichenanzahl mit `len()` berechnen und ausgeben
</details>

<details>
<summary>Pseudocode</summary>

```python
AUSGABE "--- Jetzt mit Eingabe ---"
vorname = EINGABE "Wie ist dein Vorname? "
nachname = EINGABE "Wie ist dein Nachname? "
voller_name = vorname + " " + nachname
AUSGABE f"Hallo {voller_name}!"
AUSGABE f"Dein vollständiger Name hat {LÄNGE VON voller_name} Zeichen..."
```
</details>

### Beispiel-Ausgabe (bei Eingabe "Anna" und "Müller")
```
--- Jetzt mit Eingabe ---
Wie ist dein Vorname? Anna
Wie ist dein Nachname? Müller
Hallo Anna Müller!
Dein vollständiger Name hat 11 Zeichen (inkl. Leerzeichen).
```

</div>

---

## Datei ausführen und testen

```bash
python strings_uebung.py
```

**Gesamte erwartete Ausgabe der Aufgaben 1-5:**
```
Lina
Lina Schmidt
12
Mara Schmidt
Hallo Lina, dein Name hat 4 Buchstaben.
```

---

## Musterlösungen

<details>
<summary>Lösung zu Aufgabe 1</summary>

```python
# 1. Einen Namen speichern und ausgeben
name = "Lina"
print(name)
```

**Erklärung:**
- Variable `name` wird mit dem String "Lina" initialisiert
- `print()` gibt den Inhalt der Variable aus
</details>

<details>
<summary>Lösung zu Aufgabe 2</summary>

```python
# 2. Zeichenketten verknüpfen
vorname = "Lina"
nachname = "Schmidt"
voller_name = vorname + " " + nachname
print(voller_name)
```

**Erklärung:**
- Drei Strings werden mit `+` verknüpft
- Das Leerzeichen `" "` trennt Vor- und Nachname
</details>

<details>
<summary>Lösung zu Aufgabe 3</summary>

```python
# 3. Länge eines Strings prüfen
print(len(voller_name))
```

**Erklärung:**
- `len()` zählt alle Zeichen inklusive Leerzeichen
</details>

<details>
<summary>Lösung zu Aufgabe 4</summary>

```python
# 4. Zeichen ersetzen
print(voller_name.replace("Lina", "Mara"))
```

**Erklärung:**
- `.replace()` erstellt einen neuen String mit der Ersetzung
- Der ursprüngliche String bleibt unverändert
</details>

<details>
<summary>Lösung zu Aufgabe 5</summary>

```python
# 5. f-Strings verwenden
print(f"Hallo {vorname}, dein Name hat {len(vorname)} Buchstaben.")
```

**Erklärung:**
- `f` vor dem String aktiviert die Formatierung
- In `{}` können Variablen und Ausdrücke stehen
</details>

<details>
<summary>Lösung zu Aufgabe 6 (Erweitert)</summary>

```python
# 6. Mit Benutzereingabe arbeiten
print("\n--- Jetzt mit Eingabe ---")
vorname = input("Wie ist dein Vorname? ")
nachname = input("Wie ist dein Nachname? ")
voller_name = vorname + " " + nachname
print(f"Hallo {voller_name}!")
print(f"Dein vollständiger Name hat {len(voller_name)} Zeichen (inkl. Leerzeichen).")
```

**Erklärung:**
- `input()` wartet auf Benutzereingabe
- Die Eingabe wird als String zurückgegeben
- f-Strings kombinieren Text mit Variablen
</details>

\newpage

# Übungsblock B – Integer (ca. 15 Min)

## Vorbereitung

1. Neue Datei erstellen: `integer_uebung.py`
2. Datei im Editor öffnen

---

## Aufgabe 1: Grundrechenarten mit ganzen Zahlen

::: {.callout-note}
# Neue Operatoren: `//` und `%`

**Ganzzahlige Division (`//`):** Teilt zwei Zahlen und gibt nur den ganzen Teil zurück.

```python
print(10 // 3)  # Ausgabe: 3 (nicht 3.333...)
print(17 // 5)  # Ausgabe: 3
```

**Modulo (`%`):** Gibt den Rest einer Division zurück.

```python
print(10 % 3)   # Ausgabe: 1 (10 geteilt durch 3 = 3 Rest 1)
print(17 % 5)   # Ausgabe: 2 (17 geteilt durch 5 = 3 Rest 2)
```

**Anwendung:** Mit `%` kann man z.B. prüfen, ob eine Zahl gerade ist: `zahl % 2 == 0`
:::

::: {.callout-note}
# Neue Funktion: `type()`

Die Funktion `type()` zeigt den Datentyp einer Variable an.

**Syntax:** `type(variable)`

**Beispiel:**
```python
x = 42
print(type(x))       # Ausgabe: <class 'int'>
y = "Hallo"
print(type(y))       # Ausgabe: <class 'str'>
```
:::

<div class="keep-together">

### Aufgabenstellung
Erstellen Sie zwei Variablen `a` und `b` mit den Werten 10 und 4. Führen Sie folgende Berechnungen durch und geben Sie jeweils das Ergebnis aus:
- Addition
- Subtraktion
- Multiplikation
- Ganzzahlige Division (Ergebnis ohne Nachkommastellen)
- Rest bei Division (Modulo)
- Datentyp von `a` anzeigen

### Hilfestellungen

<details>
<summary>Problemanalyse</summary>

- Welche Operationen sollen durchgeführt werden? -- Grundrechenarten plus Modulo
- Welche Variablen werden benötigt? -- Zwei Integer-Variablen `a` und `b`
- Was ist der Unterschied zwischen `/` und `//`? -- `//` gibt nur den ganzzahligen Teil zurück
- Was macht `%`? -- Gibt den Rest einer Division zurück
</details>

<details>
<summary>Lösungsschritte</summary>

1. Variable `a` mit Wert 10 erstellen
2. Variable `b` mit Wert 4 erstellen
3. Für jede Operation: Berechnung durchführen und mit `print()` ausgeben
4. Operatoren verwenden: `+`, `-`, `*`, `//`, `%`
5. Mit `type()` den Datentyp von `a` anzeigen
</details>

<details>
<summary>Pseudocode</summary>

```python
a = 10
b = 4
AUSGABE "Addition:", a + b
AUSGABE "Subtraktion:", a - b
AUSGABE "Multiplikation:", a * b
AUSGABE "Ganzzahlige Division:", a // b
AUSGABE "Restwert (Modulo):", a % b
AUSGABE "Typ von a:", TYP VON a
```
</details>

### Erwartete Ausgabe
```
Addition: 14
Subtraktion: 6
Multiplikation: 40
Ganzzahlige Division: 2
Restwert (Modulo): 2
Typ von a: <class 'int'>
```

</div>

---

## Aufgabe 2 (Erweitert): Taschenrechner mit Eingabe

**Schwierigkeit:** Mittel

<div class="keep-together">

### Aufgabenstellung
Erweitern Sie Ihr Programm so, dass der Benutzer zwei Zahlen eingeben kann. Das Programm soll dann alle Rechenoperationen mit diesen Zahlen durchführen und die Ergebnisse übersichtlich ausgeben.

### Hilfestellungen

<details>
<summary>Problemanalyse</summary>

- Woher kommen die Zahlen? -- Vom Benutzer über `input()`
- Warum braucht man `int()`? -- `input()` gibt immer Strings zurück, zum Rechnen braucht man Integer
- Welche Berechnungen sollen durchgeführt werden? -- Alle Grundrechenarten plus Modulo
</details>

<details>
<summary>Lösungsschritte</summary>

1. Trennlinie ausgeben
2. Erste Zahl vom Benutzer einlesen und mit `int()` umwandeln
3. Zweite Zahl vom Benutzer einlesen und mit `int()` umwandeln
4. Alle Rechenoperationen mit f-Strings ausgeben
</details>

<details>
<summary>Pseudocode</summary>

```python
AUSGABE "--- Jetzt mit Eingabe ---"
a = INTEGER VON EINGABE "Erste Zahl: "
b = INTEGER VON EINGABE "Zweite Zahl: "
AUSGABE f"{a} + {b} = {a + b}"
AUSGABE f"{a} - {b} = {a - b}"
AUSGABE f"{a} * {b} = {a * b}"
AUSGABE f"{a} geteilt durch {b} (ganzzahlig) = {a // b}"
AUSGABE f"Rest von {a} / {b} = {a % b}"
```
</details>

### Beispiel-Ausgabe (bei Eingabe 15 und 4)
```
--- Jetzt mit Eingabe ---
Erste Zahl: 15
Zweite Zahl: 4
15 + 4 = 19
15 - 4 = 11
15 * 4 = 60
15 geteilt durch 4 (ganzzahlig) = 3
Rest von 15 / 4 = 3
```

</div>

---

## Datei ausführen und testen

```bash
python integer_uebung.py
```

---

## Musterlösungen

<details>
<summary>Lösung zu Aufgabe 1</summary>

```python
# Rechnen mit ganzen Zahlen
a = 10
b = 4

print("Addition:", a + b)
print("Subtraktion:", a - b)
print("Multiplikation:", a * b)
print("Ganzzahlige Division:", a // b)  # Ergebnis ohne Rest
print("Restwert (Modulo):", a % b)      # Nur der Rest
print("Typ von a:", type(a))
```

**Erklärung:**
- `//` gibt nur den ganzzahligen Teil zurück (2, nicht 2.5)
- `%` gibt nur den Rest zurück (2, da 10 = 4*2 + 2)
- `type()` zeigt, dass `a` ein Integer ist
</details>

<details>
<summary>Lösung zu Aufgabe 2 (Erweitert)</summary>

```python
# Mit Benutzereingabe
print("\n--- Jetzt mit Eingabe ---")
a = int(input("Erste Zahl: "))
b = int(input("Zweite Zahl: "))

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} geteilt durch {b} (ganzzahlig) = {a // b}")
print(f"Rest von {a} / {b} = {a % b}")
```

**Erklärung:**
- `int(input())` konvertiert die String-Eingabe in einen Integer
- f-Strings formatieren die Ausgabe übersichtlich
</details>

\newpage

# Übungsblock C – Float (ca. 15 Min)

## Vorbereitung

1. Neue Datei erstellen: `float_uebung.py`
2. Datei im Editor öffnen

---

## Aufgabe 1: Preisberechnung mit Mehrwertsteuer

::: {.callout-note}
# Neue Funktion: `round()`

Die Funktion `round()` rundet eine Kommazahl auf eine bestimmte Anzahl von Nachkommastellen.

**Syntax:** `round(zahl, anzahl_stellen)`

**Beispiele:**
```python
preis = 3.14159
print(round(preis, 2))   # Ausgabe: 3.14 (2 Nachkommastellen)
print(round(preis, 1))   # Ausgabe: 3.1 (1 Nachkommastelle)
print(round(preis))      # Ausgabe: 3 (keine Nachkommastellen)
```

**Wichtig:** Python verwendet "kaufmännisches Runden" (round half to even).
:::

<div class="keep-together">

### Aufgabenstellung
Ein Produkt kostet 4.99€ netto. Die Mehrwertsteuer beträgt 19% (= 0.19). Berechnen Sie:
- Den Bruttopreis (Preis × (1 + Steuersatz))
- Zeigen Sie Nettopreis, Steuersatz und Bruttopreis an
- Runden Sie den Bruttopreis auf 2 Nachkommastellen
- Zeigen Sie den Datentyp der Preis-Variable an

### Hilfestellungen

<details>
<summary>Problemanalyse</summary>

- Was soll berechnet werden? -- Der Bruttopreis aus Nettopreis und Steuersatz
- Welche Formel gilt? -- Brutto = Netto × (1 + Steuersatz)
- Warum runden? -- Für eine saubere Geldbetragsdarstellung
- Wie schreibt man Kommazahlen in Python? -- Mit Punkt, nicht mit Komma: `4.99`
</details>

<details>
<summary>Lösungsschritte</summary>

1. Variable `preis` mit Wert `4.99` erstellen
2. Variable `steuer` mit Wert `0.19` erstellen
3. Berechnung durchführen: `preis * (1 + steuer)`
4. Ergebnis in `gesamtpreis` speichern
5. Alle Werte ausgeben (Preis, Steuer, Gesamtpreis, gerundet, Typ)
</details>

<details>
<summary>Pseudocode</summary>

```python
preis = 4.99
steuer = 0.19
gesamtpreis = preis * (1 + steuer)
AUSGABE "Preis:", preis
AUSGABE "Steuersatz:", steuer
AUSGABE "Gesamtpreis:", gesamtpreis
AUSGABE "Gerundet (2 Stellen):", RUNDE gesamtpreis AUF 2 Stellen
AUSGABE "Typ von preis:", TYP VON preis
```
</details>

### Erwartete Ausgabe
```
Preis: 4.99
Steuersatz: 0.19
Gesamtpreis: 5.9381
Gerundet (2 Stellen): 5.94
Typ von preis: <class 'float'>
```

</div>

---

## Aufgabe 2 (Erweitert): Preisrechner mit Eingabe

**Schwierigkeit:** Mittel

<div class="keep-together">

### Aufgabenstellung
Erweitern Sie das Programm, sodass der Benutzer einen Nettopreis und einen Steuersatz eingeben kann. Das Programm berechnet dann den Bruttopreis und gibt ihn gerundet aus.

### Hilfestellungen

<details>
<summary>Problemanalyse</summary>

- Woher kommen die Werte? -- Vom Benutzer über `input()`
- Warum `float()` statt `int()`? -- Preise haben Nachkommastellen
- Wie gibt der Benutzer den Steuersatz ein? -- Als Dezimalzahl (0.19 für 19%)
</details>

<details>
<summary>Lösungsschritte</summary>

1. Überschrift ausgeben
2. Nettopreis vom Benutzer einlesen und mit `float()` umwandeln
3. Steuersatz vom Benutzer einlesen und mit `float()` umwandeln
4. Bruttopreis berechnen
5. Nettopreis und Bruttopreis mit f-Strings und Euro-Symbol ausgeben
</details>

<details>
<summary>Pseudocode</summary>

```python
AUSGABE "--- Preisberechnung mit Eingabe ---"
preis = FLOAT VON EINGABE "Nettopreis eingeben: "
steuer = FLOAT VON EINGABE "Steuersatz eingeben..."
gesamtpreis = preis * (1 + steuer)
AUSGABE f"Nettopreis: {preis}€"
AUSGABE f"Bruttopreis: {RUNDE gesamtpreis AUF 2}€"
```
</details>

### Beispiel-Ausgabe (bei Eingabe 10.50 und 0.19)
```
--- Preisberechnung mit Eingabe ---
Nettopreis eingeben: 10.50
Steuersatz eingeben (z.B. 0.19 für 19%): 0.19
Nettopreis: 10.5€
Bruttopreis: 12.5€
```

</div>

---

## Datei ausführen und testen

```bash
python float_uebung.py
```

---

## Musterlösungen

<details>
<summary>Lösung zu Aufgabe 1</summary>

```python
# Rechnen mit Kommazahlen
preis = 4.99
steuer = 0.19
gesamtpreis = preis * (1 + steuer)

print("Preis:", preis)
print("Steuersatz:", steuer)
print("Gesamtpreis:", gesamtpreis)
print("Gerundet (2 Stellen):", round(gesamtpreis, 2))
print("Typ von preis:", type(preis))
```

**Erklärung:**
- `(1 + steuer)` entspricht 119% = 1.19
- `round()` rundet auf kaufmännische Art
- `type()` zeigt `<class 'float'>` für Kommazahlen
</details>

<details>
<summary>Lösung zu Aufgabe 2 (Erweitert)</summary>

```python
# Mit Benutzereingabe
print("\n--- Preisberechnung mit Eingabe ---")
preis = float(input("Nettopreis eingeben: "))
steuer = float(input("Steuersatz eingeben (z.B. 0.19 für 19%): "))
gesamtpreis = preis * (1 + steuer)

print(f"Nettopreis: {preis}€")
print(f"Bruttopreis: {round(gesamtpreis, 2)}€")
```

**Erklärung:**
- `float(input())` konvertiert die Eingabe in eine Kommazahl
- Der Bruttopreis wird direkt gerundet ausgegeben
</details>

\newpage

# Übungsblock D – Boolean (ca. 10 Min)

## Vorbereitung

1. Neue Datei erstellen: `boolean_uebung.py`
2. Datei im Editor öffnen

---

## Aufgabe: Logische Verknüpfungen verstehen

::: {.callout-note}
# Logische Operatoren: `and`, `or`, `not`

Mit logischen Operatoren können Boolean-Werte kombiniert werden.

**`and` (UND):** Beide Bedingungen müssen `True` sein
```python
print(True and True)    # Ausgabe: True
print(True and False)   # Ausgabe: False
```

**`or` (ODER):** Mindestens eine Bedingung muss `True` sein
```python
print(True or False)    # Ausgabe: True
print(False or False)   # Ausgabe: False
```

**`not` (NICHT):** Kehrt den Wahrheitswert um
```python
print(not True)         # Ausgabe: False
print(not False)        # Ausgabe: True
```
:::

::: {.callout-note}
# Vergleichsoperatoren

Vergleiche liefern Boolean-Werte (`True` oder `False`) zurück:

| Operator | Bedeutung | Beispiel |
|:---------|:----------|:---------|
| `==` | Gleich | `5 == 5` -- `True` |
| `!=` | Ungleich | `5 != 3` -- `True` |
| `<` | Kleiner als | `3 < 5` -- `True` |
| `>` | Größer als | `5 > 3` -- `True` |
| `<=` | Kleiner oder gleich | `3 <= 3` -- `True` |
| `>=` | Größer oder gleich | `5 >= 5` -- `True` |

: Vergleichsoperatoren in Python {#tbl:vergleiche}

**Wichtig:** `==` prüft auf Gleichheit, `=` ist Zuweisung!
:::

<div class="keep-together">

### Aufgabenstellung
Erstellen Sie zwei Boolean-Variablen:
- `ist_student` mit dem Wert `True`
- `hat_ausweis` mit dem Wert `False`

Führen Sie dann folgende logische Operationen durch:
1. Zeigen Sie beide Variablen einzeln an
2. UND-Verknüpfung (`and`)
3. ODER-Verknüpfung (`or`)
4. Negation (`not`)
5. Zeigen Sie den Datentyp an

Zusätzlich: Erstellen Sie eine Variable `alter` mit dem Wert 20 und führen Sie Vergleichsoperationen durch.

### Hilfestellungen

<details>
<summary>Problemanalyse</summary>

- Was sind Boolean-Werte? -- Wahrheitswerte: nur `True` oder `False`
- Was macht `and`? -- Beide Bedingungen müssen wahr sein
- Was macht `or`? -- Mindestens eine Bedingung muss wahr sein
- Was macht `not`? -- Kehrt den Wahrheitswert um (True -- False)
- Wie entstehen Booleans? -- Durch Vergleiche wie `>=`, `<`, `==`
</details>

<details>
<summary>Lösungsschritte</summary>

1. Variable `ist_student` mit `True` erstellen
2. Variable `hat_ausweis` mit `False` erstellen
3. Beide Variablen einzeln ausgeben
4. Logische Operationen `and`, `or`, `not` anwenden und ausgeben
5. Datentyp mit `type()` anzeigen
6. Variable `alter` mit 20 erstellen
7. Vergleichsoperationen durchführen und ausgeben
</details>

<details>
<summary>Pseudocode</summary>

```python
ist_student = True
hat_ausweis = False
AUSGABE "Ist Student:", ist_student
AUSGABE "Hat Ausweis:", hat_ausweis
AUSGABE "Student UND Ausweis:", ist_student AND hat_ausweis
AUSGABE "Student ODER Ausweis:", ist_student OR hat_ausweis
AUSGABE "NICHT Ausweis:", NOT hat_ausweis
AUSGABE "Typ von ist_student:", TYP VON ist_student

alter = 20
AUSGABE "Vergleiche:"
AUSGABE "alter >= 18:", alter >= 18
AUSGABE "alter < 18:", alter < 18
AUSGABE "alter == 20:", alter == 20
```
</details>

### Erwartete Ausgabe
```
Ist Student: True
Hat Ausweis: False
Student UND Ausweis: False
Student ODER Ausweis: True
NICHT Ausweis: True
Typ von ist_student: <class 'bool'>

Vergleiche:
alter >= 18: True
alter < 18: False
alter == 20: True
```

</div>

---

## Datei ausführen und testen

```bash
python boolean_uebung.py
```

---

## Musterlösungen

<details>
<summary>Lösung</summary>

```python
# Wahrheitswerte und logische Verknüpfungen
ist_student = True
hat_ausweis = False

print("Ist Student:", ist_student)
print("Hat Ausweis:", hat_ausweis)
print("Student UND Ausweis:", ist_student and hat_ausweis)
print("Student ODER Ausweis:", ist_student or hat_ausweis)
print("NICHT Ausweis:", not hat_ausweis)
print("Typ von ist_student:", type(ist_student))

# Vergleichsoperationen ergeben auch Boolean-Werte
alter = 20
print("\nVergleiche:")
print("alter >= 18:", alter >= 18)
print("alter < 18:", alter < 18)
print("alter == 20:", alter == 20)
```

**Erklärung:**
- `and`: Nur `True` wenn beide `True` sind
- `or`: `True` wenn mindestens einer `True` ist
- `not`: Dreht `False` zu `True` um
- Vergleiche geben immer Boolean-Werte zurück
</details>

\newpage

# Übungsblock E – Typprüfung & Umwandlung (ca. 15 Min)

## Vorbereitung

1. Neue Datei erstellen: `typumwandlung_uebung.py`
2. Datei im Editor öffnen

---

## Aufgabe: Datentypen umwandeln

::: {.callout-note}
# Typumwandlung: `str()`, `int()`, `float()`, `bool()`

Mit diesen Funktionen können Werte zwischen verschiedenen Datentypen umgewandelt werden.

**`str()` - In String umwandeln:**
```python
zahl = 42
text = str(zahl)
print(text)          # Ausgabe: "42"
print(type(text))    # Ausgabe: <class 'str'>
```

**`int()` - In Integer umwandeln:**
```python
text = "100"
zahl = int(text)
print(zahl)          # Ausgabe: 100

# Bei Float: Nachkommastellen werden ABGESCHNITTEN!
print(int(3.99))     # Ausgabe: 3 (nicht 4!)
```

**`float()` - In Float umwandeln:**
```python
text = "3.14"
zahl = float(text)
print(zahl)          # Ausgabe: 3.14
```

**`bool()` - In Boolean umwandeln:**
```python
print(bool(1))       # Ausgabe: True
print(bool(0))       # Ausgabe: False
print(bool(""))      # Ausgabe: False (leerer String)
print(bool("Hallo")) # Ausgabe: True
```

**Wichtig:**
- `int("3.5")` funktioniert NICHT! -- Erst `float()`, dann `int()`
- `True` wird zu `1`, `False` wird zu `0`
:::

<div class="keep-together">

### Aufgabenstellung
Erstellen Sie verschiedene Variablen und wandeln Sie sie zwischen Datentypen um:

1. Integer zu String umwandeln (42)
2. Float zu Integer umwandeln (3.99) - Was passiert mit den Nachkommastellen?
3. Boolean zu Integer umwandeln (True und False)
4. String zu Integer umwandeln ("100")

### Hilfestellungen

<details>
<summary>Problemanalyse</summary>

- Was bedeutet Typumwandlung? -- Den Datentyp eines Wertes ändern
- Welche Funktionen gibt es? -- `str()`, `int()`, `float()`, `bool()`
- Was passiert bei `int()` mit Kommazahlen? -- Nachkommastellen werden abgeschnitten (nicht gerundet!)
- Was wird aus `True`/`False` bei `int()`? -- 1 bzw. 0
</details>

<details>
<summary>Lösungsschritte</summary>

1. Variable `x` mit 42 erstellen
2. `x` und seinen Typ ausgeben
3. `x` mit `str()` in String umwandeln und ausgeben
4. Variable `y` mit 3.99 erstellen
5. `y` mit `int()` in Integer umwandeln und zeigen, was passiert
6. `True` und `False` mit `int()` umwandeln
7. String "100" mit `int()` umwandeln
</details>

<details>
<summary>Pseudocode</summary>

```python
x = 42
AUSGABE "x =", x
AUSGABE "Typ von x:", TYP VON x
x_str = STRING VON x
AUSGABE "x als String:", x_str, "| Typ:", TYP VON x_str

y = 3.99
AUSGABE "y =", y
AUSGABE "y als Integer:", INTEGER VON y

AUSGABE "Boolean zu Integer:"
AUSGABE "int(True) =", INTEGER VON True
AUSGABE "int(False) =", INTEGER VON False

zahl_text = "100"
zahl = INTEGER VON zahl_text
AUSGABE "String '100' zu Integer:", zahl, "| Typ:", TYP VON zahl
```
</details>

### Erwartete Ausgabe
```
x = 42
Typ von x: <class 'int'>
x als String: 42 | Typ: <class 'str'>

y = 3.99
y als Integer: 3

Boolean zu Integer:
int(True) = 1
int(False) = 0

String '100' zu Integer: 100 | Typ: <class 'int'>
```

</div>

---

## Datei ausführen und testen

```bash
python typumwandlung_uebung.py
```

---

## Musterlösungen

<details>
<summary>Lösung</summary>

```python
# Typen prüfen und umwandeln
x = 42
print("x =", x)
print("Typ von x:", type(x))

# Integer zu String
x_str = str(x)
print("x als String:", x_str, "| Typ:", type(x_str))

# Float zu Integer (Nachkommastellen werden abgeschnitten!)
y = 3.99
print("\ny =", y)
print("y als Integer:", int(y))

# Boolean zu Integer
print("\nBoolean zu Integer:")
print("int(True) =", int(True))
print("int(False) =", int(False))

# String zu Integer (nur wenn möglich!)
zahl_text = "100"
zahl = int(zahl_text)
print("\nString '100' zu Integer:", zahl, "| Typ:", type(zahl))
```

**Erklärung:**
- `int()` schneidet Nachkommastellen ab (3.99 -- 3)
- `True` wird zu 1, `False` zu 0 konvertiert
- String-zu-Integer funktioniert nur bei gültigen Zahlen
</details>

\newpage

# Übungsblock F – Gemischte Aufgaben (ca. 25 Min)

## Aufgabe 1: Temperaturumrechner

**Schwierigkeit:** Einfach

### Vorbereitung
1. Neue Datei erstellen: `temperatur_umrechner.py`

<div class="keep-together">

### Aufgabenstellung
Erstellen Sie ein Programm, das Celsius in Fahrenheit umrechnet:
- Benutzer gibt eine Temperatur in Celsius ein
- Programm berechnet den Wert in Fahrenheit
- Formel: `Fahrenheit = Celsius × 9/5 + 32`
- Ergebnis wird gerundet auf 2 Nachkommastellen ausgegeben

### Hilfestellungen

<details>
<summary>Problemanalyse</summary>

- Was soll umgerechnet werden? -- Celsius nach Fahrenheit
- Welche Formel gilt? -- `Fahrenheit = Celsius × 9/5 + 32`
- Woher kommt der Celsius-Wert? -- Vom Benutzer über `input()`
- Wie wird die Ausgabe formatiert? -- Mit f-String und den Grad-Symbolen °C und °F
</details>

<details>
<summary>Lösungsschritte</summary>

1. Überschrift "=== Temperaturumrechner ===" ausgeben
2. Celsius-Wert vom Benutzer einlesen mit `float(input(...))`
3. Formel anwenden: `celsius * 9/5 + 32`
4. Ergebnis auf 2 Nachkommastellen runden
5. Mit f-String beide Werte ausgeben
</details>

<details>
<summary>Pseudocode</summary>

```python
AUSGABE "=== Temperaturumrechner ==="
celsius = FLOAT VON EINGABE "Temperatur in °C: "
fahrenheit = celsius * 9/5 + 32
AUSGABE f"{celsius}°C = {RUNDE fahrenheit AUF 2}°F"
```
</details>

### Beispiel-Ausgabe (bei 0°C und 100°C)
```
=== Temperaturumrechner ===
Temperatur in °C: 0
0.0°C = 32.0°F

=== Temperaturumrechner ===
Temperatur in °C: 100
100.0°C = 212.0°F
```

### Testwerte zum Überprüfen
- 0°C sollte 32°F ergeben
- 100°C sollte 212°F ergeben
- 20°C sollte 68°F ergeben

</div>

### Datei ausführen und testen
```bash
python temperatur_umrechner.py
```

---

## Aufgabe 2: Notenprüfung

**Schwierigkeit:** Mittel

### Vorbereitung
1. Neue Datei erstellen: `noten_pruefung.py`

<div class="keep-together">

### Aufgabenstellung
Erstellen Sie ein Programm zur Prüfung, ob eine Note zum Bestehen ausreicht:
- Benutzer gibt eine Note zwischen 1 und 6 ein
- Programm prüft, ob die Note <= 4 ist (bestanden)
- Gibt den Boolean-Wert aus (True/False)

### Hilfestellungen

<details>
<summary>Problemanalyse</summary>

- Was soll geprüft werden? -- Ob die Note zum Bestehen ausreicht
- Welche Bedingung gilt für "bestanden"? -- Note kleiner oder gleich 4
- Was ist das Ergebnis? -- Ein Boolean-Wert (True = bestanden, False = nicht bestanden)
- Woher kommt die Note? -- Vom Benutzer über `input()`
</details>

<details>
<summary>Lösungsschritte</summary>

1. Überschrift "=== Notenprüfung ===" ausgeben
2. Note vom Benutzer einlesen mit `int(input(...))`
3. Vergleich durchführen: `note <= 4`
4. Ergebnis in Variable `bestanden` speichern
5. Note und Ergebnis ausgeben
</details>

<details>
<summary>Pseudocode</summary>

```python
AUSGABE "=== Notenprüfung ==="
note = INTEGER VON EINGABE "Note eingeben (1-6): "
bestanden = note <= 4
AUSGABE f"Note: {note}"
AUSGABE f"Bestanden: {bestanden}"
```
</details>

### Beispiel-Ausgabe (bei Note 3 und Note 5)
```
=== Notenprüfung ===
Note eingeben (1-6): 3
Note: 3
Bestanden: True

=== Notenprüfung ===
Note eingeben (1-6): 5
Note: 5
Bestanden: False
```

</div>

### Datei ausführen und testen
```bash
python noten_pruefung.py
```

---

## Musterlösungen

<details>
<summary>Lösung zu Aufgabe 1: Temperaturumrechner</summary>

```python
# Temperaturumrechner Celsius -- Fahrenheit
print("=== Temperaturumrechner ===")
celsius = float(input("Temperatur in °C: "))
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C = {round(fahrenheit, 2)}°F")
```

**Erklärung:**
- Formel wird direkt umgesetzt
- Punkt-vor-Strich wird automatisch beachtet
- `round()` sorgt für saubere Ausgabe
</details>

<details>
<summary>Lösung zu Aufgabe 2: Notenprüfung</summary>

```python
# Notenprüfung
print("=== Notenprüfung ===")
note = int(input("Note eingeben (1-6): "))
bestanden = note <= 4
print(f"Note: {note}")
print(f"Bestanden: {bestanden}")

# Hinweis: Die Textausgabe könnte mit if-else erfolgen,
# das lernen Sie aber erst in Notebook 09.
# Für jetzt reicht die Ausgabe des Boolean-Wertes.
```

**Erklärung:**
- `note <= 4` ergibt direkt einen Boolean-Wert
- Dieser wird in `bestanden` gespeichert
- Die Textausgabe mit if-else kommt erst in Notebook 09
</details>

\newpage

# Typische Anfängerfehler – Troubleshooting

## Python-Fehler

| **Fehler** | **Ursache** | **Lösung** |
|:-----------|:------------|:-----------|
| `NameError: name 'x' is not defined` | Variable wurde nicht initialisiert oder Tippfehler | Variable vor Verwendung mit Wert belegen; Schreibweise prüfen |
| `TypeError: can only concatenate str (not "int") to str` | Versuch, String mit Integer zu kombinieren | Typumwandlung verwenden: `str(zahl)` |
| `ValueError: invalid literal for int()` | Versuch, ungültigen String in Integer umzuwandeln | Erst zu Float: `int(float("3.5"))` |
| `SyntaxError: invalid syntax` | Fehlende Klammern, Anführungszeichen oder Doppelpunkt | Syntaxprüfung; öffnende und schließende Zeichen zählen |
| `IndentationError` | Falsche Einrückung | Konsistente Einrückung (4 Leerzeichen) |
| `ZeroDivisionError` | Division durch Null | Vor Division prüfen, ob Nenner != 0 |

: Häufige Python-Fehler und ihre Lösungen {#tbl:fehler}

## VSCode-spezifische Probleme

| **Problem** | **Ursache** | **Lösung** |
|:------------|:------------|:-----------|
| Datei wird nicht ausgeführt | Python nicht installiert oder nicht im PATH | Python installieren; ggf. `python3` verwenden |
| Terminal zeigt alten Code | Terminal-Cache | Terminal leeren mit `cls` oder `clear` |
| Änderungen nicht übernommen | Datei nicht gespeichert | `Strg + S` zum Speichern |
| Falsches Terminal-Verzeichnis | Terminal im falschen Ordner | `cd python_grundlagen` |
| Code wird nicht farbig | Datei nicht als `.py` gespeichert | Mit `.py`-Endung speichern |

: VSCode-Probleme und Lösungen {#tbl:vscode}

## Eingabefehler bei input()

| **Problem** | **Ursache** | **Lösung** |
|:------------|:------------|:-----------|
| `ValueError` bei `int(input())` | Buchstaben statt Zahlen eingegeben | Nur Zahlen eingeben |
| Kommazahl nicht erkannt | Komma statt Punkt | Punkt verwenden: `3.14` statt `3,14` |
| `EOFError` | Programm wartet auf Eingabe | In Terminal eingeben und Enter drücken |

: Eingabefehler und Lösungen {#tbl:eingabe}

## Tipps zur Fehlervermeidung

**Goldene Regeln:**
1. - [x] **Immer speichern** (`Strg + S`) bevor Sie ausführen
2. - [x] **Fehlermeldungen lesen** – sie zeigen oft die Zeile an
3. - [x] **Schritt für Schritt** – testen Sie jede Zeile einzeln
4. - [x] **Variablennamen prüfen** – `Name` != `name`
5. - [x] **Anführungszeichen schließen** – jedes `"` braucht ein schließendes `"`
6. - [x] **Klammern zählen** – jede `(` braucht eine `)`
7. - [x] **Bei input() den richtigen Typ verwenden:**
   - Für Zahlen: `int(input())` oder `float(input())`
   - Für Text: einfach `input()`

\newpage

# Abschluss / Reflexion (ca. 10 Min)

## Alle Skripte testen

**Checkliste zum Durchgehen:**
- [ ] Jede erstellte Datei noch einmal ausführen
- [ ] Verschiedene Eingabewerte ausprobieren
- [ ] Terminal bei Bedarf löschen (`cls` oder `clear`)

## Reflexionsfragen

Nehmen Sie sich einen Moment Zeit und überlegen Sie:

1. **Welche Datentypen gibt es in Python?**
   - String, Integer, Float, Boolean

2. **Wie prüft man den Typ einer Variable?**
   - Mit der Funktion `type()`

3. **Wie wandelt man Werte zwischen Typen um?**
   - Mit `str()`, `int()`, `float()`, `bool()`

4. **Wann muss man `int()` oder `float()` bei `input()` verwenden?**
   - Wenn man mit den eingegebenen Werten rechnen möchte

5. **Welche typischen Fehler können auftreten und wie behebt man sie?**
   - NameError -- Variable definieren
   - TypeError -- Typumwandlung
   - ValueError -- Gültige Werte verwenden

## Dateien organisieren

Überprüfen Sie, dass alle Übungsdateien im Ordner `python_grundlagen` liegen:

**Fortschritt:** 90% abgeschlossen

**Erstellte Dateien:**

- [x] `hello_world.py`
- [x] `strings_uebung.py`
- [x] `integer_uebung.py`
- [x] `float_uebung.py`
- [x] `boolean_uebung.py`
- [x] `typumwandlung_uebung.py`
- [x] `temperatur_umrechner.py`
- [x] `noten_pruefung.py`

## Was haben Sie gelernt?

In dieser Übungseinheit haben Sie:
- Die vier grundlegenden Datentypen kennengelernt
- Mit Variablen gearbeitet
- Zwischen Datentypen umgewandelt
- Erste kleine Programme geschrieben
- Benutzereingaben verarbeitet

**Herzlichen Glückwunsch!** Sie haben die Grundlagen der Datentypen in Python gemeistert!

## Nächste Schritte

Im nächsten Notebook lernen Sie:
- Listen und andere komplexe Datentypen
- Wie man mehrere Werte speichert
- Wie man mit Sammlungen von Daten arbeitet

---

**Ende der Übungseinheit**