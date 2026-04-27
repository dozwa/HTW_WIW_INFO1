---
title: "07 — Funktionen"
subtitle: "Wiederverwendbare Code-Bausteine"
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

1. Wozu Funktionen? -- Das DRY-Prinzip
2. Anatomie einer Funktion (`def`)
3. Parameter und Argumente
4. Rückgabewerte mit `return`
5. Mehrere Rückgabewerte
6. Scope: lokal vs. global

> **Lernziel**: Eigene Funktionen schreiben, die unseren Veggie-Soles-Shop strukturieren.

> **Wie wir heute arbeiten**: Nach jedem Konzept zeigt die Folie *Live-Demo* (ich im Terminal) und *Sofort ausprobieren* (Sie im Notebook 07).

---

# Wozu Funktionen?

## Ohne Funktion

```python
print(f"Eco-Sneaker kostet 89.95 EUR")
print(f"Hemp-High kostet 109.00 EUR")
print(f"Bambus-Boot kostet 135.50 EUR")
```

## Mit Funktion

```python
def zeige_produkt(name, preis):
    print(f"{name} kostet {preis} EUR")

zeige_produkt("Eco-Sneaker", 89.95)
zeige_produkt("Hemp-High", 109.00)
zeige_produkt("Bambus-Boot", 135.50)
```

> **DRY**: *Don't Repeat Yourself* -- gleiche Logik **einmal** schreiben.

---

# Was ist eine Funktion?

- Ein **benannter Code-Block**, der eine bestimmte Aufgabe erfüllt
- Wird **einmal definiert**, kann **beliebig oft aufgerufen** werden
- Analogie: ein Rezept im Kochbuch -- einmal aufschreiben, immer wieder kochen

## Vier Vorteile

| Vorteil | Was bedeutet das? |
|---|---|
| **Wiederverwendbarkeit** | Code einmal schreiben, mehrfach nutzen |
| **Übersichtlichkeit** | Aussagekräftige Namen statt 50 Zeilen Code |
| **Wartbarkeit** | Änderungen nur an einer Stelle |
| **Testbarkeit** | Funktionen einzeln prüfen |

---

# Eingebaute Funktionen kennen Sie schon

```python
print("Hallo")            # gibt Text aus
len([1, 2, 3])            # ergibt 3
type(89.95)               # ergibt <class 'float'>
input("Name: ")           # liest Eingabe
```

- Funktionen werden mit **Namen** und **runden Klammern** aufgerufen
- In den Klammern stehen die **Argumente**
- Manche geben einen **Rückgabewert** zurück, andere nicht

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 07, Kap. 1: 3 Aufgaben mit `len`, `type`, `input`
:::

---

# Anatomie: `def`-Syntax

```python
def zeige_shop_info():
    print("Willkommen bei Veggie Soles!")
    print("Vegane Sneaker, fair produziert.")
```

## Bestandteile

- `def` -- Schlüsselwort: *jetzt kommt eine Funktion*
- `zeige_shop_info` -- aussagekräftiger Name (Snake-Case)
- `()` -- runde Klammern (auch wenn leer)
- `:` -- leitet den Funktionskörper ein
- **Einrückung** (4 Leerzeichen) -- markiert was zur Funktion gehört

::: demobox
**▶ Live-Demo** -- `01_einfache_funktion.py`
:::

---

# Funktion definieren $\neq$ aufrufen

```python
def zeige_shop_info():           # Definition
    print("Willkommen bei Veggie Soles!")

# Hier passiert noch nichts -- die Funktion ist nur "im Gedächtnis".

zeige_shop_info()                # Aufruf
zeige_shop_info()                # nochmal -- kein Problem
```

- **Definition** = Rezept aufschreiben
- **Aufruf** = Rezept kochen

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 07, Kap. 2: `zeige_info`, `trennlinie`, `zeige_liste`
:::

---

# Parameter -- die Stellschrauben

```python
def zeige_produkt(name, preis):
    print(f"{name}: {preis} EUR")

zeige_produkt("Eco-Sneaker", 89.95)
zeige_produkt("Hemp-High", 109.00)
```

- **Parameter** = Platzhalter in der Definition
- **Argumente** = konkrete Werte beim Aufruf
- Die gleiche Funktion läuft mit unterschiedlichen Eingaben

---

# Positional vs. benannt

## Positional -- Reihenfolge zählt

```python
zeige_produkt("Eco-Sneaker", 89.95)        # ok
zeige_produkt(89.95, "Eco-Sneaker")        # Unfug!
```

## Benannt -- Reihenfolge egal

```python
zeige_produkt(name="Eco-Sneaker", preis=89.95)
zeige_produkt(preis=89.95, name="Eco-Sneaker")   # auch ok
```

> Mischung erlaubt, **aber**: positional **vor** benannt.

::: demobox
**▶ Live-Demo** -- `02_funktion_mit_parametern.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 07, Kap. 3: `rechne_rechteck`, `zeige_produkt`
:::

---

# `return` -- Werte rausgeben

```python
def berechne_versand(bestellsumme):
    if bestellsumme >= 100: return 0.0
    return 4.95
```

| | `print(...)` | `return ...` |
|---|---|---|
| zeigt etwas an | ✓ | -- |
| gibt Wert zurück | -- | ✓ |
| weiterverwendbar | -- | ✓ |

::: demobox
**▶ Live-Demo** -- `03_funktion_mit_return.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 07, Kap. 4: `berechne_kreis`, `erstelle_email`
:::

---

# Mehrere Rückgabewerte

```python
def warenkorb_zusammenfassung(artikel):
    anzahl = len(artikel)
    summe = sum(artikel)
    return anzahl, summe
```

- Python packt mehrere Werte automatisch in ein **Tupel**
- Beim Aufruf in mehrere Variablen entpacken

```python
artikel_preise = [89.95, 109.00, 135.50]
n, total = warenkorb_zusammenfassung(artikel_preise)
print(f"{n} Artikel, gesamt {total:.2f} EUR")
```

::: demobox
**▶ Live-Demo** -- `04_mehrere_rueckgaben.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 07, Kap. 4: `analysiere_wort`
:::

---

# Scope: wo gilt eine Variable?

```python
# Lokal -- nur innerhalb der Funktion
def berechne_brutto(netto):
    rate = 0.19                 # lokal
    return netto * (1 + rate)
# print(rate)                   # NameError -- existiert hier nicht

# Global -- überall lesbar
VERSANDPAUSCHALE = 4.95
def versand_anzeigen():
    print(f"Versand: {VERSANDPAUSCHALE} EUR")
```

::: demobox
**▶ Live-Demo** -- `05_scope_demo.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 07, Trainingsmaterial Aufg. 9 ("Scope verstehen")
:::

---

# Cheat Card

| Aufgabe | Syntax |
|---|---|
| Funktion definieren | `def name():` |
| mit Parametern | `def name(p1, p2):` |
| positional aufrufen | `name(wert1, wert2)` |
| benannt aufrufen | `name(p2=wert2, p1=wert1)` |
| Wert zurückgeben | `return wert` |
| mehrere Werte | `return a, b` |

> **Faustregel**: ein Konzept = eine Funktion. Aussagekräftige Namen schlagen Kommentare.

---

# Ausblick: Notebook 08 -- Operatoren

- Arithmetik: `+ - * / // % **`
- Vergleich: `== != < > <= >=`
- Logik: `and or not`
- Zugehörigkeit: `in`, `not in`

Damit bauen wir aus Funktionen *echte* Geschäftslogik:

```python
def darf_rabatt_bekommen(kunde, bestellsumme):
    return kunde.stammkunde and bestellsumme >= 50
```

---

# Heute geübt

✓ DRY-Prinzip verstanden  
✓ Eigene Funktionen mit `def` definiert  
✓ Parameter (positional + benannt) genutzt  
✓ Werte mit `return` zurückgegeben  
✓ Mehrere Rückgabewerte ausgepackt  
✓ Scope: lokal vs. global unterschieden  

::: exercisebox
**✎ Zur Vertiefung im Notebook 07:**

- "Sofort ausprobieren"-Aufgaben in Kap. 1-4 (sind Sie schon mitgegangen)
- Trainingsmaterial am Ende: 9 Aufgaben in drei Schwierigkeitsstufen (einfach, mittel, Herausforderung)
:::
