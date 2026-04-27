---
title: "Informatik 1: KI-Tools in der Programmierung"
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
      {\begin{tcolorbox}[colback=gray!10, colframe=gray!50, left=4pt, right=4pt, top=2pt, bottom=2pt, arc=0pt, fontupper=\small]}
      {\end{tcolorbox}}
---

# Agenda

1. Generative KI und Lernen
2. Richtig Prompten im Informatikkontext
3. KI-Tools beim Programmieren
4. Typische KI-Fehler und warum sie entstehen
5. Strategien zur Fehlerreduktion

---

# TL;DL -- Kurzfassung

- **KI und Lernen:** Erklärhilfe nutzen, nicht Lösungsgenerator
- **Richtig Prompten:** Sokratisch fragen statt Lösungen liefern lassen
- **KI-Tools:** Copilot, Gemini, Claude Code, ChatGPT kennen
- **KI-Fehler:** 62% unsicherer Code -- KI-Output nie automatisch korrekt
- **Fehlerreduktion:** Reviewen, testen, iterativ prompten

---

# 1. Generative KI-Tools: Chancen

## Studie Dell'Acqua et al. (2023, Harvard Business School)

- 750 Berater im Beratungskontext untersucht
- **Bis zu 25% schneller** (Produktivitätssteigerung)
- **Bis zu 40% besser** (Qualitätssteigerung)
- Durchschnittliche Berater profitieren besonders (43% vs 17%)

---

# 1. Generative KI-Tools: Verbreitung

## Stack Overflow Developer Survey 2025

- **84%** der Entwickler nutzen oder planen KI-Tools (2024: 76%)
- **51%** nutzen KI-Tools täglich
- Aber: Nur **29%** vertrauen der Genauigkeit von KI-Output (2024: 40%)

> Hohe Nutzung, geringes Vertrauen -- ein Widerspruch, der zum Nachdenken anregen sollte.

---

# 1. Generative KI-Tools: Forschung

## LLMs im Requirements Engineering (SIENA, Zwanzig/Dietrich 2023)

- GPT-3.5 und GPT-4 zur Extraktion von Nutzeranforderungen
- Fallstudie in der Physiotherapie
- Sensitivität: GPT-3.5 ca. 71%, GPT-4 ca. 73%
- Modelle identifizierten sogar neue, vorher unbekannte Anforderungen

---

# 1. Effekte auf den Lernerfolg: Ergebnisse

## Ergebnisse aus 10 Studien

1. **Erklärende Nutzung** (Konzepte erklären lassen): positive Lerneffekte (+12,5 Punkte, +6,8% Examensanstieg)
2. **Lösungsorientierte Nutzung** (Codegenerierung): teilweise negative Effekte
3. Effekte hängen von Promptqualität und didaktischem Kontext ab

> **Gezielter** Einsatz wirkt -- **häufigerer** Einsatz nicht (El Fathi et al. 2025, n=120).

---

# 1. Effekte auf den Lernerfolg: Positiv

## Meta-Analyse Alanazi et al. (2025)

- 35 kontrollierte Studien ausgewertet
- Signifikante Leistungsverbesserung (SMD = 0,86)
- Schnellere Aufgabenbearbeitung (SMD = -0,69)

> **Leistungsstarke Lernende** hinterfragen KI-Ergebnisse aktiv -- **schwächere** akzeptieren sie passiv.

---

# 1. Effekte auf den Lernerfolg: Warnungen

## Langfristige Risiken

**Li et al. (2025):** GenKI verbessert kurzfristige Ergebnisse, **beeinträchtigt aber den langfristigen Wissenstransfer**. "Kognitives Outsourcing" verhindert effektives Lernen.

**Yang et al. (2025):** Studie mit 153 Schülern -- ChatGPT-Nutzung führte zu **niedrigerem** Selbstwirksamkeitsempfinden und **schlechteren** Lernergebnissen.

---

# Aufgabe: KI im Studium

Diskutiert in der Gruppe oder mit ChatGPT/Gemini/Claude:

**Sollte man ChatGPT zum Lernen im Grundlagenmodul Informatik einsetzen?**

- Was spricht dafür?
- Was spricht dagegen?
- Gibt es ein sinnvolles "Wie?"

---

# 2. Richtig Prompten: Sokratisches Fragen

## Prinzip: KI soll Fragen stellen, nicht Antworten geben

Statt KI die Lösung generieren zu lassen, nutzt man KI als **Tutor**, der durch gezielte Fragen zum Verständnis führt.

- **SocraticAI (Sunil et al. 2025):** >75% der Studierenden produzierten substantielle Reflexionen
- **Sakshm AI (Gupta et al. 2025):** Positiver Einfluss auf Problemlöseverhalten (1.170 Teilnehmer)

---

# 2. Reverse Prompting (Chang et al. 2023)

## Drei Designprinzipien für KI als Lernwerkzeug

1. **Prompting als Goal-Setting:** Effektive Prompts formulieren lernen fördert metakognitive Planung
2. **Reverse Prompting:** KI so nutzen, dass sie **Rückfragen stellt** statt direkte Antworten zu geben
3. **Reflexion:** Eigenes Lernverhalten anhand der KI-Interaktionen reflektieren

> Reverse Prompting ist die Methode hinter dem Sokratischen Fragen -- mit 198 Zitierungen eine der meistzitierten Arbeiten im Feld.

---

# 2. Richtig Prompten: Strategien für Informatik

## Schlechte vs. gute Prompts

| Schlecht | Besser |
|------------|--------------------------------------------------------------|
| "Schreib mir Bubble Sort" | "Erkläre mir Schritt für Schritt, wie Bubble Sort funktioniert" |
| "Löse Aufgabe 3" | "Meine Schleife läuft endlos. Stell mir Fragen dazu" |
| "Korrigiere meinen Code" | "Mein Code gibt Fehler Y. Erkläre mir den Fehler" |

---

# 2. Richtig Prompten: Prompt-Templates (1/2)

**1. Konzept erklären lassen:**

"Erkläre mir [Konzept] mit einem Alltagsbeispiel. Frage mich danach, ob ich es verstanden habe."

**2. Fehler verstehen:**

"Mein Code gibt folgenden Fehler: [Fehler]. Erkläre mir, was der Fehler bedeutet, aber zeig mir nicht die Lösung."

---

# 2. Richtig Prompten: Prompt-Templates (2/2)

**3. Code reviewen lassen:**

"Reviewe meinen Code und sag mir, was ich verbessern kann und warum. Hier ist mein Code: [Code]"

**4. Sich selbst testen:**

"Stelle mir 5 Verständnisfragen zu [Thema] mit steigender Schwierigkeit. Warte auf meine Antworten und gib Feedback."

---

# 2. Richtig Prompten: Dos

## Geeignete Nutzung

- "Erkläre mir, was eine for-Schleife macht"
- "Warum bekomme ich einen IndexError?"
- "Stell mir Fragen zu meinem Verständnis von Listen"
- "Reviewe meinen Code und sag mir, was ich verbessern kann"

> **Faustregel:** Wenn Sie den KI-Output nicht Zeile für Zeile erklären können, haben Sie nichts gelernt.

---

# 2. Richtig Prompten: Don'ts

## Ungeeignete Nutzung

- "Schreib mir die Lösung für Übungsaufgabe 4"
- Code kopieren ohne ihn zu verstehen
- KI-Output blind in die Abgabe übernehmen
- "Mach meinen Code besser" ohne eigenes Verständnis

> **59%** der Entwickler nutzen KI-Code, den sie nicht vollständig verstehen (Clutch.co).

---

# 2. Überabhängigkeit vermeiden

## Übermäßige KI-Nutzung schränkt Problemlösefähigkeit ein

- Wer immer KI fragt, hört auf, **selbst** nach Lösungen zu suchen (Parsakia 2023)
- Positive Effekte bei **gezielter** Nutzung, negative bei Ersatzfunktion
- **Erosion kritischen Denkens** ist das meistgenannte Risiko in der gesamten Literatur (Schei et al. 2024; Vargas-Murillo 2023)

> Ziel: KI als Werkzeug beherrschen -- nicht von ihr beherrscht werden.

---

# 3. KI-Tools: Überblick

| Tool | Typ | Integration | Kostenlos? |
|---------------------|-------------------|----------------------|------------|
| **GitHub Copilot** | Code-Completion | VS Code, JetBrains | Free-Tier |
| **Gemini** | Assistent | Google Colab | Ja |
| **Claude Code** | Terminal-Agent | CLI, VS Code | Free-Tier |
| **ChatGPT** | Chat + Sandbox | Browser, App | Free-Tier |
| **Cursor** | AI-Editor | Eigener Editor | Free-Tier |

Alle Tools basieren auf LLMs -- sie **generieren** plausiblen Code, sie **verstehen** ihn nicht.

---

# 3. GitHub Copilot in VS Code

- **Inline-Vorschläge:** Code-Completion beim Tippen
- **Copilot Chat:** Fragen zur Codebasis in der IDE
- **Agent Mode:** Plant, schreibt, testet und korrigiert Code
- **Next Edit Suggestions:** Schlägt den nächsten Edit vor
- Genutzt von **77.000+** Organisationen weltweit
- Free-Tier verfügbar

---

# 3. Gemini in Google Colab: Features

- **Code-Completion:** Schlägt Code-Segmente beim Tippen vor
- **Code-Generierung:** Code aus natürlichsprachlichen Beschreibungen
- **Learn Mode (NEU):** Persönlicher Coding-Tutor -- gibt **Anleitung statt Code**
- **Data Science Agent:** Erstellt Notebooks automatisch

---

# 3. Gemini in Google Colab: Empfehlung

## Empfehlung für diesen Kurs

- **Learn Mode aktiv nutzen** -- ideal für Übungen
- "Code generieren" nur in Ausnahmefällen
- Generierte Ergebnisse **immer** kritisch prüfen

> Der Learn Mode ist das beste Werkzeug für Anfänger -- er erklärt, statt die Arbeit abzunehmen.

---

# 3. Claude Code (Anthropic)

- **Terminal-Tool:** Arbeitet direkt in der Kommandozeile
- **Codebase-Verständnis:** Liest und versteht ganze Projekte
- **Multi-File-Refactoring:** Bearbeitet mehrere Dateien gleichzeitig
- **Subagents:** Delegiert Teilaufgaben parallel

Quelle: [anthropic.com/product/claude-code](https://www.anthropic.com/product/claude-code)

---

# 3. ChatGPT (OpenAI)

- **Code Interpreter:** Sandboxed Python-Umgebung
- **Datenanalyse:** CSV-Upload, Bereinigung, Visualisierung
- **Canvas-Mode:** Code-Editing neben dem Chat
- **Multi-Round Fixing:** Debuggt den eigenen Code iterativ

---

# 3. Empfehlung: Welches Tool wofür?

| Zweck | Empfohlenes Tool |
|-------------------------------|----------------------------------------------|
| Übungen im Notebook | Google Colab + **Gemini Learn Mode** |
| Konzepte verstehen | ChatGPT, Claude, Gemini |
| Fehler verstehen | ChatGPT, Claude |
| Code-Completion in der IDE | GitHub Copilot (**erst ab Semester 2+**) |

---

# 3. Empfehlung: Grundsätze

- Copilot-artige Tools **erst nutzen, wenn Grundlagen sitzen**
- KI als **Sparringspartner**, nicht als **Ghostwriter**
- Nutzung in Übungsabgaben: **immer angeben!**

> Erst die Konzepte verstehen, dann KI als Werkzeug einsetzen.

---

# Generative KI-Tools: Regeln in diesem Kurs

- Verwenden Sie KI-Tools wie ChatGPT für Ihr Studium
- Kritische Auseinandersetzung mit Ergebnissen zwingend notwendig
- **Angabe** welche Tools, wo und wie eingesetzt wurden
- Nicht-Nennung = **Plagiat**

> **Die Lösung Ihrer Übungsaufgaben muss eigenständig erfolgen! GenKI-Einsatz zur Erstellung der Lösung ist unzulässig und wird als Plagiat gewertet.**

---

# 4. Typische KI-Fehler: Die Zahlen

- **62%** der KI-generierten C-Programme haben Sicherheitslücken (Tihanyi et al. 2024)
- **~40%** des Copilot-Codes enthält Bugs oder Schwachstellen (NYU 2021)
- **59%** der Entwickler nutzen KI-Code, den sie nicht verstehen (Clutch.co)
- Nur **29%** vertrauen der Genauigkeit von KI-Output (Stack Overflow 2025)

---

# 4. Typische KI-Fehler: Vier Kategorien

1. **Halluzinationen** -- nicht-existente APIs, erfundene Funktionen
2. **Falsche Logik** -- Code sieht plausibel aus, ist aber falsch
3. **Sicherheitslücken** -- unsichere Patterns, fehlende Validierung
4. **Veraltetes Wissen** -- deprecated APIs, alte Library-Versionen

> KI kann nur **29,2%** der eigenen Bugs nach zwei Iterationen beheben (Dou et al. 2024).

---

# 4. Halluzinationen

## KI erfindet Dinge, die nicht existieren

- **Nicht-existente APIs** und Funktionssignaturen (CodeMirage, Agarwal et al. 2024)
- 10 dokumentierte Bug-Muster: Misinterpretation, Hallucinated Object, Missing Corner Case u.a. (Tambon et al. 2024)

---

# 4. Falsche Logik

## Code sieht korrekt aus, ist es aber nicht

- Code, der auf den ersten Blick plausibel aussieht, aber bei Edge Cases versagt
- **EvalPlus** (Liu et al. 2023): Bei erweiterten Tests (80x mehr) sinkt die Pass-Rate um **19--29%**
- Standard-Tests erkennen die Fehler **nicht**
- Modelle sind schlecht darin, **eigene** Fehler zu erkennen

---

# 4. Sicherheitslücken

- **62%** der KI-generierten Programme sind verwundbar (Tihanyi et al. 2024, 331.000 Programme)
- **29,5%** der Copilot Python-Snippets haben Sicherheitsschwächen (Fu et al. 2023)
- **Kein Zusammenhang** zwischen "Code funktioniert" und "Code ist sicher" (Sabra et al. 2025)
- Hardcoded Passwords, Path Traversal, fehlende Input-Validierung

---

# 4. Veraltetes Wissen

- **48% bessere** Ergebnisse für Probleme **vor** dem Training-Cutoff (Liu et al. 2023)
- Veraltete Library-Versionen, deprecated Funktionen
- KI hat keinen Zugriff auf aktuelle Dokumentation

> Wenn eine Library ein Update bekommt, weiß die KI davon erst nach dem nächsten Training.

---

# 4. Warum passieren diese Fehler?

| Eigenschaft | Compiler | LLM |
|----------------------|--------------------------------------|--------------------------------------|
| Arbeitsweise | Regelbasiert, deterministisch | Statistisch, probabilistisch |
| Korrektheit | Garantiert | Nie garantiert |
| Trainingsgrundlage | Sprachspezifikation | Internet-Code (inkl. Fehler) |
| Optimierungsziel | Korrekte Ausführung | Plausibel klingende Antwort |

---

# 4. Warum passieren diese Fehler? (2)

- LLMs generieren das **wahrscheinlichste nächste Token** -- nicht die **korrekte** Antwort
- Trainiert auf öffentlichem Code: Stack Overflow, GitHub -- inkl. Bugs und unsicherem Code
- Kein echtes "Verständnis" von Programmlogik oder Sicherheitskonzepten

---

# 5. Fehlerreduktion: Checkliste

## KI-Code immer reviewen -- niemals blind übernehmen

1. **Funktionalität:** Macht der Code was er soll?
2. **Edge Cases:** Leere Eingabe, Null, negative Zahlen?
3. **Sicherheit:** Keine Hardcoded Secrets, keine Injections?
4. **Lesbarkeit:** Jeden Ausdruck verstehen? Wenn nein $\rightarrow$ nachfragen

---

# 5. Fehlerreduktion: Recursive Criticism

## KI den eigenen Code nochmal reviewen lassen

"Prüfe diesen Code auf Fehler, Sicherheitslücken und Edge Cases."

- Kann Schwachstellen **um eine Größenordnung** reduzieren (OpenSSF)
- Funktioniert besser als einmaliges Generieren

Quelle: [OpenSSF Security Guide](https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions.html)

---

# 5. Fehlerreduktion: Testen

## Testfälle VOR dem KI-Einsatz definieren

- Wie im **Programmierprozess Schritt 2**: Erst von Hand lösen, dann Testfälle ableiten
- KI-Code gegen **eigene** Testfälle prüfen
- **TiCoder** (Fakhoury et al. 2024): +45,97% Korrektheit durch testgetriebene Interaktion

---

# 5. Fehlerreduktion: Verification Paradox

## KI-Tests für KI-Code haben blinde Flecken

- Wenn KI Code **und** Tests generiert, können beide den **gleichen** Fehler haben
- **89%** der Sicherheitslücken behebbar bei gezieltem Feedback (Liu et al. 2023)

> Tests müssen **eigene** Logik widerspiegeln, nicht KI-Logik.

---

# 5. Fehlerreduktion: Iteratives Prompting

## Nicht alles auf einmal -- schrittweise verfeinern

1. **Kontext geben:** Sprache, Framework, Constraints
2. **Klein anfangen:** Erst eine Funktion, nicht das ganze Programm
3. **Fehler zurückspielen:** "Dieser Code gibt Fehler X. Warum?"
4. **Verfeinern:** "Berücksichtige auch den Fall Y."
5. **Prüfen:** Jeden Schritt testen

---

# 5. Fehlerreduktion: Chain-of-Thought

## Im Prompt die gewünschte Denkstruktur vorgeben

"Denke Schritt für Schritt: Was ist die Eingabe? Was die Ausgabe? Welche Schritte liegen dazwischen?"

- Structured Chain-of-Thought verbessert die Code-Qualität
- Quelle: [IBM -- Iterative Prompting](https://www.ibm.com/think/topics/iterative-prompting)

---

# 5. Wann NICHT KI einsetzen

**METR RCT (2025):** Erfahrene Entwickler waren mit KI **+19% langsamer** -- obwohl sie glaubten, schneller zu sein.

## KI vermeiden bei:

- **Grundlagen lernen:** Erst selbst verstehen
- **Prüfungen und Übungsabgaben:** Eigenständige Leistung
- **Sicherheitskritischem Code:** Immer menschliche Prüfung
- **Wenn man den Output nicht versteht**

---

# 5. Das größte Risiko: Erosion kritischen Denkens

## Studierende und Akademiker benennen dasselbe Problem

- **Verlust eigenständiger Problemlösefähigkeit** -- meistgenanntes Risiko über alle Studien hinweg (Schei et al. 2024, 58 Zit.)
- Studierende, die KI **passiv** nutzen, entwickeln keine eigene Denkstruktur
- **Kognitives Outsourcing** verhindert nachhaltiges Lernen (Li et al. 2025)

> Wer nie selbst debuggt hat, wird auch mit KI kein guter Programmierer.

---

# Zusammenfassung

- **KI und Lernen:** Erklärhilfe $\rightarrow$ positiv, Lösungsgenerator $\rightarrow$ negativ
- **Richtig Prompten:** Sokratisch fragen, nicht Lösungen liefern lassen
- **Tools kennen:** Jedes Tool hat seinen Einsatzbereich
- **KI-Fehler:** 62% unsicherer Code, Halluzinationen, falsche Logik
- **Fehler reduzieren:** Reviewen, testen, iterativ prompten
- **Grundlagen zuerst:** Erst Konzepte verstehen, dann KI nutzen

---

# Quellen: Studien (1/2)

- Dell'Acqua et al. (2023): "Navigating the Jagged Frontier" -- HBS Working Paper 24-013
- Sunil et al. (2025): "SocraticAI" -- [arxiv.org/abs/2512.03501](https://arxiv.org/abs/2512.03501)
- Gupta et al. (2025): "Sakshm AI" -- [arxiv.org/html/2503.12479](https://arxiv.org/html/2503.12479)
- Alanazi et al. (2025): Meta-Analyse KI-gestütztes CS-Lernen
- Li et al. (2025): GenKI und langfristiger Wissenstransfer
- Chang et al. (2023): SRL-Designprinzipien, Reverse Prompting (198 Zit.)

---

# Quellen: Studien (2/2)

- Tihanyi et al. (2024): 331.000 KI-generierte Programme
- Fu et al. (2023): Copilot Security Weaknesses
- Tambon et al. (2024): 10 Bug-Patterns in LLM-Code
- Liu et al. (2023): EvalPlus -- HumanEval+
- Fakhoury et al. (2024): TiCoder
- METR (2025): [metr.org RCT Study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
- El Fathi et al. (2025): CILP Framework, gezielter KI-Einsatz
- Schei et al. (2024): Scoping Review KI-Chatbots (58 Zit.)
- Parsakia (2023): Chatbots und Selbstwirksamkeit

---

# Quellen: Surveys, Tools und Guides

- Stack Overflow 2025: [survey.stackoverflow.co/2025/ai/](https://survey.stackoverflow.co/2025/ai/)
- GitHub Copilot: [code.visualstudio.com/docs/copilot](https://code.visualstudio.com/docs/copilot/overview)
- Gemini in Colab: [Google Colab AI Features](https://blog.google/technology/developers/google-colab-ai-coding-features/)
- Claude Code: [anthropic.com/product/claude-code](https://www.anthropic.com/product/claude-code)
- OpenSSF: [best.openssf.org](https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions.html)
- Prompt Guide: [promptingguide.ai](https://www.promptingguide.ai/)
