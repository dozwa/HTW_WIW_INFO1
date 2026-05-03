---
title: "01 — Einführung in Programmiersprachen"
subtitle: "Was Computer verstehen -- und wie wir mit ihnen reden"
author: "HTW Berlin -- Wirtschaftsingenieurwesen"
date: "SoSe 2026"
header-includes:
  - \usepackage{etoolbox}
  - \usepackage{tcolorbox}
  - |
    \AtBeginEnvironment{longtable}{\footnotesize}
    \renewcommand{\arraystretch}{1.15}
    \renewenvironment{quote}
      {\begin{tcolorbox}[colback=gray!10, colframe=gray!50, left=4pt, right=4pt, top=2pt, bottom=2pt, arc=0pt, fontupper=\small]}
      {\end{tcolorbox}}
    \newenvironment{demobox}
      {\begin{tcolorbox}[colback=blue!8, colframe=blue!55, left=4pt, right=4pt, top=2pt, bottom=2pt, arc=0pt, fontupper=\small]}
      {\end{tcolorbox}}
    \newenvironment{exercisebox}
      {\begin{tcolorbox}[colback=orange!8, colframe=orange!70!black, left=4pt, right=4pt, top=2pt, bottom=2pt, arc=0pt, fontupper=\small]}
      {\end{tcolorbox}}
---

# Agenda

1. Was ist eine Programmiersprache?
2. Python -- unsere Wahl im Kurs
3. Interpreter vs. Compiler
4. Wo schreibt man Python? (Jupyter, VSCode)
5. Algorithmen -- Schritt-für-Schritt-Denken
6. Bugs -- Fehler gehören dazu
7. Syntax und Semantik

> **Lernziel**: Verstehen, *was* eine Programmiersprache ist und *wie* Python funktioniert -- bevor wir ab Notebook 02 selbst Code schreiben.

> **Wie wir heute arbeiten**: Diese Sitzung ist konzeptionell. *Live-Demos* sind Mini-Beispiele, *Sofort ausprobieren* zielt auf die Reflexionsfragen am Ende von Notebook 01.

---

# Mensch und Maschine -- zwei Welten

- Computer kennen nur **Einsen und Nullen**
- Menschen denken in Sätzen, Bildern, Begriffen
- Eine **Programmiersprache** ist die Brücke dazwischen

## Drei Bestandteile -- wie in jeder Sprache

| In einer Sprache gibt es... | ...in Python heißt das |
|---|---|
| Vokabeln | Befehle wie `print`, `input` |
| Grammatik | Wo Klammern, Anführungszeichen, Doppelpunkte stehen |
| Bedeutung | Was passiert, wenn der Code läuft |

> Computer sind **präzise**: ein Tippfehler -- und nichts läuft mehr.

---

# Warum Python?

- Anfang der 90er von Guido van Rossum entwickelt
- Name kommt von **Monty Python** -- nicht von der Schlange
- Heute eine der **meistgenutzten** Sprachen weltweit (Google, NASA, Spotify, Forschung, KI)

## Vier Eigenschaften, die Python anfängerfreundlich machen

- **Lesbar** -- Code sieht oft fast wie Englisch aus
- **Wenig Boilerplate** -- weniger merkwürdige Zeichen als z. B. Java oder C++
- **Vielseitig** -- Web, Daten, KI, Automatisierung, Spiele
- **Riesige Community** -- zu fast jeder Frage gibt es eine Antwort online

---

# Wie führt der Computer Python aus?

```python
print("Hallo, Welt!")
```

- Python ist eine **interpretierte Sprache**
- Der **Interpreter** übersetzt Ihren Code **Zeile für Zeile** in Maschinensprache
- Vorteil: sofort ausführbar, schnell ausprobieren, ideal zum Lernen

::: demobox
**▶ Live-Demo** -- `01_hallo_welt.py`
:::

---

# Interpreter vs. Compiler

| | **Interpretiert** (Python, JS) | **Kompiliert** (C, C++, Rust) |
|---|---|---|
| Übersetzung | zur Laufzeit, Zeile für Zeile | einmal vorab, komplett |
| Start | sofort | nach Build-Schritt |
| Ausführung | meist langsamer | meist schneller |
| Änderung testen | sofort | neu kompilieren |

> Für **Lernen, Prototypen, Datenanalyse** ist die interpretierte Welt ideal -- für hochperformante Systemsoftware oft die kompilierte.

::: demobox
**▶ Live-Demo** -- `02_interpreter_zeile_fuer_zeile.py`
:::

---

# Wo schreibt man Python?

| Werkzeug | Wann |
|---|---|
| **Jupyter Notebook** | interaktives Lernen, Daten, Mischung Text + Code |
| **VSCode** | richtige Skripte, Debugger, Terminal -- *unser Klausur-Editor* |
| Texteditor (Notepad, …) | technisch möglich, aber ohne Hilfe |
| IDE (PyCharm, Spyder) | Profi-Setup, viele Funktionen |

- In diesem Kurs: **Jupyter Notebooks** zum Lernen, **VSCode** zum Üben
- In der **Klausur** steht nur VSCode zur Verfügung

---

# Was ist ein Algorithmus?

> Eine **präzise Schritt-für-Schritt-Anleitung** zur Lösung eines Problems.

## Algorithmus „Tee zubereiten"

1. Wasser in den Wasserkocher
2. Einschalten, kochen lassen
3. Teebeutel in die Tasse
4. Wasser eingießen
5. 3-5 Minuten ziehen lassen
6. Beutel entfernen, evtl. Zucker

## Vom Problem zum Programm

Problem verstehen $\rightarrow$ Algorithmus entwerfen $\rightarrow$ Code schreiben $\rightarrow$ Testen $\rightarrow$ Optimieren

---

# Bugs -- Fehler gehören dazu

- **Bug** = Fehler im Programm
- Begriff stammt von einer **echten Motte** in einem Computer der 1940er
- **Auch Profis** machen ständig Fehler -- der Unterschied: sie wissen, wie man sie findet

## Drei Fehlerklassen

| Art | Wann tritt er auf? | Schwierigkeitsgrad |
|---|---|---|
| **Syntaxfehler** | Code verletzt die Grammatik | leicht zu finden |
| **Laufzeitfehler** | Während der Ausführung -- z. B. Division durch Null | mittel |
| **Logischer Fehler** | Code läuft, aber Ergebnis ist falsch | am schwersten |

::: demobox
**▶ Live-Demo** -- `03_syntax_fehler.py`
:::

---

# Syntax: die Grammatik

Die **Syntax** legt fest, *wie* Sie Code schreiben dürfen, damit Python ihn überhaupt versteht.

```python
print("Hallo Welt")     # ok
Print("Hallo Welt")     # NameError: Print existiert nicht
print "Hallo Welt"      # SyntaxError: Klammern fehlen
print("Hallo Welt"      # SyntaxError: Klammer nicht geschlossen
```

- Welche Zeichen sind erlaubt?
- Wo müssen Klammern, Anführungszeichen, Doppelpunkte stehen?
- Python ist **case-sensitiv**: `print` $\neq$ `Print`

> Bei Syntaxfehlern sagt Python meistens **genau**, in welcher Zeile das Problem steckt -- lesen lohnt sich.

---

# Semantik: die Bedeutung

Die **Semantik** beschreibt, *was* der Code tatsächlich tut, wenn er läuft.

## Beide Sätze sind grammatikalisch ok -- aber bedeuten verschiedenes:

- "Der Hund beißt den Mann."
- "Der Mann beißt den Hund."

## Beide Code-Schnipsel sind syntaktisch ok -- aber das Ergebnis ist verschieden:

```python
print("Eco-Sneaker kostet 89.95")
print("Eco-Sneaker kostet 98.95")    # Tippdreher -- Programm läuft
                                     # trotzdem, aber falscher Preis
```

> Syntaktisch korrekt $\neq$ semantisch korrekt. Code, der läuft, ist nicht automatisch *richtig*.

---

# Cheat Card

| Begriff | Worum geht's? |
|---|---|
| Programmiersprache | formale Sprache, um dem Computer Aufgaben zu erklären |
| Python | interpretierte, lesbare Anfänger-/Profi-Sprache |
| Interpreter | übersetzt Code Zeile für Zeile zur Laufzeit |
| Compiler | übersetzt vorab in eine fertige ausführbare Datei |
| Algorithmus | Schritt-für-Schritt-Anleitung zur Problemlösung |
| Bug | Programmfehler (Syntax / Laufzeit / Logik) |
| Syntax | formale Regeln -- wie Code aussehen muss |
| Semantik | Bedeutung -- was der Code wirklich tut |

---

# Ausblick: Notebook 02 -- Konsole

Bisher: Theorie. Ab nächster Sitzung: **echter Code**.

```python
print("Willkommen bei Veggie Soles!")
input("Wie heißen Sie? ")
```

- `print(...)` -- der **Mund** Ihres Programms
- `input(...)` -- das **Ohr** Ihres Programms
- F-Strings -- elegante, formatierte Ausgaben

So beginnt der erste Dialog zwischen Ihnen und dem Computer.

---

# Heute geübt

✓ Programmiersprachen als Brücke Mensch -- Maschine verstanden  
✓ Python in den Kontext anderer Sprachen eingeordnet  
✓ Interpreter vs. Compiler unterschieden  
✓ Algorithmus-Begriff am Alltagsbeispiel begriffen  
✓ Drei Fehlerklassen (Syntax, Laufzeit, Logik) benennen können  
✓ Syntax und Semantik unterscheiden  

::: exercisebox
**✎ Zur Vertiefung im Notebook 01:**

- **Reflexionsfragen** am Ende: Erklären Sie Syntax vs. Semantik in eigenen Worten
- **Transferfragen**: Drei Probleme aus Ihrem Alltag, die ein Programm lösen könnte
- Notebook 02 vorbereiten: Jupyter / VSCode lauffähig haben
:::
