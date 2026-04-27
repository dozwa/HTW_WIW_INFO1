---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
---

# 01 - Einführung in Programmiersprachen: Ihre ersten Schritte in die Welt des Programmierens 🎯

## Willkommen! 👋

Herzlich willkommen zu Ihrem ersten Schritt in die faszinierende Welt der Programmierung! In diesem Notebook lernen Sie die grundlegenden Konzepte kennen, die das Fundament für alles Weitere bilden.

Sie werden verstehen, was eine Programmiersprache ist, warum wir Python verwenden und wie Computer überhaupt Programme verarbeiten.

## Was Sie heute lernen:
- Was Programmiersprachen sind und wofür wir sie brauchen
- Warum Python eine ideale Einstiegssprache ist
- Wie Python-Programme ausgeführt werden (Interpreter vs. Compiler)
- Was Syntax und Semantik bedeuten
- Grundlegende Konzepte der Programmentwicklung

## Voraussetzungen 📚
**Keine!** Dies ist das erste Notebook. Sie benötigen keinerlei Programmiererfahrung.

+++

---

## 1. Was ist eine Programmiersprache? 🗣️

### Die Brücke zwischen Mensch und Computer

Stellen Sie sich vor, Sie möchten einem Computer eine Aufgabe erklären. Das Problem: Computer verstehen keine menschliche Sprache wie Deutsch oder Englisch. Sie arbeiten nur mit Zahlen - genauer gesagt mit Einsen und Nullen. Hier kommen Programmiersprachen ins Spiel!

Eine **Programmiersprache** ist eine formale Sprache, die speziell dafür entwickelt wurde, dass Menschen mit Computern kommunizieren können. Sie ist wie ein Übersetzer zwischen Ihrer Denkweise und der Art, wie Computer arbeiten.

+++

### Der Vergleich mit natürlichen Sprachen

Ähnlich wie bei menschlichen Sprachen (Deutsch, Englisch, Spanisch) gibt es auch in Programmiersprachen:

- **Vokabeln** (Befehle und Funktionen, die der Computer kennt)
- **Grammatik** (Regeln, wie man diese Befehle korrekt formuliert)
- **Bedeutung** (Was passiert, wenn der Computer Ihre Anweisungen ausführt)

Der große Unterschied: Während Menschen flexibel sind und auch fehlerhafte Sätze verstehen können, sind Computer sehr präzise. Ein einziger Tippfehler - und das Programm funktioniert nicht!

+++

### Von der Idee zum lauffähigen Programm

Der Entwicklungsprozess läuft typischerweise so ab:

1. **Sie haben eine Idee** - z.B. "Ich möchte alle Zahlen von 1 bis 100 addieren"
2. **Sie überlegen sich einen Algorithmus** - also eine Schritt-für-Schritt-Anleitung
3. **Sie schreiben Code** - Sie übersetzen Ihre Idee in eine Programmiersprache
4. **Der Computer führt aus** - Er folgt Ihren Anweisungen präzise
5. **Sie erhalten das Ergebnis** - Der Computer zeigt Ihnen das Ergebnis an

In den kommenden Wochen werden Sie genau diesen Prozess immer wieder durchlaufen und dabei immer komplexere Aufgaben lösen können!

+++

---

## 2. Python - Unsere Programmiersprache 🐍

### Eine Sprache mit Geschichte

**Python** wurde Anfang der 1990er Jahre von dem niederländischen Programmierer Guido van Rossum entwickelt. Der Name "Python" stammt übrigens nicht von der Schlange, sondern von der britischen Comedy-Gruppe "Monty Python" - Guido van Rossum war großer Fan!

Heute, über 30 Jahre später, ist Python eine der meistgenutzten Programmiersprachen weltweit. Sie wird von Millionen von Entwicklern verwendet - von Anfängern bis zu Experten bei Google, NASA und anderen führenden Organisationen.

+++

### Warum ist Python ideal für Einsteiger?

Python zeichnet sich durch mehrere Eigenschaften aus, die sie besonders anfängerfreundlich machen:

**Lesbarkeit:** Python-Code sieht fast aus wie englische Sätze. Selbst ohne Programmierkenntnisse können Sie oft erahnen, was ein Programm macht.

**Einfache Syntax:** Im Vergleich zu anderen Programmiersprachen hat Python weniger "merkwürdige" Zeichen und Regeln. Sie können sich auf die Lösung von Problemen konzentrieren, statt sich mit komplizierter Syntax herumzuschlagen.

**Vielseitigkeit:** Mit Python können Sie fast alles machen - Webseiten erstellen, Daten analysieren, künstliche Intelligenz entwickeln, Spiele programmieren und vieles mehr.

**Große Community:** Millionen von Menschen nutzen Python. Das bedeutet: Zu fast jeder Frage finden Sie Hilfe online!

+++

### Python in der echten Welt

Python wird in vielen Bereichen eingesetzt:

- **Wissenschaft & Forschung:** Forscher nutzen Python, um komplexe Datenanalysen durchzuführen
- **Künstliche Intelligenz:** Die meisten modernen KI-Systeme basieren auf Python
- **Webentwicklung:** Plattformen wie Instagram und Spotify nutzen Python
- **Automatisierung:** Unternehmen automatisieren wiederkehrende Aufgaben mit Python
- **Spieleentwicklung:** Viele Indie-Spiele werden mit Python entwickelt

Das Wissen, das Sie in diesem Kurs erwerben, ist also nicht nur theoretisch - es ist hochrelevant für die Praxis!

+++

---

## 3. Wie funktioniert Python? ⚙️

### Der Python-Interpreter: Ihr persönlicher Übersetzer

Python ist eine **interpretierte Sprache**. Aber was bedeutet das genau?

Stellen Sie sich vor, Sie lesen ein Buch in einer fremden Sprache und haben einen Dolmetscher an Ihrer Seite. Der Dolmetscher übersetzt Satz für Satz - Sie hören einen Satz in Ihrer Sprache, dann den nächsten, und so weiter.

Genau so arbeitet der **Python-Interpreter**: Er nimmt Ihren Python-Code und übersetzt ihn Zeile für Zeile in Anweisungen, die der Computer verstehen und ausführen kann.

Der große Vorteil: Sie können Ihren Code sofort ausführen und testen. Sie müssen nicht warten, bis ein komplizierter Übersetzungsprozess abgeschlossen ist.

+++

### Interpreter vs. Compiler: Zwei verschiedene Ansätze

Es gibt zwei grundlegende Arten, wie Programme ausgeführt werden können:

**Interpretierte Sprachen (wie Python):**
- Der Code wird zur Laufzeit Zeile für Zeile übersetzt
- Sie können Code sofort ausführen und Änderungen schnell testen
- Ideal für Entwicklung und Lernen
- Beispiele: Python, JavaScript, Ruby

**Kompilierte Sprachen (wie C++ oder Java):**
- Der gesamte Code wird vorher in Maschinencode übersetzt ("kompiliert")
- Das Ergebnis ist eine ausführbare Datei
- Meistens schneller in der Ausführung
- Änderungen erfordern eine neue Kompilierung
- Beispiele: C, C++, Rust

Für das Lernen und für viele praktische Anwendungen ist die interpretierte Natur von Python ein großer Vorteil!

+++

---

## 4. Wo schreibt man Python-Code? 💻

### Die Werkzeuge eines Programmierers

Um Python-Programme zu schreiben, benötigen Sie eine **Entwicklungsumgebung**. Das ist im Grunde ein spezialisierter Texteditor, der Sie beim Programmieren unterstützt.

Es gibt verschiedene Möglichkeiten:

**Einfache Texteditoren:**
- Notepad (Windows), TextEdit (Mac), Nano (Linux)
- Funktionieren, aber bieten keine Unterstützung
- Nicht empfohlen für Anfänger

**Code-Editoren:**
- Visual Studio Code (sehr beliebt, kostenlos)
- Sublime Text
- Atom
- Bieten Syntax-Highlighting (Farbcodierung) und Auto-Vervollständigung

**IDEs (Integrated Development Environments):**
- PyCharm (speziell für Python)
- Spyder
- Komplette Entwicklungsumgebungen mit vielen Funktionen

**Jupyter Notebooks (das verwenden wir!):**
- Interaktive Umgebung für Python
- Kombination von Code, Text und Visualisierungen
- Ideal für Lernen und Datenanalyse
- Genau das, was Sie gerade sehen!

+++

### Warum Jupyter Notebooks?

In diesem Kurs verwenden wir **Jupyter Notebooks** - und das hat gute Gründe:

**Interaktivität:** Sie können Code-Schnipsel einzeln ausführen und sofort das Ergebnis sehen. Sie müssen nicht immer das gesamte Programm laufen lassen.

**Dokumentation:** Sie können Text, Code und Ergebnisse in einem Dokument kombinieren. Das macht es leicht, Ihre Gedanken und Erklärungen direkt neben dem Code zu notieren.

**Visualisierungen:** Grafiken und Diagramme werden direkt im Notebook angezeigt.

**Lernen:** Die schrittweise Ausführung macht es einfacher, den Code zu verstehen und mit verschiedenen Ansätzen zu experimentieren.

Jupyter Notebooks werden übrigens auch von professionellen Datenwissenschaftlern und Forschern weltweit verwendet!

+++

---

## 5. Was ist ein Algorithmus? 📋

### Schritt-für-Schritt-Anleitungen für den Computer

Bevor wir Code schreiben, müssen wir uns überlegen: **Wie** lösen wir eigentlich ein Problem? Die Antwort: mit einem **Algorithmus**.

Ein Algorithmus ist nichts anderes als eine präzise Schritt-für-Schritt-Anleitung zur Lösung eines Problems. Sie begegnen Algorithmen täglich, oft ohne es zu merken!

+++

### Algorithmen im Alltag

Betrachten wir ein einfaches Beispiel: **Eine Tasse Tee zubereiten**

1. Wasser in den Wasserkocher füllen
2. Wasserkocher einschalten
3. Warten, bis das Wasser kocht
4. Teebeutel in die Tasse legen
5. Heißes Wasser in die Tasse gießen
6. 3-5 Minuten ziehen lassen
7. Teebeutel entfernen
8. Nach Belieben Zucker oder Milch hinzufügen

Das ist ein Algorithmus! Eine klare Abfolge von Schritten, die zu einem gewünschten Ergebnis führen.

Weitere Alltagsalgorithmen:
- Ein IKEA-Möbelstück aufbauen (Anleitung)
- Ein Rezept kochen
- Den Weg zur Universität finden
- Eine Mathematikaufgabe lösen

+++

### Von der Idee zum Code

Beim Programmieren ist der Prozess ähnlich:

**Schritt 1 - Problem verstehen:**  
Was genau soll das Programm tun? Was ist die Eingabe, was die gewünschte Ausgabe?

**Schritt 2 - Algorithmus entwickeln:**  
Wie löse ich das Problem? Welche Schritte sind nötig? Oft hilft es, dies zuerst in normaler Sprache oder als Diagramm aufzuschreiben.

**Schritt 3 - In Code übersetzen:**  
Den Algorithmus in Python-Code umwandeln.

**Schritt 4 - Testen:**  
Funktioniert der Code? Liefert er die richtigen Ergebnisse?

**Schritt 5 - Optimieren:**  
Kann man es besser, schneller oder eleganter lösen?

Diese Denkweise - erst den Algorithmus planen, dann programmieren - werden Sie im Laufe des Kurses immer mehr verinnerlichen.

+++

---

## 6. Fehler gehören dazu: Bugs 🐛

### Was ist ein Bug?

Ein **Bug** ist ein Fehler in einem Programm, der dazu führt, dass sich das Programm nicht wie erwartet verhält. Es kann abstürzen, falsche Ergebnisse liefern oder sich merkwürdig verhalten.

Der Begriff "Bug" (englisch für "Käfer") hat eine interessante Geschichte: In den 1940er Jahren fand Grace Hopper, eine Pionierin der Informatik, eine echte Motte in einem Computer, die einen Fehler verursachte. Seitdem nennt man Programmfehler "Bugs"!

+++

### Fehler sind normal und wertvoll!

**Wichtige Botschaft:** Fehler zu machen ist nicht schlimm - es ist ein normaler und wichtiger Teil des Lernprozesses!

Selbst erfahrene Programmierer machen ständig Fehler. Der Unterschied ist: Sie haben gelernt, diese Fehler systematisch zu finden und zu beheben.

**Warum Fehler wertvoll sind:**
- Sie zeigen Ihnen, was noch nicht funktioniert
- Sie helfen Ihnen, das Konzept besser zu verstehen
- Sie trainieren Ihre Problemlösungsfähigkeiten
- Sie machen Sie zu einem besseren Programmierer

Die Fähigkeit, Fehler zu finden und zu beheben ("Debugging"), ist eine der wichtigsten Fähigkeiten in der Programmierung!

+++

### Arten von Fehlern

Es gibt verschiedene Kategorien von Bugs:

**Syntaxfehler:**
- Sie haben gegen die Grammatik-Regeln von Python verstoßen
- Beispiel: Ein Tippfehler, vergessene Klammer, falsches Zeichen
- Python zeigt diese Fehler sofort an
- Am einfachsten zu finden und zu beheben

**Laufzeitfehler:**
- Der Code ist syntaktisch korrekt, aber während der Ausführung geht etwas schief
- Beispiel: Division durch Null, Zugriff auf eine nicht existierende Datei
- Python bricht die Ausführung ab und zeigt eine Fehlermeldung

**Logische Fehler:**
- Der Code läuft durch, aber das Ergebnis ist falsch
- Beispiel: Sie wollten addieren, haben aber subtrahiert
- Am schwierigsten zu finden, weil Python keinen Fehler anzeigt
- Erfordert sorgfältiges Testen und Überprüfen

Im Laufe des Kurses werden Sie lernen, mit allen drei Fehlerarten umzugehen!

+++

---

## 7. Syntax und Semantik: Die DNA einer Programmiersprache 🧬

### Zwei grundlegende Konzepte

Jede Sprache - ob natürlich oder programmiert - basiert auf zwei fundamentalen Konzepten: **Syntax** und **Semantik**. Diese Begriffe werden Ihnen im Laufe Ihres Informatikstudiums immer wieder begegnen.

+++

### Syntax: Die Grammatik des Programmierens

Die **Syntax** einer Programmiersprache beschreibt die formalen Regeln, nach denen Sie Code schreiben müssen, damit Python (oder jede andere Sprache) ihn überhaupt verstehen kann.

**Ein Beispiel aus der deutschen Sprache:**
- ✅ Korrekt: "Ich gehe zum Supermarkt."
- ❌ Falsch: "Ich zum gehe Supermarkt."

Beides enthält die gleichen Wörter, aber nur der erste Satz folgt den deutschen Grammatikregeln.

**In Python:**
- ✅ Korrekt: `print("Hallo Welt")`
- ❌ Falsch: `print"Hallo Welt"`
- ❌ Falsch: `Print("Hallo Welt")`

Die Syntax legt fest:
- Welche Zeichen erlaubt sind
- Wie Befehle strukturiert sein müssen
- Wo Klammern, Anführungszeichen etc. stehen müssen
- Ob Groß-/Kleinschreibung relevant ist (in Python: ja!)

+++

### Semantik: Die Bedeutung verstehen

Die **Semantik** beschreibt die Bedeutung eines Programms - also das, was der Code tatsächlich bewirkt, wenn er ausgeführt wird.

**Ein Beispiel aus der deutschen Sprache:**
- "Der Hund beißt den Mann."
- "Der Mann beißt den Hund."

Beide Sätze sind syntaktisch korrekt, haben aber eine völlig unterschiedliche Bedeutung (Semantik)!

**In der Programmierung:**

Stellen Sie sich vor, wir wollen zwei Zahlen vertauschen:

```python
# Variante 1 - funktioniert NICHT wie gewünscht:
a = 5
b = 10
a = b  # a ist jetzt 10
b = a  # b ist auch 10 - der Wert 5 ist verloren!
```

```python
# Variante 2 - funktioniert:
a = 5
b = 10
temp = a  # Zwischenspeicher für den Wert 5
a = b     # a ist jetzt 10
b = temp  # b ist jetzt 5
```

+++

Beide Code-Abschnitte sind syntaktisch korrekt. Aber nur der zweite hat die richtige Semantik - nur er vertauscht die Werte tatsächlich wie gewünscht.

+++

### Warum sind Syntax und Semantik wichtig?

Das Verständnis dieser beiden Konzepte hilft Ihnen beim Programmieren:

**Syntaxfehler erkennen:**  
Wenn Python einen Syntaxfehler meldet, wissen Sie: "Ich habe gegen die Grammatik-Regeln verstoßen." Python kann Ihnen meist genau sagen, wo der Fehler ist.

**Logische Fehler vermeiden:**  
Wenn Ihr Code läuft, aber falsche Ergebnisse liefert, liegt ein semantisches Problem vor. Sie müssen überprüfen: "Macht mein Code wirklich das, was ich will?"

**Code verstehen:**  
Wenn Sie Code lesen, fragen Sie sich immer:
- Ist die Syntax korrekt? (Wird Python das verstehen?)
- Was ist die Semantik? (Was bewirkt dieser Code tatsächlich?)

Diese beiden Fragen werden Sie durch Ihre gesamte Programmierkarriere begleiten!

+++

---

## Zusammenfassung 🎓

### Was Sie gelernt haben:

✅ **Programmiersprachen** sind formale Sprachen, die die Kommunikation zwischen Mensch und Computer ermöglichen

✅ **Python** ist eine anfängerfreundliche, vielseitige und weit verbreitete Programmiersprache

✅ Python ist eine **interpretierte Sprache** - der Code wird zur Laufzeit Zeile für Zeile übersetzt und ausgeführt

✅ **Entwicklungsumgebungen** wie Jupyter Notebooks unterstützen Sie beim Schreiben von Code

✅ Ein **Algorithmus** ist eine präzise Schritt-für-Schritt-Anleitung zur Lösung eines Problems

✅ **Bugs** (Fehler) sind ein normaler Teil der Programmierung und helfen beim Lernen

✅ **Syntax** definiert die Regeln, wie Code geschrieben werden muss

✅ **Semantik** beschreibt die Bedeutung und Wirkung des Codes

+++

### Wichtige Konzepte:

| Konzept | Bedeutung | Beispiel |
|---------|-----------|----------|
| Programmiersprache | Formale Sprache für Computer-Anweisungen | Python, Java, C++ |
| Interpreter | Übersetzt Code zur Laufzeit | Python-Interpreter |
| Compiler | Übersetzt Code vorab in Maschinencode | C-Compiler |
| Algorithmus | Schritt-für-Schritt-Anleitung | Rezept, Wegbeschreibung |
| Syntax | Grammatik-Regeln der Sprache | `print("Text")` vs. `Print(Text)` |
| Semantik | Bedeutung des Codes | Was macht der Code? |
| Bug | Fehler im Programm | Syntaxfehler, Logikfehler |

### Der nächste Schritt

Im nächsten Notebook lernen Sie, wie Sie mit Python kommunizieren können - durch die **Konsole**. Sie werden Ihre ersten echten Python-Befehle schreiben und sehen, wie der Computer darauf reagiert!

+++

---

## Reflexionsfragen 🤔

Nehmen Sie sich einen Moment Zeit, um über das Gelernte nachzudenken:

### Verständnisfragen:

1. **Was ist der Unterschied zwischen Syntax und Semantik?**  
   Überlegen Sie sich ein eigenes Beispiel aus dem Alltag.

2. **Warum ist Python eine interpretierte Sprache?**  
   Was sind die Vor- und Nachteile gegenüber kompilierten Sprachen?

3. **Was ist ein Algorithmus?**  
   Beschreiben Sie einen Algorithmus für eine alltägliche Tätigkeit (z.B. Zähneputzen, Kaffee kochen).

4. **Warum sind Fehler (Bugs) beim Programmieren lernen eigentlich hilfreich?**

5. **Erklären Sie den Unterschied zwischen einem Interpreter und einem Compiler einem Freund, der noch nie programmiert hat.**

+++

### Transferfragen:

6. **Überlegen Sie sich drei Probleme aus Ihrem Alltag, die Sie mit einem Programm lösen könnten.**  
   Was sollte das Programm tun? Was wäre die Eingabe, was die Ausgabe?

7. **Python wird in vielen Bereichen eingesetzt (Wissenschaft, KI, Web, etc.). Welcher Bereich interessiert Sie persönlich am meisten und warum?**

---

### Notizen:

*Nutzen Sie diesen Bereich für Ihre eigenen Gedanken, Fragen und Ideen:*
