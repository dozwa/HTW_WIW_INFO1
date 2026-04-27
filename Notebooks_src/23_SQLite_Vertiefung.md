---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
kernelspec:
  display_name: base2
  language: python
  name: python3
---

# 23 - SQLite Vertiefung: Fortgeschrittene Abfragen und Datenmanipulation

## Lernziele

Nach Abschluss dieses Notebooks können Sie:
- Daten mit WHERE, ORDER BY und komplexen Bedingungen gezielt filtern und sortieren
- Tabellen mit INNER JOIN und LEFT JOIN verknüpfen und Beziehungen abfragen
- Daten mit UPDATE und DELETE gezielt ändern und löschen
- Aggregatfunktionen (COUNT, SUM, AVG) mit GROUP BY für Auswertungen nutzen

**Kompetenzstufen**: Anwenden, Analysieren

---

## Voraussetzungen

Für dieses Notebook sollten Sie folgende Konzepte beherrschen:
- Grundlagen relationaler Datenbanken: Tabellen, Primär- und Fremdschlüssel (Notebook 21)
- SQLite-Grundlagen: connect(), cursor(), execute(), fetchall(), commit() (Notebook 22)
- CREATE TABLE und INSERT-Befehle (Notebook 22)
- Parametrisierte Abfragen mit ? (Notebook 22)

Falls Sie diese Konzepte noch nicht sicher beherrschen, wiederholen Sie bitte die entsprechenden Notebooks.

---

+++

## Vorbereitung: Die Chinook-Datenbank

In diesem Notebook arbeiten wir mit der **Chinook-Datenbank**, einer Beispieldatenbank, die einen digitalen Musikshop simuliert. Sie enthält Informationen über Künstler, Alben, Tracks, Kunden und Rechnungen.

Die wichtigsten Tabellen für dieses Notebook sind:
- `artists`: Künstler (ArtistId, Name)
- `albums`: Alben (AlbumId, Title, ArtistId)
- `tracks`: Musikstücke (TrackId, Name, AlbumId, GenreId, Composer, Milliseconds, UnitPrice)
- `genres`: Musikgenres (GenreId, Name)
- `customers`: Kunden (CustomerId, FirstName, LastName, Country, City)
- `invoices`: Rechnungen (InvoiceId, CustomerId, InvoiceDate, Total)

```{code-cell} ipython3
# Import des sqlite3-Moduls
import sqlite3

# Hilfsfunktion für Abfragen (aus Notebook 22 bekannt)
def query_db(query, params=(), limit=10):
    """Führt eine SELECT-Abfrage aus und zeigt die Ergebnisse."""
    with sqlite3.connect('chinook.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        ergebnisse = cursor.fetchall()
        
        print(f"{len(ergebnisse)} Ergebnisse gefunden.")
        print("-" * 60)
        
        for zeile in ergebnisse[:limit]:
            print(zeile)
        
        if len(ergebnisse) > limit:
            print(f"... und {len(ergebnisse) - limit} weitere Ergebnisse")
        
        return ergebnisse
```

---

## Kapitel 1: Daten filtern mit WHERE

+++

### Einführung und Motivation

In Notebook 22 haben Sie gelernt, mit `SELECT` alle Daten aus einer Tabelle abzurufen. In der Praxis benötigen Sie jedoch selten alle Daten – stattdessen suchen Sie nach spezifischen Informationen. Die `WHERE`-Klausel ermöglicht es, Ergebnisse auf Datensätze zu beschränken, die bestimmten Bedingungen entsprechen.

Stellen Sie sich vor, Sie verwalten eine Musikdatenbank mit tausenden Tracks. Ohne Filterung müssten Sie alle Einträge manuell durchsuchen. Mit `WHERE` können Sie gezielt nach Rock-Songs, Tracks eines bestimmten Komponisten oder Liedern mit einem Preis unter 1€ suchen.

Die `WHERE`-Klausel ist das wichtigste Werkzeug für präzise Datenbankabfragen und bildet die Grundlage für alle fortgeschrittenen Filteroperationen.

+++

### Syntax der WHERE-Klausel

**Grundsyntax:**
```sql
SELECT spalte1, spalte2, ...
FROM tabelle
WHERE bedingung;
```

**Verfügbare Vergleichsoperatoren:**

| Operator | Bedeutung | Beispiel |
|----------|-----------|----------|
| `=` | Gleich | `WHERE jahr = 2024` |
| `!=` oder `<>` | Ungleich | `WHERE status != 'aktiv'` |
| `<` | Kleiner als | `WHERE preis < 10` |
| `>` | Größer als | `WHERE alter > 18` |
| `<=` | Kleiner oder gleich | `WHERE menge <= 100` |
| `>=` | Größer oder gleich | `WHERE punkte >= 50` |

+++

### Beispiel 1: Einfache Bedingung

Wir suchen alle Tracks, die genau 0.99€ kosten:

```{code-cell} ipython3
query_db("SELECT Name, UnitPrice FROM tracks")
```

```{code-cell} ipython3
# Tracks mit Preis von 0.99€
query_db("SELECT Name, UnitPrice FROM tracks WHERE UnitPrice = 0.99")
```

```{code-cell} ipython3
query_db("SELECT Name, UnitPrice FROM tracks WHERE UnitPrice != 0.99")
```

Die Abfrage gibt nur Tracks zurück, bei denen der Preis exakt 0.99 beträgt. Alle anderen Datensätze werden herausgefiltert.

+++

### Beispiel 2: Textvergleiche

Bei Textvergleichen müssen Werte in Anführungszeichen gesetzt werden:

```{code-cell} ipython3
# Alle Kunden aus Deutschland
query_db("SELECT FirstName, LastName, City FROM customers WHERE Country = 'Germany'")
```

**Wichtig:** Bei Textvergleichen wird standardmäßig die Groß-/Kleinschreibung beachtet. `'Germany'` und `'germany'` sind unterschiedliche Werte.

+++

### Übung 1.1: Einfache WHERE-Abfrage

**Aufgabe:** Schreiben Sie eine Abfrage, die alle Tracks mit einer Länge von mehr als 300.000 Millisekunden (5 Minuten) anzeigt. Geben Sie den Namen und die Länge in Millisekunden aus.

**Hinweise:**
- Die Spalte für die Länge heißt `Milliseconds`
- Verwenden Sie den Operator `>`
- Nutzen Sie die Funktion `query_db()`

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung:**

<details>
<summary>Lösung anzeigen</summary>

```python
# Tracks länger als 5 Minuten (300.000 ms)
query_db("SELECT Name, Milliseconds FROM tracks WHERE Milliseconds > 300000")
```

**Erklärung:** Die WHERE-Klausel filtert alle Tracks, deren Milliseconds-Wert größer als 300.000 ist. Dies entspricht Tracks mit einer Länge von mehr als 5 Minuten.
</details>

+++

---

### Komplexe Bedingungen mit AND, OR und NOT

+++

Häufig müssen mehrere Bedingungen kombiniert werden. SQL bietet dafür die logischen Operatoren `AND`, `OR` und `NOT`, die Sie bereits aus Notebook 08 (Operatoren) kennen.

**Logische Operatoren:**

| Operator | Bedeutung | Ergebnis |
|----------|-----------|----------|
| `AND` | Beide Bedingungen müssen wahr sein | Nur wenn A UND B wahr |
| `OR` | Mindestens eine Bedingung muss wahr sein | Wenn A ODER B wahr |
| `NOT` | Kehrt die Bedingung um | Wenn A NICHT wahr |

+++

### Beispiel 3: Bedingungen mit AND

Wir suchen günstige, kurze Tracks – Songs unter 1€ UND unter 3 Minuten:

```{code-cell} ipython3
# Günstige UND kurze Tracks
query_db("""
    SELECT Name, UnitPrice, Milliseconds 
    FROM tracks 
    WHERE UnitPrice < 1 AND Milliseconds < 180000
""")
```

```{code-cell} ipython3
# Günstige UND kurze Tracks
query_db("""
    SELECT Name, UnitPrice 
    FROM tracks 
    WHERE UnitPrice < 1 AND Milliseconds < 180000
""")
```

Mit `AND` werden nur Datensätze zurückgegeben, die **beide** Bedingungen erfüllen.

+++

### Beispiel 4: Bedingungen mit OR

Wir suchen Kunden aus Deutschland ODER Frankreich:

```{code-cell} ipython3
# Kunden aus Deutschland ODER Frankreich
query_db("""
    SELECT FirstName, LastName, Country 
    FROM customers 
    WHERE Country = 'Germany' OR Country = 'France'
""")
```

Mit `OR` werden Datensätze zurückgegeben, die **mindestens eine** der Bedingungen erfüllen.

+++

### Übung 1.2: Komplexe Bedingungen

**Aufgabe:** Finden Sie alle Tracks, die entweder zum Genre 1 (Rock) ODER zum Genre 3 (Metal) gehören UND einen Preis von 0.99€ haben.

**Hinweise:**
- Verwenden Sie Klammern zur Gruppierung: `(bedingung1 OR bedingung2) AND bedingung3`
- Die Genre-Spalte heißt `GenreId`

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung:**

<details>
<summary>Lösung anzeigen</summary>

```python
# Rock oder Metal Tracks für 0.99€
query_db("""
    SELECT Name, GenreId, UnitPrice 
    FROM tracks 
    WHERE (GenreId = 1 OR GenreId = 3) AND UnitPrice = 0.99
""")
```

**Erklärung:** Die Klammern stellen sicher, dass zuerst die OR-Bedingung ausgewertet wird. Ohne Klammern würde `GenreId = 1 OR (GenreId = 3 AND UnitPrice = 0.99)` ausgewertet – ein völlig anderes Ergebnis!
</details>

+++

---

### Spezielle Operatoren: BETWEEN, IN und LIKE

+++

SQL bietet spezielle Operatoren für häufige Filterszenarien:

| Operator | Verwendung | Beispiel |
|----------|------------|----------|
| `BETWEEN` | Wertebereich (inklusiv) | `WHERE preis BETWEEN 1 AND 5` |
| `IN` | Liste von Werten | `WHERE land IN ('DE', 'AT', 'CH')` |
| `LIKE` | Musterabgleich | `WHERE name LIKE 'A%'` |

+++

### Beispiel 5: BETWEEN für Wertebereiche

Tracks mit einer Länge zwischen 3 und 4 Minuten:

```{code-cell} ipython3
# Tracks zwischen 3 und 4 Minuten
query_db("""
    SELECT Name, Milliseconds 
    FROM tracks 
    WHERE Milliseconds BETWEEN 180000 AND 240000
""")
```

`BETWEEN` ist inklusiv – die Grenzen sind im Ergebnis enthalten. Die Abfrage entspricht: `WHERE Milliseconds >= 180000 AND Milliseconds <= 240000`

+++

### Beispiel 6: IN für Wertelisten

Kunden aus deutschsprachigen Ländern:

```{code-cell} ipython3
# Kunden aus Deutschland, Österreich oder Schweiz
query_db("""
    SELECT FirstName, LastName, Country 
    FROM customers 
    WHERE Country IN ('Germany', 'France')
""")
```

`IN` ist eine elegante Alternative zu mehreren OR-Bedingungen und macht die Abfrage lesbarer.

+++

### Beispiel 7: LIKE für Musterabgleiche

Der LIKE-Operator ermöglicht die Suche nach Textmustern:
- `%` steht für beliebig viele Zeichen (0 oder mehr)
- `_` steht für genau ein Zeichen

```{code-cell} ipython3
# Tracks, deren Name mit "Love" beginnt
query_db("SELECT Name FROM tracks WHERE Name LIKE '%Love%'")
```

```{code-cell} ipython3
# Tracks, die "Love" irgendwo im Namen enthalten
query_db("SELECT Name FROM tracks WHERE Name LIKE '%Love%'")
```

---

### NULL-Werte prüfen

+++

In Notebook 21 haben Sie gelernt, dass `NULL` in Datenbanken "kein Wert" bedeutet. NULL-Werte können **nicht** mit `=` verglichen werden – Sie müssen `IS NULL` oder `IS NOT NULL` verwenden.

**Wichtig:** `WHERE spalte = NULL` funktioniert NICHT! Verwenden Sie stattdessen `WHERE spalte IS NULL`.

```{code-cell} ipython3
# Tracks ohne Komponisten-Angabe
query_db("SELECT Name, Composer FROM tracks WHERE Composer IS NULL")
```

```{code-cell} ipython3
# Tracks MIT Komponisten-Angabe
query_db("SELECT Name, Composer FROM tracks WHERE Composer IS NOT NULL")
```

---

## Kapitel 2: Ergebnisse sortieren mit ORDER BY

+++

### Einführung und Motivation

Die Reihenfolge der Ergebnisse einer SQL-Abfrage ist standardmäßig nicht definiert – die Datenbank gibt die Daten in der internen Speicherreihenfolge zurück. Für aussagekräftige Analysen und Berichte benötigen Sie jedoch oft sortierte Daten: alphabetisch nach Namen, chronologisch nach Datum oder nach Preis geordnet.

Die `ORDER BY`-Klausel ermöglicht die Sortierung nach einer oder mehreren Spalten in aufsteigender (`ASC`) oder absteigender (`DESC`) Reihenfolge.

+++

### Syntax von ORDER BY

```sql
SELECT spalten
FROM tabelle
WHERE bedingung
ORDER BY spalte [ASC|DESC];
```

- `ASC` (ascending): Aufsteigende Sortierung (Standard, kann weggelassen werden)
- `DESC` (descending): Absteigende Sortierung

+++

### Beispiel 8: Aufsteigende Sortierung

```{code-cell} ipython3
# Kunden alphabetisch nach Nachname sortiert
query_db("""
    SELECT FirstName, LastName, Country 
    FROM customers 
    ORDER BY LastName ASC
""")
```

### Beispiel 9: Absteigende Sortierung

```{code-cell} ipython3
# Längste Tracks zuerst
query_db("""
    SELECT Name, Milliseconds 
    FROM tracks 
    ORDER BY Milliseconds ASC
""")
```

### Beispiel 10: Sortierung nach mehreren Spalten

Sie können nach mehreren Spalten sortieren – die erste Spalte hat Priorität:

```{code-cell} ipython3
# Kunden nach Land, dann nach Stadt sortiert
query_db("""
    SELECT Country, City, FirstName, LastName 
    FROM customers 
    ORDER BY Country ASC, City ASC
""")
```

### Übung 2.1: Sortierung anwenden

**Aufgabe:** Zeigen Sie die 10 günstigsten Tracks an. Geben Sie Name und Preis aus, sortiert nach Preis aufsteigend.

**Hinweise:**
- Nutzen Sie ORDER BY für die Sortierung
- Die Funktion query_db zeigt standardmäßig nur 10 Ergebnisse

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung:**

<details>
<summary>Lösung anzeigen</summary>

```python
# Die 10 günstigsten Tracks
query_db("""
    SELECT Name, UnitPrice 
    FROM tracks 
    ORDER BY UnitPrice ASC
""")
```

**Erklärung:** ORDER BY UnitPrice ASC sortiert die Tracks nach Preis, beginnend mit dem günstigsten. Die query_db-Funktion zeigt automatisch nur die ersten 10 Ergebnisse.
</details>

+++

---

## Kapitel 3: Tabellen verbinden mit JOIN

+++

### Einführung und Motivation

In Notebook 21 haben Sie gelernt, dass relationale Datenbanken Daten in mehreren verknüpften Tabellen speichern, um Redundanzen zu vermeiden. Die Künstler-Informationen stehen in der `artists`-Tabelle, die Alben in der `albums`-Tabelle. Um beide Informationen gemeinsam abzufragen – etwa "Welche Alben hat welcher Künstler?" – müssen die Tabellen verknüpft werden.

Der `JOIN`-Befehl ermöglicht genau das: Er verbindet Zeilen aus zwei oder mehr Tabellen basierend auf einer gemeinsamen Spalte (typischerweise einem Fremdschlüssel). Dies ist eines der mächtigsten Konzepte in SQL und essentiell für die Arbeit mit relationalen Datenbanken.

SQLite unterstützt verschiedene JOIN-Typen. Die wichtigsten sind:
- **INNER JOIN**: Gibt nur Zeilen zurück, die in beiden Tabellen eine Übereinstimmung haben
- **LEFT JOIN**: Gibt alle Zeilen der linken Tabelle zurück, auch ohne Übereinstimmung

+++

### INNER JOIN: Nur übereinstimmende Zeilen

**Syntax:**
```sql
SELECT spalten
FROM tabelle1
INNER JOIN tabelle2 ON tabelle1.spalte = tabelle2.spalte;
```

Der INNER JOIN gibt nur Zeilen zurück, bei denen die Verknüpfungsbedingung (nach `ON`) erfüllt ist.

+++

### Beispiel 11: INNER JOIN zwischen albums und artists

Wir möchten wissen, welche Alben zu welchen Künstlern gehören:

```{code-cell} ipython3
# Alben mit Künstlernamen
query_db("""
    SELECT albums.Title, artists.Name
    FROM albums
    INNER JOIN artists ON albums.ArtistId = artists.ArtistId
""")
```

**Erklärung des Beispiels:**

1. `FROM albums`: Wir starten mit der albums-Tabelle
2. `INNER JOIN artists`: Wir verbinden mit der artists-Tabelle
3. `ON albums.ArtistId = artists.ArtistId`: Die Verknüpfung erfolgt über die ArtistId
4. `SELECT albums.Title, artists.Name`: Wir wählen die gewünschten Spalten aus beiden Tabellen

+++

### Beispiel 12: INNER JOIN mit WHERE-Filter

JOINs können mit WHERE kombiniert werden:

```{code-cell} ipython3
# Alben des Künstlers "AC/DC"
query_db("""
    SELECT albums.Title, artists.Name
    FROM albums
    INNER JOIN artists ON albums.ArtistId = artists.ArtistId
    WHERE artists.Name = 'AC/DC'
""")
```

### Übung 3.1: INNER JOIN anwenden

**Aufgabe:** Schreiben Sie eine Abfrage, die alle Tracks mit ihrem Genrenamen anzeigt. Die Tabelle `genres` enthält die Spalten GenreId und Name.

**Hinweise:**
- Verbinden Sie `tracks` und `genres` über `GenreId`
- Geben Sie den Track-Namen und den Genre-Namen aus
- Achten Sie auf eindeutige Spaltennamen: `tracks.Name` und `genres.Name`

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung:**

<details>
<summary>Lösung anzeigen</summary>

```python
# Tracks mit Genre-Namen
query_db("""
    SELECT tracks.Name, genres.Name
    FROM tracks
    INNER JOIN genres ON tracks.GenreId = genres.GenreId
""")
```

**Erklärung:** Der JOIN verbindet jeden Track mit seinem Genre über die gemeinsame GenreId. Da beide Tabellen eine Spalte "Name" haben, müssen wir die Tabellennamen als Präfix verwenden.
</details>

+++

---

### LEFT JOIN: Alle Zeilen der linken Tabelle

+++

Der **LEFT JOIN** gibt alle Zeilen der linken Tabelle zurück, auch wenn es keine Übereinstimmung in der rechten Tabelle gibt. Für nicht übereinstimmende Zeilen werden NULL-Werte eingesetzt.

**Syntax:**
```sql
SELECT spalten
FROM tabelle1
LEFT JOIN tabelle2 ON tabelle1.spalte = tabelle2.spalte;
```

+++

### Beispiel 13: LEFT JOIN – Künstler mit und ohne Alben

```{code-cell} ipython3
# Alle Künstler, auch ohne Alben
query_db("""
    SELECT artists.Name, albums.Title
    FROM artists
    LEFT JOIN albums ON artists.ArtistId = albums.ArtistId
    ORDER BY artists.Name
""")
```

Beachten Sie: Der erste Künstler "A Cor Do Som" hat `None` (NULL) als Album-Titel – er hat keine Alben in der Datenbank.

+++

### Beispiel 14: LEFT JOIN – Nur Datensätze ohne Übereinstimmung finden

Mit LEFT JOIN und einer WHERE-Bedingung auf NULL können Sie Datensätze finden, die keine Verknüpfung haben:

```{code-cell} ipython3
# Künstler OHNE Alben
query_db("""
    SELECT artists.Name
    FROM artists
    LEFT JOIN albums ON artists.ArtistId = albums.ArtistId
    WHERE albums.AlbumId IS NULL
""")
```

### Übung 3.2: LEFT JOIN anwenden

**Aufgabe:** Finden Sie heraus, wie viele Kunden noch nie eine Rechnung erhalten haben. Nutzen Sie dafür einen LEFT JOIN zwischen `customers` und `invoices` und filtern Sie nach NULL-Werten.

**Hinweise:**
- Die Tabellen werden über `CustomerId` verknüpft
- Geben Sie Vorname, Nachname und InvoiceId aus
- Filtern Sie nach `invoices.InvoiceId IS NULL`

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung:**

<details>
<summary>Lösung anzeigen</summary>

```python
# Kunden ohne Rechnungen
query_db("""
    SELECT customers.FirstName, customers.LastName, invoices.InvoiceId
    FROM customers
    LEFT JOIN invoices ON customers.CustomerId = invoices.CustomerId
    WHERE invoices.InvoiceId IS NULL
""")
```

**Erklärung:** Der LEFT JOIN zeigt alle Kunden, auch solche ohne Rechnungen. Die WHERE-Bedingung filtert dann nur die Kunden heraus, bei denen keine Rechnung existiert (InvoiceId ist NULL). In der Chinook-Datenbank haben alle Kunden Rechnungen, daher ist das Ergebnis leer.
</details>

+++

---

## Kapitel 4: Daten ändern und löschen

+++

### Einführung und Motivation

In Notebook 22 haben Sie gelernt, Daten mit `INSERT` einzufügen. Doch Daten müssen auch aktualisiert und gelöscht werden können. Ein Kunde zieht um und seine Adresse ändert sich – wir brauchen `UPDATE`. Ein Produkt wird aus dem Sortiment genommen – wir brauchen `DELETE`.

Diese Operationen sind **destruktiv** und können nicht rückgängig gemacht werden (ohne Backup). Daher ist besondere Vorsicht geboten, insbesondere bei der Verwendung der `WHERE`-Klausel.

+++

### Hilfsfunktion für Schreiboperationen

Wir erstellen zunächst eine Hilfsfunktion für UPDATE- und DELETE-Operationen:

```{code-cell} ipython3
def execute_db(query, params=()):
    """Führt eine INSERT, UPDATE oder DELETE-Operation aus."""
    try:
        with sqlite3.connect('chinook.db') as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            print(f"Erfolgreich: {cursor.rowcount} Zeile(n) betroffen.")
            return cursor.rowcount
    except sqlite3.Error as e:
        print(f"Fehler: {e}")
        return 0
```

---

### UPDATE: Daten aktualisieren

+++

Der `UPDATE`-Befehl ändert bestehende Datensätze.

**Syntax:**
```sql
UPDATE tabelle
SET spalte1 = wert1, spalte2 = wert2, ...
WHERE bedingung;
```

**⚠️ WICHTIG:** Ohne `WHERE`-Klausel werden ALLE Zeilen der Tabelle aktualisiert!

+++

### Beispiel 15: Einzelnen Datensatz aktualisieren

Wir fügen zunächst einen Testdatensatz ein und aktualisieren ihn dann:

```{code-cell} ipython3
# Neuen Künstler einfügen
execute_db("INSERT INTO artists (Name) VALUES (?)", ('Test Künstler',))
```

```{code-cell} ipython3
# Namen des Künstlers ändern
execute_db("""
    UPDATE artists 
    SET Name = ? 
    WHERE Name = ?
""", ('Neuer Name', 'Test Künstler'))
```

```{code-cell} ipython3
# Überprüfen, ob die Änderung erfolgreich war
query_db("SELECT * FROM artists WHERE Name LIKE 'Neuer%'")
```

### Beispiel 16: Mehrere Spalten gleichzeitig aktualisieren

```{code-cell} ipython3
# Vorher: Kundeninformationen anzeigen
query_db("SELECT FirstName, LastName, City, Country FROM customers WHERE CustomerId = 1")
```

```{code-cell} ipython3
# Stadt und Land eines Kunden ändern (Beispiel - wird wieder rückgängig gemacht)
execute_db("""
    UPDATE customers 
    SET City = 'München', Country = 'Germany'
    WHERE CustomerId = 1
""")
```

```{code-cell} ipython3
# Nachher: Änderung überprüfen
query_db("SELECT FirstName, LastName, City, Country FROM customers WHERE CustomerId = 1")
```

```{code-cell} ipython3
# Änderung rückgängig machen
execute_db("""
    UPDATE customers 
    SET City = 'São José dos Campos', Country = 'Brazil'
    WHERE CustomerId = 1
""")
```

### Übung 4.1: UPDATE anwenden

**Aufgabe:** Erstellen Sie einen neuen Künstler mit dem Namen "Übungskünstler" und ändern Sie den Namen dann zu "Mein Lieblingskünstler".

**Hinweise:**
- Nutzen Sie `execute_db()` für beide Operationen
- Verwenden Sie parametrisierte Abfragen

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung:**

<details>
<summary>Lösung anzeigen</summary>

```python
# Schritt 1: Künstler erstellen
execute_db("INSERT INTO artists (Name) VALUES (?)", ('Übungskünstler',))

# Schritt 2: Namen ändern
execute_db("""
    UPDATE artists 
    SET Name = ? 
    WHERE Name = ?
""", ('Mein Lieblingskünstler', 'Übungskünstler'))

# Überprüfen
query_db("SELECT * FROM artists WHERE Name LIKE '%Lieblingskünstler%'")
```

**Erklärung:** Zuerst wird der Künstler mit INSERT erstellt, dann mit UPDATE umbenannt. Die WHERE-Klausel stellt sicher, dass nur der gewünschte Datensatz geändert wird.
</details>

+++

---

### DELETE: Daten löschen

+++

Der `DELETE`-Befehl entfernt Datensätze aus einer Tabelle.

**Syntax:**
```sql
DELETE FROM tabelle
WHERE bedingung;
```

**⚠️ KRITISCH:** Ohne `WHERE`-Klausel werden ALLE Zeilen gelöscht! Dies ist nicht rückgängig zu machen.

+++

### Beispiel 17: Datensatz löschen

```{code-cell} ipython3
# Den zuvor erstellten Test-Künstler löschen
execute_db("DELETE FROM artists WHERE Name = ?", ('Neuer Name',))
```

```{code-cell} ipython3
# Überprüfen, ob die Löschung erfolgreich war
query_db("SELECT * FROM artists WHERE Name LIKE 'Neuer%'")
```

### Best Practices für UPDATE und DELETE

1. **Immer WHERE verwenden**: Ohne WHERE werden ALLE Datensätze betroffen
2. **Erst SELECT, dann UPDATE/DELETE**: Testen Sie die WHERE-Bedingung zuerst mit SELECT
3. **Parametrisierte Abfragen**: Schützen vor SQL-Injection
4. **Backups erstellen**: Vor größeren Änderungen

```{code-cell} ipython3
# Gute Praxis: Erst prüfen, was gelöscht würde
query_db("SELECT * FROM artists WHERE Name LIKE '%Lieblingskünstler%'")
```

```{code-cell} ipython3
# Dann löschen
execute_db("DELETE FROM artists WHERE Name LIKE '%Lieblingskünstler%'")
```

---

## Kapitel 5: Aggregatfunktionen und GROUP BY

+++

### Einführung und Motivation

Bisher haben Sie einzelne Datensätze abgefragt. Oft benötigen Sie jedoch zusammenfassende Informationen: Wie viele Tracks gibt es? Was ist der durchschnittliche Preis? Welches Genre hat die meisten Songs?

**Aggregatfunktionen** berechnen einen einzelnen Wert aus einer Menge von Zeilen. In Kombination mit **GROUP BY** können Sie diese Berechnungen für Gruppen von Daten durchführen – ähnlich wie die groupby()-Funktion in Pandas (Notebook 17).

+++

### Die wichtigsten Aggregatfunktionen

| Funktion | Beschreibung | Beispiel |
|----------|--------------|----------|
| `COUNT(*)` | Zählt alle Zeilen | Anzahl der Tracks |
| `COUNT(spalte)` | Zählt Nicht-NULL-Werte | Anzahl der Tracks mit Komponist |
| `SUM(spalte)` | Summiert Werte | Gesamtumsatz |
| `AVG(spalte)` | Berechnet Durchschnitt | Durchschnittspreis |
| `MIN(spalte)` | Findet Minimum | Günstigster Preis |
| `MAX(spalte)` | Findet Maximum | Teuerster Preis |

+++

### Beispiel 18: Einfache Aggregatfunktionen

```{code-cell} ipython3
# Anzahl aller Tracks
query_db("SELECT COUNT(*) FROM tracks")
```

```{code-cell} ipython3
# Durchschnittspreis aller Tracks
query_db("SELECT AVG(UnitPrice) FROM tracks")
```

```{code-cell} ipython3
# Minimaler und maximaler Preis
query_db("SELECT MIN(UnitPrice), MAX(UnitPrice) FROM tracks")
```

### Beispiel 19: COUNT mit und ohne NULL

```{code-cell} ipython3
# COUNT(*) zählt alle Zeilen
query_db("SELECT COUNT(*) FROM tracks")
```

```{code-cell} ipython3
# COUNT(spalte) zählt nur Nicht-NULL-Werte
query_db("SELECT COUNT(Composer) FROM tracks")
```

Es gibt 3503 Tracks, aber nur 2525 haben einen Komponisten eingetragen.

+++

---

### GROUP BY: Gruppierte Auswertungen

+++

Mit `GROUP BY` können Aggregatfunktionen für Gruppen von Daten berechnet werden.

**Syntax:**
```sql
SELECT spalte, AGGREGAT(spalte)
FROM tabelle
GROUP BY spalte;
```

+++

### Beispiel 20: Tracks pro Genre zählen

```{code-cell} ipython3
# Anzahl der Tracks pro Genre
query_db("""
    SELECT genres.Name, COUNT(*) as Anzahl
    FROM tracks
    INNER JOIN genres ON tracks.GenreId = genres.GenreId
    GROUP BY genres.Name
    ORDER BY Anzahl DESC
""")
```

**Erklärung:** Die Abfrage zählt Tracks pro Genre. `GROUP BY genres.Name` gruppiert die Daten, `COUNT(*)` zählt die Einträge pro Gruppe. `ORDER BY Anzahl DESC` sortiert nach Häufigkeit.

+++

### Beispiel 21: Durchschnittswerte pro Gruppe

```{code-cell} ipython3
# Durchschnittliche Tracklänge pro Genre (in Minuten)
query_db("""
    SELECT genres.Name, ROUND(AVG(tracks.Milliseconds) / 60000, 2) as DurchschnittMin
    FROM tracks
    INNER JOIN genres ON tracks.GenreId = genres.GenreId
    GROUP BY genres.Name
    ORDER BY DurchschnittMin DESC
""")
```

### Übung 5.1: Aggregatfunktionen anwenden

**Aufgabe:** Berechnen Sie den Gesamtumsatz (SUM) pro Kunde. Zeigen Sie Vorname, Nachname und Gesamtsumme an, sortiert nach Umsatz absteigend.

**Hinweise:**
- Verknüpfen Sie `customers` und `invoices` über `CustomerId`
- Die Rechnungssumme steht in der Spalte `Total`
- Gruppieren Sie nach Kunde

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung:**

<details>
<summary>Lösung anzeigen</summary>

```python
# Gesamtumsatz pro Kunde
query_db("""
    SELECT customers.FirstName, customers.LastName, SUM(invoices.Total) as Gesamtumsatz
    FROM customers
    INNER JOIN invoices ON customers.CustomerId = invoices.CustomerId
    GROUP BY customers.CustomerId
    ORDER BY Gesamtumsatz DESC
""")
```

**Erklärung:** Der JOIN verbindet Kunden mit ihren Rechnungen. GROUP BY fasst alle Rechnungen eines Kunden zusammen. SUM() addiert die Total-Werte dieser Rechnungen.
</details>

+++

---

### HAVING: Filter für Gruppen

+++

Die `WHERE`-Klausel filtert einzelne Zeilen **vor** der Gruppierung. Um Gruppen nach der Aggregation zu filtern, verwenden Sie `HAVING`.

**Syntax:**
```sql
SELECT spalte, AGGREGAT(spalte)
FROM tabelle
GROUP BY spalte
HAVING bedingung_auf_aggregat;
```

+++

### Beispiel 22: Nur Genres mit mehr als 100 Tracks

```{code-cell} ipython3
# Genres mit mehr als 100 Tracks
query_db("""
    SELECT genres.Name, COUNT(*) as Anzahl
    FROM tracks
    INNER JOIN genres ON tracks.GenreId = genres.GenreId
    GROUP BY genres.Name
    HAVING Anzahl > 100
    ORDER BY Anzahl DESC
""")
```

### Übung 5.2: HAVING anwenden

**Aufgabe:** Finden Sie alle Kunden, die mehr als 40€ Gesamtumsatz haben. Zeigen Sie Name und Gesamtumsatz an.

**Hinweise:**
- Basieren Sie auf der vorherigen Übung
- Fügen Sie eine HAVING-Klausel hinzu

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung:**

<details>
<summary>Lösung anzeigen</summary>

```python
# Kunden mit mehr als 40€ Umsatz
query_db("""
    SELECT customers.FirstName, customers.LastName, SUM(invoices.Total) as Gesamtumsatz
    FROM customers
    INNER JOIN invoices ON customers.CustomerId = invoices.CustomerId
    GROUP BY customers.CustomerId
    HAVING Gesamtumsatz > 40
    ORDER BY Gesamtumsatz DESC
""")
```

**Erklärung:** HAVING filtert die Gruppen nach der Aggregation. Nur Kunden, deren SUM(Total) größer als 40 ist, werden angezeigt.
</details>

+++

---

## Abschlussübungen

Die folgenden Aufgaben testen Ihr Verständnis der in diesem Notebook erlernten Konzepte. Bearbeiten Sie die Aufgaben selbstständig und vergleichen Sie Ihre Lösung anschließend mit den Musterlösungen am Ende des Notebooks.

### Teil 1: Grundlegende Anwendung

**Kompetenzstufe**: Anwenden

Diese Aufgaben testen die direkte Anwendung der erlernten Konzepte.

+++

**Aufgabe 1:** Schreiben Sie eine Abfrage, die alle Kunden aus den USA anzeigt, deren Vorname mit "J" beginnt. Sortieren Sie die Ergebnisse alphabetisch nach Nachname.

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 1
```

**Aufgabe 2:** Zeigen Sie alle Alben an, die von Künstlern stammen, deren Name "The" enthält. Nutzen Sie einen INNER JOIN zwischen `albums` und `artists`. Geben Sie Albumtitel und Künstlername aus.

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 2
```

### Teil 2: Transfer und Problemlösung

**Kompetenzstufe**: Analysieren

Diese Aufgaben erfordern die Kombination mehrerer Konzepte und eigenständiges Problemlösen.

+++

**Aufgabe 3:** Erstellen Sie eine Umsatzanalyse nach Land. Zeigen Sie für jedes Land die Anzahl der Kunden und den durchschnittlichen Umsatz pro Kunde an. Filtern Sie nur Länder mit mindestens 2 Kunden. Sortieren Sie nach durchschnittlichem Umsatz absteigend.

*Tipp: Sie benötigen einen JOIN, GROUP BY und HAVING.*

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 3
```

**Aufgabe 4:** Finden Sie die 5 längsten Tracks pro Genre. Zeigen Sie Genrename, Trackname und Länge in Minuten an. Sortieren Sie innerhalb jedes Genres nach Länge absteigend.

*Tipp: Diese Aufgabe erfordert einen Subquery oder eine kreative Kombination von Konzepten.*

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 4
```

---

## Zusammenfassung

In diesem Notebook haben Sie fortgeschrittene SQL-Techniken für SQLite kennengelernt:

| Konzept | SQL-Syntax | Anwendungsfall |
|---------|------------|----------------|
| Filtern | `WHERE bedingung` | Gezielt Datensätze auswählen |
| Logische Operatoren | `AND`, `OR`, `NOT` | Komplexe Bedingungen formulieren |
| Spezialoperatoren | `BETWEEN`, `IN`, `LIKE` | Bereiche, Listen, Muster abfragen |
| Sortieren | `ORDER BY spalte [ASC\|DESC]` | Ergebnisse ordnen |
| INNER JOIN | `JOIN ... ON ...` | Tabellen über Schlüssel verbinden |
| LEFT JOIN | `LEFT JOIN ... ON ...` | Alle Zeilen der linken Tabelle |
| UPDATE | `UPDATE ... SET ... WHERE` | Daten ändern |
| DELETE | `DELETE FROM ... WHERE` | Daten löschen |
| Aggregatfunktionen | `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` | Zusammenfassungen berechnen |
| Gruppieren | `GROUP BY spalte` | Aggregatfunktionen pro Gruppe |
| Gruppenfilter | `HAVING bedingung` | Gruppen nach Aggregation filtern |

**Zentrale Erkenntnisse**:
- WHERE filtert vor der Gruppierung, HAVING danach
- JOINs verbinden Tabellen und ermöglichen komplexe Abfragen über mehrere Tabellen
- UPDATE und DELETE sind destruktiv – immer WHERE verwenden!
- Aggregatfunktionen ermöglichen statistische Auswertungen direkt in SQL

**Abschluss der Datenbankmodule**: Mit den Notebooks 20-23 haben Sie einen umfassenden Überblick über relationale Datenbanken und deren praktische Anwendung mit Python und SQLite erhalten.

+++

---

## Musterlösungen

<details>
<summary>Lösung zu Aufgabe 1</summary>

```python
# Kunden aus USA mit Vorname beginnend mit J
query_db("""
    SELECT FirstName, LastName, City 
    FROM customers 
    WHERE Country = 'USA' AND FirstName LIKE 'J%'
    ORDER BY LastName ASC
""")
```

**Erklärung**:
- `Country = 'USA'` filtert nach US-Kunden
- `FirstName LIKE 'J%'` findet Vornamen, die mit J beginnen
- `AND` kombiniert beide Bedingungen
- `ORDER BY LastName ASC` sortiert alphabetisch

**Häufige Fehler**:
- LIKE 'J' statt LIKE 'J%' (findet nur genau 'J')
- Vergessen der Anführungszeichen bei Textwerten
</details>

<details>
<summary>Lösung zu Aufgabe 2</summary>

```python
# Alben von Künstlern mit "The" im Namen
query_db("""
    SELECT albums.Title, artists.Name
    FROM albums
    INNER JOIN artists ON albums.ArtistId = artists.ArtistId
    WHERE artists.Name LIKE '%The%'
    ORDER BY artists.Name
""")
```

**Erklärung**:
- INNER JOIN verbindet Alben mit Künstlern
- LIKE '%The%' findet "The" an beliebiger Stelle im Namen
- Die Sortierung nach Künstlername gruppiert Alben desselben Künstlers
</details>

<details>
<summary>Lösung zu Aufgabe 3</summary>

```python
# Umsatzanalyse nach Land
query_db("""
    SELECT 
        customers.Country,
        COUNT(DISTINCT customers.CustomerId) as AnzahlKunden,
        ROUND(AVG(invoices.Total), 2) as DurchschnittUmsatz
    FROM customers
    INNER JOIN invoices ON customers.CustomerId = invoices.CustomerId
    GROUP BY customers.Country
    HAVING AnzahlKunden >= 2
    ORDER BY DurchschnittUmsatz DESC
""")
```

**Erklärung**:
- JOIN verbindet Kunden mit ihren Rechnungen
- COUNT(DISTINCT) zählt eindeutige Kunden pro Land
- AVG berechnet den Durchschnitt der Rechnungen
- HAVING filtert Länder mit weniger als 2 Kunden
- ROUND formatiert auf 2 Dezimalstellen

**Alternative Ansätze**:
- SUM(Total)/COUNT(DISTINCT CustomerId) statt AVG für exakten Durchschnitt pro Kunde
</details>

<details>
<summary>Lösung zu Aufgabe 4</summary>

```python
# Die längsten Tracks pro Genre (vereinfachte Lösung: Top 10 insgesamt)
query_db("""
    SELECT 
        genres.Name as Genre,
        tracks.Name as Track,
        ROUND(tracks.Milliseconds / 60000.0, 2) as Minuten
    FROM tracks
    INNER JOIN genres ON tracks.GenreId = genres.GenreId
    ORDER BY genres.Name, tracks.Milliseconds DESC
""", limit=20)
```

**Erklärung**:
- Diese vereinfachte Lösung sortiert nach Genre und dann nach Länge
- Die Division durch 60000.0 konvertiert Millisekunden in Minuten
- Für exakt die Top 5 pro Genre wäre ein Subquery mit ROW_NUMBER() nötig, was fortgeschrittenes SQL ist

**Fortgeschrittene Lösung mit Subquery** (zur Inspiration):
```python
# Exakt Top 5 pro Genre (komplexer)
query_db("""
    SELECT Genre, Track, Minuten
    FROM (
        SELECT 
            genres.Name as Genre,
            tracks.Name as Track,
            ROUND(tracks.Milliseconds / 60000.0, 2) as Minuten,
            ROW_NUMBER() OVER (PARTITION BY genres.GenreId ORDER BY tracks.Milliseconds DESC) as rn
        FROM tracks
        INNER JOIN genres ON tracks.GenreId = genres.GenreId
    )
    WHERE rn <= 5
    ORDER BY Genre, Minuten DESC
""", limit=50)
```
</details>

+++

---

## Aufräumen

Zum Abschluss entfernen wir eventuelle Testdaten:

```{code-cell} ipython3
# Testdaten aufräumen
execute_db("DELETE FROM artists WHERE Name LIKE 'Test%' OR Name LIKE 'Neuer%' OR Name LIKE '%Lieblingskünstler%' OR Name LIKE 'Übungs%'")
print("Aufräumen abgeschlossen.")
```
