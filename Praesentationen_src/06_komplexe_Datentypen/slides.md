---
title: "06 — Komplexe Datentypen"
subtitle: "Listen, Tupel, Sets, Dictionaries"
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

1. Wozu Sammlungen? -- mehrere Werte unter einem Namen
2. **Listen** -- geordnet, veränderbar
3. **Tupel** -- geordnet, unveränderbar
4. **Sets** -- ungeordnet, ohne Duplikate
5. **Dictionaries** -- Schlüssel-Wert-Paare
6. Welche Sammlung wann?

> **Lernziel**: Veggie-Soles-Warenkorb, Produktkatalog und Bestellungen mit dem passenden Sammlungstyp modellieren.

> **Wie wir heute arbeiten**: Nach jedem Konzept zeigt die Folie *Live-Demo* (ich im Terminal) und *Sofort ausprobieren* (Sie im Notebook 06).

---

# Wozu Sammlungen?

Bisher: **eine** Variable hält **einen** Wert.

```python
produkt_1 = "Eco-Sneaker"
produkt_2 = "Hemp-High"
produkt_3 = "Bambus-Boot"
```

Bei 50 Produkten? Bei dynamischen Bestellungen? Bei einem Warenkorb, der mal 2, mal 8 Artikel hat?

```python
produkte = ["Eco-Sneaker", "Hemp-High", "Bambus-Boot"]
```

> **Sammlung** = ein Name für **mehrere Werte**. Python kennt vier Sorten -- jede mit unterschiedlichen Stärken.

---

# Die vier komplexen Datentypen

| Typ | Klammer | Geordnet | Veränderbar | Duplikate |
|---|---|---|---|---|
| **Liste** | `[ ]` | ✓ | ✓ | ✓ |
| **Tupel** | `( )` | ✓ | -- | ✓ |
| **Set**  | `{ }` | -- | ✓ | -- |
| **Dictionary** | `{k:v}` | ✓ (3.7+) | ✓ | Schlüssel: nein |

```python
liste = ["Eco-Sneaker", "Hemp-High"]
tupel = ("Eco-Sneaker", 89.95)
menge = {38, 39, 40, 41}
karte = {"name": "Eco-Sneaker", "preis": 89.95}
```

---

# Listen -- die flexible Sammlung

```python
warenkorb = ["Eco-Sneaker", "Hemp-High", "Bambus-Boot"]

print(warenkorb[0])       # 'Eco-Sneaker'  (Index 0!)
print(warenkorb[-1])      # 'Bambus-Boot'  (letztes)
print(len(warenkorb))     # 3
```

- Eckige Klammern `[ ]`
- **Index** beginnt bei 0
- Negative Indizes zählen vom Ende
- Inhalt **veränderbar**

::: demobox
**▶ Live-Demo** -- `01_listen_basics.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 06, Kap. 1: Liste `städte`, Index-Zugriff
:::

---

# Listen-Operationen

```python
warenkorb.append("Jute-Runner")     # hinten dran
warenkorb.remove("Hemp-High")       # entfernen
warenkorb[0] = "Cork-Slipper"       # ueberschreiben

len(warenkorb)                       # Anzahl
"Eco-Sneaker" in warenkorb           # Pruefen
warenkorb.sort()                     # alphabetisch sortieren
```

> Listen sind die meistgenutzte Sammlung. Wenn unsicher: nimm eine Liste.

::: demobox
**▶ Live-Demo** -- `02_listen_operationen.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 06, Kap. 1: `werkzeuge` mit `append`, `tiere` mit `remove`
:::

---

# Tupel -- unveränderlich

```python
produkt = ("Eco-Sneaker", 89.95, 42)
#         (Name,         Preis, Bestand)

print(produkt[1])         # 89.95

# produkt[1] = 79.95      # TypeError -- nicht erlaubt!
```

- Runde Klammern `( )`
- **Inhalt steht fest**, kann nicht geändert werden
- Schneller als Listen, sicherer gegen Versehen
- Klassisch für **Stammdaten** und **mehrere Rückgabewerte** (NB 07)

::: demobox
**▶ Live-Demo** -- `03_tupel_immutable.py`
:::

---

# Wann Liste, wann Tupel?

| Liste | Tupel |
|---|---|
| Inhalt ändert sich | Inhalt steht fest |
| z. B. **Warenkorb** | z. B. **GPS-Koordinate** |
| z. B. **Lager-Bestand** | z. B. **(Name, Preis, ID)** |
| `[1, 2, 3]` | `(1, 2, 3)` |

> **Faustregel**: ändert sich's? → Liste. Steht fest? → Tupel.

---

# Sets -- keine Duplikate

```python
bestellte_groessen = [40, 41, 40, 42, 41, 41]
einzigartige = set(bestellte_groessen)

print(einzigartige)    # {40, 41, 42}
print(len(einzigartige))   # 3
```

- Geschweifte Klammern `{ }`
- **Reihenfolge** spielt **keine** Rolle
- **Duplikate** werden automatisch entfernt
- Schnell für „ist X drin?"

```python
groessen = {40, 41, 40, 42, 41}
print(groessen)        # {40, 41, 42}
groessen.add(43)
groessen.remove(40)
```

> Mengenoperationen (Schnitt, Vereinigung) lernen Sie zusammen mit den Operatoren in NB 08.

::: demobox
**▶ Live-Demo** -- `04_sets_unique.py`
:::

---

# Dictionaries -- Schlüssel ↔ Wert

```python
produkt = {
    "name":    "Eco-Sneaker",
    "preis":   89.95,
    "bestand": 42,
    "vegan":   True,
}

print(produkt["name"])         # 'Eco-Sneaker'
print(produkt["preis"])        # 89.95
```

- Geschweifte Klammern mit `key: value`
- Zugriff über den **Schlüssel** (nicht Index!)
- Schlüssel sind **eindeutig** -- jeder einmal
- Werte können beliebige Typen sein

> Wenn jeder Wert einen **Namen** hat → Dictionary statt Tupel/Liste.

::: demobox
**▶ Live-Demo** -- `05_dict_produkt.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 06, Kap. 4: Dictionary mit Personendaten, Werte ergänzen und ändern
:::

---

# Cheat Card

| Aufgabe | Liste | Tupel | Set | Dict |
|---|---|---|---|---|
| Erstellen | `[1,2]` | `(1,2)` | `{1,2}` | `{"k":1}` |
| Lesen | `l[0]` | `t[0]` | `x in s` | `d["k"]` |
| Hinzufügen | `l.append(x)` | -- | `s.add(x)` | `d["k"]=v` |
| Entfernen | `l.remove(x)` | -- | `s.remove(x)` | `del d["k"]` |
| Größe | `len(l)` | `len(t)` | `len(s)` | `len(d)` |

> **Welcher Typ?**  
> Reihenfolge & änderbar → **Liste**.  
> Reihenfolge & fest → **Tupel**.  
> Eindeutigkeit → **Set**.  
> Schlüssel → Wert → **Dict**.

---

# Ausblick: Notebook 07 -- Funktionen

Mit Sammlungen und Datentypen können wir jetzt **eigene Bausteine** bauen:

```python
def warenkorb_zusammenfassung(preise):
    anzahl = len(preise)
    summe = sum(preise)
    return anzahl, summe
```

Funktionen sind **wiederverwendbare Code-Bausteine** -- das mächtigste Werkzeug, das Sie diesen Monat lernen.

---

# Heute geübt

✓ Vier Sammlungstypen unterschieden  
✓ Listen erstellt, gelesen, verändert  
✓ Tupel als unveränderliche Variante verstanden  
✓ Sets für Eindeutigkeit eingesetzt  
✓ Dictionaries als Schlüssel-Wert-Speicher  

::: exercisebox
**✎ Zur Vertiefung im Notebook 06:**

- Inline-Aufgaben in Kap. 1-4 (sind Sie schon mitgegangen)
- Trainingsmaterial am Ende: gestufte Aufgaben quer durch alle vier Sammlungstypen
:::
