---
title: "09 — Programmverzweigungen"
subtitle: "Entscheidungen im Code mit if, elif, else, match"
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

1. Wozu Verzweigungen?
2. `if` -- die Wenn-Anweisung
3. `if-else` -- entweder / oder
4. `elif` -- mehrere Stufen
5. Bedingungen kombinieren mit `and`/`or`
6. `match-case` -- elegante Fallunterscheidung
7. Anti-Pattern: `== True`, `if x = 5`

> **Lernziel**: Programme treffen Entscheidungen anhand von Vergleichen aus Notebook 08.

> **Wie wir heute arbeiten**: Nach jedem Konzept zeigt die Folie *Live-Demo* (ich im Terminal) und *Sofort ausprobieren* (Sie im Notebook 09).

---

# Wozu Verzweigungen?

## Ohne Verzweigung -- Programm ist starr

```python
print("Versand: 4.95 EUR")    # immer gleich, egal wie gross der Warenkorb
```

## Mit Verzweigung -- Programm reagiert

```python
if bestellsumme >= 50:
    print("versandfrei")
else:
    print("Versand: 4.95 EUR")
```

> Verzweigungen lassen Programme **auf Daten reagieren** -- sie sind das, was Code von einer Tabelle unterscheidet.

---

# `if` -- die Wenn-Anweisung

```python
bestand = 3
if bestand < 5:
    print("Achtung -- Bestand niedrig!")
```

## Bestandteile

- `if` -- Schluesselwort
- `bestand < 5` -- **Bedingung**, liefert `True`/`False` (NB 08)
- `:` -- Doppelpunkt schliesst die Bedingung ab
- **Einrueckung** (4 Leerzeichen) -- markiert was zur if-Anweisung gehoert

> Bedingung **wahr** $\to$ Block laeuft. Bedingung **falsch** $\to$ Block wird uebersprungen.

::: demobox
**▶ Live-Demo** -- `01_if_einfach.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 09, Kap. 2: Volljaehrigkeit, Notentest, Passwort-Pruefung
:::

---

# Einrückung ist Pflicht

```python
if bestellsumme >= 50:
    print("versandfrei")           # gehoert zum if
    print("Geschenk dazu")         # gehoert zum if
print("Vielen Dank!")              # laeuft IMMER
```

- Python erkennt Bloecke an der **Einrueckung**
- Konvention: **4 Leerzeichen**, keine Tabs
- `IndentationError`, wenn die Einrueckung nicht passt

> Andere Sprachen nutzen `{ }` -- Python nutzt **Leerzeichen**. Saubere Optik = lauffaehiger Code.

---

# `if-else` -- beide Pfade

```python
if bestellsumme >= 50:
    print("versandfrei")
else:
    print("Versand: 4.95 EUR")
```

- **Genau einer** der beiden Bloecke laeuft
- `else` braucht keine eigene Bedingung -- "alles uebrige"
- Auch hier: Doppelpunkt + Einrueckung

::: demobox
**▶ Live-Demo** -- `02_if_else_versand.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 09, Kap. 3: gerade/ungerade, positiv/negativ, Volljaehrigkeit
:::

---

# `elif` -- mehrere Stufen

```python
if bestellsumme >= 100:
    rabatt = 0.10
elif bestellsumme >= 50:
    rabatt = 0.05
else:
    rabatt = 0.0
```

- Python prueft die `elif`-Bedingungen **der Reihe nach** von oben nach unten
- Sobald eine wahr ist, laeuft ihr Block -- der Rest wird **uebersprungen**
- `elif` so viele wie noetig

> **Wichtig**: Bedingungen **disjunkt** halten -- die spezifischste zuerst, die allgemeinste zuletzt.

::: demobox
**▶ Live-Demo** -- `03_elif_rabattstufen.py`
:::

---

# Bedingungen kombinieren -- `and`, `or`, `not`

```python
if stammkunde and bestellsumme >= 50:
    print("VIP-Versand")
elif bestellsumme >= 50 or premium:
    print("Standard-Versand kostenlos")
else:
    print("Versand 4.95 EUR")
```

- Operatoren aus Notebook 08 leben hier auf
- Klammern erhoehen Lesbarkeit -- besonders bei `and`/`or`-Mix

::: demobox
**▶ Live-Demo** -- `04_kombinierte_bedingungen.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 09, Kap. 4 (mehrere): Notenstufen, Wettervorhersage, Passwort-Staerke
:::

---

# `match-case` -- elegante Fallunterscheidung

```python
modell = "Eco-Sneaker"

match modell:
    case "Eco-Sneaker":
        print("Klassiker -- recyceltes Polyester")
    case "Hemp-High":
        print("Knoechelhoch -- aus Hanf")
    case "Bambus-Boot":
        print("Winterfest -- Bambusfaser")
    case _:
        print("Modell nicht im Sortiment")
```

- `case _:` ist der **Default-Fall** (wie `else`)
- Ideal fuer **gleichwertige, exakte** Vergleiche
- Verfuegbar **ab Python 3.10**

::: demobox
**▶ Live-Demo** -- `05_match_case.py`
:::

---

# `match` vs. `if-elif`

| Wann besser `match`? | Wann besser `if-elif`? |
|---|---|
| viele exakte Werte (`"A"`, `"B"`, ...) | Bereiche (`x < 18`, `x >= 65`) |
| eine Variable, viele Faelle | mehrere Variablen kombiniert |
| Code soll uebersichtlich bleiben | komplexe Bedingungen mit `and`/`or` |

```python
# besser if-elif
if alter < 18:    rabatt = 0.10
elif alter > 65:  rabatt = 0.15
else:             rabatt = 0.0

# besser match
match plz_region:
    case "10": ort = "Berlin"
    case "80": ort = "Muenchen"
    case _:    ort = "unbekannt"
```

---

# Anti-Patterns

```python
if storniert == True:        # ueberfluessig
    ...
if storniert:                # so reicht's
    ...

if x = 5:                    # SyntaxError -- = ist Zuweisung!
if x == 5:                   # so meinte man's
```

- `bool`-Werte direkt nutzen, nicht mit `True`/`False` vergleichen
- `==` (Vergleich) und `=` (Zuweisung) **strikt** trennen
- **Verschachtelte ifs** vermeiden, wenn `elif` reicht

> Code, der **nichts Falsches macht**, ist gut. Code, der zusaetzlich **leicht zu lesen** ist, ist sehr gut.

---

# Cheat Card

| Aufgabe | Syntax |
|---|---|
| eine Bedingung | `if cond:` |
| zwei Pfade | `if cond: ... else: ...` |
| mehrere Stufen | `if c1: ... elif c2: ... else: ...` |
| kombinierte Bedingung | `if a and b or not c:` |
| exakte Werte | `match x: case "a": ... case _: ...` |
| Default-Fall | `case _:` |

> **Faustregel**: zuerst Bedingung in Worten, dann in Python. Wenn Sie's nicht sagen koennen, koennen Sie's nicht programmieren.

---

# Ausblick: Notebook 10 -- Schleifen

`if` entscheidet **einmal**. Schleifen **wiederholen**:

```python
for produkt in warenkorb:
    if produkt in lager:
        print(f"{produkt}: lieferbar")
    else:
        print(f"{produkt}: nicht verfuegbar")
```

Damit lassen sich ganze Warenkoerbe, Bestellungen, Listen pruefen -- nicht nur ein Eintrag.

---

# Heute geübt

✓ `if` -- bedingt ausfuehren  
✓ `if-else` -- entweder / oder  
✓ `elif` -- mehrstufig pruefen  
✓ Bedingungen mit `and`/`or`/`not` kombinieren  
✓ `match-case` -- exakte Werte elegant verzweigen  
✓ Klassiker-Fallen `=` vs. `==` und `== True` umgangen  

::: exercisebox
**✎ Zur Vertiefung im Notebook 09:**

- "Sofort ausprobieren"-Aufgaben in Kap. 2-4 + Kap. 6 (sind Sie schon mitgegangen)
- Praktische Uebung Kap. 5 / 7: Maschinenauslastung, mehrere Maschinen
- Trainingsmaterial mit gestuften Aufgaben am Notebook-Ende
:::
