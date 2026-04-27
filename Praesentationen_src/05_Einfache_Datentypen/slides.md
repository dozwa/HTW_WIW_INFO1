---
title: "05 — Einfache Datentypen"
subtitle: "str, int, float, bool"
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

1. Was sind Datentypen? -- `type()`
2. **String** (`str`) -- Text
3. **Integer** (`int`) -- ganze Zahlen
4. **Float** (`float`) -- Kommazahlen
5. **Boolean** (`bool`) -- wahr/falsch
6. Typumwandlung (`int()`, `str()`, `float()`)

> **Lernziel**: Veggie-Soles-Daten korrekt typisieren -- Preise als `float`, Namen als `str`, Bestand als `int`, Verfügbarkeit als `bool`.

> **Wie wir heute arbeiten**: Nach jedem Konzept zeigt die Folie *Live-Demo* (ich im Terminal) und *Sofort ausprobieren* (Sie im Notebook 05).

---

# Was sind Datentypen?

Jeder Wert in Python hat einen **Typ** -- der bestimmt, was damit geht:

```python
"Eco-Sneaker"  + " ist toll"   # str + str → ok
89.95          + 4.95           # float + float → ok
"89.95"        + 4.95           # str + float → FEHLER
```

Mit `type()` den Typ herausfinden:

```python
print(type(89.95))    # <class 'float'>
print(type("Eco"))    # <class 'str'>
print(type(42))       # <class 'int'>
print(type(True))     # <class 'bool'>
```

> **Datentyp** = die "Sorte" eines Wertes. Operationen sind nur zwischen passenden Typen erlaubt.

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 05, Kap. 1: Datentyp herausfinden bei Name, Zahl, "123" als String
:::

---

# String -- Text (`str`)

```python
produkt   = "Eco-Sneaker"
beschreibung = 'Klassischer Low-Cut'
mehrzeilig = """Vegane Sneaker
fair produziert"""
```

- Mit **doppelten** oder **einfachen** Anführungszeichen
- **Dreifach** für mehrzeiligen Text
- Aneinanderhängen mit `+`
- Vervielfältigen mit `*`
- Länge mit `len(...)`

```python
print(produkt + " kostet 89.95 EUR")
print("=" * 30)              # 30 Gleichheitszeichen
print(len(produkt))          # 11
```

::: demobox
**▶ Live-Demo** -- `01_string_basics.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 05, Kap. 2: Lieblingsfarbe, Satz mit Anführungszeichen
:::

---

# String-Methoden

Strings haben eingebaute **Methoden** -- werden mit `.` aufgerufen:

```python
name = "Eco-Sneaker"

name.upper()         # "ECO-SNEAKER"
name.lower()         # "eco-sneaker"
name.replace("-", " ")   # "Eco Sneaker"
name.startswith("Eco")   # True
"  Anna  ".strip()   # "Anna" (Leerzeichen weg)
```

::: demobox
**▶ Live-Demo** -- `02_string_methoden.py`
:::

---

# Integer -- ganze Zahlen (`int`)

```python
bestand = 42
verkaufte_paare = 7
neuer_bestand = bestand - verkaufte_paare
```

- **Ganze Zahlen** ohne Komma -- positiv, negativ, null
- Beliebig groß (Python begrenzt nicht)
- Operatoren: `+ - * / // % **`

```python
17 / 5     # 3.4   (Division -- ergibt float)
17 // 5    # 3     (ganzzahlige Division)
17 %  5    # 2     (Rest -- "modulo")
2 ** 10    # 1024  (Potenz)
```

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 05, Kap. 3: Variable mit Zahl, Datentyp prüfen
:::

---

# Float -- Kommazahlen (`float`)

```python
preis = 89.95
mwst_satz = 0.19
brutto = preis * (1 + mwst_satz)   # 107.04..
```

- **Kommazahlen** -- Dezimalpunkt, **kein** Komma
- Auch in wissenschaftlicher Notation: `1.5e3` = 1500.0
- **Ungenau** bei manchen Berechnungen: `0.1 + 0.2 = 0.30000000000000004`

```python
print(f"Brutto: {brutto:.2f} EUR")   # auf 2 Stellen runden
```

::: demobox
**▶ Live-Demo** -- `03_zahlen_rechnen.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 05, Kap. 4: Float-Rechnungen, Rundung mit `:.2f`
:::

---

# Boolean -- wahr oder falsch (`bool`)

```python
auf_lager = True
ausverkauft = False

# Ergebnis von Vergleichen
print(89.95 > 100)            # False
print(89.95 < 100)            # True
print("Eco" in "Eco-Sneaker") # True
```

- Nur zwei Werte: `True` und `False` (groß geschrieben!)
- Ergebnis aller **Vergleiche**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Verknüpfungen `and`/`or`/`not` lernen Sie in **Notebook 08**

::: demobox
**▶ Live-Demo** -- `04_boolean_bedingungen.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 05, Kap. 5: Bedingungen, Vergleiche, `and`/`or`
:::

---

# Typumwandlung

Python wandelt **nicht automatisch** zwischen `str` und Zahl:

```python
input_text = input("Anzahl: ")     # input liefert IMMER str
anzahl = int(input_text)            # → in int wandeln

preis = 89.95
print("Preis: " + str(preis) + " EUR")   # float → str
```

| Funktion | Wandelt nach |
|---|---|
| `int(x)` | ganze Zahl |
| `float(x)` | Kommazahl |
| `str(x)` | Text |
| `bool(x)` | True/False |

::: demobox
**▶ Live-Demo** -- `05_typumwandlung.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 05, Kap. 1+3: type() ausprobieren, Eingabe in Zahl wandeln
:::

---

# Cheat Card

| Typ | Beispiel | Wofür |
|---|---|---|
| `str` | `"Eco-Sneaker"` | Texte, Namen, Beschreibungen |
| `int` | `42` | Stück, Anzahlen, IDs |
| `float` | `89.95` | Preise, Maße, Anteile |
| `bool` | `True` / `False` | Verfügbarkeit, Bedingungen |

```python
type(x)       # Typ herausfinden
int(x)        # in ganze Zahl wandeln
float(x)      # in Kommazahl wandeln
str(x)        # in Text wandeln
```

> **Faustregel**: input() liefert immer `str` -- bei Zahlen sofort umwandeln.

---

# Ausblick: Notebook 06 -- komplexe Datentypen

Einfache Datentypen halten **einen** Wert. Komplexe Datentypen halten **mehrere**:

```python
warenkorb = ["Eco-Sneaker", "Hemp-High"]    # Liste
produkt   = ("Eco-Sneaker", 89.95)          # Tupel
groessen  = {38, 39, 40, 41}                # Set
preise    = {"Eco-Sneaker": 89.95}          # Dictionary
```

Damit modellieren wir Warenkörbe, Produktkataloge und Bestellungen.

---

# Heute geübt

✓ `type()` zur Typ-Bestimmung genutzt  
✓ Strings erstellt und Methoden angewendet  
✓ Integer und Float-Operationen unterschieden  
✓ Boolean-Werte aus Vergleichen erzeugt  
✓ Typumwandlung mit `int()`, `str()`, `float()`  

::: exercisebox
**✎ Zur Vertiefung im Notebook 05:**

- "Sofort ausprobieren"-Aufgaben in Kap. 1-5 (sind Sie schon mitgegangen)
- Trainingsmaterial am Ende: gestufte Aufgaben quer durch alle vier Datentypen
:::
