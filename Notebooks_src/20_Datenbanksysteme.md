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

# 20 - Datenbanksysteme: Grundlagen und Konzepte

## Lernziele

Nach Abschluss dieses Notebooks können Sie:
- Den Unterschied zwischen einer Datenbank und einem Datenbankmanagementsystem erklären
- Verschiedene Arten von Datenbanken kategorisieren und ihre Einsatzgebiete benennen
- Die Vorteile von Datenbanken gegenüber einfachen Tabellenkalkulationen bewerten
- Grundlegende Datenbankkonzepte wie Transaktionen und ACID-Prinzipien verstehen

**Kompetenzstufen**: Verstehen, Analysieren

---

## Voraussetzungen

Für dieses Notebook sollten Sie folgende Konzepte beherrschen:
- Grundlegendes Verständnis von Datenstrukturen (Notebook 06)
- Dateiverwaltung und -speicherung (Notebook 12)

Dieses Notebook ist **rein konzeptuell** und enthält keine Programmierbeispiele. Die praktische Umsetzung folgt in den Notebooks 22 und 23.

---

+++

## Kapitel 1: Wozu dienen Datenbanken?

### Einführung und Motivation

In unserer digitalen Welt werden täglich unvorstellbare Mengen an Daten erzeugt, gespeichert und verarbeitet. Ob Sie online einkaufen, soziale Medien nutzen oder Ihre Bankgeschäfte erledigen – überall arbeiten im Hintergrund Datenbanken. Aber was genau sind Datenbanken und warum sind sie so wichtig?

Eine **Datenbank** ist im Kern eine strukturierte Sammlung von Daten, die elektronisch gespeichert und verwaltet wird. Stellen Sie sich eine Bibliothek vor: Die Bücher selbst sind wie die Daten, während das Ordnungssystem (Katalog, Regale, Signaturen) dem Datenbankmanagementsystem entspricht. Gemeinsam ermöglichen sie es, Informationen effizient zu speichern, zu finden und zu nutzen.

Der entscheidende Unterschied zu einer einfachen Dateisammlung auf Ihrer Festplatte liegt in der **Struktur und Verwaltung**. Während Sie in einem Ordner mit tausenden Textdateien mühsam nach einer bestimmten Information suchen müssten, ermöglicht eine Datenbank den gezielten und schnellen Zugriff auf genau die Daten, die Sie benötigen – selbst bei Millionen von Einträgen.

+++

### Was ist eine Datenbank?

Eine Datenbank besteht aus zwei wesentlichen Komponenten:

1. **Die Daten selbst**: Die eigentlichen Informationen, die gespeichert werden sollen
2. **Das Datenbankmanagementsystem (DBMS)**: Die Software, die diese Daten verwaltet

Das DBMS ist dabei wie ein intelligenter Bibliothekar, der nicht nur weiß, wo jedes Buch steht, sondern auch sicherstellt, dass:
- Mehrere Personen gleichzeitig auf die Daten zugreifen können
- Die Daten konsistent und korrekt bleiben
- Nur berechtigte Personen bestimmte Daten sehen oder ändern dürfen
- Die Daten auch bei Systemausfällen nicht verloren gehen

Diese Trennung zwischen Daten und Verwaltungssystem ist fundamental. Sie ermöglicht es, dass verschiedene Programme und Benutzer gleichzeitig mit denselben Daten arbeiten können, ohne sich gegenseitig zu stören.

+++

### Einsatzbereiche von Datenbanken

Datenbanken sind heute allgegenwärtig und bilden das Rückgrat der digitalen Wirtschaft. Lassen Sie uns einige konkrete Einsatzbereiche betrachten:

**Warenwirtschaftssysteme (WWS)**
In jedem Supermarkt wird beim Scannen eines Produkts an der Kasse automatisch der Lagerbestand in einer Datenbank aktualisiert. Das System weiß dadurch in Echtzeit, welche Produkte nachbestellt werden müssen und kann automatisch Bestellungen auslösen.

**Enterprise Resource Planning (ERP)**
Große Unternehmen nutzen ERP-Systeme, die alle Geschäftsprozesse in einer zentralen Datenbank vereinen. Von der Personalabteilung über die Buchhaltung bis zur Produktion – alle Abteilungen greifen auf dieselben, konsistenten Daten zu.

**Content Management Systeme (CMS)**
Websites wie Wikipedia oder Nachrichtenportale speichern ihre Inhalte in Datenbanken. Dadurch können Artikel dynamisch zusammengestellt, durchsucht und von mehreren Autoren gleichzeitig bearbeitet werden.

**Customer Relationship Management (CRM)**
Unternehmen verwalten ihre Kundenbeziehungen über CRM-Systeme. Jeder Kontakt, jede E-Mail und jeder Anruf wird in der Datenbank gespeichert, sodass jeder Mitarbeiter sofort den kompletten Verlauf einer Kundenbeziehung einsehen kann.

+++

### TLDR - Die wichtigsten Punkte

- **Datenbanken** sind Systeme zur elektronischen Datenverwaltung, bestehend aus Datenbankmanagementsystem (DBMS) und Daten
- **Einsatzbereiche** umfassen Wirtschaft, Wissenschaft, Banken, Versicherungen, E-Commerce und soziale Netzwerke
- **Vorteile** gegenüber einfachen Dateisystemen: Strukturierte Speicherung, Multi-User-Fähigkeit, Datensicherheit
- **DBMS** organisiert die Speicherung und kontrolliert alle Zugriffe auf die Daten

+++

### Übung 1.1: Datenbanken im Alltag

**Aufgabe**: Identifizieren Sie drei Situationen aus Ihrem Alltag, in denen Sie (direkt oder indirekt) mit Datenbanken interagieren. Beschreiben Sie für jede Situation:

1. Welche Art von Daten wird gespeichert?
2. Warum ist hier eine Datenbank sinnvoll?
3. Was wäre die Alternative ohne Datenbank?

**Beispielantwort**:

<details>
<summary>Lösung anzeigen</summary>

**Situation 1: Online-Banking**
- Gespeicherte Daten: Kontostände, Transaktionen, Überweisungen, Kundendaten
- Warum Datenbank: Millionen von Transaktionen müssen sicher, konsistent und schnell verarbeitet werden
- Alternative: Papierbasierte Kontoführung wäre langsam, fehleranfällig und unpraktisch

**Situation 2: Streaming-Dienst (Netflix, Spotify)**
- Gespeicherte Daten: Nutzerprofile, Wiedergabeverlauf, Empfehlungen, Medienkatalog
- Warum Datenbank: Personalisierte Empfehlungen basierend auf Nutzerverhalten, schneller Zugriff auf Millionen von Titeln
- Alternative: Physische Mediathek würde keine Personalisierung und keinen sofortigen Zugriff ermöglichen

**Situation 3: Online-Shop**
- Gespeicherte Daten: Produktkatalog, Lagerbestände, Kundenbestellungen, Bewertungen
- Warum Datenbank: Echtzeit-Lagerverwaltung, Bestellhistorie, automatische Nachbestellungen
- Alternative: Papierkataloge mit telefonischer Bestellung wären ineffizient und fehleranfällig
</details>

+++

---

## Kapitel 2: Arten von Datenbanken

### Einführung in die Datenbanklandschaft

Nicht alle Daten sind gleich strukturiert, und nicht alle Anwendungsfälle haben dieselben Anforderungen. Daher haben sich im Laufe der Zeit verschiedene Arten von Datenbanken entwickelt, die jeweils für spezifische Szenarien optimiert sind. Diese Vielfalt ist vergleichbar mit verschiedenen Transportmitteln: Ein Fahrrad eignet sich für kurze Strecken in der Stadt, während für Langstrecken ein Flugzeug die bessere Wahl ist.

Die Wahl der richtigen Datenbankart kann entscheidend für die Performance und Skalierbarkeit einer Anwendung sein. Ein soziales Netzwerk hat andere Anforderungen als ein Bankensystem, und ein wissenschaftliches Datenarchiv funktioniert anders als ein Online-Shop. Verstehen wir die verschiedenen Datenbanktypen, können wir fundierte Entscheidungen für unsere Projekte treffen.

In diesem Kapitel lernen Sie die wichtigsten Datenbankarten kennen und verstehen, wann welcher Typ sinnvoll eingesetzt wird.

+++

### Relationale Datenbanken

**Relationale Datenbanken** sind der klassische und am weitesten verbreitete Datenbanktyp. Sie organisieren Daten in Tabellen (ähnlich wie Excel), wobei jede Tabelle aus Zeilen und Spalten besteht. Die "Relation" bezieht sich auf die Beziehungen zwischen verschiedenen Tabellen.

**Charakteristika:**
- Strukturierte Daten in Tabellenform
- Feste Schemata (jede Zeile hat dieselben Spalten)
- SQL als standardisierte Abfragesprache
- ACID-Eigenschaften für Transaktionssicherheit

**Beispiele:** MySQL, PostgreSQL, Oracle, Microsoft SQL Server

**Einsatzgebiete:** 
- Bankensysteme (Transaktionssicherheit ist kritisch)
- ERP-Systeme (komplexe Geschäftsdaten)
- E-Commerce (Bestellungen, Kunden, Produkte)

**Vorteile:** Bewährte Technologie, standardisiert, konsistent
**Nachteile:** Weniger flexibel bei unstrukturierten Daten

+++

### NoSQL-Datenbanken

Der Begriff **NoSQL** steht für "Not Only SQL" und umfasst verschiedene nicht-relationale Datenbanktypen. Diese wurden entwickelt, um Limitierungen relationaler Datenbanken zu überwinden, besonders bei sehr großen Datenmengen oder flexiblen Datenstrukturen.

#### Key-Value-Datenbanken

**Funktionsweise:** Wie ein riesiges Python-Dictionary - jeder Schlüssel ist mit genau einem Wert verknüpft.

**Beispiel:** Redis, Amazon DynamoDB
**Einsatz:** Session-Speicher, Caching, Echtzeit-Empfehlungen
**Stärke:** Extrem schnell bei einfachen Abfragen

#### Dokumentenorientierte Datenbanken

**Funktionsweise:** Speichern Daten als Dokumente (meist JSON), die unterschiedliche Strukturen haben können.

**Beispiel:** MongoDB, CouchDB
**Einsatz:** Content Management, Produktkataloge, Blog-Systeme
**Stärke:** Flexibilität bei sich ändernden Datenstrukturen

#### Graph-Datenbanken

**Funktionsweise:** Modellieren Daten als Netzwerk von Knoten und Verbindungen.

**Beispiel:** Neo4j, Amazon Neptune
**Einsatz:** Soziale Netzwerke, Empfehlungssysteme, Wissensgraphen
**Stärke:** Effizient bei der Analyse von Beziehungen

+++

### Übung 2.1: Datenbanktyp-Zuordnung

**Aufgabe**: Ordnen Sie jedem der folgenden Szenarien den am besten geeigneten Datenbanktyp zu und begründen Sie Ihre Wahl:

1. Ein soziales Netzwerk möchte Freundschaftsbeziehungen und Empfehlungen analysieren
2. Eine Bank verwaltet Konten und Transaktionen
3. Ein Online-Shop speichert Produktinformationen, die sich häufig ändern
4. Eine Gaming-Plattform speichert Spieler-Sessions und Highscores

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

1. **Graph-Datenbank (z.B. Neo4j)**
   - Begründung: Freundschaftsbeziehungen bilden ein Netzwerk, Graph-DBs sind optimal für Beziehungsanalysen

2. **Relationale Datenbank (z.B. PostgreSQL)**
   - Begründung: Transaktionssicherheit (ACID) ist kritisch, strukturierte Daten, bewährte Technologie für Finanzen

3. **Dokumentenorientierte Datenbank (z.B. MongoDB)**
   - Begründung: Flexible Produktstrukturen, unterschiedliche Attribute je nach Produkttyp möglich

4. **Key-Value-Datenbank (z.B. Redis)**
   - Begründung: Schneller Zugriff auf Session-Daten, einfache Struktur (Spieler-ID → Score), Caching-Fähigkeiten
</details>

+++

---

## Kapitel 3: Datenbank vs. Excel-Tabelle

### Die Grenzen von Tabellenkalkulationen

Viele Menschen nutzen Excel oder andere Tabellenkalkulationsprogramme als ersten Ansatz zur Datenverwaltung. Das ist verständlich: Excel ist vertraut, visuell und für kleine Datenmengen durchaus praktisch. Doch ab einem gewissen Punkt stoßen Tabellenkalkulationen an ihre Grenzen.

Stellen Sie sich vor, Sie verwalten die Kundendaten eines wachsenden Unternehmens in Excel. Anfangs funktioniert das gut – Sie haben eine überschaubare Anzahl von Kunden, und eine Person kümmert sich um die Datenpflege. Doch was passiert, wenn das Unternehmen wächst? Wenn plötzlich mehrere Mitarbeiter gleichzeitig Daten ändern müssen? Wenn Sie aus Versehen eine Formel überschreiben? Wenn die Datei so groß wird, dass Excel beim Öffnen abstürzt?

Diese Szenarien sind keine Seltenheit und zeigen, warum professionelle Datenverwaltung mehr erfordert als eine Tabellenkalkulation. Datenbanken wurden genau für diese Herausforderungen entwickelt.

+++

### Multi-User-Fähigkeit und Netzwerktauglichkeit

**Problem bei Excel:**
Wenn zwei Personen gleichzeitig dieselbe Excel-Datei bearbeiten wollen, entstehen Konflikte. Entweder wird die Datei für andere Nutzer gesperrt, oder es entstehen verschiedene Versionen, die manuell zusammengeführt werden müssen.

**Lösung durch Datenbanken:**
Datenbankmanagementsysteme sind von Grund auf für gleichzeitige Zugriffe konzipiert. Sie verwenden ausgeklügelte Mechanismen wie:
- **Transaktionsmanagement**: Änderungen werden atomar durchgeführt
- **Locking-Mechanismen**: Nur die betroffenen Datensätze werden kurzzeitig gesperrt
- **Versionsverwaltung**: Konflikte werden automatisch erkannt und aufgelöst

In einer Datenbank können hunderte Nutzer gleichzeitig arbeiten, ohne sich gegenseitig zu behindern.

+++

### Datenintegrität und Konsistenz

**Problem bei Excel:**
In Excel gibt es keine automatische Überprüfung von Datenbeziehungen. Sie können versehentlich:
- Inkonsistente Daten eingeben (z.B. verschiedene Schreibweisen desselben Namens)
- Wichtige Verknüpfungen zerstören
- Duplikate erzeugen

**Lösung durch Datenbanken:**
Datenbanken erzwingen Datenintegrität durch:
- **Primärschlüssel**: Jeder Datensatz ist eindeutig identifizierbar
- **Fremdschlüssel**: Beziehungen zwischen Tabellen werden überwacht
- **Constraints**: Regeln verhindern ungültige Daten
- **Datentypen**: Jede Spalte akzeptiert nur Daten des richtigen Typs

+++

### Performance und Skalierbarkeit

**Excel-Limitierungen:**
- Maximal 1.048.576 Zeilen pro Arbeitsblatt
- Performance-Probleme ab einigen zehntausend Zeilen
- Gesamte Datei muss in den Arbeitsspeicher geladen werden

**Datenbank-Stärken:**
- Millionen oder Milliarden von Datensätzen möglich
- Indizierung ermöglicht blitzschnelle Suchen
- Nur benötigte Daten werden geladen
- Verteilung auf mehrere Server möglich

+++

### Vergleichstabelle: Excel vs. Datenbank

| Kriterium | Excel | Datenbank |
|-----------|-------|----------|
| **Multi-User** | ❌ Problematisch | ✅ Kernfunktion |
| **Datenmenge** | < 1 Million Zeilen | Praktisch unbegrenzt |
| **Geschwindigkeit** | Langsam bei großen Daten | Optimiert für große Mengen |
| **Datenintegrität** | Manuell | Automatisch erzwungen |
| **Backup** | Manuell | Automatisiert möglich |
| **Zugriffskontrolle** | Dateiebene | Granular (Tabellen, Zeilen) |
| **Komplexe Abfragen** | Begrenzt | SQL sehr mächtig |
| **Kosten** | Niedrig | Höher (aber skalierbar) |
| **Lernkurve** | Flach | Steiler |

+++

### Übung 3.1: Entscheidungsfindung Excel vs. Datenbank

**Aufgabe**: Entscheiden Sie für folgende Szenarien, ob Excel oder eine Datenbank die bessere Wahl wäre. Begründen Sie Ihre Entscheidung.

1. Ein Freelancer verwaltet seine 50 Kundenkontakte
2. Ein Krankenhaus verwaltet Patientendaten
3. Eine Privatperson führt ein Haushaltsbuch
4. Ein Online-Marktplatz verwaltet Millionen von Produktangeboten

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

1. **Excel ist ausreichend**
   - Kleine Datenmenge (50 Kontakte)
   - Einzelnutzer
   - Einfache Struktur
   - Keine kritischen Anforderungen

2. **Datenbank ist zwingend**
   - Sensible Daten (Datenschutz)
   - Multi-User (Ärzte, Pfleger, Verwaltung)
   - Kritische Datenintegrität
   - Gesetzliche Aufbewahrungspflichten
   - Große Datenmengen

3. **Excel ist geeignet**
   - Überschaubare Datenmenge
   - Einzelnutzer
   - Einfache Berechnungen
   - Keine kritischen Anforderungen

4. **Datenbank ist notwendig**
   - Millionen von Datensätzen
   - Multi-User (Verkäufer, Käufer, Admin)
   - Echtzeit-Updates erforderlich
   - Komplexe Suchanfragen
   - Transaktionssicherheit wichtig
</details>

+++

---

## Abschlussübungen

Die folgenden Aufgaben testen Ihr Verständnis der in diesem Notebook erlernten Konzepte. Bearbeiten Sie die Aufgaben selbstständig und vergleichen Sie Ihre Lösung anschließend mit den Musterlösungen am Ende des Notebooks.

### Teil 1: Grundlegende Anwendung

**Kompetenzstufe**: Verstehen

Diese Aufgaben testen Ihr Verständnis der grundlegenden Datenbankkonzepte.

+++

**Aufgabe 1**: Erklären Sie den Unterschied zwischen einer Datenbank und einem Datenbankmanagementsystem in eigenen Worten. Geben Sie ein konkretes Beispiel.

+++

**Aufgabe 2**: Ein Start-up möchte eine App für Essenslieferungen entwickeln. Welche Art von Datenbank würden Sie empfehlen und warum? Berücksichtigen Sie dabei:
- Restaurants und ihre Menüs
- Kundenbestellungen
- Lieferfahrer und Routen
- Echtzeit-Tracking

+++

### Teil 2: Transfer und Problemlösung

**Kompetenzstufe**: Analysieren

Diese Aufgaben erfordern die Anwendung und Kombination mehrerer Konzepte.

+++

**Aufgabe 3**: Ein mittelständisches Unternehmen verwaltet derzeit alle Kundendaten, Bestellungen und Lagerbestände in verschiedenen Excel-Dateien. Erstellen Sie einen Migrationsplan mit:

a) Drei Hauptprobleme der aktuellen Lösung
b) Vorteile einer Datenbanklösung für diesen Fall
c) Welchen Datenbanktyp Sie empfehlen würden
d) Potenzielle Herausforderungen bei der Migration

+++

**Aufgabe 4**: Analysieren Sie folgendes Szenario:

Eine Universität plant ein neues System zur Verwaltung von:
- Studierendendaten
- Kursen und Vorlesungen 
- Prüfungsergebnissen
- Raumbelegungen
- Forschungspublikationen und deren Autoren-Netzwerke

Würden Sie eine einzelne Datenbank oder mehrere spezialisierte Datenbanken empfehlen? Begründen Sie Ihre Architekturentscheidung.

+++

---

## Zusammenfassung

In diesem Notebook haben Sie die Grundlagen von Datenbanksystemen kennengelernt:

| Konzept | Beschreibung | Wichtigkeit |
|---------|--------------|-------------|
| Datenbank vs. DBMS | Trennung von Daten und Verwaltungssystem | Ermöglicht Multi-User-Zugriff und Konsistenz |
| Datenbankarten | Relational, Key-Value, Dokument, Graph | Verschiedene Typen für verschiedene Anforderungen |
| DB vs. Excel | Professionelle vs. einfache Datenverwaltung | Skalierbarkeit und Sicherheit bei großen Datenmengen |
| Einsatzgebiete | WWS, ERP, CMS, CRM | Datenbanken sind überall im digitalen Leben |

**Zentrale Erkenntnisse**:
- Datenbanken sind essentiell für die moderne Informationsverarbeitung
- Die Wahl des richtigen Datenbanktyps hängt vom Anwendungsfall ab
- Ab einer gewissen Komplexität sind Datenbanken Excel-Tabellen überlegen
- Multi-User-Fähigkeit und Datenintegrität sind Kernvorteile von Datenbanken

**Nächste Schritte**: Im folgenden Notebook (21 - Relationale Datenbanken) werden Sie das wichtigste Datenbankmodell im Detail kennenlernen und verstehen, wie Daten strukturiert in Tabellen organisiert werden.

+++

---

## Musterlösungen

<details>
<summary>Lösung zu Aufgabe 1</summary>

**Unterschied Datenbank vs. DBMS:**

Eine **Datenbank** ist die Sammlung der eigentlichen Daten - die gespeicherten Informationen selbst.

Ein **Datenbankmanagementsystem (DBMS)** ist die Software, die diese Daten verwaltet, organisiert und den Zugriff darauf kontrolliert.

**Konkretes Beispiel:**
- Datenbank: Alle Kundendaten, Bestellungen und Produkte eines Online-Shops
- DBMS: MySQL als Software, die diese Daten speichert, Suchanfragen ausführt, Zugriffsrechte verwaltet und Backups erstellt

Das DBMS ist wie ein Bibliothekar (Software), während die Datenbank die Büchersammlung (Daten) ist.
</details>

<details>
<summary>Lösung zu Aufgabe 2</summary>

**Empfehlung für Essenslieferungs-App:**

Ich würde eine **Kombination aus relationaler Datenbank und Key-Value-Store** empfehlen:

**Hauptdatenbank: PostgreSQL (Relational)**
- Restaurants, Menüs, Preise → strukturierte Daten mit klaren Beziehungen
- Kundenkonten und Bestellhistorie → Transaktionssicherheit wichtig
- Rechnungen und Zahlungen → ACID-Eigenschaften erforderlich

**Ergänzung: Redis (Key-Value)**
- Echtzeit-Tracking der Lieferfahrer → schnelle Updates
- Session-Daten der App-Nutzer → temporäre Daten
- Caching von häufig abgerufenen Restaurantdaten → Performance

**Begründung:**
Die relationalen Aspekte (Bestellungen, Zahlungen) erfordern Konsistenz und Struktur, während Echtzeit-Features von der Geschwindigkeit einer Key-Value-DB profitieren.
</details>

<details>
<summary>Lösung zu Aufgabe 3</summary>

**Migrationsplan Excel → Datenbank:**

**a) Drei Hauptprobleme der Excel-Lösung:**
1. **Dateninkonsistenz**: Gleiche Kunden in verschiedenen Dateien mit unterschiedlichen Daten
2. **Keine Multi-User-Fähigkeit**: Mitarbeiter können nicht gleichzeitig arbeiten
3. **Fehleranfälligkeit**: Keine automatische Validierung, Formeln können überschrieben werden

**b) Vorteile der Datenbanklösung:**
- Zentrale Datenhaltung eliminiert Redundanzen
- Mehrere Mitarbeiter können gleichzeitig arbeiten
- Automatische Lagerbestandsaktualisierung bei Bestellungen
- Zugriffsrechte pro Mitarbeiter definierbar
- Automatische Backups möglich

**c) Empfohlener Datenbanktyp:**
**Relationale Datenbank (z.B. PostgreSQL)**
- Strukturierte Geschäftsdaten (Kunden, Produkte, Bestellungen)
- Klare Beziehungen zwischen Entitäten
- Transaktionssicherheit für Bestellvorgänge
- Bewährte Technologie, viel Support verfügbar

**d) Herausforderungen bei der Migration:**
- Datenbereinigung (Duplikate, Inkonsistenzen)
- Schulung der Mitarbeiter
- Initiale Kosten für Lizenz und Implementation
- Übergangsphase mit parallelen Systemen
</details>

<details>
<summary>Lösung zu Aufgabe 4</summary>

**Systemarchitektur für Universität:**

**Empfehlung: Hybrid-Ansatz mit zwei spezialisierten Datenbanken**

**1. Hauptdatenbank: Relationale DB (z.B. PostgreSQL)**
Für den Verwaltungskern:
- Studierendendaten (strukturiert, DSGVO-relevant)
- Kurse und Vorlesungen (klare Beziehungen)
- Prüfungsergebnisse (Transaktionssicherheit kritisch)
- Raumbelegungen (Kalenderdaten, Konfliktvermeidung)

**2. Spezialdatenbank: Graph-DB (z.B. Neo4j)**
Für Forschungsnetzwerk:
- Publikationen und Autoren-Beziehungen
- Zitationsnetzwerke
- Forschungskooperationen
- Interdisziplinäre Verbindungen

**Begründung:**
- Verwaltungsdaten sind hochstrukturiert → Relational
- Forschungsnetzwerke sind beziehungszentriert → Graph
- Trennung ermöglicht optimale Performance für beide Bereiche
- Verschiedene Zugriffsmuster und Nutzergruppen
- Einfachere Skalierung und Wartung

**Integration:**
- REST-API als Abstraktionsschicht
- Gemeinsame Nutzer-IDs als Brücke
- Regelmäßige Synchronisation der Stammdaten
</details>
