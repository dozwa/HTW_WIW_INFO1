---
title: "10 — Schleifen"
subtitle: "Wiederholungen automatisieren mit while und for"
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

1. Wozu Schleifen?
2. `while` -- Wiederholen mit Bedingung
3. Endlosschleifen vermeiden
4. `for` -- ueber Sammlungen iterieren
5. `range()` -- Zahlenfolgen
6. `break` und `continue`
7. List Comprehensions

> **Lernziel**: Wiederkehrende Aufgaben (Bestand pruefen, Summen bilden, Listen filtern) automatisieren -- statt 50 mal copy-paste.

> **Wie wir heute arbeiten**: Nach jedem Konzept zeigt die Folie *Live-Demo* (ich im Terminal) und *Sofort ausprobieren* (Sie im Notebook 10).

---

# Wozu Schleifen?

## Ohne Schleife

```python
print(warenkorb[0])
print(warenkorb[1])
print(warenkorb[2])     # was, wenn 50 Eintraege?
```

## Mit Schleife

```python
for produkt in warenkorb:
    print(produkt)
```

> **DRY** wieder einmal -- gleiche Logik einmal schreiben, beliebig oft anwenden.

---

# `while` -- Wiederholen mit Bedingung

```python
versuche = 3
while versuche > 0:
    print(f"Restversuche: {versuche}")
    versuche = versuche - 1     # auch: versuche -= 1
print("Keine Versuche mehr.")
```

- Solange die Bedingung **wahr** ist, laeuft der Block
- Bedingung wird **vor** jedem Durchlauf geprueft
- **Wichtig**: irgendetwas im Block muss die Bedingung am Ende **falsch** machen

::: demobox
**▶ Live-Demo** -- `01_while_countdown.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 10, Kap. While: Countdown 10$\to$0, Hochzaehlen 0$\to$5, gerade Zahlen
:::

---

# Endlosschleifen vermeiden

```python
versuche = 3
while versuche > 0:
    print("...")
    # versuche -= 1   # vergessen -> Endlosschleife
```

- Bei laufender Endlosschleife: **STRG+C** im Terminal
- In Jupyter: "Interrupt Kernel"

## Bewusst eingesetzt: `while True` + `break`

```python
while True:
    eingabe = input("Modell? ")
    if eingabe in ["Eco-Sneaker", "Hemp-High", "Bambus-Boot"]:
        break
    print("nicht im Sortiment, nochmal.")
```

> **Faustregel**: jede Schleife muss eine **Abbruchbedingung** haben -- sei es im Header oder ueber `break`.

---

# `for` -- ueber Sammlungen iterieren

```python
warenkorb = ["Eco-Sneaker", "Hemp-High", "Bambus-Boot"]

for produkt in warenkorb:
    print(produkt)
```

- `for VAR in SAMMLUNG:` -- in jedem Durchlauf bekommt `VAR` den naechsten Wert
- Funktioniert mit **Listen, Tupeln, Sets, Strings, Dicts**
- Beendet sich automatisch, wenn alle Elemente abgearbeitet sind

::: demobox
**▶ Live-Demo** -- `02_for_produkte.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 10, Kap. For: Liste ausgeben, gegen Schwellenwert pruefen, Strings durchgehen
:::

---

# `range()` -- Zahlenfolgen erzeugen

```python
for i in range(5):           # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):        # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 21, 5):    # 0, 5, 10, 15, 20
    print(i)
```

| Form | Bedeutung |
|---|---|
| `range(stop)` | 0, 1, ..., stop-1 |
| `range(start, stop)` | start, ..., stop-1 |
| `range(start, stop, step)` | mit Schrittweite |

> Die obere Grenze ist **exklusiv** -- typische Anfaenger-Falle: `range(1, 10)` geht **nicht** bis 10.

---

# Summen, Mittelwerte -- klassische for-Muster

```python
preise = [89.95, 109.00, 135.50]

# Summe
gesamt = 0
for p in preise:
    gesamt = gesamt + p

# Mittelwert
mittel = gesamt / len(preise)

print(f"Gesamt: {gesamt:.2f} EUR, Mittel: {mittel:.2f} EUR")
```

- "Sammelvariable" (`gesamt`) **vor** der Schleife auf den Startwert
- In jedem Durchlauf erweitern
- Nach der Schleife auswerten

::: demobox
**▶ Live-Demo** -- `03_for_range_summe.py`
:::

---

# `break` und `continue`

```python
for produkt in warenkorb:
    if produkt == "Bambus-Boot":
        break                 # Schleife komplett verlassen
    print(produkt)

for preis in preise:
    if preis > 100:
        continue              # diesen Durchlauf ueberspringen
    print(f"guenstig: {preis}")
```

| Anweisung | Wirkung |
|---|---|
| `break` | Schleife sofort beenden |
| `continue` | Rest des Durchlaufs ueberspringen, naechster Wert |

::: demobox
**▶ Live-Demo** -- `04_break_continue.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 10, Kap. break/continue: Suche abbrechen, ungerade Zahlen ueberspringen
:::

---

# Schleife ueber ein Dictionary

```python
preise = {"Eco-Sneaker": 89.95, "Hemp-High": 109.00, "Bambus-Boot": 135.50}

for name, preis in preise.items():
    print(f"{name}: {preis} EUR")
```

| Methode | Was kommt im Durchlauf |
|---|---|
| `for k in d:` | nur Schluessel |
| `for v in d.values():` | nur Werte |
| `for k, v in d.items():` | Paare |

::: demobox
**▶ Live-Demo** -- `05_for_dict_warenkorb.py`
:::

---

# List Comprehensions -- kompakter for

## Klassisch

```python
brutto = []
for p in [89.95, 109.00, 135.50]:
    brutto.append(p * 1.19)
```

## Comprehension

```python
brutto = [p * 1.19 for p in [89.95, 109.00, 135.50]]
```

## Mit Filter

```python
guenstig = [p for p in preise if p < 100]
```

> Comprehensions sind **kuerzer**, aber nur sinnvoll, wenn der Ausdruck **eine Zeile** bleibt. Im Zweifel: klassische `for`-Schleife.

---

# Cheat Card

| Aufgabe | Syntax |
|---|---|
| while-Schleife | `while cond: ...` |
| for ueber Liste | `for x in liste: ...` |
| Zahlenfolge | `for i in range(start, stop, step):` |
| Dict iterieren | `for k, v in d.items():` |
| Schleife verlassen | `break` |
| Durchlauf ueberspringen | `continue` |
| Liste bauen | `[ausdruck for x in liste if cond]` |

> **Faustregel**: feste Anzahl Wiederholungen $\to$ `for`. Unbekannte Anzahl bis Ereignis $\to$ `while`.

---

# Ausblick: Notebook 11 -- Fehlerbehandlung

Schleifen + Eingaben + Daten = **Dinge gehen schief**:

```python
for eintrag in eingaben:
    zahl = int(eintrag)         # ValueError, wenn keine Zahl
    print(1 / zahl)             # ZeroDivisionError, wenn 0
```

Im naechsten Notebook: **`try`/`except`** -- Programme robust gegen Fehler machen, statt sie crashen zu lassen.

---

# Heute geübt

✓ `while` -- bedingte Wiederholung  
✓ Endlosschleifen erkannt und vermieden  
✓ `for` ueber Listen, Strings, Dicts  
✓ `range()` fuer Zahlenfolgen  
✓ `break` / `continue` -- Schleifensteuerung  
✓ List Comprehensions als Kurzform  

::: exercisebox
**✎ Zur Vertiefung im Notebook 10:**

- "Sofort ausprobieren"-Aufgaben in jedem Kapitel
- Praktische Uebung: Bestandsaufnahme mit `while True` + `break`
- Trainingsmaterial: gestufte Aufgaben (Quadratzahlen, FizzBuzz, Filterung)
:::
