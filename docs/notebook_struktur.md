# Metabeschreibung: Struktur der Jupyter Notebooks

**Informatik 1 – HTW Berlin, Wirtschaftsingenieurwesen**
**Stand:** April 2026

---

## 1. Korpus-Überblick

| Kennzahl | Wert |
|----------|------|
| Notebooks gesamt | 25 (01–23, mit 13a/b und 16a/b) |
| Zellen gesamt | ca. 2.300 |
| Durchschnitt Zellen/Notebook | ~92 (Spanne: 12–162) |
| Markdown : Code Verhältnis | ca. 63 % : 37 % |

---

## 2. Kanonische Gliederungsstruktur

Nahezu alle Notebooks (23 von 25) folgen diesem Schema:

| Nr. | Abschnitt | Beschreibung |
|-----|-----------|--------------|
| 1 | **Titel mit Emoji** | z. B. *„07 – Funktionen: Wiederverwendbare Code-Bausteine 🎯"* |
| 2 | **Willkommen / Einstieg** | Persönliche Ansprache, Alltagsmetapher oder Praxisszenario |
| 3 | **Lernziele** | Bullet-Point-Liste („Was Sie in diesem Notebook lernen") |
| 4 | **Voraussetzungen** | Verweise auf frühere Notebooks |
| 5 | **Kernkonzepte (3–8 Kapitel)** | Pro Konzept: Theorie → Beispielcode → Angeleitete Übung |
| 6 | **Abschlussübungen** | Teil 1: Grundlagen / Teil 2: Transfer & Problemlösung |
| 7 | **Zusammenfassung** | Tabelle oder Bullet-Points der Kernerkenntnisse |
| 8 | **Musterlösungen** | Ausklappbar in `<details>`-Tags |
| 9 | **Ausblick** | Verweis auf das nächste Notebook |

**Abweichungen:** NB 15 (Suchalgorithmen, nur 12 Zellen – Fragment) und NB 01 (rein theoretisch, kein Code).

---

## 3. Wiederkehrende didaktische Elemente

### 3.1 Emoji-System

- **Funktion:** Visuelle Gliederung und emotionale Anker
- **Häufigkeit:** Durchschnittlich 30–50 pro Notebook, höher in frühen NBs (NB 02: 94 Emojis)
- **Trend:** Abnehmende Dichte mit steigender Komplexität (von „Motivation" zu „Fokus")
- **Typische Emojis:** Fortschrittsbalken (⬜/✅), Checkmarks, Zielscheiben (🎯), Feier (🎉)

### 3.2 Fortschrittsbalken

- Visueller Lernfortschritt mit leeren/gefüllten Quadraten
- Durchschnittlich 6–31 pro Notebook (frühe NBs: mehr)

### 3.3 Aufklappbare Lösungen (`<details>`-Tags)

- Durchschnittlich ~30 pro Notebook
- Funktion: Selbstkontrolle ohne Spoiler
- Spitzenreiter: NB 12 (48 Blöcke), NB 13b (39 Blöcke)

### 3.4 Hinweiskästen / Blockquotes

- Für Best Practices, Warnungen, Tipps
- Besonders dicht in den Pandas/Matplotlib-NBs (bis zu 144 pro NB)

### 3.5 Übungsaufgaben

- **Inline-Übungen** zwischen Erklärungen („Sofort ausprobieren!", Lückentext-Code mit `# Ihr Code hier`)
- **Abschlussübungen** am Ende (zweiteilig: Verstehen + Transfer)
- Durchschnittlich 15–36 Aufgaben pro Notebook

### 3.6 Reflexionsfragen

- Offene Fragen zum Nachdenken („Warum funktioniert das?")
- Nicht in allen NBs gleich stark (am stärksten: NB 09, NB 19)

### 3.7 Alltagsmetaphern

| Notebook | Metapher |
|----------|----------|
| NB 03 | Kommentare = „Post-it-Notizen in einem Buch" |
| NB 04 | Variablen = „Schubladen" |
| NB 20 | Datenbanken = „Bibliothek" |

Besonders in den frühen Notebooks zur Konzeptverankerung eingesetzt.

### 3.8 Praxisszenarien

- Durchgehend WIW-relevante Domänen: Produktion, E-Commerce, Finanzen, Verwaltung
- NB 23: Reale Chinook-Datenbank (Musik-Shop)

---

## 4. Code-Zellen: Muster und Kennzahlen

| Phase | Notebooks | Code-Anteil | Komplexität | Output-Anteil |
|-------|-----------|-------------|-------------|---------------|
| Python-Basics | 01–06 | 0–48 % | Niedrig (1–5 Zeilen) | Selten |
| Kontrollfluss | 07–11 | 30–48 % | Mittel (4–10 Zeilen) | ~30 % |
| Algorithmen | 12–15 | 25–39 % | Mittel–Hoch (bis 43 Zeilen) | Variabel |
| Datenanalyse | 16–19 | 22–29 % | Mittel–Komplex | Nur 16a (66 %) |
| Datenbanken | 20–23 | 0–39 % | Mittel–Komplex (SQL) | 65–74 % |

**Beobachtete Muster:**

- Frühe NBs: Viele kurze Code-Zellen ohne Output (zum Selbst-Ausführen)
- Späte NBs: Weniger, aber komplexere Zellen, häufiger mit Output
- Code-Peak: NB 05 (66 Code-Zellen), NB 10 (58 Code-Zellen)

---

## 5. Progressionsmodell

| Phase | Notebooks | Charakter |
|-------|-----------|-----------|
| **Phase 1 – Grundlagen** | 01–06 | Hohe Emotion, einfache Konzepte, viele Metaphern |
| **Phase 2 – Kontrollfluss** | 07–11 | Mittlere Komplexität, error-fokussiert |
| **Phase 3 – Algorithmen** | 12–15 | Abstraktion, Visualisierung (Mermaid), Analyse |
| **Phase 4 – Datenanalyse** | 16–19 | Bibliotheks-basiert, praxisnah |
| **Phase 5 – Datenbanken** | 20–23 | Theorie→Praxis-Dualismus, reale Daten |

### Erkennbare Entwicklungen über den Kursverlauf

| Dimension | Frühe NBs (01–06) | Späte NBs (20–23) |
|-----------|--------------------|--------------------|
| Emoji-Dichte | Hoch (~94) | Niedrig (~10) |
| Code-Komplexität | 1-Zeiler | Mehrzeilige Programme |
| Selbständigkeit | Viele Lösungen, viel Scaffolding | Eigenständige Problemlösung |
| Übungsform | Lückentext, „Sofort ausprobieren!" | Transfer und Problemlösung |

---

## 6. Einzelanalyse pro Notebook

### Phase 1: Python-Basics (NB 01–06)

| Notebook | Zellen | MD / Code | Charakter | Besonderheit |
|----------|--------|-----------|-----------|--------------|
| **01** Einführung | 26 | 100 % / 0 % | Rein theoretisch | Grace-Hopper-Geschichte als Engagement |
| **02** Konsole | 82 | 68 % / 32 % | Erste Praxis, höchste Emotion | 94 Emojis, 30 Inline-Aufgaben |
| **03** Kommentare | 84 | 69 % / 31 % | Code-Qualität | Post-it-Metapher, 6 gestufte Aufgaben |
| **04** Variablen | 88 | 61 % / 39 % | Datenkonzept | ✅/❌ Markierungen für erlaubte Namen |
| **05** Einfache Datentypen | 138 | 52 % / 48 % | Code-Peak | 66 Code-Zellen, 48 Inline-Aufgaben |
| **06** Komplexe Datentypen | 147 | 62 % / 38 % | Umfangreichstes NB | 16 `<details>`-Lösungen |

### Phase 2: Kontrollfluss (NB 07–11)

| Notebook | Zellen | MD / Code | Charakter | Besonderheit |
|----------|--------|-----------|-----------|--------------|
| **07** Funktionen | 129 | 52 % / 48 % | Mittlere Komplexität | 21 Aufgaben, Scope-Konzept |
| **08** Operatoren | 148 | 61 % / 39 % | Demonstrationsgetrieben | 22 Lösungsblöcke, Übersichtstabelle |
| **09** Verzweigungen | 99 | 65 % / 35 % | Error-fokussiert | 23 Fehler-Diskussionen |
| **10** Schleifen | 162 | 64 % / 36 % | Aufgabenreichstes NB | 31 Aufgaben, max. 43 Zeilen/Zelle |
| **11** Fehlerbehandlung | 52 | 67 % / 33 % | Explorativ | 32 „Versuchen Sie"-Aufforderungen |

### Phase 3: Algorithmen (NB 12–15)

| Notebook | Zellen | MD / Code | Charakter | Besonderheit |
|----------|--------|-----------|-----------|--------------|
| **12** File I/O | 96 | 72 % / 28 % | Praxisorientiert | 48 `<details>`-Blöcke, EVA-Prinzip |
| **13a** Algorithmen Modellierung | 89 | 74 % / 26 % | Konzeptuell | 7 Mermaid-Ablaufdiagramme |
| **13b** Algorithmen Grundlagen | 78 | 72 % / 28 % | Analytisch | Big-O-Notation, Komplexitätsgrafik |
| **14** Sortieralgorithmen | 102 | 70 % / 30 % | Implementierung | Bubble/Insertion/Quicksort Vergleich |
| **15** Suchalgorithmen | 12 | 58 % / 42 % | Fragment | Kein Einstieg/Abschluss, keine Übungen |

### Phase 4: Datenanalyse (NB 16–19)

| Notebook | Zellen | MD / Code | Charakter | Besonderheit |
|----------|--------|-----------|-----------|--------------|
| **16a** Pandas Visualisierungen | 109 | 71 % / 29 % | Output-visuell | 66 % Code-Zellen mit Output |
| **16b** Pandas DataFrames | 96 | 71 % / 29 % | Konzeptionell | 202 Fett-Formatierungen, 0 % Output |
| **17** Pandas Statistik | 86 | 71 % / 29 % | Task-orientiert | mean/median/std/groupby-Methoden |
| **18** Matplotlib Grundlagen | 71 | 73 % / 27 % | Anfängerfreundlich | Kompaktestes NB, 193 Listenpunkte |
| **19** Matplotlib Vertiefung | 82 | 76 % / 24 % | Fortgeschritten | 9 Reflexionsfragen, höchste Komplexität |

### Phase 5: Datenbanken (NB 20–23)

| Notebook | Zellen | MD / Code | Charakter | Besonderheit |
|----------|--------|-----------|-----------|--------------|
| **20** Datenbanksysteme | 24 | 100 % / 0 % | Rein konzeptuell | Excel-vs-Datenbank-Vergleich |
| **21** Relationale Datenbanken | 31 | 100 % / 0 % | Strukturmodell | ERD, ACID-Prinzip, Datentypen |
| **22** SQLite Grundlagen | 67 | 61 % / 39 % | Praktische Grundlagen | CRUD-Operationen, 65 % Output |
| **23** SQLite Vertiefung | 145 | 63 % / 37 % | Fortgeschritten | Chinook-Datenbank, JOINs, 74 % Output |

---

## 7. Qualitätskriterien

### 7.1 Stärken (konsistent über alle Notebooks)

1. **Strukturelle Konsistenz** – Vorhersehbarer Aufbau reduziert kognitive Last
2. **Scaffolding** – Progressive Komplexitätssteigerung mit abnehmendem Support
3. **Multimodalität** – Text + Code + Tabellen + Metaphern + Emojis + Diagramme
4. **Selbstlern-Fähigkeit** – `<details>`-Lösungen ermöglichen asynchrones Lernen
5. **WIW-Relevanz** – Durchgehend ingenieurnahe Anwendungsszenarien
6. **Fehlerfreundlichkeit** – Häufige Fehler werden explizit thematisiert (bes. NB 09, 11)
7. **Verkettung** – Jedes Notebook verweist auf Voraussetzungen und Ausblick

### 7.2 Verbesserungspotenzial

1. **Fehlende Code-Outputs** – NB 16b, 17, 18, 19 zeigen keine Outputs (bei Visualisierungen kritisch)
2. **NB 15 unvollständig** – Nur 12 Zellen, keine Übungen, kein Einstieg/Abschluss
3. **Reflexionsfragen** – Ungleichmäßig verteilt (stark in NB 09/19, fehlend in NB 07/08/10)
4. **Lösungsdichte** – NB 08 hat 22 Lösungen aber wenig eigenständige Übungen
5. **NB 10 ohne Lösungen** – 31 Aufgaben ohne Musterlösungen können überfordern

---

## 8. Richtwerte: Das „ideale" Notebook

| Kriterium | Richtwert |
|-----------|-----------|
| Zellen gesamt | 80–120 |
| Markdown : Code | 60 : 40 |
| Code-Zellen mit Output | mind. 50 % |
| Übungsaufgaben | 10–20 (inline + Abschluss) |
| `<details>`-Lösungen | Zu jeder Übung |
| Überschriften-Ebenen | 3–4 |
| Hauptkapitel | 4–8 |
| Einstieg | Alltagsmetapher oder Praxisszenario |
| Abschluss | Zusammenfassung + Ausblick + Glückwünsche |
| Reflexionsfragen | mind. 3–5 |
| Fortschrittsbalken | Ja (mindestens Start/Ende) |
