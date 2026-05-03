---
title: "11 — Fehlerbehandlung"
subtitle: "Programme mit try / except / finally robust machen"
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

1. Wozu Fehlerbehandlung?
2. Was ist eine **Exception**?
3. `try` / `except` -- Fehler abfangen
4. **Spezifische** Exception-Typen
5. Wichtige Exceptions im Ueberblick
6. Der `finally`-Block
7. Best Practices

> **Lernziel**: Programme bauen, die nicht crashen, wenn der Anwender unsinnige Eingaben macht.

> **Wie wir heute arbeiten**: Nach jedem Konzept zeigt die Folie *Live-Demo* (ich im Terminal) und *Sofort ausprobieren* (Sie im Notebook 11).

---

# Wozu Fehlerbehandlung?

## Ohne Behandlung

```python
preis_text = input("Preis? ")
preis = float(preis_text)        # User tippt "neunundachtzig"
                                 # -> ValueError, Programm bricht ab
```

## Mit Behandlung

```python
try:
    preis = float(input("Preis? "))
except ValueError:
    print("Bitte eine Zahl wie 89.95 eingeben.")
```

> **Robust** = das Programm laeuft auch dann sinnvoll weiter, wenn aussen etwas schief geht.

---

# Was ist eine Exception?

```text
Traceback (most recent call last):
  File "rechnung.py", line 5, in <module>
    summe = 100 / 0
ZeroDivisionError: division by zero
```

- Eine **Exception** ("Ausnahme") ist Pythons Art, "etwas ist schiefgelaufen" zu signalisieren
- Das Traceback zeigt **wo** und **was**
- **Unbehandelt** $\to$ Programm endet sofort
- **Behandelt** $\to$ wir entscheiden, was passieren soll

---

# `try` / `except` -- die Grundstruktur

```python
try:
    # Code, der eventuell schiefgehen koennte
    bestellung = int(input("Stueckzahl? "))
    print(f"OK, {bestellung} Stueck")
except:
    # Was tun, wenn ein Fehler auftritt?
    print("Eingabe nicht verstaendlich.")
```

| Block | Wann laeuft er? |
|---|---|
| `try:` | immer (bis zum ersten Fehler) |
| `except:` | nur wenn im try eine Exception fliegt |

::: demobox
**▶ Live-Demo** -- `01_try_except_einfach.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 11, Angeleitete Uebung 1.1: Division mit Eingabe absichern
:::

---

# Spezifische Exception-Typen

```python
try:
    pi     = float(input("Pi? "))
    radius = float(input("Radius? "))
    umfang = 2 * pi * radius
except ValueError:
    print("Bitte gueltige Zahlen eingeben.")
except ZeroDivisionError:
    print("Division durch Null nicht erlaubt.")
```

- Jede `except`-Klausel **fuer einen Fehlertyp**
- Reihenfolge: spezifisch zuerst, allgemein zuletzt
- **Bare `except:`** (ohne Typ) faengt **alles** -- nur sehr selten gewollt

::: demobox
**▶ Live-Demo** -- `02_spezifische_exceptions.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 11, Angeleitete Uebung 2.1: Kreisumfang mit ValueError
:::

---

# Wichtige Exception-Typen

| Typ | Wann tritt er auf? | Beispiel |
|---|---|---|
| `ValueError` | richtiger Typ, falscher Wert | `int("abc")` |
| `TypeError` | falscher Typ fuer Operation | `"Hallo" + 5` |
| `ZeroDivisionError` | Teilen durch Null | `10 / 0` |
| `KeyError` | Schluessel im Dict fehlt | `preise["Sandale"]` |
| `IndexError` | Listenindex zu gross | `liste[99]` |
| `FileNotFoundError` | Datei existiert nicht | `open("fehlt.txt")` |

> Fast jede Exception bekommt am Ende ein "Error" oder "Exception" -- Klassennamen helfen beim Lesen des Tracebacks.

---

# Mehrere Exceptions kompakt

```python
try:
    eintrag = preise[modell]
    pro_stueck = gesamt / anzahl
except (KeyError, ZeroDivisionError):
    print("Pruefen Sie Modell und Stueckzahl.")
```

- Mehrere Typen in einem `except` mit **Tupel**
- Praktisch, wenn die Reaktion fuer beide gleich ist

```python
except ValueError as e:
    print(f"Fehler: {e}")
```

- `as e` -- Exception-Objekt einfangen, um die Meldung anzuzeigen

---

# Der `finally`-Block -- immer aufraeumen

```python
try:
    summe = 100 / int(input("Teiler? "))
    print(summe)
except ZeroDivisionError:
    print("Null geht nicht.")
except ValueError:
    print("Keine Zahl.")
finally:
    print("Pruefung abgeschlossen.")
```

- `finally` laeuft **immer** -- mit oder ohne Fehler, mit oder ohne `except`-Treffer
- Typisch fuer **Aufraeumen**: Datei schliessen, Verbindung trennen, Statusmeldung

::: demobox
**▶ Live-Demo** -- `03_finally_block.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 11, Angeleitete Uebung 3.1: try/except/finally mit Statusmeldung
:::

---

# Schleife + try/except -- robuste Eingabe

```python
while True:
    try:
        anzahl = int(input("Wie viele Eco-Sneaker? "))
        break
    except ValueError:
        print("Bitte eine ganze Zahl, z. B. 3.")
print(f"OK, {anzahl} Stueck.")
```

- `while True` + `break` aus Notebook 10
- Bei jeder **falschen** Eingabe nur Hinweis + erneut fragen
- Bei der **ersten** korrekten Eingabe verlaesst `break` die Schleife

::: demobox
**▶ Live-Demo** -- `04_eingabe_validieren.py`
:::

---

# Best Practices -- und was zu vermeiden ist

```python
# schlecht:
try:
    ...
except:                          # alles schlucken -- inkl. KeyboardInterrupt
    pass                         # und dann gar nichts tun

# gut:
try:
    ...
except (ValueError, TypeError) as e:
    print(f"Eingabe-Fehler: {e}")
```

| Tu | Lass |
|---|---|
| Spezifische Exceptions abfangen | `except:` ohne Typ |
| Hilfreiche Meldung ausgeben | stillschweigend ignorieren |
| Nur den Code im `try` halten, der wirklich fehlerhaft sein kann | ganze Funktionen umhuellen |

---

# Cheat Card

| Aufgabe | Syntax |
|---|---|
| Fehler abfangen | `try: ... except Type: ...` |
| Mehrere Typen | `except (T1, T2): ...` |
| Meldung lesen | `except T as e: print(e)` |
| Immer ausfuehren | `finally: ...` |
| Eingabe absichern | `while True: try ... except ...` |

> **Faustregel**: Fehlerbehandlung ist **fuer den Anwender da**, nicht zum Verstecken eigener Bugs. Fangen Sie nur, wovon Sie wissen, *was* Sie tun.

---

# Ausblick: Notebook 12 -- File I/O

Dateien sind ein **Hotspot** fuer Fehler -- es gibt Pfade, Berechtigungen, fehlende Dateien:

```python
try:
    with open("preise.csv") as f:
        text = f.read()
except FileNotFoundError:
    print("preise.csv fehlt -- Standardwerte werden genutzt.")
```

`try`/`except` plus `with` ist das **Standard-Muster** beim Lesen und Schreiben von Dateien.

---

# Heute geübt

✓ Was eine Exception ist und wie ein Traceback aussieht  
✓ `try` / `except` als Grundstruktur  
✓ Spezifische Exception-Typen unterscheiden  
✓ Mehrere `except`-Bloecke kombinieren  
✓ `finally` fuer garantierte Aufraeumarbeit  
✓ Robuste Eingabe-Schleife mit `while True`  

::: exercisebox
**✎ Zur Vertiefung im Notebook 11:**

- Angeleitete Uebungen 1.1, 1.2, 2.1, 3.1 (sind Sie schon mitgegangen)
- Abschlussuebungen Teil 1 (Grundlagen) und Teil 2 (Transfer)
- Musterloesungen am Notebook-Ende zur Selbstkontrolle
:::
