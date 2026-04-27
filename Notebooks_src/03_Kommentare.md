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

# 03 - Kommentare: Notizen in Ihrem Code

+++

## Willkommen!

In diesem Notebook lernen Sie, wie Sie Notizen und Erklärungen direkt in Ihrem Python-Code hinterlassen können. Kommentare sind wie Post-it-Notizen in einem Buch - sie helfen Ihnen und anderen, den Code später zu verstehen.

+++

## Was Sie heute lernen:
- Warum Kommentare in der Programmierung wichtig sind
- Wie Sie einzeilige Kommentare mit `#` schreiben
- Wie Sie mehrzeilige Kommentare mit `'''` erstellen
- Wann und wo Sie Kommentare sinnvoll einsetzen

+++

## Voraussetzungen
Was Sie schon können sollten:
- Grundverständnis von Programmiersprachen (Notebook 01)
- Die `print()` Funktion verwenden (Notebook 02)
- Die `input()` Funktion verwenden (Notebook 02)

+++

## Warum brauchen wir Kommentare?

+++

### Die Motivation: Notizen für die Zukunft

Stellen Sie sich vor, Sie schreiben heute ein Rezept auf. Drei Monate später wollen Sie das Gericht nachkochen. Manche Schritte haben Sie vergessen - warum sollte die Soße genau 10 Minuten köcheln? Hätten Sie sich damals eine kleine Notiz gemacht: "10 Minuten, damit die Gewürze sich entfalten", wäre alles klar!

Genau so ist es beim Programmieren. Heute schreiben Sie Code und wissen genau, was jede Zeile macht und warum. Aber was ist in einer Woche? In einem Monat? Oder wenn eine Kollegin Ihren Code lesen muss?

**Kommentare sind Ihre Notizen im Code.** Sie erklären:
- **Was** ein bestimmter Code-Abschnitt macht
- **Warum** Sie etwas auf eine bestimmte Weise programmiert haben
- **Wie** komplizierte Teile funktionieren
- **Achtung** bei möglichen Problemen oder Besonderheiten

Das Besondere: Python ignoriert diese Kommentare komplett beim Ausführen des Programms! Sie sind nur für menschliche Leser gedacht - für Sie selbst, Ihre Kollegen, oder jeden, der später mit dem Code arbeitet.

Gute Kommentare machen den Unterschied zwischen einem Code, den man versteht, und einem, der wie eine Geheimsprache wirkt!

+++

## 1️⃣ Einzeilige Kommentare mit #

+++

### Das Raute-Symbol: Ihr Kommentar-Marker

In Python verwenden wir das **Raute-Symbol `#`** (auch Hashtag genannt), um einen Kommentar zu beginnen. Stellen Sie sich das `#` wie einen Stoppschild für Python vor: "Halt! Ab hier ist eine Notiz für Menschen, nicht für dich!"

**Wie funktioniert das?** Sobald Python beim Ausführen Ihres Programms ein `#` sieht, ignoriert es alles, was in dieser Zeile danach kommt. Die gesamte Zeile ab dem `#` wird übersprungen - als wäre sie unsichtbar für den Computer.

**Wo können Sie das `#` platzieren?**
- Am Anfang einer Zeile: Die ganze Zeile wird zum Kommentar
- Mitten in einer Zeile: Nur der Teil nach dem `#` wird zum Kommentar

**Wann sollten Sie einzeilige Kommentare nutzen?**
- Für kurze Erklärungen zu einer Zeile Code
- Um komplizierte Berechnungen zu erläutern
- Für schnelle Hinweise und Erinnerungen
- Um Code vorübergehend zu "deaktivieren" (ohne ihn zu löschen)

Wichtig: Ein Kommentar sollte erklären WARUM etwas gemacht wird, nicht nur WAS. Das WAS sieht man oft am Code selbst!

+++

### Beispiel 1: Kommentar am Zeilenanfang

Schauen wir uns an, wie ein Kommentar aussieht, der eine ganze Zeile einnimmt:

```{code-cell}
# Dies ist ein Kommentar - Python ignoriert diese Zeile komplett!
print("Hallo Welt")
```

**Was passiert hier?**
- Die erste Zeile beginnt mit `#` - Python überspringt sie
- Nur die zweite Zeile wird ausgeführt und gibt "Hallo Welt" aus
- Der Kommentar erscheint nicht in der Ausgabe!

+++

### Beispiel 2: Kommentar nach Code in derselben Zeile

Sie können auch Kommentare direkt hinter Code-Zeilen schreiben:

```{code-cell}
print("Willkommen!")  # Begrüßung für den Benutzer
```

**Was passiert hier?**
- Python führt den Teil vor dem `#` aus: `print("Willkommen!")`
- Alles nach dem `#` wird ignoriert
- Diese Art Kommentar erklärt, was die Zeile macht

+++

### Beispiel 3: Mehrere Kommentarzeilen hintereinander

Für längere Erklärungen können Sie mehrere Zeilen mit `#` verwenden:

```{code-cell}
# Dieses Programm begrüßt den Benutzer
# und fragt nach seinem Namen.
# Dann wird eine personalisierte Nachricht ausgegeben.

print("Hallo! Wie heißen Sie?")
name = input()  # Wartet auf Benutzereingabe
print("Schön, Sie kennenzulernen!")
```

**Was passiert hier?**
- Die ersten drei Zeilen sind Kommentare (alle beginnen mit `#`)
- Sie beschreiben, was das gesamte Programm macht
- Nur die Code-Zeilen ohne `#` werden ausgeführt

+++

### Beispiel 4: Code vorübergehend deaktivieren

Ein praktischer Trick: Mit `#` können Sie Code "auskommentieren", ohne ihn zu löschen:

```{code-cell}
print("Diese Zeile wird ausgeführt")
# print("Diese Zeile wird NICHT ausgeführt")
print("Diese Zeile wird auch ausgeführt")
```

**Was passiert hier?**
- Die erste und dritte `print()` werden ausgeführt
- Die mittlere `print()` Zeile ist auskommentiert - sie wird übersprungen
- Praktisch zum Testen: Code behalten, aber vorübergehend deaktivieren!

+++

### Sofort ausprobieren!

**Aufgabe 1:** Schreiben Sie einen Kommentar, der erklärt, was Ihr Lieblingsgericht ist, und darunter einen `print()` Befehl, der "Guten Appetit!" ausgibt.

```{code-cell}
# Ihr Code hier:
```

**Aufgabe 2:** Schreiben Sie drei `print()` Befehle untereinander. Kommentieren Sie den mittleren aus, sodass nur der erste und dritte ausgeführt werden.

```{code-cell}
# Ihr Code hier:
```

**Aufgabe 3:** Schreiben Sie eine `print()` Anweisung mit einem Kommentar am Ende der Zeile (hinter dem Code), der erklärt, was ausgegeben wird.

```{code-cell}
# Ihr Code hier:
```

<details>
<summary>Lösungen anzeigen</summary>

```python
# Aufgabe 1:
# Mein Lieblingsgericht ist Pizza Margherita
print("Guten Appetit!")

# Aufgabe 2:
print("Diese Zeile wird angezeigt")
# print("Diese Zeile wird NICHT angezeigt")
print("Diese Zeile wird auch angezeigt")

# Aufgabe 3:
print("Python macht Spaß!")  # Gibt eine motivierende Nachricht aus
```
</details>

+++

## 2️⃣ Mehrzeilige Kommentare mit '''

+++

### Längere Erklärungen: Der Kommentar-Block

Manchmal reicht eine einzelne Kommentarzeile nicht aus. Stellen Sie sich vor, Sie müssten erklären, wie ein komplexeres Programm funktioniert, oder Sie möchten eine ausführliche Beschreibung am Anfang einer Datei schreiben. Jede Zeile mit einem `#` zu beginnen, wäre mühsam!

**Die Lösung: Mehrzeilige Kommentare mit drei Anführungszeichen `'''`**

In Python können Sie einen Textblock in dreifache Anführungszeichen einschließen: `'''` am Anfang und `'''` am Ende. Technisch gesehen ist dies ein String (eine Zeichenkette), aber wenn dieser String nirgendwo verwendet wird - also nicht ausgegeben oder gespeichert wird - verhält er sich wie ein Kommentar.

**Wann sollten Sie mehrzeilige Kommentare nutzen?**
- Für Programmbeschreibungen am Dateianfang
- Für ausführliche Erklärungen komplexer Abschnitte
- Für Dokumentationen (wer hat's geschrieben, wann, warum)
- Für längere Hinweise oder Anleitungen

**Wichtig zu wissen:** Sie können auch dreifache doppelte Anführungszeichen `"""` verwenden - beide funktionieren gleich. Am häufigsten sehen Sie aber die einfachen Anführungszeichen `'''`.

Ein Vorteil: Alles zwischen den `'''` wird als ein Block behandelt - Sie können neue Zeilen beginnen, ohne jedes Mal ein `#` zu tippen!

+++

### Beispiel 1: Einfacher mehrzeiliger Kommentar

So sieht ein mehrzeiliger Kommentar aus:

```{code-cell}
'''
Dies ist ein mehrzeiliger Kommentar.
Er kann über mehrere Zeilen gehen.
Python ignoriert diesen gesamten Block.
'''

print("Nur diese Zeile wird ausgeführt!")
```

**Was passiert hier?**
- Alles zwischen den beiden `'''` wird ignoriert
- Sie können beliebig viele Zeilen schreiben
- Nur der `print()` Befehl wird ausgeführt

+++

### Beispiel 2: Programm-Dokumentation

Mehrzeilige Kommentare werden oft am Anfang eines Programms verwendet:

```{code-cell}
'''
Programm: Begrüßungs-Assistent
Autor: Max Mustermann
Datum: 2025-11-09

Beschreibung:
Dieses Programm begrüßt Benutzer und merkt sich ihren Namen.
Es zeigt, wie man mit Benutzereingaben arbeitet.
'''

print("Herzlich willkommen!")
print("Dieses Programm wurde sorgfältig dokumentiert.")
```

**Was passiert hier?**
- Der mehrzeilige Kommentar enthält wichtige Metadaten
- Wer das Programm später öffnet, weiß sofort, worum es geht
- Nur die beiden `print()` Befehle werden ausgeführt

+++

### Beispiel 3: Alternative mit doppelten Anführungszeichen

Sie können auch `"""` statt `'''` verwenden - das Ergebnis ist identisch:

```{code-cell}
"""
Dies ist ebenfalls ein mehrzeiliger Kommentar.
Manche Programmierer bevorzugen diese Variante.
Beide Formen funktionieren genau gleich!
"""

print("Code wird normal ausgeführt.")
```

**Was passiert hier?**
- Dreifache doppelte Anführungszeichen `"""` funktionieren genauso wie `'''`
- Der Text dazwischen wird ignoriert
- Wählen Sie die Variante, die Ihnen besser gefällt!

+++

### Beispiel 4: Kombination mit einzeiligen Kommentaren

Sie können beide Kommentar-Arten im selben Programm verwenden:

```{code-cell}
'''
Dieses Programm demonstriert verschiedene Ausgaben.
Es zeigt, wie man Kommentare kombiniert.
'''

print("Erste Nachricht")  # Einfache Ausgabe

# Hier kommt die zweite Ausgabe
print("Zweite Nachricht")

print("Dritte Nachricht")  # Noch eine Ausgabe
```

**Was passiert hier?**
- Mehrzeiliger Kommentar am Anfang für die Gesamtbeschreibung
- Einzeilige Kommentare (`#`) für spezifische Zeilen-Erklärungen
- So kombinieren Sie beide Techniken sinnvoll!

+++

### Sofort ausprobieren!

**Aufgabe 1:** Erstellen Sie einen mehrzeiligen Kommentar, der Ihre drei Lieblingshobby beschreibt. Schreiben Sie darunter einen `print()` Befehl.

```{code-cell}
# Ihr Code hier:
```

**Aufgabe 2:** Schreiben Sie eine Programm-Dokumentation mit: Ihrem Namen, dem heutigen Datum und einer kurzen Beschreibung (was das Programm machen soll). Verwenden Sie einen mehrzeiligen Kommentar.

```{code-cell}
# Ihr Code hier:
```

**Aufgabe 3:** Kombinieren Sie einen mehrzeiligen Kommentar am Anfang mit zwei `print()` Befehlen, von denen jeder einen einzeiligen Kommentar (mit `#`) am Ende hat.

```{code-cell}
# Ihr Code hier:
```

<details>
<summary>Lösungen anzeigen</summary>

```python
# Aufgabe 1:
'''
Meine drei Lieblingshobby sind:
1. Lesen
2. Wandern
3. Fotografieren
'''
print("Hobbys sind wichtig für die Work-Life-Balance!")

# Aufgabe 2:
'''
Programm: Mein erstes Python-Programm
Autor: Anna Schmidt
Datum: 2025-11-09

Beschreibung:
Dieses Programm dient als Übung für mehrzeilige Kommentare.
Es zeigt, wie man Programme richtig dokumentiert.
'''
print("Dokumentation ist wichtig!")

# Aufgabe 3:
'''
Kombinations-Beispiel:
Dieses Programm zeigt beide Kommentar-Arten.
'''
print("Erste Ausgabe")  # Begrüßung
print("Zweite Ausgabe")  # Abschied
```
</details>

+++

## Wann welche Kommentar-Art verwenden?

+++

### Entscheidungshilfe: `#` oder `'''`?

Jetzt kennen Sie beide Kommentar-Arten. Aber wann verwendet man welche? Hier eine praktische Übersicht:

**Einzeilige Kommentare (`#`) verwenden für:**
- Kurze Erklärungen zu einzelnen Code-Zeilen
- Hinweise direkt neben dem Code
- Schnelle Notizen und Erinnerungen
- Vorübergehendes Deaktivieren von Code-Zeilen

**Mehrzeilige Kommentare (`'''`) verwenden für:**
- Programm-Dokumentation am Dateianfang
- Ausführliche Beschreibungen komplexer Abschnitte
- Längere Erklärungen, die mehrere Zeilen benötigen
- Metadaten (Autor, Datum, Version, etc.)

**Faustregel:** Wenn Ihre Erklärung länger als 2-3 Zeilen ist, verwenden Sie `'''`. Für alles andere reicht `#`!

Wichtig: Gute Kommentare erklären das WARUM, nicht nur das WAS. Der Code selbst zeigt WAS passiert - Ihr Kommentar sollte erklären WARUM Sie es so gemacht haben!

+++

## Zusammenfassung

Was Sie gelernt haben:
- ✅ **Kommentare** sind Notizen im Code, die Python ignoriert
- ✅ **Einzeilige Kommentare** beginnen mit `#` und gehen bis zum Zeilenende
- ✅ **Mehrzeilige Kommentare** stehen zwischen `'''` oder `"""`
- ✅ Kommentare helfen Ihnen und anderen, den Code zu verstehen
- ✅ Gute Kommentare erklären das WARUM, nicht nur das WAS
- ✅ Sie können beide Kommentar-Arten kombinieren

**Wichtigste Erkenntnis:** Kommentare sind wie Wegweiser in Ihrem Code. Sie kosten wenig Zeit beim Schreiben, sparen aber viel Zeit beim späteren Lesen und Verstehen!

+++

## Trainingsmaterial

+++

### Einfache Aufgaben (zum Warmwerden)

**Aufgabe 1:** Schreiben Sie drei einzeilige Kommentare, die Ihre Morgenroutine beschreiben (z.B. Aufstehen, Frühstücken, Zähneputzen). Schreiben Sie darunter einen `print()` Befehl, der "Guten Morgen!" ausgibt.

```{code-cell}
# Ihr Code hier:
```

**Aufgabe 2:** Kopieren Sie diesen Code und kommentieren Sie die mittlere Zeile aus:
```python
print("Zeile 1")
print("Zeile 2")
print("Zeile 3")
```
Nur Zeile 1 und 3 sollen ausgegeben werden.

```{code-cell}
# Ihr Code hier:
```

**Aufgabe 3:** Schreiben Sie einen mehrzeiligen Kommentar, der erklärt, was Ihr Lieblingsbuch ist und warum Sie es mögen. Mindestens 3 Zeilen!

```{code-cell}
# Ihr Code hier:
```

### Mittlere Aufgaben (schon besser!)

**Aufgabe 4:** Erstellen Sie ein kleines Programm mit folgender Struktur:
- Mehrzeiliger Kommentar am Anfang mit Programm-Titel, Ihrem Namen und Datum
- Drei `print()` Befehle, die verschiedene Nachrichten ausgeben
- Jeder `print()` Befehl hat einen einzeiligen Kommentar, der erklärt, was ausgegeben wird

```{code-cell}
# Ihr Code hier:
```

**Aufgabe 5:** Schreiben Sie ein Programm, das:
- Mit `input()` nach dem Namen fragt
- Mit `input()` nach dem Wohnort fragt
- Mit `print()` beide Informationen ausgibt
- Jede Zeile hat einen sinnvollen Kommentar, der erklärt, was passiert

```{code-cell}
# Ihr Code hier:
```

### Herausforderungen (für Profis)

**Aufgabe 6:** Erstellen Sie ein gut dokumentiertes Programm, das:
- Einen mehrzeiligen Kommentar am Anfang hat (Programmbeschreibung)
- Den Benutzer nach drei verschiedenen Informationen fragt (z.B. Name, Alter, Lieblingsfarbe)
- Alle drei Informationen in einer zusammenhängenden Nachricht ausgibt
- Mindestens 5 sinnvolle einzeilige Kommentare enthält
- Professionell strukturiert und leicht verständlich ist

Stellen Sie sich vor, dass eine Kollegin in 6 Monaten Ihren Code lesen muss - sie sollte sofort verstehen, was Sie gemacht haben!

```{code-cell}
# Ihr Code hier:
```

## Musterlösungen

+++

### Lösung Aufgabe 1

**Überlegung:**
- Wir brauchen drei einzeilige Kommentare mit `#`
- Jeder Kommentar beschreibt einen Schritt der Morgenroutine
- Danach kommt ein `print()` Befehl

**Lösung:**

```{code-cell}
# Schritt 1: Um 7 Uhr aufstehen und Wecker ausschalten
# Schritt 2: Frühstück mit Kaffee und Brötchen
# Schritt 3: Zähne putzen und für den Tag fertig machen

print("Guten Morgen!")
```

**Erklärung:**
- Drei Kommentarzeilen beginnen jeweils mit `#`
- Sie beschreiben die Morgenroutine
- Die `print()` Zeile wird ausgeführt, die Kommentare werden ignoriert

+++

### Lösung Aufgabe 2

**Überlegung:**
- Wir müssen die mittlere `print()` Zeile deaktivieren
- Dazu setzen wir ein `#` an den Anfang dieser Zeile
- Die anderen beiden Zeilen bleiben unverändert

**Lösung:**

```{code-cell}
print("Zeile 1")
# print("Zeile 2")
print("Zeile 3")
```

**Erklärung:**
- Die erste Zeile wird normal ausgeführt
- Die zweite Zeile ist auskommentiert und wird übersprungen
- Die dritte Zeile wird wieder ausgeführt
- Ausgabe: "Zeile 1" und "Zeile 3"

+++

### Lösung Aufgabe 3

**Überlegung:**
- Wir brauchen einen mehrzeiligen Kommentar mit `'''`
- Mindestens 3 Zeilen Text über ein Lieblingsbuch
- Der Kommentar wird von Python ignoriert

**Lösung:**

```{code-cell}
'''
Mein Lieblingsbuch ist "Der kleine Prinz" von Antoine de Saint-Exupéry.
Es gefällt mir, weil es tiefe Lebensweisheiten in einer einfachen,
poetischen Geschichte verpackt.
Die Botschaft über Freundschaft und das Wesentliche im Leben
berührt mich jedes Mal aufs Neue.
'''
```

**Erklärung:**
- Der gesamte Text zwischen `'''` wird als Kommentar behandelt
- Mehrere Zeilen sind möglich ohne `#` vor jeder Zeile
- Python ignoriert diesen Block komplett

+++

### Lösung Aufgabe 4

**Überlegung:**
- Mehrzeiliger Kommentar am Anfang für Metadaten
- Drei `print()` Befehle mit unterschiedlichen Nachrichten
- Jeder `print()` bekommt einen erklärenden Kommentar am Ende

**Lösung:**

```{code-cell}
'''
Programm: Nachrichten-Ausgabe
Autor: Lisa Müller
Datum: 2025-11-09

Beschreibung:
Dieses Programm zeigt verschiedene Nachrichten an
und demonstriert die Verwendung von Kommentaren.
'''

print("Willkommen bei unserem Programm!")  # Begrüßung des Benutzers
print("Heute lernen wir Kommentare.")  # Information über das Lernziel
print("Viel Erfolg beim Üben!")  # Motivierende Abschlussnachricht
```

**Erklärung:**
- Der mehrzeilige Kommentar dokumentiert das Programm professionell
- Jeder `print()` Befehl hat einen Kommentar, der den Zweck erklärt
- Die Struktur ist übersichtlich und gut dokumentiert

**Häufige Fehler:**
- Vergessen, die `'''` am Ende zu schließen
- Kommentare zu allgemein ("gibt Text aus" statt zu erklären WELCHEN Text und WARUM)

+++

### Lösung Aufgabe 5

**Überlegung:**
- Zwei `input()` Befehle für Name und Wohnort
- Ein `print()` Befehl zur Ausgabe
- Jede Zeile braucht einen sinnvollen Kommentar

**Lösung:**

```{code-cell}
# Frage nach dem Namen des Benutzers
print("Wie heißen Sie?")
name = input()  # Wartet auf Eingabe und speichert den Namen

# Frage nach dem Wohnort
print("Wo wohnen Sie?")
wohnort = input()  # Wartet auf Eingabe und speichert den Wohnort

# Ausgabe der gesammelten Informationen
print("Schön, Sie kennenzulernen!")
print(name)
print(wohnort)
```

**Erklärung:**
- Kommentare erklären, was jeder Schritt macht
- Die `input()` Befehle warten auf Benutzereingaben
- Die `print()` Befehle geben die Informationen aus

**Häufige Fehler:**
- Vergessen, vor `input()` eine Frage mit `print()` auszugeben
- Kommentare sind zu kurz oder nicht aussagekräftig

+++

### Lösung Aufgabe 6

**Überlegung:**
- Professionelle Dokumentation am Anfang
- Drei `input()` Befehle für verschiedene Informationen
- Zusammenhängende Ausgabe aller Informationen
- Mindestens 5 sinnvolle Kommentare
- Gut strukturiert und verständlich

**Lösung:**

```{code-cell}
'''
Programm: Benutzer-Profil-Erfassung
Autor: Thomas Weber
Datum: 2025-11-09
Version: 1.0

Beschreibung:
Dieses Programm sammelt drei Informationen vom Benutzer
(Name, Alter, Lieblingsfarbe) und gibt sie in einer
zusammenhängenden, benutzerfreundlichen Nachricht aus.

Zweck:
Demonstriert die Verwendung von input() und print()
sowie professionelle Code-Dokumentation.
'''

# Begrüßung und Erklärung des Programms
print("Willkommen! Ich möchte Sie gerne kennenlernen.")
print("Bitte beantworten Sie drei kurze Fragen.")
print("")  # Leerzeile für bessere Lesbarkeit

# Erste Frage: Name des Benutzers erfassen
print("Wie ist Ihr Name?")
name = input()  # Speichert die Namenseingabe

# Zweite Frage: Alter des Benutzers erfassen
print("Wie alt sind Sie?")
alter = input()  # Speichert die Alterseingabe

# Dritte Frage: Lieblingsfarbe erfassen
print("Was ist Ihre Lieblingsfarbe?")
farbe = input()  # Speichert die Farbeingabe

# Zusammenfassende Ausgabe aller Informationen
print("")  # Leerzeile zur Trennung
print("Vielen Dank für Ihre Angaben!")
print("Hier ist Ihr Profil:")
print("")
print("Name:")
print(name)
print("Alter:")
print(alter)
print("Lieblingsfarbe:")
print(farbe)
print("")  # Abschließende Leerzeile
print("Schön, Sie kennenzulernen!")
```

**Erklärung:**
- Der mehrzeilige Kommentar am Anfang ist sehr ausführlich und professionell
- Jeder wichtige Code-Abschnitt hat einen erklärenden Kommentar
- Das Programm ist logisch strukturiert (Begrüßung → Fragen → Ausgabe)
- Leerzeilen (mit `print("")`) machen die Ausgabe übersichtlicher
- Insgesamt 8 einzeilige Kommentare erklären den Code-Ablauf

**Häufige Fehler:**
- Zu wenig Kommentare oder nur oberflächliche Erklärungen
- Unstrukturierte Ausgabe ohne Leerzeilen
- Fehlende Programm-Dokumentation am Anfang
- Kommentare, die nur wiederholen, was der Code macht, statt zu erklären WARUM

+++

## Gratulation!

Sie haben das Notebook zu Kommentaren erfolgreich abgeschlossen! Sie wissen jetzt, wie Sie Ihren Code dokumentieren und für andere (und Ihr zukünftiges Ich) verständlich machen.

**Nächste Schritte:**
- Im nächsten Notebook lernen Sie **Variablen** kennen
- Variablen sind wie beschriftete Schubladen, in denen Sie Werte speichern können
- Mit Variablen wird Ihr Code noch mächtiger und flexibler!

Bis bald! 👋
