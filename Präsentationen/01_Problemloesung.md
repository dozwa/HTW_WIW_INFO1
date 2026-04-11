---
title: "Informatik 1: Problemlösung"
subtitle: "Wirtschaftsingenieurwesen Bachelor"
author: "HTW Berlin -- Wirtschaftsingenieurwesen"
date: "WiSe 2025-26"
header-includes:
  - \usepackage{etoolbox}
  - |
    \AtBeginEnvironment{longtable}{\footnotesize}
    \renewcommand{\arraystretch}{1.15}
---

# Agenda

1. Einsatz generativer KI Tools
2. EVA Prinzip
3. Daten-Informationen-Wissen
4. Problemlösungsprozess nach Haberfellner
5. Programmierprozess -- Haberfellner in der Praxis

---

# TL;DL -- Kurzfassung

- **Generative KI:** Nutzen Sie KI-Tools, um Verständnis zu vertiefen -- nicht um Lösungen zu generieren
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

# 1. Generative KI-Tools: Chancen

## Studie Dell'Acqua et al. (2023, Harvard Business School)

- 750 Berater im Beratungskontext untersucht
- **Bis zu 25% schneller** (Produktivitätssteigerung)
- **Bis zu 40% besser** (Qualitätssteigerung)
- Berater mit durchschnittlichen Leistungen profitieren besonders stark (43% vs 17%)

> GenKI kann Produktivität und Qualität steigern -- aber die Effekte hängen vom Einsatzkontext ab.

---

# 1. Generative KI-Tools: Forschung

## LLMs im Requirements Engineering (SIENA, Zwanzig/Dietrich 2023)

- GPT-3.5 und GPT-4 zur Extraktion von Nutzeranforderungen aus Interviews
- Fallstudie in der Physiotherapie
- Sensitivität: GPT-3.5 ca. 71%, GPT-4 ca. 73%
- Modelle konnten sogar neue, vorher unbekannte Anforderungen identifizieren

---

# 1. Generative KI-Tools: Effekte auf den Lernerfolg

## Ergebnisse aus 10 Studien

1. **Erklärende Nutzung** (z.B. Konzepte erklären lassen): positive Lerneffekte (+12,5 Punkte, +6,8% Examensanstieg)
2. **Lösungsorientierte Nutzung** (z.B. Codegenerierung): teilweise negative Effekte (signifikante negative Korrelation)
3. Effekte hängen von Promptqualität, Nutzungshäufigkeit und didaktischem Kontext ab

> Gezielter Einsatz als Erklärhilfe verbessert Lernleistungen. Übermäßige Nutzung zur direkten Problemlösung kann schaden.

---

# Aufgabe: KI im Studium

Diskutiert in der Gruppe oder mit ChatGPT/Gemini/Claude:

**Sollte man ChatGPT zum Lernen im Grundlagenmodul Informatik einsetzen?**

- Was spricht dafür?
- Was spricht dagegen?
- Gibt es ein sinnvolles "Wie?"

---

# 1. Generative KI-Tools: Regeln in diesem Kurs

- Verwenden Sie KI-Tools wie ChatGPT für Ihr Studium
- Kritische Auseinandersetzung mit Ergebnissen zwingend notwendig
- **Angabe** welche Tools, wo und wie eingesetzt wurden
- Nicht-Nennung = **Plagiat**

> **Die Lösung Ihrer Übungsaufgaben muss eigenständig erfolgen! GenKI-Einsatz zur Erstellung der Lösung ist unzulässig und wird als Plagiat gewertet.**

Geeignete Nutzung: "Erkläre mir Funktion A" oder "Warum bekomme ich diesen Fehler?"

---

# 1. Generative KI-Tools: Google Colab

## KI-Funktionen in Google Colab

- **Code generieren:** Prompt beschreibt die Aufgabe, KI erzeugt Code
- **Code korrigieren:** Automatische Fehlerbereinigung

## Empfehlung

- "Code generieren" nur in Ausnahmefällen nutzen (z.B. alternative Lösungen suchen)
- Generierte Ergebnisse mit großer Aufmerksamkeit prüfen

---

# 2. EVA-Prinzip: Computersystem

> **E**ingabe $\rightarrow$ **V**erarbeitung $\rightarrow$ **A**usgabe

| Komponente | Beispiele |
|------------|-----------|
| **Eingabe** | Tastatur, Maus, Touchpad, Scanner |
| **Verarbeitung** | CPU, Chipsatz, Controller |
| **Ausgabe** | Monitor, Lautsprecher, Drucker |
| **Speicher** | RAM, Festplatte, SSD, USB-Stick |

---

# 2. EVA-Prinzip: Programm/Prozess

> Input $\rightarrow$ Blackbox (Verarbeitung) $\rightarrow$ Output

## Beispiel: OEE-Berechnung

| Schritt | Inhalt |
|---------|--------|
| **Eingabe** | Rohdaten aus Produktionssimulation (Logdateien) |
| **Verarbeitung** | Berechnung in Excel/Python |
| **Ausgabe** | Verfügbarkeit 0,646 / Leistung 0,849 / Qualität 0,959 / OEE 52,6% |

---

# 3. Daten, Information, Wissen

## Drei Ebenen

| Ebene | Beschreibung | Beispiel |
|-------|-------------|----------|
| **Daten** (Syntaktik) | Zeichen + Syntax | 181 |
| **Information** (Semantik) | Daten + Bedeutung | 181 cm ist die Größe von Herrn Mustermann |
| **Wissen** (Pragmatik) | Information + Kontext | Durchschnittsgröße zur Parkbank-Konstruktion |

> Daten sind Rohwerte. Information entsteht durch Interpretation. Wissen entsteht durch Anwendung.

---

# 3. Daten vs. Information: ISO-Norm

## ISO IEC 2382-1 (1993)

**Daten:** Wieder interpretierbare Darstellung von Informationen in formalistischer Art, geeignet zur Kommunikation, Interpretation und Verarbeitung. Inhalt in Zeichen kodiert (Syntax).

**Information:** Aus Daten gewonnen durch Interpretation in einem Bedeutungszusammenhang (Semantik).

**Signal:** Physikalische Darstellung einer Information -- ein oder mehrere Parameter tragen Information über variable Größen.

---

# 3. Daten-Information-Wissen: Stufenmodell

## Aufsteigende Veredelung

- **1.20** $\rightarrow$ Daten (Rohwert)
- **Devisenkurs: 1 Euro = 1.20 Dollar** $\rightarrow$ Information (Kontext)
- **Auswirkungen auf Zinsen und Aktienkurse** $\rightarrow$ Wissen (Interpretation)

> **Information = Daten + Zweckbezug**
>
> **Wissen = Information + Interpretation/Klassifikation**

---

# 3. Wissenstreppe nach North

## Von Zeichen zur Wettbewerbsfähigkeit

Zeichen $\rightarrow$ (+Syntax) **Daten** $\rightarrow$ (+Bedeutung) **Informationen** $\rightarrow$ (+Vernetzung) **Wissen** $\rightarrow$ (+Anwendung) **Handeln** $\rightarrow$ (+richtig handeln) **Kompetenz** $\rightarrow$ (+Einzigartigkeit) **Wettbewerbsfähigkeit**

| Bereich | Umfang |
|---------|--------|
| Informationsmanagement | Zeichen bis Informationen |
| Wissensmanagement | Wissen bis Wettbewerbsfähigkeit |
| Explizites Wissen | Kodifizierbar, teilbar |
| Implizites Wissen | Erfahrung, schwer übertragbar |

---

# 4. Haberfellner: Überblick

## Problemlösungsprozess (Mikrologik)

- Basiert auf der Dewey'schen Problemlösungslogik (Hall 1962)
- Mikrologik, die in jeder (Projekt-)Phase angewendet werden kann

## Die vier Phasen

1. **Zielsuche:** Wo stehen wir? Was brauchen wir?
2. **Lösungssuche:** Welche Möglichkeiten gibt es?
3. **Auswahl:** Welche Lösung ist zweckmäßig?
4. **Ergebnis:** Lösung gefunden oder Prozess neu starten

---

# 4. Haberfellner: Zielsuche

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

# 4. Haberfellner: Lösungssuche

## Synthese von Lösungen

- Passende Lösungsmöglichkeiten finden (kreativer Schritt)
- Kreativitätstechniken: Brainstorming, Brainwriting, Mindmapping
- Beschreibung in passendem Detailierungsgrad

## Analyse von Lösungen

- Strukturierte Untersuchung (analytischer Schritt)
- Prüfung: Muss-Ziele erfüllt? Ressourcen vorhanden? Auswirkungen?

---

# 4. Haberfellner: Auswahl und Ergebnis

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

# 5. Programmierprozess: Warum?

## Häufige Anfängerfehler

- Sofort Code schreiben ohne nachzudenken
- Kein Plan, was das Programm eigentlich tun soll
- Keine Testfälle -- "läuft irgendwie" reicht nicht
- Bei Fehlern alles löschen und von vorne anfangen

> **Programmieren ist Problemlösen.** Haberfellner funktioniert auch hier -- wir müssen ihn nur übersetzen.

---

# 5. Programmierprozess: Überblick

## Von Haberfellner zum Code in 6 Schritten

| Haberfellner | Programmierschritt |
|--------------|--------------------|
| Anstoß | 1. Aufgabe verstehen |
| Zielsuche | 2. Beispiel von Hand lösen |
| Zielsuche | 3. Schritte aufschreiben |
| Lösungssuche | 4. Verallgemeinern |
| Lösungssuche | 5. In Code übersetzen |
| Auswahl/Ergebnis | 6. Testen und Debuggen |

---

# 5. Schritt 1: Aufgabe verstehen

## Haberfellner: Anstoß + Situationsanalyse

- Aufgabenstellung **vollständig lesen** (wirklich!)
- In **eigenen Worten** wiedergeben: Was soll das Programm tun?
- **EVA-Prinzip** anwenden:
  - Was ist die **Eingabe**? (Welche Daten bekommt das Programm?)
  - Was ist die **Ausgabe**? (Was soll am Ende rauskommen?)
  - Was passiert bei der **Verarbeitung**? (Welche Regeln/Berechnungen?)

> Wer die Aufgabe nicht erklären kann, kann sie auch nicht programmieren.

---

# 5. Schritt 2: Beispiel von Hand lösen

## Haberfellner: Zielsuche

- Ein **konkretes Beispiel** nehmen und **manuell** durchrechnen
- Mit echten Zahlen/Werten arbeiten, nicht abstrakt denken
- Das Ergebnis aufschreiben -- das ist euer Testfall!

## Beispiel: "Schreibe eine Funktion, die prüft ob eine Zahl gerade ist"

- Eingabe: 4 $\rightarrow$ Ergebnis: ja (4 / 2 = 2, kein Rest)
- Eingabe: 7 $\rightarrow$ Ergebnis: nein (7 / 2 = 3, Rest 1)
- Eingabe: 0 $\rightarrow$ Ergebnis: ja (0 / 2 = 0, kein Rest)

---

# 5. Schritt 3: Schritte aufschreiben

## Haberfellner: Zielformulierung

Frage: **Was habe ich gerade getan?** Jeden Schritt einzeln notieren.

## Pseudocode für das Beispiel

```
Nimm eine Zahl entgegen
Teile die Zahl durch 2
Wenn der Rest gleich 0 ist:
    Gib "gerade" zurück
Sonst:
    Gib "ungerade" zurück
```

- Noch kein Python -- nur menschliche Sprache!
- Alternativ: Ablaufdiagramm zeichnen (UML)

---

# 5. Schritt 4: Verallgemeinern

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

# 5. Schritt 5: In Code übersetzen

## Haberfellner: Lösungssuche $\rightarrow$ Umsetzung

Jetzt erst wird programmiert! Pseudocode Zeile für Zeile übersetzen:

```python
def ist_gerade(zahl):
    if zahl % 2 == 0:
        return "gerade"
    else:
        return "ungerade"
```

## Tipps

- **Eine Zeile Pseudocode = eine Zeile Code** (ungefähr)
- Wenn eine Zeile nicht übersetzbar ist $\rightarrow$ Pseudocode verfeinern
- Nicht alles auf einmal -- Funktion für Funktion

---

# 5. Schritt 6: Testen und Debuggen

## Haberfellner: Auswahl + Ergebnis

Die Testfälle aus Schritt 2 verwenden:

```python
print(ist_gerade(4))   # erwartet: "gerade"
print(ist_gerade(7))   # erwartet: "ungerade"
print(ist_gerade(0))   # erwartet: "gerade"
```

## Bei Fehlern: Systematisch debuggen

1. **Fehlermeldung lesen** -- Was sagt Python?
2. **Eingabe prüfen** -- Stimmen die Testdaten?
3. **Tracing wiederholen** -- Schritt für Schritt durchgehen
4. **Nicht alles löschen!** -- Fehler isolieren und beheben

---

# 5. Der Prozess im Überblick

> **Erst denken, dann tippen.** Die meiste Arbeit passiert *vor* dem Code.

1. **Verstehen** -- Aufgabe lesen, EVA identifizieren
2. **Beispiel** -- Konkreten Fall von Hand lösen
3. **Aufschreiben** -- Schritte als Pseudocode notieren
4. **Verallgemeinern** -- Variablen einsetzen, auf Papier testen
5. **Coden** -- Pseudocode in Python übersetzen
6. **Testen** -- Testfälle durchlaufen, debuggen

Inspiriert von Polya (1945) und dem "Seven Steps"-Ansatz (Duke University, Hilton et al.)

---

# 5. Häufige Fehler und Tipps

| Fehler | Besser |
|--------|--------|
| Sofort Code schreiben | Erst Pseudocode, dann Code |
| "Läuft irgendwie" | Mit Testfällen aus Schritt 2 prüfen |
| Alles in eine Funktion | Teilprobleme einzeln lösen |
| Bei Fehler alles löschen | Fehlermeldung lesen, Fehler isolieren |
| Nur einen Fall testen | Normalfall, Grenzfall, Fehlerfall testen |
| Code kopieren ohne Verständnis | Erst von Hand lösen, dann programmieren |

---

# Zusammenfassung

- **GenKI:** Als Erklärhilfe nutzen, nicht als Lösungsgenerator. Nutzung angeben!
- **EVA:** Eingabe $\rightarrow$ Verarbeitung $\rightarrow$ Ausgabe -- Grundmuster aller Informationssysteme
- **Daten $\rightarrow$ Information $\rightarrow$ Wissen:** Veredelung durch Kontext und Interpretation
- **Haberfellner:** Zielsuche $\rightarrow$ Lösungssuche $\rightarrow$ Auswahl $\rightarrow$ Ergebnis
- **Programmierprozess:** Verstehen $\rightarrow$ Beispiel $\rightarrow$ Pseudocode $\rightarrow$ Verallgemeinern $\rightarrow$ Code $\rightarrow$ Testen
