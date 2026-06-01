---
title: "23 — SQLite Vertiefung"
subtitle: "WHERE, ORDER BY, JOIN, UPDATE/DELETE, GROUP BY & Aggregate"
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

1. `WHERE` feiner: `AND`/`OR`, `BETWEEN`, `IN`, `LIKE`, `IS NULL`
2. `ORDER BY` -- Ergebnisse sortieren
3. `JOIN` -- Tabellen verbinden (`INNER`, `LEFT`)
4. `UPDATE` & `DELETE` -- ändern und löschen (vorsichtig!)
5. Aggregatfunktionen + `GROUP BY` + `HAVING` -- Auswertungen
6. Der Bauplan einer Abfrage -- in welcher Reihenfolge das passiert

> **Lernziel**: Mit SQL gezielt filtern, sortieren, Tabellen verknüpfen, Daten ändern und Kennzahlen berechnen.

> **Wie wir heute arbeiten**: Konzept → *Live-Demo* (Veggie-Soles-Shop, In-Memory-DB) → *Sofort ausprobieren* (Notebook 23, Chinook-Datenbank).

---

# Von „alles holen" zu „genau das brauchen"

`SELECT * FROM produkt` gibt *alle* Spalten und *alle* Zeilen zurück. In der Praxis will man:

- nur bestimmte Zeilen (`WHERE`), in einer Reihenfolge (`ORDER BY`)
- Daten aus mehreren Tabellen (`JOIN`)
- Daten auch *ändern* (`UPDATE`, `DELETE`)
- *zusammengefasst*: Anzahl, Summe, Durchschnitt (`GROUP BY` + Aggregate)

```sql
SELECT kunde.name, SUM(bestellung.betrag) AS umsatz
FROM kunde JOIN bestellung ON kunde.kunde_id = bestellung.kunde_id
GROUP BY kunde.kunde_id HAVING umsatz > 200 ORDER BY umsatz DESC;
```

> Diese Bausteine schauen wir uns heute Stück für Stück an.

---

# `WHERE` -- gezielt filtern

```sql
SELECT name, preis FROM produkt
WHERE (kategorie = 'Low-Cut' OR kategorie = 'High-Cut') AND preis < 100;
```

| Werkzeug | Beispiel |
|---|---|
| Vergleiche / Logik | `= != < >` · `... AND ...` · `... OR ...` (Klammern!) |
| Bereich (inklusiv) | `preis BETWEEN 90 AND 120` |
| Liste / Textmuster | `kategorie IN ('Boot','High-Cut')` · `name LIKE '%er%'` |
| fehlender Wert | `kategorie IS NULL` -- **nicht** `= NULL`! |

::: demobox
**▶ Live-Demo** -- `01_where_und_order_by.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 23, Übungen 1.1 & 1.2: Tracks > 300.000 ms; Rock-/Metal-Tracks für 0.99 (mit Klammern!).
:::

---

# `ORDER BY` -- sortieren

```sql
SELECT name, preis FROM produkt ORDER BY preis ASC;             -- günstigste zuerst
SELECT kategorie, name, preis FROM produkt ORDER BY kategorie, preis DESC;
```

- `ASC` = aufsteigend (Standard, kann weg) · `DESC` = absteigend
- mehrere Spalten: die **erste** hat Vorrang, die zweite entscheidet bei Gleichstand
- ohne `ORDER BY` ist die Reihenfolge **nicht garantiert**

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 23, Übung 2.1: die 10 günstigsten Tracks (Name + Preis, nach Preis aufsteigend).
:::

---

# `JOIN` -- Tabellen verbinden

![](23_joins_mengen.png){width=68%}

- `INNER JOIN` -- nur Treffer in **beiden** Tabellen · `LEFT JOIN` -- **alle** links, fehlt rechts → `NULL` · verbunden über `ON` (FK = PK)

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 23, Übungen 3.1 & 3.2: Tracks mit Genrenamen (`INNER JOIN`); Kunden ohne Rechnung (`LEFT JOIN` + `IS NULL`).
:::

---

# `INNER` vs. `LEFT` -- konkret

![](23_joins_tabellen.png){width=52%}

`INNER JOIN` „vergisst" Zeilen ohne Treffer · `LEFT JOIN` behält sie -- so findet man auch *die ohne* (`... WHERE rechte.id IS NULL`).

::: demobox
**▶ Live-Demo** -- `02_inner_join.py` (3-Tabellen-JOIN) · `03_left_join.py` (Kund:innen ohne Bestellung)
:::

---

# `UPDATE` & `DELETE` -- ändern und löschen

```sql
UPDATE produkt SET preis = 79.90 WHERE name = 'Kork-Slip';
DELETE FROM produkt WHERE aktiv = 0;
```

- **immer mit `WHERE`!** Ohne `WHERE` trifft es *alle* Zeilen -- und ist nicht rückgängig zu machen.
- **erst `SELECT`** mit derselben `WHERE`-Bedingung -- prüfen, *was* getroffen würde · Backup vor größeren Änderungen
- mehrere Spalten: `SET a = ..., b = ...` · auch hier Platzhalter `?`

::: demobox
**▶ Live-Demo** -- `04_update_delete.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 23, Übung 4.1: Künstler anlegen und per `UPDATE` umbenennen.
:::

---

# Aggregatfunktionen -- aus vielen Zeilen ein Wert

| `COUNT(*)` | `SUM(x)` | `AVG(x)` | `MIN(x)` | `MAX(x)` |
|---|---|---|---|---|
| Zeilen zählen | summieren | Durchschnitt | Minimum | Maximum |

```sql
SELECT COUNT(*), AVG(preis), MAX(preis) FROM produkt;
```

- über die ganze Tabelle: das Ergebnis ist **eine** Zeile
- `COUNT(*)` zählt alle Zeilen, `COUNT(spalte)` nur die mit Wert (ohne `NULL`)

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 23, Übung 5.1: Gesamtumsatz pro Kunde (`JOIN` + `GROUP BY`).
:::

---

# `GROUP BY` & `HAVING` -- Auswertung je Gruppe

![](23_groupby_aggregation.png){width=54%}

- `GROUP BY g` → Aggregate **je Gruppe** · `HAVING` filtert Gruppen *nach* der Aggregation, `WHERE` Zeilen *davor*

::: demobox
**▶ Live-Demo** -- `05_aggregat_group_by.py`
:::

::: exercisebox
**✎ Sofort ausprobieren** -- Notebook 23, Übung 5.2: nur Kunden mit Umsatz > 40 (`HAVING`).
:::

---

# Der Bauplan einer Abfrage

![](23_sql_pipeline.png){width=92%}

> Geschrieben wird `SELECT ... FROM ... WHERE ... GROUP BY ... HAVING ... ORDER BY` -- *abgearbeitet* in anderer Reihenfolge. Deshalb kann `WHERE` nicht auf ein Aggregat zugreifen -- dafür gibt es `HAVING`.

---

# Cheat Card -- Notebook 23

| Aufgabe | SQL |
|---|---|
| filtern | `WHERE bedingung` -- `AND`/`OR`, `BETWEEN`, `IN`, `LIKE`, `IS NULL` |
| sortieren | `ORDER BY spalte [ASC\|DESC]` |
| Tabellen verbinden | `... JOIN andere ON a.x = andere.x` (`INNER` / `LEFT`) |
| ändern / löschen | `UPDATE t SET s = w WHERE ...` · `DELETE FROM t WHERE ...` |
| zusammenfassen | `SELECT g, COUNT(*), SUM(x) FROM t GROUP BY g` |
| Gruppen filtern | `... GROUP BY g HAVING aggregat > wert` |

> **Faustregel**: `UPDATE`/`DELETE` *nie* ohne `WHERE`. `WHERE` filtert Zeilen, `HAVING` filtert Gruppen.

---

# Ausblick: Datenbankmodule abgeschlossen

Mit den Notebooks **20--23** haben Sie den Bogen geschlagen:

- **20** -- was Datenbanken sind, welche Arten es gibt, warum nicht Excel
- **21** -- das relationale Modell: Tabellen, Schlüssel, Beziehungen, ACID
- **21b** -- Datenmodelle als ER-Diagramm entwerfen
- **22** -- SQLite mit Python: anlegen, einfügen, abfragen
- **23** -- fortgeschrittene Abfragen: filtern, sortieren, verbinden, ändern, auswerten

> Damit können Sie eine kleine Anwendung mit dauerhafter, strukturierter Datenhaltung bauen -- vom ER-Entwurf bis zur Auswertungsabfrage.

---

# Heute gelernt

✓ `WHERE` mit `AND`/`OR`, `BETWEEN`, `IN`, `LIKE`, `IS NULL`  
✓ `ORDER BY` -- ein- und mehrspaltig, `ASC`/`DESC`  
✓ `INNER JOIN` und `LEFT JOIN` -- inkl. „die ohne Treffer" finden  
✓ `UPDATE` und `DELETE` -- immer mit `WHERE`  
✓ Aggregatfunktionen, `GROUP BY`, `HAVING`  
✓ in welcher Reihenfolge SQL eine Abfrage abarbeitet  

::: exercisebox
**✎ Zur Vertiefung im Notebook 23:**

- „Sofort ausprobieren"-Übungen 1.1--5.2 (sind Sie schon mitgegangen)
- Abschlussübungen Aufg. 1--4: USA-Kunden mit „J", Alben von „The …", Umsatzanalyse nach Land, längste Tracks pro Genre
:::
