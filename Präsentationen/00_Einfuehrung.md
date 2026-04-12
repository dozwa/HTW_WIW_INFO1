---
title: "Informatik 1: Einführungsveranstaltung"
subtitle: "Wirtschaftsingenieurwesen Bachelor"
author: "HTW Berlin -- Wirtschaftsingenieurwesen"
date: "SoSe 2026"
header-includes:
  - \usepackage{etoolbox}
  - \usepackage{tcolorbox}
  - |
    \AtBeginEnvironment{longtable}{\footnotesize}
    \renewcommand{\arraystretch}{1.15}
    \renewenvironment{quote}
      {\begin{tcolorbox}[colback=gray!10, colframe=gray!50, left=4pt, right=4pt, top=2pt, bottom=2pt, arc=0pt]}
      {\end{tcolorbox}}
---

# Agenda

1. Vorstellung
2. Semestertermine
3. Prüfungsmodalitäten
4. Inhaltsübersicht
5. Entwicklungsumgebungen
6. Ergänzende Klausurhinweise

---

# 1. Vorstellung

## Kurze Umfrage zu Ihren Vorkenntnissen

- Nutzen Sie den Link oder den QR-Code um die Umfrage zu bearbeiten

<!-- TODO: Menti-Link und QR-Code für aktuelles Semester einfügen -->

---

# 2. Semestertermine: Format

## Präsenz ist die Regel

- Einzelne Termine im Distanzformat möglich (<20%)
  - Eigenständige Bearbeitung der Unterlagen an einem Ort Ihrer Wahl
- Überbelegung: Kurs mit 150% Teilnehmern belegt
  - Weniger individuelle Betreuung möglich
  - Übung parallel in zwei Laboren -- eines ohne Lehrperson (Audioübertragung)
  - Mehr Eigenständigkeit Ihrerseits gefordert

---

# 2. Semestertermine: Vorlesung

<!-- TODO: Termine für aktuelles Semester aktualisieren -->

| Tag | Zeit | Rhythmus | Dauer | Raum |
|-|---|---|---|---|
| Mo. | 14:00 -- 17:15 | wöchentlich | 13.04.26 -- X | TGS Haus 1 404 |

Lehrperson: Zwanzig

---

# 2. Semestertermine: Übung

| Gruppe | Rhythmus | Dauer | Räume |
|-|-|-|-|
| 1. Gruppe | gerade Wochen | 13.04.26 -- X | TGS 1a/b 427 |
| 2. Gruppe | ungerade Wochen | 20.04.26 -- X | TGS 1a/b 427 |

Jeweils Montags 17:30 -- 20:45, Lehrperson: Zwanzig

---

# 3. Prüfungsmodalitäten: Klausur

> **Für den Abschluss des Moduls müssen Sie eine Klausur bestehen.**

- Elektronische Klausur (eKlausur) im Computerlabor der HTW
- **Keine** Hilfsmittel (keine Ordner, kein Taschenrechner, kein Spicker, keine KI)
- Aufgabentypen: Multiple Choice, Lückentexte, Freitextaufgaben, Programmieraufgaben (ohne IDE/Debugger)
- Bestehen ab 50% der Punkte, Notenskala siehe RStPO

---

# 3. Prüfungsmodalitäten: Zulassung

> **Die erfolgreiche Abgabe der Wiederholungsfragen ist Voraussetzung für die Prüfungszulassung.**

- Wiederholungsfragen = notwendige Prüfungsvorleistung
- Wöchentlich (manchmal alle zwei Wochen) als **Moodle-Test** verfügbar
- **80% der Tests müssen bestanden sein** (je Test min. 50%)
- Zulassung ist **nur drei Semester gültig** -- danach muss sie neu erworben werden
- Anerkennung aus Vorsemestern: **Bringpflicht** durch die Studierenden (Nachweis selbst erbringen!)
- Alle Hilfsmittel bei der Bearbeitung erlaubt

---

# 3. Prüfungsmodalitäten: Tests

## Tests mit 2 Wochen Bearbeitungszeit

- Beliebig oft bearbeitbar im Verfügbarkeitszeitraum
- Keine Einschränkung bei den Hilfsmitteln
- I.d.R. Multiple-Choice Fragen
- Keine zeitliche Begrenzung nach Teststart
- **Kein Nachholen möglich**
- Sie sind für die Durchführung selbst verantwortlich

---

# 4. Inhaltsübersicht: Allgemeines und Werkzeuge

## Allgemeines

- Betriebssysteme, Rechnerarchitektur, Zahlensysteme
- Daten-Informationen-Wissen-Taxonomie
- Strukturierter Problemlösungsprozess
- Syntax und Semantik, Datenformate

## Werkzeuge

- Google Colab, Visual Studio Code
- Pseudocode, Strukturgramme, Flussdiagramme (UML)

---

# 4. Inhaltsübersicht: Programmierung und Datenbanken

## Programmierung

- Klassifikation Programmiersprachen, Programmierstil
- Python: Variablen, Operatoren, Bedingungen, Schleifen, Funktionen, Bibliotheken

## Datenbanken

- Einführung (DB, DBMS, DBS), Datenmodelle
- Relationales Modell, ERM, SQL, NoSQL, Normalformen

---

# 5. Entwicklungsumgebungen

Wir arbeiten mit zwei Werkzeugen: **Google Colab** und **Visual Studio Code (VSCode)**.

- **In der Klausur steht nur VSCode zur Verfügung** -- kein Colab
- Anleitungen für beide Tools im **Moodle** verfügbar
- **Empfehlung:** VSCode auf dem eigenen Rechner installieren (inkl. Python)
- In der **Übung** kann ich bei der Einrichtung von VSCode auf privaten Rechnern unterstützen
- Wer VSCode nicht auf dem eigenen Rechner nutzen möchte $\rightarrow$ Google Colab verwenden
- Funktioniert auch auf Tablets -- aber mit Einschränkungen
- **Nutzung eines Laptops wird dringend empfohlen**

---

# 5. Entwicklungsumgebungen: Google Colab

Google Colab ist eine von Google bereitgestellte Plattform für Jupyter Notebooks.

- **Google Account** erforderlich
- Notebooks-Link über **Moodle** verfügbar
- Eigenständiges Experimentieren und Übungen möglich
- Code wird zellenweise ausgeführt -- schnell zu erlernen

> Jupyter Notebooks sind keine klassische IDE, aber ideal für interaktives Lernen.

---

# 5. Entwicklungsumgebungen: Visual Studio Code

VSCode ist ein kostenloser, quelloffener Code-Editor von Microsoft.

- Auf den **Laborrechnern der HTW** bereits installiert
- Für alle gängigen Betriebssysteme verfügbar (Windows, macOS, Linux)
- Python-Unterstützung über **Extensions** (z.B. Python, Jupyter)
- Integriertes Terminal, Debugger und Dateiverwaltung
- Wird in der **Klausur** als Editor verwendet

> VSCode ist eine vollwertige IDE -- ideal für die Arbeit mit Python-Skripten und Notebooks.

---

# 6. Klausurhinweise: Allgemein

- Informatik 1 Note geht **nicht** in die Abschlussnote ein
- eKlausur im Computerlabor mit **VSCode** als Editor (kein Colab)
- Hilfsmittel: **Python und SQL Cheat Sheet** (sonst nichts erlaubt)
- Kein Hin- und Herwechseln zwischen Klausurfragen
- Grobe Themeneingrenzung am Semesterende

> Aktive Teilnahme an Vorlesungen und Übungen erhöht die Bestehenschance signifikant!

---

# 6. Klausurhinweise: Programmieraufgaben (NEU!)

> **NEU ab diesem Semester: Richtige Programmieraufgaben in der Klausur!**

## Beispiele

1. Manipulieren Sie eine Liste mit den folgenden Operationen
2. Erstellen Sie eine SQLite Tabelle mit den folgenden Features
3. Implementieren Sie den Bubble-Sort Algorithmus analog zum Pseudocode

**Programmieraufgaben machen ca. 50% der Gesamtpunkte aus.** Ohne entsprechende Fähigkeiten wird die Klausur kaum zu bestehen sein.

---

# 6. Klausurhinweise: Fragetypen

| Fragetyp | Beispiel | Punkte |
|----------|----------|--------|
| Freitextaufgabe | Unterschied DB vs. DBMS erklären | 4 |
| Kurzantwort | Ergebnis eines Python-Programms | 1 |
| Multiple Choice | ACID-Eigenschaften identifizieren | 1 |
| Lückentext | Python-Skript vervollständigen | 4 |
| Drag-and-Drop | SQLite-Befehle sortieren | 3 |
| Zuordnung | Werte Python-Datentypen zuordnen | 4 |
| Wahr/Falsch | Pseudocode analysieren | 2 |

---

# Beispiel: Kurzantwort (1 Punkt)

**Geben Sie das Ergebnis des folgenden Python-Programms aus.**

```python
def addiere(zahl1 = 1, zahl2 = 3):
    return zahl1 + zahl2

ergebnis = addiere(5)
print(ergebnis)
```

---

# Beispiel: Multiple Choice (1 Punkt)

**Welche der folgenden Eigenschaften gehört NICHT zu den ACID-Eigenschaften?**

- A) Isolation
- B) Continuity
- C) Atomicity
- D) Durability

---

# Beispiel: Drag-and-Drop (3 Punkte)

**Sortieren Sie die Befehle für einen SQLite-Datenbankabruf:**

1. Importieren des SQLite3-Moduls
2. Verbindung zur Datenbank herstellen
3. Cursor erstellen
4. SQL-Abfrage ausführen
5. Ergebnisse abrufen und ausgeben
6. Verbindung schließen

Bausteine: `import sqlite3`, `conn = sqlite3.connect(...)`, `cur = conn.cursor()`, `cur.execute(...)`, `data = cur.fetchall()`, `conn.close()`

---

# Beispiel: Zuordnung (4 Punkte)

**Ordnen Sie den Werten die Python-Datentypen zu.**

| Wert | Datentyp |
|------|----------|
| "Käsekuchen" | str |
| True | bool |
| 1 | int |
| 2.0 | float |
| [1,2,3,4,5] | list |
| (1,2,3,4,5) | tuple |
| {"key":"value"} | dict |

---

# Beispiel: Wahr/Falsch (2 Punkte)

**Welche Aussagen stimmen für dieses Programm?**

```
FOR i = 0 TO Länge(list) - 1 DO
  FOR j = 0 TO Länge(list) - i - 1 DO
    IF list[j] > list[j+1] THEN
      Tausche list[j] und list[j+1]
END FOR  END FOR
PRINT list
```

| Aussage | Antwort |
|---------|---------|
| Verarbeitet numerische Elemente | Wahr / Falsch |
| Es ist Quick Sort | Wahr / Falsch |
| Sortiert absteigend | Wahr / Falsch |
| Es ist Bubble Sort | Wahr / Falsch |

---

# Zusammenfassung

## Wichtigste Punkte

- **Klausur** als eKlausur im Computerlabor, Bestehen ab 50%
- **Prüfungszulassung** durch Wiederholungsfragen (80% der Tests bestehen)
- **Programmieraufgaben** machen ca. 50% der Klausur aus (NEU!)
- **Google Colab und VSCode** als Entwicklungsumgebungen -- in der Klausur nur VSCode
- **Aktive Teilnahme** ist der beste Weg zum Bestehen

## Nächster Schritt

$\rightarrow$ Entwicklungsumgebung einrichten (VSCode oder Google Colab) und erstes Notebook öffnen
