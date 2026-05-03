---
title: "02 — Konsole"
subtitle: "Erste Unterhaltung mit dem Computer"
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

1. Wozu eine Konsole?
2. Ausgaben mit `print(...)`
3. Eingaben mit `input(...)`
4. F-Strings -- Text mit Platzhaltern
5. F-Strings + `input()` kombinieren

> **Lernziel**: Den ersten echten Dialog zwischen Programm und Mensch bauen -- mit `print`, `input` und F-Strings.

> **Wie wir heute arbeiten**: Nach jedem Konzept zeigt die Folie *Live-Demo* (ich im Terminal) und *Sofort ausprobieren* (Sie im Notebook 02).

---

# Wozu eine Konsole?

## Stummes Programm vs. sprechendes Programm

```python
"Eco-Sneaker"
"89.95"
```

$\rightarrow$ Python rechnet im Kopf, aber wir sehen nichts.

```python
print("Eco-Sneaker")
print("89.95 EUR")
```

$\rightarrow$ jetzt erscheint etwas auf dem Bildschirm.

> Die **Konsole** ist das Chat-Fenster zwischen Ihnen und dem Computer.  
> Programme **schreiben** dort hinein -- Sie **lesen** und **antworten**.

---

# `print(...)` -- der Mund des Programms

```python
print("Hallo, Welt!")
print("Willkommen bei Veggie Soles!")
```

- `print` ist eine eingebaute **Funktion**
- Die runden Klammern `()` heißen "jetzt ausführen"
- Der Text in **Anführungszeichen** wird ausgegeben (`"..."` oder `'...'`)
- Jedes `print(...)` bricht am Ende automatisch in eine **neue Zeile** um

::: demobox
**▶ Live-Demo** -- `01_print_grundlagen.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 02, Kap. 2 (Mini-Übung): Namen ausgeben, drei Begrüßungen, Satz aus drei Teilen
:::

---

# `print(...)` -- mehrere Werte und Leerzeilen

```python
print("Eco-Sneaker", "89.95", "EUR")     # mit Komma
print("---")                              # Trennlinie
print("")                                 # leere Zeile
print("Hemp-High", "109.00", "EUR")
```

- Mehrere Werte mit **Komma** -- Python setzt automatisch ein Leerzeichen dazwischen
- `print("")` (oder `print()`) erzeugt eine **leere Zeile**
- Praktisch zum Strukturieren: Überschrift, Trennlinie, Eintrag, Trennlinie, …

::: demobox
**▶ Live-Demo** -- `02_print_mehrere.py`
:::

---

# `input(...)` -- das Ohr des Programms

```python
input("Wie heißen Sie? ")
```

1. Python zeigt den **Prompt-Text** an (`"Wie heißen Sie? "`)
2. Wartet, bis Sie etwas tippen und **Enter** drücken
3. Nimmt Ihre Eingabe als **Text** entgegen

```python
print(input("Wie heißen Sie? "))
```

$\rightarrow$ fragt und gibt sofort wieder aus.

> **Wichtig für später**: `input(...)` liefert **immer Text** zurück -- auch wenn Sie eine Zahl tippen. Mehr dazu in Notebook 05.

::: demobox
**▶ Live-Demo** -- `03_input_einfach.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 02, Kap. 3 (Mini-Übung): Lieblingsfarbe, zwei Fragen nacheinander, Mini-Dialog mit drei Fragen
:::

---

# Was uns heute (noch) fehlt

```python
input("Wie heißen Sie? ")        # Antwort kommt rein...
print("...wo ist sie hin?")      # ...und ist sofort wieder weg.
```

- Heute können wir Eingaben **nicht speichern**
- Jede Antwort muss sofort verwendet (z. B. mit `print` ausgegeben) werden
- Lösung: **Variablen** -- ab Notebook 04

> Bis dahin: alle Beispiele packen `input(...)` direkt in einen `print(...)` -- so wird die Antwort genau **einmal** verwendet.

---

# F-Strings -- Text mit Platzhaltern

## Umständlich

```python
print("Eco-Sneaker", "kostet", "89.95", "EUR")
```

## Elegant

```python
print(f"Eco-Sneaker kostet 89.95 EUR")
```

- Ein **F-String** beginnt mit einem `f` **vor** dem Anführungszeichen
- Innerhalb der `{ }` steht später ein **Wert** (richtig spannend mit Variablen ab NB 04)

```python
print(f"Willkommen bei {'Veggie Soles'}!")
```

---

# F-Strings -- Anatomie

```python
f"Hallo {NAME}, willkommen in {ORT}!"
```

| Bestandteil | Bedeutung |
|---|---|
| `f` vor `"` | macht den String zum F-String |
| normaler Text | wird unverändert ausgegeben |
| `{ ... }` | Platzhalter -- wird durch den Wert ersetzt |

> **Häufige Falle**: das `f` vergessen -- dann erscheinen `{}` einfach **als Text** in der Ausgabe.

::: demobox
**▶ Live-Demo** -- `04_fstring_grundlagen.py`
:::

---

# F-String + `input(...)` -- echter Dialog

```python
print(f"Hallo {input('Wie heißen Sie? ')}, schön Sie kennenzulernen!")
```

- `input(...)` fragt
- Der Rückgabe-Text landet **direkt** im Platzhalter
- `print(...)` gibt die personalisierte Nachricht aus

## Beispielablauf

- Eingabe: `Anna`
- Ausgabe: `Hallo Anna, schön Sie kennenzulernen!`

::: demobox
**▶ Live-Demo** -- `05_dialog_kombiniert.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 02, Kap. 4 (Mini-Übung): Lieblingsspeise, Drei-Fragen-Dialog, Vorstellungsrunde
:::

---

# Cheat Card

| Aufgabe | Syntax |
|---|---|
| Text ausgeben | `print("Text")` |
| Mehrere Werte | `print("a", "b", "c")` |
| Leerzeile | `print("")` oder `print()` |
| Eingabe lesen | `input("Frage? ")` |
| Eingabe sofort ausgeben | `print(input("Frage? "))` |
| F-String | `f"Hallo {wert}"` |
| F-String + Eingabe | `print(f"Hallo {input('Name? ')}!")` |

> **Faustregel heute**: alles in einer Zeile -- ohne Variablen müssen wir die Antwort dort verwenden, wo sie ankommt.

---

# Ausblick: Notebook 03 -- Kommentare

Jetzt können Sie Code **schreiben**. Im nächsten Schritt geht es darum, Code **lesbar** zu machen:

```python
# Veggie Soles -- Tagesreport
print("Eco-Sneaker")        # unser Klassiker
print("89.95 EUR")           # aktueller Preis
```

- Einzeilige Kommentare mit `#`
- Blöcke mit `'''...'''`
- Wann kommentiert man? Wann nicht?

---

# Heute geübt

✓ Wozu die Konsole gut ist  
✓ Texte mit `print(...)` ausgeben  
✓ Mehrere Werte und Leerzeilen kombinieren  
✓ Eingaben mit `input(...)` lesen  
✓ F-Strings als Vorlagen mit Platzhaltern  
✓ Eingabe direkt in einen F-String einbauen  

::: exercisebox
**✎ Zur Vertiefung im Notebook 02:**

- "Mini-Übungen" in Kap. 2, 3, 4 (sind Sie schon mitgegangen)
- Trainingsmaterial Aufg. 1-3 (einfach): Begrüßung, Echo, personalisierte Begrüßung
- Trainingsmaterial Aufg. 4-5 (mittel): Mini-Interview, Restaurant-Bestellung
- Trainingsmaterial Aufg. 6 (Herausforderung): Kreative Geschichte mit `input` + F-String
:::
