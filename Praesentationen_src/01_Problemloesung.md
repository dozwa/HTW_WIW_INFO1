---
title: "Informatik 1: Problemlösung"
subtitle: "Wirtschaftsingenieurwesen Bachelor"
author: "HTW Berlin -- Wirtschaftsingenieurwesen"
date: "SoSe 2026"
header-includes:
  - \usepackage{etoolbox}
  - \usepackage{tcolorbox}
  - |
    \AtBeginEnvironment{longtable}{\footnotesize}
    \renewcommand{\arraystretch}{1.15}
    \renewenvironment{quote}
      {\begin{tcolorbox}[colback=gray!10, colframe=gray!50, left=4pt, right=4pt, top=2pt, bottom=2pt, arc=0pt]}
      {\end{tcolorbox}}
---

# Agenda

1. EVA Prinzip
2. Daten-Informationen-Wissen
3. Problemlösungsprozess nach Haberfellner
4. Programmierprozess -- Haberfellner in der Praxis

---

# TL;DL -- Kurzfassung

- **Daten-Informationen-Wissen:** Daten sind Werte, Informationen sind Daten mit Kontext, Wissen ist Informationen mit Interpretation
- **EVA-Prinzip:** Eingabe, Verarbeitung, Ausgabe -- das Grundmuster jedes Informationssystems
- **Haberfellner:** Strukturierter Problemlösungsprozess -- auch direkt beim Programmieren anwendbar

---

# Glossar (1/2)

- **Data Mining:** Auffinden von Mustern und Anomalien in großen Datenmengen mittels Statistik, ML und KI
- **Data Science:** Interdisziplinäres Feld -- wissenschaftliche Methoden zur Wissensgewinnung aus Daten
- **Feature:** Messbares Merkmal, das als Eingabevariable in ein Modell eingespeist wird

---

# Glossar (2/2)

- **Methode:** Definierter, systematischer Prozess zur Aufgabenlösung. In der Programmierung: Funktion eines Objekts/einer Klasse
- **Modell:** Vereinfachte Darstellung der Realität zur Vorhersage oder Analyse
- **Vorgehensmodell:** Strukturierter Rahmen, der den Prozess der Softwareentwicklung oder des Projektmanagements leitet

---

# 1. EVA-Prinzip: Computersystem

> **E**ingabe $\rightarrow$ **V**erarbeitung $\rightarrow$ **A**usgabe

| Komponente | Beispiele |
|------------|-------------------------------|
| **Eingabe** | Tastatur, Maus, Touchpad, Scanner |
| **Verarbeitung** | CPU, Chipsatz, Controller |
| **Ausgabe** | Monitor, Lautsprecher, Drucker |
| **Speicher** | RAM, Festplatte, SSD, USB-Stick |

---

# 1. EVA-Prinzip: Programm/Prozess

> Input $\rightarrow$ Blackbox (Verarbeitung) $\rightarrow$ Output

## Beispiel: OEE-Berechnung

| Schritt | Inhalt |
|---------|----------------------------------------------|
| **Eingabe** | Rohdaten aus Produktionssimulation (Logdateien) |
| **Verarbeitung** | Berechnung in Excel/Python |
| **Ausgabe** | Verfügbarkeit 0,646 / Leistung 0,849 / Qualität 0,959 / OEE 52,6% |

---

# 2. Daten, Information, Wissen

## Drei Ebenen

| Ebene | Beschreibung | Beispiel |
|-|-|--|
| **Daten** (Syntaktik) | Zeichen + Syntax | 181 |
| **Information** (Semantik) | Daten + Bedeutung | 181 cm ist die Größe von Herrn Mustermann |
| **Wissen** (Pragmatik) | Information + Kontext | Durchschnittsgröße zur Parkbank-Konstruktion |

Daten sind Rohwerte. Information entsteht durch Interpretation. Wissen entsteht durch Anwendung.

---

# 2. Daten vs. Information: ISO-Norm

## ISO IEC 2382-1 (1993)

**Daten:** Wieder interpretierbare Darstellung von Informationen in formalistischer Art, geeignet zur Kommunikation, Interpretation und Verarbeitung. Inhalt in Zeichen kodiert (Syntax).

**Information:** Aus Daten gewonnen durch Interpretation in einem Bedeutungszusammenhang (Semantik).

**Signal:** Physikalische Darstellung einer Information -- ein oder mehrere Parameter tragen Information über variable Größen.

---

# 2. Daten-Information-Wissen: Stufenmodell

## Aufsteigende Veredelung

- **1.20** $\rightarrow$ Daten (Rohwert)
- **Devisenkurs: 1 Euro = 1.20 Dollar** $\rightarrow$ Information (Kontext)
- **Auswirkungen auf Zinsen und Aktienkurse** $\rightarrow$ Wissen (Interpretation)

> **Information = Daten + Zweckbezug**
>
> **Wissen = Information + Interpretation/Klassifikation**

---

# 2. Wissenstreppe nach North

## Von Zeichen zur Wettbewerbsfähigkeit

Zeichen $\rightarrow$ (+Syntax) **Daten** $\rightarrow$ (+Bedeutung) **Informationen** $\rightarrow$ (+Vernetzung) **Wissen** $\rightarrow$ (+Anwendung) **Handeln** $\rightarrow$ (+richtig handeln) **Kompetenz** $\rightarrow$ (+Einzigartigkeit) **Wettbewerbsfähigkeit**

| Bereich | Umfang |
|---------------|-------------------------------|
| Informationsmanagement | Zeichen bis Informationen |
| Wissensmanagement | Wissen bis Wettbewerbsfähigkeit |
| Explizites Wissen | Kodifizierbar, teilbar |
| Implizites Wissen | Erfahrung, schwer übertragbar |

---

# 3. Haberfellner: Überblick

## Problemlösungsprozess (Mikrologik)

- Basiert auf der Dewey'schen Problemlösungslogik (Hall 1962)
- Mikrologik, die in jeder (Projekt-)Phase angewendet werden kann

## Die vier Phasen

1. **Zielsuche:** Wo stehen wir? Was brauchen wir?
2. **Lösungssuche:** Welche Möglichkeiten gibt es?
3. **Auswahl:** Welche Lösung ist zweckmäßig?
4. **Ergebnis:** Lösung gefunden oder Prozess neu starten

---

# 3. Haberfellner: Zielsuche

## Situationsanalyse

- Problem wird ergründet und verstanden
- Nachfragen stellen
- Fundiertes Problemverständnis ist zwingend notwendig
- Klare Unterscheidung: Fakten vs. Interpretation

## Zielformulierung

- Ziele: lösungsneutral, vollständig, verständlich, realistisch
- Priorisierung: Muss (zwingend) vs. Kann (wünschenswert)
- Detailgrad abhängig von Komplexität

---

# 3. Haberfellner: Lösungssuche

## Synthese von Lösungen

- Passende Lösungsmöglichkeiten finden (kreativer Schritt)
- Kreativitätstechniken: Brainstorming, Brainwriting, Mindmapping
- Beschreibung in passendem Detailierungsgrad

## Analyse von Lösungen

- Strukturierte Untersuchung (analytischer Schritt)
- Prüfung: Muss-Ziele erfüllt? Ressourcen vorhanden? Auswirkungen?

---

# 3. Haberfellner: Auswahl und Ergebnis

## Bewertung

- Lösungsansätze systematisch gegenüberstellen
- Achtung: Präferierte Lösung kann zu suboptimaler Auswahl führen
- Methoden: Nutzwertanalyse, Kosten-Nutzen-Rechnung
- Gruppenbewertung reduziert Subjektivität

## Entscheidung und Ergebnis

- Lösung wird festgelegt auf Basis der Bewertung
- Keine zufriedenstellende Lösung? $\rightarrow$ Prozess neu starten, Ziele anpassen oder abbrechen

---

# Aufgabe: Haberfellner anwenden

**Ausgangssituation:** Die BVG hat zum Semesterstart intensive Bauarbeiten an den Straßenbahnverbindungen zur HTW begonnen.

**Problem:** Montagmorgen, 8:00 Uhr -- wichtige Klausur, die ihr bestehen müsst.

**Aufgabe:** Erarbeitet in Kleingruppen (2-4 Personen) eine Lösung. Haltet euch an den Problemlösungsprozess nach Haberfellner.

---

# 4. Programmierprozess: Warum?

## Häufige Anfängerfehler

- Sofort Code schreiben ohne nachzudenken
- Kein Plan, was das Programm eigentlich tun soll
- Keine Testfälle -- "läuft irgendwie" reicht nicht
- Bei Fehlern alles löschen und von vorne anfangen

**Programmieren ist Problemlösen.** Haberfellner funktioniert auch hier -- wir müssen ihn nur übersetzen.

---

# 4. Programmierprozess: Überblick

## Von Haberfellner zum Code in 6 Schritten

![Programmierprozess](Grafiken/01_problemloesung_programmierprozess.png){width=95%}

---

# 4. Schritt 1: Aufgabe verstehen

## Haberfellner: Anstoß + Situationsanalyse

- Aufgabenstellung **vollständig lesen** (wirklich!)
- In **eigenen Worten** wiedergeben: Was soll das Programm tun?
- **EVA-Prinzip** anwenden:
  - Was ist die **Eingabe**? (Welche Daten bekommt das Programm?)
  - Was ist die **Ausgabe**? (Was soll am Ende rauskommen?)
  - Was passiert bei der **Verarbeitung**? (Welche Regeln/Berechnungen?)

Wer die Aufgabe nicht erklären kann, kann sie auch nicht programmieren.

---

# 4. Schritt 2: Beispiel von Hand lösen

## Haberfellner: Zielsuche

- Ein **konkretes Beispiel** nehmen und **manuell** durchrechnen
- Mit echten Zahlen/Werten arbeiten, nicht abstrakt denken
- Das Ergebnis aufschreiben -- das ist euer Testfall!

## Beispiel: "Schreibe eine Funktion, die prüft ob eine Zahl gerade ist"

- Eingabe: 4 $\rightarrow$ Ergebnis: ja (4 / 2 = 2, kein Rest)
- Eingabe: 7 $\rightarrow$ Ergebnis: nein (7 / 2 = 3, Rest 1)
- Eingabe: 0 $\rightarrow$ Ergebnis: ja (0 / 2 = 0, kein Rest)

---

# 4. Schritt 3: Schritte aufschreiben

## Haberfellner: Zielformulierung

Frage: **Was habe ich gerade getan?** Jeden Schritt einzeln notieren.

- Noch kein Python -- nur menschliche Sprache!
- Alternativ: Ablaufdiagramm zeichnen (UML)

---

# 4. Schritt 3: Pseudocode-Beispiel

```
Nimm eine Zahl entgegen
Teile die Zahl durch 2
Wenn der Rest gleich 0 ist:
    Gib "gerade" zurück
Sonst:
    Gib "ungerade" zurück
```

Pseudocode beschreibt die Logik -- die Programmiersprache kommt später.

---

# 4. Schritt 4: Verallgemeinern

## Haberfellner: Synthese von Lösungen

- Konkrete Zahlen durch **Variablen/Parameter** ersetzen
- Prüfen: Funktioniert der Pseudocode auch mit **anderen Eingaben**?
- Algorithmus **auf dem Papier testen** (Tracing):

## Tracing mit verschiedenen Eingaben

| zahl | zahl % 2 | Rest == 0? | Ergebnis |
|------|----------|-----------|----------|
| 4 | 0 | ja | "gerade" |
| 7 | 1 | nein | "ungerade" |
| 0 | 0 | ja | "gerade" |
| -3 | -1 | nein | "ungerade" |

---

# 4. Schritt 5: In Code übersetzen

## Haberfellner: Lösungssuche $\rightarrow$ Umsetzung

Jetzt erst wird programmiert! Pseudocode Zeile für Zeile übersetzen:

```python
def ist_gerade(zahl):
    if zahl % 2 == 0:
        return "gerade"
    else:
        return "ungerade"
```

---

# 4. Schritt 5: Tipps zur Übersetzung

**Eine Zeile Pseudocode = eine Zeile Code** (ungefähr). Wenn eine Zeile nicht übersetzbar ist $\rightarrow$ Pseudocode verfeinern.

**Nicht alles auf einmal** -- Funktion für Funktion entwickeln und testen.

Erst Pseudocode schreiben, dann übersetzen. Nie direkt drauflos programmieren.

---

# 4. Schritt 6: Testen

## Haberfellner: Auswahl + Ergebnis

**Testfälle aus Schritt 2 verwenden** und Ergebnisse mit Erwartungen abgleichen:

```python
print(ist_gerade(4))   # erwartet: "gerade"
print(ist_gerade(7))   # erwartet: "ungerade"
print(ist_gerade(0))   # erwartet: "gerade"
```

**Stimmt das Ergebnis nicht?** $\rightarrow$ Systematisch debuggen (siehe nächste Folie)

---

# 4. Schritt 6: Debuggen

## Bei Fehlern: Systematisch vorgehen

1. **Fehlermeldung lesen** -- Was sagt Python?
2. **Eingabe prüfen** -- Stimmen die Testdaten?
3. **Tracing wiederholen** -- Schritt für Schritt durchgehen
4. **Nicht alles löschen!** -- Fehler isolieren und beheben

---

# 4. Der Prozess im Überblick

**Erst denken, dann tippen.** Die meiste Arbeit passiert *vor* dem Code.

1. **Verstehen** -- Aufgabe lesen, EVA identifizieren
2. **Beispiel** -- Konkreten Fall von Hand lösen
3. **Aufschreiben** -- Schritte als Pseudocode notieren
4. **Verallgemeinern** -- Variablen einsetzen, auf Papier testen
5. **Coden** -- Pseudocode in Python übersetzen
6. **Testen** -- Testfälle durchlaufen, debuggen

Inspiriert von Polya (1945) und dem "Seven Steps"-Ansatz (Duke University, Hilton et al.)

---

# 4. Häufige Fehler und Tipps

| Fehler | Besser |
|---------------------|---------------------------------------------|
| Sofort Code schreiben | Erst Pseudocode, dann Code |
| "Läuft irgendwie" | Mit Testfällen aus Schritt 2 prüfen |
| Alles in eine Funktion | Teilprobleme einzeln lösen |
| Bei Fehler alles löschen | Fehlermeldung lesen, Fehler isolieren |
| Nur einen Fall testen | Normalfall, Grenzfall, Fehlerfall testen |
| Code kopieren ohne Verständnis | Erst von Hand lösen, dann programmieren |

---

# Zusammenfassung

- **EVA:** Eingabe $\rightarrow$ Verarbeitung $\rightarrow$ Ausgabe -- Grundmuster aller Informationssysteme
- **Daten $\rightarrow$ Information $\rightarrow$ Wissen:** Veredelung durch Kontext und Interpretation
- **Haberfellner:** Zielsuche $\rightarrow$ Lösungssuche $\rightarrow$ Auswahl $\rightarrow$ Ergebnis
- **Programmierprozess:** Verstehen $\rightarrow$ Beispiel $\rightarrow$ Pseudocode $\rightarrow$ Verallgemeinern $\rightarrow$ Code $\rightarrow$ Testen
