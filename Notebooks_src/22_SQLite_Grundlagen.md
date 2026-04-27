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

# 22 - SQLite Grundlagen: Datenbanken mit Python

## Lernziele

Nach Abschluss dieses Notebooks können Sie:
- SQLite-Datenbanken in Python erstellen und verwalten
- Grundlegende SQL-Befehle (CREATE, INSERT, SELECT) in Python ausführen
- Sichere Parametrisierung zur Vermeidung von SQL-Injection anwenden
- Ergebnisse von Datenbankabfragen in Python-Datenstrukturen verarbeiten

**Kompetenzstufen**: Verstehen, Anwenden, Erschaffen

---

## Voraussetzungen

Für dieses Notebook sollten Sie folgende Konzepte beherrschen:
- Grundlagen relationaler Datenbanken (Notebook 21)
- Python-Funktionen (Notebook 07)
- Fehlerbehandlung mit try-except (Notebook 11)
- Dateiverwaltung (Notebook 12)
- Listen und Dictionaries (Notebook 06)

Falls Sie diese Konzepte noch nicht sicher beherrschen, wiederholen Sie bitte die entsprechenden Notebooks.

---

+++

## Kapitel 1: SQLite und das sqlite3-Modul

### Einführung und Motivation

SQLite ist eine leichtgewichtige, in sich geschlossene SQL-Datenbank-Engine, die direkt in Python integriert ist. Im Gegensatz zu großen Datenbanksystemen wie MySQL oder PostgreSQL benötigt SQLite keinen separaten Server-Prozess. Die gesamte Datenbank wird in einer einzigen Datei gespeichert, was SQLite ideal für kleine bis mittlere Anwendungen, Prototypen und Lehrzwecke macht.

Das Besondere an SQLite ist seine Einfachheit: Sie benötigen keine Installation, keine Konfiguration und keinen Administrator. Trotzdem bietet SQLite fast alle Features einer "großen" relationalen Datenbank. Viele bekannte Anwendungen nutzen SQLite, darunter Firefox, Chrome, Android und iOS.

Python enthält das `sqlite3`-Modul standardmäßig, sodass Sie sofort mit Datenbanken arbeiten können. In diesem Notebook lernen Sie, wie Sie diese mächtige Kombination nutzen, um Daten dauerhaft und strukturiert zu speichern.

+++

### Das sqlite3-Modul importieren

Der erste Schritt ist immer der Import des sqlite3-Moduls. Dies ist ein Standard-Modul in Python, das keine zusätzliche Installation erfordert.

```{code-cell} ipython3
# Import des sqlite3-Moduls
import sqlite3

# Überprüfen der Version
print(f"SQLite Version: {sqlite3.sqlite_version}")
#print(f"Python sqlite3 Modul Version: {sqlite3.version}")
```

### Verbindung zu einer Datenbank herstellen

Eine SQLite-Datenbank ist einfach eine Datei auf Ihrer Festplatte. Wenn die Datei nicht existiert, wird sie automatisch erstellt.

**Syntax:**
```python
connection = sqlite3.connect('datenbankname.db')
```

**Wichtige Parameter:**
- `'datenbankname.db'`: Pfad zur Datenbankdatei
- `':memory:'`: Erstellt eine temporäre Datenbank im Arbeitsspeicher

```{code-cell} ipython3
# Verbindung zu einer Datenbank herstellen
# Die Datei wird erstellt, falls sie nicht existiert
verbindung = sqlite3.connect('meine_erste_db.db')

print("Verbindung zur Datenbank hergestellt!")
print(f"Datenbankdatei: meine_erste_db.db")
```

### Der Cursor - Ihr Werkzeug für SQL-Befehle

Ein **Cursor** ist wie ein Zeiger, der durch die Datenbank navigiert und SQL-Befehle ausführt. Sie benötigen einen Cursor für alle Datenbankoperationen.

**Analogie:** Stellen Sie sich den Cursor wie einen Stift vor, mit dem Sie in die Datenbank schreiben oder aus ihr lesen.

```{code-cell} ipython3
# Einen Cursor erstellen
cursor = verbindung.cursor()

print("Cursor erstellt - bereit für SQL-Befehle!")
print(f"Cursor-Objekt: {cursor}")
```

### Verbindung schließen

**Wichtig**: Datenbankverbindungen sollten immer geschlossen werden, wenn sie nicht mehr benötigt werden. Dies gibt Ressourcen frei und stellt sicher, dass alle Änderungen gespeichert werden.

```{code-cell} ipython3
# Verbindung schließen
verbindung.close()

print("Verbindung geschlossen!")
```

### Übung 1.1: Erste Datenbankverbindung

**Aufgabe**: Erstellen Sie eine Verbindung zu einer Datenbank namens "uebung.db", erstellen Sie einen Cursor und schließen Sie die Verbindung wieder.

**Hinweise**:
- Schritt 1: Importieren Sie sqlite3
- Schritt 2: Verbindung mit `connect()` herstellen
- Schritt 3: Cursor mit `cursor()` erstellen
- Schritt 4: Verbindung mit `close()` schließen

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung:**

<details>
<summary>Lösung anzeigen</summary>

```python
import sqlite3

# Verbindung herstellen
verbindung = sqlite3.connect('uebung.db')
print("Verbindung zu 'uebung.db' hergestellt")

# Cursor erstellen
cursor = verbindung.cursor()
print("Cursor erstellt")

# Verbindung schließen
verbindung.close()
print("Verbindung geschlossen")
```

**Erklärung**: Diese drei Schritte (Verbindung, Cursor, Schließen) sind das Grundgerüst für jede Datenbankoperation.
</details>

+++

---

## Kapitel 2: Tabellen erstellen (CREATE TABLE)

### Einführung in CREATE TABLE

Der SQL-Befehl `CREATE TABLE` erstellt eine neue Tabelle in der Datenbank. Dabei definieren Sie die Struktur der Tabelle: welche Spalten sie hat, welche Datentypen diese Spalten haben und welche Einschränkungen gelten.

In Python führen Sie SQL-Befehle mit der `execute()`-Methode des Cursors aus. Der SQL-Befehl wird als String übergeben. Dies ist die Brücke zwischen Python und SQL - Python steuert die Ausführung, SQL definiert die Operation.

+++

### Syntax und Beispiel

**SQL-Syntax:**
```sql
CREATE TABLE tabellenname (
    spalte1 DATENTYP CONSTRAINTS,
    spalte2 DATENTYP CONSTRAINTS,
    ...
)
```

```{code-cell} ipython3
# Neue Verbindung für dieses Beispiel
verbindung = sqlite3.connect('bibliothek.db')
cursor = verbindung.cursor()

# SQL-Befehl zum Erstellen einer Tabelle
sql_befehl = """
CREATE TABLE buecher (
    id INTEGER PRIMARY KEY,
    titel TEXT NOT NULL,
    autor TEXT NOT NULL,
    jahr INTEGER,
    isbn TEXT UNIQUE
)
"""

# Befehl ausführen
cursor.execute(sql_befehl)

# Änderungen speichern
verbindung.commit()

print("Tabelle 'buecher' wurde erstellt!")
```

### SQLite Datentypen

SQLite hat nur fünf Hauptdatentypen (im Vergleich zu den vielen in Notebook 21):

| SQLite Typ | Beschreibung | Python-Entsprechung |
|------------|--------------|--------------------|
| INTEGER | Ganzzahlen | int |
| REAL | Gleitkommazahlen | float |
| TEXT | Text/Strings | str |
| BLOB | Binärdaten | bytes |
| NULL | Kein Wert | None |

**Hinweis**: SQLite ist typ-flexibel. Es konvertiert automatisch zwischen Typen, wenn möglich.

+++

### Tabelle nur erstellen, wenn sie nicht existiert

Um Fehler zu vermeiden, wenn eine Tabelle bereits existiert, verwenden Sie `IF NOT EXISTS`:

```{code-cell} ipython3
# Sichere Tabellenerstellung mit IF NOT EXISTS
sql_befehl = """
CREATE TABLE IF NOT EXISTS autoren (
    autor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    geburtsjahr INTEGER,
    nationalitaet TEXT
)
"""

cursor.execute(sql_befehl)
verbindung.commit()

print("Tabelle 'autoren' wurde erstellt (falls sie nicht existierte)!")
```

### Übung 2.1: Eigene Tabelle erstellen

**Aufgabe**: Erstellen Sie eine Tabelle "studenten" mit folgenden Spalten:
- matrikelnummer (INTEGER, PRIMARY KEY)
- vorname (TEXT, NOT NULL)
- nachname (TEXT, NOT NULL)
- studiengang (TEXT)
- semester (INTEGER)

**Hinweise**:
- Verwenden Sie CREATE TABLE IF NOT EXISTS
- Vergessen Sie nicht commit()

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung:**

<details>
<summary>Lösung anzeigen</summary>

```python
# Tabelle für Studenten erstellen
sql_befehl = """
CREATE TABLE IF NOT EXISTS studenten (
    matrikelnummer INTEGER PRIMARY KEY,
    vorname TEXT NOT NULL,
    nachname TEXT NOT NULL,
    studiengang TEXT,
    semester INTEGER
)
"""

cursor.execute(sql_befehl)
verbindung.commit()

print("Tabelle 'studenten' wurde erfolgreich erstellt!")
```

**Erklärung**: 
- PRIMARY KEY macht matrikelnummer eindeutig
- NOT NULL erzwingt, dass Vor- und Nachname angegeben werden müssen
- Studiengang und Semester können NULL sein (optional)
</details>

+++

---

## Kapitel 3: Daten einfügen (INSERT)

### Einführung in INSERT

Der `INSERT`-Befehl fügt neue Datensätze in eine Tabelle ein. In Python gibt es zwei Hauptmethoden: direkte Werte im SQL-String oder sichere Parametrisierung. Die Parametrisierung ist **immer** vorzuziehen, da sie vor SQL-Injection-Angriffen schützt.

SQL-Injection ist eine der häufigsten Sicherheitslücken in Webanwendungen. Durch die Verwendung von Parametern statt String-Konkatenation schützen Sie Ihre Anwendung automatisch davor.

+++

### Einzelnen Datensatz einfügen

```{code-cell} ipython3
# Einzelnen Datensatz mit festen Werten einfügen
sql_befehl = """
INSERT INTO buecher (titel, autor, jahr, isbn)
VALUES ('Der Herr der Ringe', 'J.R.R. Tolkien', 1954, '978-3608938289')
"""

cursor.execute(sql_befehl)
verbindung.commit()

print("Buch wurde eingefügt!")
print(f"ID des eingefügten Datensatzes: {cursor.lastrowid}")
```

### Sichere Parametrisierung (WICHTIG!)

**Niemals** Benutzereingaben direkt in SQL-Strings einbauen! Verwenden Sie stattdessen Platzhalter:

```{code-cell} ipython3
# SICHER: Mit Parametern arbeiten
buch_daten = ('1984', 'George Orwell', 1949, '978-3548234106')

sql_befehl = """
INSERT INTO buecher (titel, autor, jahr, isbn)
VALUES (?, ?, ?, ?)
"""

cursor.execute(sql_befehl, buch_daten)
verbindung.commit()

print(f"Buch '{buch_daten[0]}' wurde sicher eingefügt!")
```

### Mehrere Datensätze einfügen

Mit `executemany()` können Sie effizient viele Datensätze auf einmal einfügen:

```{code-cell} ipython3
# Liste von Büchern
buecher_liste = [
    ('Die Verwandlung', 'Franz Kafka', 1915, '978-3150093443'),
    ('Faust', 'Johann Wolfgang von Goethe', 1808, '978-3150000014'),
    ('Das Parfum', 'Patrick Süskind', 1985, '978-3257228007')
]

sql_befehl = "INSERT INTO buecher (titel, autor, jahr, isbn) VALUES (?, ?, ?, ?)"

# executemany für mehrere Datensätze
cursor.executemany(sql_befehl, buecher_liste)
verbindung.commit()

print(f"{cursor.rowcount} Bücher wurden eingefügt!")
```

### Übung 3.1: Daten sicher einfügen

**Aufgabe**: Fügen Sie drei Studenten in Ihre studenten-Tabelle ein. Verwenden Sie parametrisierte Abfragen!

**Hinweise**:
- Erstellen Sie eine Liste mit Tupeln
- Verwenden Sie executemany()
- Verwenden Sie ? als Platzhalter

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung:**

<details>
<summary>Lösung anzeigen</summary>

```python
# Studentendaten vorbereiten
studenten_liste = [
    (100001, 'Anna', 'Schmidt', 'Informatik', 3),
    (100002, 'Max', 'Müller', 'Wirtschaftsinformatik', 2),
    (100003, 'Lisa', 'Weber', 'Data Science', 1)
]

# SQL-Befehl mit Platzhaltern
sql_befehl = """
INSERT INTO studenten (matrikelnummer, vorname, nachname, studiengang, semester)
VALUES (?, ?, ?, ?, ?)
"""

# Mehrere Datensätze einfügen
cursor.executemany(sql_befehl, studenten_liste)
verbindung.commit()

print(f"{len(studenten_liste)} Studenten wurden eingefügt!")
```

**Erklärung**: executemany() ist effizienter als mehrere einzelne execute()-Aufrufe und die Parametrisierung mit ? schützt vor SQL-Injection.
</details>

+++

---

## Kapitel 4: Daten abfragen (SELECT)

### Einführung in SELECT

Der `SELECT`-Befehl ist das Herzstück von SQL. Er ermöglicht es, Daten aus der Datenbank zu lesen und zu filtern. In Python müssen Sie nach dem `execute()` zusätzlich die Ergebnisse abrufen.

Es gibt drei Hauptmethoden, um Ergebnisse zu erhalten:
- `fetchone()`: Gibt eine Zeile zurück
- `fetchall()`: Gibt alle Zeilen zurück
- `fetchmany(n)`: Gibt n Zeilen zurück

Die Wahl der richtigen Methode hängt von der erwarteten Datenmenge ab.

+++

### Alle Daten abrufen

```{code-cell} ipython3
# Alle Bücher abrufen
sql_befehl = "SELECT * FROM buecher"
cursor.execute(sql_befehl)

# Alle Ergebnisse abrufen
alle_buecher = cursor.fetchall()

print("Alle Bücher in der Datenbank:")
print("=" * 50)
for buch in alle_buecher:
    print(f"ID: {buch[0]}, Titel: {buch[1]}, Autor: {buch[2]}, ISBN: {buch[4]}")
```

### Bestimmte Spalten auswählen

```{code-cell} ipython3
# Nur Titel und Autor abrufen
sql_befehl = "SELECT titel, autor FROM buecher"
cursor.execute(sql_befehl)

ergebnisse = cursor.fetchall()

print("Bücherliste (Titel und Autor):")
for titel, autor in ergebnisse:
    print(f"- '{titel}' von {autor}")
```

### Mit WHERE filtern

```{code-cell} ipython3
# Bücher nach einem bestimmten Jahr filtern
jahr_grenze = 1950

sql_befehl = "SELECT titel, jahr FROM buecher WHERE jahr < ?"
cursor.execute(sql_befehl, (jahr_grenze,))

alte_buecher = cursor.fetchall()

print(f"Bücher vor {jahr_grenze}:")
for titel, jahr in alte_buecher:
    print(f"- {titel} ({jahr})")
```

### Einzelnes Ergebnis mit fetchone()

```{code-cell} ipython3
# Ein bestimmtes Buch suchen
sql_befehl = "SELECT * FROM buecher WHERE titel = ?"
cursor.execute(sql_befehl, ('1984',))

# Nur ein Ergebnis abrufen
buch = cursor.fetchone()

if buch:
    print(f"Gefunden: {buch[1]} von {buch[2]} (Jahr: {buch[3]})")
else:
    print("Buch nicht gefunden")
```

### Übung 4.1: Daten filtern und abrufen

**Aufgabe**: Schreiben Sie eine Abfrage, die alle Studenten aus dem Studiengang "Informatik" anzeigt. Geben Sie nur Vor- und Nachname aus.

**Hinweise**:
- Verwenden Sie SELECT mit WHERE
- Nutzen Sie Parametrisierung für den Studiengang
- Verwenden Sie eine Schleife für die Ausgabe

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung:**

<details>
<summary>Lösung anzeigen</summary>

```python
# Studiengang als Parameter
gesuchter_studiengang = 'Informatik'

# SQL-Abfrage mit WHERE-Klausel
sql_befehl = """
SELECT vorname, nachname 
FROM studenten 
WHERE studiengang = ?
"""

cursor.execute(sql_befehl, (gesuchter_studiengang,))
informatik_studenten = cursor.fetchall()

print(f"Studenten im Studiengang {gesuchter_studiengang}:")
print("=" * 40)
for vorname, nachname in informatik_studenten:
    print(f"- {vorname} {nachname}")
    
print(f"\nGesamt: {len(informatik_studenten)} Studenten")
```

**Erklärung**: Die WHERE-Klausel filtert die Ergebnisse. Die Parametrisierung mit ? macht die Abfrage sicher und flexibel.
</details>

+++

---

## Kapitel 5: Praktische Patterns und Best Practices

### Context Manager (with-Statement)

Das `with`-Statement stellt sicher, dass die Datenbankverbindung automatisch geschlossen wird, auch wenn ein Fehler auftritt. Dies ist die empfohlene Methode für Datenbankoperationen.

```{code-cell} ipython3
# Best Practice: Context Manager verwenden
with sqlite3.connect('bibliothek.db') as verbindung:
    cursor = verbindung.cursor()
    
    # Datenbankoperationen
    cursor.execute("SELECT COUNT(*) FROM buecher")
    anzahl = cursor.fetchone()[0]
    print(f"Anzahl Bücher in der Datenbank: {anzahl}")
    
# Verbindung wird automatisch geschlossen
print("Verbindung wurde automatisch geschlossen")
```

### Fehlerbehandlung

```{code-cell} ipython3
# Robuste Fehlerbehandlung
try:
    with sqlite3.connect('bibliothek.db') as verbindung:
        cursor = verbindung.cursor()
        
        # Versuch, ein Duplikat einzufügen (wird fehlschlagen wegen UNIQUE)
        cursor.execute(
            "INSERT INTO buecher (titel, autor, jahr, isbn) VALUES (?, ?, ?, ?)",
            ('Test', 'Test', 2024, '978-3608938289')  # ISBN existiert bereits!
        )
        
except sqlite3.IntegrityError as e:
    print(f"Integritätsfehler: {e}")
    print("Die ISBN existiert bereits!")
    
except sqlite3.Error as e:
    print(f"Datenbankfehler: {e}")
    
else:
    print("Operation erfolgreich!")
```

### Row Factory für Dictionary-Zugriff

Standardmäßig gibt SQLite Tupel zurück. Mit einer Row Factory können Sie die Ergebnisse als Dictionaries erhalten:

```{code-cell} ipython3
# Verbindung mit Row Factory
verbindung = sqlite3.connect('bibliothek.db')
verbindung.row_factory = sqlite3.Row
cursor = verbindung.cursor()

# Abfrage
cursor.execute("SELECT * FROM buecher WHERE jahr > 1980")
buecher = cursor.fetchall()

# Zugriff wie auf ein Dictionary
for buch in buecher:
    print(f"{buch['titel']} ({buch['jahr']}) - ISBN: {buch['isbn']}")

verbindung.close()
```

### Übung 5.1: Komplette Anwendung

**Aufgabe**: Erstellen Sie eine kleine Bibliotheksverwaltung mit folgenden Funktionen:
1. Funktion zum Hinzufügen eines Buches
2. Funktion zum Suchen nach Autor
3. Verwenden Sie Context Manager und Fehlerbehandlung

**Hinweise**:
- Definieren Sie separate Funktionen
- Verwenden Sie with-Statements
- Fügen Sie try-except hinzu

```{code-cell} ipython3
# Ihr Code hier
```

**Musterlösung:**

<details>
<summary>Lösung anzeigen</summary>

```python
def buch_hinzufuegen(titel, autor, jahr, isbn):
    """Fügt ein neues Buch zur Datenbank hinzu"""
    try:
        with sqlite3.connect('bibliothek.db') as verbindung:
            cursor = verbindung.cursor()
            cursor.execute(
                "INSERT INTO buecher (titel, autor, jahr, isbn) VALUES (?, ?, ?, ?)",
                (titel, autor, jahr, isbn)
            )
            print(f"Buch '{titel}' wurde hinzugefügt!")
            return True
            
    except sqlite3.IntegrityError:
        print(f"Fehler: ISBN {isbn} existiert bereits!")
        return False
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        return False


def suche_nach_autor(autor_name):
    """Sucht alle Bücher eines Autors"""
    try:
        with sqlite3.connect('bibliothek.db') as verbindung:
            cursor = verbindung.cursor()
            cursor.execute(
                "SELECT titel, jahr FROM buecher WHERE autor LIKE ?",
                (f"%{autor_name}%",)
            )
            
            buecher = cursor.fetchall()
            
            if buecher:
                print(f"\nBücher von {autor_name}:")
                for titel, jahr in buecher:
                    print(f"  - {titel} ({jahr})")
            else:
                print(f"Keine Bücher von {autor_name} gefunden.")
                
            return buecher
            
    except sqlite3.Error as e:
        print(f"Fehler bei der Suche: {e}")
        return []


# Test der Funktionen
print("=== Bibliotheksverwaltung ===")

# Buch hinzufügen
buch_hinzufuegen(
    "Die unendliche Geschichte",
    "Michael Ende",
    1979,
    "978-3522128001"
)

# Nach Autor suchen
suche_nach_autor("Tolkien")
suche_nach_autor("Ende")
```

**Erklärung**: 
- Jede Funktion hat eine klare Aufgabe
- Context Manager stellt sicheres Schließen sicher
- Fehlerbehandlung macht die Anwendung robust
- LIKE mit % ermöglicht Teilsuchen
</details>

+++

---

## Abschlussübungen

Die folgenden Aufgaben testen Ihr Verständnis der in diesem Notebook erlernten Konzepte. Bearbeiten Sie die Aufgaben selbstständig und vergleichen Sie Ihre Lösung anschließend mit den Musterlösungen am Ende des Notebooks.

### Teil 1: Grundlegende Anwendung

**Kompetenzstufe**: Anwenden

Diese Aufgaben testen die direkte Anwendung der erlernten Konzepte.

+++

**Aufgabe 1**: Erstellen Sie eine Datenbank "firma.db" mit einer Tabelle "mitarbeiter" mit den Spalten:
- id (INTEGER PRIMARY KEY AUTOINCREMENT)
- name (TEXT NOT NULL)
- abteilung (TEXT)
- gehalt (REAL)

Fügen Sie mindestens 3 Mitarbeiter ein.

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 1
```

**Aufgabe 2**: Schreiben Sie eine Funktion `get_high_earners(min_gehalt)`, die alle Mitarbeiter mit einem Gehalt über dem angegebenen Wert zurückgibt.

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 2
```

### Teil 2: Transfer und Problemlösung

**Kompetenzstufe**: Analysieren & Erschaffen

Diese Aufgaben erfordern die Kombination mehrerer Konzepte und eigenständiges Problemlösen.

+++

**Aufgabe 3**: Erstellen Sie ein kleines Notenverwaltungssystem:
- Tabelle "noten" mit student_id, fach, note, datum
- Funktion zum Eintragen einer Note
- Funktion zur Berechnung des Durchschnitts eines Studenten
- Fehlerbehandlung für ungültige Noten (nur 1.0 bis 5.0)

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 3
```

**Aufgabe 4**: Entwickeln Sie eine Funktion `backup_table(tabelle, backup_name)`, die:
- Eine komplette Tabelle in eine neue Tabelle kopiert
- Das aktuelle Datum an den backup_name anhängt
- Prüft, ob die Backup-Tabelle bereits existiert

```{code-cell} ipython3
# Arbeitsbereich für Aufgabe 4
```

---

## Zusammenfassung

In diesem Notebook haben Sie die Grundlagen von SQLite mit Python kennengelernt:

| Konzept | Python-Code | Beschreibung |
|---------|-------------|-------------|
| Verbindung | `sqlite3.connect()` | Öffnet/erstellt Datenbank |
| Cursor | `connection.cursor()` | Werkzeug für SQL-Befehle |
| CREATE TABLE | `cursor.execute("CREATE TABLE...")` | Tabelle erstellen |
| INSERT | `cursor.execute("INSERT...", data)` | Daten einfügen |
| SELECT | `cursor.execute("SELECT...")` + `fetch*()` | Daten abfragen |
| Parametrisierung | `?` Platzhalter | Schutz vor SQL-Injection |
| Context Manager | `with sqlite3.connect()` | Automatisches Schließen |

**Zentrale Erkenntnisse**:
- SQLite ist perfekt für kleine bis mittlere Anwendungen
- Immer parametrisierte Abfragen für Sicherheit verwenden
- Context Manager und Fehlerbehandlung machen Code robust
- Python und SQL ergänzen sich perfekt für Datenmanagement

**Nächste Schritte**: Im folgenden Notebook (23 - SQLite Vertiefung) werden Sie fortgeschrittene Techniken wie UPDATE, DELETE, JOINs und Aggregatfunktionen kennenlernen.

+++

---

## Musterlösungen

<details>
<summary>Lösung zu Aufgabe 1</summary>

```python
import sqlite3

# Datenbank und Tabelle erstellen
with sqlite3.connect('firma.db') as verbindung:
    cursor = verbindung.cursor()
    
    # Tabelle erstellen
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mitarbeiter (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        abteilung TEXT,
        gehalt REAL
    )
    """)
    
    # Mitarbeiter einfügen
    mitarbeiter_daten = [
        ('Max Mustermann', 'IT', 55000.0),
        ('Anna Schmidt', 'Personal', 48000.0),
        ('Tom Weber', 'Vertrieb', 62000.0),
        ('Lisa Müller', 'IT', 58000.0)
    ]
    
    cursor.executemany(
        "INSERT INTO mitarbeiter (name, abteilung, gehalt) VALUES (?, ?, ?)",
        mitarbeiter_daten
    )
    
    print(f"{len(mitarbeiter_daten)} Mitarbeiter wurden eingefügt!")
    
    # Kontrolle
    cursor.execute("SELECT * FROM mitarbeiter")
    for mitarbeiter in cursor.fetchall():
        print(mitarbeiter)
```
</details>

<details>
<summary>Lösung zu Aufgabe 2</summary>

```python
def get_high_earners(min_gehalt):
    """Gibt alle Mitarbeiter mit Gehalt über min_gehalt zurück"""
    try:
        with sqlite3.connect('firma.db') as verbindung:
            cursor = verbindung.cursor()
            
            cursor.execute(
                "SELECT name, abteilung, gehalt FROM mitarbeiter WHERE gehalt > ?",
                (min_gehalt,)
            )
            
            high_earners = cursor.fetchall()
            
            if high_earners:
                print(f"\nMitarbeiter mit Gehalt über {min_gehalt}€:")
                print("=" * 50)
                for name, abteilung, gehalt in high_earners:
                    print(f"{name:20} | {abteilung:10} | {gehalt:,.2f}€")
            else:
                print(f"Keine Mitarbeiter mit Gehalt über {min_gehalt}€ gefunden.")
                
            return high_earners
            
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        return []

# Test
get_high_earners(50000)
get_high_earners(60000)
```
</details>

<details>
<summary>Lösung zu Aufgabe 3</summary>

```python
import sqlite3
from datetime import datetime

# Datenbank einrichten
def setup_noten_db():
    with sqlite3.connect('noten.db') as verbindung:
        cursor = verbindung.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS noten (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            fach TEXT NOT NULL,
            note REAL NOT NULL,
            datum TEXT NOT NULL
        )
        """)

def note_eintragen(student_id, fach, note):
    """Trägt eine Note für einen Studenten ein"""
    # Validierung der Note
    if not 1.0 <= note <= 5.0:
        print(f"Fehler: Note {note} ist ungültig! Nur 1.0 bis 5.0 erlaubt.")
        return False
    
    try:
        with sqlite3.connect('noten.db') as verbindung:
            cursor = verbindung.cursor()
            
            datum = datetime.now().strftime('%Y-%m-%d')
            
            cursor.execute(
                "INSERT INTO noten (student_id, fach, note, datum) VALUES (?, ?, ?, ?)",
                (student_id, fach, note, datum)
            )
            
            print(f"Note {note} für Student {student_id} in {fach} eingetragen.")
            return True
            
    except sqlite3.Error as e:
        print(f"Fehler beim Eintragen: {e}")
        return False

def durchschnitt_berechnen(student_id):
    """Berechnet den Notendurchschnitt eines Studenten"""
    try:
        with sqlite3.connect('noten.db') as verbindung:
            cursor = verbindung.cursor()
            
            cursor.execute(
                "SELECT AVG(note) FROM noten WHERE student_id = ?",
                (student_id,)
            )
            
            durchschnitt = cursor.fetchone()[0]
            
            if durchschnitt:
                print(f"\nNotendurchschnitt für Student {student_id}: {durchschnitt:.2f}")
                
                # Alle Noten anzeigen
                cursor.execute(
                    "SELECT fach, note, datum FROM noten WHERE student_id = ?",
                    (student_id,)
                )
                
                noten = cursor.fetchall()
                print("\nEinzelne Noten:")
                for fach, note, datum in noten:
                    print(f"  {fach:20} | {note:.1f} | {datum}")
            else:
                print(f"Keine Noten für Student {student_id} gefunden.")
                
            return durchschnitt
            
    except sqlite3.Error as e:
        print(f"Fehler bei Berechnung: {e}")
        return None

# Test
setup_noten_db()

# Noten eintragen
note_eintragen(100001, "Mathematik", 2.3)
note_eintragen(100001, "Informatik", 1.7)
note_eintragen(100001, "Physik", 2.0)
note_eintragen(100001, "Ungültig", 6.0)  # Fehler!

# Durchschnitt berechnen
durchschnitt_berechnen(100001)
```
</details>

<details>
<summary>Lösung zu Aufgabe 4</summary>

```python
import sqlite3
from datetime import datetime

def backup_table(db_name, tabelle, backup_name):
    """Erstellt ein Backup einer Tabelle mit Zeitstempel"""
    
    # Backup-Name mit Datum erstellen
    datum = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_tabelle = f"{backup_name}_{datum}"
    
    try:
        with sqlite3.connect(db_name) as verbindung:
            cursor = verbindung.cursor()
            
            # Prüfen, ob Originaltabelle existiert
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
                (tabelle,)
            )
            
            if not cursor.fetchone():
                print(f"Fehler: Tabelle '{tabelle}' existiert nicht!")
                return False
            
            # Prüfen, ob Backup bereits existiert (sollte nicht, wegen Zeitstempel)
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
                (backup_tabelle,)
            )
            
            if cursor.fetchone():
                print(f"Warnung: Backup '{backup_tabelle}' existiert bereits!")
                return False
            
            # Tabellenstruktur kopieren
            cursor.execute(f"CREATE TABLE {backup_tabelle} AS SELECT * FROM {tabelle}")
            
            # Anzahl kopierter Zeilen ermitteln
            cursor.execute(f"SELECT COUNT(*) FROM {backup_tabelle}")
            anzahl = cursor.fetchone()[0]
            
            print(f"Backup erfolgreich erstellt!")
            print(f"  Original: {tabelle}")
            print(f"  Backup: {backup_tabelle}")
            print(f"  Kopierte Zeilen: {anzahl}")
            
            return True
            
    except sqlite3.Error as e:
        print(f"Fehler beim Backup: {e}")
        return False

# Test mit der bibliothek.db
backup_table('bibliothek.db', 'buecher', 'buecher_backup')

# Verifizierung
with sqlite3.connect('bibliothek.db') as verbindung:
    cursor = verbindung.cursor()
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'buecher_backup%'"
    )
    backups = cursor.fetchall()
    print("\nVorhandene Backups:")
    for backup in backups:
        print(f"  - {backup[0]}")
```
</details>

+++

---

## Aufräumen

Zum Abschluss schließen wir alle Verbindungen:

```{code-cell} ipython3
# Alle Datenbankverbindungen schließen
try:
    verbindung.close()
    print("Alle Verbindungen geschlossen.")
except:
    print("Verbindungen bereits geschlossen.")
```
