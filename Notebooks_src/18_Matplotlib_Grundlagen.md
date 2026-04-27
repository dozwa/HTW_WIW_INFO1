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

# 18 - Matplotlib Grundlagen: Einführung in die Datenvisualisierung

+++

## Lernziele

Nach Abschluss dieses Notebooks können Sie:
- Die Bedeutung von Datenvisualisierung in der Datenanalyse erklären
- Die Matplotlib-Bibliothek importieren und die pyplot-Schnittstelle verwenden
- Einfache Liniendiagramme mit `plt.plot()` erstellen und anpassen
- Balkendiagramme mit `plt.bar()` zur Darstellung kategorialer Daten erstellen
- Achsenbeschriftungen und Titel zu Diagrammen hinzufügen
- Das hierarchische Modell von Matplotlib (Figure, Axes) verstehen und anwenden

**Kompetenzstufen**: Verstehen, Anwenden

+++

## Voraussetzungen

Für dieses Notebook sollten Sie folgende Konzepte beherrschen:
- Variablen, Listen und Dictionaries (Notebooks 04-06)
- Schleifen und Kontrollstrukturen (Notebooks 09-10)
- Import von externen Bibliotheken (Notebook 16: Pandas)
- Grundlegende Datenverarbeitung mit Pandas (Notebooks 16-17)

Falls Sie diese Konzepte noch nicht sicher beherrschen, wiederholen Sie bitte die entsprechenden Notebooks.

+++

## Einführung: Warum Datenvisualisierung?

In den vorherigen Notebooks haben Sie gelernt, wie Sie Daten mit Pandas laden, verarbeiten und statistisch analysieren können. Sie können Mittelwerte berechnen, Daten gruppieren und Zusammenhänge in Zahlen ausdrücken. Diese numerischen Analysen sind wertvoll, doch sie haben eine Einschränkung: Menschen können komplexe Muster und Zusammenhänge in Zahlenkolonnen nur schwer erfassen.

Hier kommt die Datenvisualisierung ins Spiel. Die grafische Darstellung von Daten ermöglicht es, Muster, Trends und Ausreißer auf einen Blick zu erkennen. Ein Diagramm kann Zusammenhänge verdeutlichen, die in einer Tabelle verborgen bleiben würden. Visualisierungen sind daher ein unverzichtbares Werkzeug in der Datenanalyse – sowohl zur explorativen Analyse als auch zur Kommunikation von Ergebnissen.

**Beispiel**: Betrachten Sie folgende Temperaturdaten für eine Woche:
```
Mo: 18°C, Di: 20°C, Mi: 22°C, Do: 21°C, Fr: 19°C, Sa: 17°C, So: 16°C
```

Als Zahlenliste ist der Trend nicht sofort erkennbar. In einem Liniendiagramm würden Sie hingegen sofort sehen, dass die Temperatur zur Wochenmitte ansteigt und zum Wochenende hin wieder fällt.

In diesem Notebook lernen Sie Matplotlib kennen, die wichtigste Python-Bibliothek für Datenvisualisierung. Matplotlib ist seit 2003 in der wissenschaftlichen Gemeinschaft etabliert und bildet die Grundlage für viele andere Visualisierungsbibliotheken.

+++

## Matplotlib importieren und erste Schritte

### Theoretische Grundlagen

Matplotlib ist eine externe Bibliothek, die nicht zum Python-Standardumfang gehört. Ähnlich wie bei Pandas müssen Sie sie zunächst importieren, bevor Sie ihre Funktionen nutzen können. Die Bibliothek besteht aus verschiedenen Modulen, wobei `matplotlib.pyplot` die wichtigste Schnittstelle für die Erstellung von Diagrammen darstellt.

**Namenskonvention**: In der Python-Community hat sich die Konvention etabliert, `matplotlib.pyplot` unter dem Alias `plt` zu importieren. Dies verkürzt die Schreibweise und macht Code lesbarer. Diese Konvention ist so verbreitet, dass Sie sie in nahezu jedem Python-Projekt mit Datenvisualisierung finden werden.

**Syntax**:
```python
import matplotlib.pyplot as plt
```

**Semantik**:
- `import`: Python-Schlüsselwort zum Laden externer Module
- `matplotlib.pyplot`: Vollständiger Name des Moduls (Bibliothek.Untermodul)
- `as plt`: Erstellt einen Alias (Kurznamen) für das Modul
- Nach dem Import können Sie alle Funktionen über `plt.funktionsname()` aufrufen

Nach dem Import steht Ihnen die gesamte Funktionalität von pyplot zur Verfügung. Die beiden wichtigsten Grundfunktionen sind:
- `plt.plot()`: Erstellt Liniendiagramme
- `plt.show()`: Zeigt das erstellte Diagramm an

Das Prinzip ähnelt dem Malen eines Bildes: Sie erstellen zunächst die grafischen Elemente (mit `plot()`, `bar()`, etc.) und zeigen das fertige Werk dann an (mit `show()`).

+++

### Beispiel 1: Matplotlib importieren und erster Plot

```{code-cell} ipython3
# Importieren der Matplotlib-Bibliothek unter dem Alias plt
import matplotlib.pyplot as plt
```

Nach dem Import können Sie Ihre erste Visualisierung erstellen. Ein einfacher Plot benötigt nur eine Liste von Werten:

```{code-cell} ipython3
# Einfacher Plot mit fünf Datenpunkten
plt.plot([1, 2, 1, 4, 3])
plt.show()
```

**Was ist passiert?**

- Die Funktion `plt.plot()` erhält eine Liste mit fünf Werten: [1, 2, 1, 4, 3]
- Matplotlib interpretiert diese Werte als **y-Koordinaten** (Höhe der Punkte)
- Da keine x-Werte angegeben wurden, verwendet Matplotlib automatisch die **Indizes der Liste** als x-Koordinaten (0, 1, 2, 3, 4)
- Die Funktion `plt.show()` zeigt das fertige Diagramm an
- Das Ergebnis ist ein Liniendiagramm, das die Werte durch eine durchgezogene Linie verbindet

+++

### Angeleitete Übung 1.1: Ein W-Muster plotten

**Aufgabe**: Erstellen Sie einen Plot, der die Form des Buchstabens "W" nachbildet.

**Hinweise**:
- Überlegen Sie, welche y-Werte ein W-Muster ergeben: Start niedrig, hoch, niedrig, hoch, niedrig
- Eine mögliche Wertefolge wäre: [1, 5, 1, 5, 1]
- Verwenden Sie `plt.plot()` mit einer Liste von mindestens 5 Werten
- Vergessen Sie nicht `plt.show()` am Ende

```{code-cell} ipython3
# Ihr Code hier
```

<details>
<summary>Lösung anzeigen</summary>

```python
# W-Muster plotten
plt.plot([1, 5, 1, 5, 1])
plt.show()
```

**Erklärung**:
- Die Liste [1, 5, 1, 5, 1] erzeugt die charakteristische Zickzack-Form eines W
- Die Werte alternieren zwischen niedrig (1) und hoch (5)
- Matplotlib verbindet die Punkte automatisch mit Linien
- Sie können auch andere Werte verwenden, solange das Muster erhalten bleibt (z.B. [0, 4, 0, 4, 0])
</details>

+++

## Das hierarchische Modell von Matplotlib

### Theoretische Grundlagen

Um Matplotlib effektiv nutzen zu können, ist es wichtig, das zugrundeliegende hierarchische Modell zu verstehen. Matplotlib organisiert Visualisierungen in einer Struktur aus mehreren verschachtelten Objekten. Dieses Modell mag zunächst komplex erscheinen, ermöglicht aber große Flexibilität bei der Erstellung komplexer Visualisierungen.

Die drei wichtigsten Ebenen dieser Hierarchie sind:

**1. Figure (Figur)**
- Das oberste Objekt in der Hierarchie
- Entspricht dem gesamten Fenster oder der Bilddatei
- Kann ein oder mehrere Diagramme (Axes) enthalten
- Stellt Funktionen zur Verwaltung und Konfiguration der gesamten Visualisierung bereit

**2. Axes (Achsensystem / Diagramm)**
- Ein einzelnes Diagramm innerhalb einer Figure
- Enthält die x- und y-Achse sowie den Zeichenbereich
- Hier werden die eigentlichen Daten dargestellt (Linien, Balken, Punkte etc.)
- Eine Figure kann mehrere Axes enthalten (z.B. für mehrere Diagramme nebeneinander)

**3. Axis (Achse)**
- Die einzelnen Achsen (x-Achse, y-Achse) eines Diagramms
- Steuert Skalierung, Beschriftung und Teilstriche (Ticks)
- Jedes Axes-Objekt hat mindestens zwei Axis-Objekte (x und y)

**Wichtig**: Verwechseln Sie nicht "Axes" (Mehrzahl von Axis, bezeichnet aber ein ganzes Diagramm) mit "Axis" (eine einzelne Achse)! Diese Begriffe sind in Matplotlib spezifisch definiert.

+++

### Arbeiten mit Figure und Axes

Bisher haben Sie die einfache pyplot-Schnittstelle verwendet (`plt.plot()`). Diese erstellt automatisch im Hintergrund Figure- und Axes-Objekte. Für mehr Kontrolle können Sie diese Objekte auch explizit erstellen.

**Syntax**:
```python
fig, ax = plt.subplots()
```

**Semantik**:
- `plt.subplots()`: Erstellt eine neue Figure mit einem oder mehreren Axes
- Gibt zwei Werte zurück (deshalb die Zuweisung an zwei Variablen)
- `fig`: Das Figure-Objekt (die gesamte Abbildung)
- `ax`: Das Axes-Objekt (das Diagramm)
- Ohne Parameter erstellt die Funktion eine Figure mit einem einzelnen Axes

Mit den Parametern `nrows` und `ncols` (oder kurz als zwei Zahlen) können Sie mehrere Diagramme erstellen:
```python
fig, ax = plt.subplots(2, 2)  # 2 Zeilen, 2 Spalten = 4 Diagramme
```

Der Vorteil dieser Vorgehensweise: Sie haben direkte Kontrolle über Figure und Axes und können diese gezielt anpassen.

+++

### Beispiel 2: Figure mit einem Axes erstellen

```{code-cell} ipython3
# Erstellen einer Figure mit einem Axes
fig, ax = plt.subplots()

# Titel für die gesamte Figure
fig.suptitle('Meine erste Figure')

# Titel für das Diagramm (Axes)
ax.set_title('Meine erste Axes')

# Figure anzeigen
plt.show()
```

**Was ist passiert?**

- `plt.subplots()` erstellt eine Figure und ein Axes-Objekt
- `fig.suptitle()` setzt einen Titel für die gesamte Figure ("super title", oben zentriert)
- `ax.set_title()` setzt einen Titel für das Diagramm (Axes)
- Die beiden Titel erscheinen an unterschiedlichen Positionen
- Das Diagramm selbst ist noch leer – es wurden keine Daten geplottet

+++

### Beispiel 3: Figure mit mehreren Axes (Subplots)

```{code-cell} ipython3
# Erstellen einer Figure mit 4 Axes (2 Zeilen, 2 Spalten)
fig, ax = plt.subplots(2, 2)

# Figure anzeigen
plt.show()
```

**Was ist passiert?**

- `plt.subplots(2, 2)` erstellt eine Figure mit 4 Diagrammen in einem 2×2-Raster
- Die Variable `ax` enthält nun keine einzelne Axes mehr, sondern ein **Array von Axes-Objekten**
- Auf einzelne Diagramme können Sie über Indizierung zugreifen: `ax[0, 0]` (oben links), `ax[0, 1]` (oben rechts), etc.
- Alle vier Diagramme sind aktuell noch leer

+++

### Angeleitete Übung 2.1: Figure mit Titeln

**Aufgabe**: Erstellen Sie eine Figure mit 4 Subplots (2×2) und geben Sie jedem Subplot einen individuellen Titel.

**Hinweise**:
- Verwenden Sie `plt.subplots(2, 2)` zur Erstellung der Figure und Axes
- Die Variable `ax` ist dann ein 2D-Array: `ax[zeile, spalte]`
- Setzen Sie Titel mit `ax[zeile, spalte].set_title('Titel')`
- Beispiel: `ax[0, 0].set_title('Oben links')`
- Falls die Titel sich überlappen, verwenden Sie `fig.tight_layout()` vor `plt.show()`

```{code-cell} ipython3
# Ihr Code hier
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Figure mit 4 Subplots erstellen
fig, ax = plt.subplots(2, 2)

# Titel für jeden Subplot setzen
ax[0, 0].set_title('Diagramm 1: Oben links')
ax[0, 1].set_title('Diagramm 2: Oben rechts')
ax[1, 0].set_title('Diagramm 3: Unten links')
ax[1, 1].set_title('Diagramm 4: Unten rechts')

# Layout optimieren, damit sich Titel nicht überlappen
fig.tight_layout()

# Figure anzeigen
plt.show()
```

**Erklärung**:
- `ax[0, 0]` greift auf das Diagramm in der ersten Zeile, ersten Spalte zu (Python beginnt bei 0)
- `ax[0, 1]` ist die erste Zeile, zweite Spalte usw.
- `fig.tight_layout()` optimiert automatisch die Abstände zwischen den Subplots
- Diese Methode verhindert, dass sich Titel, Achsenbeschriftungen oder Diagramme überlappen
</details>

+++

## Liniendiagramme (Line Plots)

### Theoretische Grundlagen

Liniendiagramme gehören zu den grundlegendsten und häufigsten Visualisierungsformen. Sie sind besonders geeignet, um **kontinuierliche Daten** und **Verläufe über die Zeit** darzustellen. Typische Anwendungsfälle sind Temperaturverläufe, Aktienkurse, Messreihen oder Wachstumskurven.

Die Stärke von Liniendiagrammen liegt darin, Trends und Entwicklungen auf einen Blick erkennbar zu machen. Die durchgezogene Linie suggeriert Kontinuität zwischen den Datenpunkten und eignet sich daher nicht für kategoriale Daten.

**Syntax**:
```python
plt.plot(x_werte, y_werte)
```

**Semantik**:
- `x_werte`: Liste oder Array mit Werten für die x-Achse (z.B. Zeitpunkte, Tage)
- `y_werte`: Liste oder Array mit Werten für die y-Achse (z.B. Temperaturen, Preise)
- Beide Listen müssen die **gleiche Länge** haben
- Die Funktion verbindet die Punkte (x[0], y[0]), (x[1], y[1]), ... mit Linien
- Wird nur ein Parameter angegeben, wird er als y-Werte interpretiert (x = Indizes)

**Wichtig**: Achten Sie darauf, dass x- und y-Werte zusammenpassen. Der erste x-Wert gehört zum ersten y-Wert, der zweite x-Wert zum zweiten y-Wert usw.

+++

### Beispiel 4: Liniendiagramm mit x- und y-Werten

```{code-cell} ipython3
# Daten für die x- und y-Achse
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Liniendiagramm erstellen
plt.plot(x, y)

# Diagramm anzeigen
plt.show()
```

**Was ist passiert?**

- Die Liste `x` enthält die Werte für die horizontale Achse: [1, 2, 3, 4, 5]
- Die Liste `y` enthält die Werte für die vertikale Achse: [2, 3, 5, 7, 11]
- Matplotlib zeichnet Punkte an den Koordinaten (1, 2), (2, 3), (3, 5), (4, 7), (5, 11)
- Die Punkte werden mit einer durchgezogenen blauen Linie verbunden (Standardfarbe)
- Die y-Werte [2, 3, 5, 7, 11] sind übrigens Primzahlen – das Diagramm zeigt ihr Wachstum

+++

### Angeleitete Übung 3.1: Wochentemperaturen visualisieren

**Aufgabe**: Erstellen Sie ein Liniendiagramm, das die Temperaturen einer Woche darstellt.

**Hinweise**:
- Verwenden Sie für die x-Achse die Wochentage: [1, 2, 3, 4, 5, 6, 7] (oder Texte wie ['Mo', 'Di', ...])
- Wählen Sie realistische Temperaturwerte für die y-Achse, z.B. [18, 20, 22, 21, 19, 17, 16]
- Erstellen Sie das Diagramm mit `plt.plot(x, y)`
- Zeigen Sie es mit `plt.show()` an

```{code-cell} ipython3
# Ihr Code hier
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Daten für eine Woche
tage = [1, 2, 3, 4, 5, 6, 7]
temperaturen = [18, 20, 22, 21, 19, 17, 16]

# Liniendiagramm erstellen
plt.plot(tage, temperaturen)

# Diagramm anzeigen
plt.show()
```

**Erklärung**:
- Die Variable `tage` repräsentiert die Wochentage als Zahlen (1 = Montag, 7 = Sonntag)
- Die Variable `temperaturen` enthält die Temperaturwerte für jeden Tag
- Das Liniendiagramm macht den Temperaturverlauf sofort sichtbar: Anstieg zur Mitte der Woche, Abfall zum Wochenende
- Alternativ könnten Sie auch Texte für die x-Achse verwenden: `tage = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So']`
</details>

+++

### Angeleitete Übung 3.2: Mehrere Linien in einem Diagramm

**Aufgabe**: Erstellen Sie ein Liniendiagramm mit zwei Linien, das die Temperaturen zweier Städte vergleicht.

**Hinweise**:
- Verwenden Sie die gleichen x-Werte (Tage) für beide Städte
- Rufen Sie `plt.plot()` zweimal auf: einmal für Stadt 1, einmal für Stadt 2
- Beispiel:
  ```python
  plt.plot(x, y_stadt1)
  plt.plot(x, y_stadt2)
  ```
- Matplotlib verwendet automatisch unterschiedliche Farben für die Linien

```{code-cell} ipython3
# Ihr Code hier
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Gemeinsame x-Achse: Wochentage
tage = [1, 2, 3, 4, 5, 6, 7]

# Temperaturen für zwei Städte
temp_berlin = [18, 20, 22, 21, 19, 17, 16]
temp_muenchen = [15, 17, 19, 20, 18, 16, 14]

# Beide Linien plotten
plt.plot(tage, temp_berlin)
plt.plot(tage, temp_muenchen)

# Diagramm anzeigen
plt.show()
```

**Erklärung**:
- Beide `plt.plot()`-Aufrufe zeichnen in dasselbe Diagramm
- Matplotlib wählt automatisch unterschiedliche Farben (standardmäßig blau und orange)
- Sie können die beiden Temperaturverläufe direkt vergleichen
- Die Linien zu beschriften (Legende) lernen Sie im nächsten Abschnitt
</details>

+++

## Achsenbeschriftungen und Titel

### Theoretische Grundlagen

Ein Diagramm ohne Beschriftungen ist wie ein Text ohne Überschriften – schwer verständlich und nicht aussagekräftig. Beschriftungen sind essentiell, um einem Betrachter mitzuteilen, was visualisiert wird. Zu einer vollständigen Beschriftung gehören:

- **Titel**: Beschreibt, was das Diagramm zeigt
- **x-Achsen-Label**: Beschreibt, was auf der horizontalen Achse dargestellt ist (inkl. Einheit)
- **y-Achsen-Label**: Beschreibt, was auf der vertikalen Achse dargestellt ist (inkl. Einheit)
- **Legende** (optional): Erklärt verschiedene Linien oder Datenserien

**Wichtig**: Geben Sie immer Einheiten an, wenn Ihre Daten welche haben (z.B. "Temperatur in °C", "Zeit in Sekunden", "Preis in €").

**Syntax**:
```python
plt.title('Diagrammtitel')
plt.xlabel('Beschriftung x-Achse')
plt.ylabel('Beschriftung y-Achse')
```

**Semantik**:
- `plt.title()`: Setzt den Titel oberhalb des Diagramms
- `plt.xlabel()`: Beschriftet die x-Achse (horizontal, unterhalb des Diagramms)
- `plt.ylabel()`: Beschriftet die y-Achse (vertikal, links vom Diagramm)
- Alle drei Funktionen erwarten einen String als Parameter
- Die Beschriftungen werden dem aktuellen Diagramm hinzugefügt

+++

### Beispiel 5: Vollständig beschriftetes Liniendiagramm

```{code-cell} ipython3
# Daten für eine Woche
tage = [1, 2, 3, 4, 5, 6, 7]
temperaturen = [18, 20, 22, 21, 19, 17, 16]

# Liniendiagramm erstellen
plt.plot(tage, temperaturen)

# Beschriftungen hinzufügen
plt.title('Temperaturverlauf einer Woche')
plt.xlabel('Tag der Woche')
plt.ylabel('Temperatur in °C')

# Diagramm anzeigen
plt.show()
```

**Was ist passiert?**

- Das Diagramm hat nun einen aussagekräftigen Titel: "Temperaturverlauf einer Woche"
- Die x-Achse ist beschriftet: "Tag der Woche" – der Betrachter weiß, dass die Zahlen Tage repräsentieren
- Die y-Achse ist beschriftet: "Temperatur in °C" – die Einheit ist klar erkennbar
- Das Diagramm ist nun selbsterklärend und könnte in einem Bericht verwendet werden

+++

### Angeleitete Übung 4.1: Beschriftetes Diagramm erstellen

**Aufgabe**: Erstellen Sie ein vollständig beschriftetes Liniendiagramm, das das Wachstum einer Pflanze über 6 Wochen zeigt.

**Hinweise**:
- x-Werte: Wochen [1, 2, 3, 4, 5, 6]
- y-Werte: Höhe der Pflanze in cm, z.B. [5, 8, 12, 18, 25, 32] (zeigt Wachstum)
- Setzen Sie einen passenden Titel (z.B. "Pflanzenwachstum")
- Beschriften Sie die x-Achse mit "Woche"
- Beschriften Sie die y-Achse mit "Höhe in cm"

```{code-cell} ipython3
# Ihr Code hier
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Daten für 6 Wochen
wochen = [1, 2, 3, 4, 5, 6]
hoehe = [5, 8, 12, 18, 25, 32]

# Liniendiagramm erstellen
plt.plot(wochen, hoehe)

# Beschriftungen hinzufügen
plt.title('Pflanzenwachstum über 6 Wochen')
plt.xlabel('Woche')
plt.ylabel('Höhe in cm')

# Diagramm anzeigen
plt.show()
```

**Erklärung**:
- Das Diagramm zeigt deutlich, dass die Pflanze nicht linear wächst, sondern das Wachstum beschleunigt
- Die Beschriftungen machen sofort klar, was dargestellt wird
- Die Einheit "cm" in der y-Achsen-Beschriftung ist wichtig für die Interpretation
- Ein solches Diagramm könnte in einem Biologiebericht verwendet werden
</details>

+++

## Balkendiagramme (Bar Charts)

### Theoretische Grundlagen

Während Liniendiagramme für kontinuierliche Daten und Zeitverläufe geeignet sind, dienen Balkendiagramme zur Darstellung **kategorialer Daten**. Sie eignen sich hervorragend, um Mengen, Häufigkeiten oder Vergleiche zwischen verschiedenen Kategorien zu visualisieren.

Typische Anwendungsfälle für Balkendiagramme:
- Verkaufszahlen verschiedener Produkte
- Umfrageergebnisse (z.B. Zustimmung zu verschiedenen Aussagen)
- Vergleich von Werten zwischen verschiedenen Gruppen oder Zeitpunkten
- Häufigkeiten von Kategorien

Im Gegensatz zum Liniendiagramm suggeriert das Balkendiagramm **keine Kontinuität** zwischen den Kategorien. Jeder Balken steht für sich und repräsentiert eine diskrete Kategorie.

**Syntax**:
```python
plt.bar(kategorien, werte)
```

**Semantik**:
- `kategorien`: Liste mit Kategorie-Namen (Strings) oder Zahlen für die x-Achse
- `werte`: Liste mit numerischen Werten für die Höhe der Balken (y-Achse)
- Beide Listen müssen die gleiche Länge haben
- Jeder Wert in `werte` bestimmt die Höhe des entsprechenden Balkens
- Die Balken werden vertikal dargestellt (für horizontale Balken gibt es `plt.barh()`)

+++

### Beispiel 6: Einfaches Balkendiagramm

```{code-cell} ipython3
# Kategorien und zugehörige Werte
kategorien = ['A', 'B', 'C', 'D', 'E']
werte = [3, 7, 2, 5, 8]

# Balkendiagramm erstellen
plt.bar(kategorien, werte)

# Diagramm anzeigen
plt.show()
```

**Was ist passiert?**

- Matplotlib erstellt für jede Kategorie (A, B, C, D, E) einen vertikalen Balken
- Die Höhe jedes Balkens entspricht dem zugehörigen Wert aus der Liste `werte`
- Kategorie B hat den höchsten Wert (7), Kategorie C den niedrigsten (2)
- Die Balken stehen nebeneinander, getrennt durch kleine Abstände
- Die Standardfarbe ist blau (kann angepasst werden)

+++

### Beispiel 7: Beschriftetes Balkendiagramm mit realistischen Daten

```{code-cell} ipython3
# Verkaufszahlen verschiedener Produkte
produkte = ['Laptop', 'Tablet', 'Smartphone', 'Monitor', 'Tastatur']
verkaufte_stueckzahl = [45, 78, 132, 56, 89]

# Balkendiagramm erstellen
plt.bar(produkte, verkaufte_stueckzahl)

# Beschriftungen hinzufügen
plt.title('Verkaufszahlen Elektronikprodukte im Januar')
plt.xlabel('Produkt')
plt.ylabel('Verkaufte Stückzahl')

# Diagramm anzeigen
plt.show()
```

**Was ist passiert?**

- Das Diagramm vergleicht Verkaufszahlen von fünf Produktkategorien
- Auf der x-Achse stehen die Produktnamen (Text-Kategorien)
- Die y-Achse zeigt die verkauften Stückzahlen
- Auf einen Blick erkennbar: Smartphones wurden am häufigsten verkauft (132 Stück)
- Das Diagramm ist vollständig beschriftet und selbsterklärend
- Solche Visualisierungen sind typisch für Geschäftsberichte und Präsentationen

+++

### Angeleitete Übung 5.1: Umfrageergebnisse visualisieren

**Aufgabe**: Eine Umfrage hat gefragt, welche Programmiersprache Studierende bevorzugen. Erstellen Sie ein Balkendiagramm mit den Ergebnissen.

**Hinweise**:
- Kategorien: ['Python', 'Java', 'JavaScript', 'C++', 'Ruby']
- Anzahl Stimmen: [45, 23, 31, 12, 8] (Beispielwerte)
- Erstellen Sie ein Balkendiagramm mit `plt.bar()`
- Fügen Sie einen Titel hinzu: "Beliebteste Programmiersprachen (Umfrage)"
- Beschriften Sie die Achsen passend

```{code-cell} ipython3
# Ihr Code hier
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Umfragedaten
sprachen = ['Python', 'Java', 'JavaScript', 'C++', 'Ruby']
stimmen = [45, 23, 31, 12, 8]

# Balkendiagramm erstellen
plt.bar(sprachen, stimmen)

# Beschriftungen hinzufügen
plt.title('Beliebteste Programmiersprachen (Umfrage)')
plt.xlabel('Programmiersprache')
plt.ylabel('Anzahl Stimmen')

# Diagramm anzeigen
plt.show()
```

**Erklärung**:
- Das Balkendiagramm zeigt deutlich, dass Python die beliebteste Sprache ist (45 Stimmen)
- JavaScript folgt auf Platz 2, Ruby ist am wenigsten beliebt
- Die diskrete Darstellung als Balken ist hier angemessen – es gibt keine "Übergänge" zwischen den Sprachen
- Ein Liniendiagramm wäre hier ungeeignet, da es Kontinuität suggerieren würde
</details>

+++

### Angeleitete Übung 5.2: Monatliche Ausgaben

**Aufgabe**: Erstellen Sie ein Balkendiagramm, das Ihre monatlichen Ausgaben in verschiedenen Kategorien darstellt.

**Hinweise**:
- Kategorien: ['Miete', 'Lebensmittel', 'Transport', 'Freizeit', 'Sonstiges']
- Wählen Sie realistische Beträge in Euro, z.B. [800, 300, 100, 150, 200]
- Beschriften Sie die y-Achse mit "Ausgaben in €"
- Setzen Sie einen passenden Titel

```{code-cell} ipython3
# Ihr Code hier
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Ausgabenkategorien
kategorien = ['Miete', 'Lebensmittel', 'Transport', 'Freizeit', 'Sonstiges']
ausgaben = [800, 300, 100, 150, 200]

# Balkendiagramm erstellen
plt.bar(kategorien, ausgaben)

# Beschriftungen hinzufügen
plt.title('Monatliche Ausgaben nach Kategorie')
plt.xlabel('Kategorie')
plt.ylabel('Ausgaben in €')

# Diagramm anzeigen
plt.show()
```

**Erklärung**:
- Das Diagramm macht sofort sichtbar, wo das meiste Geld ausgegeben wird
- Die Miete ist mit Abstand der größte Posten (800 €)
- Solche Visualisierungen sind nützlich für Budgetplanung und Finanzübersicht
- Die Einheit "€" in der y-Achsen-Beschriftung ist wichtig für die Interpretation
</details>

+++

## Abschlussübungen

Die folgenden Aufgaben testen Ihr Verständnis der in diesem Notebook erlernten Konzepte. Bearbeiten Sie die Aufgaben selbstständig und vergleichen Sie Ihre Lösung anschließend mit den Musterlösungen am Ende des Notebooks.

+++

### Teil 1: Grundlegende Anwendung

**Kompetenzstufe**: Anwenden

Diese Aufgaben testen die direkte Anwendung der erlernten Konzepte.

+++

**Aufgabe 1**: Erstellen Sie ein vollständig beschriftetes Liniendiagramm, das die Anzahl der Studierenden in einem Informatik-Kurs über 5 Semester hinweg zeigt. Verwenden Sie folgende Daten:
- Semester: [1, 2, 3, 4, 5]
- Studierende: [120, 135, 148, 142, 156]

Das Diagramm soll einen Titel sowie Achsenbeschriftungen haben.

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 1
```

**Aufgabe 2**: Ein Online-Shop hat die Verkäufe verschiedener Produktkategorien erfasst. Erstellen Sie ein beschriftetes Balkendiagramm mit folgenden Daten:
- Kategorien: ['Bücher', 'Elektronik', 'Kleidung', 'Spielzeug', 'Sport']
- Verkäufe: [234, 567, 389, 156, 298]

Fügen Sie einen aussagekräftigen Titel und Achsenbeschriftungen hinzu.

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 2
```

### Teil 2: Transfer und Problemlösung

**Kompetenzstufe**: Analysieren & Erschaffen

Diese Aufgaben erfordern die Kombination mehrerer Konzepte und eigenständiges Problemlösen.

+++

**Aufgabe 3**: Sie haben Daten über die durchschnittlichen Tageshöchsttemperaturen zweier Städte für eine Woche gesammelt:
- Stadt A: [22, 24, 26, 25, 23, 21, 20]
- Stadt B: [18, 19, 21, 22, 21, 19, 18]

Erstellen Sie ein Liniendiagramm, das beide Temperaturverläufe vergleicht. Das Diagramm soll:
- Beide Linien in einem Diagramm zeigen
- Einen aussagekräftigen Titel haben
- Die Achsen beschriften
- Die x-Achse soll die Wochentage repräsentieren (verwenden Sie Zahlen 1-7 oder Abkürzungen)

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 3
```

**Aufgabe 4**: Erstellen Sie eine Figure mit 2 Subplots (nebeneinander, also 1 Zeile, 2 Spalten):
- **Linker Subplot**: Liniendiagramm mit Umsatzentwicklung über 6 Monate: [10000, 12000, 11500, 13000, 14500, 15000]
- **Rechter Subplot**: Balkendiagramm mit Mitarbeiterzahlen in 4 Abteilungen:
  - Abteilungen: ['Entwicklung', 'Vertrieb', 'Marketing', 'Support']
  - Mitarbeiter: [25, 18, 12, 15]

Beide Subplots sollen Titel und Achsenbeschriftungen haben. Verwenden Sie `fig.tight_layout()`, um Überlappungen zu vermeiden.

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 4
```

## Zusammenfassung

In diesem Notebook haben Sie folgende Konzepte kennengelernt:

| Konzept | Syntax | Anwendungsfall |
|---------|--------|----------------|
| Matplotlib importieren | `import matplotlib.pyplot as plt` | Bibliothek für Visualisierungen laden |
| Liniendiagramm | `plt.plot(x, y)` | Kontinuierliche Daten, Zeitverläufe |
| Balkendiagramm | `plt.bar(kategorien, werte)` | Kategoriale Daten, Vergleiche |
| Diagramm anzeigen | `plt.show()` | Fertige Visualisierung darstellen |
| Titel setzen | `plt.title('Text')` | Diagramm benennen |
| x-Achse beschriften | `plt.xlabel('Text')` | x-Achse erklären |
| y-Achse beschriften | `plt.ylabel('Text')` | y-Achse erklären (inkl. Einheit) |
| Figure und Axes | `fig, ax = plt.subplots()` | Explizite Kontrolle über Diagrammstruktur |
| Subplots erstellen | `fig, ax = plt.subplots(zeilen, spalten)` | Mehrere Diagramme in einer Figure |
| Layout optimieren | `fig.tight_layout()` | Überlappungen vermeiden |

**Zentrale Erkenntnisse**:
- **Datenvisualisierung macht Muster erkennbar**: Grafiken zeigen auf einen Blick, was in Zahlenkolonnen verborgen bleibt
- **Matplotlib ist die Standardbibliothek** für Visualisierungen in Python und wird mit dem Alias `plt` importiert
- **Liniendiagramme** eignen sich für kontinuierliche Daten und Zeitverläufe, **Balkendiagramme** für kategoriale Daten
- **Beschriftungen sind essentiell**: Titel, Achsenbeschriftungen und Einheiten machen Diagramme selbsterklärend
- **Das hierarchische Modell** (Figure → Axes → Plots) ermöglicht flexible und komplexe Visualisierungen

**Nächste Schritte**: Im folgenden Notebook (19 - Matplotlib Vertiefung) werden Sie weitere Diagrammtypen (Histogramme, Scatter Plots), erweiterte Anpassungsmöglichkeiten (Farben, Stile, Marker) und komplexere Layouts kennenlernen.

+++

## Musterlösungen

+++

<details>
<summary>Lösung zu Aufgabe 1</summary>

```python
# Daten für Studierendenzahlen
semester = [1, 2, 3, 4, 5]
studierende = [120, 135, 148, 142, 156]

# Liniendiagramm erstellen
plt.plot(semester, studierende)

# Beschriftungen hinzufügen
plt.title('Entwicklung der Studierendenzahlen im Informatik-Kurs')
plt.xlabel('Semester')
plt.ylabel('Anzahl Studierende')

# Diagramm anzeigen
plt.show()
```

**Erklärung**:
- Das Liniendiagramm zeigt einen insgesamt steigenden Trend der Studierendenzahlen
- Im 4. Semester gab es einen leichten Rückgang (von 148 auf 142)
- Die Beschriftungen machen sofort klar, was dargestellt wird
- Ein solches Diagramm könnte in einem Universitätsbericht verwendet werden

**Häufige Fehler**:
- Vergessen von `plt.show()` – das Diagramm wird dann nicht angezeigt
- Fehlende oder unvollständige Achsenbeschriftungen (Einheiten vergessen)
- x- und y-Listen haben unterschiedliche Längen → Fehlermeldung
</details>

+++

<details>
<summary>Lösung zu Aufgabe 2</summary>

```python
# Verkaufsdaten
kategorien = ['Bücher', 'Elektronik', 'Kleidung', 'Spielzeug', 'Sport']
verkaeufe = [234, 567, 389, 156, 298]

# Balkendiagramm erstellen
plt.bar(kategorien, verkaeufe)

# Beschriftungen hinzufügen
plt.title('Verkäufe nach Produktkategorie')
plt.xlabel('Produktkategorie')
plt.ylabel('Anzahl Verkäufe')

# Diagramm anzeigen
plt.show()
```

**Erklärung**:
- Das Balkendiagramm zeigt deutlich, dass Elektronik am besten verkauft wurde (567 Einheiten)
- Spielzeug hatte die wenigsten Verkäufe (156 Einheiten)
- Die kategoriale Darstellung ist hier angemessen – jede Produktkategorie steht für sich
- Solche Visualisierungen sind typisch für Verkaufsberichte

**Häufige Fehler**:
- Verwendung von `plt.plot()` statt `plt.bar()` – würde eine Linie erzeugen, was hier unpassend ist
- Umlaute in Strings (ü, ö, ä) können in manchen Umgebungen Probleme verursachen – verwenden Sie ue, oe, ae
</details>

+++

<details>
<summary>Lösung zu Aufgabe 3</summary>

```python
# Gemeinsame x-Achse: Wochentage
tage = [1, 2, 3, 4, 5, 6, 7]

# Temperaturdaten für beide Städte
temp_stadt_a = [22, 24, 26, 25, 23, 21, 20]
temp_stadt_b = [18, 19, 21, 22, 21, 19, 18]

# Beide Linien plotten
plt.plot(tage, temp_stadt_a)
plt.plot(tage, temp_stadt_b)

# Beschriftungen hinzufügen
plt.title('Temperaturvergleich zweier Städte über eine Woche')
plt.xlabel('Tag der Woche')
plt.ylabel('Temperatur in °C')

# Diagramm anzeigen
plt.show()
```

**Erklärung**:
- Beide `plt.plot()`-Aufrufe zeichnen in dasselbe Diagramm
- Matplotlib wählt automatisch unterschiedliche Farben (blau für die erste, orange für die zweite Linie)
- Der Vergleich zeigt, dass Stadt A durchgehend wärmer ist als Stadt B
- Beide Städte zeigen einen ähnlichen Verlauf: Maximum zur Wochenmitte, Abkühlung zum Wochenende
- In Notebook 19 lernen Sie, wie Sie Legenden hinzufügen, um die Linien zu beschriften

**Alternative Ansätze**:
- Sie könnten auch Text-Labels für die Tage verwenden: `tage = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So']`
- Dies macht die x-Achse noch lesbarer, funktioniert mit `plt.plot()` genauso
</details>

+++

<details>
<summary>Lösung zu Aufgabe 4</summary>

```python
# Figure mit 2 Subplots erstellen (1 Zeile, 2 Spalten)
fig, ax = plt.subplots(1, 2)

# Linker Subplot: Umsatzentwicklung (Liniendiagramm)
monate = [1, 2, 3, 4, 5, 6]
umsatz = [10000, 12000, 11500, 13000, 14500, 15000]

ax[0].plot(monate, umsatz)
ax[0].set_title('Umsatzentwicklung')
ax[0].set_xlabel('Monat')
ax[0].set_ylabel('Umsatz in €')

# Rechter Subplot: Mitarbeiterzahlen (Balkendiagramm)
abteilungen = ['Entwicklung', 'Vertrieb', 'Marketing', 'Support']
mitarbeiter = [25, 18, 12, 15]

ax[1].bar(abteilungen, mitarbeiter)
ax[1].set_title('Mitarbeiter nach Abteilung')
ax[1].set_xlabel('Abteilung')
ax[1].set_ylabel('Anzahl Mitarbeiter')

# Layout optimieren
fig.tight_layout()

# Figure anzeigen
plt.show()
```

**Erklärung**:
- `plt.subplots(1, 2)` erstellt eine Figure mit 2 Subplots nebeneinander
- `ax` ist nun ein eindimensionales Array: `ax[0]` ist links, `ax[1]` ist rechts
- Für jeden Subplot verwenden Sie die Methoden des jeweiligen Axes-Objekts (z.B. `ax[0].plot()`, `ax[1].bar()`)
- Wichtig: Bei Axes-Objekten heißen die Funktionen `set_title()`, `set_xlabel()`, `set_ylabel()` (mit "set_")
- `fig.tight_layout()` verhindert, dass sich Beschriftungen überlappen
- Diese Technik ermöglicht es, mehrere Visualisierungen übersichtlich in einer Abbildung zu kombinieren

**Alternative Ansätze**:
- Sie könnten die Subplots auch untereinander anordnen: `plt.subplots(2, 1)` (2 Zeilen, 1 Spalte)
- Für mehr als 2 Subplots wären größere Raster möglich: `plt.subplots(2, 2)` für 4 Diagramme
</details>
