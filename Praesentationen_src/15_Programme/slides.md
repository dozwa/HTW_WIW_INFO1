---
title: "15 — Python-Programme"
subtitle: "Vom Skript zum strukturierten Programm"
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

1. Vom Skript zum Programm -- warum Struktur?
2. Funktionen als Bausteine (Single Responsibility)
3. Die `main()`-Funktion -- der Dirigent
4. Das `if __name__ == "__main__":`-Idiom
5. Die 5 Bausteine einer `.py`-Datei
6. Notebook vs. `.py`-Datei
7. Häufige Fehler vermeiden

> **Lernziel**: Aus einzelnen Code-Schnipseln ein **richtiges Programm** machen -- mit klarer Struktur, die auch ein Kollege versteht.

> **Wie wir heute arbeiten**: Nach jedem Konzept zeigt die Folie *Live-Demo* (ich im Terminal) und *Sofort ausprobieren* (Sie im Notebook 15).

---

# Motivation: Spaghetti oder Bauplan?

## Ohne Struktur ("Spaghetti-Code")

```python
shop = {"Eco-Sneaker": 89.95, "Hemp-High": 109.00}
for p, preis in shop.items():
    print(f"{p}: {preis} EUR")
gesamt = 0
for preis in shop.values():
    gesamt = gesamt + preis
print(f"Summe: {gesamt} EUR")
```

- Alles auf einer Ebene -- liest sich wie eine Wäscheliste
- Nicht wiederverwendbar, schwer testbar, schwer erweiterbar

> **Faustregel**: Wird ein Skript länger als ca. 20 Zeilen, braucht es Struktur.

---

# Motivation: Mit Struktur

```python
def bestand_anzeigen(shop):
    for p, preis in shop.items():
        print(f"{p}: {preis} EUR")

def gesamtwert(shop):
    gesamt = 0
    for preis in shop.values():
        gesamt = gesamt + preis
    return gesamt

def main():
    shop = {"Eco-Sneaker": 89.95, "Hemp-High": 109.00}
    bestand_anzeigen(shop)
    print(f"Summe: {gesamtwert(shop)} EUR")

main()
```

::: demobox
**▶ Live-Demo** -- `01_spaghetti_vs_strukturiert.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 15, Kap. 1: Übung 1.1 ("Drei Aufgaben erkennen")
:::

---

# Funktionen als Bausteine

## Single Responsibility: eine Funktion, eine Aufgabe

| Schlecht | Besser |
|---|---|
| `daten_laden_und_speichern()` | `daten_laden()` + `daten_speichern()` |
| `berechne_und_zeige()` | `berechne()` + `zeige()` |
| `pruefen_und_senden()` | `pruefen()` + `senden()` |

> **Test**: Wenn Sie die Funktion mit "und" beschreiben müssen, sind es vermutlich **zwei** Funktionen.

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 15, Kap. 2: Übung 2.1 (`durchschnitt_berechnen`, `beste_note_finden`, `bestanden_zaehlen`)
:::

---

# Funktionen rufen Funktionen auf

```python
def bericht_erstellen(shop):
    """Erstellt einen Lagerbericht."""
    print("=== Veggie Soles Bericht ===")
    bestand_anzeigen(shop)
    summe = gesamtwert(shop)
    print(f"Lagerwert: {summe:.2f} EUR")
```

- `bericht_erstellen` muss **nicht wissen**, *wie* der Bestand angezeigt wird
- Sie delegiert -- die Details stecken in `bestand_anzeigen`
- Das nennt man **Abstraktion**: Schichten von Bedeutung

::: demobox
**▶ Live-Demo** -- `02_funktionen_als_bausteine.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 15, Kap. 2: Übung 2.2 (`notenbericht_erstellen` kombiniert die drei Funktionen)
:::

---

# Die `main()`-Funktion -- der Dirigent

```python
def main():
    """Hauptprogramm: Veggie Soles Shop."""
    shop = {"Eco-Sneaker": 89.95, "Hemp-High": 109.00,
            "Bambus-Boot": 135.50}
    bestand_anzeigen(shop)
    print(f"Lagerwert: {gesamtwert(shop):.2f} EUR")

main()
```

- **Steuert den Ablauf** -- ruft Hilfsfunktionen in der richtigen Reihenfolge auf
- **Enthält selbst wenig Logik** -- die steckt in den Hilfsfunktionen
- **Liest sich wie eine Zusammenfassung** Ihres Programms

::: demobox
**▶ Live-Demo** -- `03_main_funktion.py`
:::

---

# Was gehört in `main()` -- und was nicht?

| Gehört in `main()` | Gehört NICHT in `main()` |
|---|---|
| Programmablauf steuern | Funktionsdefinitionen |
| Hilfsfunktionen aufrufen | Import-Anweisungen |
| Anfangsdaten bereitstellen | Konstanten-Definitionen |
| Benutzereingaben (wenn nötig) | Komplexe Berechnungslogik |
| Ergebnisse ausgeben | Hilfsfunktionen |

> **Test**: Wer nur `main()` liest, versteht **was** das Programm tut -- ohne **wie**.

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 15, Kap. 3: Übung 3.1 (`main()` für Notenauswertung), Übung 3.2 (Refaktorisieren)
:::

---

# Das `if __name__ == "__main__":`-Idiom

```python
# shop_utils.py
def bestand_anzeigen(shop):
    for p, preis in shop.items():
        print(f"{p}: {preis} EUR")

def main():
    bestand_anzeigen({"Eco-Sneaker": 89.95})

if __name__ == "__main__":
    main()
```

- `__name__` ist eine **eingebaute Variable**
- Direkter Aufruf (`python shop_utils.py`): `__name__` $=$ `"__main__"` → `main()` läuft
- Import (`import shop_utils`): `__name__` $=$ `"shop_utils"` → `main()` läuft **nicht**

> **Warum?** Damit Kollegen Ihre Funktionen importieren können, ohne dass nebenbei Ihr Hauptprogramm startet.

---

# Skript vs. Modul -- eine Datei, zwei Rollen

| Aspekt | Skript (direkt ausgeführt) | Modul (importiert) |
|---|---|---|
| `__name__` | `"__main__"` | Dateiname (z. B. `"shop_utils"`) |
| Zweck | Programm starten | Funktionen bereitstellen |
| Beispiel | `python shop.py` | `import shop_utils` |

> Mit `if __name__ == "__main__":` kann **dieselbe Datei beides sein** -- Skript *und* importierbares Modul.

::: demobox
**▶ Live-Demo** -- `04_modul_oder_skript.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 15, Kap. 4: Übung 4.1 (`__name__` untersuchen), Übung 4.2 (Modul-Verhalten simulieren)
:::

---

# Die 5 Bausteine einer `.py`-Datei

![](15_programme_bausteine.png){width=85%}

> Reihenfolge ist **nicht zufällig**: Was die Funktionen brauchen (Imports, Konstanten) steht oben, was sie startet, ganz unten.

---

# Vollständiges Beispiel -- Veggie Soles

```python
# --- 1. Imports ---
# (keine)

# --- 2. Konstanten ---
VERSANDPAUSCHALE = 4.95
FREI_AB = 100.00

# --- 3. Hilfsfunktionen ---
def versand_berechnen(summe):
    if summe >= FREI_AB:
        return 0.0
    return VERSANDPAUSCHALE

# --- 4. main() ---
def main():
    bestellung = [89.95, 109.00]
    summe = sum(bestellung)
    versand = versand_berechnen(summe)
    print(f"Summe: {summe:.2f} EUR, Versand: {versand:.2f} EUR")

# --- 5. Einstiegspunkt ---
if __name__ == "__main__":
    main()
```

::: demobox
**▶ Live-Demo** -- `05_veggie_soles_komplett.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 15, Kap. 5: Übung 5.1 (Einkaufsliste), Kap. 6: Übung 6.1 (Lohnberechnung in 5-Bausteine-Struktur)
:::

---

# Notebook vs. `.py`-Datei

| Aspekt | Notebook | `.py`-Datei |
|---|---|---|
| Ausführung | Zellen, beliebige Reihenfolge | Sequenziell von oben |
| Zustand | Bleibt zwischen Zellen | Frisch bei jedem Start |
| `__name__` | Immer `"__main__"` | `"__main__"` oder Modulname |
| Ideal für | Lernen, Experimentieren | Programme, Tools, Module |
| Versionierung | Schwierig (JSON) | Einfach (reiner Text) |

> **Das Notebook ist Ihre Werkbank -- die `.py`-Datei ist das fertige Produkt.**

> Im Notebook: `main()` direkt aufrufen. In der `.py`-Datei: `if __name__ == "__main__": main()`.

---

# Anti-Patterns -- was Sie vermeiden

| Anti-Pattern | Warum schlecht? |
|---|---|
| Loser Code statt Funktion | Beim Import würde alles sofort laufen |
| Globale Variablen statt Parameter | Versteckte Abhängigkeiten, nicht testbar |
| Riesige `tue_alles()`-Funktion | Unlesbar, nicht wiederverwendbar |
| `print()` statt `return` in Berechnungen | Aufrufer kann Ergebnis nicht weiterverwenden |
| Kryptische Namen (`bp()`, `f3()`) | Niemand versteht den Code in 2 Wochen |
| Konstanten klein geschrieben | Verschwimmen mit Variablen |

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 15, Kap. 7: Übung 7.1 ("Vier Strukturfehler finden")
:::

---

# Cheat Card

| Konzept | Syntax |
|---|---|
| Funktion definieren | `def name(parameter):` |
| Hauptfunktion | `def main():` |
| Einstiegspunkt | `if __name__ == "__main__":` |
| Konstante | `MAX_WERT = 100` |
| Docstring | `"""Beschreibung."""` |
| Wert zurückgeben | `return wert` |

> **Die 5 Bausteine**: Imports → Konstanten → Hilfsfunktionen → `main()` → `if __name__`.

---

# Ausblick: Notebook 16 -- Pandas

- **DataFrames**: tabellarische Daten elegant verarbeiten
- **Visualisierungen**: Diagramme direkt aus Daten
- **CSV-Dateien**: echte Datensätze laden
- **Externe Bibliotheken**: `import pandas as pd`

> Auch Datenanalyse-Programme profitieren von `main()` und guter Struktur -- die heutigen Bausteine bleiben Ihr Werkzeug.

---

# Heute geübt

✓ Spaghetti-Code von strukturiertem Programm unterschieden  
✓ Funktionen nach **Single Responsibility** entworfen  
✓ Funktionen rufen Funktionen auf (Abstraktion)  
✓ `main()` als Dirigent geschrieben  
✓ `if __name__ == "__main__":` verstanden  
✓ Die **5 Bausteine** einer `.py`-Datei kennengelernt  
✓ Häufige Anti-Patterns erkannt  

::: exercisebox
**✎ Zur Vertiefung im Notebook 15:**

- "Sofort ausprobieren"-Aufgaben in Kap. 1-7 (sind Sie schon mitgegangen)
- Abschlussübungen: 4 Aufgaben (Taschenrechner, Notenrechner, Lagerverwaltung, Lohnabrechnung refaktorisieren)
:::
