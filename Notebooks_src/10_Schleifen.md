---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
kernelspec:
  display_name: base2
  language: python
  name: python3
---

# 10 - Schleifen: Wiederholungen automatisieren 🔄

## Willkommen! 👋

Herzlich willkommen zum zehnten Notebook! Sie haben bereits gelernt, wie Programme Entscheidungen treffen können (mit if-else). Heute lernen Sie, wie Programme Aufgaben automatisch wiederholen können - eine der mächtigsten Fähigkeiten der Programmierung!

## Was Sie heute lernen:
- While-Schleifen für bedingte Wiederholungen
- For-Schleifen für Iterationen über Kollektionen
- Die range()-Funktion für Zahlenfolgen
- Schleifensteuerung mit break und continue
- List Comprehensions als kompakte Alternative

## Voraussetzungen 📚
Was Sie schon können sollten:
- Mit Variablen arbeiten (Notebook 04)
- Datentypen verwenden (int, float, str, bool) (Notebook 05)
- Listen, Dictionaries und andere Kollektionen nutzen (Notebook 06)
- Funktionen definieren und aufrufen (Notebook 07)
- Mit Operatoren rechnen und vergleichen (Notebook 08)
- If-else-Verzweigungen schreiben (Notebook 09)

+++

## Warum brauchen wir Schleifen? 🤔

Stellen Sie sich vor, Sie müssen 100 Zahlen ausgeben. Würden Sie 100 Mal `print()` schreiben? Oder Sie müssen einen Text durchsuchen und jeden Buchstaben prüfen - würden Sie für jeden Buchstaben eine eigene if-Anweisung schreiben?

**Das wäre furchtbar viel Arbeit!**

Genau hier kommen **Schleifen** ins Spiel. Eine Schleife ist wie ein Fließband in einer Fabrik:
- Ein Fließband führt die gleiche Aufgabe immer wieder aus (z.B. eine Schraube eindrehen)
- Es stoppt automatisch, wenn die Arbeit erledigt ist
- Es kann vorzeitig gestoppt werden, wenn etwas schiefgeht

Mit Schleifen können Sie **Code automatisch wiederholen lassen**, ohne ihn mehrfach zu schreiben. Das spart nicht nur Zeit, sondern macht Ihren Code auch viel übersichtlicher und flexibler!

+++

## While-Schleifen: Wiederholen mit Bedingung 🔁

### Was ist eine While-Schleife?

Eine **While-Schleife** ist wie ein geduldiger Helfer, der eine Aufgabe so lange wiederholt, bis eine bestimmte Bedingung nicht mehr erfüllt ist.

**Alltags-Beispiel:**
Stellen Sie sich vor, Sie schälen Kartoffeln für ein Essen:
- **SOLANGE** (while) noch ungeschälte Kartoffeln im Korb sind
- **WIEDERHOLE**: Nimm eine Kartoffel und schäle sie
- **DANN**: Wenn der Korb leer ist, höre auf

Genau so funktioniert eine While-Schleife in Python!

### Wie funktioniert sie?

Eine While-Schleife prüft **vor jedem Durchlauf** eine Bedingung:
1. **Ist die Bedingung WAHR?** → Führe den Code im Schleifenkörper aus
2. **Ist die Bedingung FALSCH?** → Springe aus der Schleife heraus und mache weiter

Die Schleife wiederholt sich automatisch, solange die Bedingung erfüllt ist. Sobald die Bedingung falsch wird, stoppt die Schleife.

### Wann verwendet man While-Schleifen?

While-Schleifen sind perfekt, wenn Sie **nicht im Voraus wissen**, wie oft etwas wiederholt werden muss:
- Benutzereingaben wiederholen, bis eine gültige Eingabe kommt
- Einen Countdown laufen lassen
- Daten verarbeiten, bis ein bestimmter Wert erreicht ist
- Ein Spiel laufen lassen, bis der Spieler gewinnt oder aufhört

+++

### Die Syntax der While-Schleife

So schreibt man eine While-Schleife in Python:

```python
while Bedingung:
    # Dieser Code wird wiederholt
    # solange die Bedingung WAHR ist
```

**Wichtige Bestandteile:**
1. **`while`** - Das Schlüsselwort, das die Schleife einleitet
2. **Bedingung** - Ein Ausdruck, der entweder True oder False ergibt (genau wie bei if!)
3. **Doppelpunkt `:`** - Markiert das Ende der Bedingung
4. **Eingerückter Code** - Alle eingerückten Zeilen gehören zur Schleife

**Achtung:** Genau wie bei if-else muss der Code im Inneren eingerückt sein (mit 4 Leerzeichen oder Tab)!

+++

### Erstes Beispiel: Ein einfacher Countdown

Schauen wir uns ein ganz einfaches Beispiel an - einen Countdown von 5 bis 0:

```{code-cell} ipython3
# Einfacher Countdown mit While-Schleife

x = 10  # Startwert

while x >= 0:  # Solange x größer oder gleich 0 ist
    print(x)    # Gib x aus
    x = x - 2   # Verringere x um 1

print("Fertig!")  # Wird ausgeführt, wenn die Schleife endet
```

**Was passiert hier?**

1. Wir starten mit `x = 5`
2. **Durchlauf 1:** Ist `x >= 0`? JA (5 >= 0) → Gib 5 aus, setze x auf 4
3. **Durchlauf 2:** Ist `x >= 0`? JA (4 >= 0) → Gib 4 aus, setze x auf 3
4. **Durchlauf 3:** Ist `x >= 0`? JA (3 >= 0) → Gib 3 aus, setze x auf 2
5. **Durchlauf 4:** Ist `x >= 0`? JA (2 >= 0) → Gib 2 aus, setze x auf 1
6. **Durchlauf 5:** Ist `x >= 0`? JA (1 >= 0) → Gib 1 aus, setze x auf 0
7. **Durchlauf 6:** Ist `x >= 0`? JA (0 >= 0) → Gib 0 aus, setze x auf -1
8. **Prüfung:** Ist `x >= 0`? NEIN (-1 ist nicht >= 0) → **Schleife endet!**
9. Gib "Fertig!" aus

**Wichtig:** Die Zeile `x = x - 1` ist entscheidend! Ohne sie würde x immer 5 bleiben und die Schleife würde niemals enden (mehr dazu gleich).

+++

### 🏃 Sofort ausprobieren!

**Aufgabe 1:** Schreiben Sie einen Countdown von 10 bis 0

```{code-cell} ipython3
# Ihr Code hier:

n = 10

while n >= 0:
    print (n)
    n -= 1 # gleich wie "n = n - 1"
```

**Aufgabe 2:** Schreiben Sie eine While-Schleife, die von 0 bis 5 hochzählt (nicht runterzählt!)

```{code-cell} ipython3
# Ihr Code hier:

m = 0

while m <= 5:
    print(m)
    m = m + 1
```

**Aufgabe 3:** Schreiben Sie eine While-Schleife, die nur gerade Zahlen von 0 bis 10 ausgibt (0, 2, 4, 6, 8, 10)

```{code-cell} ipython3
# Ihr Code hier:
y = 0

while y <= 10:
    print(y)
    y = y + 2
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1: Countdown von 10 bis 0
x = 10
while x >= 0:
    print(x)
    x = x - 1
print("Start!")

# Aufgabe 2: Hochzählen von 0 bis 5
x = 0
while x <= 5:
    print(x)
    x = x + 1  # Diesmal addieren wir!

# Aufgabe 3: Nur gerade Zahlen
x = 0
while x <= 10:
    print(x)
    x = x + 2  # Wir erhöhen um 2, nicht um 1!
```
</details>

+++

### Praktisches Beispiel: Quader-Volumen berechnen

Schauen wir uns ein realistischeres Beispiel an. Ein Programm, das so lange Quader-Volumen berechnet, bis der Benutzer nicht mehr möchte:

```{code-cell} ipython3
# Quader-Volumen berechnen mit While-Schleife

print("Berechnung des Volumens eines Quaders")

antwort = 'j'  # Startwert: Benutzer möchte beginnen

while (antwort == 'j') or (antwort =='ja'):  # Solange der Benutzer 'j' eingibt
    # Maße abfragen
    l = input("Länge in cm: ")
    b = input("Breite in cm: ")
    h = input("Höhe in cm: ")
    
    # Volumen berechnen
    volumen = float(l) * float(b) * float(h)
    print("Das Volumen ist", volumen, "ccm.")
    
    # Fragen, ob weiter gemacht werden soll
    antwort = input("Noch einmal? (j=ja/n=nein): ")

print("Vielen Dank für die Benutzung dieses Programms!")
```

```{code-cell} ipython3
False or bool('ja')
```

**Was passiert hier?**

1. Wir setzen `antwort` auf `'j'`, damit die Schleife startet
2. Die Bedingung `antwort == 'j'` ist anfangs WAHR
3. Im Schleifenkörper:
   - Benutzer gibt Maße ein
   - Volumen wird berechnet und ausgegeben
   - Benutzer wird gefragt: "Noch einmal?"
4. **Falls Benutzer 'j' eingibt:** Die Bedingung bleibt WAHR → Schleife läuft erneut
5. **Falls Benutzer etwas anderes eingibt:** Die Bedingung wird FALSCH → Schleife endet
6. Abschlussnachricht wird ausgegeben

**Wichtig:** Die Variable `antwort` wird **innerhalb** der Schleife verändert. So kann die Bedingung irgendwann falsch werden und die Schleife beenden.

+++

### 🏃 Sofort ausprobieren!

**Aufgabe 1:** Schreiben Sie ein Programm, das den Benutzer nach zwei Zahlen fragt, sie multipliziert und ausgibt. Das Programm soll so lange laufen, bis der Benutzer "stop" eingibt.

```{code-cell} ipython3
# Ihr Code hier:
antwort = "" 

while antwort != "stop":
    n = float(input("Zahl1: "))
    m = float(input("Zahl2: "))
    print(n*m)
    antwort = input("Stop? mit 'stop'!: ")

print("Ende Gelände!")
```

```{code-cell} ipython3
antwort = "stop"
print(antwort != "stop")
```

**Aufgabe 2:** Erweitern Sie das Programm: Zählen Sie mit, wie viele Berechnungen durchgeführt wurden, und geben Sie am Ende aus: "Sie haben X Berechnungen durchgeführt."

```{code-cell} ipython3
# Ihr Code hier:
antwort = "" 
ergebnisse = []

while antwort != "stop":
    n = float(input("Zahl1: "))
    m = float(input("Zahl2: "))
    ergebnis = n *m 
    print(f"Das Ergebnis ist: {ergebnis}")
    ergebnisse.append(ergebnis)
    antwort = input("Stop? mit 'stop'!: ")

print(f"Alle Ergebnisse: {ergebnisse}")
print(f"Anzahl der Durchläufe {len(ergebnisse)}")
print("Ende Gelände!")
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1: Multiplikation wiederholen
print("Multiplikations-Rechner")
antwort = "start"  # Beliebiger Startwert, nur nicht "stop"

while antwort != "stop":
    zahl1 = input("Erste Zahl: ")
    zahl2 = input("Zweite Zahl: ")
    ergebnis = float(zahl1) * float(zahl2)
    print("Ergebnis:", ergebnis)
    antwort = input("Weiter? (beliebige Taste oder 'stop'): ")

print("Programm beendet!")

# Aufgabe 2: Mit Zähler
print("Multiplikations-Rechner")
antwort = "start"
zaehler = 0  # Zähler für Berechnungen

while antwort != "stop":
    zahl1 = input("Erste Zahl: ")
    zahl2 = input("Zweite Zahl: ")
    ergebnis = float(zahl1) * float(zahl2)
    print("Ergebnis:", ergebnis)
    zaehler = zaehler + 1  # Zähler erhöhen
    antwort = input("Weiter? (beliebige Taste oder 'stop'): ")

print("Sie haben", zaehler, "Berechnungen durchgeführt.")
```
</details>

+++

## Endlosschleifen: Wenn die Schleife nicht aufhört 🔄

### Was ist eine Endlosschleife?

Eine **Endlosschleife** (auch "infinite loop" genannt) ist eine Schleife, die niemals endet - sie läuft ewig weiter!

**Alltags-Beispiel:**
Stellen Sie sich vor, Sie sagen zu jemandem:
- "Solange die Ampel rot ist, warte!"
- **Aber:** Die Ampel ist kaputt und wird niemals grün!
- Die Person würde ewig warten...

Genau das passiert bei einer Endlosschleife: Die Bedingung wird niemals falsch, also läuft die Schleife endlos weiter.

### Wie entstehen Endlosschleifen?

**Zwei häufige Ursachen:**

1. **Die Bedingung ist immer wahr:**
```python
while True:  # True bleibt immer True!
    print("Ich höre nie auf!")
```

2. **Die Variable in der Bedingung wird nicht verändert:**
```python
x = 0
while x < 10:  # x wird nie größer!
    print(x)    # x bleibt immer 0!
    # Ups! Wir haben vergessen: x = x + 1
```

+++

### Beispiel einer versehentlichen Endlosschleife

**ACHTUNG: Führen Sie diese Zelle NICHT aus!** Sie würde nie aufhören!

```python
# ⚠️ NICHT AUSFÜHREN! Dies ist eine Endlosschleife:
x = 0
while x < 10:
    print(x)  # x wird ausgegeben, aber nie verändert!
```

**Was ist das Problem?**
- `x` startet bei 0
- Die Bedingung `x < 10` ist WAHR (0 < 10)
- `x` wird ausgegeben
- Die Schleife wiederholt sich
- **Aber:** `x` ist immer noch 0!
- Die Bedingung `x < 10` ist immer noch WAHR
- Die Schleife läuft ewig weiter...

**Wie man das verhindert:**
Man muss die Variable ändern, die in der Bedingung geprüft wird!

```python
# ✅ So ist es richtig:
x = 0
while x < 10:
    print(x)
    x = x + 1  # WICHTIG! x wird verändert!
```

+++

### Was tun, wenn eine Endlosschleife läuft?

**Keine Panik!** Falls Sie versehentlich eine Endlosschleife starten:

1. **In Jupyter Notebook:** Klicken Sie auf den "Stop"-Button (■) in der Symbolleiste
2. **In der Konsole/Terminal:** Drücken Sie `Strg+C` (Windows/Linux) oder `Cmd+C` (Mac)
3. **Notfall:** Schließen Sie das Programm-Fenster

**Tipp:** Wenn Sie unsicher sind, ob Ihre Schleife endet:
- Fügen Sie einen Zähler hinzu
- Begrenzen Sie die maximale Anzahl der Durchläufe
- Prüfen Sie, ob die Variable in der Bedingung wirklich verändert wird

+++

### Endlosschleifen mit Absicht: while True

Manchmal **will** man eine Endlosschleife! Zum Beispiel, wenn man nicht weiß, wie oft etwas wiederholt werden muss.

**Beispiel:** Eingabe-Validierung - wir wollen so lange fragen, bis eine gültige Eingabe kommt:

```{code-cell} ipython3
# Endlosschleife mit break - Eingabe validieren

print("Bitte geben Sie eine Zahl zwischen 1 und 10 ein.")

while True:  # Endlosschleife!
    zahl = input("Zahl: ")
    
    # Prüfen, ob die Zahl gültig ist
    if 1 <= int(zahl) <= 10:
        break  # Schleife beenden - Zahl ist in Ordnung!
    else:
        print("Die Zahl muss zwischen 1 und 10 liegen.")

print("Danke für die Zahl:", zahl)
```

**Was passiert hier?**

1. `while True` startet eine Endlosschleife (True ist immer wahr!)
2. Benutzer wird nach einer Zahl gefragt
3. **Falls die Zahl zwischen 1 und 10 liegt:**
   - `break` wird ausgeführt
   - Die Schleife wird **sofort beendet**
4. **Falls die Zahl außerhalb des Bereichs liegt:**
   - Fehlermeldung wird ausgegeben
   - Die Schleife läuft erneut (fragt wieder nach einer Zahl)

**Das `break`-Schlüsselwort** ist hier entscheidend:
- Es beendet die Schleife sofort
- Es springt zur ersten Zeile nach der Schleife
- Ohne `break` würde die Schleife ewig laufen!

Mehr zu `break` und `continue` lernen Sie gleich!

+++

### 🏃 Sofort ausprobieren!

**Aufgabe 1:** Schreiben Sie ein Programm mit einer while True-Schleife, das so lange nach einem Passwort fragt, bis "1234" eingegeben wird.

```{code-cell} ipython3
# Ihr Code hier:
```

**Aufgabe 2:** Erweitern Sie das Programm: Nach 3 falschen Versuchen soll das Programm mit "Zugang gesperrt!" enden.

```{code-cell} ipython3
# Ihr Code hier:
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1: Passwort-Abfrage
print("Passwort-Schutz")

while True:
    passwort = input("Passwort: ")
    if passwort == "1234":
        print("Zugang gewährt!")
        break
    else:
        print("Falsches Passwort!")

# Aufgabe 2: Mit maximalen Versuchen
print("Passwort-Schutz")
versuche = 0

while True:
    passwort = input("Passwort: ")
    if passwort == "1234":
        print("Zugang gewährt!")
        break
    else:
        versuche = versuche + 1
        if versuche >= 3:
            print("Zugang gesperrt!")
            break
        print("Falsches Passwort! Versuche übrig:", 3 - versuche)
```
</details>

+++

### Praktische Übung: Bestandsaufnahme mit While-Schleife 📦

Jetzt kombinieren wir While-Schleifen mit Dictionaries! Sie erstellen ein Programm für eine Bestandsaufnahme.

**Ziel:** Bauteile und ihre Anzahlen in einem Dictionary speichern

```{code-cell} ipython3
# Bestandsaufnahme mit While-Schleife

# 1. Erstellen Sie ein leeres Dictionary für den Bestand
bestand = {}

# 2. Variable für die Benutzereingabe
bauteil = ""

print("Bestandsaufnahme - Geben Sie 'ENDE' ein zum Beenden")

# 3. While-Schleife: Läuft, bis Benutzer "ENDE" eingibt
while bauteil != "ENDE":
    # Bauteilname abfragen
    bauteil = input("Bauteilname: ")
    
    # Prüfen, ob Benutzer beenden möchte
    if bauteil == "ENDE":
        break  # Schleife beenden
    
    # Anzahl abfragen
    anzahl = input("Anzahl: ")
    
    # Im Dictionary speichern
    bestand[bauteil] = int(anzahl)

# Bestand ausgeben
print("\nIhr Bestand:")
print(bestand)
```

**Ihre Aufgabe:** Testen Sie das Programm!
- Geben Sie mehrere Bauteile ein (z.B. "Schrauben", "Muttern", "Bolzen")
- Geben Sie jeweils Anzahlen ein
- Beenden Sie mit "ENDE"
- Schauen Sie sich das Dictionary an!

```{code-cell} ipython3
while time <= "15.45 UHR":
    student_in_room = False
```

## For-Schleifen: Über Kollektionen iterieren 📋

### Was ist eine For-Schleife?

Eine **For-Schleife** ist wie ein Postbote, der jeden Brief in seinem Stapel einzeln zustellt:
- Der Postbote nimmt sich **für jeden** Brief aus dem Stapel
- Er bearbeitet ihn (liest die Adresse, stellt ihn zu)
- Dann nimmt er sich den nächsten Brief
- Das macht er, bis alle Briefe zugestellt sind

**Im Gegensatz zur While-Schleife:**
- **While:** "Wiederhole, **SOLANGE** eine Bedingung erfüllt ist" (wir wissen nicht, wie oft)
- **For:** "Wiederhole **FÜR JEDES** Element in einer Kollektion" (wir wissen genau, wie oft)

### Warum brauchen wir For-Schleifen?

For-Schleifen sind perfekt, wenn Sie über Dinge iterieren wollen:
- **Listen durchgehen:** Jedes Element einer Liste verarbeiten
- **Text analysieren:** Jeden Buchstaben eines Strings prüfen
- **Dictionary durchlaufen:** Jedes Schlüssel-Wert-Paar bearbeiten
- **Bestimmte Anzahl wiederholen:** Etwas genau 10 Mal machen

**Alltags-Beispiel:**
Sie haben eine Einkaufsliste und möchten jeden Artikel abhaken:
- **FÜR JEDEN** Artikel auf der Liste
- Suche ihn im Regal
- Lege ihn in den Einkaufswagen
- Hake ihn ab

Genau das macht eine For-Schleife!

+++

### Die Syntax der For-Schleife

So schreibt man eine For-Schleife in Python:

```python
for element in kollektion:
    # Dieser Code wird für jedes Element ausgeführt
```

**Wichtige Bestandteile:**
1. **`for`** - Das Schlüsselwort, das die Schleife einleitet
2. **`element`** - Eine Variable, die nacheinander jedes Element der Kollektion bekommt
3. **`in`** - Bedeutet "ist enthalten in"
4. **`kollektion`** - Die Liste, der String, das Tupel, etc., über das iteriert wird
5. **Doppelpunkt `:`** - Markiert das Ende der For-Zeile
6. **Eingerückter Code** - Wird für jedes Element ausgeführt

**Wichtig:** Der Name `element` ist frei wählbar - Sie können die Variable nennen, wie Sie möchten!

+++

### Erstes Beispiel: Über eine Liste iterieren

Schauen wir uns das einfachste Beispiel an - eine Liste von Zahlen durchgehen:

```{code-cell} ipython3
# Einfache For-Schleife über eine Liste

zahlen_liste = [5,4,3,2,1,0]

for zahl in zahlen_liste:
    print(zahl)
```

**Was passiert hier?**

1. Python nimmt das **erste Element** aus der Liste: `1`
2. Die Variable `zahl` bekommt den Wert `1`
3. Der Code im Inneren wird ausgeführt: `print(1)`
4. Python nimmt das **nächste Element**: `2`
5. Die Variable `zahl` bekommt den Wert `2`
6. Der Code wird ausgeführt: `print(2)`
7. Das geht so weiter für `3`, `4`, `5`
8. Wenn alle Elemente durch sind, ist die Schleife fertig

**Wichtig:** Die Variable `zahl` ändert sich automatisch bei jedem Durchlauf!

+++

### Beispiel: Berechnungen in der Schleife

Natürlich können wir nicht nur ausgeben, sondern auch rechnen:

```{code-cell} ipython3
# Quadrate berechnen mit For-Schleife

zahlen = [1, 2, 3, 4, 5]

for zahl in zahlen:
    quadrat = zahl ** 2  # Zahl hoch 2
    print("Das Quadrat von", zahl, "ist", quadrat)
```

**Was passiert hier?**

- **Durchlauf 1:** `zahl = 1`, `quadrat = 1 ** 2 = 1`, Ausgabe: "Das Quadrat von 1 ist 1"
- **Durchlauf 2:** `zahl = 2`, `quadrat = 2 ** 2 = 4`, Ausgabe: "Das Quadrat von 2 ist 4"
- **Durchlauf 3:** `zahl = 3`, `quadrat = 3 ** 2 = 9`, Ausgabe: "Das Quadrat von 3 ist 9"
- Und so weiter...

**Tipp:** Sie können beliebig komplexe Berechnungen im Schleifenkörper machen!

+++

### 🏃 Sofort ausprobieren!

**Aufgabe 1:** Erstellen Sie eine Liste mit den Zahlen [10, 20, 30, 40, 50] und geben Sie jede Zahl aus.

```{code-cell} ipython3
# Ihr Code hier:
liste =  [10, 20, 30, 40, 50]

for n in liste:
    print(n)
```

**Aufgabe 2:** Erstellen Sie eine Liste mit den Zahlen [2, 4, 6, 8] und geben Sie für jede Zahl aus, ob sie größer als 5 ist.

```{code-cell} ipython3
# Ihr Code hier:
liste = [2,4,6,8]
for l in liste:
    if l <= 5:
        print(f"{l} ist kleiner/gleich als 5")
    else:
        print(f"{l} ist größer als 5")
```

**Aufgabe 3:** Erstellen Sie eine Liste mit den Zahlen [1, 2, 3, 4, 5] und berechnen Sie die Summe aller Zahlen. Geben Sie am Ende aus: "Die Summe ist: X"

```{code-cell} ipython3
# Ihr Code hier:
summe = 0
liste = [1,2,3,4,5]
for x in liste:
    summe = summe + x

print(f"Die Summe ist {summe}")
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1: Liste ausgeben
zahlen = [10, 20, 30, 40, 50]
for zahl in zahlen:
    print(zahl)

# Aufgabe 2: Prüfen, ob größer als 5
zahlen = [2, 4, 6, 8]
for zahl in zahlen:
    if zahl > 5:
        print(zahl, "ist größer als 5")
    else:
        print(zahl, "ist nicht größer als 5")

# Aufgabe 3: Summe berechnen
zahlen = [1, 2, 3, 4, 5]
summe = 0  # Startwert
for zahl in zahlen:
    summe = summe + zahl  # Addiere jede Zahl zur Summe
print("Die Summe ist:", summe)
```
</details>

+++

### For-Schleifen mit Strings

For-Schleifen funktionieren nicht nur mit Listen, sondern auch mit **Strings** (Zeichenketten)!

Ein String ist wie eine Liste von Buchstaben - wir können über jeden Buchstaben einzeln iterieren:

```{code-cell} ipython3
# Über einen String iterieren

wort = "Python"

for buchstabe in wort:
    print(buchstabe)
```

**Was passiert hier?**

Python behandelt den String wie eine Liste von Zeichen:
- **Durchlauf 1:** `buchstabe = 'P'`, Ausgabe: P
- **Durchlauf 2:** `buchstabe = 'y'`, Ausgabe: y
- **Durchlauf 3:** `buchstabe = 't'`, Ausgabe: t
- **Durchlauf 4:** `buchstabe = 'h'`, Ausgabe: h
- **Durchlauf 5:** `buchstabe = 'o'`, Ausgabe: o
- **Durchlauf 6:** `buchstabe = 'n'`, Ausgabe: n

**Praktisch:** So können Sie Texte Zeichen für Zeichen analysieren!

+++

### Beispiel: Vokale zählen

```{code-cell} ipython3
# Vokale in einem Wort zählen

wort = "LAAAaaangweiligggg!"
vokale = "aeiouAEIOU"  # Alle Vokale (groß und klein)
anzahl_vokale = 0

for buchstabe in wort:
    if buchstabe in vokale:  # Ist der Buchstabe ein Vokal?
        anzahl_vokale = anzahl_vokale + 1

print("Das Wort", wort, "enthält", anzahl_vokale, "Vokale")
```

**Was passiert hier?**

1. Wir haben einen Zähler `anzahl_vokale` der bei 0 startet
2. Für jeden Buchstaben im Wort prüfen wir:
   - Ist er in der String `vokale` enthalten?
   - Falls ja: Erhöhe den Zähler um 1
3. Am Ende geben wir die Gesamtzahl aus

**Tipp:** Der `in`-Operator prüft, ob ein Zeichen in einem String vorkommt!

+++

### 🏃 Sofort ausprobieren!

**Aufgabe 1:** Schreiben Sie ein Programm, das einen String durchläuft und jeden Buchstaben einzeln mit seiner Position ausgibt (z.B. "Position 0: P", "Position 1: y", ...)

```{code-cell} ipython3
# Ihr Code hier:
# Tipp: Verwenden Sie einen Zähler, der bei 0 startet und bei jedem Durchlauf erhöht wird
zähler = 0
wort = "Ausschlafen"
for buchstabe in wort:
    print(f"Position {zähler}: {buchstabe}")
    zähler += 1
```

**Aufgabe 2:** Erweitern Sie das Vokale-Zähl-Programm: Zählen Sie sowohl Vokale als auch Konsonanten und geben Sie beide Zahlen aus.

```{code-cell} ipython3
# Ihr Code hier:
# Vokale und Konsonanten in einem Wort zählen

wort = "LAAAaaangweiligggg!!??!..."
vokale = "aeiouAEIOU"  # Alle Vokale (groß und klein)
anzahl_vokale = 0
anzahl_konsonanten = 0
for buchstabe in wort:
    if buchstabe in vokale:  # Ist der Buchstabe ein Vokal?
        # anzahl_vokale = anzahl_vokale + 1
        anzahl_vokale += 1
    elif buchstabe in " !?'.,":
        continue
    else:
        anzahl_konsonanten += 1

print("Das Wort", wort, "enthält", anzahl_vokale, "Vokale und", anzahl_konsonanten, "Konsonanten")
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1: Buchstaben mit Position
wort = "Python"
position = 0

for buchstabe in wort:
    print("Position", position, ":", buchstabe)
    position = position + 1

# Aufgabe 2: Vokale und Konsonanten zählen
wort = "Programmierung"
vokale = "aeiouAEIOU"
anzahl_vokale = 0
anzahl_konsonanten = 0

for buchstabe in wort:
    if buchstabe in vokale:
        anzahl_vokale = anzahl_vokale + 1
    else:
        anzahl_konsonanten = anzahl_konsonanten + 1

print("Vokale:", anzahl_vokale)
print("Konsonanten:", anzahl_konsonanten)
```
</details>

+++

### For-Schleifen mit Dictionaries

Auch über Dictionaries können Sie iterieren! Mit der `.items()`-Methode können Sie über Schlüssel-Wert-Paare iterieren:

```{code-cell} ipython3
# Über ein Dictionary iterieren

lager = {"Schrauben": 100, "Muttern": 75, "Bolzen": 50}

for x, y in lager.items():
    print(x, ":", y)
```

```{code-cell} ipython3
lager.items()
```

**Was passiert hier?**

1. `.items()` gibt alle Schlüssel-Wert-Paare zurück
2. In jedem Durchlauf bekommt `bauteil` den Schlüssel und `anzahl` den Wert
3. **Durchlauf 1:** `bauteil = "Schrauben"`, `anzahl = 100`
4. **Durchlauf 2:** `bauteil = "Muttern"`, `anzahl = 75`
5. **Durchlauf 3:** `bauteil = "Bolzen"`, `anzahl = 50`

**Wichtig:** Sie können die Variablen beliebig benennen - `key, value` oder `bauteil, anzahl` - beides funktioniert!

+++

### Praktische Übung: Bestandsaufnahme ausgeben 📦

Erweitern wir die Bestandsaufnahme von vorhin! Jetzt können wir sie schön formatiert ausgeben:

```{code-cell} ipython3
# Beispiel-Bestand (Sie können auch Ihren eigenen von oben verwenden)
bestand = {"Schrauben": 150, "Muttern": 120, "Bolzen": 80, "Dübel": 200}

# Überschrift
print("=== BESTANDSLISTE ===")

# Über den Bestand iterieren
for bauteil, anzahl in bestand.items():
    print(f"{bauteil}: {anzahl} Stück")

print("=====================")
```

**Ihre Aufgabe:**
1. Erweitern Sie das Programm: Berechnen Sie die **Gesamtzahl aller Bauteile**
2. Geben Sie am Ende aus: "Gesamt: X Teile im Lager"

**Tipp:** Verwenden Sie einen Zähler, der bei jedem Durchlauf erhöht wird!

```{code-cell} ipython3
# Ihr Code hier:
```

## Die range()-Funktion: Zahlenfolgen erzeugen 🔢

### Was ist range()?

Die `range()`-Funktion ist ein praktisches Werkzeug, um **Zahlenfolgen** zu erzeugen. Sie wird sehr oft mit For-Schleifen kombiniert!

**Stellen Sie sich vor:**
Sie möchten eine Aufgabe genau 10 Mal wiederholen. Mit `range()` können Sie sagen:
- "Gib mir die Zahlen von 0 bis 9" (10 Zahlen)
- "Gib mir die Zahlen von 5 bis 15"
- "Gib mir jede zweite Zahl von 0 bis 20" (0, 2, 4, 6, ...)

### Warum brauchen wir range()?

**Ohne range():**
```python
# Mühsam: Liste von Hand erstellen
zahlen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for zahl in zahlen:
    print(zahl)
```

**Mit range():**
```python
# Einfach: range() erstellt die Zahlen automatisch
for zahl in range(10):
    print(zahl)
```

Viel kürzer und flexibler!

+++

### Die drei Varianten von range()

`range()` gibt es in drei verschiedenen Varianten:

**1. range(stop)** - Von 0 bis stop-1
```python
range(5)  # Erzeugt: 0, 1, 2, 3, 4
```

**2. range(start, stop)** - Von start bis stop-1
```python
range(3, 8)  # Erzeugt: 3, 4, 5, 6, 7
```

**3. range(start, stop, step)** - Von start bis stop-1 mit Schrittweite
```python
range(0, 10, 2)  # Erzeugt: 0, 2, 4, 6, 8
```

**Wichtig:** Der `stop`-Wert ist **NICHT enthalten**! `range(5)` erzeugt 0 bis 4, nicht 0 bis 5.

+++

### Beispiel 1: range(stop) - Etwas x-mal wiederholen

```{code-cell} ipython3
# Eine Aufgabe genau 5 Mal ausführen

for i in range(5):
    print("Durchlauf Nummer:", i)
```

**Was passiert hier?**

- `range(5)` erzeugt die Zahlen: 0, 1, 2, 3, 4
- Die Schleife läuft genau **5 Mal** (für jede dieser Zahlen)
- Die Variable `i` nimmt nacheinander jeden Wert an

**Tipp:** Der Name `i` steht für "index" und wird oft für Zählvariablen verwendet!

+++

### range() in eine Liste umwandeln

Um zu sehen, welche Zahlen `range()` erzeugt, können Sie sie in eine Liste umwandeln:

```{code-cell} ipython3
# range() in Liste umwandeln, um die Zahlen zu sehen

print("range(10):", list(range(10)))
print("range(5, 15):", list(range(5, 15)))
print("range(0, 20, 3):", list(range(0, 20, 3)))
```

**Achtung:** Normalerweise brauchen Sie `list()` nicht! In der For-Schleife funktioniert `range()` direkt:

```python
for i in range(10):  # Kein list() nötig!
    print(i)
```

+++

### 🏃 Sofort ausprobieren!

**Aufgabe 1:** Erzeugen Sie mit `range()` eine Liste mit den Zahlen 0 bis 10 und geben Sie sie aus.

```{code-cell} ipython3
# Ihr Code hier:
list(range(0,11))
```

**Aufgabe 2:** Erzeugen Sie eine Liste mit den Zahlen 5 bis 10 (inklusive 10!).

```{code-cell} ipython3
# Ihr Code hier:
# Tipp: range(stop) geht BIS stop-1, also müssen Sie stop+1 verwenden!
list(range(5,11))
```

**Aufgabe 3:** Erzeugen Sie eine Liste aller geraden Zahlen von 0 bis 20 (inklusive 20).

```{code-cell} ipython3
# Ihr Code hier:
# Tipp: Verwenden Sie den step-Parameter!
list(range(2,21,2))
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1: 0 bis 10
zahlen = list(range(11))  # 11, weil range(11) 0 bis 10 erzeugt
print(zahlen)

# Aufgabe 2: 5 bis 10 (inklusive 10)
zahlen = list(range(5, 11))  # 11, damit 10 enthalten ist
print(zahlen)

# Aufgabe 3: Gerade Zahlen 0 bis 20
zahlen = list(range(0, 21, 2))  # start=0, stop=21, step=2
print(zahlen)
```
</details>

+++

### Praktisches Beispiel: Teilbarkeit prüfen

Kombinieren wir range() mit Berechnungen und Verzweigungen:

```{code-cell} ipython3
# Für die ersten 20 Zahlen prüfen, ob sie durch 2, 3 oder 5 teilbar sind

for zahl in range(1, 21):  # 1 bis 20
    teiler = []  # Liste für die Teiler
    
    # Prüfen, durch welche Zahlen teilbar
    if zahl % 2 == 0:
        teiler.append("2")
    if zahl % 3 == 0:
        teiler.append("3")
    if zahl % 5 == 0:
        teiler.append("5")
    
    # Ausgabe
    if teiler:  # Falls Liste nicht leer ist
        teiler_text = " und ".join(teiler)
        print(f"Die Zahl {zahl} ist durch {teiler_text} teilbar")
    else:
        print(f"Die Zahl {zahl} ist nicht durch 2, 3 oder 5 teilbar")
```

**Was passiert hier?**

1. Wir iterieren über die Zahlen 1 bis 20 (mit `range(1, 21)`)
2. Für jede Zahl erstellen wir eine leere Liste `teiler`
3. Wir prüfen nacheinander, ob die Zahl durch 2, 3 oder 5 teilbar ist
4. Falls ja, fügen wir den Teiler zur Liste hinzu
5. Am Ende geben wir aus, durch welche Zahlen sie teilbar ist

**Techniken, die Sie bereits kennen:**
- `%` (Modulo-Operator) aus Notebook 08
- `if`-Verzweigungen aus Notebook 09
- Listen und `.append()` aus Notebook 06
- F-Strings aus Notebook 02

+++

## Schleifensteuerung: break und continue 🛑

### Warum brauchen wir break und continue?

Manchmal möchten Sie eine Schleife **nicht komplett durchlaufen**:
- **break:** Schleife sofort beenden ("Ich bin fertig, ich höre auf!")
- **continue:** Aktuellen Durchlauf überspringen ("Dieses Element überspringe ich, weiter geht's!")

**Alltags-Beispiel:**

**break** ist wie beim Einkaufen:
- Sie haben eine Einkaufsliste
- Sie gehen Artikel für Artikel durch
- Plötzlich ist Ihr Geldbeutel leer!
- **→ Sie brechen ab und verlassen das Geschäft (break)**

**continue** ist wie beim Sortieren:
- Sie sortieren Ihre Post
- Brief für Brief durchgehen
- Ein Brief ist Werbung?
- **→ Sie überspringen ihn und machen mit dem nächsten weiter (continue)**

+++

## Das break-Statement: Schleife beenden 🛑

### Was macht break?

`break` beendet die Schleife **sofort** und **komplett**:
- Die Schleife stoppt
- Alle verbleibenden Elemente werden übersprungen
- Der Code nach der Schleife wird ausgeführt

**Wann verwendet man break?**
- **Suchen:** Element gefunden? → Abbrechen!
- **Validierung:** Fehler gefunden? → Abbrechen!
- **Begrenzung:** Maximale Anzahl erreicht? → Abbrechen!
- **Endlosschleifen:** Bedingung erfüllt? → Abbrechen!

+++

### Beispiel 1: Suche nach einer Zahl

```{code-cell} ipython3
# Suche nach der Zahl 7 in einer Liste

zahlen = [2, 4, 7, 9, 12, 15]

for zahl in zahlen:
    print("Prüfe:", zahl)
    if zahl == 7:
        print("Gefunden!")
        break  # Schleife sofort beenden!

print("Suche beendet")
```

**Was passiert hier?**

1. **Durchlauf 1:** `zahl = 2`, nicht 7, weiter
2. **Durchlauf 2:** `zahl = 4`, nicht 7, weiter
3. **Durchlauf 3:** `zahl = 7`, **gefunden!** → `break`
4. **Schleife endet sofort** (9, 12, 15 werden nicht mehr geprüft)
5. Code nach der Schleife wird ausgeführt: "Suche beendet"

**Wichtig:** Ohne `break` würde die Schleife alle Zahlen durchgehen, auch nachdem 7 gefunden wurde!

+++

### Beispiel 2: Primzahl-Prüfung

```{code-cell} ipython3
# Prüfen, ob eine Zahl eine Primzahl ist

n = int(input("Zahl: "))
ist_primzahl = True  # Annahme: Zahl ist Primzahl

for i in range(2, n):  # Prüfe alle Zahlen von 2 bis n-1
    if n % i == 0:  # Ist n durch i teilbar?
        print(n, "==", i, "*", n // i)
        ist_primzahl = False
        break  # Teiler gefunden, wir können abbrechen!

if ist_primzahl and n > 1:
    print(n, "ist eine Primzahl")
else:
    print(n, "ist keine Primzahl")
```

**Was passiert hier?**

Eine Primzahl ist nur durch 1 und sich selbst teilbar. Wenn wir **einen** Teiler finden:
1. Die Zahl ist **keine** Primzahl
2. Wir müssen **nicht weitermachen** (Zeit sparen!)
3. **break** beendet die Suche sofort

**Beispiel:** Für n = 12:
- i = 2: 12 % 2 == 0 → **Teiler gefunden! → break**
- Die Schleife endet (i = 3, 4, 5, ... werden nicht mehr geprüft)

**Effizienz:** Ohne break würden wir alle Zahlen von 2 bis 11 prüfen, obwohl wir schon bei 2 wissen, dass 12 keine Primzahl ist!

+++

### 🏃 Sofort ausprobieren!

**Aufgabe 1:** Schreiben Sie eine Schleife, die die Zahlen 1 bis 100 ausgibt, aber bei 50 abbricht.

```{code-cell} ipython3
# Ihr Code hier:
```

**Aufgabe 2:** Erstellen Sie eine Liste mit Namen. Suchen Sie nach einem bestimmten Namen und geben Sie "Gefunden!" aus, wenn er da ist. Brechen Sie die Suche ab, sobald Sie ihn gefunden haben.

```{code-cell} ipython3
# Ihr Code hier:
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1: Bis 50 zählen
for i in range(1, 101):
    print(i)
    if i == 50:
        break

# Aufgabe 2: Namen suchen
namen = ["Anna", "Ben", "Clara", "David", "Emma"]
gesuchter_name = "Clara"

for name in namen:
    print("Prüfe:", name)
    if name == gesuchter_name:
        print("Gefunden!")
        break
```
</details>

+++

## Das continue-Statement: Durchlauf überspringen ⏭️

### Was macht continue?

`continue` überspringt den **aktuellen** Durchlauf und macht mit dem **nächsten** Element weiter:
- Der Rest des aktuellen Durchlaufs wird übersprungen
- Die Schleife läuft weiter (im Gegensatz zu break!)
- Das nächste Element wird verarbeitet

**Wann verwendet man continue?**
- **Filtern:** Bestimmte Elemente überspringen
- **Validierung:** Ungültige Werte ignorieren
- **Bedingte Verarbeitung:** Nur bestimmte Elemente verarbeiten

+++

### Beispiel 1: Nur gerade Zahlen ausgeben

```{code-cell} ipython3
# Nur gerade Zahlen ausgeben, ungerade überspringen

for i in range(1, 11):
    if i % 2 != 0:  # Ist die Zahl ungerade?
        continue     # Ja → überspringen!
    
    print(i)  # Wird nur für gerade Zahlen ausgeführt
```

**Was passiert hier?**

1. **i = 1:** Ungerade (1 % 2 != 0) → `continue` → Ausgabe übersprungen
2. **i = 2:** Gerade → Keine continue → Ausgabe: 2
3. **i = 3:** Ungerade → `continue` → Ausgabe übersprungen
4. **i = 4:** Gerade → Ausgabe: 4
5. Und so weiter...

**Ergebnis:** Es werden nur 2, 4, 6, 8, 10 ausgegeben

**Wichtig:** `continue` springt zum nächsten Durchlauf, die Schleife läuft vollständig durch!

+++

### Beispiel 2: Konsonanten zählen

```{code-cell} ipython3
# Konsonanten in einem Wort zählen

wort = input("Wort: ")
vokale = "aeiouAEIOU"
anzahl_konsonanten = 0

for buchstabe in wort:
    if buchstabe in vokale:  # Ist es ein Vokal?
        continue              # Ja → überspringen!
    
    # Dieser Code wird nur für Konsonanten ausgeführt
    anzahl_konsonanten = anzahl_konsonanten + 1

print("Das Wort enthält", anzahl_konsonanten, "Konsonanten.")
```

**Was passiert hier?**

Wir zählen nur Konsonanten, Vokale sollen ignoriert werden:

Beispiel für "Python":
1. **'P':** Kein Vokal → Zähler +1 (anzahl = 1)
2. **'y':** Kein Vokal → Zähler +1 (anzahl = 2)
3. **'t':** Kein Vokal → Zähler +1 (anzahl = 3)
4. **'h':** Kein Vokal → Zähler +1 (anzahl = 4)
5. **'o':** **Vokal!** → `continue` → Zähler wird nicht erhöht
6. **'n':** Kein Vokal → Zähler +1 (anzahl = 5)

**Ergebnis:** 5 Konsonanten

**Alternative ohne continue:**
```python
for buchstabe in wort:
    if buchstabe not in vokale:  # Ist es KEIN Vokal?
        anzahl_konsonanten = anzahl_konsonanten + 1
```

Beide Varianten funktionieren - continue macht den Code manchmal lesbarer!

+++

### 🏃 Sofort ausprobieren!

**Aufgabe 1:** Schreiben Sie eine Schleife, die die Zahlen 1 bis 20 ausgibt, aber alle Zahlen überspringt, die durch 3 teilbar sind.

```{code-cell} ipython3
# Ihr Code hier:
```

**Aufgabe 2:** Erstellen Sie eine Liste mit verschiedenen Werten (Zahlen, Strings, etc.). Geben Sie nur die Zahlen aus, alle anderen Typen sollen übersprungen werden.

Tipp: Verwenden Sie `type(element) == int`

```{code-cell} ipython3
# Ihr Code hier:
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1: Durch 3 teilbare Zahlen überspringen
for i in range(1, 21):
    if i % 3 == 0:  # Durch 3 teilbar?
        continue     # Überspringen!
    print(i)

# Aufgabe 2: Nur Zahlen ausgeben
gemischt = [5, "Hallo", 42, "Welt", 7, True, 99]

for element in gemischt:
    if type(element) != int:  # Kein Integer?
        continue               # Überspringen!
    print(element)
```
</details>

+++

### break vs. continue: Der Unterschied

**Wichtig:** Verwechseln Sie break und continue nicht!

| **break** | **continue** |
|-----------|-------------|
| Beendet die **gesamte** Schleife | Überspringt nur den **aktuellen** Durchlauf |
| Springt **aus** der Schleife heraus | Springt zum **nächsten** Element |
| Code nach break wird nicht mehr ausgeführt | Code in den nächsten Durchläufen wird ausgeführt |
| Für Abbruch-Bedingungen | Für Filter-Bedingungen |

**Beispiel zum Vergleich:**

```{code-cell} ipython3
# Vergleich break vs. continue

print("Mit break:")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

print("\nMit continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

**Ausgabe:**
```
Mit break:
1
2
(Schleife endet hier!)

Mit continue:
1
2
(3 wird übersprungen)
4
5
```

+++

## List Comprehensions: Kompakte Listen erstellen 🚀

### Was sind List Comprehensions?

Eine **List Comprehension** ist eine kompakte Methode, um Listen zu erstellen oder zu transformieren - alles in einer einzigen Zeile!

**Stellen Sie sich vor:**
Sie haben eine Liste von Zahlen und möchten eine neue Liste mit den Quadraten erstellen.

**Klassische Methode:**
```python
zahlen = [1, 2, 3, 4, 5]
quadrate = []  # Leere Liste

for zahl in zahlen:
    quadrate.append(zahl ** 2)  # Jedes Quadrat hinzufügen
```

**Mit List Comprehension:**
```python
zahlen = [1, 2, 3, 4, 5]
quadrate = [zahl ** 2 for zahl in zahlen]  # Alles in einer Zeile!
```

Viel kürzer und eleganter!

### Warum List Comprehensions?

**Vorteile:**
- **Kürzer:** Eine Zeile statt fünf
- **Lesbarer:** Fokus auf das "Was", nicht das "Wie"
- **Schneller:** Python optimiert List Comprehensions intern
- **Eleganter:** Wirkt professioneller

**Achtung:** Sie sind optional! Die klassische For-Schleife funktioniert genauso gut. List Comprehensions sind nur eine praktische Abkürzung.

+++

### Die Syntax von List Comprehensions

**Grundstruktur:**
```python
[ausdruck for element in sequenz]
```

Das liest sich fast wie normales Deutsch:
- **"Erstelle eine Liste"** → `[` ... `]`
- **"mit diesem Ausdruck"** → `ausdruck`
- **"für jedes Element"** → `for element`
- **"in dieser Sequenz"** → `in sequenz`

**Beispiel:**
```python
[x ** 2 for x in [1, 2, 3, 4, 5]]
```

Gelesen: "Erstelle eine Liste mit x hoch 2 für jedes x in [1, 2, 3, 4, 5]"

+++

### Beispiel 1: Quadratzahlen erstellen

```{code-cell} ipython3
# Vergleich: For-Schleife vs. List Comprehension

zahlen = [1, 2, 3, 4, 5]

# Methode 1: Klassische For-Schleife
quadrate_klassisch = []
for x in zahlen:
    quadrate_klassisch.append(x ** 2)

print("Mit For-Schleife:", quadrate_klassisch)

# Methode 2: List Comprehension
quadrate_kompakt = [x ** 2 for x in zahlen]

print("Mit List Comprehension:", quadrate_kompakt)
```

**Was passiert hier?**

Die List Comprehension macht intern genau das Gleiche wie die For-Schleife:
1. Nehme jedes `x` aus `zahlen`
2. Berechne `x ** 2`
3. Füge das Ergebnis zur neuen Liste hinzu

**Beide Methoden liefern das gleiche Ergebnis:** `[1, 4, 9, 16, 25]`

+++

### Beispiel 2: Strings transformieren

```{code-cell} ipython3
# Namen in Großbuchstaben umwandeln

namen = ["anna", "ben", "clara", "david"]

# Mit List Comprehension
namen_gross = [name.upper() for name in namen]

print("Original:", namen)
print("Großbuchstaben:", namen_gross)
```

**Was passiert hier?**

- Für jeden `name` in der Liste `namen`
- Rufe `.upper()` auf (wandelt in Großbuchstaben um)
- Erstelle eine neue Liste mit den Ergebnissen

**Ergebnis:** `['ANNA', 'BEN', 'CLARA', 'DAVID']`

+++

### List Comprehensions mit Bedingungen

Sie können auch **Bedingungen** in List Comprehensions verwenden:

**Syntax:**
```python
[ausdruck for element in sequenz if bedingung]
```

Das bedeutet: "Nur Elemente, die die Bedingung erfüllen"

```{code-cell} ipython3
# Nur gerade Zahlen quadrieren

zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Mit List Comprehension und Bedingung
gerade_quadrate = [x ** 2 for x in zahlen if x % 2 == 0]

print("Quadrate der geraden Zahlen:", gerade_quadrate)
```

**Was passiert hier?**

1. Für jedes `x` in `zahlen`
2. **Nur wenn** `x % 2 == 0` (x ist gerade)
3. Berechne `x ** 2`
4. Füge zur Liste hinzu

**Ergebnis:** `[4, 16, 36, 64, 100]` (Quadrate von 2, 4, 6, 8, 10)

+++

### 🏃 Sofort ausprobieren!

**Aufgabe 1:** Erstellen Sie mit einer List Comprehension eine Liste mit den Zahlen 0 bis 9.

```{code-cell} ipython3
# Ihr Code hier:
# Tipp: Kombinieren Sie List Comprehension mit range()
```

**Aufgabe 2:** Erstellen Sie eine Liste mit den Zahlen 1 bis 20, aber nur die Zahlen, die durch 3 teilbar sind.

```{code-cell} ipython3
# Ihr Code hier:
```

**Aufgabe 3:** Gegeben ist eine Liste von Preisen. Erstellen Sie eine neue Liste, in der auf jeden Preis 19% Mehrwertsteuer aufgeschlagen wird.

```{code-cell} ipython3
# Ihr Code hier:
preise_netto = [10.0, 25.5, 100.0, 5.99]
# Erstellen Sie preise_brutto mit 19% Aufschlag
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1: Zahlen 0 bis 9
zahlen = [x for x in range(10)]
print(zahlen)

# Aufgabe 2: Durch 3 teilbare Zahlen
durch_drei = [x for x in range(1, 21) if x % 3 == 0]
print(durch_drei)  # [3, 6, 9, 12, 15, 18]

# Aufgabe 3: Preise mit Mehrwertsteuer
preise_netto = [10.0, 25.5, 100.0, 5.99]
preise_brutto = [preis * 1.19 for preis in preise_netto]
print(preise_brutto)
```
</details>

+++

### Praktische Übung: Maschinenauslastung berechnen 🏭

Jetzt kombinieren wir alles, was Sie gelernt haben! Sie erstellen ein Programm zur Berechnung der Maschinenauslastung.

```{code-cell} ipython3
# Maschinenauslastung für eine Woche berechnen

# 1. Maximale Stückzahl pro Tag eingeben
max_stueckzahl = int(input("Maximale Stückzahl pro Tag: "))

# 2. Produktionszahlen für 5 Tage (Montag bis Freitag) eingeben
print("\nGeben Sie die Produktionszahlen ein:")
tage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]
produktion = []

for tag in tage:
    anzahl = int(input(f"{tag}: "))
    produktion.append(anzahl)

# 3. Auslastung in Prozent berechnen (mit List Comprehension)
auslastung = [ist / max_stueckzahl * 100 for ist in produktion]

# 4. Verbleibende Kapazität berechnen (mit List Comprehension)
verbleibend = [max_stueckzahl - ist for ist in produktion]

# 5. Gesamt-Produktion und Gesamt-Auslastung berechnen
gesamt_produktion = 0
for anzahl in produktion:
    gesamt_produktion = gesamt_produktion + anzahl

gesamt_max = max_stueckzahl * 5  # 5 Tage
gesamt_auslastung = gesamt_produktion / gesamt_max * 100

# 6. Mittelwert der Auslastungen berechnen
summe_auslastung = 0
for wert in auslastung:
    summe_auslastung = summe_auslastung + wert
durchschnitt_auslastung = summe_auslastung / 5

# 7. Ergebnisse ausgeben
print("\n=== AUSWERTUNG ===")
print("\nTagesauslastungen:")
for i in range(5):
    print(f"{tage[i]}: {produktion[i]} Stück ({auslastung[i]:.1f}%) - Verbleibend: {verbleibend[i]}")

print(f"\nGesamt-Produktion: {gesamt_produktion} Stück")
print(f"Gesamt-Auslastung: {gesamt_auslastung:.1f}%")
print(f"Durchschnittliche Auslastung: {durchschnitt_auslastung:.1f}%")
```

**Was haben wir hier kombiniert?**

- **For-Schleifen:** Produktionszahlen eingeben
- **List Comprehensions:** Auslastung und verbleibende Kapazität berechnen
- **Listen:** Daten speichern
- **Berechnungen:** Prozente und Summen
- **F-Strings:** Schöne Ausgabe

**Testen Sie das Programm!**
- Geben Sie z.B. als Maximum 100 ein
- Geben Sie verschiedene Produktionszahlen ein (z.B. 80, 95, 70, 100, 85)
- Schauen Sie sich die Auswertung an!

+++

## Zusammenfassung 🎓

### Was Sie gelernt haben:

**While-Schleifen:**
- Wiederholen Code, **solange** eine Bedingung erfüllt ist
- Perfekt, wenn Sie nicht wissen, wie oft wiederholt werden muss
- Syntax: `while bedingung: code`
- Achtung vor Endlosschleifen!

**For-Schleifen:**
- Iterieren über Kollektionen (Listen, Strings, Dictionaries, etc.)
- Perfekt, wenn Sie über alle Elemente gehen wollen
- Syntax: `for element in kollektion: code`
- Funktioniert mit Listen, Strings, range(), Dictionaries, etc.

**Die range()-Funktion:**
- Erzeugt Zahlenfolgen
- `range(stop)` → 0 bis stop-1
- `range(start, stop)` → start bis stop-1
- `range(start, stop, step)` → mit Schrittweite

**Schleifensteuerung:**
- `break` → Beendet die gesamte Schleife sofort
- `continue` → Überspringt den aktuellen Durchlauf, Schleife läuft weiter

**List Comprehensions:**
- Kompakte Syntax zum Erstellen von Listen
- `[ausdruck for element in sequenz]`
- Optional mit Bedingung: `[ausdruck for element in sequenz if bedingung]`
- Kürzer und eleganter als klassische For-Schleifen

+++

## Trainingsmaterial 💪

Jetzt sind Sie dran! Üben Sie das Gelernte mit diesen Aufgaben.

+++

### 🟢 Einfache Aufgaben (zum Warmwerden)

**Aufgabe 1:** Schreiben Sie eine While-Schleife, die von 10 bis 1 runterzählt und dann "Start!" ausgibt.

```{code-cell} ipython3
# Ihr Code hier:
```

**Aufgabe 2:** Erstellen Sie eine Liste mit 5 Früchten und geben Sie jede Frucht mit einer For-Schleife aus.

```{code-cell} ipython3
# Ihr Code hier:
```

**Aufgabe 3:** Verwenden Sie range() und eine For-Schleife, um die Zahlen 1 bis 10 auszugeben.

```{code-cell} ipython3
# Ihr Code hier:
```

**Aufgabe 4:** Erstellen Sie mit einer List Comprehension eine Liste mit den Zahlen 1 bis 10, verdoppelt (2, 4, 6, ..., 20).

```{code-cell} ipython3
# Ihr Code hier:
```

### 🟡 Mittlere Aufgaben (schon besser!)

**Aufgabe 5:** Schreiben Sie ein Programm, das eine Zahl rät (zwischen 1 und 10). Der Benutzer hat maximal 3 Versuche. Verwenden Sie eine While-Schleife mit einem Zähler.

```{code-cell} ipython3
# Ihr Code hier:
# Tipp: Setzen Sie die zu ratende Zahl fest (z.B. zahl = 7)
```

**Aufgabe 6:** Erstellen Sie ein Dictionary mit Produkten und Preisen. Geben Sie alle Produkte aus, die teurer als 10 Euro sind. Verwenden Sie eine For-Schleife mit if-Bedingung.

```{code-cell} ipython3
# Ihr Code hier:
```

**Aufgabe 7:** Schreiben Sie eine Funktion `summe_bis(n)`, die die Summe aller Zahlen von 1 bis n berechnet. Verwenden Sie eine For-Schleife mit range().

```{code-cell} ipython3
# Ihr Code hier:

# Testen Sie die Funktion:
# summe_bis(5) sollte 15 ergeben (1+2+3+4+5)
# summe_bis(10) sollte 55 ergeben
```

### 🔴 Herausforderungen (für Profis)

**Aufgabe 8:** Schreiben Sie eine Funktion `fibonacci(n)`, die die ersten n Zahlen der Fibonacci-Folge in einer Liste zurückgibt. Die Fibonacci-Folge beginnt mit 0 und 1, und jede weitere Zahl ist die Summe der beiden vorherigen.

Beispiel: fibonacci(7) → [0, 1, 1, 2, 3, 5, 8]

```{code-cell} ipython3
# Ihr Code hier:
# Tipp: Starten Sie mit [0, 1] und fügen Sie in einer Schleife weitere Zahlen hinzu
```

**Aufgabe 9:** Erstellen Sie ein Programm zur Kennwort-Validierung:
- Benutzer gibt ein Kennwort ein
- Prüfen Sie: Mindestens 8 Zeichen, enthält mindestens eine Zahl, enthält mindestens einen Großbuchstaben
- Geben Sie aus, welche Anforderungen erfüllt/nicht erfüllt sind
- Wiederholen Sie die Eingabe, bis alle Anforderungen erfüllt sind

Verwenden Sie: While-Schleife, For-Schleife (zum Durchgehen des Kennworts), if-Bedingungen

```{code-cell} ipython3
# Ihr Code hier:
```

### Musterlösungen

<details>
<summary>🔍 Klicken Sie hier für die Lösungen</summary>

```python
# Aufgabe 1: Countdown
x = 10
while x >= 1:
    print(x)
    x = x - 1
print("Start!")

# Aufgabe 2: Früchte ausgeben
fruechte = ["Apfel", "Banane", "Orange", "Birne", "Traube"]
for frucht in fruechte:
    print(frucht)

# Aufgabe 3: Zahlen 1 bis 10
for i in range(1, 11):
    print(i)

# Aufgabe 4: Verdoppelte Zahlen
verdoppelt = [x * 2 for x in range(1, 11)]
print(verdoppelt)

# Aufgabe 5: Zahlenraten
geheimzahl = 7
versuche = 0
max_versuche = 3

while versuche < max_versuche:
    tipp = int(input("Rate die Zahl (1-10): "))
    versuche = versuche + 1
    
    if tipp == geheimzahl:
        print("Richtig! Gratuliere!")
        break
    elif versuche < max_versuche:
        print(f"Falsch! Noch {max_versuche - versuche} Versuche übrig.")
    else:
        print(f"Leider verloren! Die Zahl war {geheimzahl}.")

# Aufgabe 6: Teure Produkte
produkte = {"Buch": 15.99, "Stift": 1.50, "Lampe": 25.00, "Heft": 2.99}

print("Produkte über 10 Euro:")
for produkt, preis in produkte.items():
    if preis > 10:
        print(f"{produkt}: {preis} Euro")

# Aufgabe 7: Summe bis n
def summe_bis(n):
    summe = 0
    for i in range(1, n + 1):
        summe = summe + i
    return summe

# Test
print(summe_bis(5))   # 15
print(summe_bis(10))  # 55

# Aufgabe 8: Fibonacci
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    folge = [0, 1]
    for i in range(2, n):
        naechste = folge[i-1] + folge[i-2]
        folge.append(naechste)
    
    return folge

# Test
print(fibonacci(7))  # [0, 1, 1, 2, 3, 5, 8]

# Aufgabe 9: Kennwort-Validierung
def kennwort_pruefen(kennwort):
    # Bedingungen prüfen
    laenge_ok = len(kennwort) >= 8
    
    hat_zahl = False
    hat_grossbuchstabe = False
    
    for zeichen in kennwort:
        if zeichen.isdigit():
            hat_zahl = True
        if zeichen.isupper():
            hat_grossbuchstabe = True
    
    # Feedback geben
    print("\nKennwort-Prüfung:")
    if laenge_ok:
        print("✓ Mindestens 8 Zeichen")
    else:
        print("✗ Zu kurz (mindestens 8 Zeichen)")
    
    if hat_zahl:
        print("✓ Enthält mindestens eine Zahl")
    else:
        print("✗ Keine Zahl enthalten")
    
    if hat_grossbuchstabe:
        print("✓ Enthält mindestens einen Großbuchstaben")
    else:
        print("✗ Kein Großbuchstabe enthalten")
    
    return laenge_ok and hat_zahl and hat_grossbuchstabe

# Hauptprogramm
print("Kennwort-Anforderungen:")
print("- Mindestens 8 Zeichen")
print("- Mindestens eine Zahl")
print("- Mindestens ein Großbuchstabe\n")

while True:
    kennwort = input("Geben Sie ein Kennwort ein: ")
    
    if kennwort_pruefen(kennwort):
        print("\n✓ Kennwort ist gültig!")
        break
    else:
        print("\nBitte versuchen Sie es erneut.\n")
```
</details>

+++

## Glückwunsch! 🎉

Sie haben das Schleifen-Notebook erfolgreich abgeschlossen!

### Was Sie jetzt können:
- ✅ While-Schleifen für bedingte Wiederholungen schreiben
- ✅ For-Schleifen für Iterationen über Kollektionen verwenden
- ✅ Mit range() Zahlenfolgen erzeugen
- ✅ Schleifen mit break und continue steuern
- ✅ List Comprehensions für kompakte Listen-Erstellung nutzen

**Im nächsten Notebook (11 - Fehlerbehandlung)** lernen Sie:
- Wie Sie Programme gegen Fehler absichern
- Was try-except-finally bedeutet
- Wie Sie mit Fehlern elegant umgehen

**Bis zum nächsten Mal!** 👋
