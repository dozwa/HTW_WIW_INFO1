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

# 13 - Algorithmen: Grundlagen der Komplexitätsanalyse

## Lernziele

Nach Abschluss dieses Notebooks können Sie:
- Den Begriff **Algorithmus** definieren und von Programmen abgrenzen
- Die **Big-O-Notation** verstehen und gängige Komplexitätsklassen erkennen
- Die **Zeitkomplexität** einfacher Algorithmen durch Zählen von Operationen bestimmen
- Die **Speicherkomplexität** von Algorithmen analysieren
- Algorithmen anhand ihrer Komplexität vergleichen und bewerten

**Kompetenzstufen**: Verstehen, Anwenden, Analysieren

---

## Voraussetzungen

Für dieses Notebook sollten Sie folgende Konzepte beherrschen:
- Funktionen definieren mit `def` und `return` (Notebook 07)
- Schleifen (`for`, `while`) und `range()` (Notebook 10)
- Listen, Tupel und grundlegende Listenoperationen (Notebook 06)
- Verschachtelte Schleifen und deren Funktionsweise (Notebook 10)

Falls Sie diese Konzepte noch nicht sicher beherrschen, wiederholen Sie bitte die entsprechenden Notebooks.

---

+++

## 1. Was ist ein Algorithmus?

### Einführung und Motivation

In den bisherigen Notebooks haben Sie gelernt, wie man Variablen verwendet, Funktionen definiert und mit Schleifen arbeitet. Sie haben damit bereits viele **Programme** geschrieben. Doch was unterscheidet ein Programm von einem **Algorithmus**?

Ein **Algorithmus** ist eine präzise, endliche Folge von Anweisungen zur Lösung eines klar definierten Problems. Algorithmen sind sprachunabhängig – derselbe Algorithmus kann in Python, Java oder einer anderen Programmiersprache implementiert werden. Ein **Programm** hingegen ist die konkrete Umsetzung eines Algorithmus in einer bestimmten Programmiersprache.

Algorithmen sind das konzeptionelle Fundament der Informatik. Sie beschreiben **wie** ein Problem gelöst wird, unabhängig davon, in welcher Sprache oder auf welchem Computer die Lösung später ausgeführt wird.

+++

### Eigenschaften eines Algorithmus

Ein korrekter Algorithmus muss folgende Eigenschaften erfüllen:

1. **Eindeutigkeit**: Jeder Schritt ist präzise definiert und lässt keine Interpretationsspielräume
2. **Endlichkeit der Beschreibung**: Der Algorithmus muss in endlich vielen Zeilen beschrieben werden können
3. **Terminiertheit**: Der Algorithmus muss nach endlich vielen Schritten enden
4. **Determinismus**: Bei gleicher Eingabe liefert der Algorithmus stets dasselbe Ergebnis
5. **Effektivität**: Jeder Schritt muss tatsächlich ausführbar sein

Diese formalen Eigenschaften stellen sicher, dass Algorithmen zuverlässig und reproduzierbar funktionieren.

+++

### Beispiele für Algorithmen aus dem Alltag

Algorithmen begegnen uns nicht nur in der Informatik, sondern auch im Alltag:

- **Kochrezept**: Eine Schritt-für-Schritt-Anleitung zum Zubereiten eines Gerichts
- **Wegbeschreibung**: Anweisungen, um von Punkt A nach Punkt B zu gelangen
- **Montageanleitung**: Schritte zum Zusammenbauen eines Möbelstücks

Diese Beispiele zeigen: Ein Algorithmus ist immer eine **Handlungsanweisung** zur systematischen Lösung eines Problems.

+++

### Beispiel 1: Ein einfacher Algorithmus in Python

Betrachten Sie folgenden Algorithmus, der die Summe aller Zahlen von 1 bis n berechnet:

```{code-cell} ipython3
def summe_bis_n(n):
    """Berechnet die Summe aller Zahlen von 1 bis n."""
    summe = 0
    for i in range(1, n + 1):
        summe += i
    return summe

# Algorithmus anwenden
ergebnis = summe_bis_n(5)
print(f"Summe von 1 bis 5: {ergebnis}")
```

**Erwartete Ausgabe**:
```
Summe von 1 bis 5: 15
```

**Erklärung**: Der Algorithmus durchläuft alle Zahlen von 1 bis n und addiert sie schrittweise zur Variable `summe`. Am Ende wird die Gesamtsumme zurückgegeben. Dieser Algorithmus ist eindeutig, deterministisch und terminiert nach genau n Schritten.

+++

### Angeleitete Übung 1.1

**Aufgabe**: Schreiben Sie einen Algorithmus, der das Produkt aller Zahlen von 1 bis n berechnet (Fakultät).

**Hinweise**:
- Schritt 1: Definieren Sie eine Funktion `fakultaet(n)`
- Schritt 2: Initialisieren Sie eine Variable `produkt` mit dem Wert 1
- Schritt 3: Verwenden Sie eine `for`-Schleife mit `range(1, n + 1)`
- Schritt 4: Multiplizieren Sie in jedem Schleifendurchlauf `produkt` mit der aktuellen Zahl
- Schritt 5: Geben Sie das Ergebnis zurück

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
def fakultaet(n):
    """Berechnet die Fakultät von n (n!)."""
    produkt = 1
    for i in range(1, n + 1):
        produkt *= i
    return produkt

# Test
print(f"5! = {fakultaet(5)}")
```

**Erklärung**: Die Fakultät ist das Produkt aller positiven ganzen Zahlen bis n. Der Algorithmus startet mit `produkt = 1` und multipliziert in jedem Schritt die aktuelle Zahl hinzu. Für n=5 ergibt sich: 1×2×3×4×5 = 120.
</details>

+++

### Angeleitete Übung 1.2

**Aufgabe**: Schreiben Sie einen Algorithmus, der prüft, ob eine gegebene Zahl eine Primzahl ist.

**Hinweise**:
- Eine Primzahl ist nur durch 1 und sich selbst teilbar
- Prüfen Sie, ob die Zahl durch irgendeine Zahl von 2 bis n-1 teilbar ist
- Verwenden Sie den Modulo-Operator `%` zur Prüfung auf Teilbarkeit
- Geben Sie `True` zurück, wenn die Zahl prim ist, sonst `False`

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
def ist_primzahl(n):
    """Prüft, ob n eine Primzahl ist."""
    if n < 2:
        return False
    
    for teiler in range(2, n):
        if n % teiler == 0:
            return False
    
    return True

# Tests
print(f"7 ist Primzahl: {ist_primzahl(7)}")
print(f"8 ist Primzahl: {ist_primzahl(8)}")
```

**Erklärung**: Der Algorithmus prüft systematisch alle möglichen Teiler von 2 bis n-1. Sobald ein Teiler gefunden wird (Rest der Division ist 0), kann die Zahl keine Primzahl sein. Wird kein Teiler gefunden, ist die Zahl prim.
</details>

+++

---

## 2. Warum Algorithmen analysieren?

### Einführung und Motivation

Sie haben nun verstanden, was ein Algorithmus ist. Doch nicht alle Algorithmen sind gleich gut! Manche sind schnell, andere langsam. Manche benötigen viel Speicher, andere wenig.

Betrachten Sie folgendes Problem: Sie möchten die Summe aller Zahlen von 1 bis n berechnen. Sie haben bereits einen Algorithmus mit einer Schleife kennengelernt. Es gibt aber auch einen direkten mathematischen Ansatz:

**Algorithmus 1 (mit Schleife)**: Summiere alle Zahlen von 1 bis n nacheinander

**Algorithmus 2 (mit Formel)**: Verwende die Formel n × (n + 1) / 2

Welcher Algorithmus ist besser? Um diese Frage zu beantworten, müssen wir Algorithmen **analysieren** und **vergleichen** können.

+++

### Kriterien zur Bewertung von Algorithmen

Bei der Analyse von Algorithmen betrachten wir hauptsächlich zwei Aspekte:

1. **Zeitkomplexität**: Wie lange dauert die Ausführung in Abhängigkeit von der Eingabegröße?
2. **Speicherkomplexität**: Wie viel Arbeitsspeicher wird in Abhängigkeit von der Eingabegröße benötigt?

Beide Aspekte hängen von der **Eingabegröße** ab, die wir üblicherweise mit **n** bezeichnen. Je größer n ist, desto mehr Zeit und Speicher kann ein Algorithmus benötigen.

**Warum ist das wichtig?**
- Ein Algorithmus, der für n=10 schnell ist, kann für n=1.000.000 unbenutzbar langsam sein
- Ressourcen (Zeit und Speicher) sind begrenzt – effiziente Algorithmen sind entscheidend
- Die Wahl des richtigen Algorithmus kann den Unterschied zwischen Sekunden und Stunden Laufzeit ausmachen

+++

### Beispiel 2: Zwei Algorithmen im Vergleich

Vergleichen wir die beiden Algorithmen zur Berechnung der Summe von 1 bis n:

```{code-cell} ipython3
def summe_mit_schleife(n):
    """Algorithmus 1: Summe mit Schleife berechnen."""
    summe = 0
    for i in range(1, n + 1):
        summe += i
    return summe

def summe_mit_formel(n):
    """Algorithmus 2: Summe mit mathematischer Formel berechnen."""
    return n * (n + 1) // 2

# Beide Algorithmen testen
n = 100
print(f"Algorithmus 1 (Schleife): {summe_mit_schleife(n)}")
print(f"Algorithmus 2 (Formel): {summe_mit_formel(n)}")
```

**Erwartete Ausgabe**:
```
Algorithmus 1 (Schleife): 5050
Algorithmus 2 (Formel): 5050
```

**Erklärung**: Beide Algorithmen liefern dasselbe Ergebnis. Doch Algorithmus 1 muss n Schritte durchlaufen, während Algorithmus 2 nur eine einzige Berechnung durchführt. Bei n=100 ist der Unterschied gering, aber bei n=1.000.000 wird er erheblich. Diese Unterschiede zu verstehen und zu quantifizieren, ist das Ziel der Komplexitätsanalyse.

+++

### Angeleitete Übung 2.1

**Aufgabe**: Implementieren Sie zwei Algorithmen zur Prüfung, ob eine Zahl in einer Liste enthalten ist: (1) mit einer Schleife, (2) mit dem `in`-Operator.

**Hinweise**:
- Algorithmus 1: Durchlaufen Sie die Liste mit einer `for`-Schleife und vergleichen Sie jedes Element
- Algorithmus 2: Verwenden Sie den eingebauten `in`-Operator
- Testen Sie beide mit einer Liste `[1, 2, 3, 4, 5]` und der Zahl 3

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
def suche_mit_schleife(liste, ziel):
    """Sucht ein Element mit einer Schleife."""
    for element in liste:
        if element == ziel:
            return True
    return False

def suche_mit_in(liste, ziel):
    """Sucht ein Element mit dem in-Operator."""
    return ziel in liste

# Tests
zahlen = [1, 2, 3, 4, 5]
print(f"Mit Schleife: {suche_mit_schleife(zahlen, 3)}")
print(f"Mit in-Operator: {suche_mit_in(zahlen, 3)}")
```

**Erklärung**: Beide Algorithmen lösen dasselbe Problem. Der `in`-Operator ist jedoch prägnanter und intern optimiert. Beide haben dieselbe grundlegende Funktionsweise: Sie durchlaufen die Liste, bis das Element gefunden wird.
</details>

+++

---

## 3. Big-O-Notation

### Einführung und Motivation

Um Algorithmen vergleichen zu können, benötigen wir eine einheitliche **Notation** zur Beschreibung ihrer Effizienz. Die **Big-O-Notation** (auch Landau-Notation genannt) ist das Standardwerkzeug der Informatik zur Beschreibung der Zeitkomplexität.

Die Big-O-Notation beschreibt, wie die Laufzeit eines Algorithmus **im schlimmsten Fall** wächst, wenn die Eingabegröße n gegen unendlich strebt. Sie abstrahiert von konkreten Zeitmessungen und Hardware-Unterschieden und fokussiert sich auf das **asymptotische Wachstumsverhalten**.

**Warum "Big-O"?**
- **O** steht für "Ordnung" (englisch: Order)
- Die Notation beschreibt die Größenordnung der Laufzeit
- Konstante Faktoren und niedrigere Terme werden ignoriert, da sie für große n vernachlässigbar sind

+++

### Die wichtigsten Komplexitätsklassen

Folgende Komplexitätsklassen begegnen Ihnen am häufigsten (von schnell zu langsam):

| Notation | Name | Beispiel |
|----------|------|----------|
| O(1) | Konstant | Zugriff auf Listenelement per Index |
| O(log n) | Logarithmisch | Binäre Suche (wird in Notebook 15 behandelt) |
| O(n) | Linear | Durchlaufen einer Liste |
| O(n log n) | Linearithmisch | Effiziente Sortieralgorithmen (Notebook 14) |
| O(n²) | Quadratisch | Verschachtelte Schleife über dieselbe Liste |
| O(2^n) | Exponentiell | Rekursive Fibonacci-Berechnung |

**Interpretation**:
- **O(1)**: Die Laufzeit ist unabhängig von n – egal wie groß die Eingabe ist, die Zeit bleibt konstant
- **O(n)**: Die Laufzeit wächst proportional zu n – doppelte Eingabegröße bedeutet doppelte Laufzeit
- **O(n²)**: Die Laufzeit wächst quadratisch – doppelte Eingabegröße bedeutet vierfache Laufzeit

+++

### Visualisierung der Komplexitätsklassen

Da wir noch keine Plotting-Bibliotheken kennengelernt haben, betrachten wir das Wachstum anhand einer Tabelle:

```{code-cell} ipython3
# Vergleich der Operationen für verschiedene n-Werte
import math

def vergleiche_komplexitaeten(n_werte):
    """Zeigt Anzahl der Operationen für verschiedene Komplexitätsklassen."""
    print(f"{'n':>10} | {'O(1)':>12} | {'O(log n)':>12} | {'O(n)':>12} | {'O(n log n)':>12} | {'O(n²)':>12}")
    print("-" * 85)
    
    for n in n_werte:
        o_1 = 1
        o_log_n = int(math.log2(n))
        o_n = n
        o_n_log_n = int(n * math.log2(n))
        o_n2 = n * n
        
        print(f"{n:>10} | {o_1:>12} | {o_log_n:>12} | {o_n:>12} | {o_n_log_n:>12} | {o_n2:>12}")

# Tabelle erstellen
vergleiche_komplexitaeten([10, 100, 1000, 10000])
```

**Erwartete Ausgabe** (ungefähr):
```
         n |         O(1) |     O(log n) |         O(n) |   O(n log n) |         O(n²)
-------------------------------------------------------------------------------------
        10 |            1 |            3 |           10 |           33 |          100
       100 |            1 |            6 |          100 |          664 |       10000
      1000 |            1 |            9 |         1000 |         9965 |     1000000
     10000 |            1 |           13 |        10000 |       132877 |   100000000
```

**Erklärung**: Die Tabelle zeigt eindrucksvoll, wie unterschiedlich Algorithmen mit steigender Eingabegröße skalieren. Bei n=10000 benötigt ein O(n²)-Algorithmus 100 Millionen Operationen, während ein O(log n)-Algorithmus nur 13 Operationen durchführt!

+++

### Beispiel 3: Komplexitätsklassen erkennen

Betrachten Sie folgende Funktionen und ihre Komplexitätsklassen:

```{code-cell} ipython3
# O(1) - Konstante Zeit
def erstes_element(liste):
    """Gibt das erste Element einer Liste zurück."""
    return liste[0]

# O(n) - Lineare Zeit
def liste_durchlaufen(liste):
    """Durchläuft alle Elemente einer Liste."""
    for element in liste:
        print(element)

# O(n²) - Quadratische Zeit
def alle_paare(liste):
    """Gibt alle möglichen Paare aus einer Liste aus."""
    for i in liste:
        for j in liste:
            print(f"({i}, {j})")
```

**Erklärung**:
- `erstes_element()`: Der Zugriff auf ein Listenelement per Index ist immer gleich schnell, egal wie lang die Liste ist → **O(1)**
- `liste_durchlaufen()`: Die Schleife wird n-mal durchlaufen (n = Länge der Liste) → **O(n)**
- `alle_paare()`: Zwei verschachtelte Schleifen über dieselbe Liste ergeben n × n = n² Durchläufe → **O(n²)**

+++

### Angeleitete Übung 3.1

**Aufgabe**: Bestimmen Sie die Komplexitätsklasse folgender Funktion:

```python
def summe_liste(liste):
    summe = 0
    for zahl in liste:
        summe += zahl
    return summe
```

**Hinweise**:
- Zählen Sie, wie oft die Schleife durchlaufen wird
- Überlegen Sie, wie viele Operationen bei einer Liste mit n Elementen durchgeführt werden
- Ordnen Sie das Ergebnis einer der Komplexitätsklassen zu

```{code-cell} ipython3
# Ihre Analyse hier als Kommentar:
# Komplexität: ???
# Begründung: ???
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

**Komplexität**: O(n)

**Begründung**: Die Funktion durchläuft die Liste genau einmal mit einer `for`-Schleife. Bei n Elementen werden n Additionen durchgeführt. Die Anzahl der Operationen wächst linear mit der Größe der Eingabe → **O(n)**.
</details>

+++

### Angeleitete Übung 3.2

**Aufgabe**: Bestimmen Sie die Komplexitätsklasse folgender Funktion:

```python
def maximum_finden(liste):
    maximum = liste[0]
    for zahl in liste:
        if zahl > maximum:
            maximum = zahl
    return maximum
```

**Hinweise**:
- Wie oft wird die Schleife durchlaufen?
- Sind die Operationen innerhalb der Schleife konstant?

```{code-cell} ipython3
# Ihre Analyse hier als Kommentar:
# Komplexität: ???
# Begründung: ???
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

**Komplexität**: O(n)

**Begründung**: Die Schleife durchläuft alle n Elemente der Liste. Innerhalb der Schleife werden nur Vergleiche und Zuweisungen durchgeführt (konstante Zeit). Insgesamt also n Durchläufe mit konstanten Operationen → **O(n)**.
</details>

+++

---

## 4. Zeitkomplexität berechnen

### Einführung und Motivation

Sie wissen nun, was die Big-O-Notation bedeutet und kennen die wichtigsten Komplexitätsklassen. Doch wie bestimmt man die Zeitkomplexität eines konkreten Algorithmus?

Die Zeitkomplexität wird ermittelt, indem man die **Anzahl der elementaren Operationen** in Abhängigkeit von der Eingabegröße n analysiert. Elementare Operationen sind beispielsweise:
- Zuweisungen (`x = 5`)
- Vergleiche (`x > y`)
- Arithmetische Operationen (`x + y`)
- Zugriffe auf Datenstrukturen (`liste[i]`)

Das Ziel ist nicht, die exakte Anzahl zu ermitteln, sondern die **Größenordnung** zu bestimmen.

+++

### Methodik: Operationen zählen

Um die Zeitkomplexität zu berechnen, gehen Sie wie folgt vor:

1. **Identifizieren Sie alle Operationen** im Code
2. **Zählen Sie, wie oft jede Operation** in Abhängigkeit von n ausgeführt wird
3. **Summieren Sie die Anzahl der Operationen**
4. **Reduzieren Sie auf die Big-O-Notation**: Behalten Sie nur den dominanten Term und ignorieren Sie konstante Faktoren

**Beispiel**: Wenn Sie 3n² + 5n + 7 Operationen haben, ist die Komplexität **O(n²)**, da n² für große n den Ausdruck dominiert.

+++

### Beispiel 4: Schritt-für-Schritt-Analyse

Analysieren wir die Zeitkomplexität der Funktion `summe_bis_n()` aus Beispiel 1:

```{code-cell} ipython3
def summe_bis_n(n):
    summe = 0              # Operation 1: Eine Zuweisung (konstant)
    for i in range(1, n + 1):  # Operation 2: n Iterationen
        summe += i         # Operation 3: n Additionen und Zuweisungen
    return summe           # Operation 4: Eine Rückgabe (konstant)
```

**Analyse**:
- **Zeile 2** (`summe = 0`): 1 Operation
- **Zeile 3** (Schleifenkopf): Die Schleife läuft n Mal
- **Zeile 4** (`summe += i`): Wird n Mal ausgeführt → n Operationen
- **Zeile 5** (`return summe`): 1 Operation

**Gesamt**: 1 + n + 1 = n + 2 Operationen

**Big-O-Notation**: Der dominierende Term ist n. Konstanten werden ignoriert → **O(n)**

+++

### Beispiel 5: Verschachtelte Schleifen

Betrachten wir einen Algorithmus mit verschachtelten Schleifen:

```{code-cell} ipython3
def kombiniere_paarweise(liste):
    """Erzeugt alle möglichen Paare aus einer Liste (ohne Wiederholung)."""
    ergebnisse = []
    n = len(liste)
    
    for i in range(n):
        for j in range(i + 1, n):
            ergebnisse.append((liste[i], liste[j]))
    
    return ergebnisse

# Test
zahlen = [1, 2, 3, 4]
paare = kombiniere_paarweise(zahlen)
print("Alle Paare:")
for paar in paare:
    print(paar)
```

**Erwartete Ausgabe**:
```
Alle Paare:
(1, 2)
(1, 3)
(1, 4)
(2, 3)
(2, 4)
(3, 4)
```

**Analyse**:
- Die äußere Schleife läuft n Mal
- Die innere Schleife läuft im Durchschnitt etwa n/2 Mal (da sie bei i+1 startet)
- Insgesamt: n × (n/2) ≈ n²/2 Operationen

**Big-O-Notation**: Der dominierende Term ist n²/2. Konstante Faktoren werden ignoriert → **O(n²)**

+++

### Angeleitete Übung 4.1

**Aufgabe**: Analysieren Sie die Zeitkomplexität folgender Funktion:

```python
def enthaelt_duplikat(liste):
    for i in range(len(liste)):
        for j in range(i + 1, len(liste)):
            if liste[i] == liste[j]:
                return True
    return False
```

**Hinweise**:
- Zählen Sie die Schleifeniterationen
- Beachten Sie, dass es zwei verschachtelte Schleifen gibt
- Bestimmen Sie die Komplexitätsklasse

```{code-cell} ipython3
# Ihre Analyse hier als Kommentar:
# Äußere Schleife: ??? Iterationen
# Innere Schleife: ??? Iterationen
# Gesamt: ???
# Komplexität: ???
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

**Analyse**:
- **Äußere Schleife**: Läuft n Mal (für jedes Element)
- **Innere Schleife**: Läuft im Durchschnitt n/2 Mal (startet bei i+1)
- **Operationen innerhalb**: Vergleich (konstante Zeit)
- **Gesamt**: n × (n/2) ≈ n²/2 Operationen

**Komplexität**: O(n²)

**Begründung**: Zwei verschachtelte Schleifen über dieselbe Datenstruktur führen typischerweise zu quadratischer Komplexität. Der konstante Faktor 1/2 wird in der Big-O-Notation ignoriert.
</details>

+++

### Angeleitete Übung 4.2

**Aufgabe**: Implementieren Sie eine Funktion, die prüft, ob eine Liste sortiert ist, und analysieren Sie ihre Zeitkomplexität.

**Hinweise**:
- Durchlaufen Sie die Liste und vergleichen Sie aufeinanderfolgende Elemente
- Wenn ein Element größer als das nächste ist, ist die Liste nicht sortiert
- Bestimmen Sie anschließend die Komplexität

```{code-cell} ipython3
# Ihr Code hier

# Ihre Komplexitätsanalyse als Kommentar:
# Komplexität: ???
# Begründung: ???
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
def ist_sortiert(liste):
    """Prüft, ob eine Liste aufsteigend sortiert ist."""
    for i in range(len(liste) - 1):
        if liste[i] > liste[i + 1]:
            return False
    return True

# Tests
print(f"[1,2,3,4] sortiert: {ist_sortiert([1,2,3,4])}")
print(f"[1,3,2,4] sortiert: {ist_sortiert([1,3,2,4])}")
```

**Komplexität**: O(n)

**Begründung**: Die Funktion durchläuft die Liste genau einmal (n-1 Vergleiche bei n Elementen). Es gibt keine verschachtelten Schleifen. Die Anzahl der Operationen wächst linear mit der Eingabegröße.
</details>

+++

---

## 5. Speicherkomplexität

### Einführung und Motivation

Neben der Zeit ist auch der **Speicherverbrauch** ein wichtiger Aspekt bei der Bewertung von Algorithmen. Die **Speicherkomplexität** (oder Platzkomplexität) beschreibt, wie viel zusätzlicher Arbeitsspeicher ein Algorithmus in Abhängigkeit von der Eingabegröße n benötigt.

Wichtig: Es geht um den **zusätzlichen** Speicher, nicht um den Speicher für die Eingabedaten selbst. Wenn Sie eine Liste mit n Elementen als Eingabe haben, zählt diese nicht zur Speicherkomplexität – nur neu angelegte Datenstrukturen innerhalb des Algorithmus.

Auch für die Speicherkomplexität verwenden wir die Big-O-Notation.

+++

### Methodik: Speicher analysieren

Um die Speicherkomplexität zu bestimmen, fragen Sie sich:

1. **Welche neuen Datenstrukturen** werden angelegt? (Listen, Tupel, Dictionaries)
2. **Wie groß werden diese Strukturen** in Abhängigkeit von n?
3. **Wie viele lokale Variablen** werden verwendet?

**Beispiele**:
- Eine einzige Variable (egal welcher Wert) → **O(1)**
- Eine Liste mit n Elementen → **O(n)**
- Eine Matrix mit n×n Elementen → **O(n²)**

+++

### Beispiel 6: Speicherkomplexität O(1)

Ein Algorithmus mit konstantem Speicherbedarf:

```{code-cell} ipython3
def summe_bis_n(n):
    """Berechnet die Summe von 1 bis n."""
    summe = 0
    for i in range(1, n + 1):
        summe += i
    return summe
```

**Speicheranalyse**:
- Variable `summe`: 1 Integer (konstant)
- Variable `i`: 1 Integer (konstant)
- Keine zusätzlichen Datenstrukturen

**Speicherkomplexität**: O(1) – Der Speicherbedarf ist unabhängig von n

+++

### Beispiel 7: Speicherkomplexität O(n)

Ein Algorithmus, der eine neue Liste erstellt:

```{code-cell} ipython3
def quadrate_liste(n):
    """Erstellt eine Liste mit Quadratzahlen von 1 bis n."""
    quadrate = []
    for i in range(1, n + 1):
        quadrate.append(i * i)
    return quadrate

# Test
print(quadrate_liste(5))
```

**Erwartete Ausgabe**:
```
[1, 4, 9, 16, 25]
```

**Speicheranalyse**:
- Liste `quadrate`: Enthält n Elemente
- Variable `i`: Konstanter Speicher

**Speicherkomplexität**: O(n) – Die Liste wächst proportional zur Eingabegröße

+++

### Beispiel 8: Speicherkomplexität O(n²)

Ein Algorithmus, der eine Matrix (Liste von Listen) erstellt:

```{code-cell} ipython3
def multiplikationstabelle(n):
    """Erstellt eine n×n Multiplikationstabelle."""
    tabelle = []
    for i in range(1, n + 1):
        zeile = []
        for j in range(1, n + 1):
            zeile.append(i * j)
        tabelle.append(zeile)
    return tabelle

# Test
tabelle = multiplikationstabelle(4)
for zeile in tabelle:
    print(zeile)
```

**Erwartete Ausgabe**:
```
[1, 2, 3, 4]
[2, 4, 6, 8]
[3, 6, 9, 12]
[4, 8, 12, 16]
```

**Speicheranalyse**:
- Liste `tabelle`: Enthält n Listen
- Jede innere Liste enthält n Elemente
- Gesamt: n × n = n² Elemente

**Speicherkomplexität**: O(n²) – Die Matrix benötigt quadratischen Speicher

+++

### Angeleitete Übung 5.1

**Aufgabe**: Analysieren Sie die Speicherkomplexität folgender Funktion:

```python
def reverse_liste(liste):
    ergebnis = []
    for i in range(len(liste) - 1, -1, -1):
        ergebnis.append(liste[i])
    return ergebnis
```

**Hinweise**:
- Welche neuen Datenstrukturen werden erstellt?
- Wie groß ist die neue Liste in Abhängigkeit von n?

```{code-cell} ipython3
# Ihre Analyse hier als Kommentar:
# Neue Datenstrukturen: ???
# Größe: ???
# Speicherkomplexität: ???
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

**Analyse**:
- **Neue Datenstruktur**: Liste `ergebnis`
- **Größe**: Enthält n Elemente (alle Elemente der Eingabeliste)
- **Zusätzliche Variablen**: `i` (konstant)

**Speicherkomplexität**: O(n)

**Begründung**: Die neue Liste `ergebnis` wächst proportional zur Größe der Eingabeliste. Bei n Eingabeelementen werden n Elemente in der neuen Liste gespeichert.
</details>

+++

### Angeleitete Übung 5.2

**Aufgabe**: Implementieren Sie eine Funktion `doppelte_werte(liste)`, die jeden Wert in einer Liste verdoppelt und als neue Liste zurückgibt. Analysieren Sie Zeit- und Speicherkomplexität.

**Hinweise**:
- Durchlaufen Sie die Eingabeliste und multiplizieren Sie jeden Wert mit 2
- Speichern Sie die Ergebnisse in einer neuen Liste
- Analysieren Sie sowohl Zeit- als auch Speicherkomplexität

```{code-cell} ipython3
# Ihr Code hier

# Ihre Analyse als Kommentar:
# Zeitkomplexität: ???
# Speicherkomplexität: ???
# Begründung: ???
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
def doppelte_werte(liste):
    """Verdoppelt alle Werte in einer Liste."""
    ergebnis = []
    for wert in liste:
        ergebnis.append(wert * 2)
    return ergebnis

# Test
zahlen = [1, 2, 3, 4, 5]
print(f"Original: {zahlen}")
print(f"Verdoppelt: {doppelte_werte(zahlen)}")
```

**Zeitkomplexität**: O(n)
- Die Schleife läuft n Mal (einmal pro Element)
- Jede Operation innerhalb der Schleife ist konstant

**Speicherkomplexität**: O(n)
- Eine neue Liste mit n Elementen wird erstellt
- Zusätzliche Variablen sind konstant

**Begründung**: Sowohl Zeit als auch Speicher skalieren linear mit der Eingabegröße.
</details>

+++

---

## Abschlussübungen

Die folgenden Aufgaben testen Ihr Verständnis der in diesem Notebook erlernten Konzepte. Bearbeiten Sie die Aufgaben selbstständig und vergleichen Sie Ihre Lösung anschließend mit den Musterlösungen am Ende des Notebooks.

### Teil 1: Grundlegende Anwendung

**Kompetenzstufe**: Anwenden

Diese Aufgaben testen die direkte Anwendung der erlernten Konzepte.

+++

**Aufgabe 1**: Bestimmen Sie die Zeit- und Speicherkomplexität folgender Funktion:

```python
def finde_minimum(liste):
    minimum = liste[0]
    for element in liste:
        if element < minimum:
            minimum = element
    return minimum
```

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 1
# Ihre Analyse als Kommentar:
# Zeitkomplexität: ???
# Speicherkomplexität: ???
# Begründung: ???
```

**Aufgabe 2**: Implementieren Sie eine Funktion `enthält_element(liste, ziel)`, die prüft, ob ein Element in einer Liste vorhanden ist. Verwenden Sie eine einfache Schleife und analysieren Sie die Zeitkomplexität.

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 2

# Ihre Komplexitätsanalyse:
# Zeitkomplexität: ???
```

---

### Teil 2: Transfer und Problemlösung

**Kompetenzstufe**: Analysieren & Erschaffen

Diese Aufgaben erfordern die Kombination mehrerer Konzepte und eigenständiges Problemlösen.

+++

**Aufgabe 3**: Schreiben Sie eine Funktion `zähle_vorkommen(liste, element)`, die zählt, wie oft ein bestimmtes Element in einer Liste vorkommt. Analysieren Sie anschließend Zeit- und Speicherkomplexität.

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 3

# Ihre Komplexitätsanalyse:
# Zeitkomplexität: ???
# Speicherkomplexität: ???
```

**Aufgabe 4**: Implementieren Sie eine Funktion `matrix_transponieren(matrix)`, die eine n×m Matrix transponiert (Zeilen und Spalten vertauschen). Die Matrix ist als Liste von Listen gegeben. Analysieren Sie Zeit- und Speicherkomplexität.

**Beispiel**:
```python
eingabe = [[1, 2, 3],
           [4, 5, 6]]
           
ausgabe = [[1, 4],
           [2, 5],
           [3, 6]]
```

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 4

# Ihre Komplexitätsanalyse:
# Zeitkomplexität: ???
# Speicherkomplexität: ???
```

---

## Zusammenfassung

In diesem Notebook haben Sie folgende Konzepte kennengelernt:

| Konzept | Bedeutung | Anwendungsfall |
|---------|-----------|----------------|
| **Algorithmus** | Endliche Abfolge von Anweisungen zur Problemlösung | Grundlage für alle Programme |
| **Big-O-Notation** | Beschreibung des asymptotischen Wachstums | Vergleich von Algorithmen |
| **Zeitkomplexität** | Wie lange dauert ein Algorithmus? | Effizienzanalyse |
| **Speicherkomplexität** | Wie viel Speicher benötigt ein Algorithmus? | Ressourcenplanung |
| **O(1)** | Konstante Komplexität | Zugriff auf Listenelement per Index |
| **O(n)** | Lineare Komplexität | Eine Schleife über n Elemente |
| **O(n²)** | Quadratische Komplexität | Zwei verschachtelte Schleifen über n Elemente |

**Zentrale Erkenntnisse**:
- Algorithmen sind sprachunabhängige Lösungsstrategien, Programme sind deren konkrete Implementierung
- Die Big-O-Notation abstrahiert von Hardware und fokussiert auf das Wachstumsverhalten
- Verschachtelte Schleifen führen oft zu höherer Komplexität (O(n²) statt O(n))
- Speicherkomplexität bezieht sich auf zusätzlichen Speicher, nicht auf die Eingabedaten
- Die Wahl des Algorithmus kann dramatische Auswirkungen auf die Performance haben

**Nächste Schritte**: Im folgenden Notebook (14 - Sortieralgorithmen) werden Sie konkrete Algorithmen zum Sortieren von Daten kennenlernen und deren Komplexität analysieren.

---

+++

## Musterlösungen

<details>
<summary>Lösung zu Aufgabe 1</summary>

**Zeitkomplexität**: O(n)

**Speicherkomplexität**: O(1)

**Begründung**:
- **Zeit**: Die Funktion durchläuft die Liste genau einmal mit einer `for`-Schleife. Bei n Elementen werden n Vergleiche durchgeführt → O(n)
- **Speicher**: Es wird nur eine einzige Variable `minimum` verwendet, unabhängig von der Listengröße → O(1)

**Häufige Fehler**:
- Die Eingabeliste selbst zur Speicherkomplexität zählen (nur zusätzlicher Speicher zählt)
- Vergleiche als O(1) nicht erkennen (jeder einzelne Vergleich ist konstant)
</details>

<details>
<summary>Lösung zu Aufgabe 2</summary>

```python
def enthält_element(liste, ziel):
    """Prüft, ob ein Element in einer Liste vorhanden ist."""
    for element in liste:
        if element == ziel:
            return True
    return False

# Tests
zahlen = [1, 5, 3, 8, 2]
print(f"5 enthalten: {enthält_element(zahlen, 5)}")
print(f"7 enthalten: {enthält_element(zahlen, 7)}")
```

**Zeitkomplexität**: O(n)

**Erklärung**:
- Im schlechtesten Fall (Element nicht vorhanden) muss die gesamte Liste durchlaufen werden
- Bei n Elementen werden bis zu n Vergleiche durchgeführt
- Auch wenn die Funktion früher abbrechen kann (Best Case: O(1)), betrachten wir den Worst Case → O(n)

**Häufige Fehler**:
- Nur den Best Case betrachten (Element am Anfang gefunden)
- Die Big-O-Notation bezieht sich standardmäßig auf den Worst Case
</details>

<details>
<summary>Lösung zu Aufgabe 3</summary>

```python
def zähle_vorkommen(liste, element):
    """Zählt, wie oft ein Element in einer Liste vorkommt."""
    anzahl = 0
    for item in liste:
        if item == element:
            anzahl += 1
    return anzahl

# Test
zahlen = [1, 2, 3, 2, 4, 2, 5]
print(f"Die Zahl 2 kommt {zähle_vorkommen(zahlen, 2)} mal vor")
```

**Zeitkomplexität**: O(n)
- Die Schleife durchläuft alle n Elemente der Liste
- Jeder Vergleich und jede Addition ist eine konstante Operation

**Speicherkomplexität**: O(1)
- Es wird nur eine Variable `anzahl` verwendet
- Der Speicherbedarf ist unabhängig von der Listengröße

**Besonderheiten**:
- Diese Funktion könnte auch mit `liste.count(element)` gelöst werden
- Die eingebaute Methode hat dieselbe Komplexität O(n)
</details>

<details>
<summary>Lösung zu Aufgabe 4</summary>

```python
def matrix_transponieren(matrix):
    """Transponiert eine n×m Matrix."""
    if not matrix:
        return []
    
    zeilen = len(matrix)
    spalten = len(matrix[0])
    
    # Neue Matrix mit vertauschten Dimensionen erstellen
    transponiert = []
    for j in range(spalten):
        neue_zeile = []
        for i in range(zeilen):
            neue_zeile.append(matrix[i][j])
        transponiert.append(neue_zeile)
    
    return transponiert

# Test
matrix = [[1, 2, 3],
          [4, 5, 6]]
          
transponiert = matrix_transponieren(matrix)
print("Original:")
for zeile in matrix:
    print(zeile)
    
print("\nTransponiert:")
for zeile in transponiert:
    print(zeile)
```

**Zeitkomplexität**: O(n × m)
- Die äußere Schleife läuft `spalten` Mal (m)
- Die innere Schleife läuft `zeilen` Mal (n)
- Jedes Element wird genau einmal kopiert
- Gesamt: n × m Operationen

**Speicherkomplexität**: O(n × m)
- Eine neue Matrix mit m Zeilen und n Spalten wird erstellt
- Die neue Matrix enthält n × m Elemente

**Alternative Ansätze**:
- Mit List Comprehension: `[[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]`
- Dieselbe Komplexität, aber kompakterer Code
- Für absolute Anfänger ist die explizite Schleifenversion verständlicher
</details>
