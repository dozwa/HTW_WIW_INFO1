---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
---

## 4. Suchalgorithmen

Suchalgorithmen dienen dazu, ein bestimmtes Element in einer Datenstruktur zu finden.

### Anwendungsbeispiele

- **Telefonbuchsuche**: Finden einer Telefonnummer anhand eines Namens.
- **Produktkatalog**: Finden eines Produkts in einem Online-Shop.
- **Datenbanken**: Abrufen von Datensätzen basierend auf Suchkriterien.

Wir betrachten drei Suchalgorithmen:

- **Lineare Suche**: Einfach, aber ineffizient bei großen Datenmengen.
- **Hash-basierte Suche**: Sehr effizient, benötigt jedoch zusätzliche Datenstrukturen.
- **Binäre Suche**: Effizient, aber erfordert sortierte Daten.

+++

### 4.1 Lineare Suche

#### Funktionsweise

Die lineare Suche durchläuft die Liste von Anfang bis Ende und vergleicht jedes Element mit dem gesuchten Wert.

```{code-cell}
def lineare_suche(arr, x):
    for index, element in enumerate(arr):
        # print(f"Prüfe Index {index}: Wert {element}")
        if element == x:
            print(f"Element {x} gefunden an Position {index}")
            return index
    print(f"Element {x} nicht gefunden")
    return -1  # Element nicht gefunden

# Beispiel
liste = [4, 2, 5, 1, 3]
lineare_suche(liste, 5)
```

#### Zeitkomplexität

- **Best Case**: O(1) (wenn das Element an erster Stelle steht)
- **Worst Case**: O(n) (wenn das Element am Ende steht oder nicht vorhanden ist)

#### Speicherkomplexität

- **Zusätzlicher Speicherbedarf**: O(1)
- Es wird kein zusätzlicher Speicher proportional zur Eingabedatenmenge benötigt.

+++

### 4.2 Binäre Suche

#### Voraussetzungen

- Die Liste muss **sortiert** sein.

#### Funktionsweise

Die binäre Suche halbiert den Suchraum bei jedem Schritt.

```{code-cell}
def binaere_suche(arr, x):
    links, rechts = 0, len(arr) - 1
    while links <= rechts:
        mitte = (links + rechts) // 2
        # print(f"Suche zwischen Index {links} und {rechts}, Mitte: {mitte}")
        if arr[mitte] == x:
            print(f"Element {x} gefunden an Position {mitte}")
            return mitte
        elif arr[mitte] < x:
            links = mitte + 1
        else:
            rechts = mitte - 1
    print(f"Element {x} nicht gefunden")
    return -1  # Element nicht gefunden

# Beispiel
sortierte_liste = [1, 2, 3, 4, 5]
binaere_suche(sortierte_liste, 4)
```

#### Zeitkomplexität

- **Best Case**: O(1)
- **Worst Case**: O(log n)

#### Speicherkomplexität

- **Zusätzlicher Speicherbedarf**: O(1)
- Es werden nur wenige zusätzliche Variablen verwendet, unabhängig von der Eingabedatenmenge.

+++

### Vergleich der Suchalgorithmen

Wir vergleichen die Suchalgorithmen **Lineare Suche** und **Binäre Suche** anhand einer Liste von 10.000 zufällig generierten Zahlen. Dabei messen wir die Zeit- und Speicherkomplexität der Algorithmen.

```{code-cell}
import random

# Generiere eine sortierte Liste mit 1.000 zufälligen Zahlen
daten = sorted(random.randint(1, 100000) for _ in range(1000))
gesuchter_wert = daten[random.randint(0, 999)]
```

```{code-cell}
# Lineare Suche
import time
import tracemalloc

start_time = time.time()
tracemalloc.start()
index_linear = lineare_suche(daten, gesuchter_wert)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
dauer_linear = time.time() - start_time
print(f"Lineare Suche Dauer: {dauer_linear:.5f} Sekunden, Index: {index_linear}")
print(f"Lineare Suche Speicherverbrauch: {peak / 10**6:.5f} MB")
```

```{code-cell}
# Binäre Suche
start_time = time.time()
tracemalloc.start()
index_binaer = binaere_suche(daten, gesuchter_wert)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
dauer_binaer = time.time() - start_time
print(f"Binäre Suche Dauer: {dauer_binaer:.5f} Sekunden, Index: {index_binaer}")
print(f"Binäre Suche Speicherverbrauch: {peak / 10**6:.5f} MB")
```

## Zusammenfassung

- **Algorithmen** sind essenziell für die Lösung von Problemen in der Informatik.
- Die **Analyse der Zeit- und Speicherkomplexität** hilft bei der Auswahl effizienter Algorithmen.
- **Bubble Sort**:
  - **Zeitkomplexität**: O(n²)
  - **Speicherkomplexität**: O(1)
- **Insertion Sort**:
  - **Zeitkomplexität**: O(n²)
  - **Speicherkomplexität**: O(1)
- **Lineare Suche**:
  - **Zeitkomplexität**: O(n)
  - **Speicherkomplexität**: O(1)
- **Binäre Suche**:
  - **Zeitkomplexität**: O(log n)
  - **Speicherkomplexität**: O(1)
