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

# 08 - Operatoren: Die Werkzeuge für Berechnungen und Entscheidungen 🔧

## Willkommen! 👋

Herzlich willkommen zu einem der wichtigsten Themen in Python! In diesem Notebook lernst du die **Operatoren** kennen - die grundlegenden Werkzeuge, mit denen du Berechnungen durchführst, Werte vergleichst und logische Entscheidungen triffst.

Stell dir vor, du hast einen Werkzeugkasten. Darin befinden sich verschiedene Werkzeuge: ein Hammer, eine Säge, eine Zange. Jedes Werkzeug hat eine spezielle Aufgabe. Genau so ist es mit Operatoren in Python - sie sind deine Werkzeuge zum Programmieren!

## Was du heute lernst:
- **Arithmetische Operatoren**: Wie du mit Zahlen rechnest (+, -, *, /, %, **)
- **Vergleichsoperatoren**: Wie du Werte miteinander vergleichst (==, !=, >, <, >=, <=)
- **Logische Operatoren**: Wie du mehrere Bedingungen kombinierst (and, or, not)
- **Spezielle Operatoren**: Wie du Zugehörigkeit und Identität prüfst (in, not in, is, is not)

## Voraussetzungen 📚
Was du schon können solltest:
- Ausgabe mit `print()` und Eingabe mit `input()`
- Variablen erstellen und verwenden
- Einfache Datentypen kennen (int, float, str, bool)
- Komplexe Datentypen nutzen (Listen, Tupel, Sets, Dictionaries)
- Funktionen definieren mit `def` und Werte zurückgeben mit `return`

**Wichtig**: In diesem Notebook lernen wir nur die Operatoren kennen. Wie man damit Entscheidungen trifft (if-else) und Wiederholungen macht (Schleifen), lernst du in den nächsten Notebooks!

+++

## 1. Arithmetische Operatoren: Rechnen mit Python 🧮

### Was sind arithmetische Operatoren?

Stell dir vor, du hast einen Taschenrechner vor dir. Mit den Tasten +, -, ×, ÷ kannst du verschiedene Berechnungen durchführen. Genau das sind arithmetische Operatoren in Python - deine Rechenwerkzeuge!

Warum brauchen wir diese Operatoren? In fast jedem Programm müssen wir irgendwann rechnen: Preise berechnen, Mengen addieren, Durchschnitte ermitteln, Rabatte abziehen. Ohne arithmetische Operatoren wäre das unmöglich!

Python bietet dir sechs grundlegende arithmetische Operatoren. Jeder hat eine spezielle Aufgabe:

- Der **Plus-Operator (+)** addiert zwei Zahlen - wie wenn du zwei Stapel Münzen zusammenlegst
- Der **Minus-Operator (-)** subtrahiert - wie wenn du aus deinem Geldbeutel Geld herausnimmst
- Der **Mal-Operator (*)** multipliziert - wie wenn du drei Tüten mit je 5 Äpfeln hast (3 × 5 = 15 Äpfel)
- Der **Geteilt-Operator (/)** dividiert - wie wenn du einen Kuchen in gleich große Stücke teilst
- Der **Modulo-Operator (%)** gibt den Rest einer Division zurück - wie die übrigen Stücke, wenn du nicht alles gleichmäßig teilen kannst
- Der **Potenz-Operator (**)** potenziert - wie wenn du eine Zahl mehrmals mit sich selbst multiplizierst

Diese Operatoren sind die Grundlage für alle Berechnungen in Python. Du wirst sie in praktisch jedem Programm verwenden!

+++

### Die arithmetischen Operatoren im Überblick

Hier sind alle sechs arithmetischen Operatoren mit ihrer Bedeutung:

| Operator | Name | Beschreibung | Beispiel | Ergebnis |
|----------|------|--------------|----------|----------|
| `+` | Addition | Addiert zwei Zahlen | `10 + 3` | `13` |
| `-` | Subtraktion | Zieht die zweite von der ersten Zahl ab | `10 - 3` | `7` |
| `*` | Multiplikation | Multipliziert zwei Zahlen | `10 * 3` | `30` |
| `/` | Division | Teilt die erste durch die zweite Zahl | `10 / 3` | `3.333...` |
| `%` | Modulo | Gibt den Rest der Division zurück | `10 % 3` | `1` |
| `**` | Potenz | Potenziert die erste mit der zweiten Zahl | `10 ** 3` | `1000` |

+++

### Der Plus-Operator (+): Addition

Der Plus-Operator ist der einfachste Operator. Er addiert zwei Zahlen miteinander. Das kennst du aus der Schule!

**Praxisbeispiel**: Du hast in deinem Lager 150 Produkteinheiten. Heute kommen 45 neue Einheiten dazu. Wie viele hast du jetzt insgesamt?

```{code-cell} ipython3
# Addition: Zwei Zahlen zusammenzählen
lager_aktuell = 150
neue_lieferung = 45
lager_neu = lager_aktuell + neue_lieferung

print(f"Vorher: {lager_aktuell} Einheiten")
print(f"Neue Lieferung: {neue_lieferung} Einheiten")
print(f"Nachher: {lager_neu} Einheiten")
```

### 🏃 Sofort ausprobieren!

**Aufgabe 1:** Du hast 23 Euro in deiner Geldbörse. Du bekommst 17 Euro Taschengeld. Berechne, wie viel Geld du jetzt hast.

```{code-cell} ipython3
# Dein Code hier:
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# Lösung:
geld_vorher = 23
taschengeld = 17
geld_nachher = geld_vorher + taschengeld

print(f"Du hast jetzt {geld_nachher} Euro")
# Ausgabe: Du hast jetzt 40 Euro
```
</details>

+++

### Der Minus-Operator (-): Subtraktion

Der Minus-Operator zieht eine Zahl von einer anderen ab. Auch das kennst du aus dem Alltag!

**Praxisbeispiel**: Von deinem Gehalt von 2500 Euro gehen 450 Euro Miete ab. Wie viel bleibt dir?

```{code-cell} ipython3
# Subtraktion: Eine Zahl von einer anderen abziehen
gehalt = 2500
miete = 450
verfuegbar = gehalt - miete

print(f"Gehalt: {gehalt} Euro")
print(f"Miete: {miete} Euro")
print(f"Verfügbar: {verfuegbar} Euro")
```

### 🏃 Sofort ausprobieren!

**Aufgabe 2:** Eine Maschine produziert 500 Teile pro Tag. Heute sind 87 Teile defekt. Wie viele funktionierende Teile gibt es?

```{code-cell} ipython3
# Dein Code hier:
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# Lösung:
produktion_gesamt = 500
defekt = 87
funktionierende = produktion_gesamt - defekt

print(f"Funktionierende Teile: {funktionierende}")
# Ausgabe: Funktionierende Teile: 413
```
</details>

+++

### Der Mal-Operator (*): Multiplikation

Der Mal-Operator multipliziert zwei Zahlen miteinander. Das ist wie wiederholtes Addieren!

**Praxisbeispiel**: Ein Artikel kostet 15 Euro. Du kaufst 4 Stück. Was zahlst du insgesamt?

```{code-cell} ipython3
# Multiplikation: Zwei Zahlen miteinander malnehmen
preis_pro_artikel = 15
anzahl = 4
gesamtpreis = preis_pro_artikel * anzahl

print(f"Preis pro Artikel: {preis_pro_artikel} Euro")
print(f"Anzahl: {anzahl} Stück")
print(f"Gesamtpreis: {gesamtpreis} Euro")
```

### 🏃 Sofort ausprobieren!

**Aufgabe 3:** Eine Arbeitsschicht dauert 8 Stunden. Wie viele Stunden arbeitest du in 5 Tagen?

```{code-cell} ipython3
# Dein Code hier:
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# Lösung:
stunden_pro_tag = 8
anzahl_tage = 5
stunden_gesamt = stunden_pro_tag * anzahl_tage

print(f"In {anzahl_tage} Tagen arbeitest du {stunden_gesamt} Stunden")
# Ausgabe: In 5 Tagen arbeitest du 40 Stunden
```
</details>

+++

### Der Geteilt-Operator (/): Division

Der Geteilt-Operator teilt eine Zahl durch eine andere. Das Ergebnis ist **immer** eine Kommazahl (float), auch wenn die Division aufgeht!

**Praxisbeispiel**: Du hast 100 Euro und willst sie gleichmäßig auf 4 Personen aufteilen. Wie viel bekommt jede Person?

```{code-cell} ipython3
# Division: Eine Zahl durch eine andere teilen
geld_gesamt = 100
anzahl_personen = 4
geld_pro_person = geld_gesamt / anzahl_personen

print(f"Gesamtbetrag: {geld_gesamt} Euro")
print(f"Anzahl Personen: {anzahl_personen}")
print(f"Pro Person: {geld_pro_person} Euro")
```

### 🏃 Sofort ausprobieren!

**Aufgabe 4:** Eine Strecke von 450 Kilometern wird in 5 Stunden zurückgelegt. Berechne die Durchschnittsgeschwindigkeit.

```{code-cell} ipython3
# Dein Code hier:
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# Lösung:
strecke = 450
zeit = 5
geschwindigkeit = strecke / zeit

print(f"Durchschnittsgeschwindigkeit: {geschwindigkeit} km/h")
# Ausgabe: Durchschnittsgeschwindigkeit: 90.0 km/h
```
</details>

+++

### Der Modulo-Operator (%): Der Rest der Division

Der Modulo-Operator ist etwas speziell. Er gibt nicht das Ergebnis der Division zurück, sondern den **Rest**!

**Beispiel**: 10 geteilt durch 3 ist 3, Rest 1. Der Modulo-Operator gibt dir diese 1 zurück.

**Praxisbeispiel**: Du hast 23 Schokoladenstücke und willst sie auf 4 Kinder aufteilen. Jedes Kind bekommt 5 Stücke (23 ÷ 4 = 5). Wie viele Stücke bleiben übrig?

```{code-cell} ipython3
# Modulo: Den Rest einer Division berechnen
schokolade = 23
kinder = 4
pro_kind = schokolade // kinder  # Ganzzahlige Division (noch nicht eingeführt, daher anders)
rest = schokolade % kinder

print(f"Schokoladenstücke: {schokolade}")
print(f"Anzahl Kinder: {kinder}")
print(f"Es bleiben {rest} Stücke übrig")
```

**Wichtiger Hinweis**: Im obigen Beispiel haben wir `//` verwendet - das ist die **ganzzahlige Division**. Sie ist noch nicht offiziell eingeführt, aber für das Beispiel nötig. Du musst sie noch nicht verstehen!

**Wann ist Modulo nützlich?**
- Um zu prüfen, ob eine Zahl gerade ist (Zahl % 2 == 0)
- Um zu prüfen, ob eine Zahl durch eine andere teilbar ist
- Bei zyklischen Abläufen (z.B. Wochentage)

+++

### 🏃 Sofort ausprobieren!

**Aufgabe 5:** Was ist der Rest, wenn du 47 durch 5 teilst?

```{code-cell} ipython3
# Dein Code hier:
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# Lösung:
zahl = 47
teiler = 5
rest = zahl % teiler

print(f"Der Rest von {zahl} geteilt durch {teiler} ist: {rest}")
# Ausgabe: Der Rest von 47 geteilt durch 5 ist: 2
# (Erklärung: 47 ÷ 5 = 9, Rest 2, denn 5×9 = 45, und 47-45 = 2)
```
</details>

+++

### Der Potenz-Operator (**): Potenzierung

Der Potenz-Operator potenziert eine Zahl. Das bedeutet: Er multipliziert eine Zahl mehrmals mit sich selbst.

**Beispiel**: 2³ ("2 hoch 3") bedeutet: 2 × 2 × 2 = 8

**Praxisbeispiel**: Eine Bakterienkultur verdoppelt sich jede Stunde. Nach 5 Stunden hast du 2⁵ = 32-mal so viele Bakterien wie am Anfang.

```{code-cell} ipython3
# Potenzierung: Eine Zahl hoch eine andere
basis = 2
exponent = 5
ergebnis = basis ** exponent

print(f"{basis} hoch {exponent} = {ergebnis}")
print(f"Das bedeutet: {basis} × {basis} × {basis} × {basis} × {basis} = {ergebnis}")
```

### 🏃 Sofort ausprobieren!

**Aufgabe 6:** Berechne 3 hoch 4 (3⁴).

```{code-cell} ipython3
# Dein Code hier:
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# Lösung:
basis = 3
exponent = 4
ergebnis = basis ** exponent

print(f"{basis} hoch {exponent} = {ergebnis}")
# Ausgabe: 3 hoch 4 = 81
# (Erklärung: 3 × 3 × 3 × 3 = 81)
```
</details>

+++

### Alle arithmetischen Operatoren zusammen

Schauen wir uns alle Operatoren noch einmal in einem praktischen Beispiel an:

```{code-cell} ipython3
def taschenrechner(a,b):
    print(f"Zahl a: {a}")
    print(f"Zahl b: {b}")
    print()
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraktion: {a} - {b} = {a - b}")
    print(f"Multiplikation: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Modulo (Rest): {a} % {b} = {a % b}")
    print(f"Potenz: {a} ** {b} = {a ** b}")

taschenrechner(int(input("Zahl1")), int(input("Zahl2:")))
```

### 🏃 Große Übung: Arithmetische Operatoren

**Aufgabe 7:** Schreibe eine Funktion `berechne_alles()`, die zwei Zahlen als Parameter erhält und alle sechs arithmetischen Operationen durchführt. Die Funktion soll die Ergebnisse mit `print()` ausgeben.

**Beispiel**: `berechne_alles(15, 4)` soll ausgeben:
```
Addition: 15 + 4 = 19
Subtraktion: 15 - 4 = 11
...
```

```{code-cell} ipython3
# Dein Code hier:
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# Lösung:
def berechne_alles(zahl1, zahl2):
    print(f"Addition: {zahl1} + {zahl2} = {zahl1 + zahl2}")
    print(f"Subtraktion: {zahl1} - {zahl2} = {zahl1 - zahl2}")
    print(f"Multiplikation: {zahl1} * {zahl2} = {zahl1 * zahl2}")
    print(f"Division: {zahl1} / {zahl2} = {zahl1 / zahl2}")
    print(f"Modulo: {zahl1} % {zahl2} = {zahl1 % zahl2}")
    print(f"Potenz: {zahl1} ** {zahl2} = {zahl1 ** zahl2}")

# Testen:
berechne_alles(15, 4)
```
</details>

+++

## 2. Vergleichsoperatoren: Werte miteinander vergleichen ⚖️

### Was sind Vergleichsoperatoren?

Stell dir vor, du bist Richter in einer Gerichtsverhandlung. Jemand behauptet: "A ist größer als B". Deine Aufgabe ist es zu entscheiden: Ist das wahr oder falsch? Genau das machen Vergleichsoperatoren - sie vergleichen zwei Werte und geben **True** (wahr) oder **False** (falsch) zurück.

Warum brauchen wir Vergleichsoperatoren? Im echten Leben vergleichen wir ständig Dinge: Ist das Produkt teurer als mein Budget? Ist die Temperatur höher als 30 Grad? Hat der Kunde genug Guthaben? Ohne Vergleiche könnten unsere Programme keine Entscheidungen treffen!

Python bietet dir sechs Vergleichsoperatoren:

- **==** (gleich): Sind zwei Werte identisch?
- **!=** (ungleich): Sind zwei Werte verschieden?
- **>** (größer): Ist der linke Wert größer als der rechte?
- **<** (kleiner): Ist der linke Wert kleiner als der rechte?
- **>=** (größer oder gleich): Ist der linke Wert größer oder gleich dem rechten?
- **<=** (kleiner oder gleich): Ist der linke Wert kleiner oder gleich dem rechten?

Das Ergebnis eines Vergleichs ist immer ein **boolescher Wert** (bool): entweder `True` oder `False`. Das kennst du bereits aus Notebook 05!

+++

### Die Vergleichsoperatoren im Überblick

| Operator | Name | Bedeutung | Beispiel | Ergebnis |
|----------|------|-----------|----------|----------|
| `==` | Gleich | Sind beide Werte gleich? | `5 == 5` | `True` |
| `!=` | Ungleich | Sind beide Werte verschieden? | `5 != 3` | `True` |
| `>` | Größer | Ist links größer als rechts? | `5 > 3` | `True` |
| `<` | Kleiner | Ist links kleiner als rechts? | `5 < 3` | `False` |
| `>=` | Größer oder gleich | Ist links größer oder gleich rechts? | `5 >= 5` | `True` |
| `<=` | Kleiner oder gleich | Ist links kleiner oder gleich rechts? | `5 <= 3` | `False` |

+++

### Der Gleich-Operator (==): Sind zwei Werte identisch?

Der Gleich-Operator prüft, ob zwei Werte exakt gleich sind. **Achtung**: Es sind zwei Gleichheitszeichen (`==`), nicht eins!

**Wichtig**: `=` ist Zuweisung (Variable = Wert), `==` ist Vergleich!

**Praxisbeispiel**: Ein Kunde gibt den PIN-Code 1234 ein. Ist das der richtige Code?

```{code-cell} ipython3
# Gleich-Operator: Sind zwei Werte identisch?
richtiger_pin = "1234"
eingegebener_pin = "12347"
ist_korrekt = richtiger_pin == eingegebener_pin

print(f"Richtiger PIN: {richtiger_pin}")
print(f"Eingegebener PIN: {eingegebener_pin}")
print(f"PIN korrekt? {ist_korrekt}")
```

### 🏃 Sofort ausprobieren!

**Aufgabe 1:** Prüfe, ob die Zahl 42 gleich 42 ist. Prüfe auch, ob 42 gleich 43 ist.

```{code-cell} ipython3
# Dein Code hier:
print(42==43)
print(42==42)
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# Lösung:
zahl1 = 42
zahl2 = 42
zahl3 = 43

print(f"Ist {zahl1} gleich {zahl2}? {zahl1 == zahl2}")
print(f"Ist {zahl1} gleich {zahl3}? {zahl1 == zahl3}")
# Ausgabe:
# Ist 42 gleich 42? True
# Ist 42 gleich 43? False
```
</details>

+++

### Der Ungleich-Operator (!=): Sind zwei Werte verschieden?

Der Ungleich-Operator ist das Gegenteil vom Gleich-Operator. Er gibt `True` zurück, wenn die Werte **verschieden** sind.

**Praxisbeispiel**: Ein Passwort darf nicht "123456" sein (zu unsicher). Ist das eingegebene Passwort verschieden davon?

```{code-cell} ipython3
# Ungleich-Operator: Sind zwei Werte verschieden?
verbotenes_passwort = "123456"
neues_passwort = "SuperSicher2024"
ist_sicher = neues_passwort != verbotenes_passwort

print(f"Verbotenes Passwort: {verbotenes_passwort}")
print(f"Neues Passwort: {neues_passwort}")
print(f"Ist das neue Passwort verschieden vom verbotenen? {ist_sicher}")
```

### 🏃 Sofort ausprobieren!

**Aufgabe 2:** Prüfe, ob die Zeichenkette "Hallo" ungleich "Tschüss" ist.

```{code-cell} ipython3
# Dein Code hier:
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# Lösung:
wort1 = "Hallo"
wort2 = "Tschüss"

print(f"Ist '{wort1}' ungleich '{wort2}'? {wort1 != wort2}")
# Ausgabe: Ist 'Hallo' ungleich 'Tschüss'? True
```
</details>

+++

### Der Größer-Operator (>): Ist links größer als rechts?

Der Größer-Operator prüft, ob der linke Wert größer ist als der rechte.

**Praxisbeispiel**: Ein Fahrstuhl hat eine maximale Traglast von 500 kg. Aktuell sind 480 kg drin. Ist die Traglast überschritten?

```{code-cell} ipython3
# Größer-Operator: Ist der linke Wert größer?
max_traglast = 500
aktuelles_gewicht = 480
ist_ueberladen = aktuelles_gewicht > max_traglast

print(f"Maximale Traglast: {max_traglast} kg")
print(f"Aktuelles Gewicht: {aktuelles_gewicht} kg")
print(f"Ist überladen? {ist_ueberladen}")
```

### 🏃 Sofort ausprobieren!

**Aufgabe 3:** Prüfe, ob die Temperatur 35 Grad höher ist als 30 Grad.

```{code-cell} ipython3
# Dein Code hier:
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# Lösung:
temperatur = 35
grenzwert = 30

print(f"Ist {temperatur} Grad größer als {grenzwert} Grad? {temperatur > grenzwert}")
# Ausgabe: Ist 35 Grad größer als 30 Grad? True
```
</details>

+++

### Der Kleiner-Operator (<): Ist links kleiner als rechts?

Der Kleiner-Operator prüft, ob der linke Wert kleiner ist als der rechte.

**Praxisbeispiel**: Für einen Rabatt musst du mindestens 100 Euro ausgeben. Du hast 85 Euro im Warenkorb. Bekommst du den Rabatt?

```{code-cell} ipython3
# Kleiner-Operator: Ist der linke Wert kleiner?
mindestbetrag_rabatt = 100
warenkorbwert = 85
zu_wenig = warenkorbwert < mindestbetrag_rabatt

print(f"Mindestbetrag für Rabatt: {mindestbetrag_rabatt} Euro")
print(f"Aktueller Warenkorbwert: {warenkorbwert} Euro")
print(f"Warenkorbwert zu niedrig für Rabatt? {zu_wenig}")
```

### 🏃 Sofort ausprobieren!

**Aufgabe 4:** Prüfe, ob 15 kleiner ist als 20.

```{code-cell} ipython3
# Dein Code hier:
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# Lösung:
zahl1 = 15
zahl2 = 20

print(f"Ist {zahl1} kleiner als {zahl2}? {zahl1 < zahl2}")
# Ausgabe: Ist 15 kleiner als 20? True
```
</details>

+++

### Der Größer-oder-Gleich-Operator (>=): Ist links mindestens so groß wie rechts?

Dieser Operator prüft, ob der linke Wert größer **oder gleich** dem rechten ist. Er gibt `True` zurück, wenn eine der beiden Bedingungen erfüllt ist.

**Praxisbeispiel**: Ab 18 Jahren darfst du Auto fahren. Du bist 18. Darfst du fahren?

```{code-cell} ipython3
# Größer-oder-Gleich-Operator
mindestalter = 18
dein_alter = 18
darfst_fahren = dein_alter >= mindestalter

print(f"Mindestalter: {mindestalter} Jahre")
print(f"Dein Alter: {dein_alter} Jahre")
print(f"Darfst du Auto fahren? {darfst_fahren}")
```

### 🏃 Sofort ausprobieren!

**Aufgabe 5:** Prüfe, ob 25 größer oder gleich 25 ist. Prüfe auch, ob 25 größer oder gleich 30 ist.

```{code-cell} ipython3
# Dein Code hier:
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# Lösung:
zahl = 25

print(f"Ist {zahl} >= {zahl}? {zahl >= zahl}")
print(f"Ist {zahl} >= 30? {zahl >= 30}")
# Ausgabe:
# Ist 25 >= 25? True
# Ist 25 >= 30? False
```
</details>

+++

### Der Kleiner-oder-Gleich-Operator (<=): Ist links höchstens so groß wie rechts?

Dieser Operator prüft, ob der linke Wert kleiner **oder gleich** dem rechten ist.

**Praxisbeispiel**: Ein Paket darf maximal 10 kg wiegen. Dein Paket wiegt 10 kg. Kannst du es versenden?

```{code-cell} ipython3
# Kleiner-oder-Gleich-Operator
max_gewicht = 10
paket_gewicht = 10
kann_versenden = paket_gewicht <= max_gewicht

print(f"Maximalgewicht: {max_gewicht} kg")
print(f"Paketgewicht: {paket_gewicht} kg")
print(f"Kann versenden? {kann_versenden}")
```

### 🏃 Sofort ausprobieren!

**Aufgabe 6:** Prüfe, ob 50 kleiner oder gleich 75 ist.

```{code-cell} ipython3
# Dein Code hier:
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# Lösung:
zahl1 = 50
zahl2 = 75

print(f"Ist {zahl1} <= {zahl2}? {zahl1 <= zahl2}")
# Ausgabe: Ist 50 <= 75? True
```
</details>

+++

### Alle Vergleichsoperatoren zusammen

Schauen wir uns alle Vergleichsoperatoren gemeinsam an:

```{code-cell} ipython3
# Alle Vergleichsoperatoren in Aktion
x = 10
y = 5

print(f"x = {x}, y = {y}")
print()
print(f"x == y (gleich): {x == y}")
print(f"x != y (ungleich): {x != y}")
print(f"x > y (größer): {x > y}")
print(f"x < y (kleiner): {x < y}")
print(f"x >= y (größer oder gleich): {x >= y}")
print(f"x <= y (kleiner oder gleich): {x <= y}")
```

### 🏃 Große Übung: Vergleichsoperatoren

**Aufgabe 7:** Schreibe eine Funktion `vergleiche()`, die zwei Zahlen als Parameter erhält und alle sechs Vergleichsoperationen durchführt. Die Funktion soll die Ergebnisse mit `print()` ausgeben.

```{code-cell} ipython3
# Dein Code hier:
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# Lösung:
def vergleiche(a, b):
    print(f"Vergleich von {a} und {b}:")
    print(f"{a} == {b}: {a == b}")
    print(f"{a} != {b}: {a != b}")
    print(f"{a} > {b}: {a > b}")
    print(f"{a} < {b}: {a < b}")
    print(f"{a} >= {b}: {a >= b}")
    print(f"{a} <= {b}: {a <= b}")

# Testen:
vergleiche(8, 12)
```
</details>

+++

## 3. Logische Operatoren: Bedingungen kombinieren 🔗

### Was sind logische Operatoren?

Stell dir vor, du planst einen Grillabend. Aber er findet nur statt, **wenn** das Wetter schön ist **UND** du Zeit hast. Beide Bedingungen müssen erfüllt sein! Oder: Du kaufst ein neues Handy, **wenn** es im Angebot ist **ODER** dein altes kaputt geht. Hier reicht eine Bedingung.

Genau für solche Situationen gibt es logische Operatoren. Sie verbinden mehrere Bedingungen miteinander!

In der realen Welt nutzen wir ständig logische Verknüpfungen: "Wenn du über 18 bist UND einen Führerschein hast, darfst du Auto fahren." Oder: "Wenn es regnet ODER schneit, nehme ich einen Regenschirm mit." Ohne logische Operatoren könnten unsere Programme keine komplexen Entscheidungen treffen!

Python bietet dir drei logische Operatoren:

- **and** (und): Beide Bedingungen müssen wahr sein
- **or** (oder): Mindestens eine Bedingung muss wahr sein
- **not** (nicht): Kehrt den Wahrheitswert um (aus True wird False, aus False wird True)

Diese Operatoren arbeiten mit **booleschen Werten** (True/False) und geben immer einen booleschen Wert zurück.

+++

### Der and-Operator: BEIDE Bedingungen müssen wahr sein

Der `and`-Operator gibt nur dann `True` zurück, wenn **beide** Operanden `True` sind. Ist auch nur einer `False`, ist das Gesamtergebnis `False`.

**Wahrheitstabelle für and**:

| Bedingung 1 | Bedingung 2 | Ergebnis (and) |
|-------------|-------------|----------------|
| False | False | False |
| False | True | False |
| True | False | False |
| True | True | **True** |

**Praxisbeispiel**: Du darfst nur Auto fahren, wenn du mindestens 18 Jahre alt bist **UND** einen Führerschein hast. Beide Bedingungen müssen erfüllt sein!

```{code-cell} ipython3
# Der and-Operator: BEIDE müssen True sein
alter = 20
hat_fuehrerschein = True

darf_fahren = (alter >= 18) and hat_fuehrerschein

print(f"Alter: {alter}")
print(f"Hat Führerschein: {hat_fuehrerschein}")
print(f"Darf Auto fahren: {darf_fahren}")
```

### Weitere Beispiele mit and

```{code-cell} ipython3
# Verschiedene Kombinationen mit and
print("True and True:", True and True)      # Beide wahr → True
print("True and False:", True and False)    # Eine falsch → False
print("False and True:", False and True)    # Eine falsch → False
print("False and False:", False and False)  # Beide falsch → False
```

### 🏃 Sofort ausprobieren!

**Aufgabe 1:** Eine Party findet statt, wenn das Wetter schön ist (True) UND genug Essen da ist (True). Prüfe verschiedene Kombinationen.

```{code-cell} ipython3
# Dein Code hier:
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# Lösung:
# Fall 1: Beides erfüllt
wetter_schoen = True
genug_essen = True
party_findet_statt = wetter_schoen and genug_essen
print(f"Fall 1 - Party findet statt: {party_findet_statt}")  # True

# Fall 2: Nur Wetter schön
wetter_schoen = True
genug_essen = False
party_findet_statt = wetter_schoen and genug_essen
print(f"Fall 2 - Party findet statt: {party_findet_statt}")  # False

# Fall 3: Nichts erfüllt
wetter_schoen = False
genug_essen = False
party_findet_statt = wetter_schoen and genug_essen
print(f"Fall 3 - Party findet statt: {party_findet_statt}")  # False
```
</details>

+++

### Der or-Operator: MINDESTENS EINE Bedingung muss wahr sein

Der `or`-Operator gibt `True` zurück, wenn **mindestens eine** der Bedingungen `True` ist. Nur wenn beide `False` sind, ist das Ergebnis `False`.

**Wahrheitstabelle für or**:

| Bedingung 1 | Bedingung 2 | Ergebnis (or) |
|-------------|-------------|---------------|
| False | False | False |
| False | True | **True** |
| True | False | **True** |
| True | True | **True** |

**Praxisbeispiel**: Du bekommst Rabatt, wenn du Student bist **ODER** über 65 Jahre alt bist. Eine der beiden Bedingungen reicht!

```{code-cell} ipython3
# Der or-Operator: MINDESTENS EINE muss True sein
ist_student = True
alter = 30

bekommt_rabatt = ist_student or (alter > 65)

print(f"Ist Student: {ist_student}")
print(f"Alter: {alter}")
print(f"Bekommt Rabatt: {bekommt_rabatt}")
```

### Weitere Beispiele mit or

```{code-cell} ipython3
# Verschiedene Kombinationen mit or
print("True or True:", True or True)      # Beide wahr → True
print("True or False:", True or False)    # Eine wahr → True
print("False or True:", False or True)    # Eine wahr → True
print("False or False:", False or False)  # Beide falsch → False
```

### 🏃 Sofort ausprobieren!

**Aufgabe 2:** Ein Museum ist kostenlos, wenn du unter 6 Jahre alt bist ODER über 65 Jahre alt bist. Teste verschiedene Altersangaben.

```{code-cell} ipython3
# Dein Code hier:
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# Lösung:
# Fall 1: Kind (4 Jahre)
alter = 4
ist_kostenlos = (alter < 6) or (alter > 65)
print(f"Alter {alter}: Kostenlos? {ist_kostenlos}")  # True

# Fall 2: Erwachsener (30 Jahre)
alter = 30
ist_kostenlos = (alter < 6) or (alter > 65)
print(f"Alter {alter}: Kostenlos? {ist_kostenlos}")  # False

# Fall 3: Senior (70 Jahre)
alter = 70
ist_kostenlos = (alter < 6) or (alter > 65)
print(f"Alter {alter}: Kostenlos? {ist_kostenlos}")  # True
```
</details>

+++

### Der not-Operator: Wahrheitswert umkehren

Der `not`-Operator kehrt einen Wahrheitswert um. Aus `True` wird `False`, aus `False` wird `True`.

**Wahrheitstabelle für not**:

| Bedingung | Ergebnis (not) |
|-----------|----------------|
| True | False |
| False | True |

**Praxisbeispiel**: Eine Tür ist verschlossen, wenn sie **nicht** offen ist.

```{code-cell} ipython3
# Der not-Operator: Wahrheitswert umkehren
tuer_offen = False
tuer_verschlossen = not tuer_offen

print(f"Tür offen: {tuer_offen}")
print(f"Tür verschlossen: {tuer_verschlossen}")
```

### Weitere Beispiele mit not

```{code-cell} ipython3
# Verschiedene Beispiele mit not
print("not True:", not True)    # True wird zu False
print("not False:", not False)  # False wird zu True
```

### 🏃 Sofort ausprobieren!

**Aufgabe 3:** Eine Ampel zeigt rot (ist_gruen = False). Ein Auto darf fahren, wenn die Ampel **nicht** rot ist (also grün). Nutze `not`, um zu prüfen, ob das Auto fahren darf.

```{code-cell} ipython3
# Dein Code hier:
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# Lösung:
ist_gruen = False
darf_fahren = not ist_gruen  # Nicht grün = rot, also nicht fahren

print(f"Ampel ist grün: {ist_gruen}")
print(f"Darf fahren: {not ist_gruen}")  # False (weil rot)

# Wenn Ampel grün:
ist_gruen = True
print(f"\nAmpel ist grün: {ist_gruen}")
print(f"Darf fahren: {ist_gruen}")  # True (weil grün)
```
</details>

+++

### Logische Operatoren kombinieren

Du kannst mehrere logische Operatoren kombinieren! Allerdings wird es dann schnell unübersichtlich. Hier hilft eine **gute Regel**:

**Verwende Klammern, um die Lesbarkeit zu verbessern!**

Auch wenn Python die Operatoren in einer bestimmten Reihenfolge auswertet (not → and → or), machen Klammern den Code für Menschen leichter verständlich.

```{code-cell} ipython3
# Beispiel: Kombinierte logische Operatoren
# Ohne Klammern (funktioniert, aber schwer zu lesen)
a = 10
b = 5
c = 15

ergebnis = a > b and b < c or a == b
print(f"Ohne Klammern: {ergebnis}")

# Mit Klammern (viel klarer!)
ergebnis = (a > b and b < c) or (a == b)
print(f"Mit Klammern: {ergebnis}")
```

### 🏃 Große Übung: Logische Operatoren

**Aufgabe 4:** Schreibe eine Funktion `pruefe_zugang()`, die drei Parameter erhält:
- `alter` (int): Das Alter der Person
- `ist_mitglied` (bool): Ist die Person Mitglied?
- `hat_einladung` (bool): Hat die Person eine Einladung?

Die Funktion soll prüfen, ob die Person Zugang bekommt. Zugang gibt es, wenn:
- Die Person mindestens 18 Jahre alt ist **UND** (Mitglied **ODER** Einladung hat)

Die Funktion soll das Ergebnis zurückgeben (return True/False).

```{code-cell} ipython3
# Dein Code hier:
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# Lösung:
def pruefe_zugang(alter, ist_mitglied, hat_einladung):
    # Mindestens 18 UND (Mitglied ODER Einladung)
    zugang = (alter >= 18) and (ist_mitglied or hat_einladung)
    return zugang

# Tests:
print("Test 1:", pruefe_zugang(20, True, False))   # True (alt genug + Mitglied)
print("Test 2:", pruefe_zugang(20, False, True))   # True (alt genug + Einladung)
print("Test 3:", pruefe_zugang(17, True, False))   # False (zu jung)
print("Test 4:", pruefe_zugang(20, False, False))  # False (kein Zugangsrecht)
print("Test 5:", pruefe_zugang(25, True, True))    # True (alles erfüllt)
```
</details>

+++

### Hinweis zur Lesbarkeit: Klammern verwenden!

Auch wenn Python eine feste Rangfolge für Operatoren hat (zuerst `not`, dann `and`, dann `or`), verbessern **Klammern** die Lesbarkeit enorm!

**Schlechter Stil** (funktioniert, aber schwer zu verstehen):
```python
ergebnis = a < b or c > d and e != f
```

**Guter Stil** (gleiche Bedeutung, aber viel klarer):
```python
ergebnis = (a < b) or ((c > d) and (e != f))
```

```{code-cell} ipython3
# Beispiel: Klammern verbessern Lesbarkeit
a = 5
b = 10
c = 15

# Ohne Klammern (funktioniert, aber unklar)
print(a < b and b < c)  # True

# Mit Klammern (viel klarer!)
print((a < b) and (b < c))  # True
```

## 4. Identitäts- und Zugehörigkeitsoperatoren: Spezielle Vergleiche 🔍

### Was sind Identitäts- und Zugehörigkeitsoperatoren?

Stell dir vor, du hast zwei Briefumschläge. In beiden steht "Hallo". Sind das die **gleichen** Umschläge? Nein! Es sind zwei **verschiedene** Umschläge mit dem **gleichen Inhalt**. Das ist der Unterschied zwischen Gleichheit (==) und Identität (is)!

Oder: Du hast eine Einkaufsliste. Du möchtest wissen: Steht "Milch" auf der Liste? Genau das macht der `in`-Operator - er prüft, ob etwas in einer Sammlung enthalten ist.

Diese Operatoren brauchst du für fortgeschrittene Vergleiche:

- **is**: Sind zwei Variablen **identisch** (zeigen auf dasselbe Objekt im Speicher)?
- **is not**: Sind zwei Variablen **nicht identisch**?
- **in**: Ist ein Wert in einer Sammlung (Liste, String, etc.) **enthalten**?
- **not in**: Ist ein Wert **nicht** in einer Sammlung enthalten?

Diese Operatoren sind besonders wichtig, wenn du mit Listen, Strings, Dictionaries und anderen Sammlungen arbeitest!

+++

### Der is-Operator: Identität prüfen

Der `is`-Operator prüft, ob zwei Variablen auf **dasselbe Objekt** im Speicher zeigen. Das ist etwas anderes als gleicher Inhalt!

**Wichtig**: `is` prüft **Identität**, `==` prüft **Gleichheit**!

```{code-cell} ipython3
# Beispiel: Der Unterschied zwischen is und ==
# Fall 1: Beide Variablen zeigen auf die GLEICHE Liste
liste_a = [1, 2, 3]
liste_b = liste_a  # liste_b zeigt auf dieselbe Liste wie liste_a!

print("Fall 1: Beide zeigen auf dasselbe Objekt")
print(f"liste_a == liste_b: {liste_a == liste_b}")  # True (gleicher Inhalt)
print(f"liste_a is liste_b: {liste_a is liste_b}")  # True (identisch!)

# Fall 2: Zwei VERSCHIEDENE Listen mit gleichem Inhalt
liste_c = [1, 2, 3]
liste_d = [1, 2, 3]  # Neue Liste mit gleichem Inhalt

print("\nFall 2: Zwei verschiedene Objekte mit gleichem Inhalt")
print(f"liste_c == liste_d: {liste_c == liste_d}")  # True (gleicher Inhalt)
print(f"liste_c is liste_d: {liste_c is liste_d}")  # False (nicht identisch!)
```

```{code-cell} ipython3
zahl1 = 42
zahl2 = zahl1
print(zahl1 is zahl2)

zahl1 += 7
print(zahl1 is zahl2)
```

### 🏃 Sofort ausprobieren!

**Aufgabe 1:** Erstelle zwei Variablen `x` und `y`, die auf dieselbe Liste zeigen. Prüfe dann mit `is`, ob sie identisch sind.

```{code-cell} ipython3
# Dein Code hier:
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# Lösung:
x = [10, 20, 30]
y = x  # y zeigt auf dieselbe Liste wie x

print(f"x == y: {x == y}")  # True
print(f"x is y: {x is y}")  # True

# Wenn wir x ändern, ändert sich auch y!
x.append(40)
print(f"\nNach x.append(40):")
print(f"x: {x}")  # [10, 20, 30, 40]
print(f"y: {y}")  # [10, 20, 30, 40] (auch geändert!)
```
</details>

+++

### Der is not-Operator: Nicht-Identität prüfen

Der `is not`-Operator ist das Gegenteil von `is`. Er gibt `True` zurück, wenn zwei Variablen **nicht identisch** sind.

```{code-cell} ipython3
# is not Operator
liste1 = [1, 2, 3]
liste2 = [1, 2, 3]

print(f"liste1 is not liste2: {liste1 is not liste2}")  # True (nicht identisch)
```

### Der in-Operator: Zugehörigkeit prüfen

Der `in`-Operator prüft, ob ein Wert in einer Sammlung (Liste, Tupel, Set, String, etc.) **enthalten** ist.

**Praxisbeispiel**: Du hast eine Einkaufsliste. Steht "Milch" auf der Liste?

```{code-cell} ipython3
# Der in-Operator: Ist etwas in einer Sammlung enthalten?
einkaufsliste = ["Milch", "Brot", "Eier", "Butter"]

print(f"Ist 'Milch' auf der Liste? {'Milch' in einkaufsliste}")
print(f"Ist 'Schokolade' auf der Liste? {'Schokolade' in einkaufsliste}")
```

### in funktioniert auch mit Strings!

```{code-cell} ipython3
# in funktioniert auch mit Strings
text = "Hallo Welt"

print(f"Ist 'Hallo' in '{text}'? {'Hallo' in text}")
print(f"Ist 'Tschüss' in '{text}'? {'Tschüss' in text}")
```

### 🏃 Sofort ausprobieren!

**Aufgabe 2:** Erstelle eine Liste mit deinen Lieblingszahlen. Prüfe dann, ob die Zahl 7 in der Liste ist.

```{code-cell} ipython3
# Dein Code hier:
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# Lösung:
lieblingszahlen = [3, 7, 12, 21, 42]

print(f"Ist 7 in der Liste? {7 in lieblingszahlen}")
print(f"Ist 100 in der Liste? {100 in lieblingszahlen}")
```
</details>

+++

### Der not in-Operator: NICHT enthalten

Der `not in`-Operator ist das Gegenteil von `in`. Er gibt `True` zurück, wenn ein Wert **nicht** in einer Sammlung enthalten ist.

```{code-cell} ipython3
# Der not in-Operator
verfuegbare_produkte = ["Laptop", "Maus", "Tastatur"]

print(f"Ist 'Monitor' NICHT verfügbar? {'Monitor' not in verfuegbare_produkte}")
print(f"Ist 'Laptop' NICHT verfügbar? {'Laptop' not in verfuegbare_produkte}")
```

### 🏃 Sofort ausprobieren!

**Aufgabe 3:** Erstelle eine Liste mit erlaubten Benutzernamen. Prüfe, ob "admin123" **nicht** in der Liste ist.

```{code-cell} ipython3
# Dein Code hier:
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# Lösung:
erlaubte_namen = ["user01", "user02", "max_m", "anna_s"]

print(f"Ist 'admin123' nicht erlaubt? {'admin123' not in erlaubte_namen}")
print(f"Ist 'user01' nicht erlaubt? {'user01' not in erlaubte_namen}")
```
</details>

+++

### Praktisches Beispiel: Alle Operatoren zusammen

```{code-cell} ipython3
# Identitäts- und Zugehörigkeitsoperatoren in Aktion
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("Identität:")
print(f"a is b: {a is b}")          # True (identisch)
print(f"a is c: {a is c}")          # False (nicht identisch)
print(f"a is not c: {a is not c}")  # True (nicht identisch)

print("\nZugehörigkeit:")
print(f"2 in a: {2 in a}")                  # True
print(f"5 in a: {5 in a}")                  # False
print(f"5 not in a: {5 not in a}")          # True
```

### 🏃 Große Übung: Identitäts- und Zugehörigkeitsoperatoren

**Aufgabe 4:** Schreibe eine Funktion `pruefe_liste()`, die eine Liste und einen Wert als Parameter erhält. Die Funktion soll:
1. Prüfen, ob der Wert in der Liste enthalten ist
2. Prüfen, ob der Wert NICHT in der Liste enthalten ist
3. Beide Ergebnisse mit `print()` ausgeben

```{code-cell} ipython3
# Dein Code hier:
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# Lösung:
def pruefe_liste(liste, wert):
    ist_enthalten = wert in liste
    ist_nicht_enthalten = wert not in liste
    
    print(f"Ist {wert} in der Liste? {ist_enthalten}")
    print(f"Ist {wert} NICHT in der Liste? {ist_nicht_enthalten}")

# Tests:
meine_liste = [10, 20, 30, 40, 50]
pruefe_liste(meine_liste, 30)
print()
pruefe_liste(meine_liste, 100)
```
</details>

+++

## Übersichtstabelle: Alle Operatoren auf einen Blick 📋

Hier sind noch einmal alle Operatoren zusammengefasst:

### Arithmetische Operatoren

| Operator | Name | Beispiel | Ergebnis |
|----------|------|----------|----------|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraktion | `10 - 3` | `7` |
| `*` | Multiplikation | `10 * 3` | `30` |
| `/` | Division | `10 / 3` | `3.333...` |
| `%` | Modulo | `10 % 3` | `1` |
| `**` | Potenz | `10 ** 3` | `1000` |

### Vergleichsoperatoren

| Operator | Name | Beispiel | Ergebnis |
|----------|------|----------|----------|
| `==` | Gleich | `5 == 5` | `True` |
| `!=` | Ungleich | `5 != 3` | `True` |
| `>` | Größer | `5 > 3` | `True` |
| `<` | Kleiner | `5 < 3` | `False` |
| `>=` | Größer oder gleich | `5 >= 5` | `True` |
| `<=` | Kleiner oder gleich | `5 <= 3` | `False` |

### Logische Operatoren

| Operator | Name | Beispiel | Ergebnis |
|----------|------|----------|----------|
| `and` | Und | `True and True` | `True` |
| `or` | Oder | `False or True` | `True` |
| `not` | Nicht | `not True` | `False` |

### Identitäts- und Zugehörigkeitsoperatoren

| Operator | Name | Beispiel | Bedeutung |
|----------|------|----------|----------|
| `is` | Identität | `a is b` | Sind a und b identisch? |
| `is not` | Nicht-Identität | `a is not b` | Sind a und b nicht identisch? |
| `in` | Zugehörigkeit | `2 in [1, 2, 3]` | Ist 2 in der Liste? |
| `not in` | Nicht-Zugehörigkeit | `4 not in [1, 2, 3]` | Ist 4 nicht in der Liste? |

+++

## Zusammenfassung 🎓

### Was du gelernt hast:

**Arithmetische Operatoren** - Rechnen mit Python:
- `+` addiert zwei Zahlen
- `-` subtrahiert Zahlen
- `*` multipliziert Zahlen
- `/` dividiert Zahlen (Ergebnis ist immer float)
- `%` gibt den Rest einer Division zurück
- `**` potenziert Zahlen

**Vergleichsoperatoren** - Werte vergleichen:
- `==` prüft auf Gleichheit
- `!=` prüft auf Ungleichheit
- `>`, `<`, `>=`, `<=` vergleichen Größen
- Ergebnis ist immer True oder False

**Logische Operatoren** - Bedingungen kombinieren:
- `and`: Beide Bedingungen müssen True sein
- `or`: Mindestens eine Bedingung muss True sein
- `not`: Kehrt den Wahrheitswert um
- Klammern verbessern die Lesbarkeit!

**Identitäts- und Zugehörigkeitsoperatoren**:
- `is` prüft Identität (gleiches Objekt im Speicher)
- `==` prüft Gleichheit (gleicher Inhalt)
- `in` prüft, ob etwas in einer Sammlung enthalten ist
- `not in` prüft, ob etwas NICHT enthalten ist

### Wichtige Erkenntnisse:
- Operatoren sind die Werkzeuge zum Programmieren
- Sie ermöglichen Berechnungen, Vergleiche und logische Verknüpfungen
- Klammern machen komplexe Ausdrücke lesbarer
- `is` und `==` sind verschieden!

**Nächster Schritt**: Im nächsten Notebook lernst du, wie du mit `if-else` Entscheidungen auf Basis dieser Operatoren triffst!

+++

## Trainingsmaterial 💪

Zeit, dein Wissen zu festigen! Die Übungen sind in drei Schwierigkeitsstufen eingeteilt.

+++

### 🟢 Einfache Aufgaben (zum Warmwerden)

**Aufgabe 1**: Schreibe eine Funktion `flaeche_rechteck()`, die Länge und Breite als Parameter erhält und die Fläche berechnet (Länge × Breite). Die Funktion soll das Ergebnis zurückgeben.

```{code-cell} ipython3
# Dein Code hier:
```

**Aufgabe 2**: Schreibe eine Funktion `ist_gerade()`, die eine Zahl als Parameter erhält und `True` zurückgibt, wenn die Zahl gerade ist (nutze Modulo %).

```{code-cell} ipython3
# Dein Code hier:
```

**Aufgabe 3**: Schreibe eine Funktion `ist_im_bereich()`, die prüft, ob eine Zahl zwischen 10 und 20 liegt (inklusive). Nutze Vergleichsoperatoren und `and`.

```{code-cell} ipython3
# Dein Code hier:
```

### 🟡 Mittlere Aufgaben (schon besser!)

**Aufgabe 4**: Schreibe eine Funktion `rabatt_berechnen()`, die einen Preis und einen Rabattprozentsatz erhält und den reduzierten Preis zurückgibt.

Beispiel: `rabatt_berechnen(100, 20)` soll `80.0` zurückgeben (20% Rabatt auf 100€)

```{code-cell} ipython3
# Dein Code hier:
```

**Aufgabe 5**: Schreibe eine Funktion `passwort_stark()`, die prüft, ob ein Passwort stark ist. Ein Passwort ist stark, wenn:
- Es mindestens 8 Zeichen lang ist UND
- Es das Zeichen "!" oder "?" enthält

Nutze `len()`, `in`, `or` und `and`.

```{code-cell} ipython3
# Dein Code hier:
```

### 🔴 Herausforderungen (für Profis)

**Aufgabe 6**: Schreibe eine Funktion `taschenrechner()`, die zwei Zahlen und einen Operator (+, -, *, /) als Strings erhält und das Ergebnis zurückgibt.

Beispiel: `taschenrechner(10, 5, "+")` soll `15` zurückgeben

Hinweis: Du musst prüfen, welcher Operator übergeben wurde, und dann die entsprechende Operation ausführen. Du darfst mehrere `return`-Anweisungen verwenden!

```{code-cell} ipython3
# Dein Code hier:
```

## Musterlösungen 📝

<details>
<summary>🔍 Lösungen zu den einfachen Aufgaben</summary>

```python
# Aufgabe 1: Fläche eines Rechtecks
def flaeche_rechteck(laenge, breite):
    flaeche = laenge * breite
    return flaeche

print(flaeche_rechteck(5, 3))  # 15
print(flaeche_rechteck(10, 7))  # 70

# Aufgabe 2: Ist eine Zahl gerade?
def ist_gerade(zahl):
    return zahl % 2 == 0

print(ist_gerade(4))   # True
print(ist_gerade(7))   # False
print(ist_gerade(10))  # True

# Aufgabe 3: Ist im Bereich?
def ist_im_bereich(zahl):
    return (zahl >= 10) and (zahl <= 20)

print(ist_im_bereich(15))  # True
print(ist_im_bereich(5))   # False
print(ist_im_bereich(20))  # True
```
</details>

<details>
<summary>🔍 Lösungen zu den mittleren Aufgaben</summary>

```python
# Aufgabe 4: Rabatt berechnen
def rabatt_berechnen(preis, rabatt_prozent):
    rabatt_betrag = preis * (rabatt_prozent / 100)
    neuer_preis = preis - rabatt_betrag
    return neuer_preis

print(rabatt_berechnen(100, 20))  # 80.0
print(rabatt_berechnen(50, 10))   # 45.0

# Aufgabe 5: Ist Passwort stark?
def passwort_stark(passwort):
    lang_genug = len(passwort) >= 8
    hat_sonderzeichen = ("!" in passwort) or ("?" in passwort)
    return lang_genug and hat_sonderzeichen

print(passwort_stark("Hallo!"))        # False (zu kurz)
print(passwort_stark("HalloWelt"))     # False (kein Sonderzeichen)
print(passwort_stark("Hallo123!"))     # True
print(passwort_stark("SuperGeheim?"))  # True
```
</details>

<details>
<summary>🔍 Lösung zur Herausforderung</summary>

```python
# Aufgabe 6: Taschenrechner
def taschenrechner(zahl1, zahl2, operator):
    # Wir prüfen, welcher Operator übergeben wurde
    # und führen die entsprechende Operation aus
    
    # Addition
    ist_addition = operator == "+"
    if ist_addition:  # Diese Syntax lernst du in Notebook 09!
        return zahl1 + zahl2
    
    # Subtraktion
    ist_subtraktion = operator == "-"
    if ist_subtraktion:
        return zahl1 - zahl2
    
    # Multiplikation
    ist_multiplikation = operator == "*"
    if ist_multiplikation:
        return zahl1 * zahl2
    
    # Division
    ist_division = operator == "/"
    if ist_division:
        return zahl1 / zahl2

# Tests:
print(taschenrechner(10, 5, "+"))   # 15
print(taschenrechner(10, 5, "-"))   # 5
print(taschenrechner(10, 5, "*"))   # 50
print(taschenrechner(10, 5, "/"))   # 2.0

# Hinweis: Diese Lösung verwendet if-Anweisungen, die du noch nicht kennst!
# Das ist okay - es zeigt dir einen Ausblick auf Notebook 09.
# Eine Lösung NUR mit Operatoren ist hier nicht möglich.
```
</details>

+++

---

## Herzlichen Glückwunsch! 🎉

Du hast die Operatoren gemeistert! Das sind die grundlegenden Werkzeuge, mit denen du in Python arbeitest. Im nächsten Notebook lernst du, wie du mit diesen Operatoren **Entscheidungen** triffst (if-else-Anweisungen).

Bis bald! 👋
