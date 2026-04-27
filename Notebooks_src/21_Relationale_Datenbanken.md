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

# 21 - Relationale Datenbanken: Struktur und Konzepte

## Lernziele

Nach Abschluss dieses Notebooks können Sie:
- Das relationale Modell und seine Grundprinzipien erklären
- Tabellen, Primär- und Fremdschlüssel sowie deren Beziehungen verstehen
- Verschiedene SQL-Datentypen und ihre Anwendungsbereiche identifizieren
- Die Konzepte von Transaktionen und ACID-Eigenschaften erläutern

**Kompetenzstufen**: Verstehen, Anwenden, Analysieren

---

## Voraussetzungen

Für dieses Notebook sollten Sie folgende Konzepte beherrschen:
- Grundlegendes Verständnis von Datenbanksystemen (Notebook 20)
- Datenstrukturen wie Listen und Dictionaries (Notebook 06)
- Grundlegende Programmierkonzepte (Notebooks 01-12)

Dieses Notebook führt in die **Theorie relationaler Datenbanken** ein. Die praktische Umsetzung mit SQLite folgt in den Notebooks 22 und 23.

---

+++

## Kapitel 1: Das Relationale Modell

### Einführung und Motivation

Das relationale Modell ist das Fundament der meisten modernen Datenbanksysteme. Es wurde 1970 von Edgar F. Codd bei IBM entwickelt und revolutionierte die Art, wie wir Daten speichern und organisieren. Aber warum war diese Entwicklung so bedeutend?

Vor dem relationalen Modell waren Datenbanken oft hierarchisch oder netzwerkartig organisiert. Diese Strukturen waren komplex, unflexibel und erforderten tiefes technisches Verständnis. Das relationale Modell brachte eine elegante Lösung: Es organisiert Daten in einfachen, zweidimensionalen Tabellen – ähnlich wie Sie es von Excel kennen, aber mit wesentlich mehr Struktur und Intelligenz.

Der geniale Ansatz liegt in der **mathematischen Fundierung** durch die Mengenlehre und Relationsalgebra. Dies ermöglicht es, komplexe Datenbeziehungen durch einfache, standardisierte Operationen zu beschreiben. SQL (Structured Query Language) wurde als Sprache entwickelt, um diese Operationen auszudrücken – sie ist heute der weltweite Standard für Datenbankabfragen.

Das relationale Modell löst drei fundamentale Probleme der Datenverwaltung: Es vermeidet Redundanzen durch Normalisierung, gewährleistet Datenintegrität durch Constraints und ermöglicht flexible Abfragen ohne vorherige Kenntnis der Datenstruktur.

+++

### Grundkonzepte: Tabellen, Zeilen und Spalten

Im relationalen Modell werden Daten in **Tabellen** (auch Relationen genannt) organisiert. Jede Tabelle repräsentiert eine Entität oder ein Konzept aus der realen Welt.

**Die drei Grundelemente:**

1. **Tabelle (Relation)**: Eine strukturierte Sammlung zusammengehöriger Daten
   - Beispiel: Eine Tabelle "Studierende" enthält alle Studierendendaten

2. **Zeile (Tupel/Datensatz)**: Ein einzelner Eintrag in der Tabelle
   - Beispiel: Die Daten eines bestimmten Studierenden

3. **Spalte (Attribut)**: Eine Eigenschaft, die für alle Einträge definiert ist
   - Beispiel: Matrikelnummer, Name, Studiengang

**Wichtige Eigenschaften:**
- Jede Spalte hat einen eindeutigen Namen
- Jede Spalte hat einen festgelegten Datentyp
- Die Reihenfolge der Zeilen ist irrelevant
- Jede Zeile ist eindeutig (keine Duplikate)

+++

### Visualisierung einer Tabelle

Betrachten wir ein konkretes Beispiel einer Tabelle "Studierende":

```
Tabelle: Studierende
┌──────────────┬─────────────┬──────────────┬───────────────────┬──────────┐
│ MatrikelNr   │ Vorname     │ Nachname     │ Studiengang       │ Semester │
├──────────────┼─────────────┼──────────────┼───────────────────┼──────────┤
│ 100001       │ Anna        │ Schmidt      │ Informatik        │ 3        │
│ 100002       │ Max         │ Müller       │ Wirtschaftsinf.   │ 2        │
│ 100003       │ Lisa        │ Weber        │ Informatik        │ 5        │
│ 100004       │ Tom         │ Fischer      │ Data Science      │ 1        │
└──────────────┴─────────────┴──────────────┴───────────────────┴──────────┘
```

**Beobachtungen:**
- Jede Zeile repräsentiert einen Studierenden
- Jede Spalte hat einen spezifischen Datentyp (MatrikelNr: Zahl, Name: Text, etc.)
- Die MatrikelNr könnte als eindeutiger Identifikator dienen

+++

### Primärschlüssel

Ein **Primärschlüssel** ist das wichtigste Konzept zur Gewährleistung der Eindeutigkeit in relationalen Datenbanken.

**Definition**: Ein Primärschlüssel ist eine Spalte (oder Kombination von Spalten), die jeden Datensatz in einer Tabelle eindeutig identifiziert.

**Eigenschaften eines Primärschlüssels:**
- **Eindeutigkeit**: Kein Wert darf doppelt vorkommen
- **Nicht-NULL**: Jeder Datensatz muss einen Primärschlüssel haben
- **Unveränderlich**: Sollte sich nach der Erstellung nicht ändern

**Beispiele für Primärschlüssel:**
- Matrikelnummer bei Studierenden
- ISBN bei Büchern
- Personalausweisnummer bei Bürgern
- Automatisch generierte ID-Nummern

In SQL-Syntax:
```sql
CREATE TABLE Studierende (
    MatrikelNr INTEGER PRIMARY KEY,
    Vorname VARCHAR(50),
    Nachname VARCHAR(50),
    Studiengang VARCHAR(100),
    Semester INTEGER
);
```

+++

### NULL-Werte verstehen

In relationalen Datenbanken hat **NULL** eine spezielle Bedeutung: Es repräsentiert das Fehlen eines Wertes.

**NULL ist NICHT:**
- Die Zahl 0
- Ein leerer String ""
- Ein Leerzeichen " "
- False

**NULL bedeutet:**
- Wert ist unbekannt
- Wert ist nicht anwendbar
- Wert wurde noch nicht eingegeben

**Beispiel:**
```
Tabelle: Mitarbeiter
┌────────┬─────────┬──────────────┬─────────────┐
│ ID     │ Name    │ Telefon      │ Abteilung   │
├────────┼─────────┼──────────────┼─────────────┤
│ 1      │ Meyer   │ 0123-456789  │ IT          │
│ 2      │ Schmidt │ NULL         │ Personal    │  ← Telefonnummer unbekannt
│ 3      │ Weber   │ 0987-654321  │ NULL        │  ← Noch keiner Abteilung zugeordnet
└────────┴─────────┴──────────────┴─────────────┘
```

**Wichtig für Abfragen:**
- NULL-Werte müssen mit `IS NULL` oder `IS NOT NULL` geprüft werden
- Normale Vergleiche (=, !=) funktionieren nicht mit NULL

+++

### Übung 1.1: Tabellenstruktur entwerfen

**Aufgabe**: Entwerfen Sie eine Tabellenstruktur für eine Bibliotheksverwaltung. Die Tabelle "Bücher" soll folgende Informationen speichern:
- Eindeutige Buchnummer
- Titel
- Autor
- Erscheinungsjahr
- Verfügbarkeit (ausgeliehen/verfügbar)

Bestimmen Sie:
1. Welche Spalte sollte der Primärschlüssel sein?
2. Welche Datentypen würden Sie verwenden?
3. Welche Spalten könnten NULL-Werte enthalten?

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

```sql
CREATE TABLE Buecher (
    BuchNr INTEGER PRIMARY KEY,      -- Primärschlüssel, eindeutig, NOT NULL
    Titel VARCHAR(200) NOT NULL,     -- Pflichtfeld, Text
    Autor VARCHAR(100),              -- Kann NULL sein (z.B. bei anonymen Werken)
    Erscheinungsjahr INTEGER,        -- Kann NULL sein (z.B. bei alten Büchern unbekannt)
    Verfuegbar BOOLEAN NOT NULL      -- Pflichtfeld, true/false
);
```

**Erklärung:**
1. **Primärschlüssel**: BuchNr - eindeutige Identifikation jedes Buches
2. **Datentypen**: 
   - INTEGER für Nummern und Jahr
   - VARCHAR für Texte mit Längenbeschränkung
   - BOOLEAN für Ja/Nein-Werte
3. **NULL-Werte**: Autor und Erscheinungsjahr könnten unbekannt sein
</details>

+++

---

## Kapitel 2: Tabellenbeziehungen

### Einführung in Beziehungen

Die wahre Stärke relationaler Datenbanken liegt in der Fähigkeit, Beziehungen zwischen verschiedenen Tabellen herzustellen. Diese Beziehungen spiegeln die Verbindungen wider, die auch in der realen Welt existieren.

Stellen Sie sich eine Universität vor: Studierende belegen Kurse, Professoren unterrichten Kurse, Kurse finden in Räumen statt. All diese Entitäten sind miteinander verbunden. In einer relationalen Datenbank modellieren wir diese Verbindungen durch **Fremdschlüssel** und definierte **Beziehungstypen**.

Der Vorteil dieser Aufteilung in mehrere verknüpfte Tabellen liegt in der **Normalisierung**: Daten werden nur einmal gespeichert, Redundanzen vermieden und Aktualisierungen müssen nur an einer Stelle vorgenommen werden. Dies reduziert Speicherplatz, verhindert Inkonsistenzen und macht das System wartungsfreundlicher.

+++

### Fremdschlüssel

Ein **Fremdschlüssel** ist eine Spalte (oder Spaltenkombination) in einer Tabelle, die auf den Primärschlüssel einer anderen Tabelle verweist.

**Zweck von Fremdschlüsseln:**
- Verbindung zwischen Tabellen herstellen
- Referentielle Integrität gewährleisten
- Verhindern von "verwaisten" Datensätzen

**Beispiel:**

```
Tabelle: Kurse                          Tabelle: Anmeldungen
┌─────────┬──────────────┬────────┐    ┌────┬──────────────┬─────────┬───────┐
│ KursNr  │ Bezeichnung  │ ECTS   │    │ ID │ MatrikelNr   │ KursNr  │ Note  │
├─────────┼──────────────┼────────┤    ├────┼──────────────┼─────────┼───────┤
│ CS101   │ Informatik 1 │ 6      │    │ 1  │ 100001       │ CS101   │ 2.3   │
│ CS102   │ Informatik 2 │ 6      │    │ 2  │ 100001       │ MA201   │ 1.7   │
│ MA201   │ Mathematik 1 │ 8      │    │ 3  │ 100002       │ CS101   │ 1.3   │
└─────────┴──────────────┴────────┘    └────┴──────────────┴─────────┴───────┘
                                               ↑              ↑
                                         Fremdschlüssel  Fremdschlüssel
                                         zu Studierende  zu Kurse
```

In SQL:
```sql
CREATE TABLE Anmeldungen (
    ID INTEGER PRIMARY KEY,
    MatrikelNr INTEGER,
    KursNr VARCHAR(10),
    Note DECIMAL(2,1),
    FOREIGN KEY (MatrikelNr) REFERENCES Studierende(MatrikelNr),
    FOREIGN KEY (KursNr) REFERENCES Kurse(KursNr)
);
```

+++

### Beziehungstypen

Es gibt drei Haupttypen von Beziehungen zwischen Tabellen:

#### 1:1-Beziehung (One-to-One)

Jeder Datensatz in Tabelle A ist mit genau einem Datensatz in Tabelle B verknüpft.

**Beispiel**: Person ↔ Personalausweis
- Jede Person hat genau einen Personalausweis
- Jeder Personalausweis gehört genau einer Person

#### 1:n-Beziehung (One-to-Many)

Ein Datensatz in Tabelle A kann mit mehreren Datensätzen in Tabelle B verknüpft sein.

**Beispiel**: Professor → Kurse
- Ein Professor kann mehrere Kurse unterrichten
- Jeder Kurs wird von einem Professor unterrichtet

#### n:m-Beziehung (Many-to-Many)

Mehrere Datensätze in Tabelle A können mit mehreren Datensätzen in Tabelle B verknüpft sein.

**Beispiel**: Studierende ↔ Kurse
- Ein Studierender kann mehrere Kurse belegen
- Ein Kurs kann von mehreren Studierenden belegt werden

**Wichtig**: n:m-Beziehungen erfordern eine Zwischentabelle (Junction Table)!

+++

### Entity-Relationship-Diagramm (ERD)

Ein ERD visualisiert die Struktur einer Datenbank und ihre Beziehungen:

```
┌──────────────┐        1:n        ┌──────────────┐
│  Professor   │───────────────────▶│    Kurse     │
├──────────────┤                    ├──────────────┤
│ ProfNr (PK)  │                    │ KursNr (PK)  │
│ Name         │                    │ Bezeichnung  │
│ Fakultät     │                    │ ProfNr (FK)  │
└──────────────┘                    └──────────────┘
                                            │
                                            │ n:m
                                            │
┌──────────────┐        n:m        ┌──────────────┐
│ Studierende  │◀───────────────────│ Anmeldungen  │
├──────────────┤                    ├──────────────┤
│ MatrikelNr(PK)│                   │ ID (PK)      │
│ Name         │                    │ MatrikelNr(FK)│
│ Studiengang  │                    │ KursNr (FK)  │
└──────────────┘                    │ Note         │
                                    └──────────────┘

Legende:
PK = Primary Key (Primärschlüssel)
FK = Foreign Key (Fremdschlüssel)
───▶ = Beziehung
```

+++

### Übung 2.1: Beziehungen modellieren

**Aufgabe**: Modellieren Sie die Beziehungen für ein Online-Shop-System mit folgenden Entitäten:
- Kunden (KundenNr, Name, Email)
- Produkte (ProduktNr, Bezeichnung, Preis)
- Bestellungen (BestellNr, KundenNr, Datum)
- Bestellpositionen (Position, BestellNr, ProduktNr, Anzahl)

Identifizieren Sie:
1. Die Beziehungstypen zwischen den Tabellen
2. Wo Fremdschlüssel benötigt werden

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

**Beziehungen:**

1. **Kunden → Bestellungen** (1:n)
   - Ein Kunde kann mehrere Bestellungen haben
   - Jede Bestellung gehört zu genau einem Kunden
   - Fremdschlüssel: KundenNr in Bestellungen-Tabelle

2. **Bestellungen → Bestellpositionen** (1:n)
   - Eine Bestellung kann mehrere Positionen haben
   - Jede Position gehört zu genau einer Bestellung
   - Fremdschlüssel: BestellNr in Bestellpositionen-Tabelle

3. **Produkte ↔ Bestellungen** (n:m über Bestellpositionen)
   - Ein Produkt kann in mehreren Bestellungen vorkommen
   - Eine Bestellung kann mehrere Produkte enthalten
   - Verknüpfung über Bestellpositionen-Tabelle
   - Fremdschlüssel: ProduktNr in Bestellpositionen-Tabelle

**SQL-Struktur:**
```sql
CREATE TABLE Kunden (
    KundenNr INTEGER PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100)
);

CREATE TABLE Produkte (
    ProduktNr INTEGER PRIMARY KEY,
    Bezeichnung VARCHAR(200),
    Preis DECIMAL(10,2)
);

CREATE TABLE Bestellungen (
    BestellNr INTEGER PRIMARY KEY,
    KundenNr INTEGER,
    Datum DATE,
    FOREIGN KEY (KundenNr) REFERENCES Kunden(KundenNr)
);

CREATE TABLE Bestellpositionen (
    Position INTEGER,
    BestellNr INTEGER,
    ProduktNr INTEGER,
    Anzahl INTEGER,
    PRIMARY KEY (BestellNr, Position),
    FOREIGN KEY (BestellNr) REFERENCES Bestellungen(BestellNr),
    FOREIGN KEY (ProduktNr) REFERENCES Produkte(ProduktNr)
);
```
</details>

+++

---

## Kapitel 3: SQL-Datentypen

### Einführung in Datentypen

Datentypen in SQL definieren, welche Art von Daten in einer Spalte gespeichert werden kann. Die richtige Wahl des Datentyps ist entscheidend für:

- **Datenintegrität**: Verhindert ungültige Eingaben
- **Speichereffizienz**: Optimaler Speicherplatzverbrauch
- **Performance**: Schnellere Abfragen und Sortierungen
- **Funktionalität**: Bestimmte Operationen sind nur mit passenden Datentypen möglich

Stellen Sie sich Datentypen wie Schubladen verschiedener Größen vor: Sie würden keine Büroklammern in einer riesigen Kiste aufbewahren und keine Aktenordner in eine winzige Schublade quetschen. Genauso sollten Sie für jede Art von Daten den passenden Datentyp wählen.

+++

### Numerische Datentypen

#### Ganzzahlen (Integer)

**Verwendung**: Für Zahlen ohne Nachkommastellen

| Typ | Bereich | Speicher | Verwendung |
|-----|---------|----------|------------|
| TINYINT | -128 bis 127 | 1 Byte | Alter, Anzahl |
| SMALLINT | ±32.767 | 2 Bytes | Postleitzahlen |
| INTEGER | ±2 Milliarden | 4 Bytes | IDs, Standardzahlen |
| BIGINT | ±9 Quintillionen | 8 Bytes | Große IDs |

#### Dezimalzahlen

**DECIMAL(p,s)** - Exakte Dezimalzahlen
- p = Gesamtzahl der Stellen
- s = Nachkommastellen
- Beispiel: DECIMAL(10,2) für Geldbeträge (99999999.99)

**FLOAT/DOUBLE** - Gleitkommazahlen
- Für wissenschaftliche Berechnungen
- Nicht für Geldbeträge (Rundungsfehler!)

+++

### Text-Datentypen

#### Feste Länge vs. Variable Länge

**CHAR(n)** - Feste Länge
- Immer genau n Zeichen
- Wird mit Leerzeichen aufgefüllt
- Gut für: Ländercodes (DE, FR), Postleitzahlen

**VARCHAR(n)** - Variable Länge
- Maximal n Zeichen
- Speichert nur tatsächliche Länge
- Gut für: Namen, Adressen, Beschreibungen

**TEXT** - Lange Texte
- Für sehr lange Texte (bis 65.535 Zeichen)
- Gut für: Artikel, Kommentare, Beschreibungen

**Beispiel:**
```sql
CREATE TABLE Artikel (
    ArtikelNr CHAR(10),        -- Immer 10 Zeichen, z.B. 'ART0000001'
    Titel VARCHAR(200),         -- Bis zu 200 Zeichen
    Kurzbeschreibung VARCHAR(500),
    Volltext TEXT              -- Beliebig langer Text
);
```

+++

### Datums- und Zeit-Datentypen

**DATE** - Nur Datum
- Format: 'YYYY-MM-DD'
- Beispiel: '2024-03-15'

**TIME** - Nur Uhrzeit
- Format: 'HH:MM:SS'
- Beispiel: '14:30:00'

**DATETIME** - Datum und Uhrzeit
- Format: 'YYYY-MM-DD HH:MM:SS'
- Beispiel: '2024-03-15 14:30:00'

**TIMESTAMP** - Zeitstempel
- Automatisch aktualisiert bei Änderungen
- Gut für: Erstellungs-/Änderungszeitpunkte

+++

### Spezielle Datentypen

**BOOLEAN** - Wahrheitswerte
- TRUE/FALSE oder 1/0
- Gut für: Ja/Nein-Entscheidungen, Status

**ENUM** - Aufzählungstyp
- Vordefinierte Werteliste
- Beispiel: ENUM('klein', 'mittel', 'groß')

**BLOB** - Binary Large Object
- Für Binärdaten (Bilder, Dokumente)
- Verschiedene Größen: TINYBLOB, BLOB, MEDIUMBLOB, LONGBLOB

**Beispiel:**
```sql
CREATE TABLE Mitarbeiter (
    MitarbeiterNr INTEGER PRIMARY KEY,
    Name VARCHAR(100),
    Gehalt DECIMAL(10,2),
    Eintrittsdatum DATE,
    Vollzeit BOOLEAN,
    Abteilung ENUM('IT', 'Personal', 'Vertrieb', 'Produktion'),
    Profilbild BLOB
);
```

+++

### Übung 3.1: Datentypen auswählen

**Aufgabe**: Wählen Sie für folgende Daten den optimalen SQL-Datentyp und begründen Sie:

1. E-Mail-Adresse
2. Preis eines Produkts
3. Anzahl der Lagerbestände
4. Geburtsdatum
5. Produktbeschreibung (kann sehr lang sein)
6. Geschlecht
7. Telefonnummer

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

1. **E-Mail-Adresse**: `VARCHAR(255)`
   - Variable Länge, max. 255 Zeichen reichen aus
   - Nicht CHAR, da E-Mails unterschiedlich lang sind

2. **Preis eines Produkts**: `DECIMAL(10,2)`
   - Exakte Dezimalzahl für Geldbeträge
   - Nicht FLOAT wegen Rundungsfehlern

3. **Anzahl der Lagerbestände**: `INTEGER`
   - Ganze Zahlen, keine Nachkommastellen
   - Reichweite ausreichend für normale Lagermengen

4. **Geburtsdatum**: `DATE`
   - Nur Datum benötigt, keine Uhrzeit
   - Ermöglicht Altersberechnungen

5. **Produktbeschreibung**: `TEXT`
   - Kann sehr lang werden
   - VARCHAR zu begrenzt

6. **Geschlecht**: `ENUM('m', 'w', 'd')` oder `CHAR(1)`
   - Begrenzte Auswahl
   - Speichereffizient

7. **Telefonnummer**: `VARCHAR(20)`
   - Als Text speichern (führende Nullen, internationale Formate)
   - Nicht INTEGER, da keine Berechnungen
</details>

+++

---

## Kapitel 4: Transaktionen und ACID

### Einführung in Transaktionen

Eine **Transaktion** ist eine Folge von Datenbankoperationen, die als eine unteilbare Einheit behandelt wird. Das klassische Beispiel ist eine Banküberweisung: Geld wird von einem Konto abgebucht und einem anderen gutgeschrieben. Diese beiden Operationen müssen entweder beide erfolgreich sein oder beide fehlschlagen – es darf niemals nur eine davon ausgeführt werden.

Transaktionen sind das Herzstück der Datenkonsistenz in relationalen Datenbanken. Sie garantieren, dass die Datenbank auch bei gleichzeitigen Zugriffen, Systemausfällen oder Fehlern immer in einem konsistenten Zustand bleibt. Ohne Transaktionen wären verlässliche Geschäftsanwendungen, Online-Banking oder E-Commerce undenkbar.

Die Qualität von Transaktionen wird durch vier fundamentale Eigenschaften definiert, die als **ACID-Prinzipien** bekannt sind. Diese Prinzipien unterscheiden professionelle Datenbanksysteme von einfachen Datenspeichern.

+++

### Das ACID-Prinzip

ACID steht für vier Eigenschaften, die Transaktionen erfüllen müssen:

#### A - Atomicity (Atomarität)

**"Alles oder Nichts"**

Eine Transaktion wird entweder vollständig ausgeführt oder gar nicht. Es gibt keine halben Transaktionen.

**Beispiel Überweisung:**
```sql
BEGIN TRANSACTION;
UPDATE Konten SET Saldo = Saldo - 1000 WHERE KontoNr = 'DE123';  -- Abbuchung
UPDATE Konten SET Saldo = Saldo + 1000 WHERE KontoNr = 'DE456';  -- Gutschrift
COMMIT;
```

Wenn die Gutschrift fehlschlägt, wird auch die Abbuchung rückgängig gemacht!

#### C - Consistency (Konsistenz)

**"Regeln werden immer eingehalten"**

Jede Transaktion überführt die Datenbank von einem konsistenten Zustand in einen anderen. Alle definierten Regeln (Constraints) bleiben gültig.

**Beispiel**: Kontostand darf nie negativ werden
- Vor Transaktion: Konto A = 1500€, Konto B = 500€
- Transaktion: 2000€ von A nach B überweisen
- Würde Regel verletzen → Transaktion wird abgelehnt

+++

#### I - Isolation (Isolierung)

**"Transaktionen stören sich nicht gegenseitig"**

Gleichzeitig ausgeführte Transaktionen beeinflussen sich nicht. Jede Transaktion läuft so ab, als wäre sie die einzige.

**Problem ohne Isolation:**
```
Zeit  Transaktion 1         Transaktion 2
────────────────────────────────────────────
t1    Lese Saldo: 1000€
t2                          Lese Saldo: 1000€
t3    Addiere 500€
t4                          Subtrahiere 200€
t5    Schreibe 1500€
t6                          Schreibe 800€  ← 500€ sind verloren!
```

**Mit Isolation**: Transaktionen werden serialisiert oder verwenden Locking-Mechanismen

#### D - Durability (Dauerhaftigkeit)

**"Bestätigte Änderungen bleiben erhalten"**

Sobald eine Transaktion mit COMMIT bestätigt wurde, bleiben die Änderungen dauerhaft erhalten – auch bei Stromausfall oder Systemabsturz.

**Mechanismen:**
- Write-Ahead Logging (WAL)
- Transaktionslogs
- Regelmäßige Checkpoints

+++

### Transaktionssteuerung in SQL

**Grundlegende Befehle:**

```sql
-- Transaktion starten
BEGIN TRANSACTION;

-- Operationen durchführen
INSERT INTO Bestellungen VALUES (...);
UPDATE Lager SET Bestand = Bestand - 1 WHERE ...;

-- Option 1: Änderungen bestätigen
COMMIT;

-- Option 2: Änderungen verwerfen
ROLLBACK;
```

**Beispiel einer sicheren Transaktion:**

```sql
BEGIN TRANSACTION;

-- Prüfung: Ist genug Geld vorhanden?
SELECT Saldo FROM Konten WHERE KontoNr = 'DE123';
-- Wenn Saldo >= 1000:

UPDATE Konten SET Saldo = Saldo - 1000 WHERE KontoNr = 'DE123';
UPDATE Konten SET Saldo = Saldo + 1000 WHERE KontoNr = 'DE456';

-- Log-Eintrag
INSERT INTO Transaktionslog (Von, Nach, Betrag, Zeitpunkt) 
VALUES ('DE123', 'DE456', 1000, NOW());

COMMIT;  -- Alle Änderungen werden dauerhaft
```

+++

### Übung 4.1: ACID-Prinzipien anwenden

**Aufgabe**: Ein Online-Shop verarbeitet eine Bestellung. Folgende Schritte sind nötig:
1. Produkt aus Lager entnehmen (Bestand reduzieren)
2. Bestellung anlegen
3. Rechnung erstellen
4. Versandauftrag generieren

Analysieren Sie:
a) Was könnte ohne Transaktionen schiefgehen?
b) Wie gewährleistet jedes ACID-Prinzip die Korrektheit?

**Musterlösung**:

<details>
<summary>Lösung anzeigen</summary>

**a) Mögliche Probleme ohne Transaktionen:**

1. **Inkonsistente Lagerbestände**: 
   - Lager wird reduziert, aber Bestellung schlägt fehl
   - Resultat: Ware ist "verschwunden"

2. **Doppelte Abbuchungen**:
   - Bei gleichzeitigen Bestellungen könnten beide denselben letzten Artikel bekommen

3. **Unvollständige Bestellungen**:
   - Bestellung angelegt, aber kein Versandauftrag
   - Kunde wartet ewig auf Lieferung

**b) ACID-Prinzipien lösen diese Probleme:**

**Atomicity**: 
- Entweder alle 4 Schritte erfolgreich ODER keine
- Bei Fehler in Schritt 3 werden auch Schritte 1-2 rückgängig gemacht

**Consistency**:
- Regel: "Lagerbestand >= 0" wird eingehalten
- Regel: "Jede Bestellung hat eine Rechnung" wird garantiert

**Isolation**:
- Zwei gleichzeitige Bestellungen für letztes Produkt:
- Nur eine erhält das Produkt, andere bekommt "ausverkauft"

**Durability**:
- Bestätigte Bestellung bleibt auch nach Stromausfall erhalten
- Kunde kann sicher sein, dass Bestellung angenommen wurde

**SQL-Transaktion:**
```sql
BEGIN TRANSACTION;
    -- 1. Lagerbestand prüfen und reduzieren
    UPDATE Produkte SET Lagerbestand = Lagerbestand - 1 
    WHERE ProduktNr = 'P123' AND Lagerbestand > 0;
    
    -- 2. Bestellung anlegen
    INSERT INTO Bestellungen (KundenNr, Datum) VALUES (456, NOW());
    
    -- 3. Rechnung erstellen  
    INSERT INTO Rechnungen (BestellNr, Betrag) VALUES (LAST_INSERT_ID(), 99.90);
    
    -- 4. Versandauftrag
    INSERT INTO Versand (BestellNr, Status) VALUES (LAST_INSERT_ID(), 'neu');
COMMIT;
```
</details>

+++

---

## Abschlussübungen

Die folgenden Aufgaben testen Ihr Verständnis der in diesem Notebook erlernten Konzepte. Bearbeiten Sie die Aufgaben selbstständig und vergleichen Sie Ihre Lösung anschließend mit den Musterlösungen am Ende des Notebooks.

### Teil 1: Grundlegende Anwendung

**Kompetenzstufe**: Verstehen, Anwenden

Diese Aufgaben testen die direkte Anwendung der erlernten Konzepte.

+++

**Aufgabe 1**: Erklären Sie den Unterschied zwischen einem Primärschlüssel und einem Fremdschlüssel. Geben Sie je ein konkretes Beispiel aus einem Bibliothekssystem.

+++

**Aufgabe 2**: Eine Firma möchte Mitarbeiterprojekte verwalten. Ein Mitarbeiter kann an mehreren Projekten arbeiten, und ein Projekt hat mehrere Mitarbeiter. Entwerfen Sie die notwendigen Tabellen mit:
- Sinnvollen Spalten und Datentypen
- Primär- und Fremdschlüsseln
- Der korrekten Verknüpfungstabelle

+++

### Teil 2: Transfer und Problemlösung

**Kompetenzstufe**: Analysieren

Diese Aufgaben erfordern die Kombination mehrerer Konzepte und eigenständiges Problemlösen.

+++

**Aufgabe 3**: Analysieren Sie folgende Situation:

Ein Ticketsystem für Konzerte soll entwickelt werden. Dabei gelten folgende Geschäftsregeln:
- Jedes Konzert hat eine maximale Kapazität
- Kunden können mehrere Tickets für verschiedene Konzerte kaufen
- Jedes Ticket ist eindeutig und gehört zu genau einem Konzert
- Stornierte Tickets werden wieder verfügbar

Erstellen Sie:
a) Ein vollständiges Datenbankschema (Tabellen, Spalten, Datentypen)
b) Identifizieren Sie alle Beziehungstypen
c) Erklären Sie, warum Transaktionen beim Ticketverkauf wichtig sind

+++

**Aufgabe 4**: ACID-Analyse

Ein Geldautomat führt eine Auszahlung durch:
1. Karte und PIN werden geprüft
2. Kontostand wird geprüft
3. Geld wird ausgegeben
4. Kontostand wird reduziert
5. Transaktion wird protokolliert

Beschreiben Sie für jedes ACID-Prinzip ein konkretes Szenario, was ohne diese Eigenschaft schiefgehen könnte.

+++

---

## Zusammenfassung

In diesem Notebook haben Sie die Grundlagen relationaler Datenbanken kennengelernt:

| Konzept | Beschreibung | Wichtigkeit |
|---------|--------------|-------------|
| Relationales Modell | Daten in Tabellen mit Zeilen und Spalten | Grundlage aller relationalen DBs |
| Primärschlüssel | Eindeutige Identifikation jeder Zeile | Verhindert Duplikate |
| Fremdschlüssel | Verbindung zwischen Tabellen | Ermöglicht Beziehungen |
| Beziehungstypen | 1:1, 1:n, n:m | Modellierung realer Zusammenhänge |
| SQL-Datentypen | INTEGER, VARCHAR, DATE, etc. | Datenintegrität und Effizienz |
| Transaktionen | Gruppe von Operationen als Einheit | Konsistenz bei Änderungen |
| ACID | Atomicity, Consistency, Isolation, Durability | Zuverlässigkeit garantiert |

**Zentrale Erkenntnisse**:
- Relationale Datenbanken strukturieren Daten in verknüpften Tabellen
- Schlüssel und Beziehungen vermeiden Redundanzen und Inkonsistenzen  
- Die richtige Wahl von Datentypen ist essentiell für Effizienz
- ACID-Eigenschaften garantieren verlässliche Transaktionen

**Nächste Schritte**: Im folgenden Notebook (22 - SQLite Grundlagen) werden Sie lernen, wie Sie diese Konzepte praktisch mit Python und SQLite umsetzen.

+++

---

## Musterlösungen

<details>
<summary>Lösung zu Aufgabe 1</summary>

**Unterschied Primärschlüssel vs. Fremdschlüssel:**

**Primärschlüssel:**
- Identifiziert jeden Datensatz in einer Tabelle eindeutig
- Muss eindeutig und NOT NULL sein
- Jede Tabelle hat genau einen Primärschlüssel

**Fremdschlüssel:**
- Verweist auf den Primärschlüssel einer anderen Tabelle
- Stellt Beziehungen zwischen Tabellen her
- Kann NULL sein und mehrfach vorkommen

**Beispiele aus Bibliothekssystem:**

Tabelle "Buecher":
- **Primärschlüssel**: ISBN (eindeutige Buchnummer)

Tabelle "Ausleihen":
- **Primärschlüssel**: AusleihNr
- **Fremdschlüssel**: ISBN (verweist auf Buecher.ISBN)
- **Fremdschlüssel**: LeserNr (verweist auf Leser.LeserNr)

Die ISBN in der Ausleihen-Tabelle ist ein Fremdschlüssel, der angibt, welches Buch ausgeliehen wurde.
</details>

<details>
<summary>Lösung zu Aufgabe 2</summary>

**Datenbankdesign für Mitarbeiterprojekte (n:m-Beziehung):**

```sql
-- Tabelle: Mitarbeiter
CREATE TABLE Mitarbeiter (
    MitarbeiterNr INTEGER PRIMARY KEY,
    Vorname VARCHAR(50) NOT NULL,
    Nachname VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    Abteilung VARCHAR(50),
    Eintrittsdatum DATE
);

-- Tabelle: Projekte  
CREATE TABLE Projekte (
    ProjektNr INTEGER PRIMARY KEY,
    Bezeichnung VARCHAR(200) NOT NULL,
    Startdatum DATE,
    Enddatum DATE,
    Budget DECIMAL(12,2),
    Status ENUM('Planung', 'Aktiv', 'Abgeschlossen')
);

-- Verknüpfungstabelle für n:m-Beziehung
CREATE TABLE Projektzuteilungen (
    MitarbeiterNr INTEGER,
    ProjektNr INTEGER,
    Rolle VARCHAR(50),  -- z.B. 'Projektleiter', 'Entwickler'
    Stunden_pro_Woche INTEGER,
    Start_Zuteilung DATE,
    Ende_Zuteilung DATE,
    PRIMARY KEY (MitarbeiterNr, ProjektNr, Start_Zuteilung),
    FOREIGN KEY (MitarbeiterNr) REFERENCES Mitarbeiter(MitarbeiterNr),
    FOREIGN KEY (ProjektNr) REFERENCES Projekte(ProjektNr)
);
```

**Erklärung:**
- Die Verknüpfungstabelle löst die n:m-Beziehung auf
- Zusammengesetzter Primärschlüssel verhindert doppelte Zuteilungen
- Zusätzliche Attribute (Rolle, Stunden) in der Verknüpfungstabelle
</details>

<details>
<summary>Lösung zu Aufgabe 3</summary>

**a) Datenbankschema für Ticketsystem:**

```sql
-- Konzerte
CREATE TABLE Konzerte (
    KonzertNr INTEGER PRIMARY KEY AUTO_INCREMENT,
    Kuenstler VARCHAR(100) NOT NULL,
    Veranstaltungsort VARCHAR(200) NOT NULL,
    Datum DATE NOT NULL,
    Uhrzeit TIME NOT NULL,
    Max_Kapazitaet INTEGER NOT NULL,
    Verfuegbare_Plaetze INTEGER NOT NULL,
    Preis DECIMAL(8,2) NOT NULL,
    CHECK (Verfuegbare_Plaetze >= 0),
    CHECK (Verfuegbare_Plaetze <= Max_Kapazitaet)
);

-- Kunden
CREATE TABLE Kunden (
    KundenNr INTEGER PRIMARY KEY AUTO_INCREMENT,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Vorname VARCHAR(50),
    Nachname VARCHAR(50),
    Telefon VARCHAR(20),
    Registriert_seit DATETIME DEFAULT NOW()
);

-- Tickets
CREATE TABLE Tickets (
    TicketNr VARCHAR(20) PRIMARY KEY,  -- z.B. 'TK2024-000001'
    KonzertNr INTEGER NOT NULL,
    KundenNr INTEGER,
    Kaufdatum DATETIME DEFAULT NOW(),
    Sitzplatz VARCHAR(10),
    Status ENUM('Aktiv', 'Storniert') DEFAULT 'Aktiv',
    Storniert_am DATETIME NULL,
    FOREIGN KEY (KonzertNr) REFERENCES Konzerte(KonzertNr),
    FOREIGN KEY (KundenNr) REFERENCES Kunden(KundenNr)
);
```

**b) Beziehungstypen:**
- **Kunden → Tickets**: 1:n (Ein Kunde kann mehrere Tickets haben)
- **Konzerte → Tickets**: 1:n (Ein Konzert hat viele Tickets)
- **Kunden ↔ Konzerte**: n:m über Tickets (implizit)

**c) Wichtigkeit von Transaktionen:**

Transaktionen sind kritisch für:

1. **Vermeidung von Überbuchungen:**
   - Zwei Kunden versuchen gleichzeitig das letzte Ticket zu kaufen
   - Ohne Transaktion: Beide könnten es bekommen → Überbuchung
   - Mit Transaktion: Nur einer erhält das Ticket

2. **Konsistenz bei Stornierungen:**
   ```sql
   BEGIN TRANSACTION;
   UPDATE Tickets SET Status = 'Storniert' WHERE TicketNr = 'TK2024-000001';
   UPDATE Konzerte SET Verfuegbare_Plaetze = Verfuegbare_Plaetze + 1 
   WHERE KonzertNr = (SELECT KonzertNr FROM Tickets WHERE TicketNr = 'TK2024-000001');
   COMMIT;
   ```

3. **Atomare Ticketbuchung:**
   - Ticket erstellen + Plätze reduzieren + Zahlung verarbeiten
   - Alles muss erfolgreich sein oder nichts
</details>

<details>
<summary>Lösung zu Aufgabe 4</summary>

**ACID-Szenarien für Geldautomaten-Auszahlung:**

**Ohne Atomicity:**
- Szenario: Geld wird ausgegeben (Schritt 3), aber Kontostand wird nicht reduziert (Schritt 4 schlägt fehl)
- Folge: Kunde erhält Geld, aber Konto wird nicht belastet → Bank verliert Geld
- Mit Atomicity: Wenn Schritt 4 fehlschlägt, wird auch Schritt 3 rückgängig gemacht (kein Geld ausgegeben)

**Ohne Consistency:**
- Szenario: Kontostand ist 500€, Kunde will 1000€ abheben
- Folge: Ohne Konsistenzprüfung würde Konto ins Minus gehen (-500€)
- Mit Consistency: Regel "Kontostand >= 0" verhindert die Transaktion

**Ohne Isolation:**
- Szenario: Partner hebt gleichzeitig am anderen Automaten ab
- Beide lesen Kontostand: 1000€
- Automat 1: gibt 600€ aus, schreibt 400€
- Automat 2: gibt 700€ aus, schreibt 300€
- Folge: 1300€ ausgezahlt, aber nur 700€ abgebucht
- Mit Isolation: Zweite Transaktion wartet oder sieht aktualisierten Saldo

**Ohne Durability:**
- Szenario: Stromausfall direkt nach Geldausgabe
- Folge: Transaktion nicht gespeichert, Konto nicht belastet, aber Geld ausgegeben
- Mit Durability: Transaktion wird in Log geschrieben bevor Geld ausgegeben wird
- Nach Neustart wird aus Log rekonstruiert
</details>
