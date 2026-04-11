---
title: "Python SQLite3 Cheat Sheet"
geometry: margin=1.5cm
fontsize: 10pt
header-includes:
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhead[L]{Python SQLite3 Cheat Sheet}
  - \fancyhead[R]{Informatik 1}
  - \fancyfoot[C]{\thepage}
  - \usepackage{listings}
  - \usepackage{xcolor}
  - \lstset{basicstyle=\ttfamily\small, breaklines=true, frame=single, backgroundcolor=\color{gray!10}, aboveskip=4pt, belowskip=4pt}
  - \setlength{\parskip}{2pt}
  - \setlength{\parindent}{0pt}
  - \renewcommand{\arraystretch}{1.1}
---

# Python sqlite3 Modul

\begin{lstlisting}[language=Python]
import sqlite3
conn = sqlite3.connect('datenbank.db')   # Verbindung herstellen
conn = sqlite3.connect(':memory:')       # temporaere In-Memory-DB
cursor = conn.cursor()                   # Cursor erstellen

cursor.execute("SQL-Befehl")                          # SQL ausfuehren
cursor.execute("SELECT * FROM t WHERE id=?", (id,))   # mit Parameter
cursor.executemany("INSERT ...", liste_von_tupeln)    # mehrere Zeilen

ergebnis = cursor.fetchone()     # Ein Tupel oder None
ergebnisse = cursor.fetchall()   # Liste aller Tupel

conn.commit()   # Aenderungen speichern (nach INSERT/UPDATE/DELETE!)
conn.close()    # Verbindung schliessen
\end{lstlisting}

**Context Manager (Best Practice):** `with sqlite3.connect('db.db') as conn:`

**Attribute:** `cursor.rowcount` (betroffene Zeilen), `cursor.lastrowid` (letzte INSERT-ID)

# Datentypen

| SQLite | Python | Beschreibung |
|--------|--------|--------------|
| INTEGER | int | Ganzzahl |
| REAL | float | Gleitkommazahl |
| TEXT | str | Zeichenkette |
| BLOB | bytes | Binaerdaten |
| NULL | None | Kein Wert |

# CREATE TABLE

\begin{lstlisting}[language=SQL]
CREATE TABLE [IF NOT EXISTS] tabelle (
    spalte1 TYP [CONSTRAINTS],
    spalte2 TYP [CONSTRAINTS]
);
\end{lstlisting}

| Constraint | Beschreibung |
|------------|--------------|
| `PRIMARY KEY` | Eindeutiger Identifier |
| `AUTOINCREMENT` | Automatisch hochzaehlen |
| `NOT NULL` | Wert erforderlich |
| `UNIQUE` | Keine Duplikate |
| `DEFAULT wert` | Standardwert |
| `FOREIGN KEY (fk) REFERENCES tabelle(pk)` | Fremdschluessel |

# INSERT / SELECT

\begin{lstlisting}[language=SQL]
INSERT INTO tabelle (spalte1, spalte2) VALUES (wert1, wert2);
SELECT * FROM tabelle;
SELECT spalte1, spalte2 FROM tabelle;
SELECT DISTINCT spalte FROM tabelle;
SELECT spalte AS alias FROM tabelle;
\end{lstlisting}

# WHERE -- Filtern

\begin{lstlisting}[language=SQL]
SELECT ... FROM tabelle WHERE bedingung;
\end{lstlisting}

| Operator | Bedeutung | Operator | Bedeutung |
|----------|-----------|----------|-----------|
| `=` | Gleich | `!=`, `<>` | Ungleich |
| `<`, `>` | Kleiner/Groesser | `<=`, `>=` | Kleiner-/Groesser-gleich |
| `AND` | Beide wahr | `OR` | Mind. eine wahr |
| `NOT` | Negation | | |

\begin{lstlisting}[language=SQL]
WHERE preis BETWEEN 10 AND 50      -- Wertebereich (inklusiv)
WHERE land IN ('DE', 'AT', 'CH')   -- Liste von Werten
WHERE name LIKE 'A%'               -- beginnt mit A (% = beliebig viele Zeichen)
WHERE name LIKE 'A_B'              -- _ = genau 1 Zeichen
WHERE spalte IS NULL               -- NULL-Pruefung (NICHT: = NULL !)
WHERE spalte IS NOT NULL
\end{lstlisting}

# ORDER BY / UPDATE / DELETE

\begin{lstlisting}[language=SQL]
SELECT ... ORDER BY spalte ASC;              -- aufsteigend (Standard)
SELECT ... ORDER BY spalte DESC;             -- absteigend
SELECT ... ORDER BY spalte1 ASC, spalte2 DESC;

UPDATE tabelle SET spalte1 = wert1, spalte2 = wert2 WHERE bedingung;
DELETE FROM tabelle WHERE bedingung;
\end{lstlisting}

**Achtung:** Ohne `WHERE` werden bei UPDATE/DELETE ALLE Zeilen betroffen!

# JOIN -- Tabellen verbinden

\begin{lstlisting}[language=SQL]
-- INNER JOIN: Nur uebereinstimmende Zeilen
SELECT a.spalte, b.spalte FROM tabelle_a a
INNER JOIN tabelle_b b ON a.fk = b.pk;

-- LEFT JOIN: Alle Zeilen der linken Tabelle (keine Uebereinstimmung: NULL)
SELECT a.spalte, b.spalte FROM tabelle_a a
LEFT JOIN tabelle_b b ON a.fk = b.pk;

-- Datensaetze OHNE Verknuepfung finden:
SELECT a.* FROM tabelle_a a
LEFT JOIN tabelle_b b ON a.fk = b.pk WHERE b.pk IS NULL;
\end{lstlisting}

# Aggregatfunktionen & GROUP BY

| Funktion | Beschreibung |
|----------|--------------|
| `COUNT(*)` | Anzahl aller Zeilen |
| `COUNT(spalte)` | Anzahl Nicht-NULL-Werte |
| `SUM(spalte)` | Summe |
| `AVG(spalte)` | Durchschnitt |
| `MIN(spalte)` / `MAX(spalte)` | Minimum / Maximum |

\begin{lstlisting}[language=SQL]
SELECT spalte, COUNT(*), AVG(wert) FROM tabelle GROUP BY spalte;
SELECT spalte, COUNT(*) as anzahl FROM tabelle GROUP BY spalte HAVING anzahl > 10;
\end{lstlisting}

**WHERE** filtert Zeilen VOR Gruppierung, **HAVING** filtert Gruppen NACH Aggregation.

# SQL-Abfrage Reihenfolge

\begin{lstlisting}[language=SQL]
SELECT spalten       -- 5. Spaltenauswahl
FROM tabelle         -- 1. Datenquelle
JOIN andere ON ...   -- 2. Verknuepfung
WHERE bedingung      -- 3. Zeilenfilter
GROUP BY spalte      -- 4. Gruppierung
HAVING bedingung     -- 6. Gruppenfilter
ORDER BY spalte      -- 7. Sortierung
LIMIT n;             -- 8. Begrenzung
\end{lstlisting}

# Wichtige Regeln

1. **Parametrisierte Abfragen** (`?`) verwenden -- Schutz vor SQL-Injection!
2. **commit()** nach INSERT/UPDATE/DELETE nicht vergessen
3. **WHERE** bei UPDATE/DELETE immer angeben
4. **IS NULL** statt `= NULL` verwenden
5. **Erst SELECT testen**, dann UPDATE/DELETE ausfuehren
