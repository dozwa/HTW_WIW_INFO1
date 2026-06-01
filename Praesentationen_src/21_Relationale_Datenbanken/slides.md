---
title: "21 — Relationale Datenbanken"
subtitle: "Tabellen, Schlüssel, Beziehungen, Datentypen, ACID"
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

1. Warum verknüpfte Tabellen statt einer Riesentabelle?
2. Anatomie einer Tabelle: Zeilen, Spalten, Werte
3. Primärschlüssel -- jede Zeile eindeutig
4. NULL -- der Wert, der fehlt
5. Fremdschlüssel -- Tabellen verbinden
6. Beziehungstypen 1:1, 1:n, n:m
7. SQL-Datentypen -- die richtige Schublade
8. Transaktionen & ACID -- die Sicherheitsgarantien

> **Lernziel**: Das relationale Modell verstehen -- damit wir in NB 22 mit SQLite *darauf* arbeiten können.

> **Wie wir heute arbeiten**: Konzept → kurze *Live-Demo* (Tabellen mit Python-Mitteln nachgebaut) → *Selbst überlegen* (Denkaufgaben im Notebook 21).

---

# Eine Riesentabelle? Lieber nicht.

## Alles in einer Tabelle

| bestell_id | kunde_name | kunde_email | produkt | preis | datum |
|---|---|---|---|---|---|
| 10 | Anna Müller | anna@example.de | Eco-Sneaker | 89.95 | 2026-05-03 |
| 11 | Anna Müller | anna@example.de | Hemp-High | 109.00 | 2026-05-09 |

- Annas Mail steht **doppelt** -- ändert sie sich, müssen *alle* Zeilen angefasst werden
- Tippfehler in einer Zeile → zwei Versionen von „Anna Müller"
- Ändert der Eco-Sneaker den Preis, stimmen alte Bestellungen plötzlich nicht mehr

> **Idee des relationalen Modells**: jede „Sache" einmal in ihrer eigenen Tabelle -- und über **Schlüssel** verbinden.

---

# Anatomie einer Tabelle

![](21_tabelle_anatomie.png){width=80%}

- **Zeile** (Datensatz / Tupel) = genau ein Ding · **Spalte** (Attribut) = eine Eigenschaft mit *einem* festen Datentyp
- keine zwei identischen Zeilen, eindeutige Spaltennamen

::: demobox
**▶ Live-Demo** -- `01_tabelle_als_datenstruktur.py` (eine Tabelle als Liste von Dicts)
:::

---

# Primärschlüssel -- jede Zeile eindeutig

```sql
CREATE TABLE kunde (
    kunde_id INTEGER PRIMARY KEY,   -- der Primärschlüssel
    vorname  TEXT,
    nachname TEXT,
    email    TEXT
);
```

Ein Primärschlüssel ist eine Spalte (oder Kombination), die jede Zeile **eindeutig identifiziert**:

- **eindeutig** -- kein Wert kommt zweimal vor
- **nie NULL** -- jede Zeile *muss* einen haben
- **unveränderlich** -- ändert sich nach dem Anlegen nicht

> Gute Kandidaten: Matrikelnummer, ISBN, oder eine automatisch hochgezählte ID. Schlechte: Name, E-Mail (ändern sich, sind nicht garantiert eindeutig).

::: exercisebox
**✎ Selbst überlegen** -- Notebook 21, Übung 1.1: Tabelle „Bücher" entwerfen -- welche Spalte wird PK?
:::

---

# NULL -- der Wert, der fehlt

![](21_null_beispiel.png){width=88%}

- mögliche Bedeutungen: *unbekannt* · *nicht anwendbar* · *noch nicht eingetragen* -- in Python: `None`
- **nie** beim Primärschlüssel; mit `NOT NULL` erzwingt man „diese Spalte ist Pflicht"

> Faustregel: NULL heißt *kein Wert* -- nicht 0, nicht `""`. Darum in Abfragen mit `IS NULL` prüfen, nie mit `= NULL` (mehr dazu in NB 23).

---

# Fremdschlüssel -- Tabellen verbinden

Ein **Fremdschlüssel** ist eine Spalte, die auf den **Primärschlüssel einer anderen Tabelle** zeigt.

```sql
CREATE TABLE bestellung (
    bestell_id INTEGER PRIMARY KEY,
    kunde_id   INTEGER,              -- Fremdschlüssel
    FOREIGN KEY (kunde_id) REFERENCES kunde(kunde_id)
);
```

- verbindet `bestellung` mit `kunde` -- ohne Annas Daten zu kopieren
- **referentielle Integrität**: das DBMS lässt keinen FK zu, der ins Leere zeigt -- keine „verwaisten" Bestellungen

::: demobox
**▶ Live-Demo** -- `02_fremdschluessel_beziehung.py`
:::

---

# Drei Beziehungstypen

![](21_beziehungstypen.png){width=68%}

> Der **Fremdschlüssel steht auf der „n"-Seite**. Eine **n:m**-Beziehung braucht eine **Zwischentabelle** mit zwei Fremdschlüsseln.

::: exercisebox
**✎ Selbst überlegen** -- Notebook 21, Übung 2.1: Beziehungen für ein Shop-System modellieren.
:::

---

# SQL-Datentypen -- die richtige Schublade

| Kategorie | Typen | wofür |
|---|---|---|
| Ganzzahl | `INTEGER`, `BIGINT` | IDs, Stückzahlen |
| Dezimal | `DECIMAL(p,s)` | **Geldbeträge** -- exakt, keine Rundungsfehler |
| Gleitkomma | `FLOAT`, `DOUBLE` | wissenschaftliche Werte (nicht für Geld!) |
| Text | `CHAR(n)`, `VARCHAR(n)`, `TEXT` | feste / variable / lange Texte |
| Datum/Zeit | `DATE`, `TIME`, `DATETIME`, `TIMESTAMP` | Termine, Zeitstempel |
| weitere | `BOOLEAN`, `ENUM`, `BLOB` | Ja/Nein, feste Auswahl, Binärdaten |

- richtige Wahl = Datenintegrität + Speichereffizienz + Performance
- Telefonnummern als **Text** (führende Nullen, `+49 …`), nicht als Zahl

::: exercisebox
**✎ Selbst überlegen** -- Notebook 21, Übung 3.1: für E-Mail, Preis, Lagerbestand, Geburtsdatum … den optimalen Typ wählen.
:::

---

# Transaktion -- alles oder nichts

Eine **Transaktion** fasst mehrere Operationen zu einer **unteilbaren Einheit** zusammen.

```sql
BEGIN TRANSACTION;
  UPDATE konto SET saldo = saldo - 1000 WHERE id = 'A';   -- Abbuchung
  UPDATE konto SET saldo = saldo + 1000 WHERE id = 'B';   -- Gutschrift
COMMIT;     -- beides gilt   |   ROLLBACK;  -- nichts gilt
```

- Klassiker: Überweisung -- entweder *beide* Buchungen oder *keine*
- Bei Veggie Soles: „Lagerbestand senken **und** Bestellung anlegen **und** Rechnung schreiben" -- entweder ganz oder gar nicht

> Schlägt mittendrin etwas fehl → `ROLLBACK`: die Datenbank ist wieder wie vorher.

---

# ACID -- die vier Garantien

| | steht für | bedeutet |
|---|---|---|
| **A** | Atomicity | alles oder nichts -- keine halben Transaktionen |
| **C** | Consistency | alle Regeln (Constraints) bleiben gültig |
| **I** | Isolation | parallele Transaktionen stören sich nicht |
| **D** | Durability | bestätigte Änderungen überleben auch einen Stromausfall |

> Ohne ACID kein verlässliches Online-Banking, kein E-Commerce, kein Ticketverkauf. Genau das unterscheidet ein echtes DBMS von einer Datei.

::: exercisebox
**✎ Selbst überlegen** -- Notebook 21, Übung 4.1: für jede ACID-Eigenschaft sagen, was bei einer Shop-Bestellung ohne sie schiefginge.
:::

---

# Cheat Card -- Notebook 21

| Begriff | Kurz |
|---|---|
| Tabelle / Zeile / Spalte | Relation / Datensatz (Tupel) / Attribut |
| Primärschlüssel (PK) | identifiziert jede Zeile -- eindeutig, nie NULL |
| Fremdschlüssel (FK) | zeigt auf den PK einer anderen Tabelle |
| NULL | „kein Wert" -- prüfen mit `IS NULL`, $\neq$ 0, $\neq$ `""` |
| 1:1 / 1:n / n:m | Beziehungstypen -- n:m braucht eine Zwischentabelle |
| `DECIMAL(p,s)` | Datentyp für Geldbeträge |
| Transaktion / ACID | Operationen als Einheit / die vier Sicherheitsgarantien |

> **Faustregel**: erst das Datenmodell (Tabellen + Beziehungen), dann der Code.

---

# Ausblick: ER-Diagramme und SQLite

- **Notebook 21b** -- *ausführliche* Einführung ins **Entity-Relationship-Diagramm**: wie man ein Datenmodell *zeichnet*, Schritt für Schritt, bevor man eine einzige Tabelle anlegt.
- **Notebook 22** -- SQLite mit Python: Tabellen anlegen, Daten einfügen, abfragen.
- **Notebook 23** -- fortgeschrittene Abfragen: `JOIN`, `GROUP BY`, `UPDATE`/`DELETE`.

```sql
-- Vorgeschmack auf NB 22:
CREATE TABLE produkt (produkt_id INTEGER PRIMARY KEY, name TEXT, preis REAL);
INSERT INTO produkt (name, preis) VALUES ('Eco-Sneaker', 89.95);
```

---

# Heute gelernt

✓ Warum verknüpfte Tabellen Redundanz vermeiden  
✓ Zeile / Spalte / Wert -- die Anatomie einer Tabelle  
✓ Primärschlüssel & NULL  
✓ Fremdschlüssel + referentielle Integrität  
✓ Beziehungstypen 1:1, 1:n, n:m  
✓ SQL-Datentypen passend wählen  
✓ Transaktionen & ACID  

::: exercisebox
**✎ Zur Vertiefung im Notebook 21:**

- Übungen 1.1--4.1 -- Denkaufgaben mit Musterlösung
- Abschlussübungen Aufg. 1--4: vom PK/FK-Unterschied bis zum vollständigen Datenbankschema für ein Ticketsystem
:::
