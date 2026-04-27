---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 14 - Sortieralgorithmen: Daten systematisch ordnen

## Lernziele

Nach Abschluss dieses Notebooks können Sie:
- Das Prinzip des Sortierens und seine Bedeutung in der Informatik erklären
- Bubble Sort implementieren und dessen Arbeitsweise nachvollziehen
- Insertion Sort implementieren und dessen Arbeitsweise nachvollziehen
- Quicksort implementieren und das Divide-and-Conquer-Prinzip verstehen
- Die Zeitkomplexität verschiedener Sortieralgorithmen vergleichen
- Die eingebauten Python-Sortierfunktionen `sort()` und `sorted()` anwenden
- Entscheiden, welcher Sortieralgorithmus für eine gegebene Situation geeignet ist

**Kompetenzstufen**: Verstehen, Anwenden, Analysieren

+++

## Voraussetzungen

Für dieses Notebook sollten Sie folgende Konzepte beherrschen:
- Listen und deren Manipulation (Notebook 06)
- Funktionen mit Parametern und Rückgabewerten (Notebook 07)
- Vergleichsoperatoren und logische Ausdrücke (Notebook 08)
- if-Anweisungen und Bedingungen (Notebook 09)
- for- und while-Schleifen, verschachtelte Schleifen (Notebook 10)
- Big-O-Notation und Zeitkomplexität (Notebook 13)

Falls Sie diese Konzepte noch nicht sicher beherrschen, wiederholen Sie bitte die entsprechenden Notebooks.

+++

## Sortieralgorithmen: Einführung und Motivation

Sortieren ist eine der fundamentalsten Operationen in der Informatik. Es bezeichnet den Prozess, eine Sammlung von Elementen in eine bestimmte Reihenfolge zu bringen – typischerweise aufsteigend oder absteigend nach einem bestimmten Kriterium.

**Warum ist Sortieren wichtig?**

Sortierte Daten ermöglichen zahlreiche Optimierungen und sind in vielen Bereichen unverzichtbar:

1. **Effizientes Suchen**: Auf sortierten Daten können effiziente Suchalgorithmen wie die binäre Suche angewendet werden, die deutlich schneller als die lineare Suche sind.

2. **Datenanalyse**: Viele statistische Operationen setzen sortierte Daten voraus, beispielsweise die Berechnung des Medians oder die Identifikation von Ausreißern.

3. **Benutzerfreundlichkeit**: Sortierte Darstellungen erleichtern Menschen die Interpretation von Daten erheblich. Denken Sie an alphabetisch sortierte Kontaktlisten oder chronologisch geordnete Nachrichten.

4. **Algorithmus-Voraussetzung**: Zahlreiche Algorithmen erwarten sortierte Eingabedaten als Voraussetzung für ihre Funktionsweise.

In diesem Notebook werden Sie drei klassische Sortieralgorithmen kennenlernen, die unterschiedliche Strategien verfolgen und verschiedene Vor- und Nachteile aufweisen.

+++

## Bubble Sort: Der grundlegende Vergleichs-Algorithmus

### Theoretische Grundlagen

Bubble Sort ist einer der einfachsten Sortieralgorithmen und wird häufig als erster Sortieralgorithmus in der Lehre eingeführt. Der Name leitet sich von der Beobachtung ab, dass größere Elemente wie Blasen nach oben "aufsteigen", während kleinere Elemente nach unten "sinken".

**Grundprinzip**:

Der Algorithmus durchläuft die Liste wiederholt und vergleicht dabei benachbarte Elemente paarweise. Wenn zwei benachbarte Elemente in der falschen Reihenfolge stehen, werden sie vertauscht. Dieser Prozess wird so lange wiederholt, bis bei einem vollständigen Durchlauf kein Tausch mehr stattfindet – dann ist die Liste sortiert.

**Anschauliche Beschreibung**:

Stellen Sie sich vor, Sie sortieren Bücher nach ihrer Höhe. Sie gehen von links nach rechts durch das Regal und vergleichen immer zwei nebeneinanderstehende Bücher. Ist das linke Buch höher als das rechte, tauschen Sie die beiden. Nach einem vollständigen Durchgang steht das höchste Buch ganz rechts. Sie wiederholen diesen Vorgang, bis alle Bücher sortiert sind.

+++

### Schrittweise Funktionsweise

Betrachten wir ein konkretes Beispiel mit der Liste `[5, 3, 8, 4, 2]`:

**Erster Durchlauf:**
- Vergleiche 5 und 3: 5 > 3, also tauschen → `[3, 5, 8, 4, 2]`
- Vergleiche 5 und 8: 5 < 8, kein Tausch → `[3, 5, 8, 4, 2]`
- Vergleiche 8 und 4: 8 > 4, also tauschen → `[3, 5, 4, 8, 2]`
- Vergleiche 8 und 2: 8 > 2, also tauschen → `[3, 5, 4, 2, 8]`

Nach dem ersten Durchlauf steht die größte Zahl (8) an der richtigen Position am Ende.

**Zweiter Durchlauf:**
- Vergleiche 3 und 5: 3 < 5, kein Tausch → `[3, 5, 4, 2, 8]`
- Vergleiche 5 und 4: 5 > 4, also tauschen → `[3, 4, 5, 2, 8]`
- Vergleiche 5 und 2: 5 > 2, also tauschen → `[3, 4, 2, 5, 8]`

Nach dem zweiten Durchlauf stehen die beiden größten Zahlen (5 und 8) am Ende.

+++

**Dritter Durchlauf:**
- Vergleiche 3 und 4: 3 < 4, kein Tausch → `[3, 4, 2, 5, 8]`
- Vergleiche 4 und 2: 4 > 2, also tauschen → `[3, 2, 4, 5, 8]`

**Vierter Durchlauf:**
- Vergleiche 3 und 2: 3 > 2, also tauschen → `[2, 3, 4, 5, 8]`

**Fünfter Durchlauf:**
- Keine Tauschoperationen mehr nötig → Die Liste ist vollständig sortiert!

Bei jedem Durchlauf wird mindestens ein Element an seine endgültige Position gebracht. Die bereits sortierten Elemente am Ende müssen in den folgenden Durchläufen nicht mehr betrachtet werden.

+++

### Syntax und Semantik

**Syntax**:
```python
def bubble_sort(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste
```

**Semantik**:
- **Äußere Schleife** (`for i in range(n)`): Bestimmt die Anzahl der Durchläufe. Im schlimmsten Fall sind n Durchläufe erforderlich.
- **Innere Schleife** (`for j in range(0, n - i - 1)`): Durchläuft die Liste und vergleicht benachbarte Elemente. Mit jedem Durchlauf werden die letzten i Elemente ausgelassen, da diese bereits sortiert sind.
- **Vergleich und Tausch**: Wenn `liste[j] > liste[j + 1]`, werden die Elemente getauscht.
- **Rückgabe**: Die sortierte Liste wird zurückgegeben.

**Optimierung**: Eine verbesserte Version kann den Algorithmus vorzeitig beenden, wenn bei einem Durchlauf kein Tausch stattfindet.

+++

### Beispiel 1: Einfache Bubble Sort Implementation

Wir implementieren zunächst die grundlegende Version von Bubble Sort ohne Optimierungen:

```{code-cell}
def bubble_sort_einfach(liste):
    """Sortiert eine Liste mit dem Bubble Sort Algorithmus."""
    n = len(liste)
    
    # Äußere Schleife: n Durchläufe
    for i in range(n):
        # Innere Schleife: Vergleiche benachbarte Elemente
        for j in range(0, n - i - 1):
            # Wenn linkes Element größer als rechtes, tausche
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    
    return liste
```

```{code-cell}
# Beispiel: Unsortierte Liste
zahlen = [5, 3, 8, 4, 2]
print("Ursprüngliche Liste:", zahlen)
```

```{code-cell}
# Sortieren mit Bubble Sort
sortierte_zahlen = bubble_sort_einfach(zahlen.copy())
print("Sortierte Liste:", sortierte_zahlen)
```

**Erklärung**: 

Die Funktion verwendet `.copy()`, um eine Kopie der ursprünglichen Liste zu erstellen. Dies ist wichtig, da Bubble Sort die Liste "in-place" modifiziert, das heißt, die ursprüngliche Liste wird verändert. Durch das Kopieren bleibt die Originalliste erhalten.

Die verschachtelten Schleifen sorgen dafür, dass jedes Element mit seinen Nachbarn verglichen wird. Der Ausdruck `n - i - 1` stellt sicher, dass bereits sortierte Elemente am Ende nicht erneut betrachtet werden.

+++

### Angeleitete Übung 1.1

**Aufgabe**: Implementieren Sie eine Funktion `bubble_sort_absteigend(liste)`, die eine Liste in **absteigender** Reihenfolge sortiert (vom größten zum kleinsten Element).

**Hinweise**:
- Schritt 1: Kopieren Sie die Funktion `bubble_sort_einfach` als Ausgangspunkt
- Schritt 2: Ändern Sie den Vergleichsoperator in der if-Bedingung
- Schritt 3: Testen Sie Ihre Funktion mit der Liste `[5, 3, 8, 4, 2]`

```{code-cell}
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
def bubble_sort_absteigend(liste):
    """Sortiert eine Liste in absteigender Reihenfolge."""
    n = len(liste)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            # Änderung: Vergleichsoperator umgedreht (< statt >)
            if liste[j] < liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    
    return liste

# Test
zahlen = [5, 3, 8, 4, 2]
print("Absteigend sortiert:", bubble_sort_absteigend(zahlen.copy()))
# Ausgabe: Absteigend sortiert: [8, 5, 4, 3, 2]
```

**Erklärung**: Die einzige notwendige Änderung ist der Vergleichsoperator. Während wir für aufsteigende Sortierung `>` verwenden (größere Elemente nach rechts), nutzen wir für absteigende Sortierung `<` (kleinere Elemente nach rechts).

</details>

+++

### Beispiel 2: Optimierter Bubble Sort

Die einfache Version führt immer alle Durchläufe aus, selbst wenn die Liste bereits sortiert ist. Eine Optimierung nutzt eine Variable, um zu erkennen, ob beim letzten Durchlauf Tauschoperationen stattgefunden haben:

```{code-cell}
def bubble_sort_optimiert(liste):
    """Optimierte Version von Bubble Sort mit vorzeitigem Abbruch."""
    n = len(liste)
    
    for i in range(n):
        # Flag: Wurde in diesem Durchlauf getauscht?
        getauscht = False
        
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
                getauscht = True  # Tausch hat stattgefunden
        
        # Wenn kein Tausch stattfand, ist die Liste sortiert
        if not getauscht:
            break
    
    return liste
```

```{code-cell}
# Test mit bereits sortierter Liste
sortierte_liste = [1, 2, 3, 4, 5]
print("Bereits sortiert:", bubble_sort_optimiert(sortierte_liste.copy()))
```

**Erklärung der Optimierung**:

Die Variable `getauscht` wird zu Beginn jedes Durchlaufs auf `False` gesetzt. Findet während des Durchlaufs mindestens ein Tausch statt, wird sie auf `True` gesetzt. Am Ende des Durchlaufs prüfen wir: Wenn `getauscht` noch `False` ist, bedeutet das, dass keine Tauschoperationen mehr nötig waren – die Liste ist bereits sortiert, und wir können den Algorithmus vorzeitig mit `break` beenden.

Diese Optimierung verbessert die Best-Case-Zeitkomplexität von O(n²) auf O(n), wenn die Liste bereits sortiert ist.

+++

### Angeleitete Übung 1.2

**Aufgabe**: Erweitern Sie die optimierte Bubble Sort Funktion so, dass sie zählt, wie viele Durchläufe tatsächlich durchgeführt wurden, und diese Anzahl zusammen mit der sortierten Liste zurückgibt.

**Hinweise**:
- Fügen Sie eine Zählervariable hinzu, die bei jedem Durchlauf erhöht wird
- Geben Sie ein Tupel zurück: `(sortierte_liste, anzahl_durchlaeufe)`
- Testen Sie mit einer bereits sortierten Liste und einer unsortierten Liste

```{code-cell}
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
def bubble_sort_mit_zaehler(liste):
    """Bubble Sort mit Zähler für durchgeführte Durchläufe."""
    n = len(liste)
    durchlaeufe = 0  # Zähler initialisieren
    
    for i in range(n):
        durchlaeufe += 1  # Durchlauf zählen
        getauscht = False
        
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
                getauscht = True
        
        if not getauscht:
            break
    
    return liste, durchlaeufe

# Test mit unsortierter Liste
unsortiert = [5, 3, 8, 4, 2]
ergebnis, anzahl = bubble_sort_mit_zaehler(unsortiert.copy())
print(f"Unsortierte Liste: {anzahl} Durchläufe")
print(f"Ergebnis: {ergebnis}")

# Test mit sortierter Liste
sortiert = [1, 2, 3, 4, 5]
ergebnis, anzahl = bubble_sort_mit_zaehler(sortiert.copy())
print(f"Sortierte Liste: {anzahl} Durchlauf(e)")
print(f"Ergebnis: {ergebnis}")
```

**Erklärung**: Der Zähler `durchlaeufe` wird bei jedem äußeren Schleifendurchlauf erhöht. Bei einer bereits sortierten Liste wird nur ein Durchlauf benötigt, da die `break`-Anweisung den Algorithmus nach dem ersten Durchlauf beendet. Bei einer unsortierten Liste können bis zu n Durchläufe erforderlich sein.

</details>

+++

### Zeitkomplexität von Bubble Sort

Die Analyse der Zeitkomplexität zeigt, warum Bubble Sort für große Datenmengen ineffizient ist:

**Best Case: O(n)**
- Tritt auf, wenn die Liste bereits sortiert ist
- Mit der Optimierung (getauscht-Flag) wird nur ein Durchlauf benötigt
- Ohne Optimierung: O(n²), da alle Durchläufe ausgeführt werden

**Average Case: O(n²)**
- Bei zufällig angeordneten Daten
- Die äußere Schleife läuft n-mal, die innere Schleife durchschnittlich n/2-mal
- Gesamtzahl der Vergleiche: n × (n/2) ≈ n²/2 → O(n²)

**Worst Case: O(n²)**
- Tritt auf, wenn die Liste in umgekehrter Reihenfolge sortiert ist
- Maximale Anzahl von Vergleichen: n × (n-1) / 2
- Jedes Element muss durch die gesamte Liste "wandern"

+++

### Speicherkomplexität von Bubble Sort

**Zusätzlicher Speicherbedarf: O(1)**

Bubble Sort ist ein "In-Place"-Algorithmus, das bedeutet:
- Die Sortierung erfolgt direkt in der ursprünglichen Liste
- Es wird kein zusätzlicher Speicher proportional zur Eingabegröße benötigt
- Nur konstant viele Hilfsvariablen (i, j, getauscht) werden verwendet

Dies ist ein Vorteil von Bubble Sort: Bei sehr begrenztem Speicher kann er dennoch eingesetzt werden.

+++

## Insertion Sort: Sortieren durch schrittweises Einfügen

### Theoretische Grundlagen

Insertion Sort verfolgt eine andere Strategie als Bubble Sort. Statt benachbarte Elemente zu vergleichen und zu tauschen, baut Insertion Sort schrittweise eine sortierte Teilliste auf, indem jedes neue Element an der richtigen Position eingefügt wird.

**Grundprinzip**:

Der Algorithmus teilt die Liste gedanklich in zwei Bereiche: einen sortierten Bereich am Anfang und einen unsortierten Bereich am Ende. Zu Beginn besteht der sortierte Bereich nur aus dem ersten Element. In jedem Schritt wird das erste Element des unsortierten Bereichs entnommen und an der korrekten Position im sortierten Bereich eingefügt.

**Anschauliche Beschreibung**:

Stellen Sie sich vor, Sie sortieren Spielkarten in Ihrer Hand. Sie nehmen die Karten nacheinander auf und fügen jede neue Karte an der richtigen Position zwischen den bereits sortierten Karten ein. Genau so arbeitet Insertion Sort.

**Vergleich zu Bubble Sort**:

Während Bubble Sort die gesamte Liste wiederholt durchläuft und Elemente tauscht, konzentriert sich Insertion Sort darauf, jedes Element genau einmal zu betrachten und es direkt an die richtige Stelle zu setzen.

+++

### Schrittweise Funktionsweise

Betrachten wir wieder die Liste `[5, 3, 8, 4, 2]`:

**Ausgangssituation:**
- Sortierter Bereich: `[5]` (erstes Element ist automatisch sortiert)
- Unsortierter Bereich: `[3, 8, 4, 2]`

**Schritt 1: Element 3 einfügen**
- Aktuelles Element: 3
- Vergleiche 3 mit 5: 3 < 5, also verschiebe 5 nach rechts
- Setze 3 an Position 0
- Liste: `[3, 5, 8, 4, 2]`
- Sortierter Bereich: `[3, 5]`

**Schritt 2: Element 8 einfügen**
- Aktuelles Element: 8
- Vergleiche 8 mit 5: 8 > 5, keine Verschiebung nötig
- 8 bleibt an aktueller Position
- Liste: `[3, 5, 8, 4, 2]`
- Sortierter Bereich: `[3, 5, 8]`

+++

**Schritt 3: Element 4 einfügen**
- Aktuelles Element: 4
- Vergleiche 4 mit 8: 4 < 8, verschiebe 8 nach rechts → `[3, 5, _, 8, 2]`
- Vergleiche 4 mit 5: 4 < 5, verschiebe 5 nach rechts → `[3, _, 5, 8, 2]`
- Vergleiche 4 mit 3: 4 > 3, setze 4 an Position 1
- Liste: `[3, 4, 5, 8, 2]`
- Sortierter Bereich: `[3, 4, 5, 8]`

**Schritt 4: Element 2 einfügen**
- Aktuelles Element: 2
- Vergleiche 2 mit 8: 2 < 8, verschiebe 8 nach rechts
- Vergleiche 2 mit 5: 2 < 5, verschiebe 5 nach rechts
- Vergleiche 2 mit 4: 2 < 4, verschiebe 4 nach rechts
- Vergleiche 2 mit 3: 2 < 3, verschiebe 3 nach rechts
- Setze 2 an Position 0
- Liste: `[2, 3, 4, 5, 8]`
- Sortierter Bereich: `[2, 3, 4, 5, 8]` (vollständig!)

+++

### Syntax und Semantik

**Syntax**:
```python
def insertion_sort(liste):
    for i in range(1, len(liste)):
        schluessel = liste[i]
        j = i - 1
        while j >= 0 and liste[j] > schluessel:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = schluessel
    return liste
```

**Semantik**:
- **for i in range(1, len(liste))**: Iteriert durch die unsortierten Elemente (ab Index 1, da das erste Element bereits als sortiert gilt)
- **schluessel = liste[i]**: Speichert das aktuell einzufügende Element
- **j = i - 1**: Startposition für den Vergleich im sortierten Bereich (das Element links vom Schlüssel)
- **while-Schleife**: Verschiebt alle Elemente im sortierten Bereich, die größer als der Schlüssel sind, um eine Position nach rechts
- **liste[j + 1] = schluessel**: Fügt den Schlüssel an der korrekten Position ein

**Wichtig**: Die while-Schleife läuft rückwärts durch den sortierten Bereich und stoppt, sobald ein Element gefunden wird, das kleiner oder gleich dem Schlüssel ist.

+++

### Beispiel 1: Grundlegende Insertion Sort Implementation

```{code-cell}
def insertion_sort(liste):
    """Sortiert eine Liste mit dem Insertion Sort Algorithmus."""
    
    # Beginne bei Index 1 (erstes Element ist bereits "sortiert")
    for i in range(1, len(liste)):
        schluessel = liste[i]  # Element, das eingefügt werden soll
        j = i - 1  # Startposition im sortierten Bereich
        
        # Verschiebe Elemente nach rechts, solange sie größer als der Schlüssel sind
        while j >= 0 and liste[j] > schluessel:
            liste[j + 1] = liste[j]
            j -= 1
        
        # Füge den Schlüssel an der korrekten Position ein
        liste[j + 1] = schluessel
    
    return liste
```

```{code-cell}
# Beispiel
zahlen = [5, 3, 8, 4, 2]
print("Ursprüngliche Liste:", zahlen)
sortierte_zahlen = insertion_sort(zahlen.copy())
print("Sortierte Liste:", sortierte_zahlen)
```

**Erklärung**:

Die Variable `schluessel` speichert das aktuell zu platzierende Element. Die while-Schleife verschiebt alle größeren Elemente im sortierten Bereich um eine Position nach rechts, wodurch Platz für den Schlüssel geschaffen wird. Sobald die richtige Position gefunden ist (ein kleineres Element oder der Anfang der Liste), wird der Schlüssel eingefügt.

Beachten Sie, dass die for-Schleife bei Index 1 beginnt, da das erste Element (Index 0) bereits als sortierter Bereich mit einem Element betrachtet wird.

+++

### Angeleitete Übung 2.1

**Aufgabe**: Erweitern Sie die Insertion Sort Funktion so, dass sie bei jedem Schritt die aktuelle Liste ausgibt. So können Sie die Funktionsweise Schritt für Schritt nachvollziehen.

**Hinweise**:
- Schritt 1: Fügen Sie eine `print()`-Anweisung nach dem Einfügen des Schlüssels hinzu
- Schritt 2: Geben Sie auch den aktuellen Schlüsselwert aus
- Schritt 3: Testen Sie mit der Liste `[5, 3, 8, 4, 2]`

```{code-cell}
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
def insertion_sort_debug(liste):
    """Insertion Sort mit Schritt-für-Schritt-Ausgabe."""
    
    print("Start:", liste)
    
    for i in range(1, len(liste)):
        schluessel = liste[i]
        j = i - 1
        
        while j >= 0 and liste[j] > schluessel:
            liste[j + 1] = liste[j]
            j -= 1
        
        liste[j + 1] = schluessel
        
        # Ausgabe nach jedem Einfügen
        print(f"Schritt {i}: Schlüssel={schluessel}, Liste={liste}")
    
    return liste

# Test
zahlen = [5, 3, 8, 4, 2]
insertion_sort_debug(zahlen.copy())
```

**Erklärung**: Die Debug-Version gibt nach jedem Einfügen den aktuellen Zustand der Liste aus. Sie können beobachten, wie der sortierte Bereich am Anfang der Liste Schritt für Schritt wächst.

</details>

+++

### Beispiel 2: Insertion Sort mit Strings

Insertion Sort funktioniert nicht nur mit Zahlen, sondern mit allen vergleichbaren Datentypen. Hier ein Beispiel mit Strings:

```{code-cell}
# Sortieren von Namen
namen = ["Zoe", "Alice", "Max", "Bob", "Clara"]
print("Unsortierte Namen:", namen)
```

```{code-cell}
# Insertion Sort auf Strings anwenden
sortierte_namen = insertion_sort(namen.copy())
print("Alphabetisch sortiert:", sortierte_namen)
```

**Erklärung**:

Python vergleicht Strings lexikographisch (alphabetisch). Der Vergleichsoperator `>` funktioniert daher auch für Strings. "Zoe" > "Alice" ist `True`, da "Z" im Alphabet nach "A" kommt. Der Insertion Sort Algorithmus benötigt keine Anpassung, um mit verschiedenen Datentypen zu arbeiten – er funktioniert mit allem, was vergleichbar ist.

+++

### Angeleitete Übung 2.2

**Aufgabe**: Erstellen Sie eine Funktion, die eine Liste von Tupeln sortiert. Jedes Tupel enthält einen Namen und ein Alter: `(name, alter)`. Sortieren Sie nach dem Alter.

**Hinweise**:
- Modifizieren Sie die Insertion Sort Funktion
- Vergleichen Sie `liste[j][1]` (das Alter) statt `liste[j]`
- Testen Sie mit: `[("Anna", 25), ("Bob", 20), ("Clara", 30)]`

```{code-cell}
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
def insertion_sort_tupel(liste):
    """Sortiert eine Liste von (Name, Alter)-Tupeln nach Alter."""
    
    for i in range(1, len(liste)):
        schluessel = liste[i]
        j = i - 1
        
        # Vergleiche das Alter (Index 1 des Tupels)
        while j >= 0 and liste[j][1] > schluessel[1]:
            liste[j + 1] = liste[j]
            j -= 1
        
        liste[j + 1] = schluessel
    
    return liste

# Test
personen = [("Anna", 25), ("Bob", 20), ("Clara", 30), ("David", 22)]
print("Unsortiert:", personen)
sortiert = insertion_sort_tupel(personen.copy())
print("Nach Alter sortiert:", sortiert)
# Ausgabe: [('Bob', 20), ('David', 22), ('Anna', 25), ('Clara', 30)]
```

**Erklärung**: Durch Zugriff auf `liste[j][1]` und `schluessel[1]` vergleichen wir nur das zweite Element der Tupel (das Alter), während das gesamte Tupel verschoben wird. Dies zeigt die Flexibilität von Sortieralgorithmen bei strukturierten Daten.

</details>

+++

### Zeitkomplexität von Insertion Sort

**Best Case: O(n)**
- Tritt auf, wenn die Liste bereits sortiert ist
- Die while-Schleife wird nie ausgeführt, da kein Element verschoben werden muss
- Nur die äußere for-Schleife läuft einmal durch: n-1 Vergleiche

**Average Case: O(n²)**
- Bei zufällig angeordneten Daten
- Im Durchschnitt muss jedes Element durch die Hälfte des sortierten Bereichs wandern
- Gesamtzahl der Operationen: etwa n²/4 → O(n²)

**Worst Case: O(n²)**
- Tritt auf, wenn die Liste in umgekehrter Reihenfolge sortiert ist
- Jedes Element muss durch den gesamten sortierten Bereich bis zum Anfang wandern
- Maximale Anzahl von Vergleichen: 1 + 2 + 3 + ... + (n-1) = n(n-1)/2

+++

### Speicherkomplexität von Insertion Sort

**Zusätzlicher Speicherbedarf: O(1)**

Wie Bubble Sort ist auch Insertion Sort ein In-Place-Algorithmus:
- Die Sortierung erfolgt direkt in der ursprünglichen Liste
- Nur konstant viele Hilfsvariablen (i, j, schluessel) werden benötigt
- Kein zusätzlicher Speicher proportional zur Eingabegröße erforderlich

**Praktische Vorteile von Insertion Sort**:
- Sehr effizient für kleine Listen (n < 10-20)
- Sehr effizient für fast sortierte Listen
- Stabiler Algorithmus (gleiche Elemente behalten ihre relative Reihenfolge)
- Einfache Implementierung mit wenig Code

+++

## Quicksort: Der effiziente Divide-and-Conquer-Algorithmus

### Theoretische Grundlagen

Quicksort ist einer der am häufigsten verwendeten Sortieralgorithmen in der Praxis. Im Gegensatz zu Bubble Sort und Insertion Sort nutzt Quicksort das **Divide-and-Conquer-Prinzip** (Teile und Herrsche): Ein großes Problem wird in kleinere Teilprobleme zerlegt, diese werden gelöst, und die Lösungen werden kombiniert.

**Grundprinzip**:

1. **Divide (Teilen)**: Wähle ein Element aus der Liste als "Pivot"-Element. Teile die Liste in zwei Teillisten: Elemente kleiner als das Pivot und Elemente größer als das Pivot.

2. **Conquer (Herrschen)**: Sortiere beide Teillisten rekursiv mit dem gleichen Verfahren.

3. **Combine (Kombinieren)**: Füge die sortierten Teillisten und das Pivot-Element zusammen.

**Rekursion**: Quicksort ist ein rekursiver Algorithmus, das heißt, die Funktion ruft sich selbst auf. Die Rekursion endet, wenn eine Teilliste nur noch ein Element oder gar kein Element enthält – solche Listen sind bereits sortiert.

+++

### Schrittweise Funktionsweise

Betrachten wir die Liste `[5, 3, 8, 4, 2]` und wählen das erste Element als Pivot:

**Erster Aufruf:**
- Liste: `[5, 3, 8, 4, 2]`
- Pivot: 5
- Elemente < 5: `[3, 4, 2]`
- Elemente ≥ 5: `[8]`
- Rekursive Aufrufe für `[3, 4, 2]` und `[8]`

**Zweiter Aufruf (linke Teilliste):**
- Liste: `[3, 4, 2]`
- Pivot: 3
- Elemente < 3: `[2]`
- Elemente ≥ 3: `[4]`
- `[2]` und `[4]` sind bereits sortiert (jeweils nur ein Element)

**Kombinieren:**
- Linke Teilliste sortiert: `[2]` + `[3]` + `[4]` = `[2, 3, 4]`
- Rechte Teilliste: `[8]` (bereits sortiert)
- Gesamtergebnis: `[2, 3, 4]` + `[5]` + `[8]` = `[2, 3, 4, 5, 8]`

+++

### Syntax und Semantik

**Syntax**:
```python
def quicksort(liste):
    if len(liste) <= 1:
        return liste
    
    pivot = liste[0]
    kleiner = [x for x in liste[1:] if x < pivot]
    groesser = [x for x in liste[1:] if x >= pivot]
    
    return quicksort(kleiner) + [pivot] + quicksort(groesser)
```

**Semantik**:
- **Basisfall** (`if len(liste) <= 1`): Eine leere Liste oder eine Liste mit einem Element ist bereits sortiert und wird unverändert zurückgegeben
- **Pivot-Wahl** (`pivot = liste[0]`): Das erste Element wird als Pivot gewählt (es gibt auch andere Strategien)
- **List Comprehensions**: Erstellen zwei neue Listen – eine mit allen Elementen kleiner als das Pivot, eine mit allen größeren oder gleichen Elementen
- **Rekursive Aufrufe**: `quicksort(kleiner)` und `quicksort(groesser)` sortieren die Teillisten
- **Kombinieren**: Die sortierten Teillisten werden mit dem Pivot zusammengefügt

+++

### Beispiel 1: Grundlegende Quicksort Implementation

```{code-cell}
def quicksort(liste):
    """Sortiert eine Liste mit dem Quicksort Algorithmus."""
    
    # Basisfall: Listen mit 0 oder 1 Element sind bereits sortiert
    if len(liste) <= 1:
        return liste
    
    # Wähle das erste Element als Pivot
    pivot = liste[0]
    
    # Teile die Liste in Elemente kleiner und größer/gleich dem Pivot
    kleiner = [x for x in liste[1:] if x < pivot]
    groesser = [x for x in liste[1:] if x >= pivot]
    
    # Rekursiv sortieren und kombinieren
    return quicksort(kleiner) + [pivot] + quicksort(groesser)
```

```{code-cell}
# Beispiel
zahlen = [5, 3, 8, 4, 2, 7, 1, 6]
print("Ursprüngliche Liste:", zahlen)
sortierte_zahlen = quicksort(zahlen)
print("Sortierte Liste:", sortierte_zahlen)
```

**Erklärung**:

Diese Implementation verwendet List Comprehensions für eine elegante und lesbare Lösung. Die beiden Listen `kleiner` und `groesser` werden durch Filtern der ursprünglichen Liste erstellt. Die rekursiven Aufrufe `quicksort(kleiner)` und `quicksort(groesser)` sortieren die Teillisten, und das Ergebnis wird durch einfache Listenkombination mit dem `+`-Operator zusammengeführt.

Beachten Sie, dass `liste[1:]` alle Elemente außer dem ersten (dem Pivot) enthält. Dies verhindert, dass das Pivot-Element in beiden Teillisten erscheint.

+++

### Angeleitete Übung 3.1

**Aufgabe**: Erstellen Sie eine Version von Quicksort, die das **mittlere** Element als Pivot wählt statt des ersten Elements.

**Hinweise**:
- Schritt 1: Berechnen Sie den mittleren Index mit `len(liste) // 2`
- Schritt 2: Wählen Sie das Element an diesem Index als Pivot
- Schritt 3: Passen Sie die List Comprehensions an, um alle Elemente außer dem Pivot zu berücksichtigen
- Schritt 4: Testen Sie mit der Liste `[5, 3, 8, 4, 2]`

```{code-cell}
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
def quicksort_mitte(liste):
    """Quicksort mit mittlerem Element als Pivot."""
    
    if len(liste) <= 1:
        return liste
    
    # Wähle mittleres Element als Pivot
    mitte = len(liste) // 2
    pivot = liste[mitte]
    
    # Teile Liste (verwende enumerate für Index-Zugriff)
    kleiner = [x for i, x in enumerate(liste) if x < pivot and i != mitte]
    gleich = [x for x in liste if x == pivot]
    groesser = [x for i, x in enumerate(liste) if x > pivot and i != mitte]
    
    return quicksort_mitte(kleiner) + gleich + quicksort_mitte(groesser)

# Test
zahlen = [5, 3, 8, 4, 2]
print("Mit mittlerem Pivot:", quicksort_mitte(zahlen))
```

**Erklärung**: Die Wahl des mittleren Elements als Pivot kann bei manchen Eingabedaten zu besserer Performance führen. Wir verwenden `enumerate(liste)` um sowohl auf den Index als auch auf den Wert zuzugreifen, damit wir das Pivot-Element selbst ausschließen können. Beachten Sie auch die separate Liste `gleich` für Elemente, die dem Pivot entsprechen.

</details>

+++

### Beispiel 2: Quicksort mit Visualisierung der Rekursion

Um die rekursive Natur von Quicksort besser zu verstehen, erstellen wir eine Version, die jeden Rekursionsschritt ausgibt:

```{code-cell}
def quicksort_debug(liste, ebene=0):
    """Quicksort mit Ausgabe der Rekursionsebenen."""
    
    # Einrückung für Visualisierung der Rekursionstiefe
    einrueckung = "  " * ebene
    
    print(f"{einrueckung}Sortiere: {liste}")
    
    # Basisfall
    if len(liste) <= 1:
        print(f"{einrueckung}→ Bereits sortiert: {liste}")
        return liste
    
    # Pivot wählen und teilen
    pivot = liste[0]
    kleiner = [x for x in liste[1:] if x < pivot]
    groesser = [x for x in liste[1:] if x >= pivot]
    
    print(f"{einrueckung}Pivot: {pivot}")
    print(f"{einrueckung}Kleiner: {kleiner}")
    print(f"{einrueckung}Größer: {groesser}")
    
    # Rekursiv sortieren
    ergebnis = quicksort_debug(kleiner, ebene + 1) + [pivot] + quicksort_debug(groesser, ebene + 1)
    
    print(f"{einrueckung}→ Ergebnis: {ergebnis}")
    return ergebnis
```

```{code-cell}
# Test mit kleiner Liste
zahlen = [5, 3, 8, 4, 2]
print("=== Quicksort Visualisierung ===")
quicksort_debug(zahlen)
print()
```

**Erklärung**:

Die Debug-Version verwendet einen zusätzlichen Parameter `ebene`, um die Rekursionstiefe zu verfolgen. Durch Einrückung (`"  " * ebene`) wird visuell dargestellt, auf welcher Rekursionsebene sich der Algorithmus gerade befindet. Sie können beobachten, wie Quicksort das Problem in immer kleinere Teilprobleme zerlegt und diese dann von unten nach oben wieder zusammenfügt.

Dies verdeutlicht das Divide-and-Conquer-Prinzip: Große Probleme werden in kleinere Teilprobleme zerlegt, bis diese trivial lösbar sind (Basisfälle mit 0 oder 1 Element).

+++

### Angeleitete Übung 3.2

**Aufgabe**: Zählen Sie, wie oft die Quicksort-Funktion insgesamt aufgerufen wird (inklusive aller rekursiven Aufrufe) beim Sortieren einer Liste.

**Hinweise**:
- Verwenden Sie eine globale Variable oder einen Zähler-Parameter
- Erhöhen Sie den Zähler bei jedem Funktionsaufruf
- Geben Sie am Ende die Gesamtanzahl der Aufrufe zurück

```{code-cell}
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
def quicksort_mit_zaehler(liste, zaehler=[0]):
    """Quicksort mit Zähler für Funktionsaufrufe."""
    
    # Erhöhe Zähler bei jedem Aufruf
    zaehler[0] += 1
    
    if len(liste) <= 1:
        return liste
    
    pivot = liste[0]
    kleiner = [x for x in liste[1:] if x < pivot]
    groesser = [x for x in liste[1:] if x >= pivot]
    
    return quicksort_mit_zaehler(kleiner, zaehler) + [pivot] + quicksort_mit_zaehler(groesser, zaehler)

# Test
zahlen = [5, 3, 8, 4, 2, 7, 1, 6]
aufrufe = [0]  # Zähler initialisieren
ergebnis = quicksort_mit_zaehler(zahlen, aufrufe)
print(f"Sortiert: {ergebnis}")
print(f"Anzahl Funktionsaufrufe: {aufrufe[0]}")
```

**Erklärung**: Wir verwenden eine Liste `[0]` als Zähler-Parameter, da Listen in Python veränderbar (mutable) sind. Dadurch können wir den Wert über alle Rekursionsebenen hinweg teilen und erhöhen. Die Anzahl der Funktionsaufrufe gibt Aufschluss über die Komplexität des Algorithmus bei verschiedenen Eingaben.

**Häufige Fehler**:
- Verwendung einer einfachen Zahl statt einer Liste führt dazu, dass jede Rekursionsebene ihren eigenen Zähler hat
- Vergessen, den Zähler an die rekursiven Aufrufe weiterzugeben

</details>

+++

### Zeitkomplexität von Quicksort

Die Zeitkomplexität von Quicksort hängt stark von der Wahl des Pivot-Elements ab:

**Best Case / Average Case: O(n log n)**
- Tritt auf, wenn das Pivot die Liste gut in zwei etwa gleich große Hälften teilt
- Die Rekursionstiefe beträgt log₂(n), da die Liste bei jedem Schritt halbiert wird
- Auf jeder Rekursionsebene werden insgesamt n Vergleiche durchgeführt
- Gesamtzahl der Operationen: n × log(n) → O(n log n)

**Worst Case: O(n²)**
- Tritt auf, wenn das Pivot immer das kleinste oder größte Element ist
- Dies passiert beispielsweise bei bereits sortierten Listen, wenn das erste Element als Pivot gewählt wird
- Die Rekursionstiefe beträgt dann n (statt log n)
- Ähnliche Komplexität wie Bubble Sort im schlechtesten Fall

**Pivot-Strategien zur Vermeidung des Worst Case**:
- Zufälliges Element als Pivot wählen
- Median-of-Three: Wähle den Median aus erstem, mittlerem und letztem Element
- Diese Strategien machen den Worst Case sehr unwahrscheinlich

+++

### Speicherkomplexität von Quicksort

**Zusätzlicher Speicherbedarf: O(n)**

Die hier gezeigte Implementation von Quicksort ist **nicht** In-Place:
- Bei jedem Rekursionsaufruf werden neue Listen (`kleiner`, `groesser`) erstellt
- Im schlimmsten Fall kann der zusätzliche Speicherbedarf O(n) erreichen
- Es gibt In-Place-Varianten von Quicksort mit O(log n) Speicherbedarf, diese sind jedoch komplexer zu implementieren

**Rekursionstiefe**:
- Best/Average Case: O(log n) – die Tiefe des Rekursionsbaums
- Worst Case: O(n) – bei sehr unausgewogenen Teilungen

Trotz des höheren Speicherbedarfs ist Quicksort in der Praxis sehr effizient aufgrund seiner guten Cache-Eigenschaften und der durchschnittlichen O(n log n) Zeitkomplexität.

+++

## Pythons eingebaute Sortierfunktionen

### Theoretische Grundlagen

Python bietet zwei eingebaute Möglichkeiten zum Sortieren von Listen: die Methode `sort()` und die Funktion `sorted()`. Beide verwenden intern den **Timsort**-Algorithmus, der speziell für das Sortieren realer Daten entwickelt wurde.

**Timsort**:
- Entwickelt von Tim Peters im Jahr 2002 für Python
- Hybridalgorithmus, der Merge Sort und Insertion Sort kombiniert
- Sehr effizient bei teilweise vorsortierten Daten
- Stabiler Sortieralgorithmus (gleiche Elemente behalten ihre Reihenfolge)

**Zeitkomplexität von Timsort**:
- Best Case: O(n) – bei bereits sortierten Daten
- Average/Worst Case: O(n log n)
- Speicherkomplexität: O(n)

Timsort ist der Standard-Sortieralgorithmus nicht nur in Python, sondern auch in Java, Android und anderen modernen Programmiersprachen.

+++

### Unterschied zwischen sort() und sorted()

**`list.sort()` – In-Place-Sortierung**:
- Methode, die direkt auf einer Liste aufgerufen wird
- Modifiziert die ursprüngliche Liste
- Gibt `None` zurück (nicht die sortierte Liste!)
- Etwas effizienter, da keine Kopie erstellt wird

**`sorted(liste)` – Neue sortierte Liste**:
- Eingebaute Funktion, die mit beliebigen Sequenzen funktioniert
- Erstellt eine neue sortierte Liste
- Lässt die ursprüngliche Liste unverändert
- Gibt die sortierte Liste zurück
- Funktioniert auch mit Tupeln, Sets, Strings, etc.

+++

### Beispiel 1: Verwendung von sort() und sorted()

```{code-cell}
# Beispiel mit sort() - modifiziert die Liste
zahlen1 = [5, 3, 8, 4, 2]
print("Original:", zahlen1)

ergebnis = zahlen1.sort()  # sort() gibt None zurück!
print("Rückgabewert von sort():", ergebnis)
print("Liste nach sort():", zahlen1)
```

```{code-cell}
# Beispiel mit sorted() - erstellt neue Liste
zahlen2 = [5, 3, 8, 4, 2]
print("Original:", zahlen2)

sortiert = sorted(zahlen2)
print("Rückgabewert von sorted():", sortiert)
print("Original unverändert:", zahlen2)
```

**Erklärung**:

Der wichtigste Unterschied: `sort()` verändert die Liste direkt und gibt `None` zurück, während `sorted()` eine neue sortierte Liste zurückgibt und das Original unverändert lässt.

**Häufiger Fehler**: `sortierte_liste = zahlen.sort()` führt dazu, dass `sortierte_liste` den Wert `None` hat, nicht die sortierte Liste! Verwenden Sie stattdessen `sorted()` oder rufen Sie `sort()` auf und verwenden Sie danach die ursprüngliche Variable.

+++

### Beispiel 2: Sortierrichtung mit reverse-Parameter

```{code-cell}
zahlen = [5, 3, 8, 4, 2]

# Aufsteigend (Standard)
print("Aufsteigend:", sorted(zahlen))

# Absteigend mit reverse=True
print("Absteigend:", sorted(zahlen, reverse=True))
```

```{code-cell}
# Auch mit sort() möglich
zahlen = [5, 3, 8, 4, 2]
zahlen.sort(reverse=True)
print("Absteigend mit sort():", zahlen)
```

**Erklärung**:

Der Parameter `reverse=True` kehrt die Sortierreihenfolge um. Dies ist deutlich effizienter als erst aufsteigend zu sortieren und dann die Liste mit `reversed()` umzukehren, da die Sortierung direkt in der gewünschten Reihenfolge erfolgt.

+++

### Angeleitete Übung 4.1

**Aufgabe**: Sortieren Sie eine Liste von Strings nach ihrer Länge (kürzeste zuerst).

**Hinweise**:
- Schritt 1: Erstellen Sie eine Liste mit Strings unterschiedlicher Länge
- Schritt 2: Verwenden Sie `sorted()` mit dem Parameter `key=len`
- Schritt 3: Der `key`-Parameter gibt an, welche Funktion auf jedes Element angewendet wird, um den Sortierschlüssel zu bestimmen

```{code-cell}
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
# Liste mit Wörtern unterschiedlicher Länge
woerter = ["Python", "ist", "eine", "Programmiersprache", "für", "Anfänger"]

print("Original:", woerter)

# Nach Länge sortieren (kürzeste zuerst)
nach_laenge = sorted(woerter, key=len)
print("Nach Länge sortiert:", nach_laenge)

# Nach Länge sortieren (längste zuerst)
nach_laenge_umgekehrt = sorted(woerter, key=len, reverse=True)
print("Nach Länge (absteigend):", nach_laenge_umgekehrt)
```

**Erklärung**: Der `key`-Parameter nimmt eine Funktion, die auf jedes Element angewendet wird. `len` ist eine eingebaute Funktion, die die Länge eines Strings zurückgibt. Für das Wort "Python" gibt `len("Python")` den Wert 6 zurück, und dieser Wert wird für die Sortierung verwendet. Kombiniert mit `reverse=True` können Sie auch die längsten Wörter zuerst erhalten.

</details>

+++

### Beispiel 3: Sortieren mit eigener Sortierfunktion

Der `key`-Parameter kann auch mit selbst definierten Funktionen verwendet werden:

```{code-cell}
# Funktion, die das letzte Zeichen eines Strings zurückgibt
def letztes_zeichen(text):
    return text[-1]

# Liste von Namen
namen = ["Anna", "Bob", "Clara", "David", "Emma"]
print("Original:", namen)

# Sortiere nach dem letzten Buchstaben
nach_letztem = sorted(namen, key=letztes_zeichen)
print("Nach letztem Buchstaben:", nach_letztem)
```

**Erklärung**:

Die Funktion `letztes_zeichen` wird auf jeden Namen angewendet. Für "Anna" liefert sie "a", für "Bob" liefert sie "b", etc. Die Sortierung erfolgt dann basierend auf diesen Rückgabewerten. Dies zeigt die Flexibilität der eingebauten Sortierfunktionen – Sie können nach beliebigen Kriterien sortieren, indem Sie eine passende `key`-Funktion definieren.

+++

### Angeleitete Übung 4.2

**Aufgabe**: Sortieren Sie eine Liste von Tupeln `(name, alter, note)` zuerst nach Note (aufsteigend) und bei gleicher Note nach Alter (aufsteigend).

**Hinweise**:
- Erstellen Sie eine Liste mit Tupeln: `[("Anna", 25, 1.7), ("Bob", 20, 2.3), ...]`
- Verwenden Sie eine `key`-Funktion, die ein Tupel `(note, alter)` zurückgibt
- Python sortiert Tupel elementweise: erst nach dem ersten Element, dann nach dem zweiten, etc.

```{code-cell}
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
# Liste von Studierenden mit (Name, Alter, Note)
studierende = [
    ("Anna", 25, 1.7),
    ("Bob", 20, 2.3),
    ("Clara", 23, 1.7),
    ("David", 22, 2.0),
    ("Emma", 21, 1.7)
]

print("Original:")
for person in studierende:
    print(f"  {person[0]}: {person[1]} Jahre, Note {person[2]}")

# Sortierfunktion: Tupel (Note, Alter) für mehrstufige Sortierung
def sortier_schluessel(person):
    name, alter, note = person
    return (note, alter)

# Sortieren
sortiert = sorted(studierende, key=sortier_schluessel)

print("\nSortiert nach Note, dann Alter:")
for person in sortiert:
    print(f"  {person[0]}: {person[1]} Jahre, Note {person[2]}")
```

**Erklärung**: Die `key`-Funktion gibt ein Tupel `(note, alter)` zurück. Python vergleicht Tupel komponentenweise: Zuerst wird nach `note` sortiert. Wenn zwei Personen die gleiche Note haben, wird nach `alter` sortiert. Dies ermöglicht mehrstufige Sortierungen ohne komplexen Code.

**Ausgabe**: Sie sehen, dass Personen mit Note 1.7 nach Alter geordnet sind (Emma mit 21 Jahren vor Anna mit 25 Jahren).

</details>

+++

## Vergleich der Sortieralgorithmen

### Übersichtstabelle

| Algorithmus | Best Case | Average Case | Worst Case | Speicher | Stabil | Eigenschaften |
|-------------|-----------|--------------|------------|----------|--------|---------------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | Ja | Einfach, sehr ineffizient |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Ja | Gut für kleine/fast sortierte Listen |
| **Quicksort** | O(n log n) | O(n log n) | O(n²) | O(n) | Nein | Sehr effizient im Durchschnitt |
| **Timsort** (Python) | O(n) | O(n log n) | O(n log n) | O(n) | Ja | Optimiert für reale Daten |

**Stabilität**: Ein stabiler Sortieralgorithmus erhält die relative Reihenfolge von Elementen mit gleichem Sortierschlüssel. Beispiel: Bei Sortierung nach Alter bleiben Personen mit gleichem Alter in ihrer ursprünglichen Reihenfolge.

+++

### Wann welchen Algorithmus verwenden?

**Bubble Sort**:
- Nur für Lehrzwecke
- Sehr kleine Listen (< 10 Elemente), wenn Einfachheit wichtiger als Effizienz ist
- **In der Praxis: Nicht empfohlen**

**Insertion Sort**:
- Kleine Listen (< 20 Elemente)
- Fast sortierte Listen (sehr effizient bei Best Case O(n))
- Wenn Stabilität wichtig ist
- Wenn In-Place-Sortierung mit minimalem Speicher erforderlich ist

**Quicksort**:
- Große Listen mit zufälligen Daten
- Wenn durchschnittlich O(n log n) garantiert werden kann (durch gute Pivot-Wahl)
- Wenn Stabilität nicht erforderlich ist
- **Achtung**: Worst Case O(n²) bei ungünstiger Pivot-Wahl

**Timsort (Python's sort/sorted)**:
- **Standardwahl für fast alle Situationen in Python**
- Große Listen
- Teilweise vorsortierte Daten (sehr effizient)
- Wenn Stabilität wichtig ist
- Garantierte O(n log n) Worst-Case-Komplexität

+++

### Praktischer Vergleich

Erstellen wir einen einfachen Vergleich der Algorithmen auf einer kleinen Liste:

```{code-cell}
# Testliste
test_liste = [8, 3, 1, 7, 5, 9, 2, 4, 6]

print("Original:", test_liste)
print()

print("Bubble Sort:", bubble_sort_optimiert(test_liste.copy()))
print("Insertion Sort:", insertion_sort(test_liste.copy()))
print("Quicksort:", quicksort(test_liste.copy()))
print("Python sorted():", sorted(test_liste))
```

**Erklärung**:

Alle vier Methoden liefern dasselbe korrekte Ergebnis – eine aufsteigend sortierte Liste. Der Unterschied liegt in der Effizienz, die bei kleinen Listen kaum messbar ist, aber bei großen Datenmengen erheblich wird.

**Faustregel**: In Python-Programmen sollten Sie fast immer die eingebauten Funktionen `sort()` oder `sorted()` verwenden. Die selbst implementierten Algorithmen sind primär zum Verständnis der Konzepte wichtig.

+++

## Abschlussübungen

Die folgenden Aufgaben testen Ihr Verständnis der in diesem Notebook erlernten Konzepte. Bearbeiten Sie die Aufgaben selbstständig und vergleichen Sie Ihre Lösung anschließend mit den Musterlösungen am Ende des Notebooks.

### Teil 1: Grundlegende Anwendung

**Kompetenzstufe**: Anwenden

Diese Aufgaben testen die direkte Anwendung der erlernten Konzepte.

+++

**Aufgabe 1**: Implementieren Sie eine Funktion `bubble_sort_strings(liste)`, die eine Liste von Strings **nach ihrer Länge** sortiert (kürzeste zuerst). Verwenden Sie den Bubble Sort Algorithmus.

*Beispiel*: `["Python", "ist", "toll", "zu", "lernen"]` → `["zu", "ist", "toll", "Python", "lernen"]`

```{code-cell}
# Arbeitsbereich für Aufgabe 1
```

**Aufgabe 2**: Schreiben Sie eine Funktion `ist_sortiert(liste)`, die überprüft, ob eine Liste bereits aufsteigend sortiert ist. Geben Sie `True` zurück, wenn die Liste sortiert ist, sonst `False`.

*Beispiel*: `ist_sortiert([1, 2, 3, 4])` → `True`, `ist_sortiert([1, 3, 2, 4])` → `False`

```{code-cell}
# Arbeitsbereich für Aufgabe 2
```

### Teil 2: Transfer und Problemlösung

**Kompetenzstufe**: Analysieren & Erschaffen

Diese Aufgaben erfordern die Kombination mehrerer Konzepte und eigenständiges Problemlösen.

+++

**Aufgabe 3**: Erstellen Sie eine Funktion `top_n_elemente(liste, n)`, die die n größten Elemente einer Liste zurückgibt (in beliebiger Reihenfolge). Verwenden Sie einen Sortieralgorithmus Ihrer Wahl.

*Beispiel*: `top_n_elemente([5, 2, 8, 1, 9, 3], 3)` → `[9, 8, 5]` (Reihenfolge kann variieren)

*Hinweis*: Sie können die Liste sortieren und dann die letzten n Elemente nehmen.

```{code-cell}
# Arbeitsbereich für Aufgabe 3
```

**Aufgabe 4**: Entwickeln Sie eine Funktion `sortiere_woerterbuch_nach_wert(woerterbuch)`, die ein Dictionary nach seinen Werten sortiert und eine Liste von Tupeln `(schluessel, wert)` zurückgibt, sortiert nach den Werten.

*Beispiel*: 
```python
noten = {"Anna": 1.7, "Bob": 2.3, "Clara": 1.3}
sortiere_woerterbuch_nach_wert(noten)
# → [("Clara", 1.3), ("Anna", 1.7), ("Bob", 2.3)]
```

*Hinweis*: Verwenden Sie `woerterbuch.items()` um Tupel `(schluessel, wert)` zu erhalten, und sortieren Sie diese mit einer geeigneten `key`-Funktion.

```{code-cell}
# Arbeitsbereich für Aufgabe 4
```

## Zusammenfassung

In diesem Notebook haben Sie drei klassische Sortieralgorithmen sowie Pythons eingebaute Sortierfunktionen kennengelernt:

| Konzept | Syntax | Anwendungsfall |
|---------|--------|----------------|
| **Bubble Sort** | Verschachtelte Schleifen mit Tausch | Lehrzweck, sehr kleine Listen |
| **Insertion Sort** | Element einfügen mit while-Schleife | Kleine oder fast sortierte Listen |
| **Quicksort** | Rekursive Divide-and-Conquer | Große Listen, durchschnittlich sehr effizient |
| **list.sort()** | `liste.sort()` | In-Place-Sortierung, Standard in Python |
| **sorted()** | `sorted(liste)` | Neue sortierte Liste, Original bleibt erhalten |
| **key-Parameter** | `sorted(liste, key=funktion)` | Sortierung nach benutzerdefiniertem Kriterium |
| **reverse-Parameter** | `sorted(liste, reverse=True)` | Absteigende Sortierung |

**Zentrale Erkenntnisse**:
- Sortieralgorithmen unterscheiden sich erheblich in ihrer Effizienz: O(n²) für einfache Algorithmen vs. O(n log n) für fortgeschrittene
- In-Place-Algorithmen (Bubble Sort, Insertion Sort) benötigen weniger Speicher als Algorithmen, die neue Listen erstellen
- Pythons eingebaute Sortierfunktionen verwenden Timsort, der für reale Daten optimiert ist und in fast allen Fällen verwendet werden sollte
- Die Wahl des Algorithmus hängt von der Datengröße, dem Grad der Vorsortierung und den Anforderungen (Speicher, Stabilität) ab
- Der `key`-Parameter ermöglicht flexible Sortierkriterien ohne Änderung der Daten

**Nächste Schritte**: Im folgenden Notebook (15 - Suchalgorithmen) werden Sie lernen, wie sortierte Daten effizient durchsucht werden können, insbesondere mit der binären Suche, die eine Zeitkomplexität von O(log n) erreicht.

+++

## Musterlösungen

<details>
<summary>Lösung zu Aufgabe 1</summary>

```python
def bubble_sort_strings(liste):
    """Sortiert Strings nach ihrer Länge mit Bubble Sort."""
    n = len(liste)
    
    for i in range(n):
        getauscht = False
        
        for j in range(0, n - i - 1):
            # Vergleiche Längen statt der Strings selbst
            if len(liste[j]) > len(liste[j + 1]):
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
                getauscht = True
        
        if not getauscht:
            break
    
    return liste

# Test
woerter = ["Python", "ist", "toll", "zu", "lernen"]
print("Original:", woerter)
sortiert = bubble_sort_strings(woerter.copy())
print("Nach Länge sortiert:", sortiert)
# Ausgabe: ['zu', 'ist', 'toll', 'Python', 'lernen']
```

**Erklärung**:
- Die Funktion verwendet die Bubble Sort Struktur, ändert aber den Vergleich von `liste[j] > liste[j + 1]` zu `len(liste[j]) > len(liste[j + 1])`
- Dadurch werden die Strings nicht alphabetisch, sondern nach ihrer Länge verglichen
- "zu" (2 Zeichen) kommt vor "ist" (3 Zeichen), usw.

**Häufige Fehler**:
- Vergessen, `len()` zu verwenden – dann würde alphabetisch sortiert
- Strings direkt vergleichen statt ihre Längen

</details>

+++

<details>
<summary>Lösung zu Aufgabe 2</summary>

```python
def ist_sortiert(liste):
    """Prüft, ob eine Liste aufsteigend sortiert ist."""
    # Leere Liste oder Liste mit einem Element ist sortiert
    if len(liste) <= 1:
        return True
    
    # Prüfe alle benachbarten Paare
    for i in range(len(liste) - 1):
        if liste[i] > liste[i + 1]:
            # Gefunden: Element größer als Nachfolger
            return False
    
    # Kein unsortiertes Paar gefunden
    return True

# Tests
print(ist_sortiert([1, 2, 3, 4]))        # True
print(ist_sortiert([1, 3, 2, 4]))        # False
print(ist_sortiert([]))                   # True
print(ist_sortiert([5]))                  # True
print(ist_sortiert([1, 1, 2, 2, 3]))     # True (gleiche Werte erlaubt)
```

**Erklärung**:
- Die Funktion iteriert durch alle benachbarten Elementpaare
- Sobald ein Paar gefunden wird, bei dem das linke Element größer ist als das rechte, ist die Liste nicht sortiert
- Wenn die Schleife vollständig durchläuft ohne ein solches Paar zu finden, ist die Liste sortiert

**Alternative Lösung** (kompakter, aber weniger effizient bei nicht-sortierten Listen):
```python
def ist_sortiert_kurz(liste):
    return liste == sorted(liste)
```
Diese Version sortiert die Liste und vergleicht das Ergebnis mit dem Original. Sie ist kürzer, aber O(n log n) statt O(n).

</details>

+++

<details>
<summary>Lösung zu Aufgabe 3</summary>

```python
def top_n_elemente(liste, n):
    """Gibt die n größten Elemente einer Liste zurück."""
    # Sortiere die Liste absteigend
    sortierte_liste = sorted(liste, reverse=True)
    
    # Nimm die ersten n Elemente
    return sortierte_liste[:n]

# Test
zahlen = [5, 2, 8, 1, 9, 3, 7, 4, 6]
print("Liste:", zahlen)
print("Top 3:", top_n_elemente(zahlen, 3))
# Ausgabe: [9, 8, 7]
print("Top 5:", top_n_elemente(zahlen, 5))
# Ausgabe: [9, 8, 7, 6, 5]
```

**Erklärung**:
- Die Funktion sortiert die Liste absteigend mit `reverse=True`
- Dann werden die ersten n Elemente mit Slicing `[:n]` extrahiert
- Dies sind automatisch die n größten Elemente

**Alternative Ansätze**:
```python
# Mit eigenem Quicksort
def top_n_quicksort(liste, n):
    sortiert = quicksort(liste)
    return sortiert[-n:]  # Letzte n Elemente (größte)

# Effizienter für sehr große Listen und kleines n:
def top_n_effizient(liste, n):
    # Nur teilweises Sortieren wäre effizienter,
    # aber dafür bräuchten wir Konzepte aus späteren Notebooks
    return sorted(liste, reverse=True)[:n]
```

</details>

+++

<details>
<summary>Lösung zu Aufgabe 4</summary>

```python
def sortiere_woerterbuch_nach_wert(woerterbuch):
    """Sortiert ein Dictionary nach seinen Werten."""
    
    # Konvertiere zu Liste von Tupeln (schluessel, wert)
    items = woerterbuch.items()
    
    # Definiere Sortierfunktion: sortiere nach Wert (zweites Element des Tupels)
    def nach_wert(item):
        schluessel, wert = item
        return wert
    
    # Sortiere mit der Funktion als key
    sortierte_items = sorted(items, key=nach_wert)
    
    return sortierte_items

# Test
noten = {"Anna": 1.7, "Bob": 2.3, "Clara": 1.3, "David": 2.0}
print("Original Dictionary:", noten)
sortiert = sortiere_woerterbuch_nach_wert(noten)
print("Sortiert nach Noten:", sortiert)
# Ausgabe: [('Clara', 1.3), ('Anna', 1.7), ('David', 2.0), ('Bob', 2.3)]
```

**Erklärung**:
- `woerterbuch.items()` liefert eine Ansicht auf die Key-Value-Paare als Tupel
- Die `key`-Funktion `nach_wert` extrahiert den Wert (zweites Element) aus jedem Tupel
- `sorted()` sortiert basierend auf diesen Werten

**Kompaktere Lösung** mit Lambda-Funktion (fortgeschritten, aber erlaubt):
```python
def sortiere_woerterbuch_kompakt(woerterbuch):
    return sorted(woerterbuch.items(), key=lambda item: item[1])
```

**Alternative mit Index-Zugriff**:
```python
def sortiere_woerterbuch_index(woerterbuch):
    def nach_wert(item):
        return item[1]  # Zweites Element des Tupels
    
    return sorted(woerterbuch.items(), key=nach_wert)
```

Beide Alternativen sind gültig. Die erste Lösung mit Unpacking (`schluessel, wert = item`) ist expliziter und leichter verständlich.

</details>
