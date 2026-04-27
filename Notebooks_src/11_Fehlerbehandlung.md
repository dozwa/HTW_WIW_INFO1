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

# 11 - Fehlerbehandlung: Programme robust machen 🛡️

## Lernziele

Nach Abschluss dieses Notebooks können Sie:
- **Verstehen**, was Exceptions (Ausnahmen) sind und warum sie auftreten
- **Anwenden** von `try-except`-Blöcken zur Fehlerbehandlung
- **Unterscheiden** zwischen verschiedenen Exception-Typen (ValueError, TypeError, ZeroDivisionError)
- **Implementieren** von `finally`-Blöcken für Aufräumarbeiten
- **Erstellen** robuster Programme, die mit ungültigen Eingaben umgehen können

**Kompetenzstufen**: Verstehen, Anwenden

---

## Voraussetzungen

Für dieses Notebook sollten Sie folgende Konzepte beherrschen:
- Variablen und Datentypen (Notebooks 04-05)
- Funktionen definieren und aufrufen (Notebook 07)
- Programmverzweigungen mit if-else (Notebook 09)
- Schleifen mit while und for (Notebook 10)

Falls Sie diese Konzepte noch nicht sicher beherrschen, wiederholen Sie bitte die entsprechenden Notebooks.

---

+++

## Was sind Fehler und warum brauchen wir Fehlerbehandlung?

### Fehler sind unvermeidlich

Beim Programmieren können verschiedene Arten von Fehlern auftreten. Einige Fehler entstehen bereits beim Schreiben des Codes (Syntaxfehler), andere treten erst während der Programmausführung auf (Laufzeitfehler).

Stellen Sie sich vor, Sie schreiben ein Programm, das den Benutzer nach zwei Zahlen fragt und diese dividiert. Was passiert, wenn der Benutzer beim zweiten Wert "null" eingibt? Das Programm würde abstürzen, denn eine Division durch null ist mathematisch nicht definiert. Oder was passiert, wenn der Benutzer statt einer Zahl einen Buchstaben eingibt? Python kann "abc" nicht in eine Zahl umwandeln.

Ohne geeignete Fehlerbehandlung würden solche Situationen dazu führen, dass Ihr Programm mit einer Fehlermeldung abbricht. Der Benutzer wäre verwirrt und könnte das Programm nicht mehr verwenden. **Fehlerbehandlung** ermöglicht es Ihnen, auf solche Situationen vorbereitet zu sein und elegant darauf zu reagieren.

### Was sind Exceptions?

In Python werden Laufzeitfehler als **Exceptions** (Ausnahmen) bezeichnet. Eine Exception ist ein Objekt, das Informationen über einen Fehler enthält, der während der Programmausführung aufgetreten ist. Wenn Python auf einen Fehler stößt, "wirft" es eine Exception.

**Beispiele für typische Exceptions:**
- **ValueError**: Tritt auf, wenn eine Funktion einen Wert mit dem richtigen Typ, aber einem ungültigen Wert erhält (z.B. `int("abc")`)
- **TypeError**: Tritt auf, wenn eine Operation auf einen ungeeigneten Datentyp angewendet wird
- **ZeroDivisionError**: Tritt auf, wenn durch null geteilt wird
- **KeyError**: Tritt auf, wenn ein Dictionary-Schlüssel nicht existiert
- **IndexError**: Tritt auf, wenn auf einen ungültigen Listen-Index zugegriffen wird

### Warum ist Fehlerbehandlung wichtig?

Mit Fehlerbehandlung können Sie:
- **Programme robuster machen**: Ihr Programm stürzt nicht bei jedem unerwarteten Fehler ab
- **Benutzerfreundlichkeit erhöhen**: Statt kryptischer Python-Fehlermeldungen können Sie verständliche Nachrichten ausgeben
- **Kontrolle behalten**: Sie bestimmen, wie Ihr Programm auf Fehler reagiert
- **Debugging erleichtern**: Fehlerinformationen können gezielt ausgegeben werden

### Alltags-Beispiel

Stellen Sie sich einen Geldautomaten vor. Wenn Sie eine ungültige PIN eingeben, stürzt der Automat nicht ab. Stattdessen gibt er eine freundliche Nachricht aus: "Ungültige PIN. Bitte versuchen Sie es erneut." Das ist Fehlerbehandlung in Aktion!

+++

## Fehler ohne Behandlung: Was passiert?

### Beispiel 1: Division durch Null

Schauen wir uns zunächst an, was passiert, wenn ein Fehler **nicht** behandelt wird:

```{code-cell} ipython3
# ACHTUNG: Diese Zelle wird einen Fehler produzieren!
# Das ist beabsichtigt, um zu zeigen, was ohne Fehlerbehandlung passiert

zahl1 = 10
zahl2 = 0

ergebnis = zahl1 / zahl2  # Division durch Null!
print("Das Ergebnis ist:", ergebnis)
```

**Was ist passiert?**

Python hat eine **ZeroDivisionError-Exception** ausgelöst. Die Fehlermeldung sieht ungefähr so aus:
```
ZeroDivisionError: division by zero
```

Das Programm wurde abgebrochen, und die Zeile mit `print()` wurde nie ausgeführt. Für einen Endbenutzer ist diese Fehlermeldung nicht hilfreich.

+++

### Beispiel 2: Ungültige Typkonvertierung

Ein weiteres häufiges Problem tritt auf, wenn Benutzereingaben in Zahlen umgewandelt werden sollen:

```{code-cell} ipython3
# ACHTUNG: Diese Zelle wird einen Fehler produzieren!
# Geben Sie bei der Eingabe absichtlich Text statt einer Zahl ein (z.B. "abc")

eingabe = input("Geben Sie eine Zahl ein: ")
zahl = int(eingabe)  # Was passiert, wenn eingabe = "abc"?
print("Sie haben die Zahl", zahl, "eingegeben.")
```

**Was ist passiert?**

Wenn Sie Text statt einer Zahl eingegeben haben, hat Python eine **ValueError-Exception** ausgelöst:
```
ValueError: invalid literal for int() with base 10: 'abc'
```

Diese Fehlermeldung ist für Programmierer verständlich, für Endbenutzer jedoch nicht. Mit Fehlerbehandlung können wir eine benutzerfreundliche Nachricht ausgeben.

+++

---

## Die try-except-Struktur: Fehler abfangen

### Grundkonzept

Die **try-except-Struktur** ermöglicht es Ihnen, Code auszuführen und auf mögliche Fehler zu reagieren. Das Prinzip ist einfach:

1. **Versuche** (`try`), den Code auszuführen
2. **Falls ein Fehler auftritt**, fange ihn ab und reagiere darauf (`except`)
3. **Falls kein Fehler auftritt**, läuft das Programm normal weiter

### Die Syntax

```python
try:
    # Code, der einen Fehler verursachen könnte
    # Dieser Block wird immer zuerst ausgeführt
except:
    # Code, der ausgeführt wird, wenn ein Fehler auftritt
    # Dieser Block wird nur bei einem Fehler ausgeführt
```

**Wichtige Elemente:**
- **`try:`** - Leitet den Block ein, in dem der "gefährliche" Code steht
- **`except:`** - Definiert, was bei einem Fehler passieren soll
- **Einrückung** - Beide Blöcke müssen korrekt eingerückt sein

### Wie funktioniert es?

Python führt zunächst den Code im `try`-Block aus:
- **Falls alles gut geht**: Der `except`-Block wird übersprungen, das Programm läuft normal weiter
- **Falls ein Fehler auftritt**: Python springt sofort zum `except`-Block und führt diesen aus

Das Programm stürzt nicht ab, sondern reagiert kontrolliert auf den Fehler!

+++

### Beispiel 1: Division durch Null mit Fehlerbehandlung

```{code-cell} ipython3
# Division mit Fehlerbehandlung

zahl1 = 10
zahl2 = 0

try:
    ergebnis = zahl1 / zahl2  # Dieser Code könnte einen Fehler verursachen
    print("Das Ergebnis ist:", ergebnis)
except:
    print("Fehler: Division durch Null ist nicht erlaubt!")

print("Das Programm läuft weiter.")
```

**Was ist passiert?**

1. Python versucht, die Division durchzuführen
2. Ein `ZeroDivisionError` tritt auf
3. Python springt in den `except`-Block
4. Die benutzerfreundliche Fehlermeldung wird ausgegeben
5. **Das Programm läuft weiter!** Es stürzt nicht ab

Die Zeile `print("Das Programm läuft weiter.")` wird ausgeführt, obwohl ein Fehler aufgetreten ist.

+++

### Beispiel 2: Typkonvertierung mit Fehlerbehandlung

```{code-cell} ipython3
# Benutzereingabe mit Fehlerbehandlung

eingabe = input("Geben Sie eine Zahl ein: ")

try:
    zahl = int(eingabe)  # Versuche, in eine Ganzzahl umzuwandeln
    print("Sie haben die Zahl", zahl, "eingegeben.")
    print("Das Doppelte ist:", zahl * 2)
except:
    print("Fehler: Das war keine gültige Zahl!")
    print("Bitte geben Sie beim nächsten Mal eine Zahl ein.")
```

**Was ist passiert?**

**Fall 1: Benutzer gibt eine gültige Zahl ein (z.B. "42")**
1. Die Umwandlung mit `int(eingabe)` funktioniert
2. Die beiden print-Anweisungen im `try`-Block werden ausgeführt
3. Der `except`-Block wird übersprungen

**Fall 2: Benutzer gibt ungültigen Text ein (z.B. "abc")**
1. Die Umwandlung mit `int(eingabe)` schlägt fehl
2. Python springt sofort in den `except`-Block
3. Die Fehlermeldungen werden ausgegeben
4. Das Programm stürzt nicht ab!

+++

### Angeleitete Übung 1.1

**Aufgabe**: Schreiben Sie ein Programm, das zwei Zahlen durch den Benutzer abfragt und diese dividiert. Fangen Sie mögliche Fehler ab (sowohl bei der Eingabe als auch bei der Division).

**Schritte**:
1. Fragen Sie den Benutzer nach zwei Zahlen mit `input()`
2. Wandeln Sie beide Eingaben mit `int()` in Ganzzahlen um
3. Führen Sie die Division durch
4. Verwenden Sie `try-except`, um Fehler abzufangen
5. Geben Sie bei einem Fehler eine hilfreiche Nachricht aus

```{code-cell} ipython3
# Ihr Code hier

def nutzereingabe():
    zahl1 = input("Bitte Zahl1 eingeben:")
    zahl2 = input("Bitte Zahl2 eingeben:")
    return zahl1, zahl2

try:
    zahl1, zahl2 = nutzereingabe()
    zahl1 = int(zahl1)
    zahl2 = int(zahl2)
    ergebnis = int(zahl1)/int(zahl2)
    print(ergebnis)
except:
    print("Das waren keine gültigen Zahlen oder bei der Division ist was schiefgelaufen!")

```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
try:
    zahl1 = input("Erste Zahl: ")
    zahl2 = input("Zweite Zahl: ")
    
    # Umwandlung in Ganzzahlen
    z1 = int(zahl1)
    z2 = int(zahl2)
    
    # Division durchführen
    ergebnis = z1 / z2
    print("Das Ergebnis ist:", ergebnis)
    
except:
    print("Fehler: Bitte geben Sie gültige Zahlen ein.")
    print("Hinweis: Division durch Null ist nicht erlaubt.")
```

**Erklärung**: Diese Lösung fängt alle möglichen Fehler ab - sowohl ungültige Eingaben als auch Division durch Null. Der `except`-Block wird ausgeführt, wenn irgendetwas im `try`-Block schiefgeht.
</details>

+++

### Angeleitete Übung 1.2

**Aufgabe**: Erweitern Sie das vorherige Programm mit einer Schleife, sodass der Benutzer so lange nach neuen Zahlen gefragt wird, bis er "ende" eingibt.

**Hinweise**:
- Verwenden Sie eine `while`-Schleife
- Prüfen Sie vor der Umwandlung, ob die Eingabe "ende" ist
- Nutzen Sie `try-except` innerhalb der Schleife

```{code-cell} ipython3
# Ihr Code hier

print("Divisionsprogramm, zwei Zahlen eingeben und Ergbnis bekommen.")
print("Zum Abbrechen des Programms 'ende' eingeben")

while True:

    def nutzereingabe():
        zahl1 = input("Bitte Zahl1 eingeben:")
        zahl2 = input("Bitte Zahl2 eingeben:")
        return zahl1, zahl2

    try:
        zahl1, zahl2 = nutzereingabe()
        if zahl1.lower() == "ende" or zahl2.lower() == "ende":
            break
        zahl1 = int(zahl1)
        zahl2 = int(zahl2)
        ergebnis = int(zahl1)/int(zahl2)
        print(ergebnis)
    except:
        print("Das waren keine gültigen Zahlen oder bei der Division ist was schiefgelaufen!")
        print("Probiers nochmal!")

print("Programm beendet!")
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
print("Divisions-Rechner (Geben Sie 'ende' ein zum Beenden)")

while True:
    zahl1 = input("Erste Zahl: ")
    
    # Prüfen, ob Benutzer beenden möchte
    if zahl1.lower() == "ende":
        print("Programm beendet.")
        break
    
    zahl2 = input("Zweite Zahl: ")
    
    try:
        # Umwandlung und Division
        z1 = int(zahl1)
        z2 = int(zahl2)
        ergebnis = z1 / z2
        print(f"Ergebnis: {z1} / {z2} = {ergebnis}\n")
    except:
        print("Fehler: Ungültige Eingabe oder Division durch Null!\n")
```

**Erklärung**: Diese Lösung kombiniert eine Endlosschleife mit Fehlerbehandlung. Der Benutzer kann beliebig viele Divisionen durchführen, und Fehler führen nicht zum Programmabsturz.
</details>

+++

---

## Spezifische Exception-Typen behandeln

### Warum spezifische Exceptions?

Im vorherigen Abschnitt haben wir ein einfaches `except:` verwendet, das **alle** Fehler abfängt. Das funktioniert, ist aber nicht optimal. Oft möchten wir auf **verschiedene Fehlerarten unterschiedlich reagieren**.

**Beispiel**: Bei einer Division kann zweierlei schiefgehen:
1. Der Benutzer gibt Text statt einer Zahl ein → **ValueError**
2. Der Benutzer gibt Null als Divisor ein → **ZeroDivisionError**

Mit spezifischen Exception-Typen können wir für jeden Fall eine passende Fehlermeldung ausgeben.

### Die Syntax für spezifische Exceptions

```python
try:
    # Code, der Fehler verursachen könnte
except ExceptionTyp1:
    # Wird nur bei ExceptionTyp1 ausgeführt
except ExceptionTyp2:
    # Wird nur bei ExceptionTyp2 ausgeführt
except:
    # Fängt alle anderen Fehler ab (optional)
```

**Wichtig**: Die `except`-Blöcke werden **von oben nach unten** geprüft. Sobald ein passender Block gefunden wird, wird dieser ausgeführt, und die restlichen werden übersprungen.

+++

### Beispiel 1: ValueError und ZeroDivisionError unterscheiden

```{code-cell} ipython3
# Spezifische Fehlerbehandlung für verschiedene Exception-Typen

try:
    zahl1 = input("Geben Sie die erste Zahl ein: ")
    zahl2 = input("Geben Sie die zweite Zahl ein: ")
    
    # Umwandlung in Ganzzahlen
    z1 = int(zahl1)
    z2 = int(zahl2)
    
    # Division durchführen
    ergebnis = z1 / z2
    print(f"Ergebnis: {z1} / {z2} = {ergebnis}")
    
except ValueError:
    print("Fehler: Das war keine gültige Zahl!")
    print("Bitte geben Sie nur Zahlen ein (z.B. 42).")
    
except ZeroDivisionError:
    print("Fehler: Division durch Null ist nicht erlaubt!")
    print("Die zweite Zahl darf nicht 0 sein.")
```

```{code-cell} ipython3
int("zahl")
```

**Was passiert hier?**

**Fall 1: Benutzer gibt "abc" und "5" ein**
1. Die Umwandlung `int("abc")` schlägt fehl
2. Python sucht nach einem passenden `except`-Block
3. Der erste Block (`except ValueError`) passt → wird ausgeführt
4. Ausgabe: Fehlermeldung zu ungültiger Zahl

**Fall 2: Benutzer gibt "10" und "0" ein**
1. Die Umwandlung funktioniert
2. Die Division `10 / 0` schlägt fehl
3. Python sucht nach einem passenden `except`-Block
4. Der zweite Block (`except ZeroDivisionError`) passt → wird ausgeführt
5. Ausgabe: Fehlermeldung zur Division durch Null

**Fall 3: Benutzer gibt "10" und "2" ein**
1. Alles funktioniert einwandfrei
2. Kein `except`-Block wird ausgeführt
3. Ausgabe: "Ergebnis: 10 / 2 = 5.0"

+++

### Die wichtigsten Exception-Typen

Hier eine Übersicht der häufigsten Exception-Typen, die Sie kennen sollten:

| Exception-Typ | Wann tritt er auf? | Beispiel |
|---------------|-------------------|----------|
| **ValueError** | Wert hat falsches Format | `int("abc")` |
| **TypeError** | Falscher Datentyp für Operation | `"text" + 5` |
| **ZeroDivisionError** | Division durch Null | `10 / 0` |
| **KeyError** | Dictionary-Schlüssel existiert nicht | `dict["key"]` (key nicht vorhanden) |
| **IndexError** | Listen-Index außerhalb des gültigen Bereichs | `liste[10]` (Liste hat nur 3 Elemente) |

**Hinweis**: In diesem Notebook konzentrieren wir uns auf `ValueError`, `TypeError` und `ZeroDivisionError`, da diese am häufigsten bei Berechnungen und Benutzereingaben auftreten.

+++

### Beispiel 2: TypeError abfangen

```{code-cell} ipython3
# TypeError-Beispiel

try:
    text = "Hallo"
    zahl = 5
    
    # Versuch, Text und Zahl zu addieren
    ergebnis = text + zahl
    print(ergebnis)
    
except TypeError:
    print("Fehler: Sie können keine Texte und Zahlen addieren!")
    print("Tipp: Wandeln Sie die Zahl in einen String um: str(zahl)")
```

**Erklärung**: Python kann Strings und Zahlen nicht direkt addieren. Der `TypeError` tritt auf, weil die Operation `"Hallo" + 5` nicht definiert ist. Mit Fehlerbehandlung können wir eine hilfreiche Meldung ausgeben.

+++

### Angeleitete Übung 2.1

**Aufgabe**: Schreiben Sie ein Programm zur Kreisumfang-Berechnung mit spezifischer Fehlerbehandlung.

**Schritte**:
1. Fragen Sie den Benutzer nach dem Wert von Pi (als Kommazahl)
2. Fragen Sie nach dem Radius (als Kommazahl)
3. Berechnen Sie den Umfang: `umfang = 2 * pi * radius`
4. Fangen Sie **ValueError** ab (falls der Benutzer ungültigen Text eingibt)
5. Geben Sie das Ergebnis oder eine Fehlermeldung aus

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
try:
    # Benutzereingaben
    pi_eingabe = input("Geben Sie Pi ein (z.B. 3.14159): ")
    radius_eingabe = input("Geben Sie den Radius ein (in cm): ")
    
    # Umwandlung in Gleitkommazahlen
    pi = float(pi_eingabe)
    radius = float(radius_eingabe)
    
    # Berechnung
    umfang = 2 * pi * radius
    flaeche = pi * radius ** 2
    
    # Ausgabe
    print(f"\nKreisumfang: {umfang:.2f} cm")
    print(f"Kreisfläche: {flaeche:.2f} cm²")
    
except ValueError:
    print("Fehler: Bitte geben Sie gültige Zahlen ein!")
    print("Hinweis: Verwenden Sie einen Punkt als Dezimaltrennzeichen (z.B. 3.14)")
```

**Erklärung**: Diese Lösung verwendet `float()` für die Umwandlung, da Pi und der Radius Kommazahlen sein können. Der `ValueError` fängt ungültige Eingaben ab.
</details>

+++

---

## Der finally-Block: Aufräumarbeiten garantieren

### Was ist der finally-Block?

Der **finally-Block** wird **immer** ausgeführt - egal, ob ein Fehler aufgetreten ist oder nicht. Er ist nützlich für **Aufräumarbeiten**, die auf jeden Fall durchgeführt werden müssen.

**Alltags-Beispiel**: Stellen Sie sich vor, Sie leihen sich ein Buch aus der Bibliothek:
1. **try**: Sie versuchen, das Buch zu lesen
2. **except**: Falls Sie krank werden, behandeln Sie die Krankheit
3. **finally**: In jedem Fall geben Sie das Buch zurück (egal ob gelesen oder nicht)

Der `finally`-Block stellt sicher, dass das Buch zurückgegeben wird - auch wenn etwas schiefgeht.

### Die vollständige try-except-finally-Struktur

```python
try:
    # Code, der Fehler verursachen könnte
except:
    # Code bei Fehler
finally:
    # Code, der IMMER ausgeführt wird
```

**Ausführungsreihenfolge**:
1. `try`-Block wird ausgeführt
2. Falls Fehler: `except`-Block wird ausgeführt
3. **In jedem Fall**: `finally`-Block wird ausgeführt

### Wann verwendet man finally?

Der `finally`-Block ist nützlich für:
- Dateien schließen (wird in Notebook 12 behandelt)
- Datenbankverbindungen beenden
- Ressourcen freigeben
- Statusmeldungen ausgeben
- Aufräum-Operationen, die immer durchgeführt werden müssen

**Hinweis**: In diesem Notebook verwenden wir `finally` hauptsächlich für Statusmeldungen. Die praktische Bedeutung wird in späteren Notebooks (FileIO, Datenbanken) deutlicher.

+++

### Beispiel 1: finally mit Statusmeldung

```{code-cell} ipython3
# try-except-finally-Beispiel

try:
    zahl1 = int(input("Erste Zahl: "))
    zahl2 = int(input("Zweite Zahl: "))
    
    ergebnis = zahl1 / zahl2
    print(f"Ergebnis: {ergebnis}")
    
except ValueError:
    print("Fehler: Ungültige Eingabe!")
    
except ZeroDivisionError:
    print("Fehler: Division durch Null!")
    
finally:
    print("Berechnung abgeschlossen.")
    print("Vielen Dank für die Nutzung!")
```

**Was passiert hier?**

**Fall 1: Erfolgreiche Berechnung**
1. Benutzer gibt gültige Zahlen ein
2. Berechnung wird durchgeführt
3. Ergebnis wird ausgegeben
4. **finally-Block wird ausgeführt**: "Berechnung abgeschlossen."

**Fall 2: Fehler bei der Eingabe**
1. Benutzer gibt ungültigen Text ein
2. `ValueError` tritt auf
3. Fehlermeldung wird ausgegeben
4. **finally-Block wird trotzdem ausgeführt**: "Berechnung abgeschlossen."

**Fall 3: Division durch Null**
1. Benutzer gibt 0 als zweite Zahl ein
2. `ZeroDivisionError` tritt auf
3. Fehlermeldung wird ausgegeben
4. **finally-Block wird trotzdem ausgeführt**: "Berechnung abgeschlossen."

**Wichtig**: Der `finally`-Block wird in **allen drei Fällen** ausgeführt!

+++

### Beispiel 2: finally für Zähler

```{code-cell} ipython3
# Zähler mit finally

erfolgreiche_berechnungen = 0
fehlgeschlagene_berechnungen = 0

print("Rechner (Geben Sie 'ende' ein zum Beenden)\n")

while True:
    eingabe = input("Geben Sie eine Zahl ein (oder 'ende'): ")
    
    if eingabe.lower() == "ende":
        break
    
    try:
        zahl = int(eingabe)
        quadrat = zahl ** 2
        print(f"Das Quadrat von {zahl} ist {quadrat}\n")
        erfolgreiche_berechnungen += 1
        
    except ValueError:
        print("Fehler: Ungültige Eingabe!\n")
        fehlgeschlagene_berechnungen += 1
        
    finally:
        # Wird nach jedem Durchlauf ausgeführt
        gesamtzahl = erfolgreiche_berechnungen + fehlgeschlagene_berechnungen
        print(f"Durchgeführte Berechnungen: {gesamtzahl}\n")

# Abschlussbericht
print("\n=== ZUSAMMENFASSUNG ===")
print(f"Erfolgreiche Berechnungen: {erfolgreiche_berechnungen}")
print(f"Fehlgeschlagene Versuche: {fehlgeschlagene_berechnungen}")
```

**Erklärung**: In diesem Beispiel wird der `finally`-Block verwendet, um nach jeder Eingabe (egal ob erfolgreich oder fehlerhaft) die Gesamtzahl der Versuche auszugeben. Das zeigt, dass `finally` sich gut für Logging und Statusupdates eignet.

+++

### Angeleitete Übung 3.1

**Aufgabe**: Erweitern Sie das Kreisumfang-Programm aus Übung 2.1 mit einem `finally`-Block, der immer "Programm beendet." ausgibt.

**Hinweis**: Kopieren Sie Ihre Lösung von Übung 2.1 und fügen Sie einen `finally`-Block hinzu.

```{code-cell} ipython3
# Ihr Code hier
print("Hallo")
print()
print("Du")
```

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```python
try:
    # Benutzereingaben
    pi_eingabe = input("Geben Sie Pi ein (z.B. 3.14159): ")
    radius_eingabe = input("Geben Sie den Radius ein (in cm): ")
    
    # Umwandlung in Gleitkommazahlen
    pi = float(pi_eingabe)
    radius = float(radius_eingabe)
    
    # Berechnung
    umfang = 2 * pi * radius
    flaeche = pi * radius ** 2
    
    # Ausgabe
    print(f"\nKreisumfang: {umfang:.2f} cm")
    print(f"Kreisfläche: {flaeche:.2f} cm²")
    
except ValueError:
    print("Fehler: Bitte geben Sie gültige Zahlen ein!")
    print("Hinweis: Verwenden Sie einen Punkt als Dezimaltrennzeichen (z.B. 3.14)")
    
finally:
    print("\nProgramm beendet.")
```

**Erklärung**: Der `finally`-Block stellt sicher, dass "Programm beendet." ausgegeben wird - egal ob die Berechnung erfolgreich war oder ein Fehler aufgetreten ist.
</details>

+++

---

## Abschlussübungen

Die folgenden Aufgaben testen Ihr Verständnis der in diesem Notebook erlernten Konzepte. Bearbeiten Sie die Aufgaben selbstständig und vergleichen Sie Ihre Lösung anschließend mit den Musterlösungen am Ende des Notebooks.

### Teil 1: Grundlegende Anwendung

**Kompetenzstufe**: Anwenden

Diese Aufgaben testen die direkte Anwendung der erlernten Konzepte.

**Aufgabe 1**: Schreiben Sie ein Programm, das den Benutzer nach seinem Alter fragt. Fangen Sie ValueError ab, falls ungültiger Text eingegeben wird. Geben Sie das Alter aus, falls die Eingabe gültig ist.

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 1
```

**Aufgabe 2**: Erstellen Sie ein Programm, das zwei Zahlen multipliziert. Fangen Sie ValueError (ungültige Eingabe) und TypeError (falls versehentlich Strings nicht umgewandelt werden) ab. Verwenden Sie spezifische Fehlermeldungen für jeden Fall.

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 2
```

---

### Teil 2: Transfer und Problemlösung

**Kompetenzstufe**: Analysieren & Erschaffen

Diese Aufgaben erfordern die Kombination mehrerer Konzepte und eigenständiges Problemlösen.

**Aufgabe 3**: Schreiben Sie ein robustes Programm zur Temperaturumrechnung (Celsius → Fahrenheit). Die Formel lautet: `fahrenheit = celsius * 9/5 + 32`. Das Programm soll:
- Den Benutzer in einer Schleife nach Temperaturen fragen
- Bei "ende" die Schleife beenden
- ValueError abfangen (ungültige Eingaben)
- Einen finally-Block verwenden, um die Anzahl der durchgeführten Umrechnungen auszugeben

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 3
```

**Aufgabe 4**: Erstellen Sie ein Programm zur Produktionsauslastung-Berechnung. Das Programm soll:
- Nach der maximalen Tageskapazität fragen
- Nach der tatsächlich produzierten Menge fragen
- Die Auslastung in Prozent berechnen: `auslastung = (ist / max) * 100`
- Alle drei Exception-Typen behandeln: ValueError (ungültige Eingabe), ZeroDivisionError (max = 0), TypeError
- Einen finally-Block verwenden, um immer "Berechnung abgeschlossen" auszugeben
- Eine Bewertung ausgeben: >= 90%: "Ausgezeichnet", >= 75%: "Gut", < 75%: "Verbesserungsbedarf"

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 4
```

---

## Zusammenfassung

In diesem Notebook haben Sie folgende Konzepte kennengelernt:

| Konzept | Syntax | Anwendungsfall |
|---------|--------|----------------|
| **try-except** | `try: ... except: ...` | Fehler abfangen und behandeln |
| **ValueError** | `except ValueError:` | Ungültige Typkonvertierung (z.B. `int("abc")`) |
| **ZeroDivisionError** | `except ZeroDivisionError:` | Division durch Null |
| **TypeError** | `except TypeError:` | Ungeeigneter Datentyp für Operation |
| **finally** | `finally:` | Code, der immer ausgeführt wird |

**Zentrale Erkenntnisse**:
- Fehlerbehandlung macht Programme robust und benutzerfreundlich
- Mit `try-except` können Sie Fehler kontrolliert abfangen, statt dass das Programm abstürzt
- Spezifische Exception-Typen ermöglichen präzise Fehlerbehandlung
- Der `finally`-Block garantiert Aufräumarbeiten, unabhängig vom Erfolg

**Nächste Schritte**: Im folgenden Notebook (12 - FileIO) werden Sie lernen, wie man Dateien liest und schreibt. Fehlerbehandlung wird dort besonders wichtig, da Dateien möglicherweise nicht existieren oder nicht geöffnet werden können.

---

## Musterlösungen

<details>
<summary>Lösung zu Aufgabe 1</summary>

```python
try:
    alter_eingabe = input("Wie alt sind Sie? ")
    alter = int(alter_eingabe)
    print(f"Sie sind {alter} Jahre alt.")
    
except ValueError:
    print("Fehler: Bitte geben Sie eine gültige Zahl ein!")
```

**Erklärung**:
- Der `try`-Block versucht, die Eingabe in eine Ganzzahl umzuwandeln
- Falls der Benutzer Text eingibt, tritt ein `ValueError` auf
- Der `except`-Block fängt den Fehler ab und gibt eine verständliche Nachricht aus

**Häufige Fehler**:
- Vergessen, `int()` zu verwenden → keine Umwandlung, kein Fehler zum Abfangen
- Falscher Exception-Typ (z.B. `TypeError` statt `ValueError`)
</details>

<details>
<summary>Lösung zu Aufgabe 2</summary>

```python
try:
    zahl1 = input("Erste Zahl: ")
    zahl2 = input("Zweite Zahl: ")
    
    # Umwandlung in Zahlen
    z1 = int(zahl1)
    z2 = int(zahl2)
    
    # Multiplikation
    ergebnis = z1 * z2
    print(f"Ergebnis: {z1} * {z2} = {ergebnis}")
    
except ValueError:
    print("Fehler: Bitte geben Sie gültige Zahlen ein!")
    
except TypeError:
    print("Fehler: Die Multiplikation konnte nicht durchgeführt werden.")
    print("Stellen Sie sicher, dass beide Werte Zahlen sind.")
```

**Erklärung**: Diese Lösung behandelt beide möglichen Fehlertypen separat. In der Praxis tritt bei korrekter Programmierung nur `ValueError` auf, aber die Trennung zeigt, wie man verschiedene Fehler unterschiedlich behandelt.
</details>

<details>
<summary>Lösung zu Aufgabe 3</summary>

```python
print("Temperaturumrechner (Celsius → Fahrenheit)")
print("Geben Sie 'ende' ein zum Beenden\n")

anzahl_umrechnungen = 0

while True:
    celsius_eingabe = input("Temperatur in Celsius: ")
    
    # Prüfen, ob Benutzer beenden möchte
    if celsius_eingabe.lower() == "ende":
        break
    
    try:
        # Umwandlung und Berechnung
        celsius = float(celsius_eingabe)
        fahrenheit = celsius * 9/5 + 32
        
        print(f"{celsius}°C = {fahrenheit:.1f}°F\n")
        anzahl_umrechnungen += 1
        
    except ValueError:
        print("Fehler: Ungültige Eingabe! Bitte geben Sie eine Zahl ein.\n")
        
    finally:
        # Wird nach jedem Durchlauf ausgeführt
        print(f"Bisher durchgeführte Umrechnungen: {anzahl_umrechnungen}\n")

print(f"\nInsgesamt wurden {anzahl_umrechnungen} Umrechnungen durchgeführt.")
```

**Erklärung**: Diese Lösung kombiniert eine while-Schleife mit try-except-finally. Der `finally`-Block zählt die Umrechnungen nach jedem Versuch (erfolgreich oder nicht).
</details>

<details>
<summary>Lösung zu Aufgabe 4</summary>

```python
print("Produktionsauslastung-Rechner\n")

try:
    # Eingaben
    max_eingabe = input("Maximale Tageskapazität: ")
    ist_eingabe = input("Tatsächlich produzierte Menge: ")
    
    # Umwandlung
    max_kapazitaet = float(max_eingabe)
    ist_produktion = float(ist_eingabe)
    
    # Berechnung
    auslastung = (ist_produktion / max_kapazitaet) * 100
    
    # Ausgabe
    print(f"\nAuslastung: {auslastung:.1f}%")
    
    # Bewertung
    if auslastung >= 90:
        print("Bewertung: Ausgezeichnet!")
    elif auslastung >= 75:
        print("Bewertung: Gut")
    else:
        print("Bewertung: Verbesserungsbedarf")
        
except ValueError:
    print("\nFehler: Bitte geben Sie gültige Zahlen ein!")
    
except ZeroDivisionError:
    print("\nFehler: Die maximale Kapazität darf nicht 0 sein!")
    
except TypeError:
    print("\nFehler: Ein Typfehler ist aufgetreten.")
    print("Stellen Sie sicher, dass alle Eingaben Zahlen sind.")
    
finally:
    print("\nBerechnung abgeschlossen.")
```

**Erklärung**: Diese Lösung demonstriert die vollständige Fehlerbehandlung mit allen drei Exception-Typen und einem `finally`-Block. Sie kombiniert außerdem Konzepte aus früheren Notebooks (if-elif-else für die Bewertung).

**Alternative Ansätze**:
- Man könnte zusätzlich prüfen, ob die Werte negativ sind
- Man könnte eine Schleife hinzufügen, um mehrere Berechnungen durchzuführen
- Man könnte die Anzahl erfolgreicher/fehlgeschlagener Berechnungen zählen
</details>
