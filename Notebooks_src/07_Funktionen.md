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

# 07 - Funktionen: Wiederverwendbare Code-Bausteine 🎯

+++

## Willkommen! 👋

Herzlich willkommen zu Notebook 07! Heute lernen Sie ein fundamentales Konzept der Programmierung kennen: **Funktionen**.

Funktionen sind wie **Kochrezepte in Ihrem Programmier-Kochbuch**. Einmal aufgeschrieben, können Sie sie immer wieder verwenden, ohne jedes Mal von vorne beginnen zu müssen. Stellen Sie sich vor, Sie müssten jedes Mal, wenn Sie Nudeln kochen wollen, das gesamte Rezept neu überlegen. Viel praktischer ist es doch, ein Rezept einmal aufzuschreiben und dann immer wieder darauf zurückzugreifen!

## Was Sie heute lernen:
- 📦 **Was Funktionen sind** und warum sie so wichtig sind
- 🏗️ **Wie Sie eigene Funktionen definieren** mit dem `def`-Schlüsselwort
- 🎯 **Wie Sie Funktionen aufrufen** und Parameter übergeben
- 📥 **Wie Sie Parameter verwenden** (positional und benannt)
- 🔄 **Wie Funktionen Ergebnisse zurückgeben** mit `return`
- 🔍 **Was Scope bedeutet** und wo Variablen gültig sind

## Voraussetzungen 📚
Was Sie bereits können sollten (aus den Notebooks 01-06):
- ✅ Mit `print()` Ausgaben auf der Konsole erstellen
- ✅ Mit `input()` Benutzereingaben entgegennehmen
- ✅ Mit F-Strings formatierte Texte erstellen
- ✅ Variablen definieren und verwenden
- ✅ Datentypen unterscheiden (int, float, str, bool)
- ✅ Mit Listen, Tupeln, Sets und Dictionaries arbeiten
- ✅ Funktionen wie `len()`, `append()` und `remove()` nutzen

+++

---
## 1. Was sind Funktionen? 🤔

### Das Konzept verstehen

Stellen Sie sich vor, Sie arbeiten in einer Bibliothek. Jeden Tag müssen Sie neue Bücher in das System eintragen. Jedes Mal müssen Sie den Titel notieren, den Autor aufschreiben, die ISBN-Nummer eintragen, das Erscheinungsjahr vermerken und die Kategorie festlegen. Das sind fünf Schritte, die Sie **jedes einzelne Mal** wiederholen müssen.

Wäre es nicht praktischer, wenn Sie einmal eine **Anleitung** schreiben könnten: "So trägt man ein Buch ein", und diese Anleitung dann einfach immer wieder verwenden? Genau das sind **Funktionen in der Programmierung**!

Eine Funktion ist ein **benannter Block von Code**, der eine bestimmte Aufgabe erfüllt. Sie schreiben den Code einmal, geben ihm einen Namen, und können ihn dann beliebig oft wiederverwenden. Das hat mehrere große Vorteile:

**1. Wiederverwendbarkeit**: Sie schreiben den Code nur einmal und können ihn beliebig oft nutzen. Wenn Sie in Ihrem Programm zwanzigmal einen Namen formatieren müssen, schreiben Sie die Funktion einmal und rufen sie zwanzigmal auf.

**2. Übersichtlichkeit**: Ihr Code wird strukturierter und leichter zu lesen. Statt 50 Zeilen Code zu sehen, sehen Sie einen aussagekräftigen Funktionsnamen wie `formatiere_benutzername()`. Jeder versteht sofort, was passiert!

**3. Wartbarkeit**: Wenn Sie etwas ändern müssen, ändern Sie es nur an einer Stelle. Stellen Sie sich vor, Sie hätten den Code zur Namensformatierung zwanzigmal im Programm. Bei einem Fehler müssten Sie zwanzigmal korrigieren! Mit einer Funktion korrigieren Sie nur einmal.

**4. Testbarkeit**: Funktionen können Sie einzeln testen. Sie können überprüfen: "Funktioniert meine Funktion zur Namensformatierung?" – unabhängig vom Rest des Programms.

### Funktionen im echten Leben

In der Programmierung verwenden Sie ständig Funktionen. Tatsächlich haben Sie bereits mehrere kennengelernt, ohne es vielleicht bewusst wahrzunehmen:

- **`print()`** ist eine Funktion – sie nimmt etwas entgegen und gibt es auf dem Bildschirm aus
- **`input()`** ist eine Funktion – sie nimmt eine Nachricht entgegen und gibt zurück, was der Benutzer eingetippt hat
- **`len()`** ist eine Funktion – sie nimmt eine Liste entgegen und gibt zurück, wie viele Elemente darin sind
- **`type()`** ist eine Funktion – sie nimmt einen Wert entgegen und gibt zurück, welchen Datentyp er hat

All diese Funktionen wurden von Python-Entwicklern einmal geschrieben und stehen Ihnen nun zur Verfügung. Sie müssen nicht wissen, wie `print()` intern funktioniert – Sie nutzen einfach die Funktion!

+++

### Beispiele für bereits bekannte Funktionen

Schauen wir uns an, wie Sie bereits mit Funktionen gearbeitet haben:

```{code-cell} ipython3
# Die print()-Funktion gibt Text auf der Konsole aus
print("Hallo, ich bin eine Ausgabe!")
```

```{code-cell} ipython3
# Die len()-Funktion ermittelt die Länge einer Liste
meine_liste = ["Apfel", "Banane", "Kirsche"]
anzahl = len(meine_liste)
print(f"Die Liste enthält {anzahl} Elemente")
print("Die Liste enthält", str(anzahl), " Elemente")
```

```{code-cell} ipython3
len("String")
```

```{code-cell} ipython3
# Die type()-Funktion gibt den Datentyp zurück
zahl = 42
datentyp = type(zahl)
print(f"Der Datentyp von {zahl} ist: {datentyp}")
```

**Was ist hier passiert?**

In jedem dieser Beispiele haben Sie eine **Funktion aufgerufen**. Das Muster ist immer gleich:
1. Sie schreiben den **Funktionsnamen** (z.B. `print`, `len`, `type`)
2. Sie setzen **runde Klammern** dahinter
3. In die Klammern schreiben Sie, was die Funktion bekommen soll (die **Argumente**)

Manche Funktionen wie `len()` und `type()` geben auch ein **Ergebnis zurück**, das Sie in einer Variable speichern können.

+++

### 🏃 Sofort ausprobieren!

Bevor wir eigene Funktionen schreiben, festigen wir das Verständnis von bereits bekannten Funktionen.

**Aufgabe 1:** Erstellen Sie eine Liste mit 5 Ihrer Lieblingsbücher und verwenden Sie `len()`, um die Anzahl auszugeben.

```{code-cell} ipython3
# Ihr Code hier:
laenge = len(["Buch1", "Buch2"])
print(laenge)
```

**Aufgabe 2:** Erstellen Sie drei Variablen mit unterschiedlichen Datentypen (Text, Zahl, Liste) und geben Sie mit `type()` jeweils den Datentyp aus.

```{code-cell} ipython3
# Ihr Code hier:
str_var = "Text"
int_var = 1
lst_var = ["a", "b", "c"]

print(type(str_var), type(int_var), type(lst_var))
```

**Aufgabe 3:** Verwenden Sie `input()`, um nach dem Namen einer Person zu fragen, und `print()`, um eine Begrüßung auszugeben.

```{code-cell} ipython3
# Ihr Code hier:
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1:
lieblingsbuecher = ["1984", "Der Prozess", "Faust", "Die Verwandlung", "Frankenstein"]
anzahl_buecher = len(lieblingsbuecher)
print(f"Ich habe {anzahl_buecher} Lieblingsbücher")

# Aufgabe 2:
text_variable = "Hallo"
zahl_variable = 42
listen_variable = [1, 2, 3]

print(f"Typ von text_variable: {type(text_variable)}")
print(f"Typ von zahl_variable: {type(zahl_variable)}")
print(f"Typ von listen_variable: {type(listen_variable)}")

# Aufgabe 3:
name = input("Wie ist Ihr Name? ")
print(f"Herzlich willkommen, {name}!")
```
</details>

+++

---
## 2. Eigene Funktionen definieren 🏗️

### Das def-Schlüsselwort

Jetzt wird es spannend! Sie haben gesehen, wie Sie vorgefertigte Funktionen von Python verwenden. Aber das wahre Potenzial liegt darin, **eigene Funktionen zu schreiben**.

Um eine eigene Funktion zu erstellen, verwenden Sie das Schlüsselwort **`def`** (kurz für "define" = definieren). Das ist wie das Schreiben eines neuen Rezepts in Ihr Kochbuch.

Die grundlegende Struktur sieht so aus:

```python
def funktionsname():
    # Code, der ausgeführt werden soll
    # Weitere Anweisungen
```

Lassen Sie uns die einzelnen Bestandteile genau anschauen:

**1. Das `def`-Schlüsselwort**: Das ist das Signal an Python: "Achtung, jetzt kommt eine neue Funktion!"

**2. Der Funktionsname**: Geben Sie Ihrer Funktion einen **aussagekräftigen Namen**. Wie bei Variablen sollte der Name beschreiben, was die Funktion tut. Verwenden Sie Kleinbuchstaben und Unterstriche (z.B. `begruessung_ausgeben`, `name_formatieren`).

**3. Die runden Klammern `()`**: Diese gehören immer dazu, auch wenn sie erstmal leer sind. Später lernen Sie, dass hier die Parameter hineingehören.

**4. Der Doppelpunkt `:`**: Dieser signalisiert: "Jetzt kommt der Code, der zur Funktion gehört."

**5. Der eingerückte Code-Block**: Alles, was zur Funktion gehört, wird **eingerückt** geschrieben (normalerweise mit 4 Leerzeichen oder der Tab-Taste). Das ist extrem wichtig in Python! Die Einrückung zeigt Python, welcher Code zur Funktion gehört und welcher nicht.

+++

### Ihre erste eigene Funktion

Schreiben wir gemeinsam Ihre erste eigene Funktion! Sie soll einfach nur eine Begrüßung ausgeben:

```{code-cell} ipython3
# Definition der Funktion
def sage_hallo():
    print("Hallo! Schön, dass Sie da sind!")
    print("Willkommen zu diesem Python-Kurs!")
```

**Was ist passiert?**

Wenn Sie diese Zelle ausführen, sehen Sie... nichts! Das ist völlig normal. Sie haben die Funktion nur **definiert**, aber noch nicht **aufgerufen**. Es ist wie ein Rezept, das Sie in Ihr Kochbuch geschrieben haben – solange Sie nicht anfangen zu kochen, passiert nichts.

Die Funktion existiert jetzt in Python's Gedächtnis und wartet darauf, verwendet zu werden.

+++

### Eine Funktion aufrufen

Um die Funktion zu **verwenden** (das nennt man "aufrufen"), schreiben Sie einfach ihren Namen mit runden Klammern:

```{code-cell} ipython3
# Aufruf der Funktion
sage_hallo()
sage_hallo()
sage_hallo()
```

**Jetzt** sehen Sie die Ausgabe! Die Funktion wurde ausgeführt und hat die beiden `print()`-Anweisungen durchgeführt.

+++

### Die Funktion mehrfach verwenden

Der große Vorteil: Sie können die Funktion jetzt beliebig oft aufrufen!

```{code-cell} ipython3
# Die gleiche Funktion dreimal aufrufen
sage_hallo()
print("------------------------------")
sage_hallo()
print("------------------------------")
sage_hallo()
```

**Sehen Sie den Vorteil?**

Statt die beiden `print()`-Befehle dreimal zu schreiben (= 6 Zeilen Code), rufen Sie einfach dreimal die Funktion auf (= 3 Zeilen Code). Bei komplexeren Funktionen wird dieser Vorteil noch deutlicher!

+++

### 🏃 Sofort ausprobieren!

**Aufgabe 1:** Definieren Sie eine Funktion namens `zeige_info()`, die drei Zeilen ausgibt: Ihren Namen, Ihren Studiengang und Ihr Semester. Rufen Sie die Funktion dann auf.

```{code-cell} ipython3
# Ihr Code hier:
def irgendwas():
    print("hallo")
```

```{code-cell} ipython3
irgendwas()
```

**Aufgabe 2:** Definieren Sie eine Funktion namens `trennlinie()`, die eine optische Trennlinie aus 50 Gleichheitszeichen ausgibt. Nutzen Sie sie, um zwischen verschiedenen Ausgaben zu trennen.

```{code-cell} ipython3
# Ihr Code hier:
def trennlinie():
    print("="*50)
```

```{code-cell} ipython3
trennlinie()
```

**Aufgabe 3:** Definieren Sie eine Funktion `zeige_liste()`, die eine vorher definierte Liste von Städtenamen ausgibt (verwenden Sie eine globale Variable für die Liste).

```{code-cell} ipython3
# Ihr Code hier:
staedte = ["Berlin", "Spandau"]

def zeige_liste():
    print(staedte)

zeige_liste()
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1:
def zeige_info():
    print("Name: Max Mustermann")
    print("Studiengang: Informatik")
    print("Semester: 3")

zeige_info()

# Aufgabe 2:
def trennlinie():
    print("=" * 50)

print("Erste Nachricht")
trennlinie()
print("Zweite Nachricht")
trennlinie()
print("Dritte Nachricht")

# Aufgabe 3:
staedte = ["Berlin", "Hamburg", "München", "Köln"]

def zeige_liste():
    print("Städte:")
    print(staedte)

zeige_liste()
```
</details>

+++

---
## 3. Parameter und Argumente 📥

### Funktionen mit Eingaben versehen

Bis jetzt haben unsere Funktionen immer das Gleiche gemacht – egal, wie oft wir sie aufgerufen haben. Das ist wie ein Kochrezept, das immer für genau 4 Personen ist. Was aber, wenn Sie mal für 2, mal für 6 Personen kochen möchten? Sie brauchen ein **flexibles Rezept**, das sich anpassen lässt!

Genau das ermöglichen **Parameter** in Funktionen. Parameter sind wie **Platzhalter** in Ihrer Funktion, die bei jedem Aufruf mit konkreten Werten gefüllt werden können. Die konkreten Werte, die Sie beim Aufruf übergeben, nennt man **Argumente**.

**Die Analogie**: Stellen Sie sich eine Kaffeemaschine vor. Die Funktion ist die Kaffeemaschine selbst. Die Parameter sind die Einstellungen: Welche Stärke? Welche Menge? Die Argumente sind dann Ihre konkreten Wünsche: "Stark" und "Große Tasse".

### Syntax von Parametern

Parameter werden in den runden Klammern der Funktionsdefinition angegeben:

```python
def funktionsname(parameter1, parameter2):
    # Code, der die Parameter verwendet
```

Beim Aufruf übergeben Sie dann die konkreten Werte (Argumente):

```python
funktionsname(wert1, wert2)
```

+++

### Ihre erste Funktion mit Parametern

Schreiben wir eine Funktion, die eine Person mit ihrem Namen begrüßt:

```{code-cell} ipython3
# Funktion mit einem Parameter definieren
def begruesse_person(name):
    print(f"Hallo {name}!")
    print(f"Schön, dass Sie da sind, {name}!")
```

```{code-cell} ipython3
begruesse_person("Hans Joachim") # Hans Joachim ist das Argument für den Funktionsaufruf
begruesse_person(20)
```

**Was ist hier neu?**

- In den Klammern steht jetzt `name` – das ist der **Parameter**
- Der Parameter ist wie eine Variable, die nur innerhalb der Funktion existiert
- Sie bekommt ihren Wert erst beim Aufruf der Funktion

Jetzt rufen wir die Funktion mit verschiedenen Namen auf:

```{code-cell} ipython3
# Funktion mit verschiedenen Argumenten aufrufen
begruesse_person("Anna")
print("---")
begruesse_person("Max")
print("---")
begruesse_person("Sophie")
```

**Sehen Sie den Vorteil?**

Die gleiche Funktion kann jetzt verschiedene Personen begrüßen! Der Parameter `name` nimmt bei jedem Aufruf einen anderen Wert an: erst "Anna", dann "Max", dann "Sophie".

+++

### Mehrere Parameter

Funktionen können auch mehrere Parameter haben. Diese werden durch Kommas getrennt:

```{code-cell} ipython3
# Funktion mit zwei Parametern
def stelle_vor(vorname, nachname):
    print(f"Darf ich vorstellen: {vorname} {nachname}")
```

```{code-cell} ipython3
# Aufruf mit zwei Argumenten
stelle_vor("Albert", "Einstein")
stelle_vor("Marie", "Curie")
stelle_vor("Ada", "Lovelace")
```

### Positionale Parameter vs. Benannte Parameter

Es gibt zwei Arten, wie Sie Argumente an eine Funktion übergeben können:

#### 1. Positionale Argumente

Bei **positionalen Argumenten** kommt es auf die **Reihenfolge** an. Das erste Argument wird dem ersten Parameter zugeordnet, das zweite dem zweiten, und so weiter:

```{code-cell} ipython3
def beschreibe_person(name, alter, stadt):
    print(f"{name} ist {alter} Jahre alt und kommt aus {stadt}.")

# Positionale Argumente - die Reihenfolge ist wichtig!
beschreibe_person("Lisa", 25, "Berlin")
beschreibe_person("Lisa", "Berlin", 25)
```

**Achtung bei der Reihenfolge!** Was passiert, wenn Sie die Argumente vertauschen?

```{code-cell} ipython3
# Falsche Reihenfolge führt zu unsinnigen Ergebnissen!
beschreibe_person(25, "Lisa", "Berlin")  # 25 ist jetzt der "Name"
```

#### 2. Benannte Argumente (Keyword Arguments)

Bei **benannten Argumenten** geben Sie explizit an, welcher Wert zu welchem Parameter gehört. Die Reihenfolge spielt dann keine Rolle mehr!

```{code-cell} ipython3
def beschreibe_person(name, alter, stadt):
    print(f"{name} ist {alter} Jahre alt und kommt aus {stadt}.")

# Benannte Argumente - die Reihenfolge ist egal!
beschreibe_person(name="Tom", alter=30, stadt="München")
beschreibe_person(stadt="Hamburg", name="Sara", alter=28)

beschreibe_person(alter=35, 
                  stadt="Frankfurt", 
                  name="Max")
```

**Der Vorteil benannter Argumente:**
- Die Reihenfolge ist flexibel
- Der Code ist lesbarer (man sieht sofort, was welcher Wert bedeutet)
- Fehler durch vertauschte Argumente werden vermieden

+++

### Mischung aus positionalen und benannten Argumenten

Sie können beide Arten auch mischen, aber es gibt eine wichtige Regel: **Positionale Argumente müssen VOR benannten Argumenten stehen!**

```{code-cell} ipython3
# Gemischte Verwendung - erst positional, dann benannt
beschreibe_person("Nina", 27, stadt="Köln")  # Funktioniert!

# Das hier würde einen Fehler verursachen:
# beschreibe_person(name="Nina", 27, "Köln")  # SyntaxError!
```

### 🏃 Sofort ausprobieren!

**Aufgabe 1:** Schreiben Sie eine Funktion `rechne_rechteck()`, die zwei Parameter `laenge` und `breite` hat und die Fläche ausgibt. Rufen Sie sie einmal mit positionalen und einmal mit benannten Argumenten auf.

```{code-cell} ipython3
# Ihr Code hier:
def rechne_rechteck(laenge,breite):
    print(f"Das Rechteck hat eine Fläche von: {laenge * breite}")

rechne_rechteck(5,6)
rechne_rechteck(laenge=5, breite=7)
rechne_rechteck(breite=3, laenge=12)
```

**Aufgabe 2:** Erstellen Sie eine Funktion `zeige_produkt()` mit drei Parametern: `name`, `preis` und `kategorie`. Rufen Sie sie mit verschiedenen Kombinationen von positionalen und benannten Argumenten auf.

```{code-cell} ipython3
# Ihr Code hier:
def zeige_produkt(name, preis, kategorie):
    print(f"Das {name} kostet {preis} Euro und gehört in die Kategorie {kategorie}")

zeige_produkt("Käsekuchen", 99, "Leckerzeug")
zeige_produkt("Senf", kategorie="Zeug", preis="1")
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1:
def rechne_rechteck(laenge, breite):
    flaeche = laenge * breite
    print(f"Ein Rechteck mit Länge {laenge} und Breite {breite} hat eine Fläche von {flaeche}.")

# Positionale Argumente
rechne_rechteck(10, 5)

# Benannte Argumente
rechne_rechteck(laenge=8, breite=3)
rechne_rechteck(breite=4, laenge=7)

# Aufgabe 2:
def zeige_produkt(name, preis, kategorie):
    print(f"Produkt: {name}")
    print(f"Preis: {preis}€")
    print(f"Kategorie: {kategorie}")
    print("-" * 30)

# Nur positionale Argumente
zeige_produkt("Laptop", 999, "Elektronik")

# Nur benannte Argumente
zeige_produkt(name="Stuhl", preis=79, kategorie="Möbel")

# Gemischt
zeige_produkt("Buch", 15, kategorie="Medien")
zeige_produkt("Kaffee", kategorie="Getränke", preis=3.50)
```
</details>

+++

---
## 4. Das Return-Statement 🔄

### Funktionen mit Rückgabewerten

Bis jetzt haben unsere Funktionen Dinge **ausgegeben** mit `print()`. Aber was, wenn Sie das Ergebnis einer Berechnung **weiterverwenden** möchten? 

Stellen Sie sich vor, Sie haben eine Funktion, die das Quadrat einer Zahl berechnet. Mit `print()` wird das Ergebnis nur angezeigt, aber Sie können nicht damit weiterrechnen. Hier kommt das **`return`-Statement** ins Spiel!

**Die Analogie**: Eine Funktion ohne `return` ist wie ein Taschenrechner, der das Ergebnis nur anzeigt. Eine Funktion mit `return` ist wie ein Taschenrechner, der Ihnen das Ergebnis auf einem Zettel gibt – Sie können es aufheben und weiterverwenden.

### Der Unterschied zwischen print() und return

Dieser Unterschied ist **fundamental wichtig** und oft eine Quelle der Verwirrung für Anfänger:

```{code-cell} ipython3
# Funktion mit print() - zeigt nur an
def quadrat_print(zahl):
    ergebnis = zahl * zahl
    print(f"Das Quadrat von {zahl} ist {ergebnis}")

# Funktion mit return - gibt das Ergebnis zurück
def quadrat_return(zahl):
    ergebnis = zahl * zahl
    return ergebnis
```

Schauen wir uns den Unterschied in der Praxis an:

```{code-cell} ipython3
# Mit print() - kann nicht weiterverwendet werden
#quadrat_print(5)  # Zeigt "Das Quadrat von 5 ist 25"

# Versuch, das Ergebnis zu speichern:
resultat = quadrat_print(5)  
print(f"Resultat: {resultat}")  # Resultat ist None!
```

```{code-cell} ipython3
# Mit return - kann weiterverwendet werden
resultat = quadrat_return(5)
print(f"Resultat: {resultat}")  # Resultat ist 25!

# Jetzt können wir damit weiterrechnen:
doppeltes_quadrat = resultat * 2
print(f"Das Doppelte des Quadrats: {doppeltes_quadrat}")
```

**Merke:**
- `print()` **zeigt** etwas auf dem Bildschirm an
- `return` **gibt** einen Wert an den Aufrufer zurück
- Eine Funktion ohne `return` gibt automatisch `None` zurück

+++

### Praktische Beispiele mit return

```{code-cell} ipython3
# Eine Funktion, die die Summe zweier Zahlen zurückgibt
def addiere(a, b):
    summe = a + b
    return summe

# Wir können das Ergebnis speichern und verwenden
ergebnis = addiere(10, 15)
print(f"10 + 15 = {ergebnis}")
```

```{code-cell} ipython3
# Eine Funktion, die einen formatierten Namen zurückgibt
def formatiere_name(vorname, nachname):
    voller_name = f"{nachname.upper()}, {vorname.capitalize()}"
    return voller_name

# Den formatierten Namen verwenden
name = formatiere_name("max", "mustermann")
print(f"Formatierter Name: {name}")
```

### Funktionen können andere Funktionen nutzen

Mit `return` können Sie Funktionen verketten – das Ergebnis einer Funktion wird zur Eingabe der nächsten:

```{code-cell} ipython3
def verdopple(zahl):
    return zahl * 2

def addiere_zehn(zahl):
    return zahl + 10

# Funktionen verketten
start_wert = 5
schritt1 = verdopple(start_wert)      # 5 * 2 = 10
schritt2 = addiere_zehn(schritt1)     # 10 + 10 = 20
print(f"Ergebnis: {schritt2}")

# Oder direkt verschachtelt:
ergebnis = addiere_zehn(verdopple(5))
print(f"Direkt verschachtelt: {ergebnis}")
```

### Mehrere Werte zurückgeben

Eine Funktion kann auch mehrere Werte zurückgeben! Python packt sie automatisch in ein Tupel:

```{code-cell} ipython3
def berechne_rechteck(laenge, breite):
    flaeche = laenge * breite
    umfang = 2 * (laenge + breite)
    return flaeche, umfang  # Gibt beide Werte zurück

# Beide Werte empfangen
f, u = berechne_rechteck(10, 5)
print(f"Fläche: {f}")
print(f"Umfang: {u}")
```

### Return beendet die Funktion

Wichtig zu wissen: Sobald `return` ausgeführt wird, endet die Funktion sofort!

```{code-cell} ipython3
def teste_return():
    print("Diese Zeile wird ausgeführt")
    return "Fertig!"
    print("Diese Zeile wird NIE ausgeführt")  # Unreachable code!

ergebnis = teste_return()
print(f"Rückgabewert: {ergebnis}")
```

### 🏃 Sofort ausprobieren!

**Aufgabe 1:** Schreiben Sie eine Funktion `berechne_kreis()`, die den Radius als Parameter nimmt und die Fläche zurückgibt (Fläche = radius * radius * 3.14159). Speichern Sie das Ergebnis in einer Variable und geben Sie es aus.

```{code-cell} ipython3
# Ihr Code hier:
def berechne_kreis(radius):
    flaeche = radius * radius * 3.14159
    return flaeche

flaeche = berechne_kreis(6)
print(f"Fläche ist: {flaeche}")
```

**Aufgabe 2:** Erstellen Sie eine Funktion `erstelle_email()`, die Vorname und Nachname als Parameter nimmt und eine E-Mail-Adresse zurückgibt (Format: vorname.nachname@student.uni.de). Verwenden Sie die Funktion, um E-Mails für drei verschiedene Personen zu erstellen.

```{code-cell} ipython3
# Ihr Code hier:
def erstelle_email(vorname, nachname):
    email = f"{vorname}.{nachname}@htw-berlin.de"
    return email

vorName = input("Wie heißt du?")
nachName = input("Wie ist dein Nachname?")
print(f"Die Emailadresse von {vorName} {nachName} ist {erstelle_email(vorName, nachName)} ")
```

**Aufgabe 3:** Schreiben Sie eine Funktion `analysiere_wort()`, die ein Wort als Parameter nimmt und sowohl die Länge als auch das erste und letzte Zeichen zurückgibt (als drei separate Werte).

```{code-cell} ipython3
# Ihr Code hier:
def analysiere_wort(wort):
    laenge = len(wort)
    erster = wort[0]
    letzter = wort[-1]
    return laenge, erster, letzter

lang, erst, letzt = analysiere_wort(input("Wie ist das Wort?"))
# lang, erst, letzt = analysiere_wort("Dorian"))
# lang, erst, letzt = (6, "D", "n")

print(f"Erster: {erst}; letzer {letzt}; länge {lang}")
```

```{code-cell} ipython3
# Ihr Code hier:
def analysiere_wort(wort):
    laenge = len(wort)
    erster = wort[0]
    letzter = wort[-1]

lang, erst, letzt = analysiere_wort(input("Wie ist das Wort?"))
# lang, erst, letzt = analysiere_wort("Dorian"))
# lang, erst, letzt = (6, "D", "n")

print(f"Erster: {erster}; letzer {letzter}; länge {laenge}")
```

<details>
<summary>🔍 Lösungen anzeigen</summary>

```python
# Aufgabe 1:
def berechne_kreis(radius):
    flaeche = radius * radius * 3.14159
    return flaeche

kreis_flaeche = berechne_kreis(5)
print(f"Die Fläche eines Kreises mit Radius 5 ist: {kreis_flaeche}")

# Aufgabe 2:
def erstelle_email(vorname, nachname):
    email = f"{vorname.lower()}.{nachname.lower()}@student.uni.de"
    return email

email1 = erstelle_email("Max", "Müller")
email2 = erstelle_email("Anna", "Schmidt")
email3 = erstelle_email("Tom", "Wagner")

print(f"E-Mail 1: {email1}")
print(f"E-Mail 2: {email2}")
print(f"E-Mail 3: {email3}")

# Aufgabe 3:
def analysiere_wort(wort):
    laenge = len(wort)
    erstes_zeichen = wort[0]
    letztes_zeichen = wort[-1]
    return laenge, erstes_zeichen, letztes_zeichen

l, e, z = analysiere_wort("Python")
print(f"Das Wort 'Python' hat {l} Zeichen")
print(f"Erstes Zeichen: {e}")
print(f"Letztes Zeichen: {z}")
```
</details>

+++

---
## 5. Scope - Gültigkeitsbereiche von Variablen 🔍

### Lokale vs. Globale Variablen

Ein wichtiges Konzept bei Funktionen ist der **Scope** (Gültigkeitsbereich) von Variablen. Nicht jede Variable ist überall in Ihrem Programm sichtbar!

**Die Analogie**: Stellen Sie sich ein Bürogebäude vor. Globale Variablen sind wie Aushänge im Eingangsbereich – jeder kann sie sehen. Lokale Variablen sind wie Notizen in einem bestimmten Büro – nur wer in diesem Büro ist, kann sie sehen.

### Lokale Variablen

Variablen, die **innerhalb einer Funktion** erstellt werden, sind **lokal**. Sie existieren nur innerhalb dieser Funktion:

```{code-cell} ipython3
def meine_funktion():
    lokale_variable = "Ich bin lokal!"  # Nur in der Funktion sichtbar
    print(lokale_variable)

meine_funktion()  # Funktioniert

# Das hier würde einen Fehler verursachen:
# print(lokale_variable)  # NameError: name 'lokale_variable' is not defined
```

### Globale Variablen

Variablen, die **außerhalb aller Funktionen** erstellt werden, sind **global**. Sie können überall gelesen werden:

```{code-cell} ipython3
globale_variable = "Ich bin global!"  # Außerhalb der Funktion

def zeige_global():
    print(globale_variable)  # Kann auf die globale Variable zugreifen

zeige_global()  # Funktioniert
print(globale_variable)  # Funktioniert auch
```

### Parameter sind auch lokal

Die Parameter einer Funktion verhalten sich wie lokale Variablen:

```{code-cell} ipython3
def verarbeite_name(name):  # 'name' ist lokal in der Funktion
    begruessung = f"Hallo {name}"  # 'begruessung' ist auch lokal
    return begruessung

ergebnis = verarbeite_name("Maria")
print(ergebnis)

# Das hier würde Fehler verursachen:
# print(name)  # NameError - 'name' existiert nur in der Funktion
# print(begruessung)  # NameError - 'begruessung' auch
```

---
## Zusammenfassung 🎓

### Was Sie gelernt haben:

Herzlichen Glückwunsch! Sie haben ein fundamentales Konzept der Programmierung gemeistert. Lassen Sie uns zusammenfassen, was Sie jetzt können:

✅ **Funktionen verstehen**: Sie wissen, dass Funktionen wiederverwendbare Code-Blöcke sind, die Ihr Programm strukturieren und organisieren

✅ **Funktionen definieren**: Sie können mit `def` eigene Funktionen erstellen und ihnen aussagekräftige Namen geben

✅ **Funktionen aufrufen**: Sie können definierte Funktionen verwenden, indem Sie ihren Namen mit runden Klammern aufrufen

✅ **Parameter verwenden**: Sie können Funktionen flexibel gestalten durch positionale und benannte Parameter

✅ **Return-Statement nutzen**: Sie können Funktionen Ergebnisse zurückgeben lassen, die Sie weiterverwenden können

✅ **Scope verstehen**: Sie wissen, dass Variablen lokale oder globale Gültigkeitsbereiche haben

### Wichtige Konzepte im Überblick:

| Konzept | Syntax | Beschreibung |
|---------|--------|--------------|
| Funktion definieren | `def name():` | Erstellt eine neue Funktion |
| Parameter | `def name(param1, param2):` | Platzhalter für Eingabewerte |
| Positionale Argumente | `name(wert1, wert2)` | Reihenfolge ist wichtig |
| Benannte Argumente | `name(param2=wert2, param1=wert1)` | Reihenfolge flexibel |
| Return | `return wert` | Gibt Ergebnis zurück |
| Lokaler Scope | Variable in Funktion | Nur in Funktion gültig |
| Globaler Scope | Variable außerhalb | Überall lesbar |

### Ihr Fortschritt:
✅ Start  
✅ Funktionen verstehen  
✅ Funktionen definieren  
✅ Funktionen aufrufen  
✅ Parameter und Argumente  
✅ Return-Statement  
✅ Scope verstehen  
✅ Fertig!

**Glückwunsch! Sie haben Notebook 07 erfolgreich abgeschlossen!** 🎉

+++

---
## Zusammenfassung 🎓

### Was Sie gelernt haben:

Herzlichen Glückwunsch! Sie haben ein fundamentales Konzept der Programmierung gemeistert. Lassen Sie uns zusammenfassen, was Sie jetzt können:

✅ **Funktionen verstehen**: Sie wissen, dass Funktionen wiederverwendbare Code-Blöcke sind, die Ihr Programm strukturieren und organisieren

✅ **Funktionen definieren**: Sie können mit `def` eigene Funktionen erstellen und ihnen aussagekräftige Namen geben

✅ **Funktionen aufrufen**: Sie können definierte Funktionen verwenden, indem Sie ihren Namen mit runden Klammern aufrufen

### Ihr Fortschritt:
✅ Start  
✅ Funktionen verstehen  
✅ Funktionen definieren  
✅ Funktionen aufrufen  
⬜ Fertig!

**Hinweis**: Dieses Notebook wurde aus didaktischen Gründen auf die Grundlagen von Funktionen beschränkt. Weitere Konzepte wie **Parameter**, **return**, und **Scope** werden in nachfolgenden Notebooks oder Lektionen behandelt, nachdem Sie die notwendigen Vorkenntnisse (wie Operatoren und Kontrollstrukturen) erlernt haben.

**Glückwunsch! Sie haben Notebook 07 erfolgreich abgeschlossen!** 🎉

+++

---
## Trainingsmaterial 💪

Jetzt ist es Zeit, Ihr Wissen zu festigen! Die folgenden Aufgaben sind in drei Schwierigkeitsstufen unterteilt.

+++

### 🟢 Einfache Aufgaben (zum Warmwerden)

Diese Aufgaben testen das Grundverständnis von Funktionen.

+++

#### Aufgabe 1: Begrüßung mit Parameter

Erstellen Sie eine Funktion `personalisierte_begruessung()`, die einen Namen als Parameter nimmt und eine persönliche Begrüßung ausgibt. Rufen Sie die Funktion mit drei verschiedenen Namen auf.

```{code-cell} ipython3
# Ihr Code hier:
```

#### Aufgabe 2: Persönliche Visitenkarte

Schreiben Sie eine Funktion `zeige_visitenkarte()`, die Ihre persönlichen Daten ausgibt: Name, E-Mail, Telefon. Formatieren Sie die Ausgabe schön mit Trennlinien.

```{code-cell} ipython3
# Ihr Code hier:
```

#### Aufgabe 3: Return verwenden

Erstellen Sie eine Funktion `quadriere()`, die eine Zahl als Parameter nimmt und das Quadrat zurückgibt. Verwenden Sie das Ergebnis, um das Quadrat von 5, 10 und 15 zu berechnen und auszugeben.

```{code-cell} ipython3
# Ihr Code hier:
```

### 🟡 Mittlere Aufgaben (schon besser!)

Diese Aufgaben erfordern, dass Sie mehrere Konzepte kombinieren.

+++

#### Aufgabe 4: Formatierte Ausgabe

Erstellen Sie eine Funktion `zeige_datentypen()`, die für drei vorher definierte Variablen (eine Zahl, ein Text, eine Liste) jeweils den Datentyp ausgibt. Verwenden Sie globale Variablen.

```{code-cell} ipython3
#### Aufgabe 4: Mehrere Parameter

Erstellen Sie eine Funktion `stelle_student_vor()` mit drei Parametern: `name`, `studiengang` und `semester`. Die Funktion soll alle Informationen formatiert ausgeben. Rufen Sie sie einmal mit positionalen und einmal mit benannten Argumenten auf.
```

#### Aufgabe 5: Mehrere Funktionen

Erstellen Sie drei Funktionen:
- `zeige_header()`: Gibt eine schöne Überschrift mit Trennlinien aus
- `zeige_inhalt()`: Gibt einen vordefinierten Text aus
- `zeige_footer()`: Gibt eine Fußzeile aus

Rufen Sie alle drei Funktionen nacheinander auf, um ein formatiertes Dokument zu erstellen.

```{code-cell} ipython3
#### Aufgabe 5: Return mit Berechnung

Schreiben Sie eine Funktion `celsius_zu_fahrenheit()`, die eine Temperatur in Celsius als Parameter nimmt und die Temperatur in Fahrenheit zurückgibt (Formel: fahrenheit = celsius * 1.8 + 32). Verwenden Sie die Funktion, um 0°C, 20°C und 100°C umzurechnen.
```

#### Aufgabe 6: Verschachtelte Aufrufe

Erstellen Sie eine Funktion `zeige_alles()`, die in sich andere bereits definierte Funktionen aufruft (z.B. `trennlinie()`, `zeige_info()`, etc.).

```{code-cell} ipython3
#### Aufgabe 6: Funktionen kombinieren

Erstellen Sie zwei Funktionen:
- `verdreifache()`: Nimmt eine Zahl als Parameter und gibt das Dreifache zurück
- `addiere_hundert()`: Nimmt eine Zahl als Parameter und gibt die Zahl plus 100 zurück

Verwenden Sie beide Funktionen nacheinander (verketten Sie sie), um verschiedene Zahlen zu verarbeiten.
```

### 🔴 Herausforderungen (für Profis)

Diese Aufgaben sind anspruchsvoller und erfordern kreatives Denken!

+++

#### Aufgabe 7: Menü-System

Erstellen Sie mehrere Funktionen für ein einfaches Menü-System:
- `zeige_hauptmenu()`: Zeigt die Menüoptionen
- `zeige_option1()`: Zeigt Informationen zu Option 1
- `zeige_option2()`: Zeigt Informationen zu Option 2
- `zeige_option3()`: Zeigt Informationen zu Option 3

Das Menü soll schön formatiert sein.

```{code-cell} ipython3
# Ihr Code hier:
```

#### Aufgabe 7: Benannte Argumente

Erstellen Sie eine Funktion `erstelle_adresse()` mit vier Parametern: `strasse`, `hausnummer`, `plz`, `stadt`. Die Funktion soll eine formatierte Adresse zurückgeben. Rufen Sie die Funktion dreimal auf:
1. Mit nur positionalen Argumenten
2. Mit nur benannten Argumenten in anderer Reihenfolge
3. Mit gemischten Argumenten (erst positional, dann benannt)

```{code-cell} ipython3
# Ihr Code hier:
```

#### Aufgabe 8: Mehrere Rückgabewerte

Erstellen Sie eine Funktion `analysiere_text()`, die einen Text als Parameter nimmt und drei Werte zurückgibt:
- Die Länge des Textes
- Das erste Zeichen
- Das letzte Zeichen

Testen Sie mit dem Text "Programmieren macht Spaß!".

```{code-cell} ipython3
# Ihr Code hier:
```

#### Aufgabe 9: Scope verstehen

Erstellen Sie ein kleines Programm, das den Unterschied zwischen lokalen und globalen Variablen zeigt:
1. Definieren Sie eine globale Variable `punkte` mit dem Wert 100
2. Erstellen Sie eine Funktion `aendere_lokal()`, die eine lokale Variable `punkte` mit dem Wert 50 erstellt und ausgibt
3. Erstellen Sie eine Funktion `zeige_global()`, die die globale Variable ausgibt
4. Rufen Sie beide Funktionen auf und geben Sie danach die globale Variable aus

+++

### Lösungen zu den einfachen Aufgaben 🟢

```{code-cell} ipython3
# Lösung Aufgabe 1: Mehrfache Begrüßung

def begruesse_dreimal():
    print("Hallo und herzlich willkommen!")
    print("Schön, dass Sie hier sind!")
    print("Viel Erfolg beim Lernen!")

# Test
begruesse_dreimal()
print()
begruesse_dreimal()
```

```{code-cell} ipython3
# Lösung Aufgabe 2: Persönliche Visitenkarte

def zeige_visitenkarte():
    print("==================================================")
    print("VISITENKARTE")
    print("==================================================")
    print("Name: Max Mustermann")
    print("E-Mail: max.mustermann@example.com")
    print("Telefon: +49 123 456789")
    print("==================================================")

# Test
zeige_visitenkarte()
```

```{code-cell} ipython3
# Lösung Aufgabe 1: Begrüßung mit Parameter

def personalisierte_begruessung(name):
    print(f"Hallo {name}!")
    print(f"Herzlich willkommen zum Python-Kurs, {name}!")
    print("-" * 40)

# Test mit drei verschiedenen Namen
personalisierte_begruessung("Anna")
personalisierte_begruessung("Max")
personalisierte_begruessung("Sophie")
```

### Lösungen zu den mittleren Aufgaben 🟡

```{code-cell} ipython3
# Lösung Aufgabe 3: Return verwenden

def quadriere(zahl):
    quadrat = zahl * zahl
    return quadrat

# Test mit verschiedenen Zahlen
ergebnis1 = quadriere(5)
ergebnis2 = quadriere(10)
ergebnis3 = quadriere(15)

print(f"Das Quadrat von 5 ist: {ergebnis1}")
print(f"Das Quadrat von 10 ist: {ergebnis2}")
print(f"Das Quadrat von 15 ist: {ergebnis3}")
```

```{code-cell} ipython3
# Lösung Aufgabe 5: Mehrere Funktionen

def zeige_header():
    print("============================================================")
    print("WILLKOMMEN ZU MEINEM PYTHON-DOKUMENT")
    print("============================================================")

def zeige_inhalt():
    print("Dies ist ein Beispieltext.")
    print("Funktionen machen Python-Code übersichtlich und wiederverwendbar.")
    print("Sie sind ein fundamentales Konzept der Programmierung.")

def zeige_footer():
    print("============================================================")
    print("Ende des Dokuments - Vielen Dank!")
    print("============================================================")

# Dokument erstellen
zeige_header()
print()
zeige_inhalt()
print()
zeige_footer()
```

```{code-cell} ipython3
# Lösung Aufgabe 6: Verschachtelte Aufrufe

def trennlinie():
    print("--------------------------------------------------")

def zeige_info():
    print("Name: Anna Müller")
    print("Studiengang: Informatik")

def zeige_alles():
    trennlinie()
    print("KOMPLETTE INFORMATION")
    trennlinie()
    zeige_info()
    trennlinie()

# Test
zeige_alles()
```

### Lösungen zu den Herausforderungen 🔴

```{code-cell} ipython3
# Lösung Aufgabe 4: Mehrere Parameter

def stelle_student_vor(name, studiengang, semester):
    print("=================================================")
    print("STUDENTEN-INFORMATION")
    print("=================================================")
    print(f"Name: {name}")
    print(f"Studiengang: {studiengang}")
    print(f"Semester: {semester}")
    print("=================================================")

# Mit positionalen Argumenten
stelle_student_vor("Lisa Schmidt", "Informatik", 3)

print()  # Leerzeile für bessere Übersicht

# Mit benannten Argumenten
stelle_student_vor(semester=5, name="Tom Wagner", studiengang="Wirtschaftsinformatik")
```

```{code-cell} ipython3
# Lösung Aufgabe 5: Return mit Berechnung

def celsius_zu_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

# Test mit verschiedenen Temperaturen
temp1 = celsius_zu_fahrenheit(0)
temp2 = celsius_zu_fahrenheit(20)
temp3 = celsius_zu_fahrenheit(100)

print(f"0°C entspricht {temp1}°F")
print(f"20°C entspricht {temp2}°F")
print(f"100°C entspricht {temp3}°F")
```

```{code-cell} ipython3
# Lösung Aufgabe 6: Funktionen kombinieren

def verdreifache(zahl):
    return zahl * 3

def addiere_hundert(zahl):
    return zahl + 100

# Test mit verschiedenen Zahlen
# Erst verdreifachen, dann 100 addieren
zahl1 = 5
schritt1 = verdreifache(zahl1)
ergebnis1 = addiere_hundert(schritt1)
print(f"{zahl1} → verdreifachen → {schritt1} → +100 → {ergebnis1}")

# Direkt verschachtelt
zahl2 = 10
ergebnis2 = addiere_hundert(verdreifache(zahl2))
print(f"{zahl2} → verdreifachen & +100 → {ergebnis2}")

# Andersherum: Erst 100 addieren, dann verdreifachen
zahl3 = 7
ergebnis3 = verdreifache(addiere_hundert(zahl3))
print(f"{zahl3} → +100 & verdreifachen → {ergebnis3}")
```

---
## Ausblick auf Notebook 08 👀

Im nächsten Notebook lernen Sie **Operatoren** kennen:

- 🧮 **Arithmetische Operatoren**: Addition, Subtraktion, Multiplikation, Division
- ⚖️ **Vergleichsoperatoren**: Größer, kleiner, gleich
- 🔗 **Logische Operatoren**: and, or, not
- 📍 **Zugehörigkeitsoperatoren**: in, not in

Damit können Sie dann mathematische Berechnungen durchführen und Werte miteinander vergleichen! Anschließend werden auch die Funktionskonzepte um **Parameter**, **return** und **Scope** erweitert.

**Bis dahin: Viel Erfolg beim Üben!** 🚀

```{code-cell} ipython3
# Lösung Aufgabe 8: Mehrere Rückgabewerte

def analysiere_text(text):
    laenge = len(text)
    erstes_zeichen = text[0]
    letztes_zeichen = text[-1]
    
    return laenge, erstes_zeichen, letztes_zeichen

# Test mit dem vorgegebenen Text
test_text = "Programmieren macht Spaß!"
laenge, erstes, letztes = analysiere_text(test_text)

print(f"Analyse des Textes: '{test_text}'")
print(f"Textlänge: {laenge} Zeichen")
print(f"Erstes Zeichen: '{erstes}'")
print(f"Letztes Zeichen: '{letztes}'")
```

```{code-cell} ipython3
# Lösung Aufgabe 8: Mehrere Rückgabewerte

def analysiere_liste(zahlen_liste):
    anzahl = len(zahlen_liste)
    
    # Manuell das Minimum finden
    kleinstes = zahlen_liste[0]
    for zahl in zahlen_liste:
        if zahl < kleinstes:
            kleinstes = zahl
    
    # Manuell das Maximum finden
    groesstes = zahlen_liste[0]
    for zahl in zahlen_liste:
        if zahl > groesstes:
            groesstes = zahl
    
    return anzahl, kleinstes, groesstes

# Test mit der vorgegebenen Liste
test_liste = [15, 3, 42, 7, 28, 1, 99]
anzahl, minimum, maximum = analysiere_liste(test_liste)

print(f"Analyse der Liste {test_liste}:")
print(f"Anzahl Elemente: {anzahl}")
print(f"Kleinstes Element: {minimum}")
print(f"Größtes Element: {maximum}")
```

```{code-cell} ipython3
# Lösung Aufgabe 9: Scope verstehen

# 1. Globale Variable definieren
punkte = 100

# 2. Funktion mit lokaler Variable
def aendere_lokal():
    punkte = 50  # Dies ist eine LOKALE Variable mit gleichem Namen
    print(f"In aendere_lokal(): punkte = {punkte}")

# 3. Funktion die die globale Variable anzeigt
def zeige_global():
    print(f"In zeige_global(): punkte = {punkte}")

# 4. Beide Funktionen aufrufen und globale Variable ausgeben
print(f"Globale Variable vor Funktionsaufrufen: punkte = {punkte}")
print()

aendere_lokal()  # Zeigt 50 (lokal)
zeige_global()    # Zeigt 100 (global)

print()
print(f"Globale Variable nach Funktionsaufrufen: punkte = {punkte}")
print("→ Die globale Variable wurde nicht verändert!")
```
