# Curriculum — Informatik 1 (HTW Berlin, WIW)

**Single Source of Truth** für die Themenprogression und für die Frage:
*„Welche Python-Konzepte sind bis Notebook NN bereits eingeführt?"*

Alle anderen Dokumente (CLAUDE.md, README.md, `docs/notebook_struktur.md`,
Skills, Foliensätze, Übungen) verweisen auf diese Datei, statt die
Tabellen zu duplizieren.

> **Editieren:** Änderungen an Reihenfolge, Aufteilung oder
> Konzeptzuordnung gehören **ausschließlich hierher**. Nach jeder Änderung
> einmal `grep -rni "topic progression\|verfügbare konzepte\|bis NB"`
> laufen lassen, um Stellen zu finden, die ggf. nachgezogen werden müssen.

---

## 1. Phasenübersicht

26 Notebooks (01–23 plus 13a/b, 14a/b, 16a/b), gegliedert in fünf Phasen:

| Phase | Notebooks | Themen |
|-------|-----------|--------|
| **1 — Python-Grundlagen** | 01–06 | Einführung, Konsole, Kommentare, Variablen, einfache & komplexe Datentypen |
| **2 — Kontrollfluss** | 07–11 | Funktionen, Operatoren, Verzweigungen, Schleifen, Fehlerbehandlung |
| **3 — Algorithmen** | 12–15 | File I/O, Modellierung, Algorithmen-Grundlagen, Sortier- & Suchalgorithmen |
| **4 — Datenanalyse** | 16–19 | Pandas (DataFrames, Visualisierung, Statistik), Matplotlib |
| **5 — Datenbanken** | 20–23 | Datenbanksysteme, relationale Modelle, SQLite (Grundlagen + Vertiefung) |

Suffixe `a`/`b` markieren mehrteilige Notebooks zum selben Thema:
13a/b (Algorithmen), 14a/b (Sortieren), 16a/b (Pandas).

---

## 2. Notebook-Liste (Reihenfolge)

| NB | Titel | Phase |
|----|-------|-------|
| 01 | Einführung in die Informatik | 1 |
| 02 | Konsolen-Ein- und Ausgabe | 1 |
| 03 | Kommentare | 1 |
| 04 | Variablen | 1 |
| 05 | Einfache Datentypen | 1 |
| 06 | Komplexe Datentypen | 1 |
| 07 | Funktionen | 2 |
| 08 | Operatoren | 2 |
| 09 | Verzweigungen | 2 |
| 10 | Schleifen | 2 |
| 11 | Fehlerbehandlung | 2 |
| 12 | File I/O | 3 |
| 13a | Algorithmen — Modellierung | 3 |
| 13b | Algorithmen — Grundlagen | 3 |
| 14a | Sortieralgorithmen — Teil 1 | 3 |
| 14b | Sortieralgorithmen — Teil 2 | 3 |
| 15 | Suchalgorithmen | 3 |
| 16a | Pandas — Visualisierungen | 4 |
| 16b | Pandas — DataFrames | 4 |
| 17 | Pandas — Statistik | 4 |
| 18 | Matplotlib — Grundlagen | 4 |
| 19 | Matplotlib — Vertiefung | 4 |
| 20 | Datenbanksysteme | 5 |
| 21 | Relationale Datenbanken | 5 |
| 22 | SQLite — Grundlagen | 5 |
| 23 | SQLite — Vertiefung | 5 |

---

## 3. Konzept-Verfügbarkeit (kumulativ)

**Diese Tabelle ist normativ.** Foliensätze, Demos und Übungen für
Notebook NN dürfen **nur** Konzepte aus den Zeilen `≤ NN` verwenden.
Spätere Konzepte sind tabu (auch nicht „kurz andeuten") — sonst sehen
Studierende in der Vorlesung Syntax, die noch unbekannt ist.

| Bis NB | Neu hinzu (kumulativ) |
|--------|------------------------|
| 02 | `print()`, `input()`, String-Literale, Konsolen-Ausgabe |
| 03 | + Kommentare (`#`, Docstring `"""..."""`) |
| 04 | + **Variablen**, Wertzuweisung `=`, Variablennamen, f-strings |
| 05 | + Datentypen `str`/`int`/`float`/`bool`, `type()`, String-Methoden, Operatoren auf Zahlen (`+ - * / // %`), Bool-Operatoren (`and`/`or`/`not`), `in` auf Strings, Typumwandlung |
| 06 | + Listen, Tupel, Sets, Dictionaries, Index-Zugriff, Listen-/Dict-Methoden |
| 07 | + eigene Funktionen mit `def`, Parameter, `return`, Scope |
| 08 | + Operatoren formal (Vergleich, Logik, Zuweisung, `in`/`not in` auf Sammlungen) |
| 09 | + Verzweigungen `if`/`elif`/`else`, `match`-`case` |
| 10 | + Schleifen `for`/`while`, `break`, `continue`, List Comprehensions |
| 11 | + Fehlerbehandlung `try`/`except`/`finally`, eigene Exceptions |
| 12 | + File I/O (`open`, `with`, Lesen/Schreiben) |
| 13a/b | + Algorithmen-Begriff, Pseudocode, Komplexitätsbegriff (Big-O) |
| 14a/b | + Sortieralgorithmen (Bubble, Insertion, Quick) |
| 15 | + Suchalgorithmen (linear, binär) |
| 16a/b | + Pandas: `DataFrame`, Spaltenzugriff, Filter, Plot |
| 17 | + Pandas: `mean`/`median`/`std`, `groupby` |
| 18 | + Matplotlib: `plot`, `bar`, `hist`, Achsen, Titel |
| 19 | + Matplotlib: Subplots, Stile, Legenden, Annotationen |
| 20 | + DBMS-Begriff, Excel-vs-DB |
| 21 | + Relationales Modell, ERD, ACID, Datentypen |
| 22 | + SQLite (CRUD: `SELECT`/`INSERT`/`UPDATE`/`DELETE`) |
| 23 | + SQLite-Vertiefung (`JOIN`, `GROUP BY`, Aggregation) |

---

## 4. Häufige Fallen — was ein zu früher Foliensatz versehentlich einführt

Diese Liste dient als Checkliste vor jedem `make folien-NN`:

| Schreibst du das in einem `< NN`-Foliensatz... | ...führt es ein Konzept aus NB ... ein |
|---|---|
| `x = 5` (Variable) | NB 04 |
| `f"{x}"` (f-string) | NB 04 |
| `if x > 100: ...` | NB 09 |
| `0 if x else 1` (conditional expression) | NB 09 |
| `for x in liste:` | NB 10 |
| `[x*2 for x in ...]` (list comp) | NB 10 |
| `def f(...):` | NB 07 |
| `try: ... except:` | NB 11 |
| Tupel-Entpacken `a, b = (1, 2)` | NB 06 |
| Mengenoperationen `s1 & s2`, `s1 | s2` | NB 08 |
| `open(...)` / `with` | NB 12 |
| Eigene Klassen | nicht im Curriculum |

---

## 5. Konkrete Konsequenzen pro Foliensatz (Phase 1 + Phase 2)

- **03_Kommentare**: Demos zeigen nur `print(...)` und `input(...)` mit
  Kommentaren in verschiedenen Stilen. **Keine Variablen-Zuweisungen.**
  NB 03 nutzt zwar `name = input()` als impliziten Touchpoint, führt
  Variablen aber formell nicht ein — bleib auf demselben Niveau.
- **04_Variablen**: Variablen sind das Thema. Tupel-Entpacken nur als
  expliziter „Sneak-Peek auf NB 06". Im Zweifel: weglassen.
- **05_Einfache_Datentypen**: Datentypen + ihre Methoden + Operatoren auf
  Zahlen + Bool-Ausdrücke. **Keine Listen, keine Schleifen.**
  Hinweis auf `and`/`or`/`not` ist erlaubt, aber tiefer Einstieg gehört
  formal in NB 08.
- **06_komplexe_Datentypen**: Listen / Tupel / Sets / Dicts + Methoden.
  **Keine `for`-Loops** — stattdessen Index-Zugriff `liste[0]`,
  `dict["key"]` und einzelne `print()`-Aufrufe für Demonstrationen.
  **Keine Mengenoperatoren `&`/`|`** (gehören zu NB 08).

Wenn eine konkrete Geschäftslogik (z. B. Versandkosten) `if/else`
brauchen würde: Ergebnis als **Konstante** zeigen oder das Beispiel auf
einen späteren Foliensatz verschieben.

---

## 6. Wo verwendet?

Stellen, die auf diese Datei verweisen (zum Nachziehen bei Änderungen):

- [`CLAUDE.md`](../CLAUDE.md) — Abschnitt *Topic Progression*
- [`README.md`](../README.md) — Abschnitt *Inhalt & Aufbau*
- [`docs/notebook_struktur.md`](notebook_struktur.md) — Abschnitt 5
  *Progressionsmodell*
- `.claude/skills/folien-aus-notebook/SKILL.md` (lokal, gitignored) —
  Abschnitt *Curriculum-Disziplin*
