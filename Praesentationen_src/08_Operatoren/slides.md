---
title: "08 — Operatoren"
subtitle: "Werkzeuge für Berechnungen und Entscheidungen"
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

1. Wozu Operatoren?
2. Arithmetische Operatoren
3. Vergleichsoperatoren
4. Logische Operatoren (`and`, `or`, `not`)
5. Identität (`is`) vs. Gleichheit (`==`)
6. Zugehörigkeit (`in`, `not in`)

> **Lernziel**: Operatoren als Bausteine für Geschäftslogik nutzen -- Preise rechnen, Bedingungen kombinieren, Listen prüfen.

> **Wie wir heute arbeiten**: Nach jedem Konzept zeigt die Folie *Live-Demo* (ich im Terminal) und *Sofort ausprobieren* (Sie im Notebook 08).

---

# Wozu Operatoren?

## Ohne Operatoren

```python
def brutto():
    return 100.0   # Hardcodiert -- jede Aenderung muss von Hand
```

## Mit Operatoren

```python
netto = 89.95
mwst  = 0.19
brutto = netto * (1 + mwst)             # 107.04
versandfrei = brutto >= 50              # True
```

> **Operatoren** verknuepfen Werte zu neuen Werten -- *die Sprache der Geschaeftslogik*.

---

# Arithmetische Operatoren

| Operator | Bedeutung | Beispiel |
|---|---|---|
| `+` | Addition | `89.95 + 109.00` |
| `-` | Subtraktion | `109.00 - 89.95` |
| `*` | Multiplikation | `89.95 * 3` |
| `/` | Division (float) | `100 / 3` $\to$ `33.33...` |
| `//` | Ganzzahl-Division | `100 // 3` $\to$ `33` |
| `%` | Modulo (Rest) | `100 % 3` $\to$ `1` |
| `**` | Potenz | `2 ** 10` $\to$ `1024` |

```python
brutto = netto * (1 + mwst)
```

::: demobox
**▶ Live-Demo** -- `01_arithmetik_preise.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 08, Kap. 1: Plus, Minus, Mal, Geteilt, Modulo, Potenz (sechs kleine Aufgaben)
:::

---

# Spezialfälle: `/` vs. `//` vs. `%`

```python
print(7 / 2)      # 3.5      -- echte Division, immer float
print(7 // 2)     # 3        -- Ganzzahl-Division (abrunden)
print(7 % 2)      # 1        -- Rest
print(2 ** 10)    # 1024     -- Potenz
```

## Wofür ist `%` praktisch?

```python
artikel_pro_karton = 12
bestellte_artikel  = 47
volle_kartons      = bestellte_artikel // artikel_pro_karton    # 3
einzelartikel_rest = bestellte_artikel % artikel_pro_karton     # 11
```

> **Faustregel**: `/` ergibt immer float, `//` immer int, `%` gibt den Rest.

---

# Vergleichsoperatoren

| Operator | Bedeutung | Beispiel |
|---|---|---|
| `==` | gleich | `bestand == 0` |
| `!=` | ungleich | `kunde != "gast"` |
| `<` | kleiner | `bestand < 5` |
| `>` | groesser | `betrag > 50` |
| `<=` | kleiner-gleich | `alter <= 17` |
| `>=` | groesser-gleich | `betrag >= 50` |

- Vergleichsoperatoren liefern **immer** `True` oder `False`
- Ergebnistyp: **bool**

::: demobox
**▶ Live-Demo** -- `02_vergleich_bestand.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 08, Kap. 2: `==`, `!=`, `<`, `>`, `<=`, `>=`
:::

---

# Achtung: `=` vs. `==`

```python
preis = 89.95          # ZUWEISUNG -- "Setze preis auf 89.95"
preis == 89.95         # VERGLEICH -- "Ist preis gleich 89.95?"
```

| | `=` | `==` |
|---|---|---|
| Was tut es? | weist Wert zu | vergleicht Werte |
| Ergebnis | nichts (Seiteneffekt) | `True` / `False` |
| Wo? | links eine Variable | irgendwo in einem Ausdruck |

> **Fehlerklassiker**: `if x = 5` ist Syntax-Fehler -- gemeint ist `if x == 5`.

---

# Logische Operatoren -- `and`, `or`, `not`

```python
darf_rabatt = stammkunde and bestellsumme >= 50
versandfrei = bestellsumme >= 50 or premium_mitglied
nicht_storniert = not storniert
```

## Wahrheitstabelle (Kurzform)

| `A` | `B` | `A and B` | `A or B` | `not A` |
|---|---|---|---|---|
| `True` | `True` | `True` | `True` | `False` |
| `True` | `False` | `False` | `True` | `False` |
| `False` | `True` | `False` | `True` | `True` |
| `False` | `False` | `False` | `False` | `True` |

::: demobox
**▶ Live-Demo** -- `03_logik_versandfrei.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 08, Kap. 3: Party-Bedingung (and), Museum kostenlos (or), not-Operator
:::

---

# Vorrangregeln (Operator Precedence)

Python wertet **wie in Mathe** aus:

1. `()` -- Klammern zuerst
2. `**` -- Potenz
3. `*`, `/`, `//`, `%`
4. `+`, `-`
5. Vergleiche (`==`, `<`, ...)
6. `not`
7. `and`
8. `or`

```python
# ohne Klammern -- riskant zu lesen
a = stammkunde or bestellsumme >= 50 and premium

# mit Klammern -- klar:
a = stammkunde or (bestellsumme >= 50 and premium)
```

> **Faustregel**: lieber **eine Klammer zu viel** als ein Bug, den man drei Tage sucht.

---

# `is` vs. `==` -- Identität vs. Gleichheit

```python
liste_a = [1, 2, 3]
liste_b = liste_a            # gleicher "Briefumschlag"
liste_c = [1, 2, 3]          # zweiter Umschlag, gleicher Inhalt

print(liste_a == liste_b)    # True  (gleicher Inhalt)
print(liste_a is liste_b)    # True  (identisches Objekt)
print(liste_a == liste_c)    # True  (gleicher Inhalt)
print(liste_a is liste_c)    # False (anderes Objekt!)
```

- `==` fragt: **"Sind die Werte gleich?"** (fast immer das, was Sie wollen)
- `is`  fragt: **"Ist es dasselbe Objekt im Speicher?"**

> Praktischer Einsatz von `is`: nur fuer `is None`, `is True`, `is False`.

::: demobox
**▶ Live-Demo** -- `05_identitaet_vs_gleichheit.py`
:::

---

# `in` und `not in` -- Zugehörigkeit

```python
warenkorb = ["Eco-Sneaker", "Hemp-High"]

print("Eco-Sneaker" in warenkorb)        # True
print("Bambus-Boot" not in warenkorb)    # True
```

- Funktioniert mit **Listen, Tupeln, Sets, Dicts und Strings**
- Bei Strings prueft `in` Teil-Strings:

```python
"sneaker" in "Eco-Sneaker".lower()        # True
```

::: demobox
**▶ Live-Demo** -- `04_zugehoerigkeit_warenkorb.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 08, Kap. 4: `is`-Operator, `in` mit Lieblingszahlen, `not in` mit Benutzernamen, `pruefe_liste`-Funktion
:::

---

# Cheat Card

| Klasse | Operatoren |
|---|---|
| Arithmetik | `+ - * / // % **` |
| Vergleich | `== != < > <= >=` |
| Logik | `and or not` |
| Identität | `is`, `is not` |
| Zugehörigkeit | `in`, `not in` |
| Zuweisung | `=`, `+=`, `-=`, `*=`, `/=` |

> **Faustregel**: Vergleichs- und Logikoperatoren liefern `bool`. Genau diese `bool`-Werte brauchen wir ab Notebook 09 fuer `if`/`elif`/`else`.

---

# Ausblick: Notebook 09 -- Verzweigungen

Operatoren liefern Wahrheitswerte -- damit kann das Programm endlich **entscheiden**:

```python
if bestellsumme >= 50 and stammkunde:
    print("versandfrei")
elif bestellsumme >= 50:
    print("Versand 2.95 EUR")
else:
    print("Versand 4.95 EUR")
```

`if`, `elif`, `else` und `match` waeren ohne Vergleichs- und Logikoperatoren stumm.

---

# Heute geübt

✓ Arithmetik: `+ - * / // % **`  
✓ `/` vs. `//` vs. `%` praktisch nutzen  
✓ Vergleiche: `==`, `!=`, `<`, `>`, `<=`, `>=`  
✓ Logik: `and`, `or`, `not` mit Wahrheitstabellen  
✓ `is` vs. `==` -- Identität vs. Gleichheit  
✓ `in` / `not in` auf Listen und Strings  

::: exercisebox
**✎ Zur Vertiefung im Notebook 08:**

- "Sofort ausprobieren"-Aufgaben in Kap. 1-4 (sind Sie schon mitgegangen)
- "Grosse Uebungen" am Ende jedes Kapitels: Restaurant-Rechnung, Schaltjahr-Pruefung, kombinierte Bedingungen
- Trainingsmaterial mit Musterloesungen am Notebook-Ende
:::
