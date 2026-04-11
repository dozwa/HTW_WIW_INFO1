---
title: "Informatik 1: Einführungsveranstaltung"
subtitle: "Wirtschaftsingenieurwesen Bachelor"
author: "HTW Berlin -- Wirtschaftsingenieurwesen"
date: "WiSe 2025-26"
header-includes:
  - \usepackage{etoolbox}
  - |
    \AtBeginEnvironment{longtable}{\footnotesize}
    \renewcommand{\arraystretch}{1.15}
---

# Agenda

1. Vorstellung
2. Semestertermine
3. Prüfungsmodalitäten
4. Inhaltsübersicht
5. Google Colab
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
|-----|------|----------|-------|------|
| Mi. | 14:00 -- 17:15 | wöchentlich | 08.10.25 -- 11.02.26 | TGS Haus 2 001 |

Lehrperson: Zwanzig

---

# 2. Semestertermine: Übung

| Gruppe | Rhythmus | Dauer | Räume |
|------------|----------------|---------------------|---------------------|
| 1. Gruppe | gerade Wochen | 15.10.25 -- 04.02.26 | TGS 1a/b 425 + 427 |
| 2. Gruppe | ungerade Wochen | 08.10.25 -- 11.02.26 | TGS 1a/b 425 + 427 |

Jeweils Mittwoch 17:30 -- 20:45, Lehrperson: Zwanzig

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
- Zulassung für drei Semester gültig
- Anerkennung aus Vorsemestern ggf. möglich
- Alle Hilfsmittel bei der Bearbeitung erlaubt
- **80% der Tests müssen bestanden sein** (je Test min. 50%)

---

# 3. Prüfungsmodalitäten: Tests

## Wöchentliche Tests mit 2 Wochen Bearbeitungszeit

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

# 5. Google Colab

Google Colab ist die Entwicklungsumgebung für die Vorlesung -- eine von Google bereitgestellte Plattform für Jupyter Notebooks.

- **Google Account** erforderlich
- Notebooks-Link über **Moodle** verfügbar
- Eigenständiges Experimentieren und Übungen möglich
- Code wird zellenweise ausgeführt -- schnell zu erlernen

> Jupyter Notebooks sind keine klassische IDE, aber ideal für interaktives Lernen.

---

# 6. Klausurhinweise: Allgemein

- Informatik 1 Note geht **nicht** in die Abschlussnote ein
- eKlausur im Computerlabor
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
- **Google Colab** ist die Entwicklungsumgebung
- **Aktive Teilnahme** ist der beste Weg zum Bestehen

## Nächster Schritt

$\rightarrow$ Google Colab einrichten und erstes Notebook öffnen
