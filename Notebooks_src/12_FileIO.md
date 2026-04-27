---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
kernelspec:
  display_name: base
  language: python
  name: python3
---

# 12 - Datei-Ein- und Ausgabe: Arbeiten mit Files in Python

## Lernziele

Nach Abschluss dieses Notebooks können Sie:
- Das Konzept von Dateien (Files) im Kontext von Eingabe- und Ausgabeoperationen erklären
- Dateien mit der `open()`-Funktion in verschiedenen Modi öffnen und schließen
- Text mit den Methoden `write()` und `read()` in Dateien schreiben und aus Dateien lesen
- Absolute und relative Pfade unterscheiden und korrekt anwenden
- Das `with`-Statement für sicheres Arbeiten mit Dateien verwenden
- Fehler bei Dateioperationen mit `try-except` behandeln

**Kompetenzstufen**: Verstehen, Anwenden, Analysieren

---

## Voraussetzungen

Für dieses Notebook sollten Sie folgende Konzepte beherrschen:
- Variablen und einfache Datentypen (int, float, str, bool) (Notebook 04, 05)
- Funktionen mit Parametern und Rückgabewerten (Notebook 07)
- Programmverzweigungen mit if-else (Notebook 09)
- Fehlerbehandlung mit try-except-finally (Notebook 11)

Falls Sie diese Konzepte noch nicht sicher beherrschen, wiederholen Sie bitte die entsprechenden Notebooks.

---

+++

## Dateien im Kontext von Ein- und Ausgabeoperationen

### Einführung und Motivation

Bisher haben Sie mit Daten gearbeitet, die während der Programmausführung im Arbeitsspeicher existieren. Sobald ein Programm beendet wird, gehen diese Daten verloren. In der Praxis ist es jedoch häufig notwendig, Daten dauerhaft zu speichern oder aus externen Quellen zu laden. Genau hier kommen Dateien ins Spiel.

In der Informatik folgen Computer dem EVA-Prinzip: **E**ingabe, **V**erarbeitung, **A**usgabe. Dateien spielen sowohl bei der Eingabe als auch bei der Ausgabe eine zentrale Rolle. Wenn wir Daten aus einer Datei laden, handelt es sich um eine Eingabeoperation. Wenn wir Daten in eine Datei schreiben, führen wir eine Ausgabeoperation durch.

Python stellt leistungsfähige Werkzeuge bereit, um mit Dateien zu arbeiten. Alle Dateioperationen in Python laufen über sogenannte `file`-Objekte, die eine Verbindung zwischen Ihrem Programm und einer physischen Datei auf einem Speichermedium herstellen.

+++

### Das Konzept eines File-Objekts

Ein `file`-Objekt in Python können Sie sich konzeptionell wie ein Magnetband vorstellen, das sequenziell beschrieben und gelesen werden kann. Es ist in Felder der Länge 1 Byte aufgeteilt, wobei jedes Feld eine 8-Bit-Einheit aufnehmen kann. Die aktuelle Position beim Lesen oder Schreiben wird durch einen Cursor markiert.

Ein `file`-Objekt ist immer mit einer externen Datei verbunden, die auf einem Datenträger (Festplatte, USB-Stick etc.) unter einem Dateinamen physisch gespeichert ist. Der Zugriff auf diese Datei wird vom Betriebssystem kontrolliert, das sicherstellt, dass nicht mehrere Programme gleichzeitig unkontrolliert auf dieselbe Datei zugreifen.

+++

### Typische Ein- und Ausgabeoperationen

**Eingabeoperationen**:
- Eingabe von Zeichen über die Tastatur (bereits bekannt: `input()`-Funktion)
- Lesen von Dateien, die auf Speichermedien gespeichert sind

**Ausgabeoperationen**:
- Wiedergabe von Texten und Zahlen auf dem Bildschirm (bereits bekannt: `print()`-Funktion)
- Schreiben von Daten in Dateien, die auf Speichermedien gespeichert werden

Das Laden und Speichern von Dateien sind Ein- und Ausgabeoperationen, da Daten zwischen dem Programm und externen Speichermedien ausgetauscht werden.

+++

---

## Dateien öffnen und schließen

### Syntax und Semantik

**Syntax**:
```python
file_objekt = open(dateiname, modus)
file_objekt.close()
```

**Semantik**:
- **`open()`**: Funktion zum Öffnen einer Datei. Gibt ein `file`-Objekt zurück.
- **`dateiname`**: String, der den Namen (und optional den Pfad) der Datei angibt
- **`modus`**: String, der angibt, wie die Datei geöffnet werden soll
  - `'r'`: Lesemodus (read) - Datei muss existieren
  - `'w'`: Schreibmodus (write) - Datei wird erstellt oder überschrieben
  - `'a'`: Anhängemodus (append) - Daten werden am Ende angefügt
- **`close()`**: Methode zum Schließen der Datei. Wichtig, um Daten zu speichern und Ressourcen freizugeben.

+++

### Beispiel 1: Eine Datei erstellen

Das folgende Beispiel zeigt, wie Sie eine neue Datei erstellen. Durch das Öffnen im Schreibmodus (`'w'`) wird die Datei angelegt, falls sie noch nicht existiert.

```{code-cell} ipython3
# Eine neue Datei erstellen

file = open("meine_erste_datei.txt", "w")
file.close()

print("Datei wurde erfolgreich erstellt.")
```

**Erklärung**: 

Mit `open("meine_erste_datei.txt", "w")` wird eine Datei namens `meine_erste_datei.txt` im Schreibmodus geöffnet. Python erstellt diese Datei im aktuellen Arbeitsverzeichnis. Das zurückgegebene `file`-Objekt wird in der Variablen `file` gespeichert.

Die Methode `close()` schließt die Datei wieder. Dies ist wichtig, um sicherzustellen, dass alle Änderungen gespeichert werden und Systemressourcen freigegeben werden. Eine nicht geschlossene Datei kann zu Datenverlust führen.

+++

### Angeleitete Übung 1.1

**Aufgabe**: Erstellen Sie eine Datei namens `test.txt` im Schreibmodus und schließen Sie diese wieder.

**Hinweise**:
- Schritt 1: Verwenden Sie die `open()`-Funktion mit dem Dateinamen `"test.txt"` und dem Modus `"w"`
- Schritt 2: Speichern Sie das zurückgegebene File-Objekt in einer Variablen
- Schritt 3: Schließen Sie die Datei mit der `close()`-Methode

```{code-cell} ipython3
# Ihr Code hier
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Datei erstellen und schließen
datei = open("test.txt", "w")
datei.close()
```

**Erklärung**: Die `open()`-Funktion erstellt eine neue Datei namens `test.txt` im Schreibmodus. Das File-Objekt wird in der Variablen `datei` gespeichert. Anschließend wird die Datei mit `close()` geschlossen, um die Ressourcen freizugeben.
</details>

+++

### Beispiel 2: Die verschiedenen Dateimodi

Python bietet verschiedene Modi zum Öffnen von Dateien. Das folgende Beispiel demonstriert die Unterschiede:

```{code-cell} ipython3
# Modus 'w' - Schreibmodus (überschreibt existierende Datei)
file_w = open("demo_modi.txt", "w")
file_w.write("Das ist die erste Zeile!")
file_w.close()
print("Datei im Schreibmodus erstellt.")

# Modus 'a' - Anhängemodus (fügt am Ende hinzu)
file_a = open("demo_modi.txt", "a")
file_a.write("HAllo Test")
file_a.close()
print("Datei im Anhängemodus geöffnet.")
```

**Erklärung**:

Der Modus `'w'` erstellt eine neue Datei oder überschreibt eine existierende Datei vollständig. Der Modus `'a'` (append) öffnet eine Datei zum Anhängen. Neue Daten werden am Ende der Datei hinzugefügt, ohne den existierenden Inhalt zu löschen. Der Lesemodus `'r'` wird im nächsten Abschnitt behandelt.

+++

### Angeleitete Übung 1.2

**Aufgabe**: Erstellen Sie eine Datei namens `notizen.txt` im Anhängemodus und schließen Sie diese wieder.

**Hinweise**:
- Verwenden Sie den Modus `"a"` statt `"w"`
- Vergessen Sie nicht, die Datei zu schließen

```{code-cell} ipython3
# Ihr Code hier
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Datei im Anhängemodus öffnen
notizen = open("notizen.txt", "a")
notizen.close()
```

**Erklärung**: Der Modus `"a"` öffnet die Datei im Anhängemodus. Falls die Datei noch nicht existiert, wird sie erstellt. Falls sie bereits existiert, bleiben die vorhandenen Daten erhalten, und neue Daten würden am Ende hinzugefügt.
</details>

+++

---

## Text in Dateien schreiben

### Syntax und Semantik

**Syntax**:
```python
file_objekt.write(zeichenkette)
```

**Semantik**:
- **`write()`**: Methode eines File-Objekts zum Schreiben von Daten
- **`zeichenkette`**: Der Text (String), der in die Datei geschrieben werden soll
- **Rückgabewert**: Anzahl der geschriebenen Zeichen
- **Wichtig**: Die Datei muss im Schreibmodus (`'w'`) oder Anhängemodus (`'a'`) geöffnet sein

+++

### Beispiel 1: Einfachen Text schreiben

Das folgende Beispiel zeigt, wie Sie einen einfachen Text in eine Datei schreiben:

```{code-cell} ipython3
# Text in Datei schreiben
datei = open("gruesse.txt", "w")
datei.write("Hallo, dies ist ein Test!")
datei.close()

print("Text wurde in die Datei geschrieben.")
```

**Erklärung**:

Die Datei wird im Schreibmodus geöffnet. Die `write()`-Methode schreibt den String `"Hallo, dies ist ein Test!"` in die Datei. Erst durch den Aufruf von `close()` wird sichergestellt, dass die Daten tatsächlich auf das Speichermedium geschrieben werden. Ohne `close()` könnten die Daten verloren gehen.

+++

### Angeleitete Übung 2.1

**Aufgabe**: Erstellen Sie eine Datei namens `mein_text.txt` und schreiben Sie den Text "Python macht Spaß!" hinein.

**Hinweise**:
- Schritt 1: Öffnen Sie die Datei im Schreibmodus
- Schritt 2: Verwenden Sie die `write()`-Methode, um den Text zu schreiben
- Schritt 3: Schließen Sie die Datei

```{code-cell} ipython3
# Ihr Code hier

data = open("mein_text.txt", "w")
data.write("Das ist ein Text!")
data.close()
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Text in Datei schreiben
datei = open("mein_text.txt", "w")
datei.write("Python macht Spaß!")
datei.close()
```

**Erklärung**: Die Datei wird im Schreibmodus geöffnet, der angegebene Text wird mit `write()` geschrieben, und die Datei wird mit `close()` geschlossen.
</details>

+++

### Beispiel 2: Mehrere Zeilen schreiben

Wenn Sie mehrere Zeilen schreiben möchten, müssen Sie das Zeilenumbruch-Zeichen `\n` explizit einfügen:

```{code-cell} ipython3
# Mehrere Zeilen in Datei schreiben
datei = open("mehrzeilig.txt", "w")
datei.write("Erste Zeile\n")
datei.write("Zweite Zeile\n")
datei.write("Dritte Zeile\n")
datei.close()

print("Mehrere Zeilen wurden geschrieben.")
```

**Erklärung**:

Das Zeichen `\n` ist ein Steuerzeichen, das einen Zeilenumbruch repräsentiert. Ohne `\n` würde der gesamte Text in einer einzigen Zeile stehen. Python fügt `\n` nicht automatisch hinzu, daher müssen Sie es explizit angeben.

+++

### Angeleitete Übung 2.2

**Aufgabe**: Erstellen Sie eine Datei namens `einkaufsliste.txt` und schreiben Sie drei Artikel (jeweils in einer neuen Zeile): "Milch", "Brot", "Eier".

**Hinweise**:
- Vergessen Sie nicht das `\n` am Ende jeder Zeile
- Sie können `write()` mehrmals aufrufen oder die drei Zeilen in einem String kombinieren

```{code-cell} ipython3
# Ihr Code hier
data = open("mein_text.txt", "a")
data.write("\n")
data.write("Das ist noch mehr text\n")
data.close()
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Einkaufsliste schreiben
datei = open("einkaufsliste.txt", "w")
datei.write("Milch\n")
datei.write("Brot\n")
datei.write("Eier\n")
datei.close()
```

**Erklärung**: Jeder Artikel wird mit einem Zeilenumbruch (`\n`) geschrieben, sodass die drei Artikel untereinander in der Datei stehen.

**Alternative Lösung**:
```python
# Alle Zeilen in einem String
datei = open("einkaufsliste.txt", "w")
datei.write("Milch\nBrot\nEier\n")
datei.close()
```
</details>

+++

---

## Text aus Dateien lesen

### Syntax und Semantik

**Syntax**:
```python
inhalt = file_objekt.read()
```

**Semantik**:
- **`read()`**: Methode eines File-Objekts zum Lesen von Daten
- **Rückgabewert**: String mit dem gesamten Inhalt der Datei
- **Wichtig**: Die Datei muss im Lesemodus (`'r'`) geöffnet sein
- **Wichtig**: Die Datei muss existieren, sonst tritt ein Fehler auf

+++

### Beispiel 1: Eine Datei lesen

Das folgende Beispiel zeigt, wie Sie den Inhalt einer zuvor erstellten Datei lesen können:

```{code-cell} ipython3
# Zunächst eine Datei erstellen mit Inhalt
datei = open("lesebeispiel.txt", "w")
datei.write("Dies ist ein Beispieltext.\n")
datei.write("Er besteht aus mehreren Zeilen.")
datei.close()

# Jetzt die Datei lesen
datei = open("lesebeispiel.txt", "r")
inhalt = datei.read()
datei.close()

print("Gelesener Inhalt:")
print(inhalt)
```

**Erklärung**:

Zunächst wird eine Datei erstellt und mit Text gefüllt. Anschließend wird dieselbe Datei im Lesemodus (`'r'`) geöffnet. Die `read()`-Methode liest den gesamten Inhalt der Datei und gibt ihn als String zurück. Dieser wird in der Variablen `inhalt` gespeichert und kann dann weiterverarbeitet werden.

+++

### Angeleitete Übung 3.1

**Aufgabe**: Lesen Sie den Inhalt der zuvor erstellten Datei `mein_text.txt` und geben Sie ihn mit `print()` aus.

**Hinweise**:
- Schritt 1: Öffnen Sie die Datei im Lesemodus (`"r"`)
- Schritt 2: Verwenden Sie die `read()`-Methode, um den Inhalt zu lesen
- Schritt 3: Speichern Sie den Inhalt in einer Variablen
- Schritt 4: Schließen Sie die Datei
- Schritt 5: Geben Sie den Inhalt mit `print()` aus

```{code-cell} ipython3
# Ihr Code hier
datei = open("mein_text.txt", "r")
inhalt = datei.read()
datei.close()

print(inhalt)
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Datei lesen und Inhalt ausgeben
datei = open("mein_text.txt", "r")
inhalt = datei.read()
datei.close()
print(inhalt)
```

**Erklärung**: Die Datei wird im Lesemodus geöffnet, der Inhalt mit `read()` gelesen, die Datei geschlossen und der Inhalt ausgegeben.
</details>

+++

### Beispiel 2: Datei lesen und verarbeiten

Oft möchten Sie den gelesenen Inhalt weiterverarbeiten. Das folgende Beispiel zeigt, wie Sie den Text modifizieren können:

```{code-cell} ipython3
# Datei lesen
datei = open("lesebeispiel.txt", "r")
inhalt = datei.read()
datei.close()

# Inhalt in Großbuchstaben umwandeln
inhalt_gross = inhalt.upper()
print("Original:")
print(inhalt)
print("\nIn Großbuchstaben:")
print(inhalt_gross)
```

**Erklärung**:

Nach dem Lesen ist `inhalt` ein normaler String, auf den Sie alle bekannten String-Methoden anwenden können. Hier wird die Methode `upper()` verwendet, um den Text in Großbuchstaben umzuwandeln.

+++

### Angeleitete Übung 3.2

**Aufgabe**: Lesen Sie die Datei `einkaufsliste.txt`, zählen Sie die Anzahl der Zeilen und geben Sie diese Anzahl aus.

**Hinweise**:
- Lesen Sie zunächst den gesamten Inhalt
- Verwenden Sie die `count()`-Methode von Strings, um die Anzahl der `\n`-Zeichen zu zählen
- Geben Sie das Ergebnis aus

```{code-cell} ipython3
datei = open("mein_text.txt")
inhalt = datei.read()
datei.close()
anzahl = inhalt.upper().count("TEXT")
print(anzahl)
print(inhalt.upper())
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Datei lesen und Zeilen zählen
datei = open("einkaufsliste.txt", "r")
inhalt = datei.read()
datei.close()

anzahl_zeilen = inhalt.count("\n")
print("Anzahl der Zeilen:", anzahl_zeilen)
```

**Erklärung**: Die `count()`-Methode zählt, wie oft das Zeichen `\n` im String vorkommt. Dies entspricht der Anzahl der Zeilen in der Datei.
</details>

+++

---

## Pfade: Absolut und relativ

### Einführung und Motivation

Bisher haben wir Dateien im aktuellen Arbeitsverzeichnis erstellt und geöffnet, indem wir nur den Dateinamen angegeben haben. In der Praxis befinden sich Dateien jedoch oft in verschiedenen Verzeichnissen (Ordnern). Um auf solche Dateien zuzugreifen, benötigen Sie Kenntnisse über Pfade.

Ein **Pfad** ist eine Zeichenkette, die den Ort einer Datei oder eines Verzeichnisses im Dateisystem angibt. Es gibt zwei Arten von Pfaden: absolute und relative Pfade.

+++

### Absolute Pfade

Ein **absoluter Pfad** gibt den vollständigen Pfad zu einer Datei an, beginnend von der Wurzel (Root) des Dateisystems. Er ist unabhängig vom aktuellen Arbeitsverzeichnis und bleibt immer gleich.

**Beispiele für absolute Pfade**:
- **Unix/Mac**: `/home/benutzer/dokumente/datei.txt`
- **Windows**: `C:\Benutzer\Dokumente\datei.txt`

**Wichtig**: Unter Windows müssen Sie entweder doppelte Backslashes (`\\`) verwenden oder einen sogenannten "Raw String" mit dem Präfix `r` verwenden:

```python
# Windows-Pfad mit doppelten Backslashes
pfad1 = "C:\\Benutzer\\Dokumente\\datei.txt"

# Windows-Pfad als Raw String
pfad2 = r"C:\Benutzer\Dokumente\datei.txt"
```

+++

### Relative Pfade

Ein **relativer Pfad** gibt den Pfad zu einer Datei in Bezug auf das aktuelle Arbeitsverzeichnis an. Er ist kürzer, aber abhängig davon, wo sich Ihr Programm gerade befindet.

**Beispiele für relative Pfade**:
- `datei.txt` - Datei im aktuellen Verzeichnis
- `daten/datei.txt` - Datei im Unterverzeichnis `daten`
- `../datei.txt` - Datei im übergeordneten Verzeichnis (ein Verzeichnis höher)

**Spezielle Pfadangaben**:
- `.` - aktuelles Verzeichnis
- `..` - übergeordnetes Verzeichnis

+++

### Beispiel 1: Datei in Unterverzeichnis erstellen

Das folgende Beispiel zeigt, wie Sie einen relativen Pfad verwenden, um eine Datei in einem Unterverzeichnis zu erstellen:

**Hinweis**: Das Verzeichnis muss bereits existieren, sonst tritt ein Fehler auf.

```{code-cell} ipython3
# Datei im aktuellen Verzeichnis erstellen (kein Unterverzeichnis)
datei = open("datei_im_hauptverzeichnis.txt", "w")
datei.write("Diese Datei liegt im Hauptverzeichnis.")
datei.close()

print("Datei wurde erstellt.")
```

**Erklärung**:

Wenn Sie nur einen Dateinamen ohne Pfadangabe verwenden, wird die Datei im aktuellen Arbeitsverzeichnis erstellt. Dies ist ein impliziter relativer Pfad.

+++

### Angeleitete Übung 4.1

**Aufgabe**: Erstellen Sie eine Datei namens `notiz.txt` im aktuellen Verzeichnis und schreiben Sie "Relative Pfade sind praktisch" hinein.

**Hinweise**:
- Verwenden Sie nur den Dateinamen ohne Pfadangabe
- Öffnen Sie die Datei im Schreibmodus
- Schreiben Sie den Text und schließen Sie die Datei

```{code-cell} ipython3
# Ihr Code hier
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Datei mit relativem Pfad erstellen
datei = open("notiz.txt", "w")
datei.write("Relative Pfade sind praktisch")
datei.close()
```

**Erklärung**: Durch Angabe nur des Dateinamens wird die Datei im aktuellen Arbeitsverzeichnis erstellt.
</details>

+++

### Beispiel 2: Vor- und Nachteile von Pfadtypen

**Vorteile relativer Pfade**:
- Kürzere Pfadangaben
- Programme sind portabler (funktionieren auf verschiedenen Systemen)
- Projektordner können verschoben werden, ohne Pfade anzupassen

**Nachteile relativer Pfade**:
- Abhängig vom aktuellen Arbeitsverzeichnis
- Kann zu Verwirrung führen, wenn unklar ist, wo sich das Programm befindet

**Empfehlung**: Für einfache Programme mit wenigen Dateien im selben Verzeichnis sind relative Pfade ausreichend. Für komplexere Projekte mit mehreren Verzeichnissen sollten Sie überlegen, absolute Pfade zu verwenden oder das aktuelle Arbeitsverzeichnis explizit zu setzen.

+++

### Angeleitete Übung 4.2

**Aufgabe**: Öffnen Sie die zuvor erstellte Datei `notiz.txt`, lesen Sie den Inhalt und geben Sie ihn aus.

**Hinweise**:
- Verwenden Sie den relativen Pfad (nur Dateinamen)
- Öffnen Sie im Lesemodus
- Lesen, schließen und ausgeben Sie den Inhalt

```{code-cell} ipython3
# Ihr Code hier
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Datei lesen mit relativem Pfad
datei = open("notiz.txt", "r")
inhalt = datei.read()
datei.close()
print(inhalt)
```

**Erklärung**: Der relative Pfad funktioniert sowohl beim Schreiben als auch beim Lesen von Dateien.
</details>

+++

---

## Sicheres Arbeiten mit Dateien: Das with-Statement

### Einführung und Motivation

Bisher haben Sie Dateien mit `open()` geöffnet und mit `close()` geschlossen. Dies funktioniert, birgt aber Risiken: Wenn während der Verarbeitung ein Fehler auftritt, wird `close()` möglicherweise nie aufgerufen. Die Datei bleibt dann geöffnet, was zu Datenverlust oder Ressourcenproblemen führen kann.

Python bietet mit dem `with`-Statement eine elegantere und sicherere Lösung. Es stellt sicher, dass die Datei automatisch geschlossen wird, auch wenn ein Fehler auftritt.

+++

### Syntax und Semantik

**Syntax**:
```python
with open(dateiname, modus) as file_objekt:
    # Code, der mit der Datei arbeitet
    # Die Datei wird automatisch geschlossen
```

**Semantik**:
- **`with`**: Keyword, das einen Kontext-Manager erstellt
- **`as file_objekt`**: Weist das File-Objekt einer Variablen zu
- **Eingerückter Code**: Wird ausgeführt, während die Datei geöffnet ist
- **Automatisches Schließen**: Die Datei wird am Ende des `with`-Blocks automatisch geschlossen
- **Fehlerbehandlung**: Die Datei wird auch bei Fehlern geschlossen

+++

### Beispiel 1: Schreiben mit with-Statement

Das folgende Beispiel zeigt, wie Sie das `with`-Statement zum Schreiben verwenden:

```{code-cell} ipython3
# Datei schreiben mit with-Statement
with open("mit_with.txt", "w") as datei:
    datei.write("Dies wurde mit dem with-Statement geschrieben.\n")
    datei.write("Die Datei wird automatisch geschlossen.")

# Hier ist die Datei bereits geschlossen
print("Datei wurde geschrieben und automatisch geschlossen.")
```

**Erklärung**:

Das `with`-Statement öffnet die Datei und weist das File-Objekt der Variablen `datei` zu. Der eingerückte Code wird ausgeführt. Sobald der `with`-Block verlassen wird (nach der letzten eingerückten Zeile), wird die Datei automatisch geschlossen. Ein expliziter Aufruf von `close()` ist nicht notwendig.

+++

### Angeleitete Übung 5.1

**Aufgabe**: Verwenden Sie das `with`-Statement, um eine Datei namens `tagebuch.txt` zu erstellen und den Text "Heute habe ich Python gelernt." hineinzuschreiben.

**Hinweise**:
- Schritt 1: Verwenden Sie `with open(...)` mit dem Schreibmodus
- Schritt 2: Schreiben Sie den Text im eingerückten Block
- Schritt 3: Kein `close()` notwendig - geschieht automatisch

```{code-cell} ipython3
# Ihr Code hier
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Schreiben mit with-Statement
with open("tagebuch.txt", "w") as datei:
    datei.write("Heute habe ich Python gelernt.")
```

**Erklärung**: Das `with`-Statement öffnet die Datei, der Text wird geschrieben, und die Datei wird automatisch geschlossen, wenn der eingerückte Block endet.
</details>

+++

### Beispiel 2: Lesen mit with-Statement

Das `with`-Statement funktioniert auch beim Lesen von Dateien:

```{code-cell} ipython3
# Datei lesen mit with-Statement
with open("mit_with.txt", "r") as datei:
    inhalt = datei.read()
    print("Gelesener Inhalt:")
    print(inhalt)

# Datei ist hier bereits geschlossen
print("\nDatei wurde automatisch geschlossen.")
```

**Erklärung**:

Die Datei wird im Lesemodus geöffnet, der Inhalt wird gelesen und ausgegeben. Nach dem `with`-Block ist die Datei automatisch geschlossen. Dies ist die empfohlene Best Practice für das Arbeiten mit Dateien in Python.

+++

### Angeleitete Übung 5.2

**Aufgabe**: Verwenden Sie das `with`-Statement, um die Datei `tagebuch.txt` zu lesen und den Inhalt auszugeben.

**Hinweise**:
- Verwenden Sie `with open(...)` mit dem Lesemodus
- Lesen Sie den Inhalt mit `read()`
- Geben Sie den Inhalt im `with`-Block aus

```{code-cell} ipython3
# Ihr Code hier
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Lesen mit with-Statement
with open("tagebuch.txt", "r") as datei:
    inhalt = datei.read()
    print(inhalt)
```

**Erklärung**: Die Datei wird geöffnet, gelesen, der Inhalt ausgegeben und die Datei automatisch geschlossen.
</details>

+++

---

## Fehlerbehandlung bei Dateioperationen

### Einführung und Motivation

Beim Arbeiten mit Dateien können verschiedene Fehler auftreten:
- Die Datei existiert nicht (beim Lesen)
- Sie haben keine Berechtigung, die Datei zu lesen oder zu schreiben
- Der Speicherplatz ist voll (beim Schreiben)
- Der Pfad ist ungültig

Um zu verhindern, dass Ihr Programm bei solchen Fehlern abstürzt, können Sie die bereits bekannte Fehlerbehandlung mit `try-except` verwenden.

+++

### Syntax und Semantik

**Syntax**:
```python
try:
    # Code, der Fehler verursachen könnte
    with open(dateiname, modus) as file_objekt:
        # Dateioperationen
except FileNotFoundError:
    # Wird ausgeführt, wenn Datei nicht gefunden wurde
```

**Semantik**:
- **`FileNotFoundError`**: Tritt auf, wenn eine Datei nicht existiert (beim Lesen)
- **`PermissionError`**: Tritt auf, wenn keine Berechtigung vorliegt
- **Kombination mit `with`**: Best Practice ist, `with` innerhalb von `try` zu verwenden

+++

### Beispiel 1: Fehlerbehandlung beim Lesen

Das folgende Beispiel zeigt, wie Sie einen `FileNotFoundError` abfangen:

```{code-cell} ipython3
# Versuch, eine nicht existierende Datei zu lesen
try:
    with open("existiert_nicht.txt", "r") as datei:
        inhalt = datei.read()
        print(inhalt)
except FileNotFoundError:
    print("Fehler: Die Datei wurde nicht gefunden.")
```

**Erklärung**:

Der Code im `try`-Block versucht, eine nicht existierende Datei zu öffnen. Python löst einen `FileNotFoundError` aus, der vom `except`-Block abgefangen wird. Anstatt abzustürzen, gibt das Programm eine benutzerfreundliche Fehlermeldung aus und läuft weiter.

+++

### Angeleitete Übung 6.1

**Aufgabe**: Schreiben Sie ein Programm, das versucht, eine Datei namens `geheim.txt` zu lesen. Fangen Sie den `FileNotFoundError` ab und geben Sie die Meldung "Die Datei geheim.txt wurde nicht gefunden" aus.

**Hinweise**:
- Schritt 1: Verwenden Sie `try` und `except FileNotFoundError`
- Schritt 2: Versuchen Sie im `try`-Block, die Datei zu öffnen und zu lesen
- Schritt 3: Geben Sie im `except`-Block eine passende Fehlermeldung aus

```{code-cell} ipython3
# Ihr Code hier
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Fehlerbehandlung beim Lesen
try:
    with open("geheim.txt", "r") as datei:
        inhalt = datei.read()
        print(inhalt)
except FileNotFoundError:
    print("Die Datei geheim.txt wurde nicht gefunden")
```

**Erklärung**: Der `try`-Block versucht, die Datei zu öffnen. Da sie nicht existiert, wird der `except`-Block ausgeführt und eine benutzerfreundliche Meldung ausgegeben.
</details>

+++

### Beispiel 2: Kombination von Fehlerbehandlung und Benutzerinteraktion

Ein praxisnahes Beispiel kombiniert Fehlerbehandlung mit Benutzereingaben:

```{code-cell} ipython3
# Benutzer nach Dateinamen fragen
dateiname = input("Geben Sie den Namen einer Datei ein: ")

try:
    with open(dateiname, "r") as datei:
        inhalt = datei.read()
        print("\nInhalt der Datei:")
        print(inhalt)
except FileNotFoundError:
    print(f"Die Datei '{dateiname}' wurde nicht gefunden.")
```

**Erklärung**:

Dieses Programm fragt den Benutzer nach einem Dateinamen und versucht, diese Datei zu lesen. Falls die Datei nicht existiert, wird eine aussagekräftige Fehlermeldung mit dem eingegebenen Dateinamen ausgegeben. Dies ist ein Beispiel für robuste Programmierung, die auch mit unerwarteten Eingaben umgehen kann.

+++

### Angeleitete Übung 6.2

**Aufgabe**: Erstellen Sie eine Datei `daten.txt` mit beliebigem Inhalt. Schreiben Sie dann ein Programm, das diese Datei liest und den Inhalt ausgibt. Verwenden Sie sowohl das `with`-Statement als auch Fehlerbehandlung.

**Hinweise**:
- Erstellen Sie zunächst die Datei mit dem `with`-Statement
- Lesen Sie dann die Datei mit `try-except` und `with`
- Behandeln Sie den `FileNotFoundError`

```{code-cell} ipython3
# Ihr Code hier
```

<details>
<summary>Lösung anzeigen</summary>

```python
# Datei erstellen
with open("daten.txt", "w") as datei:
    datei.write("Dies sind wichtige Daten.\n")
    datei.write("Zweite Zeile mit mehr Daten.")

# Datei mit Fehlerbehandlung lesen
try:
    with open("daten.txt", "r") as datei:
        inhalt = datei.read()
        print("Gelesene Daten:")
        print(inhalt)
except FileNotFoundError:
    print("Die Datei daten.txt wurde nicht gefunden.")
```

**Erklärung**: Zunächst wird die Datei erstellt und mit Inhalt gefüllt. Anschließend wird sie mit Fehlerbehandlung gelesen. Dies zeigt die Kombination aller erlernten Konzepte: `with`-Statement, Fehlerbehandlung und Dateioperationen.
</details>

+++

---

## Abschlussübungen

Die folgenden Aufgaben testen Ihr Verständnis der in diesem Notebook erlernten Konzepte. Bearbeiten Sie die Aufgaben selbstständig und vergleichen Sie Ihre Lösung anschließend mit den Musterlösungen am Ende des Notebooks.

### Teil 1: Grundlegende Anwendung

**Kompetenzstufe**: Anwenden

Diese Aufgaben testen die direkte Anwendung der erlernten Konzepte.

+++

**Aufgabe 1**: Erstellen Sie eine Datei namens `begruessung.txt` und schreiben Sie folgende drei Zeilen hinein:
- "Guten Morgen!"
- "Wie geht es Ihnen?"
- "Schönen Tag noch!"

Verwenden Sie das `with`-Statement und vergessen Sie nicht die Zeilenumbrüche.

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 1
```

**Aufgabe 2**: Lesen Sie die Datei `begruessung.txt` und geben Sie den Inhalt auf dem Bildschirm aus. Verwenden Sie das `with`-Statement und Fehlerbehandlung.

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 2
```

---

### Teil 2: Transfer und Problemlösung

**Kompetenzstufe**: Analysieren & Erschaffen

Diese Aufgaben erfordern die Kombination mehrerer Konzepte und eigenständiges Problemlösen.

+++

**Aufgabe 3**: Schreiben Sie ein Programm, das eine Datei `zahlen.txt` erstellt und die Zahlen von 1 bis 10 (jeweils in einer eigenen Zeile) hineinschreibt. Lesen Sie anschließend die Datei wieder ein und geben Sie nur die geraden Zahlen aus.

**Hinweis**: Sie müssen die gelesenen Strings in Zahlen umwandeln.

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 3
```

**Aufgabe 4**: Erstellen Sie ein Programm, das eine Datei `original.txt` mit beliebigem Text liest und eine neue Datei `kopie.txt` erstellt, die denselben Inhalt enthält, aber alle Vorkommen des Wortes "Datei" durch "Text" ersetzt.

Verwenden Sie Fehlerbehandlung für den Fall, dass `original.txt` nicht existiert.

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 4
```

---

## Zusammenfassung

In diesem Notebook haben Sie folgende Konzepte kennengelernt:

| Konzept | Syntax | Anwendungsfall |
|---------|--------|----------------|
| Datei öffnen | `open(dateiname, modus)` | Verbindung zu einer Datei herstellen |
| Datei schließen | `file.close()` | Datei speichern und Ressourcen freigeben |
| Text schreiben | `file.write(text)` | Daten in eine Datei schreiben |
| Text lesen | `inhalt = file.read()` | Daten aus einer Datei lesen |
| with-Statement | `with open(...) as file:` | Sicheres Arbeiten mit automatischem Schließen |
| Fehlerbehandlung | `try: ... except FileNotFoundError:` | Robuste Programme bei Dateioperationen |

**Zentrale Erkenntnisse**:
- Dateien ermöglichen die dauerhafte Speicherung von Daten über die Programmausführung hinaus
- Das `with`-Statement ist die empfohlene Best Practice für Dateioperationen, da es automatisches Schließen garantiert
- Fehlerbehandlung mit `try-except` macht Programme robust gegenüber fehlenden oder unzugänglichen Dateien
- Relative Pfade machen Programme portabel, während absolute Pfade eindeutig sind
- Die drei wichtigsten Modi sind: `'r'` (lesen), `'w'` (schreiben/überschreiben), `'a'` (anhängen)

**Nächste Schritte**: Im folgenden Notebook (13 - Algorithmen Grundlagen) werden Sie lernen, wie Algorithmen analysiert und bewertet werden. Dies bildet die Grundlage für effiziente Programmierung.

---

+++

## Musterlösungen

<details>
<summary>Lösung zu Aufgabe 1</summary>

```python
# Datei mit drei Zeilen erstellen
with open("begruessung.txt", "w") as datei:
    datei.write("Guten Morgen!\n")
    datei.write("Wie geht es Ihnen?\n")
    datei.write("Schönen Tag noch!\n")
```

**Erklärung**:
- Die Datei wird mit dem `with`-Statement im Schreibmodus geöffnet
- Jede Zeile wird mit `write()` geschrieben, wobei `\n` für den Zeilenumbruch sorgt
- Die Datei wird automatisch geschlossen, wenn der `with`-Block endet

**Häufige Fehler**:
- Vergessen des `\n` am Ende jeder Zeile - dann stehen alle Texte in einer Zeile
- Verwenden von `print()` statt `write()` - `print()` funktioniert nicht mit File-Objekten
</details>

<details>
<summary>Lösung zu Aufgabe 2</summary>

```python
# Datei lesen mit Fehlerbehandlung
try:
    with open("begruessung.txt", "r") as datei:
        inhalt = datei.read()
        print(inhalt)
except FileNotFoundError:
    print("Die Datei begruessung.txt wurde nicht gefunden.")
```

**Erklärung**:
- Der `try`-Block enthält den Code zum Öffnen und Lesen der Datei
- Das `with`-Statement sorgt für automatisches Schließen
- Falls die Datei nicht existiert, wird der `except`-Block ausgeführt

**Häufige Fehler**:
- Falscher Modus (z.B. `"w"` statt `"r"`) - überschreibt die Datei, statt sie zu lesen
- Fehlerbehandlung außerhalb des `with`-Blocks - dann funktioniert die Fehlerbehandlung nicht richtig
</details>

<details>
<summary>Lösung zu Aufgabe 3</summary>

```python
# Schritt 1: Zahlen in Datei schreiben
with open("zahlen.txt", "w") as datei:
    for zahl in range(1, 11):
        datei.write(str(zahl) + "\n")

# Schritt 2: Datei lesen und nur gerade Zahlen ausgeben
with open("zahlen.txt", "r") as datei:
    inhalt = datei.read()
    
# Zeilen aufteilen und verarbeiten
zeilen = inhalt.split("\n")
print("Gerade Zahlen:")
for zeile in zeilen:
    if zeile != "":  # Leere Zeilen überspringen
        zahl = int(zeile)
        if zahl % 2 == 0:
            print(zahl)
```

**Erklärung**:
- Eine `for`-Schleife mit `range(1, 11)` erzeugt die Zahlen 1 bis 10
- `str(zahl)` konvertiert jede Zahl in einen String, da `write()` nur Strings akzeptiert
- Beim Lesen wird `split("\n")` verwendet, um den Text in einzelne Zeilen aufzuteilen
- Jede Zeile wird mit `int()` zurück in eine Zahl konvertiert
- Der Modulo-Operator `% 2 == 0` prüft, ob eine Zahl gerade ist

**Alternative Ansätze**:
- Sie könnten auch nur gerade Zahlen schreiben: `for zahl in range(2, 11, 2)`
- Die Filterung könnte mit List Comprehension erfolgen: `[int(z) for z in zeilen if z != "" and int(z) % 2 == 0]`
</details>

<details>
<summary>Lösung zu Aufgabe 4</summary>

```python
# Zunächst original.txt erstellen (für Testzwecke)
with open("original.txt", "w") as datei:
    datei.write("Dies ist eine Datei.\n")
    datei.write("Die Datei enthält Text.\n")
    datei.write("Dateien sind nützlich.")

# Jetzt das eigentliche Programm
try:
    # Original-Datei lesen
    with open("original.txt", "r") as datei:
        inhalt = datei.read()
    
    # Text modifizieren
    neuer_inhalt = inhalt.replace("Datei", "Text")
    
    # Neue Datei schreiben
    with open("kopie.txt", "w") as datei:
        datei.write(neuer_inhalt)
    
    print("Datei wurde erfolgreich kopiert und bearbeitet.")
    
except FileNotFoundError:
    print("Fehler: Die Datei original.txt wurde nicht gefunden.")
```

**Erklärung**:
- Die Original-Datei wird zuerst gelesen und der Inhalt in einer Variablen gespeichert
- Die String-Methode `replace()` ersetzt alle Vorkommen von "Datei" durch "Text"
- Der modifizierte Inhalt wird in eine neue Datei geschrieben
- Zwei separate `with`-Blöcke werden verwendet: einer zum Lesen, einer zum Schreiben
- Fehlerbehandlung fängt den Fall ab, dass die Original-Datei nicht existiert

**Häufige Fehler**:
- Versuchen, gleichzeitig zu lesen und zu schreiben in derselben Datei - führt zu Problemen
- Vergessen, den Inhalt in einer Variablen zu speichern, bevor die Datei geschlossen wird
- `replace()` unterscheidet Groß-/Kleinschreibung - "datei" würde nicht ersetzt

**Alternative Ansätze**:
- Sie könnten auch Klein- und Großschreibung berücksichtigen, indem Sie mehrere `replace()`-Aufrufe verwenden
- Für komplexere Ersetzungen könnten reguläre Ausdrücke nützlich sein (aber diese wurden noch nicht eingeführt)
</details>
