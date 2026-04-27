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

# 16 - Pandas DataFrames: Einführung in die tabellarische Datenverarbeitung

## Lernziele

Nach Abschluss dieses Notebooks können Sie:
- Die Pandas-Bibliothek in Python importieren und ihre Bedeutung für die Datenverarbeitung erklären
- DataFrames aus verschiedenen Datenquellen (Listen, Dictionaries, CSV-Dateien) erstellen
- Mit `loc` und `iloc` gezielt auf Zeilen und Spalten in einem DataFrame zugreifen
- Spalten zu einem DataFrame hinzufügen, entfernen und modifizieren
- DataFrames nach bestimmten Kriterien filtern und sortieren

**Kompetenzstufen**: Verstehen, Anwenden

---

## Voraussetzungen

Für dieses Notebook sollten Sie folgende Konzepte beherrschen:
- Variablen und Datentypen (Notebooks 04-05)
- Komplexe Datentypen: Listen und Dictionaries (Notebook 06)
- Operatoren und Vergleichsoperationen (Notebook 08)
- File I/O: Dateien lesen (Notebook 12)

**Wichtig**: Dies ist das erste Notebook, in dem wir eine **externe Bibliothek** verwenden. Eine Bibliothek ist eine Sammlung von vorgefertigten Funktionen und Datenstrukturen, die uns die Arbeit erleichtern. Pandas ist eine der wichtigsten Bibliotheken für die Datenanalyse in Python.

Falls Sie diese Konzepte noch nicht sicher beherrschen, wiederholen Sie bitte die entsprechenden Notebooks.

---

+++

## Einführung in Pandas: Was ist Pandas und warum benötigen wir es?

### Was ist Pandas?

Pandas ist eine leistungsstarke Open-Source-Bibliothek für die Datenanalyse und -manipulation in Python. Der Name "Pandas" leitet sich von "Panel Data" ab, einem Begriff aus der Ökonometrie für mehrdimensionale Datensätze. Die Bibliothek wurde speziell entwickelt, um die Arbeit mit strukturierten, tabellarischen Daten zu vereinfachen.

### Warum benötigen wir Pandas?

Bisher haben Sie gelernt, wie man mit grundlegenden Python-Datenstrukturen wie Listen und Dictionaries arbeitet. Diese sind für einfache Datensammlungen ausreichend. Sobald Sie jedoch mit größeren Datenmengen arbeiten, die in Tabellenform organisiert sind (wie z.B. Excel-Tabellen, CSV-Dateien oder Datenbanktabellen), stoßen Sie mit den Basisdatentypen schnell an Grenzen.

Pandas löst dieses Problem, indem es spezialisierte Datenstrukturen und Funktionen bereitstellt, die folgende Aufgaben ermöglichen:
- Effizientes Laden großer Datenmengen aus verschiedenen Quellen (CSV, Excel, Datenbanken)
- Übersichtliche Darstellung von Daten in Tabellenform
- Einfacher Zugriff auf Zeilen und Spalten
- Filtern, Sortieren und Transformieren von Daten
- Umgang mit fehlenden Werten

### Der DataFrame: Die zentrale Datenstruktur

Das Herzstück von Pandas ist der **DataFrame**. Ein DataFrame ist eine zweidimensionale, tabellenartige Datenstruktur mit beschrifteten Zeilen und Spalten. Sie können sich einen DataFrame wie eine Excel-Tabelle oder eine Datenbanktabelle vorstellen:

- Jede **Spalte** hat einen Namen und enthält Daten eines bestimmten Typs (z.B. Zahlen, Texte, Wahrheitswerte)
- Jede **Zeile** repräsentiert einen Datensatz oder Eintrag
- Jede Zeile hat einen **Index** (standardmäßig eine fortlaufende Nummer, kann aber auch benannt werden)

### Praktische Anwendungsfälle

Pandas wird in vielen Bereichen eingesetzt:
- **Wissenschaft**: Analyse von Experimentergebnissen, Verarbeitung von Messdaten
- **Wirtschaft**: Auswertung von Verkaufszahlen, Finanzanalysen
- **Sozialwissenschaften**: Umfrageauswertungen, demografische Analysen
- **Web Analytics**: Auswertung von Nutzerdaten, Klickstatistiken

In diesem Notebook werden Sie die Grundlagen von Pandas kennenlernen. Wir beginnen mit der Installation und dem Import der Bibliothek, erstellen dann erste DataFrames und lernen, wie man auf Daten zugreift und diese manipuliert.

---

+++

## Installation und Import von Pandas

### Installation von Pandas

Bevor Sie Pandas verwenden können, müssen Sie sicherstellen, dass die Bibliothek installiert ist. In den meisten Python-Umgebungen (wie Anaconda) ist Pandas bereits vorinstalliert. Falls Sie beim Ausführen des Import-Befehls eine Fehlermeldung erhalten, können Sie Pandas mit folgendem Befehl installieren:

```python
!pip install pandas
```

Das Ausrufezeichen `!` ermöglicht es, Systembefehle direkt aus einem Jupyter Notebook heraus auszuführen. Der Befehl `pip install` lädt die Bibliothek aus dem Python Package Index (PyPI) herunter und installiert sie.

**Alternative Installation über Anaconda**: Falls Sie die Anaconda-Distribution verwenden, können Sie Bibliotheken auch über den Anaconda Navigator installieren. Eine Anleitung finden Sie [hier](https://docs.anaconda.com/anaconda/navigator/tutorials/manage-packages/).

### Import von Pandas

Nach der Installation müssen Sie Pandas in Ihr Python-Skript oder Notebook importieren. Dies geschieht mit dem `import`-Statement:

```python
import pandas as pd
```

**Erklärung der Syntax**:
- `import pandas`: Lädt die Pandas-Bibliothek
- `as pd`: Erstellt eine Abkürzung (Alias) für die Bibliothek

Die Abkürzung `pd` ist eine Konvention in der Python-Community. Sie ermöglicht es uns, Pandas-Funktionen mit dem kurzen Präfix `pd.` statt dem langen `pandas.` aufzurufen. Dies macht den Code übersichtlicher und ist der etablierte Standard.

**Wichtig**: Sie müssen Pandas in jedem Notebook oder Skript importieren, in dem Sie es verwenden möchten. Der Import ist nur für die aktuelle Python-Sitzung gültig.

---

```{code-cell} ipython3
# Import der Pandas-Bibliothek mit dem Standard-Alias pd
import pandas as pd
```

**Erklärung**: Nach erfolgreicher Ausführung dieser Zelle steht Ihnen Pandas zur Verfügung. Es erscheint keine Ausgabe - das ist normal. Bei einem Fehler würden Sie eine Meldung wie `ModuleNotFoundError: No module named 'pandas'` erhalten. In diesem Fall müssen Sie Pandas zunächst installieren.

---

+++

## Erstellen eines DataFrame: Grundlagen

### Was ist ein DataFrame?

Ein DataFrame ist die zentrale Datenstruktur in Pandas. Es handelt sich um eine zweidimensionale Tabelle mit beschrifteten Zeilen und Spalten. Im Gegensatz zu einer einfachen Liste von Listen (die Sie bereits kennen) bietet ein DataFrame folgende Vorteile:

- **Spaltennamen**: Jede Spalte hat einen aussagekräftigen Namen (statt nur einem numerischen Index)
- **Verschiedene Datentypen**: Jede Spalte kann einen anderen Datentyp haben (z.B. eine Spalte mit Zahlen, eine mit Text)
- **Zeilenindizes**: Zeilen können über numerische Indizes oder Namen angesprochen werden
- **Integrierte Funktionen**: Pandas bietet viele Funktionen zum Filtern, Sortieren und Analysieren

### Syntax und Semantik

**Syntax**:
```python
df = pd.DataFrame(data=daten, columns=spaltennamen)
```

**Semantik**:
- `pd.DataFrame()`: Funktion zum Erstellen eines DataFrame-Objekts
- `data`: Die eigentlichen Daten (kann eine Liste von Listen, ein Dictionary oder andere Strukturen sein)
- `columns`: Eine Liste mit den Namen der Spalten (optional, aber empfohlen)
- `df`: Die Variable, in der das DataFrame-Objekt gespeichert wird

**Wichtige Konzepte**:
- Die Daten werden als **Liste von Listen** übergeben, wobei jede innere Liste eine Zeile repräsentiert
- Die Spaltennamen müssen in der gleichen Reihenfolge wie die Datenspalten angegeben werden
- Pandas erstellt automatisch einen numerischen Index (0, 1, 2, ...) für die Zeilen

---

+++

### Beispiel 1: DataFrame aus einer Liste von Listen erstellen

Wir erstellen einen einfachen DataFrame mit Informationen über drei Personen (Name, Alter, Stadt).

**Was wird gemacht**: Wir definieren die Daten als Liste von Listen und übergeben sie zusammen mit den Spaltennamen an die `pd.DataFrame()`-Funktion.

```{code-cell} ipython3
# Erstellen eines DataFrame aus einer Liste von Listen
daten = [
    ["Anna", 28, "Berlin"],
    ["Ben", 32, "Hamburg"],
    ["Chris", 25, "München"]
]

df = pd.DataFrame(data=daten, columns=["Name", "Alter", "Stadt"])

print(df)
```

**Erwartete Ausgabe**:
```
    Name  Alter     Stadt
0   Anna     28    Berlin
1    Ben     32   Hamburg
2  Chris     25   München
```

**Erklärung der Ausgabe**:
- Die **erste Spalte** (ohne Überschrift) zeigt den automatisch erstellten Index (0, 1, 2)
- Die **Spaltennamen** (Name, Alter, Stadt) werden in der ersten Zeile angezeigt
- Jede **Zeile** enthält die Daten einer Person
- Die Daten sind übersichtlich in Tabellenform dargestellt

**Was ist passiert**:
1. Pandas hat die Liste von Listen in eine Tabellenstruktur umgewandelt
2. Die Spaltennamen wurden den drei Datenspalten zugeordnet
3. Jede innere Liste wurde zu einer Zeile im DataFrame
4. Ein numerischer Index (0, 1, 2) wurde automatisch erstellt

---

+++

### Angeleitete Übung 1.1: Ersten eigenen DataFrame erstellen

**Aufgabe**: Erstellen Sie einen DataFrame mit Informationen über drei Tiere in einem Zoo. Der DataFrame soll folgende Spalten haben: "Tier", "Alter", "Zoo".

**Daten**:
- Panda, 4 Jahre, Zoo Berlin
- Löwe, 3 Jahre, Zoo Köln
- Maus, 2 Jahre, Zoo München

**Hinweise**:
- Schritt 1: Importieren Sie pandas (falls noch nicht geschehen)
- Schritt 2: Erstellen Sie eine Liste von Listen mit den Tierdaten
- Schritt 3: Erstellen Sie den DataFrame mit `pd.DataFrame()` und geben Sie die Spaltennamen an
- Schritt 4: Geben Sie den DataFrame mit `print()` aus

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
# Pandas importieren
import pandas as pd

# Daten als Liste von Listen
tiere_daten = [
    ["Panda", 4, "Zoo Berlin"],
    ["Löwe", 3, "Zoo Köln"],
    ["Maus", 2, "Zoo München"]
]

# DataFrame erstellen
df_tiere = pd.DataFrame(data=tiere_daten, columns=["Tier", "Alter", "Zoo"])

# Ausgabe
print(df_tiere)
```

**Erklärung**: 
- Wir haben die Tierdaten in einer Liste von Listen organisiert, wobei jede innere Liste ein Tier repräsentiert
- Die `pd.DataFrame()`-Funktion wandelt diese Struktur in eine übersichtliche Tabelle um
- Die Spaltennamen werden in der gleichen Reihenfolge angegeben wie die Daten in den Listen
</details>

---

+++

### Beispiel 2: DataFrame aus einem Dictionary erstellen

Eine alternative und oft praktischere Methode ist die Erstellung eines DataFrame aus einem Dictionary. Bei dieser Methode sind die Spaltennamen die Dictionary-Schlüssel und die Werte sind Listen mit den Spaltendaten.

**Was wird gemacht**: Wir erstellen ein Dictionary, bei dem jeder Schlüssel einen Spaltennamen repräsentiert und der zugehörige Wert eine Liste mit den Daten dieser Spalte ist.

```{code-cell} ipython3
# Erstellen eines DataFrame aus einem Dictionary
daten_dict = {
    "Name": ["Tom", "Nick", "Julia"],
    "Alter": [20, 21, 19],
    "Stadt": ["Frankfurt", "Dresden", "Bonn"]
}

df = pd.DataFrame(daten_dict)

print(df)
```

**Erwartete Ausgabe**:
```
    Name  Alter      Stadt
0    Tom     20  Frankfurt
1   Nick     21    Dresden
2  Julia     19       Bonn
```

**Erklärung**:
- Bei der Dictionary-Methode sind die **Schlüssel automatisch die Spaltennamen**
- Die **Werte** (Listen) enthalten die Daten für die jeweilige Spalte
- Alle Listen müssen die **gleiche Länge** haben (hier: jeweils 3 Elemente)
- Diese Methode ist oft übersichtlicher, da die Zuordnung von Spaltenname und Daten explizit ist

**Vorteile der Dictionary-Methode**:
- Die Struktur ist spaltenorientiert, was der natürlichen Organisation von Tabellen entspricht
- Die Spaltennamen müssen nicht separat angegeben werden
- Es ist einfacher zu erkennen, welche Daten zu welcher Spalte gehören

---

+++

### Angeleitete Übung 1.2: DataFrame aus Dictionary erstellen

**Aufgabe**: Erstellen Sie einen DataFrame mit Informationen über Autos. Verwenden Sie die Dictionary-Methode.

**Daten**:
- Marken: VW, BMW, Mercedes, Audi
- Modelle: Golf, 3er, C-Klasse, A4
- Preise: 20000, 30000, 40000, 35000

**Hinweise**:
- Erstellen Sie ein Dictionary mit den Schlüsseln "Marke", "Modell", "Preis"
- Jeder Wert im Dictionary sollte eine Liste mit den entsprechenden Daten sein
- Übergeben Sie das Dictionary an `pd.DataFrame()`

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
import pandas as pd

# Dictionary mit Auto-Daten
autos = {
    "Marke": ["VW", "BMW", "Mercedes", "Audi"],
    "Modell": ["Golf", "3er", "C-Klasse", "A4"],
    "Preis": [20000, 30000, 40000, 35000]
}

# DataFrame aus Dictionary erstellen
df_autos = pd.DataFrame(autos)

# Ausgabe
print(df_autos)
```

**Erklärung**: 
- Bei der Dictionary-Methode wird jeder Schlüssel automatisch zu einem Spaltennamen
- Die Listen als Werte müssen alle die gleiche Länge haben (hier: 4 Elemente)
- Diese Methode ist besonders übersichtlich, wenn Sie spaltenweise denken
</details>

---

+++

## DataFrame aus CSV-Datei erstellen

### Was ist eine CSV-Datei?

CSV steht für "Comma-Separated Values" (kommagetrennte Werte). Eine CSV-Datei ist ein Textdateiformat, in dem Daten in Tabellenform gespeichert werden. Jede Zeile der Datei repräsentiert eine Tabellenzeile, und die Werte innerhalb einer Zeile werden durch Kommas (oder andere Trennzeichen wie Semikolons) getrennt.

CSV-Dateien sind ein sehr häufiges Format für den Datenaustausch, da sie:
- Einfach zu lesen und zu schreiben sind
- Von vielen Programmen unterstützt werden (Excel, Google Sheets, Datenbanken)
- Plattformunabhängig sind
- Wenig Speicherplatz benötigen

### Laden einer CSV-Datei mit Pandas

**Syntax**:
```python
df = pd.read_csv('dateiname.csv')
```

**Semantik**:
- `pd.read_csv()`: Pandas-Funktion zum Einlesen von CSV-Dateien
- `'dateiname.csv'`: Pfad zur CSV-Datei (kann relativ oder absolut sein)
- Die Funktion liest die Datei automatisch ein und erstellt daraus einen DataFrame
- Die erste Zeile der CSV-Datei wird standardmäßig als Spaltenüberschrift interpretiert

**Wichtige Parameter** (optional):
- `sep=';'`: Trennzeichen angeben (falls nicht Komma)
- `encoding='utf-8'`: Zeichenkodierung festlegen (wichtig für Umlaute)
- `header=0`: Zeile mit Spaltenüberschriften (0 = erste Zeile)

---

+++

### Beispiel 3: CSV-Datei einlesen

**Was wird gemacht**: Wir lesen eine CSV-Datei namens "file.csv" ein und speichern die Daten in einem DataFrame.

**Voraussetzung**: Die Datei "file.csv" muss im gleichen Verzeichnis wie dieses Notebook liegen (oder Sie geben einen absoluten Pfad an).

```{code-cell} ipython3
# DataFrame aus CSV-Datei erstellen
df = pd.read_csv('file.csv')

# Ausgabe des DataFrame
print(df)
```

**Erwartete Ausgabe** (abhängig vom Inhalt der Datei):
```
  StudentIn   Note  Bestanden
0       Max    1.3       True
1      Lena    1.3       True
2     Peter    4.0       True
3      Hans    5.0      False
```

**Was ist passiert**:
1. Pandas hat die CSV-Datei geöffnet und gelesen
2. Die erste Zeile wurde als Spaltenüberschriften interpretiert
3. Alle weiteren Zeilen wurden als Datenzeilen eingelesen
4. Pandas hat automatisch die Datentypen erkannt (Text, Zahlen, Wahrheitswerte)
5. Ein DataFrame wurde erstellt und in der Variable `df` gespeichert

**Fehlerbehandlung**: Falls die Datei nicht gefunden wird, erhalten Sie einen `FileNotFoundError`. Überprüfen Sie in diesem Fall:
- Liegt die Datei im richtigen Verzeichnis?
- Ist der Dateiname korrekt geschrieben (Groß-/Kleinschreibung beachten)?
- Haben Sie den richtigen Pfad angegeben?

---

+++

## Datenzugriff: Spalten auswählen

### Zugriff auf einzelne Spalten

Nachdem Sie einen DataFrame erstellt haben, möchten Sie häufig auf bestimmte Spalten zugreifen. Pandas bietet hierfür eine einfache Syntax.

**Syntax**:
```python
spalte = df['Spaltenname']
```

**Semantik**:
- `df['Spaltenname']`: Greift auf die Spalte mit dem Namen "Spaltenname" zu
- Das Ergebnis ist ein sogenanntes **Series-Objekt** (eine eindimensionale Datenstruktur in Pandas)
- Die Series enthält alle Werte der ausgewählten Spalte zusammen mit dem Index

**Wichtig**: Der Spaltenname muss **exakt** so geschrieben werden, wie er im DataFrame definiert ist (Groß-/Kleinschreibung beachten).

---

+++

### Beispiel 4: Spalte auswählen

**Was wird gemacht**: Wir erstellen einen DataFrame und greifen dann auf die Spalte "Alter" zu.

```{code-cell} ipython3
# DataFrame erstellen
daten = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Alter": [23, 25, 22],
    "Stadt": ["Berlin", "Köln", "München"]
}
df = pd.DataFrame(daten)

# Zugriff auf die Spalte 'Alter'
alter_spalte = df['Alter']

print("Gesamter DataFrame:")
print(df)
print("\nNur die Alter-Spalte:")
print(alter_spalte)
```

**Erwartete Ausgabe**:
```
Gesamter DataFrame:
      Name  Alter    Stadt
0    Alice     23   Berlin
1      Bob     25     Köln
2  Charlie     22  München

Nur die Alter-Spalte:
0    23
1    25
2    22
Name: Alter, dtype: int64
```

**Erklärung**:
- Die ausgewählte Spalte wird als **Series** zurückgegeben
- Die Zahlen links (0, 1, 2) sind die **Indizes** aus dem ursprünglichen DataFrame
- `Name: Alter` zeigt den Namen der Serie (entspricht dem Spaltennamen)
- `dtype: int64` zeigt den Datentyp der Werte (64-Bit-Integer)

---

+++

## Datenzugriff mit `loc` und `iloc`

### Unterschied zwischen `loc` und `iloc`

Pandas bietet zwei mächtige Methoden für den Datenzugriff: `loc` und `iloc`. Beide ermöglichen den Zugriff auf Zeilen und Spalten, unterscheiden sich aber in der Art, wie Sie die gewünschten Daten adressieren:

- **`loc`**: Label-basierter Zugriff (über Namen/Beschriftungen)
- **`iloc`**: Integer-basierter Zugriff (über numerische Positionen)

### `loc`: Label-basierter Zugriff

**Syntax**:
```python
# Zugriff auf eine Zeile
zeile = df.loc[zeilenlabel]

# Zugriff auf eine spezifische Zelle
wert = df.loc[zeilenlabel, 'Spaltenname']
```

**Semantik**:
- `loc` verwendet die **tatsächlichen Beschriftungen** (Labels) der Zeilen und Spalten
- Zeilenlabels sind standardmäßig numerisch (0, 1, 2, ...), können aber auch benannt werden
- Spaltenlabels sind die Spaltennamen
- `loc` ist **inklusive** bei Bereichsangaben (beide Grenzen werden eingeschlossen)

### `iloc`: Integer-basierter Zugriff

**Syntax**:
```python
# Zugriff auf eine Zeile
zeile = df.iloc[zeilenindex]

# Zugriff auf eine spezifische Zelle
wert = df.iloc[zeilenindex, spaltenindex]
```

**Semantik**:
- `iloc` verwendet **numerische Positionen** (wie bei Listen)
- Die Zählung beginnt immer bei 0
- Funktioniert unabhängig von den tatsächlichen Labels
- `iloc` ist **exklusiv** bei Bereichsangaben (wie beim Slicing von Listen)

---

+++

### Beispiel 5: Unterschied zwischen `loc` und `iloc`

**Was wird gemacht**: Wir erstellen einen DataFrame mit **benannten Zeilen-Indizes** und zeigen den Unterschied zwischen `loc` und `iloc`.

```{code-cell} ipython3
# DataFrame mit benannten Indizes erstellen
df = pd.DataFrame(
    data={
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    },
    index=["eins", "zwei", "drei"]  # Benannte Zeilen-Indizes
)

print("Gesamter DataFrame:")
print(df)
```

**Erwartete Ausgabe**:
```
Gesamter DataFrame:
      A  B  C
eins  1  4  7
zwei  2  5  8
drei  3  6  9
```

**Erklärung**: Beachten Sie, dass die Zeilen nicht mehr mit 0, 1, 2 beschriftet sind, sondern mit "eins", "zwei", "drei". Dies ist der **Label-Index**.

---

+++

### Zugriff auf Zeilen mit `loc` (Label-basiert)

```{code-cell} ipython3
# Zugriff auf die Zeile mit dem Label "eins" mit loc
print("Zeile mit Label 'eins' (mit loc):")
print(df.loc["eins"])
```

**Erwartete Ausgabe**:
```
Zeile mit Label 'eins' (mit loc):
A    1
B    4
C    7
Name: eins, dtype: int64
```

**Erklärung**: `loc` verwendet den **Namen** des Zeilen-Index ("eins"), um auf die Zeile zuzugreifen.

---

+++

### Zugriff auf Zeilen mit `iloc` (Position-basiert)

```{code-cell} ipython3
# Zugriff auf die erste Zeile (Position 0) mit iloc
print("Erste Zeile (Position 0) (mit iloc):")
print(df.iloc[0])
```

**Erwartete Ausgabe**:
```
Erste Zeile (Position 0) (mit iloc):
A    1
B    4
C    7
Name: eins, dtype: int64
```

**Erklärung**: `iloc` verwendet die **numerische Position** (0 = erste Zeile), unabhängig vom Label. Das Ergebnis ist in diesem Fall identisch mit `loc["eins"]`, da beide auf dieselbe Zeile zugreifen.

**Wichtiger Unterschied**: Wenn Sie `df.loc[0]` versuchen würden, würde dies einen Fehler verursachen, da es keine Zeile mit dem Label "0" gibt (nur "eins", "zwei", "drei").

---

+++

### Zugriff auf spezifische Zellen

**Was wird gemacht**: Wir greifen auf einzelne Zellwerte zu, indem wir sowohl Zeile als auch Spalte angeben.

```{code-cell} ipython3
# Zugriff auf Zelle in Zeile "eins", Spalte "A" mit loc
print("Wert in Zeile 'eins', Spalte 'A' (mit loc):")
print(df.loc["eins", "A"])

print("\nWert in Zeile 0, Spalte 0 (mit iloc):")
print(df.iloc[0, 0])
```

**Erwartete Ausgabe**:
```
Wert in Zeile 'eins', Spalte 'A' (mit loc):
1

Wert in Zeile 0, Spalte 0 (mit iloc):
1
```

**Erklärung**:
- `df.loc["eins", "A"]`: Verwendet Label für Zeile ("eins") und Spalte ("A")
- `df.iloc[0, 0]`: Verwendet numerische Positionen (0 = erste Zeile, 0 = erste Spalte)
- Beide Zugriffe liefern den gleichen Wert (1), da sie auf dieselbe Zelle zugreifen

---

+++

### Angeleitete Übung 2.1: Datenzugriff üben

**Aufgabe**: Erstellen Sie einen DataFrame mit Namen und Alter von fünf Personen. Greifen Sie dann auf verschiedene Daten zu.

**Hinweise**:
- Erstellen Sie einen DataFrame mit den Spalten "Name" und "Alter" und fünf Zeilen
- Greifen Sie auf die gesamte Spalte "Alter" zu und geben Sie sie aus
- Greifen Sie mit `loc` auf die dritte Zeile zu (Index 2)
- Greifen Sie mit `iloc` auf das Alter der dritten Person zu (Zeile 2, Spalte 1)

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
import pandas as pd

# DataFrame erstellen
daten = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Erik"],
    "Alter": [23, 25, 22, 24, 26]
}
df = pd.DataFrame(daten)

# Zugriff auf Spalte 'Alter'
print("Alter aller Personen:")
print(df['Alter'])

# Zugriff auf dritte Zeile mit loc (Index 2)
print("\nDritte Person (mit loc):")
print(df.loc[2])

# Zugriff auf Alter der dritten Person mit iloc
print("\nAlter der dritten Person (mit iloc):")
print(df.iloc[2, 1])  # Zeile 2, Spalte 1 (Alter)
```

**Erklärung**: 
- `df['Alter']` liefert alle Werte der Spalte "Alter" als Series
- `df.loc[2]` greift auf die Zeile mit Index 2 zu (in diesem Fall die dritte Zeile, da der Index bei 0 beginnt)
- `df.iloc[2, 1]` greift auf Zeile 2 (dritte Zeile), Spalte 1 (zweite Spalte = "Alter") zu
</details>

---

+++

## Manipulation von DataFrames: Spalten hinzufügen, entfernen und modifizieren

### Spalten hinzufügen

Eine der häufigsten Operationen ist das Hinzufügen neuer Spalten zu einem DataFrame. Dies kann durch einfache Zuweisung geschehen.

**Syntax**:
```python
df['Neue_Spalte'] = werte
```

**Semantik**:
- `'Neue_Spalte'`: Name der neuen Spalte (kann frei gewählt werden)
- `werte`: Kann eine Liste, eine einzelne Konstante oder eine Berechnung basierend auf anderen Spalten sein
- Falls eine Liste übergeben wird, muss sie die gleiche Länge wie der DataFrame haben
- Falls ein einzelner Wert übergeben wird, wird dieser für alle Zeilen verwendet

---

+++

### Beispiel 6: Spalte mit Liste hinzufügen

**Was wird gemacht**: Wir erstellen einen DataFrame und fügen eine neue Spalte hinzu, indem wir eine Liste von Werten übergeben.

```{code-cell} ipython3
# DataFrame erstellen
df = pd.DataFrame({
    'Name': ['Anna', 'Ben', 'Chris'],
    'Alter': [25, 30, 35]
})

print("Ursprünglicher DataFrame:")
print(df)

# Neue Spalte 'Stadt' hinzufügen
df['Stadt'] = ['Berlin', 'Hamburg', 'München']

print("\nDataFrame nach Hinzufügen der Spalte 'Stadt':")
print(df)
```

**Erwartete Ausgabe**:
```
Ursprünglicher DataFrame:
    Name  Alter
0   Anna     25
1    Ben     30
2  Chris     35

DataFrame nach Hinzufügen der Spalte 'Stadt':
    Name  Alter     Stadt
0   Anna     25    Berlin
1    Ben     30   Hamburg
2  Chris     35   München
```

**Was ist passiert**: 
- Eine neue Spalte namens "Stadt" wurde erstellt
- Die Werte aus der Liste wurden den Zeilen zugeordnet (erstes Element zur ersten Zeile, usw.)
- Die Spalte wurde rechts an den DataFrame angehängt

---

+++

### Beispiel 7: Spalte durch Berechnung hinzufügen

**Was wird gemacht**: Wir erstellen eine neue Spalte, indem wir eine **Berechnung** auf Basis einer existierenden Spalte durchführen.

```{code-cell} ipython3
# DataFrame erstellen
df = pd.DataFrame({
    'Name': ['Anna', 'Ben', 'Chris'],
    'Alter': [25, 30, 35]
})

# Neue Spalte 'Alter_in_Monaten' durch Berechnung hinzufügen
df['Alter_in_Monaten'] = df['Alter'] * 12

print(df)
```

**Erwartete Ausgabe**:
```
    Name  Alter  Alter_in_Monaten
0   Anna     25               300
1    Ben     30               360
2  Chris     35               420
```

**Erklärung**: 
- `df['Alter'] * 12` multipliziert **jeden Wert** in der Spalte "Alter" mit 12
- Das Ergebnis wird als neue Spalte "Alter_in_Monaten" gespeichert
- Diese Operation wird **elementweise** durchgeführt (jede Zelle einzeln)

---

+++

### Spalten entfernen

**Syntax**:
```python
df = df.drop('Spaltenname', axis=1)
```

**Semantik**:
- `drop()`: Methode zum Entfernen von Zeilen oder Spalten
- `'Spaltenname'`: Name der zu entfernenden Spalte
- `axis=1`: Gibt an, dass eine **Spalte** entfernt werden soll (axis=0 würde Zeilen entfernen)
- Die Methode gibt einen **neuen** DataFrame zurück; das Original bleibt unverändert

**Alternative mit `inplace`**:
```python
df.drop('Spaltenname', axis=1, inplace=True)
```
- `inplace=True`: Verändert den DataFrame **direkt**, ohne einen neuen zu erstellen
- In diesem Fall ist keine Neuzuweisung (`df = ...`) nötig

---

+++

### Beispiel 8: Spalte entfernen

**Was wird gemacht**: Wir entfernen eine Spalte aus einem DataFrame.

```{code-cell} ipython3
# DataFrame erstellen
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

print("Ursprünglicher DataFrame:")
print(df)

# Spalte 'C' entfernen (mit Neuzuweisung)
df = df.drop('C', axis=1)

print("\nDataFrame nach Entfernen von Spalte 'C':")
print(df)
```

**Erwartete Ausgabe**:
```
Ursprünglicher DataFrame:
   A  B  C
0  1  4  7
1  2  5  8
2  3  6  9

DataFrame nach Entfernen von Spalte 'C':
   A  B
0  1  4
1  2  5
2  3  6
```

**Was ist passiert**: Die Spalte 'C' wurde aus dem DataFrame entfernt. Die Spalten 'A' und 'B' bleiben erhalten.

---

+++

### Beispiel 9: Spalte mit `inplace` entfernen

**Was wird gemacht**: Wir entfernen eine Spalte direkt (ohne Neuzuweisung) mit dem Parameter `inplace=True`.

```{code-cell} ipython3
# DataFrame erstellen
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

print("Ursprünglicher DataFrame:")
print(df)

# Spalte 'B' direkt entfernen (mit inplace=True)
df.drop('B', axis=1, inplace=True)

print("\nDataFrame nach Entfernen von Spalte 'B':")
print(df)
```

**Erwartete Ausgabe**:
```
Ursprünglicher DataFrame:
   A  B  C
0  1  4  7
1  2  5  8
2  3  6  9

DataFrame nach Entfernen von Spalte 'B':
   A  C
0  1  7
1  2  8
2  3  9
```

**Erklärung**: Mit `inplace=True` wird der DataFrame **direkt verändert**. Eine Neuzuweisung mit `df = ...` ist nicht nötig.

---

+++

### Spalten modifizieren

Bestehende Spalten können durch **Überschreiben** modifiziert werden.

**Syntax**:
```python
df['Spaltenname'] = neue_werte
```

**Semantik**:
- Die Werte der Spalte werden durch die neuen Werte ersetzt
- `neue_werte` kann eine Liste, eine Berechnung oder ein einzelner Wert sein

---

+++

### Beispiel 10: Spalte modifizieren

**Was wird gemacht**: Wir verdoppeln alle Werte in der Spalte 'A'.

```{code-cell} ipython3
# DataFrame erstellen
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

print("Ursprünglicher DataFrame:")
print(df)

# Spalte 'A' modifizieren (alle Werte verdoppeln)
df['A'] = df['A'] * 2

print("\nDataFrame nach Modifikation von Spalte 'A':")
print(df)
```

**Erwartete Ausgabe**:
```
Ursprünglicher DataFrame:
   A  B  C
0  1  4  7
1  2  5  8
2  3  6  9

DataFrame nach Modifikation von Spalte 'A':
   A  B  C
0  2  4  7
1  4  5  8
2  6  6  9
```

**Erklärung**: Jeder Wert in Spalte 'A' wurde mit 2 multipliziert. Die ursprünglichen Werte wurden überschrieben.

---

+++

### Angeleitete Übung 3.1: Spalten manipulieren

**Aufgabe**: Erstellen Sie einen DataFrame mit Namen und Alter (in Jahren) von fünf Personen. Fügen Sie eine Spalte "Alter_in_Monaten" hinzu und entfernen Sie dann die Spalte "Alter".

**Hinweise**:
- Erstellen Sie zunächst einen DataFrame mit den Spalten "Name" und "Alter"
- Fügen Sie die Spalte "Alter_in_Monaten" durch Multiplikation von "Alter" mit 12 hinzu
- Entfernen Sie die Spalte "Alter" mit der `drop()`-Methode
- Geben Sie den finalen DataFrame aus

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
import pandas as pd

# DataFrame erstellen
df = pd.DataFrame({
    'Name': ['Anna', 'Ben', 'Chris', 'Diana', 'Erik'],
    'Alter': [25, 30, 35, 40, 45]
})

# Spalte 'Alter_in_Monaten' hinzufügen
df['Alter_in_Monaten'] = df['Alter'] * 12

# Spalte 'Alter' entfernen
df = df.drop('Alter', axis=1)

# Ausgabe
print(df)
```

**Erklärung**: 
- Die neue Spalte wird durch eine elementweise Multiplikation erstellt
- `drop('Alter', axis=1)` entfernt die Spalte "Alter" (axis=1 bedeutet Spalte)
- Der resultierende DataFrame enthält nur noch "Name" und "Alter_in_Monaten"
</details>

---

+++

### Zeilen entfernen

**Syntax**:
```python
df = df.drop(index, axis=0)
```

**Semantik**:
- `index`: Der Index der zu entfernenden Zeile (z.B. 0, 1, 2 oder ein benannter Index)
- `axis=0`: Gibt an, dass eine **Zeile** entfernt werden soll (im Gegensatz zu axis=1 für Spalten)
- Auch hier kann `inplace=True` verwendet werden

---

+++

### Beispiel 11: Zeile entfernen

**Was wird gemacht**: Wir entfernen die dritte Zeile (Index 2) aus einem DataFrame.

```{code-cell} ipython3
# DataFrame erstellen
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

print("Ursprünglicher DataFrame:")
print(df)

# Zeile mit Index 2 entfernen
df = df.drop(2, axis=0)

print("\nDataFrame nach Entfernen der Zeile mit Index 2:")
print(df)
```

**Erwartete Ausgabe**:
```
Ursprünglicher DataFrame:
   A  B  C
0  1  4  7
1  2  5  8
2  3  6  9

DataFrame nach Entfernen der Zeile mit Index 2:
   A  B  C
0  1  4  7
1  2  5  8
```

**Erklärung**: Die Zeile mit Index 2 (dritte Zeile) wurde entfernt. Die Indizes der verbleibenden Zeilen bleiben unverändert (0 und 1).

---

+++

## Filtern von Daten

### Bedingte Selektion

Eine der mächtigsten Funktionen von Pandas ist die Möglichkeit, Daten basierend auf Bedingungen zu filtern. Dies ermöglicht es Ihnen, nur die Zeilen auszuwählen, die bestimmte Kriterien erfüllen.

**Syntax**:
```python
df_gefiltert = df[bedingung]
```

**Semantik**:
- `bedingung`: Ein boolescher Ausdruck, der für jede Zeile ausgewertet wird
- Nur Zeilen, bei denen die Bedingung `True` ergibt, werden in den neuen DataFrame aufgenommen
- Die Bedingung verwendet typischerweise Vergleichsoperatoren (>, <, ==, !=, >=, <=)

**Häufige Bedingungen**:
- `df['Alter'] > 25`: Alle Zeilen, bei denen Alter größer als 25 ist
- `df['Stadt'] == 'Berlin'`: Alle Zeilen, bei denen Stadt gleich 'Berlin' ist
- `df['Preis'] <= 20`: Alle Zeilen, bei denen Preis kleiner oder gleich 20 ist

---

+++

### Beispiel 12: Daten nach Bedingung filtern

**Was wird gemacht**: Wir erstellen einen DataFrame mit Personen und filtern alle heraus, die älter als 25 Jahre sind.

```{code-cell} ipython3
# DataFrame erstellen
daten = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Alter": [23, 32, 22],
    "Stadt": ["Berlin", "Köln", "München"]
}
df = pd.DataFrame(daten)

print("Ursprünglicher DataFrame:")
print(df)

# Filtern: Nur Personen älter als 25
df_gefiltert = df[df['Alter'] > 25]

print("\nGefiltert (Alter > 25):")
print(df_gefiltert)
```

**Erwartete Ausgabe**:
```
Ursprünglicher DataFrame:
      Name  Alter    Stadt
0    Alice     23   Berlin
1      Bob     32     Köln
2  Charlie     22  München

Gefiltert (Alter > 25):
  Name  Alter Stadt
1  Bob     32  Köln
```

**Was ist passiert**:
1. Die Bedingung `df['Alter'] > 25` wurde für jede Zeile ausgewertet
2. Für Alice (23) und Charlie (22) ergab die Bedingung `False`
3. Für Bob (32) ergab die Bedingung `True`
4. Nur die Zeile mit Bob wurde in den gefilterten DataFrame übernommen
5. Der **Index** der ursprünglichen Zeile (1) bleibt erhalten

**Technischer Hintergrund**: `df['Alter'] > 25` erzeugt zunächst eine Serie von Wahrheitswerten (True/False) für jede Zeile. Diese Serie wird dann als Filter verwendet.

---

+++

### Angeleitete Übung 4.1: Daten filtern

**Aufgabe**: Erstellen Sie einen DataFrame mit Produkten und Preisen. Filtern Sie alle Produkte heraus, deren Preis höher als 20 ist.

**Daten**:
- Produkte: Apfel, Banane, Kirsche, Dattel, Birne
- Preise: 10, 15, 25, 30, 22

**Hinweise**:
- Erstellen Sie einen DataFrame mit den Spalten "Produkt" und "Preis"
- Filtern Sie mit der Bedingung `df['Preis'] > 20`
- Geben Sie den gefilterten DataFrame aus

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
import pandas as pd

# DataFrame erstellen
df = pd.DataFrame({
    'Produkt': ['Apfel', 'Banane', 'Kirsche', 'Dattel', 'Birne'],
    'Preis': [10, 15, 25, 30, 22]
})

# Filtern: Preis > 20
df_gefiltert = df[df['Preis'] > 20]

# Ausgabe
print(df_gefiltert)
```

**Erklärung**: 
- Die Bedingung `df['Preis'] > 20` wird für jede Zeile ausgewertet
- Nur Zeilen mit Preis > 20 (Kirsche: 25, Dattel: 30, Birne: 22) werden im Ergebnis angezeigt
- Die ursprünglichen Indizes (2, 3, 4) bleiben erhalten
</details>

---

+++

## Sortieren von Daten

### Sortierung nach Spalten

Das Sortieren von Daten ermöglicht es, die Zeilen eines DataFrame in einer bestimmten Reihenfolge anzuzeigen. Dies ist besonders nützlich, um Daten nach Größe, alphabetisch oder chronologisch zu ordnen.

**Syntax**:
```python
df_sortiert = df.sort_values('Spaltenname')
```

**Semantik**:
- `sort_values()`: Methode zum Sortieren eines DataFrame
- `'Spaltenname'`: Die Spalte, nach der sortiert werden soll
- Standardmäßig wird **aufsteigend** sortiert (kleinste Werte zuerst)
- Mit `ascending=False` kann **absteigend** sortiert werden (größte Werte zuerst)

**Wichtig**: Die Methode gibt einen neuen, sortierten DataFrame zurück. Das Original bleibt unverändert (außer bei Verwendung von `inplace=True`).

---

+++

### Beispiel 13: Aufsteigend sortieren

**Was wird gemacht**: Wir sortieren einen DataFrame nach der Spalte "Alter" in aufsteigender Reihenfolge.

```{code-cell} ipython3
# DataFrame erstellen
daten = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Alter": [23, 32, 22],
    "Stadt": ["Berlin", "Köln", "München"]
}
df = pd.DataFrame(daten)

print("Ursprünglicher DataFrame:")
print(df)

# Sortieren nach Alter (aufsteigend)
df_sortiert = df.sort_values('Alter')

print("\nSortiert nach Alter (aufsteigend):")
print(df_sortiert)
```

**Erwartete Ausgabe**:
```
Ursprünglicher DataFrame:
      Name  Alter    Stadt
0    Alice     23   Berlin
1      Bob     32     Köln
2  Charlie     22  München

Sortiert nach Alter (aufsteigend):
      Name  Alter    Stadt
2  Charlie     22  München
0    Alice     23   Berlin
1      Bob     32     Köln
```

**Erklärung**:
- Die Zeilen wurden nach dem Alter geordnet: 22 → 23 → 32
- Die **ursprünglichen Indizes** (2, 0, 1) bleiben an den Zeilen "haften"
- Alle Daten einer Zeile bleiben zusammen (Name, Alter und Stadt werden gemeinsam verschoben)

---

+++

### Beispiel 14: Absteigend sortieren

**Was wird gemacht**: Wir sortieren denselben DataFrame nach "Alter" in absteigender Reihenfolge (höchstes Alter zuerst).

```{code-cell} ipython3
# Sortieren nach Alter (absteigend)
df_sortiert_absteigend = df.sort_values('Alter', ascending=False)

print("Sortiert nach Alter (absteigend):")
print(df_sortiert_absteigend)
```

**Erwartete Ausgabe**:
```
Sortiert nach Alter (absteigend):
      Name  Alter    Stadt
1      Bob     32     Köln
0    Alice     23   Berlin
2  Charlie     22  München
```

**Erklärung**: Mit `ascending=False` wird die Sortierrichtung umgekehrt. Die Zeilen sind nun nach abnehmendem Alter geordnet: 32 → 23 → 22.

---

+++

### Angeleitete Übung 4.2: Filtern und Sortieren kombinieren

**Aufgabe**: Erstellen Sie einen DataFrame mit Produkten und Preisen. Filtern Sie alle Produkte mit einem Preis über 20 und sortieren Sie das Ergebnis absteigend nach Preis.

**Daten**:
- Produkte: Apfel, Banane, Kirsche, Dattel, Birne
- Preise: 10, 15, 25, 30, 22

**Hinweise**:
- Erstellen Sie den DataFrame
- Filtern Sie mit `df[df['Preis'] > 20]`
- Sortieren Sie das Ergebnis mit `.sort_values('Preis', ascending=False)`
- Sie können beide Operationen verketten: `df[bedingung].sort_values(...)`

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
import pandas as pd

# DataFrame erstellen
df = pd.DataFrame({
    'Produkt': ['Apfel', 'Banane', 'Kirsche', 'Dattel', 'Birne'],
    'Preis': [10, 15, 25, 30, 22]
})

# Filtern und sortieren (beide Operationen verkettet)
df_ergebnis = df[df['Preis'] > 20].sort_values('Preis', ascending=False)

# Ausgabe
print(df_ergebnis)
```

**Erklärung**: 
- Zuerst werden die Zeilen mit Preis > 20 gefiltert (Kirsche, Dattel, Birne)
- Dann wird das gefilterte Ergebnis absteigend nach Preis sortiert (30 → 25 → 22)
- Die Verkettung von Operationen ist eine häufige Praxis in Pandas
</details>

---

+++

## Abschlussübungen

Die folgenden Aufgaben testen Ihr Verständnis der in diesem Notebook erlernten Konzepte. Bearbeiten Sie die Aufgaben selbstständig und vergleichen Sie Ihre Lösung anschließend mit den Musterlösungen am Ende des Notebooks.

---

### Teil 1: Grundlegende Anwendung

**Kompetenzstufe**: Anwenden

Diese Aufgaben testen die direkte Anwendung der erlernten Konzepte.

---

+++

**Aufgabe 1**: Erstellen Sie einen DataFrame aus folgendem Dictionary und geben Sie ihn aus:

```python
buecher = {
    'Titel': ['Python Basics', 'Data Science', 'Web Development', 'Machine Learning'],
    'Autor': ['Mueller', 'Schmidt', 'Weber', 'Fischer'],
    'Seiten': [320, 450, 280, 520]
}
```

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 1
```

---

**Aufgabe 2**: Verwenden Sie den DataFrame aus Aufgabe 1. Greifen Sie auf folgende Daten zu:
- Die gesamte Spalte "Seiten"
- Die zweite Zeile mit `iloc`
- Die Anzahl der Seiten des Buches "Data Science" (verwenden Sie `loc` mit Index 1 und Spaltenname "Seiten")

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 2
```

---

### Teil 2: Transfer und Problemlösung

**Kompetenzstufe**: Analysieren & Erschaffen

Diese Aufgaben erfordern die Kombination mehrerer Konzepte und eigenständiges Problemlösen.

---

+++

**Aufgabe 3**: Sie haben folgende Daten über Mitarbeiter eines Unternehmens:

```python
mitarbeiter_daten = [
    ['Anna', 'IT', 3500],
    ['Ben', 'Marketing', 3200],
    ['Chris', 'IT', 4000],
    ['Diana', 'Vertrieb', 2800],
    ['Erik', 'IT', 3800]
]
```

Führen Sie folgende Schritte aus:
1. Erstellen Sie einen DataFrame mit den Spalten "Name", "Abteilung", "Gehalt"
2. Fügen Sie eine Spalte "Jahresgehalt" hinzu (Gehalt * 12)
3. Filtern Sie alle Mitarbeiter aus der IT-Abteilung
4. Sortieren Sie das Ergebnis nach Gehalt (absteigend)
5. Geben Sie das finale Ergebnis aus

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 3
```

---

**Aufgabe 4**: Erstellen Sie einen DataFrame mit Informationen über fünf Städte (Name, Einwohner in Tausend, Land). Führen Sie folgende Operationen durch:

1. Erstellen Sie den DataFrame (wählen Sie selbst Städte und Daten)
2. Fügen Sie eine Spalte "Kategorie" hinzu, die basierend auf der Einwohnerzahl folgende Werte enthält:
   - "Großstadt" wenn Einwohner >= 1000
   - "Mittelstadt" wenn Einwohner < 1000
   
   **Hinweis**: Sie können dies mit einer Schleife lösen oder die Werte manuell als Liste angeben
3. Filtern Sie alle Großstädte
4. Geben Sie das Ergebnis aus

**Tipp**: Für Schritt 2 können Sie eine Schleife verwenden oder die Kategorien als Liste definieren.

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 4
```

---

## Zusammenfassung

In diesem Notebook haben Sie die Grundlagen der Arbeit mit Pandas DataFrames kennengelernt:

| Konzept | Syntax | Anwendungsfall |
|---------|--------|----------------|
| **Pandas importieren** | `import pandas as pd` | Bibliothek verfügbar machen |
| **DataFrame erstellen (Liste)** | `pd.DataFrame(data=liste, columns=namen)` | Daten aus Listen organisieren |
| **DataFrame erstellen (Dict)** | `pd.DataFrame(dictionary)` | Spaltenweise Daten definieren |
| **CSV-Datei einlesen** | `pd.read_csv('datei.csv')` | Externe Daten laden |
| **Spalte auswählen** | `df['Spaltenname']` | Auf einzelne Spalte zugreifen |
| **Zeile mit loc** | `df.loc[label]` | Label-basierter Zeilenzugriff |
| **Zeile mit iloc** | `df.iloc[position]` | Positions-basierter Zeilenzugriff |
| **Zelle mit loc** | `df.loc[label, 'Spalte']` | Spezifischen Wert abrufen (Label) |
| **Zelle mit iloc** | `df.iloc[zeile, spalte]` | Spezifischen Wert abrufen (Position) |
| **Spalte hinzufügen** | `df['Neue'] = werte` | Neue Daten ergänzen |
| **Spalte entfernen** | `df.drop('Spalte', axis=1)` | Unnötige Spalten löschen |
| **Spalte modifizieren** | `df['Spalte'] = neue_werte` | Bestehende Daten ändern |
| **Zeile entfernen** | `df.drop(index, axis=0)` | Zeile löschen |
| **Filtern** | `df[bedingung]` | Daten nach Kriterien auswählen |
| **Sortieren** | `df.sort_values('Spalte')` | Daten ordnen |

**Zentrale Erkenntnisse**:

1. **DataFrames sind tabellarische Datenstrukturen**: Sie bieten eine effiziente Möglichkeit, strukturierte Daten zu speichern und zu manipulieren, ähnlich wie Excel-Tabellen, aber mit wesentlich mehr Funktionalität.

2. **Flexibler Datenzugriff mit `loc` und `iloc`**: `loc` arbeitet mit Beschriftungen (Labels), während `iloc` mit numerischen Positionen arbeitet. Beide Methoden ermöglichen präzisen Zugriff auf Zeilen, Spalten und einzelne Zellen.

3. **Datenmanipulation ist grundlegend**: Das Hinzufügen, Entfernen und Modifizieren von Spalten ist essentiell für die Datenaufbereitung. Pandas macht diese Operationen einfach und intuitiv.

4. **Filtern und Sortieren für Datenanalyse**: Diese Operationen ermöglichen es, relevante Informationen aus großen Datensätzen zu extrahieren und übersichtlich darzustellen.

**Nächste Schritte**: Im folgenden Notebook (17 - Pandas Statistik) werden Sie lernen, wie Sie mit Pandas statistische Analysen durchführen können. Sie werden Funktionen kennenlernen, um Durchschnittswerte, Mediane und andere statistische Kennzahlen zu berechnen.

---

+++

## Musterlösungen

<details>
<summary>Lösung zu Aufgabe 1</summary>

```python
import pandas as pd

# Dictionary mit Buchdaten
buecher = {
    'Titel': ['Python Basics', 'Data Science', 'Web Development', 'Machine Learning'],
    'Autor': ['Mueller', 'Schmidt', 'Weber', 'Fischer'],
    'Seiten': [320, 450, 280, 520]
}

# DataFrame erstellen
df_buecher = pd.DataFrame(buecher)

# Ausgabe
print(df_buecher)
```

**Erklärung**:
- Das Dictionary wird direkt an `pd.DataFrame()` übergeben
- Die Schlüssel des Dictionaries werden automatisch zu Spaltennamen
- Die Listen als Werte bilden die Spalteninhalte

**Häufige Fehler**:
- Vergessen, `import pandas as pd` auszuführen
- Listen unterschiedlicher Länge verwenden (führt zu einem Fehler)
</details>

<details>
<summary>Lösung zu Aufgabe 2</summary>

```python
import pandas as pd

# DataFrame aus Aufgabe 1
buecher = {
    'Titel': ['Python Basics', 'Data Science', 'Web Development', 'Machine Learning'],
    'Autor': ['Mueller', 'Schmidt', 'Weber', 'Fischer'],
    'Seiten': [320, 450, 280, 520]
}
df_buecher = pd.DataFrame(buecher)

# Zugriff auf Spalte "Seiten"
print("Spalte 'Seiten':")
print(df_buecher['Seiten'])

# Zugriff auf zweite Zeile mit iloc
print("\nZweite Zeile (iloc):")
print(df_buecher.iloc[1])

# Seitenzahl von "Data Science" (Index 1, Spalte "Seiten")
print("\nSeiten von 'Data Science':")
print(df_buecher.loc[1, 'Seiten'])
```

**Erklärung**:
- `df_buecher['Seiten']` gibt die gesamte Spalte als Series zurück
- `df_buecher.iloc[1]` greift auf die zweite Zeile zu (Index 1, da bei 0 gestartet wird)
- `df_buecher.loc[1, 'Seiten']` kombiniert Label-Zugriff für Zeile und Spalte

**Häufige Fehler**:
- `loc` und `iloc` verwechseln
- Bei `loc[1, 'Seiten']` die Anführungszeichen um den Spaltennamen vergessen
</details>

<details>
<summary>Lösung zu Aufgabe 3</summary>

```python
import pandas as pd

# Daten als Liste von Listen
mitarbeiter_daten = [
    ['Anna', 'IT', 3500],
    ['Ben', 'Marketing', 3200],
    ['Chris', 'IT', 4000],
    ['Diana', 'Vertrieb', 2800],
    ['Erik', 'IT', 3800]
]

# 1. DataFrame erstellen
df = pd.DataFrame(data=mitarbeiter_daten, columns=['Name', 'Abteilung', 'Gehalt'])

# 2. Spalte "Jahresgehalt" hinzufügen
df['Jahresgehalt'] = df['Gehalt'] * 12

# 3. IT-Mitarbeiter filtern
df_it = df[df['Abteilung'] == 'IT']

# 4. Nach Gehalt absteigend sortieren
df_ergebnis = df_it.sort_values('Gehalt', ascending=False)

# 5. Ausgabe
print(df_ergebnis)
```

**Erklärung**:
- Schritt 1: DataFrame aus Liste von Listen mit benannten Spalten
- Schritt 2: Neue Spalte wird durch Multiplikation einer bestehenden Spalte erstellt
- Schritt 3: Filter mit Gleichheitsbedingung (`==`) für Strings
- Schritt 4: Sortierung in absteigender Reihenfolge
- Die Operationen können auch verkettet werden: `df[df['Abteilung'] == 'IT'].sort_values('Gehalt', ascending=False)`

**Alternative Lösung (verkettete Operationen)**:
```python
# Schritte 3 und 4 in einer Zeile
df_ergebnis = df[df['Abteilung'] == 'IT'].sort_values('Gehalt', ascending=False)
```
</details>

<details>
<summary>Lösung zu Aufgabe 4</summary>

```python
import pandas as pd

# 1. DataFrame erstellen
staedte = {
    'Name': ['Berlin', 'München', 'Hamburg', 'Köln', 'Frankfurt'],
    'Einwohner': [3645, 1472, 1841, 1086, 753],
    'Land': ['Deutschland', 'Deutschland', 'Deutschland', 'Deutschland', 'Deutschland']
}
df = pd.DataFrame(staedte)

# 2. Spalte "Kategorie" hinzufügen
# Lösung 1: Mit Schleife
kategorien = []
for einwohner in df['Einwohner']:
    if einwohner >= 1000:
        kategorien.append('Großstadt')
    else:
        kategorien.append('Mittelstadt')

df['Kategorie'] = kategorien

# 3. Großstädte filtern
df_grossstaedte = df[df['Kategorie'] == 'Großstadt']

# 4. Ausgabe
print(df_grossstaedte)
```

**Alternative Lösung ohne Schleife**:
```python
# Kategorien manuell als Liste definieren (wenn man die Werte kennt)
df['Kategorie'] = ['Großstadt', 'Großstadt', 'Großstadt', 'Großstadt', 'Mittelstadt']
```

**Erklärung**:
- Die Schleife iteriert über alle Einwohnerzahlen
- Für jede Zahl wird geprüft, ob sie >= 1000 ist
- Basierend auf der Bedingung wird "Großstadt" oder "Mittelstadt" zur Liste hinzugefügt
- Die Liste wird dann als neue Spalte hinzugefügt
- Das Filtern erfolgt wie gewohnt mit einer Bedingung

**Hinweis**: In einem fortgeschrittenen Pandas-Kurs würden Sie lernen, dies mit der `apply()`-Methode oder mit `numpy.where()` eleganter zu lösen. Für dieses Notebook ist die Schleifen-Lösung angemessen, da sie nur bereits bekannte Konzepte verwendet.
</details>
