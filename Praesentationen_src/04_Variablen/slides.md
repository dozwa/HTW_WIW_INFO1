---
title: "04 — Variablen"
subtitle: "Werte in benannten Schubladen speichern"
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

1. Wozu Variablen? -- Werte wiederverwenden
2. Was ist eine Variable? (Schubladen-Analogie)
3. Wertzuweisung mit `=`
4. Werte überschreiben
5. Variablennamen -- erlaubt vs. verboten
6. Konventionen für gute Namen
7. Mehrfachzuweisung

> **Lernziel**: Daten unseres Veggie-Soles-Shops in Variablen speichern und gezielt weiterverwenden.

> **Wie wir heute arbeiten**: Nach jedem Konzept zeigt die Folie *Live-Demo* (ich im Terminal) und *Sofort ausprobieren* (Sie im Notebook 04).

---

# Wozu Variablen?

## Ohne Variable

```python
print("Eco-Sneaker kostet 89.95 EUR")
print("Eco-Sneaker hat 4.5 Sterne")
print("Eco-Sneaker liegt 42 mal auf Lager")
```

## Mit Variable

```python
produkt = "Eco-Sneaker"
print(f"{produkt} kostet 89.95 EUR")
print(f"{produkt} hat 4.5 Sterne")
print(f"{produkt} liegt 42 mal auf Lager")
```

> **Variable** = Wert, der einen **Namen** bekommt. Ändert sich der Wert, ändert er sich an allen Stellen automatisch.

---

# Was ist eine Variable?

- Eine **benannte Schublade** im Speicher
- Enthält genau **einen Wert** (Zahl, Text, Liste, ...)
- Wird über ihren **Namen** angesprochen
- Kann jederzeit einen **neuen Wert** bekommen

```python
preis = 89.95            # Schublade "preis" enthält 89.95
preis = 79.95            # gleiche Schublade, neuer Wert
```

> Der Name **bleibt** -- der Wert kann sich **ändern**.

---

# Wertzuweisung mit `=`

```python
produktname = "Eco-Sneaker"
preis = 89.95
auf_lager = 42
```

- Links: **Variablenname**
- Rechts: **Wert**
- `=` ist **kein Vergleich** (das wäre `==`), sondern **Zuweisung**
- Lese-Richtung: *„weise den Wert rechts an die Variable links zu"*

::: demobox
**▶ Live-Demo** -- `01_erste_variable.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 04, Kap. 1: `lieblingsfarbe`, `punktzahl`, `vorname`/`nachname`
:::

---

# Werte überschreiben

```python
bestand = 42
print(bestand)            # 42

bestand = 5               # Verkauf: 37 Paar weg
print(bestand)            # 5

bestand = bestand - 1     # nochmal 1 verkauft
print(bestand)            # 4
```

- Eine Variable kann **beliebig oft** neu zugewiesen werden
- Der **alte Wert ist weg** -- nicht in der Schublade
- `bestand = bestand - 1` heißt: *neuer Bestand = alter Bestand minus 1*

::: demobox
**▶ Live-Demo** -- `02_werte_aendern.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 04, Kap. 2: `stadt` von Berlin → München, `leben`-Variable
:::

---

# Variablennamen -- was ist erlaubt?

## Erlaubt

- Buchstaben, Zahlen, Unterstrich `_`
- Beginnen mit Buchstaben oder `_`
- Beliebig lang
- Groß-/Kleinschreibung wird unterschieden (`Preis` $\neq$ `preis`)

## Verboten

- Beginnen mit Zahl: `1produkt` -- **Fehler**
- Sonderzeichen: `produkt-name`, `preis$` -- **Fehler**
- Reservierte Wörter: `class`, `if`, `for`, `def` -- **Fehler**
- Leerzeichen: `mein produkt` -- **Fehler**

---

# Konventionen für gute Namen

| Stil | Beispiel | Wofür |
|---|---|---|
| `snake_case` | `produktname`, `auf_lager` | normale Variablen |
| `GROSSBUCHSTABEN` | `MWST_SATZ`, `VERSANDPAUSCHALE` | Konstanten |
| sprechend | `kunden_email` statt `ke` | immer! |

```python
# schlecht
x = 89.95
p1 = "Eco-Sneaker"

# gut
preis_eco_sneaker = 89.95
produkt_name = "Eco-Sneaker"
```

> **Aussagekräftige Namen** sind die wichtigste Form von Doku.

::: demobox
**▶ Live-Demo** -- `03_namen_konventionen.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 04, Kap. 3: erlaubte vs. verbotene Namen
:::

---

# Mehrfachzuweisung

```python
# Mehrere Werte in einer Zeile
name, preis, bestand = "Eco-Sneaker", 89.95, 42

# Allen denselben Wert zuweisen
a = b = c = 0

# Werte tauschen (Python-Spezialität)
preis_alt, preis_neu = preis_neu, preis_alt
```

- Praktisch für **Tupel-Entpacken** (kommt später bei Funktionen wieder)
- Reihenfolge zählt: das *n*-te Wort links bekommt den *n*-ten Wert rechts

::: demobox
**▶ Live-Demo** -- `04_mehrfachzuweisung.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 04, Kap. 4: Mehrfachzuweisung mit drei Werten, Werte tauschen
:::

---

# Cheat Card

| Aufgabe | Syntax |
|---|---|
| Wert speichern | `name = wert` |
| Wert ändern | `name = neuer_wert` |
| Mit altem Wert rechnen | `bestand = bestand - 1` |
| Mehrere zuweisen | `a, b = 1, 2` |
| Konstante (Konvention) | `MWST_SATZ = 0.19` |
| Werte tauschen | `a, b = b, a` |

> Erlaubt: Buchstaben, Zahlen, `_` -- nicht am Anfang Zahl, keine Sonderzeichen, keine Schlüsselwörter.

---

# Ausblick: Notebook 05 -- einfache Datentypen

Variablen können verschiedene **Typen** von Werten halten:

```python
text = "Eco-Sneaker"      # str (String)
preis = 89.95             # float
bestand = 42              # int
verfuegbar = True         # bool
```

Im nächsten Notebook lernen Sie, was diese Typen können -- und wie Sie zwischen ihnen umwandeln.

---

# Heute geübt

✓ Variable als benannte Schublade verstanden  
✓ Werte mit `=` zugewiesen und überschrieben  
✓ Erlaubte und verbotene Namen unterschieden  
✓ Konventionen für gute Namen gelernt  
✓ Mehrfachzuweisung genutzt  

::: exercisebox
**✎ Zur Vertiefung im Notebook 04:**

- "Sofort ausprobieren"-Aufgaben in Kap. 1-4 (sind Sie schon mitgegangen)
- Trainingsmaterial am Ende: gestufte Aufgaben zu Variablennamen, Wertzuweisung und Mehrfachzuweisung
:::
