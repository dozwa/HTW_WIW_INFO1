---
title: "20 — Datenbanksysteme"
subtitle: "Wozu Datenbanken? DBMS, Datenbankarten, Excel vs. DB"
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
    \newenvironment{demobox}
      {\begin{tcolorbox}[colback=blue!8, colframe=blue!55, left=4pt, right=4pt, top=2pt, bottom=2pt, arc=0pt, fontupper=\small]}
      {\end{tcolorbox}}
    \newenvironment{exercisebox}
      {\begin{tcolorbox}[colback=orange!8, colframe=orange!70!black, left=4pt, right=4pt, top=2pt, bottom=2pt, arc=0pt, fontupper=\small]}
      {\end{tcolorbox}}
---

# Agenda

1. Wozu Datenbanken? -- Daten vs. Dateichaos
2. Datenbank $\neq$ DBMS
3. Wo Datenbanken überall stecken
4. Die vier wichtigsten Datenbankarten
5. Welcher Typ passt zu welchem Problem?
6. Excel stößt an Grenzen -- warum eine echte Datenbank?

> **Lernziel**: Verstehen, *was* eine Datenbank ist, *welche Arten* es gibt und *wann* sie einer Tabellenkalkulation überlegen ist.

> **Hinweis**: Dieses Kapitel ist rein konzeptuell -- noch kein Code. Praktisch wird es ab Notebook 22. Die Aufgaben im Notebook sind **Denkaufgaben**.

---

# Wozu Datenbanken? -- Das Dateichaos

## Veggie Soles als Ordner voller Textdateien

```
bestellung_2026-05-03_anna.txt
bestellung_2026-05-03_max.txt
bestellung_2026-05-04_anna_v2_final.txt
kunden.xlsx        produkte.xlsx        lager_alt.xlsx
```

- Wie viel hat Anna Müller insgesamt bestellt? → alle Dateien öffnen
- Steht der Preis des Eco-Sneaker in `produkte.xlsx` *und* in jeder Bestellung? → Redundanz, Widersprüche
- Zwei Mitarbeitende ändern `kunden.xlsx` gleichzeitig? → eine Version gewinnt

> Eine **Datenbank** speichert Daten *strukturiert* und beantwortet solche Fragen in Millisekunden -- auch bei Millionen Einträgen.

---

# Datenbank $\neq$ Datenbankmanagementsystem

| | Was ist das? | Analogie Bibliothek |
|---|---|---|
| **Datenbank** | die gespeicherten Daten selbst | die Bücher im Regal |
| **DBMS** | die Software, die sie verwaltet | Katalog + Bibliothekar:in |

Das DBMS kümmert sich um das, was die Daten allein nicht können:

- mehrere Nutzer:innen **gleichzeitig** bedienen
- Daten **konsistent** und korrekt halten (Regeln erzwingen)
- **Zugriffsrechte** durchsetzen
- bei Absturz **nichts verlieren** (Backups, Logs)

> Beispiel: *MySQL* ist das DBMS, *„alle Bestellungen von Veggie Soles"* ist die Datenbank.

---

# Datenbanken stecken überall

| System | Wofür | Beispiel |
|---|---|---|
| **WWS** -- Warenwirtschaft | Lagerbestand in Echtzeit | Kasse scannt → Bestand sinkt → Nachbestellung |
| **ERP** -- Enterprise Resource Planning | alle Abteilungen, eine Datenbasis | Buchhaltung, Personal, Produktion |
| **CMS** -- Content Management | Webinhalte dynamisch ausliefern | Wikipedia, Nachrichtenportale |
| **CRM** -- Customer Relationship Mgmt | jeder Kundenkontakt nachvollziehbar | Mails, Anrufe, Bestellhistorie |

> Wer online einkauft, streamt oder Bankgeschäfte macht, nutzt -- meist unbemerkt -- ständig Datenbanken.

---

# Die vier wichtigsten Datenbankarten

![](20_datenbankarten_uebersicht.png){width=68%}

> Es gibt nicht *die eine* Datenbank -- der Typ folgt dem Anwendungsfall.

---

# Welcher Typ passt zu welchem Problem?

| Anforderung | passender Typ |
|---|---|
| feste Struktur + ACID (Bank, Shop, ERP) | **relational** (SQL) |
| schnelle Lookups, Sessions, Caching | **Key-Value** |
| flexible Datensätze (Produktkataloge) | **Dokument** |
| Beziehungen analysieren (soziale Netze) | **Graph** |

- oft **Kombinationen**: PostgreSQL für Bestellungen *plus* Redis für Live-Tracking
- Veggie Soles → **relationale** Datenbank (klare Struktur -- genau die ab jetzt)

::: exercisebox
**✎ Selbst überlegen** -- Notebook 20, Übung 2.1: vier Szenarien dem passenden Datenbanktyp zuordnen.
:::

---

# Excel stößt an Grenzen

![](20_excel_vs_datenbank.png){width=64%}

- **Multi-User**: Excel sperrt die Datei -- ein DBMS bedient hunderte gleichzeitig
- **Integrität**: Excel prüft nichts -- ein DBMS erzwingt Regeln (eindeutige IDs, Typen)
- **Größe**: Excel ab ~100.000 Zeilen zäh -- DBMS skaliert auf Millionen

---

# Excel vs. Datenbank -- der direkte Vergleich

| Kriterium | Excel | Datenbank |
|---|---|---|
| Multi-User | problematisch | Kernfunktion |
| Datenmenge | < 1 Mio. Zeilen | praktisch unbegrenzt |
| Geschwindigkeit | langsam bei großen Daten | für große Mengen optimiert |
| Datenintegrität | manuell | automatisch erzwungen |
| Backup | manuell | automatisierbar |
| Zugriffskontrolle | ganze Datei | granular (Tabelle, Zeile) |
| Komplexe Abfragen | begrenzt | SQL sehr mächtig |
| Lernkurve | flach | steiler |

> Für 50 Kontakte reicht Excel. Für ein Krankenhaus, einen Online-Marktplatz oder Veggie Soles im Wachstum: Datenbank.

---

# Cheat Card -- Notebook 20

| Begriff | Kurz |
|---|---|
| Datenbank | strukturierte Sammlung von Daten |
| DBMS | Software, die die Datenbank verwaltet |
| relationale DB | Daten in verknüpften Tabellen, SQL, ACID |
| NoSQL | Sammelbegriff: Key-Value, Dokument, Graph |
| Transaktion | mehrere Operationen als unteilbare Einheit (Details: NB 21) |
| WWS / ERP / CMS / CRM | typische Einsatzfelder von Datenbanken |

> **Faustregel**: Der Datenbanktyp folgt dem Anwendungsfall -- nicht der Gewohnheit.

---

# Ausblick: Notebook 21 -- Relationale Datenbanken

Das wichtigste Modell, im Detail:

- **Tabellen** mit Zeilen (Datensätzen) und Spalten (Attributen)
- **Primärschlüssel** -- jede Zeile eindeutig
- **Fremdschlüssel** -- Tabellen verbinden
- **Beziehungstypen** 1:1, 1:n, n:m
- **SQL-Datentypen** und **ACID** (Transaktionssicherheit)

Und gleich danach (Notebook 21b): eine ausführliche Einführung ins **ER-Diagramm** -- wie man ein Datenmodell *zeichnet*, bevor man es baut.

---

# Heute (durch)gedacht

✓ Datenbank von DBMS unterschieden  
✓ Einsatzfelder benannt (WWS, ERP, CMS, CRM)  
✓ Die vier Datenbankarten und ihre Stärken  
✓ Datenbanktyp einem Szenario zuordnen  
✓ Erklärt, wo Excel an Grenzen stößt  

::: exercisebox
**✎ Zur Vertiefung im Notebook 20:**

- Übungen 1.1, 2.1, 3.1 -- kleine Denkaufgaben mit Musterlösung
- Abschlussübungen Aufg. 1--4: vom DBMS-Begriff bis zum Migrations- und Architekturentscheid
:::
