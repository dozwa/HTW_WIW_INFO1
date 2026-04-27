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

# 17 - Pandas Statistik: Grundlegende statistische Analysen mit DataFrames

## Lernziele

Nach Abschluss dieses Notebooks können Sie:
- Statistische Kennzahlen (Mittelwert, Median, Standardabweichung, Varianz) berechnen und interpretieren
- Die Methoden `mean()`, `median()`, `std()`, `var()`, `sum()`, `min()`, `max()` auf DataFrames anwenden
- Die Funktion `describe()` zur schnellen Übersicht statistischer Kennzahlen nutzen
- Daten mit `groupby()` gruppieren und Aggregationsfunktionen anwenden
- Statistische Analysen zur Datenexploration und Mustererkennung einsetzen

**Kompetenzstufen**: Verstehen, Anwenden, Analysieren

---

## Voraussetzungen

Für dieses Notebook sollten Sie folgende Konzepte beherrschen:
- Pandas DataFrames erstellen und manipulieren (Notebook 16)
- Spalten auswählen und indexieren mit `loc` und `iloc` (Notebook 16)
- CSV-Dateien einlesen mit `read_csv()` (Notebook 16)
- Schleifen und Funktionen (Notebooks 07, 10)

Falls Sie diese Konzepte noch nicht sicher beherrschen, wiederholen Sie bitte die entsprechenden Notebooks.

---

+++

## Einführung: Statistische Analysen in der Datenwissenschaft

Statistische Analysen bilden das Fundament der Datenwissenschaft. Sie ermöglichen es, aus großen Datenmengen Muster zu erkennen, Hypothesen zu testen und fundierte Entscheidungen zu treffen. In der Praxis werden statistische Methoden eingesetzt, um beispielsweise Kundenverhalten zu verstehen, Produktqualität zu überwachen oder Geschäftsentwicklungen zu prognostizieren.

Pandas stellt eine umfassende Sammlung statistischer Funktionen bereit, die direkt auf DataFrames angewendet werden können. Diese Funktionen berechnen wichtige Kennzahlen wie Mittelwerte, Mediane oder Standardabweichungen mit nur einer Zeile Code. Dadurch wird die explorative Datenanalyse erheblich vereinfacht.

In diesem Notebook lernen Sie die wichtigsten statistischen Funktionen in Pandas kennen. Sie beginnen mit einfachen Kennzahlen wie dem Mittelwert und arbeiten sich zu komplexeren Analysen mit gruppierten Daten vor. Alle Konzepte werden mit praxisnahen Beispielen illustriert, die Sie sofort nachvollziehen und anwenden können.

+++

## Beispiel-DataFrame für die Analysen

Für die folgenden Beispiele erstellen wir einen DataFrame mit Mitarbeiterdaten eines fiktiven Unternehmens. Dieser DataFrame enthält Informationen über Alter und Gehalt von acht Mitarbeitern.

```{code-cell}
import pandas as pd

# DataFrame mit Mitarbeiterdaten erstellen
df = pd.DataFrame({
    "Alter": [23, 24, 22, 25, 27, 23, 25, 24],
    "Gehalt": [3500, 4000, 3000, 4500, 4000, 3500, 4000, 4500]
})

print(df)
```

**Ausgabe**:
```
   Alter  Gehalt
0     23    3500
1     24    4000
2     22    3000
3     25    4500
4     27    4000
5     23    3500
6     25    4000
7     24    4500
```

Dieser DataFrame dient als Grundlage für alle nachfolgenden statistischen Analysen. Sie werden lernen, verschiedene Kennzahlen aus diesen Daten zu berechnen.

+++

---

## Mittelwert (Arithmetisches Mittel): Die Methode `mean()`

### Theoretische Grundlagen

Der **Mittelwert** (auch arithmetisches Mittel genannt) ist eine der grundlegendsten statistischen Kennzahlen. Er beschreibt den durchschnittlichen Wert einer Zahlenreihe und wird berechnet, indem man alle Werte addiert und durch ihre Anzahl teilt.

**Beispiel**: Bei den Altersangaben [23, 24, 22, 25] beträgt der Mittelwert (23 + 24 + 22 + 25) / 4 = 23,5 Jahre.

Der Mittelwert wird häufig verwendet, um einen ersten Überblick über die zentrale Tendenz von Daten zu erhalten. Er reagiert jedoch empfindlich auf Ausreißer: Ein einzelner sehr hoher oder sehr niedriger Wert kann den Mittelwert stark beeinflussen.

+++

### Syntax und Semantik

**Syntax**:
```python
mittelwert = df.mean()           # Mittelwert aller numerischen Spalten
mittelwert_spalte = df['Spaltenname'].mean()  # Mittelwert einer Spalte
```

**Semantik**:
- `df.mean()`: Berechnet den Mittelwert für jede numerische Spalte im DataFrame
- `df['Spaltenname'].mean()`: Berechnet den Mittelwert nur für die angegebene Spalte
- **Rückgabewert**: Bei `df.mean()` wird eine Series mit den Mittelwerten zurückgegeben. Bei `df['Spaltenname'].mean()` wird ein einzelner Zahlenwert (float) zurückgegeben.
- **Wichtig**: Nicht-numerische Spalten werden automatisch ignoriert.

+++

### Beispiel 1: Mittelwert aller Spalten berechnen

Wir berechnen nun den Mittelwert für alle numerischen Spalten unseres Mitarbeiter-DataFrames. Dies gibt uns einen schnellen Überblick über das durchschnittliche Alter und Gehalt.

```{code-cell}
# Mittelwert für alle Spalten berechnen
durchschnitt = df.mean()
print(durchschnitt)
```

**Ausgabe**:
```
Alter       24.125
Gehalt    3875.000
dtype: float64
```

**Erklärung**: Die Methode `mean()` berechnet automatisch für jede numerische Spalte den Mittelwert. Das durchschnittliche Alter der Mitarbeiter beträgt 24,125 Jahre, das durchschnittliche Gehalt 3.875 Euro. Das Ergebnis ist eine Series mit den Spaltennamen als Index.

+++

### Angeleitete Übung 1.1

**Aufgabe**: Erstellen Sie einen DataFrame mit folgenden Noten: [1.3, 2.0, 1.7, 2.3, 1.0] und berechnen Sie die durchschnittliche Note.

**Hinweise**:
- Schritt 1: Erstellen Sie einen DataFrame mit einer Spalte "Note" und den angegebenen Werten
- Schritt 2: Verwenden Sie die Methode `mean()` auf der Spalte "Note"
- Schritt 3: Geben Sie das Ergebnis mit `print()` aus

```{code-cell}
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
# DataFrame mit Noten erstellen
df_noten = pd.DataFrame({
    "Note": [1.3, 2.0, 1.7, 2.3, 1.0]
})

# Durchschnittliche Note berechnen
durchschnitt_note = df_noten['Note'].mean()
print("Durchschnittliche Note:", durchschnitt_note)
```

**Erklärung**: Der DataFrame wird mit einer Spalte "Note" erstellt. Die Methode `mean()` wird direkt auf diese Spalte angewendet und berechnet den Mittelwert: (1.3 + 2.0 + 1.7 + 2.3 + 1.0) / 5 = 1.66.
</details>

+++

### Beispiel 2: Mittelwert einer einzelnen Spalte

Oft benötigt man nur den Mittelwert einer bestimmten Spalte. Dies ist nützlich, wenn man gezielt eine Variable untersuchen möchte.

```{code-cell}
# Durchschnittliches Gehalt berechnen
durchschnitt_gehalt = df['Gehalt'].mean()
print("Durchschnittliches Gehalt:", durchschnitt_gehalt, "Euro")
```

**Ausgabe**:
```
Durchschnittliches Gehalt: 3875.0 Euro
```

**Erklärung**: Durch die Spaltenauswahl `df['Gehalt']` wird nur die Gehalt-Spalte ausgewählt. Die Methode `mean()` berechnet dann den Mittelwert dieser Spalte. Das Ergebnis ist ein einzelner float-Wert.

+++

### Angeleitete Übung 1.2

**Aufgabe**: Berechnen Sie das durchschnittliche Alter aus dem ursprünglichen DataFrame `df` und geben Sie es in einem vollständigen Satz aus: "Das durchschnittliche Alter beträgt X Jahre."

**Hinweise**:
- Verwenden Sie `df['Alter'].mean()` zur Berechnung
- Nutzen Sie F-String-Formatierung für die Ausgabe

```{code-cell}
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
# Durchschnittliches Alter berechnen
durchschnitt_alter = df['Alter'].mean()
print(f"Das durchschnittliche Alter beträgt {durchschnitt_alter} Jahre.")
```

**Erklärung**: Die Spalte "Alter" wird mit `df['Alter']` ausgewählt und der Mittelwert mit `mean()` berechnet. Die F-String-Formatierung ermöglicht eine leserliche Ausgabe des Ergebnisses.
</details>

+++

---

## Median: Die Methode `median()`

### Theoretische Grundlagen

Der **Median** (auch Zentralwert genannt) ist eine weitere wichtige statistische Kennzahl. Er beschreibt den mittleren Wert einer sortierten Zahlenreihe: 50% der Werte liegen unter dem Median, 50% darüber.

**Berechnung**: Um den Median zu bestimmen, sortiert man zunächst alle Werte der Größe nach. Bei einer ungeraden Anzahl von Werten ist der Median der mittlere Wert. Bei einer geraden Anzahl ist er der Mittelwert der beiden mittleren Werte.

**Beispiel**: Bei den sortierten Altersangaben [22, 23, 23, 24, 24, 25, 25, 27] gibt es 8 Werte. Der Median liegt zwischen dem 4. und 5. Wert, also zwischen 24 und 24, somit ist der Median 24.

+++

### Unterschied zwischen Mittelwert und Median

Der Median ist robuster gegenüber Ausreißern als der Mittelwert. Ein extremer Wert (z.B. ein sehr hohes Gehalt) beeinflusst den Median kaum, während er den Mittelwert stark verzerren kann.

**Beispiel**: Bei Gehältern [3000, 3500, 4000, 4500, 100000] beträgt der Mittelwert 23.000 Euro (stark verzerrt durch den Ausreißer), während der Median 4.000 Euro beträgt (realistische Mitte).

In der Praxis verwendet man den Median häufig bei Einkommensstatistiken oder Immobilienpreisen, da diese oft Ausreißer enthalten.

+++

### Syntax und Semantik

**Syntax**:
```python
median = df.median()           # Median aller numerischen Spalten
median_spalte = df['Spaltenname'].median()  # Median einer Spalte
```

**Semantik**:
- `df.median()`: Berechnet den Median für jede numerische Spalte
- `df['Spaltenname'].median()`: Berechnet den Median nur für die angegebene Spalte
- **Rückgabewert**: Wie bei `mean()` wird eine Series oder ein einzelner Wert zurückgegeben
- **Wichtig**: Die Werte werden intern automatisch sortiert

+++

### Beispiel 3: Median berechnen

Wir berechnen nun den Median für alle Spalten unseres DataFrames und vergleichen ihn mit dem Mittelwert.

```{code-cell}
# Median für alle Spalten berechnen
median = df.median()
print("Median:")
print(median)
```

**Ausgabe**:
```
Median:
Alter       24.0
Gehalt    4000.0
dtype: float64
```

**Erklärung**: Der Median des Alters beträgt 24 Jahre, der Median des Gehalts 4.000 Euro. Beachten Sie, dass der Median-Gehalt (4.000) höher ist als der Mittelwert-Gehalt (3.875). Dies deutet darauf hin, dass die niedrigeren Gehälter den Mittelwert nach unten ziehen.

+++

### Angeleitete Übung 2.1

**Aufgabe**: Erstellen Sie einen DataFrame mit Verkaufszahlen [100, 150, 200, 180, 10000] und berechnen Sie sowohl Mittelwert als auch Median. Vergleichen Sie die Ergebnisse.

**Hinweise**:
- Erstellen Sie einen DataFrame mit einer Spalte "Verkäufe"
- Berechnen Sie beide Kennzahlen
- Überlegen Sie: Welche Kennzahl ist aussagekräftiger?

```{code-cell}
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
# DataFrame mit Verkaufszahlen erstellen
df_verkauf = pd.DataFrame({
    "Verkäufe": [100, 150, 200, 180, 10000]
})

# Mittelwert und Median berechnen
mittelwert = df_verkauf['Verkäufe'].mean()
median = df_verkauf['Verkäufe'].median()

print(f"Mittelwert: {mittelwert}")
print(f"Median: {median}")
```

**Erklärung**: Der Mittelwert beträgt 2.126 (stark beeinflusst durch den Ausreißer 10.000), während der Median 180 beträgt. Der Median ist hier aussagekräftiger, da er die typische Verkaufszahl besser repräsentiert. Der Ausreißer 10.000 könnte ein Sonderfall sein (z.B. Großauftrag).
</details>

+++

---

## Minimum, Maximum und Summe: `min()`, `max()`, `sum()`

### Theoretische Grundlagen

Neben Mittelwert und Median sind auch Extremwerte und Summen wichtige statistische Kennzahlen:

- **Minimum (`min()`)**: Der kleinste Wert in einer Zahlenreihe. Zeigt die untere Grenze der Daten.
- **Maximum (`max()`)**: Der größte Wert in einer Zahlenreihe. Zeigt die obere Grenze der Daten.
- **Summe (`sum()`)**: Die Addition aller Werte. Nützlich für Gesamtberechnungen (z.B. Gesamtumsatz).

Diese Kennzahlen helfen, die Spannweite (Range = Maximum - Minimum) der Daten zu verstehen und Gesamtwerte zu ermitteln.

+++

### Syntax und Semantik

**Syntax**:
```python
minimum = df.min()              # Minimum aller Spalten
maximum = df.max()              # Maximum aller Spalten
summe = df.sum()                # Summe aller Spalten
```

**Semantik**:
- Alle drei Methoden funktionieren analog zu `mean()` und `median()`
- Sie können auf den gesamten DataFrame oder einzelne Spalten angewendet werden
- **Rückgabewert**: Series bei Anwendung auf DataFrame, einzelner Wert bei Anwendung auf Spalte

+++

### Beispiel 4: Minimum, Maximum und Summe berechnen

Wir berechnen diese drei Kennzahlen für unseren Mitarbeiter-DataFrame.

```{code-cell}
# Maximum berechnen
maximum = df.max()
print("Maximum:")
print(maximum)
```

**Ausgabe**:
```
Maximum:
Alter       27
Gehalt    4500
dtype: int64
```

**Erklärung**: Der älteste Mitarbeiter ist 27 Jahre alt, das höchste Gehalt beträgt 4.500 Euro.

```{code-cell}
# Minimum berechnen
minimum = df.min()
print("Minimum:")
print(minimum)
```

**Ausgabe**:
```
Minimum:
Alter       22
Gehalt    3000
dtype: int64
```

**Erklärung**: Der jüngste Mitarbeiter ist 22 Jahre alt, das niedrigste Gehalt beträgt 3.000 Euro.

```{code-cell}
# Summe berechnen
summe = df.sum()
print("Summe:")
print(summe)
```

**Ausgabe**:
```
Summe:
Alter       193
Gehalt    31000
dtype: int64
```

**Erklärung**: Die Summe aller Alter beträgt 193 Jahre (wenig aussagekräftig). Die Gesamtgehaltssumme beträgt 31.000 Euro – dies ist relevant für Personalkosten.

+++

### Angeleitete Übung 3.1

**Aufgabe**: Berechnen Sie die Spannweite (Range) des Alters und des Gehalts. Die Spannweite ist die Differenz zwischen Maximum und Minimum.

**Hinweise**:
- Berechnen Sie zuerst Maximum und Minimum
- Subtrahieren Sie Minimum vom Maximum
- Geben Sie die Ergebnisse aus

```{code-cell}
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
# Spannweite des Alters berechnen
spannweite_alter = df['Alter'].max() - df['Alter'].min()
print(f"Spannweite Alter: {spannweite_alter} Jahre")

# Spannweite des Gehalts berechnen
spannweite_gehalt = df['Gehalt'].max() - df['Gehalt'].min()
print(f"Spannweite Gehalt: {spannweite_gehalt} Euro")
```

**Erklärung**: Die Spannweite zeigt, wie weit die Werte auseinander liegen. Das Alter variiert um 5 Jahre (27 - 22), das Gehalt um 1.500 Euro (4.500 - 3.000). Eine große Spannweite deutet auf heterogene Daten hin.
</details>

+++

---

## Standardabweichung und Varianz: `std()` und `var()`

### Theoretische Grundlagen

Während Mittelwert und Median die zentrale Tendenz beschreiben, messen **Standardabweichung** und **Varianz** die Streuung der Daten – also wie stark die einzelnen Werte vom Mittelwert abweichen.

**Varianz**: Die durchschnittliche quadrierte Abweichung vom Mittelwert. Sie gibt an, wie stark die Werte um den Mittelwert streuen. Die Einheit ist das Quadrat der ursprünglichen Einheit (z.B. Jahre²).

**Standardabweichung**: Die Quadratwurzel der Varianz. Sie hat dieselbe Einheit wie die Ursprungsdaten (z.B. Jahre) und ist daher intuitiver interpretierbar. Eine kleine Standardabweichung bedeutet, dass die Werte nah am Mittelwert liegen. Eine große Standardabweichung bedeutet, dass die Werte weit streuen.

+++

### Interpretation der Standardabweichung

**Beispiel**: Bei einem durchschnittlichen Alter von 24 Jahren und einer Standardabweichung von 1,5 Jahren liegen die meisten Mitarbeiter im Altersbereich 22,5 bis 25,5 Jahre (Mittelwert ± Standardabweichung).

**Faustregeln**:
- Bei normalverteilten Daten liegen ca. 68% der Werte innerhalb von ± 1 Standardabweichung um den Mittelwert
- Ca. 95% liegen innerhalb von ± 2 Standardabweichungen

In der Praxis verwendet man die Standardabweichung häufiger als die Varianz, da sie in derselben Einheit wie die Daten vorliegt.

+++

### Syntax und Semantik

**Syntax**:
```python
standardabweichung = df.std()   # Standardabweichung aller Spalten
varianz = df.var()              # Varianz aller Spalten
```

**Semantik**:
- `df.std()`: Berechnet die Standardabweichung für jede numerische Spalte
- `df.var()`: Berechnet die Varianz für jede numerische Spalte
- **Rückgabewert**: Series mit den berechneten Werten
- **Wichtig**: Pandas verwendet standardmäßig die Stichproben-Standardabweichung (Division durch n-1, nicht n)

+++

### Beispiel 5: Standardabweichung und Varianz berechnen

Wir berechnen beide Kennzahlen für unseren DataFrame, um die Streuung der Daten zu verstehen.

```{code-cell}
# Standardabweichung berechnen
standardabweichung = df.std()
print("Standardabweichung:")
print(standardabweichung)
```

**Ausgabe**:
```
Standardabweichung:
Alter       1.553774
Gehalt    534.522484
dtype: float64
```

**Erklärung**: Das Alter der Mitarbeiter streut um etwa 1,55 Jahre um den Mittelwert von 24,125 Jahren. Die Gehälter streuen um etwa 535 Euro um den Mittelwert von 3.875 Euro. Die Werte sind relativ homogen.

```{code-cell}
# Varianz berechnen
varianz = df.var()
print("Varianz:")
print(varianz)
```

**Ausgabe**:
```
Varianz:
Alter         2.410714
Gehalt    285714.285714
dtype: float64
```

**Erklärung**: Die Varianz ist das Quadrat der Standardabweichung. Beachten Sie, dass die Einheiten quadriert sind (Jahre², Euro²), was die Interpretation erschwert. Daher bevorzugt man meist die Standardabweichung.

+++

### Angeleitete Übung 4.1

**Aufgabe**: Erstellen Sie zwei DataFrames: einen mit sehr homogenen Daten [50, 51, 49, 50, 50] und einen mit heterogenen Daten [10, 30, 50, 70, 90]. Berechnen Sie jeweils die Standardabweichung und vergleichen Sie.

**Hinweise**:
- Erstellen Sie beide DataFrames mit einer Spalte "Wert"
- Berechnen Sie die Standardabweichung für beide
- Interpretieren Sie den Unterschied

```{code-cell}
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
# Homogene Daten
df_homogen = pd.DataFrame({
    "Wert": [50, 51, 49, 50, 50]
})

# Heterogene Daten
df_heterogen = pd.DataFrame({
    "Wert": [10, 30, 50, 70, 90]
})

# Standardabweichungen berechnen
std_homogen = df_homogen['Wert'].std()
std_heterogen = df_heterogen['Wert'].std()

print(f"Standardabweichung homogen: {std_homogen:.2f}")
print(f"Standardabweichung heterogen: {std_heterogen:.2f}")
```

**Erklärung**: Die homogenen Daten haben eine sehr kleine Standardabweichung (ca. 0,71), da alle Werte nah beieinander liegen. Die heterogenen Daten haben eine große Standardabweichung (ca. 31,62), da die Werte stark streuen. Die Standardabweichung quantifiziert also die Variabilität der Daten.
</details>

+++

---

## Schnelle Übersicht: Die Methode `describe()`

### Theoretische Grundlagen

Bei der explorativen Datenanalyse möchte man oft schnell einen Überblick über die wichtigsten statistischen Kennzahlen erhalten. Die Methode `describe()` fasst die wichtigsten deskriptiven Statistiken kompakt zusammen.

`describe()` berechnet automatisch:
- **count**: Anzahl der nicht-fehlenden Werte
- **mean**: Mittelwert
- **std**: Standardabweichung
- **min**: Minimum
- **25%**: Erstes Quartil (25% der Werte liegen darunter)
- **50%**: Median (zweites Quartil)
- **75%**: Drittes Quartil (75% der Werte liegen darunter)
- **max**: Maximum

Diese Zusammenfassung gibt einen schnellen Überblick über Lage (Mittelwert, Median) und Streuung (Standardabweichung, Quartile) der Daten.

+++

### Syntax und Semantik

**Syntax**:
```python
übersicht = df.describe()
```

**Semantik**:
- `df.describe()`: Erzeugt eine statistische Zusammenfassung aller numerischen Spalten
- **Rückgabewert**: Ein neuer DataFrame mit Statistiken als Zeilen und den ursprünglichen Spalten als Spalten
- **Wichtig**: Nicht-numerische Spalten werden automatisch ignoriert

+++

### Beispiel 6: Vollständige statistische Übersicht erstellen

Wir verwenden `describe()`, um alle wichtigen Kennzahlen auf einen Blick zu erhalten.

```{code-cell}
# Statistische Übersicht erstellen
übersicht = df.describe()
print(übersicht)
```

**Ausgabe**:
```
            Alter        Gehalt
count    8.000000      8.000000
mean    24.125000   3875.000000
std      1.553774    534.522484
min     22.000000   3000.000000
25%     23.000000   3500.000000
50%     24.000000   4000.000000
75%     24.750000   4125.000000
max     27.000000   4500.000000
```

**Erklärung**: Diese Tabelle liefert eine kompakte Übersicht:
- Es gibt 8 vollständige Datensätze (count)
- Der Median-Alter (50%) beträgt 24 Jahre, das Median-Gehalt 4.000 Euro
- 25% der Mitarbeiter sind 23 Jahre oder jünger (25%-Quartil)
- 75% verdienen 4.125 Euro oder weniger (75%-Quartil)

Diese Übersicht ist besonders nützlich beim ersten Erkunden eines neuen Datensatzes.

+++

### Angeleitete Übung 5.1

**Aufgabe**: Erstellen Sie einen DataFrame mit Prüfungsergebnissen [45, 67, 89, 92, 78, 55, 88, 91, 73, 82] und erstellen Sie eine statistische Übersicht mit `describe()`.

**Hinweise**:
- Spaltenname: "Punkte"
- Verwenden Sie `describe()` zur Analyse
- Interpretieren Sie die 25%-, 50%- und 75%-Werte

```{code-cell}
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
# DataFrame mit Prüfungsergebnissen erstellen
df_pruefung = pd.DataFrame({
    "Punkte": [45, 67, 89, 92, 78, 55, 88, 91, 73, 82]
})

# Statistische Übersicht erstellen
übersicht_pruefung = df_pruefung.describe()
print(übersicht_pruefung)
```

**Erklärung**: Die Übersicht zeigt:
- Durchschnittlich wurden 76 Punkte erreicht
- Der Median liegt bei 80 Punkten (50%)
- 25% der Studierenden haben 66,5 oder weniger Punkte (unteres Quartil)
- 75% haben 88,75 oder weniger Punkte (oberes Quartil)
- Die Spannweite reicht von 45 bis 92 Punkten

Diese Informationen helfen, die Leistungsverteilung schnell einzuschätzen.
</details>

+++

---

## Gruppieren und Aggregieren: Die Methode `groupby()`

### Theoretische Grundlagen

In der Praxis möchte man häufig Daten nach bestimmten Kategorien gruppieren und für jede Gruppe separate Statistiken berechnen. Beispiele:
- Durchschnittsgehalt pro Abteilung
- Umsatz pro Region
- Durchschnittsnote pro Studiengang

Die Methode `groupby()` ermöglicht genau dies. Sie teilt einen DataFrame in Gruppen auf, basierend auf den Werten einer oder mehrerer Spalten. Anschließend können Aggregationsfunktionen (wie `mean()`, `sum()`, etc.) auf jede Gruppe angewendet werden.

+++

### Das Split-Apply-Combine-Prinzip

`groupby()` folgt dem **Split-Apply-Combine-Prinzip**:

1. **Split**: Der DataFrame wird in Gruppen aufgeteilt (basierend auf einer Kategoriespalte)
2. **Apply**: Eine Funktion (z.B. `mean()`) wird auf jede Gruppe angewendet
3. **Combine**: Die Ergebnisse werden zu einem neuen DataFrame zusammengefügt

Dieses Konzept ist fundamental für die Datenanalyse und wird in nahezu jedem Datenprojekt verwendet.

+++

### Syntax und Semantik

**Syntax**:
```python
gruppiert = df.groupby('Kategoriespalte')
ergebnis = gruppiert.mean()  # Oder andere Aggregationsfunktion

# Oder direkt in einem Schritt:
ergebnis = df.groupby('Kategoriespalte').mean()
```

**Semantik**:
- `df.groupby('Spaltenname')`: Erstellt ein GroupBy-Objekt, das die Gruppen repräsentiert
- `.mean()` (oder andere Aggregationsfunktion): Berechnet die Kennzahl für jede Gruppe
- **Rückgabewert**: Ein neuer DataFrame, bei dem die Gruppierspalte als Index dient
- **Wichtig**: Das GroupBy-Objekt selbst enthält noch keine Ergebnisse – erst die Aggregationsfunktion berechnet diese

+++

### Beispiel 7: Daten nach Abteilung gruppieren

Wir erweitern unseren DataFrame um eine Abteilungsspalte und berechnen das durchschnittliche Gehalt pro Abteilung.

```{code-cell}
# DataFrame mit Abteilungsinformationen erstellen
df_abteilung = pd.DataFrame({
    "Abteilung": ["Marketing", "Vertrieb", "Marketing", "Vertrieb", 
                  "Marketing", "Vertrieb", "Marketing", "Vertrieb"],
    "Alter": [23, 24, 22, 25, 27, 23, 25, 24],
    "Gehalt": [3500, 4000, 3000, 4500, 4000, 3500, 4000, 4500]
})

print("Ursprünglicher DataFrame:")
print(df_abteilung)
```

**Ausgabe**:
```
Ursprünglicher DataFrame:
   Abteilung  Alter  Gehalt
0  Marketing     23    3500
1   Vertrieb     24    4000
2  Marketing     22    3000
3   Vertrieb     25    4500
4  Marketing     27    4000
5   Vertrieb     23    3500
6  Marketing     25    4000
7   Vertrieb     24    4500
```

**Erklärung**: Der DataFrame enthält nun eine zusätzliche Spalte "Abteilung". Wir haben je 4 Mitarbeiter aus Marketing und Vertrieb.

```{code-cell}
# Daten nach Abteilung gruppieren und Mittelwerte berechnen
gruppiert = df_abteilung.groupby('Abteilung').mean()
print("\nDurchschnittswerte pro Abteilung:")
print(gruppiert)
```

**Ausgabe**:
```
Durchschnittswerte pro Abteilung:
            Alter   Gehalt
Abteilung                 
Marketing   24.25  3625.00
Vertrieb    24.00  4125.00
```

**Erklärung**: Die Methode `groupby('Abteilung')` teilt den DataFrame in zwei Gruppen (Marketing und Vertrieb). Die Funktion `mean()` berechnet dann für jede Gruppe separat die Mittelwerte. Ergebnis: Marketing-Mitarbeiter sind durchschnittlich 24,25 Jahre alt und verdienen 3.625 Euro, Vertriebs-Mitarbeiter sind 24 Jahre alt und verdienen 4.125 Euro. Die Spalte "Abteilung" wird zum Index des Ergebnis-DataFrames.

+++

### Beispiel 8: Mehrere Aggregationsfunktionen kombinieren

Man kann auch mehrere Aggregationsfunktionen gleichzeitig auf gruppierte Daten anwenden. Dies wird mit der Methode `agg()` (kurz für "aggregate") erreicht.

```{code-cell}
# Mehrere Statistiken pro Abteilung berechnen
statistiken = df_abteilung.groupby('Abteilung')['Gehalt'].agg(['mean', 'min', 'max', 'std'])
print("Gehalt-Statistiken pro Abteilung:")
print(statistiken)
```

**Ausgabe**:
```
Gehalt-Statistiken pro Abteilung:
             mean   min   max         std
Abteilung                                
Marketing  3625.0  3000  4000  433.012702
Vertrieb   4125.0  3500  4500  433.012702
```

**Erklärung**: Mit `agg()` können mehrere Aggregationsfunktionen gleichzeitig angewendet werden. Hier wurde nur die Spalte 'Gehalt' ausgewählt (`['Gehalt']`), und für jede Abteilung wurden Mittelwert, Minimum, Maximum und Standardabweichung berechnet. Dies gibt einen umfassenden Überblick über die Gehaltsverteilung in den Abteilungen.

+++

### Angeleitete Übung 6.1

**Aufgabe**: Erstellen Sie einen DataFrame mit folgenden Daten:
- Namen: ['Anna', 'Ben', 'Carla', 'Daniel', 'Eva', 'Frank']
- Abteilung: ['IT', 'IT', 'HR', 'HR', 'IT', 'HR']
- Gehalt: [4500, 4200, 3800, 3900, 4800, 3700]

Berechnen Sie das durchschnittliche Gehalt pro Abteilung.

**Hinweise**:
- Schritt 1: Erstellen Sie den DataFrame
- Schritt 2: Verwenden Sie `groupby('Abteilung')`
- Schritt 3: Wenden Sie `mean()` an
- Schritt 4: Geben Sie das Ergebnis aus

```{code-cell}
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
# DataFrame erstellen
df_personal = pd.DataFrame({
    'Name': ['Anna', 'Ben', 'Carla', 'Daniel', 'Eva', 'Frank'],
    'Abteilung': ['IT', 'IT', 'HR', 'HR', 'IT', 'HR'],
    'Gehalt': [4500, 4200, 3800, 3900, 4800, 3700]
})

# Durchschnittliches Gehalt pro Abteilung berechnen
durchschnitt_abteilung = df_personal.groupby('Abteilung')['Gehalt'].mean()
print("Durchschnittliches Gehalt pro Abteilung:")
print(durchschnitt_abteilung)
```

**Erklärung**: Der DataFrame wird nach Abteilung gruppiert. Die IT-Abteilung hat 3 Mitarbeiter mit durchschnittlich 4.500 Euro, die HR-Abteilung hat 3 Mitarbeiter mit durchschnittlich 3.800 Euro. Durch die Auswahl `['Gehalt']` wird nur diese Spalte aggregiert.
</details>

+++

### Angeleitete Übung 6.2

**Aufgabe**: Verwenden Sie denselben DataFrame wie in Übung 6.1. Berechnen Sie für jede Abteilung sowohl das Minimum als auch das Maximum des Gehalts mit einer einzigen `agg()`-Anweisung.

**Hinweise**:
- Verwenden Sie `groupby('Abteilung')['Gehalt']`
- Nutzen Sie `.agg(['min', 'max'])`

```{code-cell}
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
# Minimum und Maximum pro Abteilung berechnen
min_max_abteilung = df_personal.groupby('Abteilung')['Gehalt'].agg(['min', 'max'])
print("Gehaltsspanne pro Abteilung:")
print(min_max_abteilung)
```

**Erklärung**: Die Methode `agg()` erlaubt es, mehrere Aggregationsfunktionen in einer Liste anzugeben. Für jede Abteilung werden sowohl das niedrigste als auch das höchste Gehalt berechnet. In der IT reicht die Spanne von 4.200 bis 4.800 Euro, in HR von 3.700 bis 3.900 Euro.
</details>

+++

---

## Abschlussübungen

Die folgenden Aufgaben testen Ihr Verständnis der in diesem Notebook erlernten Konzepte. Bearbeiten Sie die Aufgaben selbstständig und vergleichen Sie Ihre Lösung anschließend mit den Musterlösungen am Ende des Notebooks.

---

### Teil 1: Grundlegende Anwendung

**Kompetenzstufe**: Anwenden

Diese Aufgaben testen die direkte Anwendung der erlernten statistischen Funktionen.

---

**Aufgabe 1**: Erstellen Sie einen DataFrame mit den folgenden Daten:
- Produkt: ['Laptop', 'Maus', 'Tastatur', 'Monitor', 'Headset']
- Preis: [899, 25, 75, 299, 89]
- Verkäufe: [45, 230, 180, 67, 120]

Berechnen Sie:
1. Den durchschnittlichen Preis
2. Die Gesamtanzahl der Verkäufe (Summe)
3. Den Median der Preise
4. Die Standardabweichung der Verkäufe

```{code-cell}
# Arbeitsbereich für Aufgabe 1
```

---

**Aufgabe 2**: Verwenden Sie denselben DataFrame aus Aufgabe 1. Erstellen Sie eine vollständige statistische Übersicht mit `describe()` für beide numerischen Spalten (Preis und Verkäufe).

```{code-cell}
# Arbeitsbereich für Aufgabe 2
```

---

### Teil 2: Transfer und Problemlösung

**Kompetenzstufe**: Analysieren & Erschaffen

Diese Aufgaben erfordern die Kombination mehrerer Konzepte und eigenständiges Problemlösen.

---

**Aufgabe 3**: Erstellen Sie einen DataFrame mit Studierendendaten:
- Name: ['Lisa', 'Max', 'Sophie', 'Tom', 'Emma', 'Paul', 'Laura', 'Felix']
- Studiengang: ['Informatik', 'BWL', 'Informatik', 'BWL', 'Informatik', 'BWL', 'Informatik', 'BWL']
- Note: [1.7, 2.3, 1.3, 2.0, 1.0, 2.7, 1.7, 2.3]
- ECTS: [180, 165, 210, 150, 195, 180, 180, 165]

Führen Sie folgende Analysen durch:
1. Berechnen Sie die durchschnittliche Note pro Studiengang
2. Berechnen Sie die durchschnittlichen ECTS-Punkte pro Studiengang
3. Ermitteln Sie, welcher Studiengang die bessere durchschnittliche Note hat
4. Berechnen Sie für jeden Studiengang sowohl den Mittelwert als auch die Standardabweichung der Noten mit `agg()`

```{code-cell}
# Arbeitsbereich für Aufgabe 3
```

---

**Aufgabe 4**: Sie haben Verkaufsdaten aus verschiedenen Filialen:
- Filiale: ['Nord', 'Süd', 'Nord', 'Ost', 'Süd', 'West', 'Nord', 'Ost', 'West', 'Süd']
- Umsatz: [45000, 52000, 48000, 39000, 55000, 42000, 51000, 41000, 44000, 53000]
- Kunden: [450, 520, 480, 390, 550, 420, 510, 410, 440, 530]

Analysieren Sie:
1. Erstellen Sie den DataFrame
2. Berechnen Sie für jede Filiale den durchschnittlichen Umsatz und die durchschnittliche Kundenanzahl
3. Berechnen Sie den durchschnittlichen Umsatz pro Kunde für jede Filiale (Hinweis: Umsatz / Kunden)
4. Identifizieren Sie die Filiale mit dem höchsten durchschnittlichen Umsatz pro Kunde
5. Erstellen Sie eine Übersicht mit Minimum, Maximum und Standardabweichung des Umsatzes pro Filiale

```{code-cell}
# Arbeitsbereich für Aufgabe 4
```

---

## Zusammenfassung

In diesem Notebook haben Sie die wichtigsten statistischen Funktionen in Pandas kennengelernt:

| Konzept | Syntax | Anwendungsfall |
|---------|--------|----------------|
| Mittelwert | `df.mean()` | Durchschnittswert einer Zahlenreihe berechnen |
| Median | `df.median()` | Mittleren Wert (robust gegen Ausreißer) bestimmen |
| Minimum | `df.min()` | Kleinsten Wert finden |
| Maximum | `df.max()` | Größten Wert finden |
| Summe | `df.sum()` | Gesamtsumme berechnen |
| Standardabweichung | `df.std()` | Streuung der Daten messen |
| Varianz | `df.var()` | Quadrierte Streuung berechnen |
| Statistische Übersicht | `df.describe()` | Schnelle Übersicht aller wichtigen Kennzahlen |
| Gruppierung | `df.groupby('Spalte')` | Daten nach Kategorien gruppieren und aggregieren |
| Mehrfach-Aggregation | `.agg(['func1', 'func2'])` | Mehrere Statistiken gleichzeitig berechnen |

**Zentrale Erkenntnisse**:
- **Statistische Kennzahlen** bieten schnellen Überblick über zentrale Tendenz (Mittelwert, Median) und Streuung (Standardabweichung) von Daten
- **Der Median** ist robuster gegenüber Ausreißern als der Mittelwert und sollte bei schiefen Verteilungen bevorzugt werden
- **`describe()`** liefert eine kompakte Übersicht und ist ideal für die explorative Datenanalyse
- **`groupby()`** ist das zentrale Werkzeug für kategoriebasierte Analysen und folgt dem Split-Apply-Combine-Prinzip
- **Statistische Analysen** sind der erste Schritt zur Mustererkennung und datengestützten Entscheidungsfindung

**Nächste Schritte**: Im folgenden Notebook (18 - Matplotlib Grundlagen) werden Sie lernen, wie Sie statistische Ergebnisse visuell darstellen können. Visualisierungen machen Muster und Zusammenhänge in Daten oft erst auf den ersten Blick erkennbar.

+++

---

## Musterlösungen

<details>
<summary>Lösung zu Aufgabe 1</summary>

```python
# DataFrame erstellen
df_produkte = pd.DataFrame({
    'Produkt': ['Laptop', 'Maus', 'Tastatur', 'Monitor', 'Headset'],
    'Preis': [899, 25, 75, 299, 89],
    'Verkäufe': [45, 230, 180, 67, 120]
})

# 1. Durchschnittlicher Preis
durchschnitt_preis = df_produkte['Preis'].mean()
print(f"Durchschnittlicher Preis: {durchschnitt_preis:.2f} Euro")

# 2. Gesamtanzahl Verkäufe
gesamt_verkäufe = df_produkte['Verkäufe'].sum()
print(f"Gesamtanzahl Verkäufe: {gesamt_verkäufe}")

# 3. Median der Preise
median_preis = df_produkte['Preis'].median()
print(f"Median der Preise: {median_preis} Euro")

# 4. Standardabweichung der Verkäufe
std_verkäufe = df_produkte['Verkäufe'].std()
print(f"Standardabweichung der Verkäufe: {std_verkäufe:.2f}")
```

**Erklärung**:
- Der durchschnittliche Preis beträgt 277,40 Euro (Summe aller Preise / 5)
- Insgesamt wurden 642 Produkte verkauft
- Der Median-Preis beträgt 89 Euro (mittlerer Wert bei sortierten Preisen: [25, 75, **89**, 299, 899])
- Die Standardabweichung der Verkäufe zeigt, wie stark die Verkaufszahlen streuen (ca. 74,5)

**Häufige Fehler**:
- Verwechslung von `mean()` und `median()` – der Median ist nicht der Durchschnitt!
- Vergessen, die richtige Spalte auszuwählen: `df['Spalte'].mean()` statt `df.mean()`
</details>

<details>
<summary>Lösung zu Aufgabe 2</summary>

```python
# Statistische Übersicht erstellen
übersicht_produkte = df_produkte.describe()
print(übersicht_produkte)
```

**Erklärung**: Die Methode `describe()` berechnet automatisch alle wichtigen statistischen Kennzahlen für die numerischen Spalten (Preis und Verkäufe). Die Spalte "Produkt" wird ignoriert, da sie nicht-numerisch ist. Aus der Übersicht können Sie ablesen:
- Count: 5 vollständige Datensätze
- Mean: Durchschnittswerte
- Std: Standardabweichungen zeigen, dass Preise stärker streuen als Verkaufszahlen
- Min/Max: Spannweite der Werte
- 25%, 50%, 75%: Quartile zeigen die Verteilung
</details>

<details>
<summary>Lösung zu Aufgabe 3</summary>

```python
# DataFrame erstellen
df_studenten = pd.DataFrame({
    'Name': ['Lisa', 'Max', 'Sophie', 'Tom', 'Emma', 'Paul', 'Laura', 'Felix'],
    'Studiengang': ['Informatik', 'BWL', 'Informatik', 'BWL', 'Informatik', 'BWL', 'Informatik', 'BWL'],
    'Note': [1.7, 2.3, 1.3, 2.0, 1.0, 2.7, 1.7, 2.3],
    'ECTS': [180, 165, 210, 150, 195, 180, 180, 165]
})

# 1. Durchschnittliche Note pro Studiengang
durchschnitt_note = df_studenten.groupby('Studiengang')['Note'].mean()
print("Durchschnittliche Note pro Studiengang:")
print(durchschnitt_note)

# 2. Durchschnittliche ECTS pro Studiengang
durchschnitt_ects = df_studenten.groupby('Studiengang')['ECTS'].mean()
print("\nDurchschnittliche ECTS pro Studiengang:")
print(durchschnitt_ects)

# 3. Welcher Studiengang hat die bessere Note?
bester_studiengang = durchschnitt_note.idxmin()  # kleinste Note ist die beste
print(f"\nStudiengang mit der besten durchschnittlichen Note: {bester_studiengang}")

# 4. Mittelwert und Standardabweichung der Noten
note_statistik = df_studenten.groupby('Studiengang')['Note'].agg(['mean', 'std'])
print("\nNoten-Statistik pro Studiengang:")
print(note_statistik)
```

**Erklärung**: 
- Die durchschnittliche Note in Informatik ist 1,425, in BWL 2,325 – Informatik hat also die bessere Durchschnittsnote
- Die durchschnittlichen ECTS-Punkte sind in Informatik höher (191,25 vs. 165)
- `idxmin()` findet den Index (hier: Studiengang) mit dem kleinsten Wert (beste Note)
- Die Standardabweichung zeigt, wie stark die Noten innerhalb jedes Studiengangs streuen

**Besonderheiten**: Bei Noten ist eine kleinere Zahl besser, daher verwenden wir `idxmin()` statt `idxmax()`.
</details>

<details>
<summary>Lösung zu Aufgabe 4</summary>

```python
# 1. DataFrame erstellen
df_filialen = pd.DataFrame({
    'Filiale': ['Nord', 'Süd', 'Nord', 'Ost', 'Süd', 'West', 'Nord', 'Ost', 'West', 'Süd'],
    'Umsatz': [45000, 52000, 48000, 39000, 55000, 42000, 51000, 41000, 44000, 53000],
    'Kunden': [450, 520, 480, 390, 550, 420, 510, 410, 440, 530]
})

# 2. Durchschnittlicher Umsatz und Kundenanzahl pro Filiale
durchschnitt_filiale = df_filialen.groupby('Filiale')[['Umsatz', 'Kunden']].mean()
print("Durchschnittswerte pro Filiale:")
print(durchschnitt_filiale)

# 3. Durchschnittlicher Umsatz pro Kunde für jede Filiale
# Zuerst Umsatz pro Kunde für jeden Datensatz berechnen
df_filialen['Umsatz_pro_Kunde'] = df_filialen['Umsatz'] / df_filialen['Kunden']

# Dann Durchschnitt pro Filiale
umsatz_pro_kunde = df_filialen.groupby('Filiale')['Umsatz_pro_Kunde'].mean()
print("\nDurchschnittlicher Umsatz pro Kunde:")
print(umsatz_pro_kunde)

# 4. Filiale mit höchstem Umsatz pro Kunde
beste_filiale = umsatz_pro_kunde.idxmax()
print(f"\nFiliale mit höchstem Umsatz pro Kunde: {beste_filiale}")
print(f"Wert: {umsatz_pro_kunde[beste_filiale]:.2f} Euro pro Kunde")

# 5. Übersicht: Minimum, Maximum, Standardabweichung des Umsatzes
umsatz_übersicht = df_filialen.groupby('Filiale')['Umsatz'].agg(['min', 'max', 'std'])
print("\nUmsatz-Statistiken pro Filiale:")
print(umsatz_übersicht)
```

**Erklärung**: 
- Die Filiale "Süd" hat den höchsten durchschnittlichen Umsatz (53.333 Euro) und die meisten Kunden (533)
- Der Umsatz pro Kunde wird berechnet, indem eine neue Spalte erstellt wird: `df['Neue_Spalte'] = df['Spalte1'] / df['Spalte2']`
- `idxmax()` findet die Filiale mit dem höchsten durchschnittlichen Umsatz pro Kunde
- Die Standardabweichung zeigt, wie konsistent die Umsätze in jeder Filiale sind

**Alternative Ansätze**:
- Man könnte auch erst gruppieren und dann den Umsatz pro Kunde berechnen: `durchschnitt_filiale['Umsatz'] / durchschnitt_filiale['Kunden']`
- Für eine vollständige Analyse könnte man auch die Anzahl der Datensätze pro Filiale mit `count()` ermitteln
</details>
