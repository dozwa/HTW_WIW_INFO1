---
title: "03 — Kommentare"
subtitle: "Code für Menschen lesbar machen"
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
    \newenvironment{demobox}
      {\begin{tcolorbox}[colback=blue!8, colframe=blue!55, left=4pt, right=4pt, top=2pt, bottom=2pt, arc=0pt]}
      {\end{tcolorbox}}
    \newenvironment{exercisebox}
      {\begin{tcolorbox}[colback=orange!8, colframe=orange!70!black, left=4pt, right=4pt, top=2pt, bottom=2pt, arc=0pt]}
      {\end{tcolorbox}}
---

# Agenda

1. Wozu Kommentare? -- Code lesen vs. Code schreiben
2. Einzeilige Kommentare mit `#`
3. Kommentare am Zeilenende
4. Mehrzeilige Kommentare mit `'''`
5. Wann welche Kommentar-Art?

> **Lernziel**: Code so kommentieren, dass die Veggie-Soles-Logik in 6 Monaten noch verstanden wird -- auch von anderen.

> **Wie wir heute arbeiten**: Nach jedem Konzept zeigt die Folie *Live-Demo* (ich im Terminal) und *Sofort ausprobieren* (Sie im Notebook 03).

---

# Wozu Kommentare?

## Ohne Kommentar

```python
p = 89.95
v = 4.95 if p < 100 else 0
g = p + v
```

## Mit Kommentar

```python
preis = 89.95             # Eco-Sneaker
versand = 4.95 if preis < 100 else 0   # gratis ab 100 EUR
gesamtpreis = preis + versand
```

> **Code wird einmal geschrieben, aber tausendmal gelesen.** Kommentare sind für Sie selbst in 6 Monaten -- und für alle, die nach Ihnen kommen.

---

# Was Kommentare können

- **Erklären, warum** etwas so gemacht wird (nicht: was steht da)
- **Domain-Wissen festhalten** ("4.95 EUR Pauschale, gratis ab 100")
- **Komplexen Code in Schritte aufbrechen**
- **Code temporär deaktivieren** (zum Debuggen)
- **Aufgaben markieren**: `# TODO`, `# FIXME`

> Faustregel: **Schlechter Kommentar** wiederholt den Code. **Guter Kommentar** beantwortet die Frage „warum?".

---

# Einzeilige Kommentare mit `#`

```python
# Eco-Sneaker: unser Klassiker im Sortiment
produkt = "Eco-Sneaker"
preis = 89.95
```

- Beginnen mit `#` und gehen bis Zeilenende
- Python ignoriert alles ab `#`
- Können auf eigener Zeile oder am Zeilenende stehen
- **Konvention**: ein Leerzeichen nach `#`

::: demobox
**▶ Live-Demo** -- `01_einzeilige_kommentare.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 03, Kap. 1: Lieblingsgericht-Kommentar, mittlere Zeile auskommentieren, Inline-Kommentar
:::

---

# Kommentare am Zeilenende

```python
preis = 89.95              # in EUR (Brutto)
versand = 4.95             # Pauschale -- gratis ab 100 EUR
gesamtpreis = preis + versand   # was der Kunde zahlt
```

- Erklären die **konkrete** Zeile direkt nebenan
- Werden bei Code-Reviews oft genutzt
- **Nicht überstrapazieren**: wenn jede Zeile einen Kommentar braucht, ist der Code schlecht

> Lieber **wenige aussagekräftige** Kommentare als viele triviale.

---

# Mehrzeilige Kommentare mit `'''`

```python
'''
Veggie Soles -- Versandkosten-Berechnung

Pauschale: 4.95 EUR
Frei-ab-Schwelle: 100.00 EUR

Stand: SoSe 2026
'''

VERSANDPAUSCHALE = 4.95
```

- **Drei Anführungszeichen** öffnen und schließen den Block
- Erstrecken sich über beliebig viele Zeilen
- Werden auch für **Modul-Dokumentation** verwendet (am Datei-Anfang)

::: demobox
**▶ Live-Demo** -- `02_mehrzeilige_kommentare.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 03, Kap. 2: Hobbies dokumentieren, Programm-Header schreiben
:::

---

# Wann welche Kommentar-Art?

| Situation | Form |
|---|---|
| Eine Zeile knapp erklären | `# wie hier` |
| Hinweis am Zeilenende | `code  # wie hier` |
| Datei-Übersicht / Doku-Block | `'''...'''` am Datei-Anfang |
| Funktion dokumentieren | `'''...'''` als erste Zeile in der Funktion (Docstring) |
| Mehrere Zeilen Code temporär aus | mehrere `#` -- IDE hat Shortcut dafür |

::: demobox
**▶ Live-Demo** -- `03_kommentar_stilarten.py`
:::

---

# Anti-Patterns: schlechte Kommentare

```python
i = i + 1                  # i um eins erhöhen   ← überflüssig

preis = preis * 1.19       # Brutto berechnen     ← was/warum, OK

# alter Code (irgendwann mal kaputt)
# preis = preis * 1.19
# print(preis)             ← bitte löschen, nicht behalten
```

- **Überflüssig**: was der Code tut, sieht man im Code
- **Auskommentierter Code**: gehört gelöscht (Git merkt sich das)
- **Veraltet**: Kommentar widerspricht Code -- schlimmer als kein Kommentar

> Ein **schlechter** Kommentar ist schlimmer als **kein** Kommentar.

---

# Cheat Card

| Aufgabe | Syntax |
|---|---|
| Einzeiliger Kommentar | `# Erklärung` |
| Inline-Kommentar | `code  # Erklärung` |
| Mehrzeiliger Block | `'''Text Text Text'''` |
| Modul-Header | `'''...'''` als erste Zeilen einer Datei |
| Aufgabe markieren | `# TODO: ...`, `# FIXME: ...` |

> Kommentare sind keine Pflicht -- sie sind ein **Werkzeug für gute Code-Qualität**.

---

# Ausblick: Notebook 04 -- Variablen

- Werte **speichern** in benannten Schubladen
- Variablen **überschreiben**
- Erlaubte und unerlaubte Namen
- Mehrfachzuweisung in einer Zeile

```python
produktname = "Eco-Sneaker"     # Variable
preis = 89.95                   # Variable
print(produktname, preis)
```

Damit beginnt das eigentliche Programmieren.

---

# Heute geübt

✓ Wozu Kommentare gut sind  
✓ Einzeilige Kommentare mit `#`  
✓ Kommentare am Zeilenende  
✓ Mehrzeilige Kommentare mit `'''`  
✓ Anti-Patterns erkannt  

::: exercisebox
**✎ Zur Vertiefung im Notebook 03:**

- "Sofort ausprobieren"-Aufgaben in Kap. 1 und Kap. 2 (sind Sie schon mitgegangen)
- Trainingsmaterial am Ende: gestufte Aufgaben mit Musterlösungen
:::
