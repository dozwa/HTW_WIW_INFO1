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

# 19 - Matplotlib Vertiefung: Erweiterte Visualisierungstechniken

+++

## Lernziele

Nach Abschluss dieses Notebooks können Sie:
- Achsenbereiche mit `xlim()` und `ylim()` gezielt anpassen
- Legenden mit `legend()` zu Diagrammen hinzufügen, um mehrere Datenreihen zu unterscheiden
- Histogramme mit `hist()` erstellen, um Verteilungen von Daten zu visualisieren
- Scatter Plots mit `scatter()` erstellen, um Beziehungen zwischen Variablen darzustellen
- Diagramme durch Farben, Linienstile und Marker anpassen
- Mehrere Diagramme mit `subplots()` in einer Figure arrangieren

**Kompetenzstufen**: Verstehen, Anwenden, Analysieren

+++

## Voraussetzungen

Für dieses Notebook sollten Sie folgende Konzepte beherrschen:
- Matplotlib importieren und pyplot-Schnittstelle verwenden (Notebook 18)
- Liniendiagramme mit `plt.plot()` erstellen (Notebook 18)
- Balkendiagramme mit `plt.bar()` erstellen (Notebook 18)
- Achsenbeschriftungen und Titel hinzufügen (Notebook 18)
- Listen und Schleifen (Notebooks 06, 10)

Falls Sie diese Konzepte noch nicht sicher beherrschen, wiederholen Sie bitte die entsprechenden Notebooks.

+++

## Einführung: Von einfachen zu aussagekräftigen Visualisierungen

Im vorherigen Notebook haben Sie die Grundlagen der Datenvisualisierung mit Matplotlib kennengelernt. Sie können bereits einfache Linien- und Balkendiagramme erstellen und diese mit Titeln sowie Achsenbeschriftungen versehen. Diese Fähigkeiten bilden das Fundament für jede Datenvisualisierung.

In der Praxis reichen jedoch einfache Standarddiagramme oft nicht aus. Sie möchten beispielsweise mehrere Datenreihen in einem Diagramm vergleichen und diese eindeutig kennzeichnen. Oder Sie müssen den Fokus auf einen bestimmten Wertebereich legen, um Details sichtbar zu machen. Manchmal ist es auch notwendig, die Verteilung von Daten oder Zusammenhänge zwischen Variablen zu untersuchen.

Dieses Notebook baut systematisch auf Ihrem Vorwissen auf und erweitert Ihre Fähigkeiten um wichtige Visualisierungstechniken. Sie lernen, wie Sie Diagramme präzise an Ihre Analysebedürfnisse anpassen können.

+++

## Erweiterte Achsenanpassung und Legenden

### Theoretische Grundlagen: Achsenbereiche anpassen

Standardmäßig wählt Matplotlib die Achsenbereiche automatisch so, dass alle Datenpunkte sichtbar sind. Diese Automatik ist praktisch, führt aber manchmal zu unerwünschten Ergebnissen. Möchten Sie beispielsweise den Fokus auf einen bestimmten Wertebereich legen oder mehrere Diagramme mit identischen Achsen vergleichen, müssen Sie die Achsenbereiche manuell festlegen.

Matplotlib bietet hierfür die Funktionen `xlim()` und `ylim()`. Mit diesen können Sie die Minimal- und Maximalwerte der x- und y-Achse explizit definieren. Dies ist besonders nützlich bei der Analyse von Zeitreihen, wo Sie bestimmte Perioden hervorheben möchten, oder bei der Untersuchung von Details in großen Datensätzen.

**Syntax**:
```python
plt.xlim(minimum, maximum)
plt.ylim(minimum, maximum)
```

**Semantik**:
- `xlim()`: Setzt den Wertebereich der x-Achse (horizontal)
- `ylim()`: Setzt den Wertebereich der y-Achse (vertikal)
- `minimum`: Kleinster angezeigter Wert auf der Achse
- `maximum`: Größter angezeigter Wert auf der Achse
- Datenpunkte außerhalb des Bereichs werden nicht angezeigt
- Sie können auch nur eine der beiden Funktionen verwenden

+++

### Beispiel 1: Achsenbereiche einschränken

Betrachten Sie folgendes Szenario: Sie haben Verkaufsdaten für ein Jahr, möchten aber nur das erste Quartal analysieren.

```{code-cell}
import matplotlib.pyplot as plt

# Monatliche Verkaufszahlen für ein Jahr
monate = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
verkaeufe = [120, 135, 142, 156, 148, 162, 178, 185, 190, 195, 210, 225]

# Liniendiagramm erstellen
plt.plot(monate, verkaeufe)
plt.title('Verkaufszahlen im ersten Quartal')
plt.xlabel('Monat')
plt.ylabel('Verkäufe')

# Nur Monate 1-3 anzeigen (erstes Quartal)
plt.xlim(1, 3)

plt.show()
```

**Was ist passiert?**

- Obwohl die Daten für alle 12 Monate vorliegen, zeigt das Diagramm nur die Monate 1 bis 3
- Die Funktion `plt.xlim(1, 3)` begrenzt die x-Achse auf diesen Bereich
- Die y-Achse passt sich automatisch an die sichtbaren Datenpunkte an
- Diese Technik ermöglicht es, bestimmte Zeiträume detailliert zu untersuchen
- Der Rest der Daten wird nicht gelöscht, sondern nur ausgeblendet

+++

### Angeleitete Übung 1.1: Ausschnitt vergrößern

**Aufgabe**: Sie haben Temperaturmessungen für 24 Stunden. Erstellen Sie ein Diagramm, das nur die Nachtstunden (22-6 Uhr) zeigt.

**Hinweise**:
- Verwenden Sie folgende Daten:
  - Stunden: Liste von 0 bis 23 (können Sie mit `list(range(24))` erstellen)
  - Temperaturen: [5, 4, 3, 3, 2, 2, 3, 5, 8, 12, 15, 18, 20, 22, 23, 22, 20, 18, 15, 12, 10, 8, 7, 6]
- Erstellen Sie das Diagramm mit `plt.plot()`
- Verwenden Sie `plt.xlim(22, 6)` – **Achtung**: Dies funktioniert nicht wie erwartet!
- Lösung: Zeigen Sie stattdessen zwei Bereiche: 0-6 Uhr ODER verwenden Sie `plt.xlim(0, 6)` für nur die Morgenstunden

```{code-cell}
# Ihr Code hier
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Daten für 24 Stunden
stunden = list(range(24))
temperaturen = [5, 4, 3, 3, 2, 2, 3, 5, 8, 12, 15, 18, 20, 22, 23, 22, 20, 18, 15, 12, 10, 8, 7, 6]

# Liniendiagramm erstellen
plt.plot(stunden, temperaturen)
plt.title('Temperaturen in den frühen Morgenstunden')
plt.xlabel('Uhrzeit (Stunden)')
plt.ylabel('Temperatur in °C')

# Nur 0-6 Uhr anzeigen (Nachtstunden bis Morgen)
plt.xlim(0, 6)

plt.show()
```

**Erklärung**:
- `list(range(24))` erstellt eine Liste [0, 1, 2, ..., 23] für die 24 Stunden
- Die Funktion `plt.xlim(0, 6)` zeigt nur die Stunden 0 bis 6
- In diesem Zeitraum fallen die Temperaturen bis zum Minimum (2°C um 4-5 Uhr) und steigen dann wieder
- Für eine vollständige Nachtdarstellung (22-6 Uhr) bräuchten Sie zwei separate Diagramme oder eine komplexere Datenaufbereitung
</details>

+++

### Theoretische Grundlagen: Legenden

Wenn Sie mehrere Datenreihen in einem Diagramm darstellen, müssen Betrachter erkennen können, welche Linie oder welcher Balken für welche Datenreihe steht. Hier kommen Legenden ins Spiel. Eine Legende ist eine Beschriftung, die die verschiedenen grafischen Elemente eines Diagramms erklärt.

In Matplotlib fügen Sie Legenden in zwei Schritten hinzu: Zunächst geben Sie beim Erstellen eines Plots ein Label an, dann rufen Sie `plt.legend()` auf, um die Legende anzuzeigen. Matplotlib platziert die Legende automatisch an einer geeigneten Position, um die Daten nicht zu verdecken.

**Syntax**:
```python
plt.plot(x, y, label='Beschreibung')
plt.legend()
```

**Semantik**:
- `label='Text'`: Parameter beim Plot-Befehl, definiert den Text für diese Datenreihe
- `plt.legend()`: Zeigt die Legende mit allen definierten Labels an
- Matplotlib wählt automatisch Position, Rahmen und Hintergrund
- Sie können die Position mit `loc`-Parameter steuern (z.B. `loc='upper left'`)
- Ohne Labels zeigt `legend()` keine Einträge an

+++

### Beispiel 2: Mehrere Linien mit Legende

```{code-cell}
# Vergleich zweier Produkte über 6 Monate
monate = [1, 2, 3, 4, 5, 6]
produkt_a = [100, 120, 140, 135, 155, 170]
produkt_b = [80, 85, 95, 110, 125, 140]

# Beide Linien mit Labels plotten
plt.plot(monate, produkt_a, label='Produkt A')
plt.plot(monate, produkt_b, label='Produkt B')

# Beschriftungen
plt.title('Verkaufsvergleich zweier Produkte')
plt.xlabel('Monat')
plt.ylabel('Verkaufte Einheiten')

# Legende anzeigen
plt.legend()

plt.show()
```

**Was ist passiert?**

- Beim ersten `plt.plot()`-Aufruf wird `label='Produkt A'` angegeben
- Beim zweiten `plt.plot()`-Aufruf wird `label='Produkt B'` angegeben
- Der Aufruf von `plt.legend()` erstellt eine Legende mit beiden Labels
- Matplotlib wählt automatisch unterschiedliche Farben (blau und orange)
- Die Legende zeigt kleine Linienmuster in den entsprechenden Farben
- Ohne die Labels würde `plt.legend()` keine Einträge anzeigen

+++

### Angeleitete Übung 1.2: Temperaturvergleich mit Legende

**Aufgabe**: Erstellen Sie ein Diagramm, das die durchschnittlichen Monatstemperaturen zweier Jahre vergleicht und eine Legende enthält.

**Hinweise**:
- Monate: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
- Jahr 2023: [2, 4, 8, 12, 16, 20, 23, 22, 18, 13, 7, 3]
- Jahr 2024: [3, 5, 9, 13, 17, 21, 24, 23, 19, 14, 8, 4]
- Verwenden Sie `label='Jahr 2023'` und `label='Jahr 2024'` in den Plot-Befehlen
- Rufen Sie `plt.legend()` auf, um die Legende anzuzeigen

```{code-cell}
# Ihr Code hier
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Daten für zwei Jahre
monate = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
temp_2023 = [2, 4, 8, 12, 16, 20, 23, 22, 18, 13, 7, 3]
temp_2024 = [3, 5, 9, 13, 17, 21, 24, 23, 19, 14, 8, 4]

# Beide Linien mit Labels plotten
plt.plot(monate, temp_2023, label='Jahr 2023')
plt.plot(monate, temp_2024, label='Jahr 2024')

# Beschriftungen
plt.title('Durchschnittstemperaturen im Jahresvergleich')
plt.xlabel('Monat')
plt.ylabel('Temperatur in °C')

# Legende anzeigen
plt.legend()

plt.show()
```

**Erklärung**:
- Die Legende macht sofort klar, welche Linie zu welchem Jahr gehört
- Der Vergleich zeigt, dass 2024 durchgehend etwas wärmer war als 2023
- Beide Jahre zeigen den typischen Temperaturverlauf mit Maximum im Sommer
- Die automatische Positionierung der Legende vermeidet Überlappungen mit den Linien
</details>

+++

## Histogramme: Verteilungen visualisieren

### Theoretische Grundlagen

Histogramme sind ein fundamentales Werkzeug zur Visualisierung der Verteilung von Daten. Im Gegensatz zu Linien- oder Balkendiagrammen, die einzelne Datenpunkte oder Kategorien darstellen, zeigen Histogramme, wie häufig bestimmte Wertebereiche in einem Datensatz vorkommen.

Die zentrale Idee: Der gesamte Wertebereich wird in gleich große Intervalle (genannt "Bins") unterteilt. Für jedes Intervall zählt das Histogramm, wie viele Datenpunkte hineinfallen. Die Höhe jedes Balkens repräsentiert diese Anzahl. So erkennen Sie auf einen Blick, ob Daten normalverteilt sind, mehrere Häufungen aufweisen oder asymmetrisch verteilt sind.

Typische Anwendungsfälle:
- Verteilung von Prüfungsnoten in einer Klasse
- Altersverteilung in einer Population
- Einkommensverteilung in einer Gesellschaft
- Messfehler in wissenschaftlichen Experimenten

+++

**Syntax**:
```python
plt.hist(daten, bins=anzahl)
```

**Semantik**:
- `daten`: Liste oder Array mit numerischen Werten
- `bins`: Anzahl der Intervalle (Balken), in die die Daten aufgeteilt werden
- Je mehr Bins, desto feiner die Auflösung, aber auch mehr Rauschen
- Je weniger Bins, desto gröber die Darstellung, aber klarere Muster
- Standardwert: 10 Bins
- Zusätzliche Parameter: `color`, `alpha` (Transparenz), `edgecolor` (Rahmenfarbe)

+++

### Beispiel 3: Verteilung von Prüfungsnoten

Betrachten Sie die Noten von 50 Studierenden in einer Prüfung (Skala 1-6).

```{code-cell}
# 50 Prüfungsnoten (Skala 1.0 bis 5.0)
noten = [2.3, 1.7, 2.0, 3.3, 2.7, 1.3, 2.0, 2.3, 3.0, 2.7,
         1.7, 2.3, 3.7, 2.0, 2.3, 1.7, 3.0, 2.7, 2.0, 3.3,
         2.3, 2.7, 1.3, 3.0, 2.3, 3.7, 2.0, 2.7, 1.7, 3.0,
         2.3, 3.3, 2.0, 2.7, 1.7, 3.0, 4.0, 2.3, 2.7, 3.3,
         2.0, 1.7, 2.3, 3.0, 2.7, 1.3, 2.0, 3.3, 2.7, 2.3]

# Histogramm erstellen
plt.hist(noten, bins=10, color='skyblue', edgecolor='black')
plt.title('Verteilung der Prüfungsnoten')
plt.xlabel('Note')
plt.ylabel('Anzahl Studierende')

plt.show()
```

**Was ist passiert?**

- Die Liste `noten` enthält 50 Notenwerte zwischen 1.3 und 4.0
- `bins=10` teilt den Wertebereich in 10 gleichgroße Intervalle
- Die Höhe jedes Balkens zeigt, wie viele Noten in das Intervall fallen
- Die meisten Noten liegen im Bereich 2.0-2.7 (häufigste Balken)
- `color='skyblue'` färbt die Balken hellblau
- `edgecolor='black'` fügt schwarze Umrandungen hinzu für bessere Lesbarkeit

+++

### Angeleitete Übung 2.1: Altersverteilung

**Aufgabe**: Sie haben die Altersangaben von 30 Teilnehmenden eines Workshops. Erstellen Sie ein Histogramm, um die Altersverteilung zu visualisieren.

**Hinweise**:
- Alter: [22, 25, 23, 28, 31, 24, 26, 29, 27, 25, 30, 24, 26, 28, 32, 23, 25, 27, 29, 31, 24, 26, 28, 25, 27, 30, 33, 24, 26, 28]
- Verwenden Sie 8 Bins
- Wählen Sie eine passende Farbe (z.B. 'lightgreen')
- Fügen Sie Titel und Achsenbeschriftungen hinzu

```{code-cell}
# Ihr Code hier
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Altersangaben der Teilnehmenden
alter = [22, 25, 23, 28, 31, 24, 26, 29, 27, 25, 30, 24, 26, 28, 32, 23, 25, 27, 29, 31, 24, 26, 28, 25, 27, 30, 33, 24, 26, 28]

# Histogramm erstellen
plt.hist(alter, bins=8, color='lightgreen', edgecolor='black')
plt.title('Altersverteilung der Workshop-Teilnehmenden')
plt.xlabel('Alter in Jahren')
plt.ylabel('Anzahl Personen')

plt.show()
```

**Erklärung**:
- Das Histogramm zeigt, dass die meisten Teilnehmenden zwischen 24 und 28 Jahre alt sind
- Die Verteilung ist relativ gleichmäßig mit einem leichten Höhepunkt in der Mitte
- Mit 8 Bins erhalten Sie eine gute Balance zwischen Detail und Übersichtlichkeit
- Die schwarzen Rahmen (`edgecolor`) machen die einzelnen Balken besser unterscheidbar
</details>

+++

### Angeleitete Übung 2.2: Einfluss der Bin-Anzahl

**Aufgabe**: Erstellen Sie zwei Histogramme mit denselben Daten, aber unterschiedlicher Bin-Anzahl, um den Unterschied zu sehen.

**Hinweise**:
- Verwenden Sie die Noten aus Beispiel 3 erneut
- Erstellen Sie ein Histogramm mit `bins=5` (grob)
- Erstellen Sie ein zweites Histogramm mit `bins=20` (fein)
- Beobachten Sie, wie sich die Darstellung ändert
- Sie können beide nebeneinander ausgeben, indem Sie beide Code-Blöcke nacheinander ausführen

```{code-cell}
# Ihr Code hier
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Dieselben Notendaten
noten = [2.3, 1.7, 2.0, 3.3, 2.7, 1.3, 2.0, 2.3, 3.0, 2.7,
         1.7, 2.3, 3.7, 2.0, 2.3, 1.7, 3.0, 2.7, 2.0, 3.3,
         2.3, 2.7, 1.3, 3.0, 2.3, 3.7, 2.0, 2.7, 1.7, 3.0,
         2.3, 3.3, 2.0, 2.7, 1.7, 3.0, 4.0, 2.3, 2.7, 3.3,
         2.0, 1.7, 2.3, 3.0, 2.7, 1.3, 2.0, 3.3, 2.7, 2.3]

# Histogramm mit wenigen Bins (grobe Darstellung)
plt.hist(noten, bins=5, color='coral', edgecolor='black')
plt.title('Notenverteilung mit 5 Bins (grob)')
plt.xlabel('Note')
plt.ylabel('Anzahl')
plt.show()

# Histogramm mit vielen Bins (feine Darstellung)
plt.hist(noten, bins=20, color='lightblue', edgecolor='black')
plt.title('Notenverteilung mit 20 Bins (fein)')
plt.xlabel('Note')
plt.ylabel('Anzahl')
plt.show()
```

**Erklärung**:
- Mit 5 Bins sehen Sie die grobe Verteilung: Die meisten Noten liegen im mittleren Bereich
- Mit 20 Bins sehen Sie mehr Details, aber auch mehr Schwankungen ("Rauschen")
- Die Wahl der Bin-Anzahl hängt von Ihren Daten und der gewünschten Detailtiefe ab
- Als Faustregel: Für kleine Datensätze (< 100 Werte) 5-15 Bins, für große (> 1000 Werte) 20-50 Bins
</details>

+++

## Scatter Plots: Zusammenhänge zwischen Variablen

### Theoretische Grundlagen

Scatter Plots (Streudiagramme) dienen der Visualisierung von Beziehungen zwischen zwei Variablen. Jeder Datenpunkt wird als einzelner Punkt im Koordinatensystem dargestellt, wobei seine Position durch die Werte beider Variablen bestimmt wird. Diese Darstellungsform ist besonders wertvoll in der Datenanalyse, da sie Muster, Korrelationen und Ausreißer sichtbar macht.

Im Gegensatz zu Liniendiagrammen, die eine Reihenfolge oder Zeitabfolge suggerieren, zeigen Scatter Plots keine Verbindungslinien. Jeder Punkt steht für sich und repräsentiert eine Beobachtung. Die räumliche Anordnung der Punkte offenbart mögliche Zusammenhänge: Bilden die Punkte eine Linie, deutet dies auf eine starke Korrelation hin. Sind sie zufällig verteilt, gibt es vermutlich keinen linearen Zusammenhang.

+++

Typische Anwendungsfälle:
- Zusammenhang zwischen Lernzeit und Prüfungsergebnis
- Korrelation zwischen Temperatur und Eisverkauf
- Beziehung zwischen Körpergröße und Gewicht
- Identifikation von Ausreißern in Messdaten

**Syntax**:
```python
plt.scatter(x_werte, y_werte)
```

**Semantik**:
- `x_werte`: Liste mit Werten für die horizontale Position der Punkte
- `y_werte`: Liste mit Werten für die vertikale Position der Punkte
- Beide Listen müssen die gleiche Länge haben
- Jedes Wertepaar (x[i], y[i]) wird als ein Punkt dargestellt
- Zusätzliche Parameter: `color`, `alpha` (Transparenz), `s` (Punktgröße), `marker` (Punktform)

+++

### Beispiel 4: Lernzeit vs. Prüfungsergebnis

```{code-cell}
# 15 Studierende: Lernzeit (Stunden) vs. Punktzahl (0-100)
lernzeit = [2, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 15, 16]
punktzahl = [45, 55, 50, 65, 62, 75, 73, 85, 82, 90, 88, 95, 92, 97, 98]

# Scatter Plot erstellen
plt.scatter(lernzeit, punktzahl, color='purple', alpha=0.6, s=100)
plt.title('Zusammenhang zwischen Lernzeit und Prüfungsergebnis')
plt.xlabel('Lernzeit in Stunden')
plt.ylabel('Erreichte Punktzahl')

plt.show()
```

**Was ist passiert?**

- Jedes der 15 Wertepaare wird als einzelner Punkt dargestellt
- Die Punkte bilden ein deutliches Muster: Je mehr Lernzeit, desto höhere Punktzahl
- Dies deutet auf eine **positive Korrelation** hin
- `color='purple'` färbt alle Punkte lila
- `alpha=0.6` macht die Punkte leicht transparent (0=unsichtbar, 1=deckend)
- `s=100` bestimmt die Größe der Punkte (Standardwert: 20)

+++

### Beispiel 5: Keine Korrelation

```{code-cell}
# 20 Personen: Schuhgröße vs. Intelligenzquotient (IQ)
schuhgroesse = [38, 42, 40, 44, 39, 43, 41, 45, 37, 46,
                39, 42, 40, 43, 38, 44, 41, 45, 39, 42]
iq = [105, 98, 112, 102, 118, 95, 108, 101, 115, 99,
      110, 103, 97, 113, 106, 100, 111, 104, 109, 107]

# Scatter Plot erstellen
plt.scatter(schuhgroesse, iq, color='green', alpha=0.5)
plt.title('Schuhgröße vs. IQ (keine Korrelation erwartet)')
plt.xlabel('Schuhgröße')
plt.ylabel('IQ')

plt.show()
```

**Was ist passiert?**

- Die Punkte sind relativ gleichmäßig verteilt, ohne erkennbares Muster
- Dies deutet darauf hin, dass **kein Zusammenhang** zwischen Schuhgröße und IQ besteht
- Genau dies ist zu erwarten, da beide Variablen unabhängig voneinander sind
- Scatter Plots helfen also auch dabei, **fehlende** Zusammenhänge zu erkennen

+++

### Angeleitete Übung 3.1: Temperatur und Eisverkauf

**Aufgabe**: Ein Eiscafé hat Daten über Tagestemperatur und Eisverkäufe gesammelt. Erstellen Sie einen Scatter Plot, um die Beziehung zu visualisieren.

**Hinweise**:
- Temperatur in °C: [15, 18, 20, 22, 25, 28, 30, 32, 27, 24, 21, 19, 17]
- Verkaufte Eisbecher: [45, 60, 70, 85, 110, 140, 160, 180, 130, 95, 75, 65, 50]
- Verwenden Sie `plt.scatter()`
- Wählen Sie eine passende Farbe (z.B. 'orange')
- Fügen Sie Titel und Achsenbeschriftungen hinzu

```{code-cell}
# Ihr Code hier
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Daten des Eiscafés
temperatur = [15, 18, 20, 22, 25, 28, 30, 32, 27, 24, 21, 19, 17]
eisverkaeufe = [45, 60, 70, 85, 110, 140, 160, 180, 130, 95, 75, 65, 50]

# Scatter Plot erstellen
plt.scatter(temperatur, eisverkaeufe, color='orange', alpha=0.7, s=100)
plt.title('Zusammenhang zwischen Temperatur und Eisverkäufen')
plt.xlabel('Temperatur in °C')
plt.ylabel('Verkaufte Eisbecher')

plt.show()
```

**Erklärung**:
- Der Scatter Plot zeigt eine klare positive Korrelation: Je wärmer, desto mehr Eisverkäufe
- Die Punkte bilden eine aufsteigende Tendenz von links unten nach rechts oben
- Bei 32°C wurden die meisten Eisbecher verkauft (180 Stück)
- Bei 15°C wurden die wenigsten verkauft (45 Stück)
- Diese Visualisierung könnte dem Café bei der Personalplanung helfen (mehr Personal an heißen Tagen)
</details>

+++

## Styling: Farben, Linienstile und Marker

### Theoretische Grundlagen

Bisher haben Sie die Standarddarstellung von Matplotlib verwendet. In der Praxis möchten Sie jedoch oft das Aussehen Ihrer Diagramme anpassen, um sie ansprechender zu gestalten, verschiedene Datenreihen zu unterscheiden oder bestimmte Informationen hervorzuheben. Matplotlib bietet umfangreiche Möglichkeiten zur Anpassung von Farben, Linienstilen und Markern.

Diese Anpassungen dienen nicht nur der Ästhetik, sondern erhöhen die Lesbarkeit und Aussagekraft Ihrer Visualisierungen. In wissenschaftlichen Publikationen, Präsentationen oder Berichten sind gut gestaltete Diagramme essentiell für die Kommunikation Ihrer Ergebnisse.

+++

**Syntax für Farben**:
```python
plt.plot(x, y, color='farbname')
```

**Verfügbare Farben** (Auswahl):
- Farbnamen: `'red'`, `'blue'`, `'green'`, `'orange'`, `'purple'`, `'cyan'`, `'magenta'`, `'yellow'`, `'black'`, `'gray'`
- Kurzformen: `'r'` (red), `'b'` (blue), `'g'` (green), `'k'` (black), `'y'` (yellow)
- Hex-Codes: `'#FF5733'` (beliebige RGB-Farben)

**Syntax für Linienstile**:
```python
plt.plot(x, y, linestyle='stil')
```

**Verfügbare Linienstile**:
- `'-'`: Durchgezogene Linie (Standard)
- `'--'`: Gestrichelt
- `'-.'`: Strich-Punkt
- `':'`: Gepunktet
- `''`: Keine Linie (nur Marker)

+++

**Syntax für Marker**:
```python
plt.plot(x, y, marker='symbol')
```

**Verfügbare Marker** (Auswahl):
- `'o'`: Kreis
- `'s'`: Quadrat
- `'^'`: Dreieck (nach oben)
- `'v'`: Dreieck (nach unten)
- `'*'`: Stern
- `'+'`: Plus
- `'x'`: X
- `'D'`: Diamant

**Kombinierte Syntax** (Kurzform):
```python
plt.plot(x, y, 'ro--')  # Rote Kreise mit gestrichelter Linie
```

+++

### Beispiel 6: Verschiedene Linienstile

```{code-cell}
# Drei verschiedene Linien mit unterschiedlichen Stilen
x = [1, 2, 3, 4, 5]
y1 = [1, 2, 3, 4, 5]
y2 = [1, 3, 2, 4, 3]
y3 = [5, 4, 3, 2, 1]

# Linien mit verschiedenen Stilen plotten
plt.plot(x, y1, linestyle='-', color='blue', label='Durchgezogen')
plt.plot(x, y2, linestyle='--', color='red', label='Gestrichelt')
plt.plot(x, y3, linestyle=':', color='green', label='Gepunktet')

plt.title('Verschiedene Linienstile')
plt.legend()
plt.show()
```

**Was ist passiert?**

- Drei Linien werden mit unterschiedlichen Stilen dargestellt
- `linestyle='-'`: Durchgezogene Linie (Standard)
- `linestyle='--'`: Gestrichelte Linie
- `linestyle=':'`: Gepunktete Linie
- Jede Linie hat eine eigene Farbe und ein Label für die Legende
- Diese Technik ist nützlich für Schwarz-Weiß-Drucke, wo Farben nicht unterscheidbar sind

+++

### Beispiel 7: Linien mit Markern

```{code-cell}
# Zwei Linien mit Markern an jedem Datenpunkt
monate = [1, 2, 3, 4, 5, 6]
standort_a = [100, 110, 105, 120, 115, 125]
standort_b = [90, 95, 100, 98, 105, 110]

# Linien mit Markern
plt.plot(monate, standort_a, marker='o', color='blue', 
         label='Standort A')
plt.plot(monate, standort_b, marker='s', color='red', 
         label='Standort B')

plt.title('Verkaufszahlen mit Datenpunkt-Markern')
plt.xlabel('Monat')
plt.ylabel('Verkäufe')
plt.legend()
plt.show()
```

**Was ist passiert?**

- Beide Linien haben Marker an jedem Datenpunkt
- `marker='o'`: Kreise an den Datenpunkten für Standort A
- `marker='s'`: Quadrate an den Datenpunkten für Standort B
- Die Marker machen die einzelnen Datenpunkte deutlich sichtbar
- Dies ist besonders hilfreich bei wenigen Datenpunkten oder wenn Sie betonen möchten, wo tatsächlich Messungen vorliegen

+++

### Angeleitete Übung 4.1: Styling anwenden

**Aufgabe**: Erstellen Sie ein Diagramm mit drei Linien, die jeweils unterschiedliche Kombinationen von Farbe, Linienstil und Marker verwenden.

**Hinweise**:
- x-Werte: [1, 2, 3, 4, 5]
- y1: [2, 4, 6, 8, 10]
- y2: [1, 3, 5, 7, 9]
- y3: [10, 8, 6, 4, 2]
- Linie 1: Blau, durchgezogen, Kreismarker
- Linie 2: Rot, gestrichelt, Quadratmarker
- Linie 3: Grün, gepunktet, Dreieckmarker ('^')
- Fügen Sie eine Legende hinzu

```{code-cell}
# Ihr Code hier
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Daten
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
y3 = [10, 8, 6, 4, 2]

# Drei Linien mit unterschiedlichem Styling
plt.plot(x, y1, color='blue', linestyle='-', marker='o', label='Linie 1')
plt.plot(x, y2, color='red', linestyle='--', marker='s', label='Linie 2')
plt.plot(x, y3, color='green', linestyle=':', marker='^', label='Linie 3')

plt.title('Drei Linien mit individuellem Styling')
plt.xlabel('x-Werte')
plt.ylabel('y-Werte')
plt.legend()
plt.show()
```

**Erklärung**:
- Jede Linie hat eine einzigartige Kombination von Farbe, Linienstil und Marker
- Die Marker machen jeden Datenpunkt einzeln identifizierbar
- Unterschiedliche Linienstile ermöglichen Unterscheidung auch ohne Farbe (z.B. beim Drucken)
- Die Legende hilft, die Linien zuzuordnen
- Sie können die Parameter auch in Kurzform kombinieren: `plt.plot(x, y1, 'bo-')` für blau, Kreis, durchgezogen
</details>

+++

## Subplots: Mehrere Diagramme arrangieren

### Theoretische Grundlagen

In der Datenanalyse möchten Sie oft mehrere Diagramme nebeneinander oder untereinander darstellen, um verschiedene Aspekte Ihrer Daten zu vergleichen. Matplotlib bietet mit der Funktion `subplots()` die Möglichkeit, mehrere Diagramme in einer einzigen Figure anzuordnen.

Sie haben diese Funktion bereits in Notebook 18 kennengelernt. Dort haben Sie `fig, ax = plt.subplots()` verwendet, um explizit eine Figure und ein Axes-Objekt zu erstellen. Nun erweitern Sie diese Technik, um mehrere Axes in einem Raster anzuordnen.

+++

**Syntax**:
```python
fig, ax = plt.subplots(nrows, ncols)
```

**Semantik**:
- `nrows`: Anzahl der Zeilen im Raster
- `ncols`: Anzahl der Spalten im Raster
- Gibt zwei Werte zurück: `fig` (die Figure) und `ax` (Array von Axes)
- Bei einem einzelnen Subplot (1, 1) ist `ax` ein einzelnes Axes-Objekt
- Bei mehreren Subplots ist `ax` ein Array, auf das Sie mit Indizes zugreifen
- Für 1D-Anordnung (z.B. 1 Zeile, 3 Spalten): `ax[0]`, `ax[1]`, `ax[2]`
- Für 2D-Anordnung (z.B. 2 Zeilen, 2 Spalten): `ax[0, 0]`, `ax[0, 1]`, `ax[1, 0]`, `ax[1, 1]`

+++

**Wichtige Axes-Methoden**:
- `ax.plot()`: Liniendiagramm im Subplot erstellen
- `ax.bar()`: Balkendiagramm im Subplot erstellen
- `ax.scatter()`: Scatter Plot im Subplot erstellen
- `ax.hist()`: Histogramm im Subplot erstellen
- `ax.set_title()`: Titel für den Subplot setzen (mit "set_"!)
- `ax.set_xlabel()`: x-Achse beschriften (mit "set_"!)
- `ax.set_ylabel()`: y-Achse beschriften (mit "set_"!)
- `ax.legend()`: Legende für den Subplot hinzufügen

**Layout-Optimierung**:
```python
fig.tight_layout()
```
Diese Funktion passt die Abstände zwischen Subplots automatisch an, um Überlappungen zu vermeiden.

+++

### Beispiel 8: Zwei Diagramme nebeneinander

```{code-cell}
# Figure mit 2 Subplots (1 Zeile, 2 Spalten)
fig, ax = plt.subplots(1, 2)

# Linker Subplot: Liniendiagramm
monate = [1, 2, 3, 4, 5, 6]
umsatz = [100, 120, 115, 135, 140, 155]
ax[0].plot(monate, umsatz, color='blue', marker='o')
ax[0].set_title('Umsatzentwicklung')
ax[0].set_xlabel('Monat')
ax[0].set_ylabel('Umsatz in Tausend €')

# Rechter Subplot: Balkendiagramm
kategorien = ['A', 'B', 'C', 'D']
werte = [25, 40, 30, 35]
ax[1].bar(kategorien, werte, color='green')
ax[1].set_title('Verteilung nach Kategorie')
ax[1].set_xlabel('Kategorie')
ax[1].set_ylabel('Anzahl')

# Layout optimieren
fig.tight_layout()
plt.show()
```

**Was ist passiert?**

- `plt.subplots(1, 2)` erstellt eine Figure mit 2 Subplots nebeneinander (1 Zeile, 2 Spalten)
- `ax` ist nun ein eindimensionales Array mit 2 Elementen: `ax[0]` (links) und `ax[1]` (rechts)
- Für jeden Subplot verwenden Sie die Methoden des jeweiligen Axes-Objekts
- Beachten Sie: Die Methoden heißen `set_title()`, `set_xlabel()`, `set_ylabel()` (mit "set_")
- `fig.tight_layout()` verhindert, dass sich Beschriftungen überlappen
- Beide Diagramme sind unabhängig voneinander und können unterschiedliche Typen haben

+++

### Beispiel 9: Vier Diagramme im Raster

```{code-cell}
# Figure mit 4 Subplots (2 Zeilen, 2 Spalten)
fig, ax = plt.subplots(2, 2)

# Oben links: Liniendiagramm
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
ax[0, 0].plot(x, y, 'b-')
ax[0, 0].set_title('Liniendiagramm')

# Oben rechts: Scatter Plot
ax[0, 1].scatter(x, [1, 4, 2, 5, 3], color='red')
ax[0, 1].set_title('Scatter Plot')

# Unten links: Balkendiagramm
ax[1, 0].bar(['A', 'B', 'C'], [10, 20, 15], color='green')
ax[1, 0].set_title('Balkendiagramm')

# Unten rechts: Histogramm
daten = [1, 2, 2, 3, 3, 3, 4, 4, 5]
ax[1, 1].hist(daten, bins=5, color='orange', edgecolor='black')
ax[1, 1].set_title('Histogramm')

# Layout optimieren
fig.tight_layout()
plt.show()
```

**Was ist passiert?**

- `plt.subplots(2, 2)` erstellt ein 2×2-Raster mit 4 Subplots
- `ax` ist nun ein zweidimensionales Array: `ax[zeile, spalte]`
- `ax[0, 0]`: Oben links, `ax[0, 1]`: Oben rechts
- `ax[1, 0]`: Unten links, `ax[1, 1]`: Unten rechts
- Jeder Subplot kann einen anderen Diagrammtyp enthalten
- Dies ermöglicht einen umfassenden Überblick über verschiedene Aspekte Ihrer Daten
- `fig.tight_layout()` ist hier besonders wichtig, da 4 Diagramme mehr Platz benötigen

+++

### Angeleitete Übung 5.1: Zwei Subplots untereinander

**Aufgabe**: Erstellen Sie eine Figure mit 2 Subplots untereinander (2 Zeilen, 1 Spalte). Der obere zeigt Temperaturen, der untere Niederschlagsmengen.

**Hinweise**:
- Verwenden Sie `plt.subplots(2, 1)` für die Anordnung
- Tage: [1, 2, 3, 4, 5, 6, 7]
- Temperaturen: [18, 20, 22, 21, 19, 17, 16]
- Niederschlag in mm: [0, 2, 0, 5, 8, 3, 1]
- Oberer Subplot: Liniendiagramm für Temperaturen
- Unterer Subplot: Balkendiagramm für Niederschlag
- Beide Subplots sollen Titel und Achsenbeschriftungen haben

```{code-cell}
# Ihr Code hier
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Figure mit 2 Subplots untereinander
fig, ax = plt.subplots(2, 1)

# Gemeinsame Daten
tage = [1, 2, 3, 4, 5, 6, 7]

# Oberer Subplot: Temperaturen
temperaturen = [18, 20, 22, 21, 19, 17, 16]
ax[0].plot(tage, temperaturen, color='red', marker='o')
ax[0].set_title('Temperaturverlauf')
ax[0].set_xlabel('Tag')
ax[0].set_ylabel('Temperatur in °C')

# Unterer Subplot: Niederschlag
niederschlag = [0, 2, 0, 5, 8, 3, 1]
ax[1].bar(tage, niederschlag, color='blue')
ax[1].set_title('Niederschlagsmenge')
ax[1].set_xlabel('Tag')
ax[1].set_ylabel('Niederschlag in mm')

# Layout optimieren
fig.tight_layout()
plt.show()
```

**Erklärung**:
- Mit 2 Zeilen und 1 Spalte werden die Diagramme übereinander angeordnet
- `ax[0]` ist der obere Subplot, `ax[1]` der untere
- Die gemeinsame x-Achse (Tage) ermöglicht direkten Vergleich: An Tag 5 war es kühler und es regnete am meisten
- Diese Darstellung ist typisch für Wetterdaten oder andere zeitabhängige Messgrößen
- Die vertikale Anordnung eignet sich besonders, wenn beide Diagramme die gleiche x-Achse haben
</details>

+++

## Abschlussübungen

Die folgenden Aufgaben testen Ihr Verständnis der in diesem Notebook erlernten Konzepte. Bearbeiten Sie die Aufgaben selbstständig und vergleichen Sie Ihre Lösung anschließend mit den Musterlösungen am Ende des Notebooks.

+++

### Teil 1: Grundlegende Anwendung

**Kompetenzstufe**: Anwenden

Diese Aufgaben testen die direkte Anwendung der erlernten Konzepte.

+++

**Aufgabe 1**: Sie haben die monatlichen Besucherzahlen zweier Websites erfasst:
- Website A: [1200, 1350, 1400, 1550, 1600, 1750]
- Website B: [1100, 1250, 1450, 1400, 1650, 1700]
- Monate: [1, 2, 3, 4, 5, 6]

Erstellen Sie ein Liniendiagramm mit beiden Websites, fügen Sie eine Legende hinzu und beschriften Sie die Achsen.

```{code-cell}
# Arbeitsbereich für Aufgabe 1
```

**Aufgabe 2**: Erstellen Sie ein Histogramm für folgende Körpergrößen (in cm) von 30 Personen:
- [165, 170, 168, 175, 180, 172, 178, 169, 173, 177, 171, 176, 174, 179, 167, 172, 175, 181, 168, 173, 170, 176, 174, 178, 169, 172, 177, 171, 175, 180]

Verwenden Sie 8 Bins und eine passende Farbe. Beschriften Sie das Diagramm vollständig.

```{code-cell}
# Arbeitsbereich für Aufgabe 2
```

### Teil 2: Transfer und Problemlösung

**Kompetenzstufe**: Analysieren & Erschaffen

Diese Aufgaben erfordern die Kombination mehrerer Konzepte und eigenständiges Problemlösen.

+++

**Aufgabe 3**: Ein Fitness-Tracker hat folgende Daten aufgezeichnet:
- Trainingstage: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
- Gelaufene Kilometer: [3, 5, 4, 6, 7, 6, 8, 9, 8, 10]
- Kalorienverbrauch: [300, 500, 400, 600, 700, 600, 800, 900, 800, 1000]

Erstellen Sie eine Figure mit 2 Subplots (nebeneinander):
- Links: Scatter Plot von Kilometern vs. Kalorienverbrauch (um Korrelation zu zeigen)
- Rechts: Liniendiagramm der gelaufenen Kilometer über die Zeit

Beide Diagramme sollen vollständig beschriftet sein und das linke soll farbige Punkte mit Transparenz (alpha=0.6) haben.

```{code-cell}
# Arbeitsbereich für Aufgabe 3
```

**Aufgabe 4**: Erstellen Sie eine umfassende Datenvisualisierung für einen Online-Shop mit 4 Subplots (2×2):

**Daten**:
- Monate: [1, 2, 3, 4, 5, 6]
- Bestellungen: [120, 135, 142, 156, 148, 165]
- Durchschnittlicher Bestellwert in €: [45, 48, 52, 50, 55, 58]
- Produktkategorien: ['Elektronik', 'Kleidung', 'Bücher', 'Sport']
- Verkäufe pro Kategorie: [450, 380, 290, 210]
- Kundenzufriedenheit (Bewertungen 1-5): [4, 5, 4, 5, 5, 4, 3, 5, 4, 5, 4, 5, 5, 4, 5]

**Subplots**:
1. Oben links: Liniendiagramm der Bestellungen über die Zeit (mit Markern)
2. Oben rechts: Liniendiagramm des durchschnittlichen Bestellwerts (mit Markern, anderer Farbe)
3. Unten links: Balkendiagramm der Verkäufe pro Kategorie
4. Unten rechts: Histogramm der Kundenzufriedenheit (5 Bins)

Alle Diagramme sollen Titel und Achsenbeschriftungen haben. Verwenden Sie `fig.tight_layout()`.

```{code-cell}
# Arbeitsbereich für Aufgabe 4
```

## Zusammenfassung

In diesem Notebook haben Sie folgende Konzepte kennengelernt:

| Konzept | Syntax | Anwendungsfall |
|---------|--------|----------------|
| Achsenbereiche | `plt.xlim(min, max)`, `plt.ylim(min, max)` | Fokus auf bestimmte Wertebereiche legen |
| Legenden | `plt.plot(..., label='Text')`, `plt.legend()` | Mehrere Datenreihen unterscheiden |
| Histogramme | `plt.hist(daten, bins=n)` | Verteilung von Daten visualisieren |
| Scatter Plots | `plt.scatter(x, y)` | Beziehungen zwischen Variablen darstellen |
| Farben | `color='name'` oder `color='#HEX'` | Diagramme farblich gestalten |
| Linienstile | `linestyle='-'`, `'--'`, `':'`, `'-.'` | Verschiedene Linien unterscheiden |
| Marker | `marker='o'`, `'s'`, `'^'`, etc. | Datenpunkte hervorheben |
| Subplots | `fig, ax = plt.subplots(rows, cols)` | Mehrere Diagramme arrangieren |
| Axes-Methoden | `ax.plot()`, `ax.set_title()`, etc. | Einzelne Subplots steuern |
| Layout-Optimierung | `fig.tight_layout()` | Überlappungen bei Subplots vermeiden |

+++

**Zentrale Erkenntnisse**:
- **Achsenanpassungen** ermöglichen präzise Kontrolle über die Darstellung und helfen, relevante Details hervorzuheben
- **Legenden** sind essentiell beim Vergleich mehrerer Datenreihen und machen Diagramme selbsterklärend
- **Histogramme** visualisieren Verteilungen und offenbaren Muster in großen Datensätzen
- **Scatter Plots** zeigen Korrelationen zwischen Variablen und helfen, Zusammenhänge zu erkennen
- **Styling-Optionen** (Farben, Linien, Marker) verbessern Lesbarkeit und ermöglichen Anpassung an verschiedene Kontexte
- **Subplots** erlauben die Kombination mehrerer Visualisierungen für umfassende Datenanalysen
- Die Wahl des richtigen Diagrammtyps hängt von der Art Ihrer Daten und Ihrer Fragestellung ab

**Nächste Schritte**: Im folgenden Notebook (20 - Datenbanksysteme) verlassen Sie die Datenvisualisierung und lernen die Grundlagen relationaler Datenbanken kennen. Sie werden verstehen, wie große Datenmengen strukturiert gespeichert und effizient abgefragt werden können.

+++

## Musterlösungen

+++

<details>
<summary>Lösung zu Aufgabe 1</summary>

```python
# Daten
monate = [1, 2, 3, 4, 5, 6]
website_a = [1200, 1350, 1400, 1550, 1600, 1750]
website_b = [1100, 1250, 1450, 1400, 1650, 1700]

# Beide Linien mit Labels plotten
plt.plot(monate, website_a, label='Website A', color='blue', marker='o')
plt.plot(monate, website_b, label='Website B', color='red', marker='s')

# Beschriftungen
plt.title('Vergleich monatlicher Besucherzahlen')
plt.xlabel('Monat')
plt.ylabel('Anzahl Besucher')
plt.legend()

plt.show()
```

**Erklärung**:
- Beide Websites zeigen einen steigenden Trend über die 6 Monate
- Website A hatte durchgehend mehr Besucher, mit Ausnahme von Monat 3
- Die Legende macht sofort klar, welche Linie zu welcher Website gehört
- Die unterschiedlichen Marker (Kreise vs. Quadrate) erleichtern die Unterscheidung zusätzlich
- Solche Visualisierungen sind typisch für Webanalyse-Berichte

**Häufige Fehler**:
- Vergessen der Labels beim `plot()`-Aufruf → Legende bleibt leer
- Vergessen von `plt.legend()` → Labels werden nicht angezeigt
- Beide Linien in derselben Farbe → schwer unterscheidbar
</details>

+++

<details>
<summary>Lösung zu Aufgabe 2</summary>

```python
# Körpergrößen in cm
groessen = [165, 170, 168, 175, 180, 172, 178, 169, 173, 177, 
            171, 176, 174, 179, 167, 172, 175, 181, 168, 173, 
            170, 176, 174, 178, 169, 172, 177, 171, 175, 180]

# Histogramm erstellen
plt.hist(groessen, bins=8, color='steelblue', edgecolor='black')
plt.title('Verteilung der Körpergrößen')
plt.xlabel('Körpergröße in cm')
plt.ylabel('Anzahl Personen')

plt.show()
```

**Erklärung**:
- Das Histogramm zeigt, dass die meisten Personen zwischen 170 und 178 cm groß sind
- Die Verteilung ist relativ symmetrisch mit einem Höhepunkt in der Mitte
- 8 Bins liefern eine gute Balance zwischen Detail und Übersichtlichkeit
- Die schwarzen Rahmen (`edgecolor`) machen die Grenzen zwischen den Bins klar sichtbar
- Solche Histogramme sind typisch für anthropometrische Daten

**Häufige Fehler**:
- Zu viele Bins (z.B. 30) → Histogram wird zu detailliert und "rauschig"
- Zu wenige Bins (z.B. 3) → Wichtige Details der Verteilung gehen verloren
- Fehlende Achsenbeschriftung, besonders der Einheit (cm)
</details>

+++

<details>
<summary>Lösung zu Aufgabe 3</summary>

```python
# Daten
tage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kilometer = [3, 5, 4, 6, 7, 6, 8, 9, 8, 10]
kalorien = [300, 500, 400, 600, 700, 600, 800, 900, 800, 1000]

# Figure mit 2 Subplots nebeneinander
fig, ax = plt.subplots(1, 2)

# Linker Subplot: Scatter Plot (Kilometer vs. Kalorien)
ax[0].scatter(kilometer, kalorien, color='red', alpha=0.6, s=100)
ax[0].set_title('Kilometer vs. Kalorienverbrauch')
ax[0].set_xlabel('Gelaufene Kilometer')
ax[0].set_ylabel('Verbrauchte Kalorien')

# Rechter Subplot: Liniendiagramm (Kilometer über Zeit)
ax[1].plot(tage, kilometer, color='blue', marker='o')
ax[1].set_title('Laufleistung über 10 Tage')
ax[1].set_xlabel('Trainingstag')
ax[1].set_ylabel('Gelaufene Kilometer')

# Layout optimieren
fig.tight_layout()
plt.show()
```

**Erklärung**:
- Der linke Scatter Plot zeigt eine starke positive Korrelation: Mehr Kilometer = mehr Kalorien
- Die Punkte bilden fast eine gerade Linie, was auf einen linearen Zusammenhang hindeutet
- Der rechte Plot zeigt die Verbesserung über die Zeit: Die Laufleistung steigt von Tag zu Tag
- Die Kombination beider Diagramme gibt einen umfassenden Überblick über die Trainingsdaten
- `alpha=0.6` macht die Punkte leicht transparent, was bei Überlappungen hilft

**Alternative Ansätze**:
- Sie könnten auch ein drittes Diagramm hinzufügen, das Kalorien über die Zeit zeigt
- Eine andere Anordnung wäre untereinander (2 Zeilen, 1 Spalte) statt nebeneinander
</details>

+++

<details>
<summary>Lösung zu Aufgabe 4</summary>

```python
# Daten
monate = [1, 2, 3, 4, 5, 6]
bestellungen = [120, 135, 142, 156, 148, 165]
bestellwert = [45, 48, 52, 50, 55, 58]
kategorien = ['Elektronik', 'Kleidung', 'Bücher', 'Sport']
verkaeufe = [450, 380, 290, 210]
zufriedenheit = [4, 5, 4, 5, 5, 4, 3, 5, 4, 5, 4, 5, 5, 4, 5]

# Figure mit 4 Subplots (2×2)
fig, ax = plt.subplots(2, 2)

# Oben links: Bestellungen über Zeit
ax[0, 0].plot(monate, bestellungen, color='blue', marker='o')
ax[0, 0].set_title('Monatliche Bestellungen')
ax[0, 0].set_xlabel('Monat')
ax[0, 0].set_ylabel('Anzahl Bestellungen')

# Oben rechts: Durchschnittlicher Bestellwert
ax[0, 1].plot(monate, bestellwert, color='green', marker='s')
ax[0, 1].set_title('Durchschnittlicher Bestellwert')
ax[0, 1].set_xlabel('Monat')
ax[0, 1].set_ylabel('Bestellwert in €')

# Unten links: Verkäufe pro Kategorie
ax[1, 0].bar(kategorien, verkaeufe, color='orange')
ax[1, 0].set_title('Verkäufe nach Kategorie')
ax[1, 0].set_xlabel('Kategorie')
ax[1, 0].set_ylabel('Anzahl Verkäufe')

# Unten rechts: Kundenzufriedenheit
ax[1, 1].hist(zufriedenheit, bins=5, color='purple', edgecolor='black')
ax[1, 1].set_title('Kundenzufriedenheit')
ax[1, 1].set_xlabel('Bewertung (1-5)')
ax[1, 1].set_ylabel('Anzahl Bewertungen')

# Layout optimieren
fig.tight_layout()
plt.show()
```

**Erklärung**:
- Diese umfassende Visualisierung zeigt vier verschiedene Aspekte des Online-Shops
- **Oben links**: Bestellungen steigen tendenziell über die Monate (positiver Trend)
- **Oben rechts**: Auch der durchschnittliche Bestellwert steigt (Kunden kaufen mehr)
- **Unten links**: Elektronik ist die umsatzstärkste Kategorie, Sport die schwächste
- **Unten rechts**: Die meisten Bewertungen sind 4 oder 5 Sterne (hohe Zufriedenheit)
- Die Kombination aller vier Diagramme gibt einen schnellen, umfassenden Überblick
- `fig.tight_layout()` ist hier essentiell, um Überlappungen zu vermeiden
- Solche Dashboard-artigen Visualisierungen sind typisch für Geschäftsberichte

**Alternative Ansätze**:
- Sie könnten die Kategorien-Namen im Balkendiagramm abkürzen oder drehen (`plt.xticks(rotation=45)`), falls sie zu lang sind
- Eine andere Anordnung wäre 1 Zeile mit 4 Spalten für einen horizontalen Dashboard-Look
- Sie könnten Farben thematisch aufeinander abstimmen (z.B. alle in Blautönen)
</details>
