---
title: "21b — ER-Diagramme: Datenmodelle zeichnen"
subtitle: "Entitäten, Attribute, Beziehungen, Kardinalität — Schritt für Schritt"
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

1. Warum erst zeichnen, dann bauen?
2. Die drei Bausteine: Entität, Attribut, Beziehung
3. Schlüsselattribute im ER-Diagramm
4. Kardinalität -- *wie viele* auf jeder Seite? (Krähenfuß-Notation)
5. Ein ERD in vier Schritten -- live am Veggie-Soles-Shop
6. n:m auflösen: die Zwischentabelle
7. Vom ER-Diagramm zur `CREATE TABLE`
8. Häufige Modellierungsfehler

> **Lernziel**: Aus einem fachlichen Sachverhalt ein **ER-Diagramm** entwerfen -- und es in Tabellen übersetzen können.

> **Wie wir heute arbeiten**: viel an der Tafel/am Beamer entwerfen; eine *Live-Demo* zeigt das fertige Modell als Python-Daten; *Selbst überlegen* = Modellierungsaufgaben aus Notebook 21.

---

# Warum erst zeichnen?

- Ein Datenmodell auf Papier zu ändern kostet *Sekunden* -- in einer laufenden Datenbank mit echten Daten kostet es *Tage*.
- Ein Bild macht **Beziehungen und Lücken** sofort sichtbar: „Moment -- woher weiß die Rechnung, zu welcher Bestellung sie gehört?"
- Das ERD ist die **gemeinsame Sprache** zwischen Fachabteilung und Entwicklung -- ohne SQL-Kenntnisse lesbar.

> **Ablauf**: Sachverhalt verstehen → **ER-Diagramm** → Tabellen (`CREATE TABLE`) → Daten. Wir bleiben heute bei den ersten beiden Schritten.

---

# Die drei Bausteine -- und die Notation

![](21b_erd_notation.png){width=84%}

- **Entität** → Tabelle · **Attribut** → Spalte · **Beziehung** → Fremdschlüssel (bei n:m: eine Zwischentabelle). In der **Krähenfuß-Notation** stehen die Attribute *im* Kästchen, **PK** unterstrichen, **FK** kursiv.

---

# Schlüsselattribute im ER-Diagramm

![](21b_erd_schluesselattribut.png){width=76%}

- Jede Entität bekommt **genau einen Primärschlüssel** (oft eine künstliche `…_id`) -- im Diagramm **unterstrichen**.
- Steht derselbe Wert als **Fremdschlüssel** (kursiv) in einer anderen Entität, entsteht eine **Beziehung**.
- Schlechte PK-Kandidaten: Name, E-Mail -- sie ändern sich und sind nicht garantiert eindeutig.

---

# Kardinalität -- wie viele auf jeder Seite?

Jede Beziehung hat **zwei** Kardinalitäten -- eine pro Ende.

| Krähenfuß | Lesart |
|---|---|
| `——||` | genau eins |
| `——o\|` | null oder eins |
| `——\|<` | eins oder viele |
| `——o<` | null oder viele |

- **kunde** `——o<` **bestellung**: eine Kundin hat *0..n* Bestellungen
- **bestellung** `——||` **rechnung**: eine Bestellung hat *genau eine* Rechnung
- Daraus liest man den **Typ** ab: 1:1, 1:n oder n:m.

> Tipp: Frage immer in *beide* Richtungen: „Eine Bestellung gehört zu wie vielen Kundinnen?" und „Eine Kundin hat wie viele Bestellungen?"

---

# Ein ERD in vier Schritten

Wir entwerfen das Veggie-Soles-Datenmodell -- Schritt für Schritt, am Beamer:

1. **Entitäten** finden -- welche Dinge kommen vor?
2. **Attribute & Primärschlüssel** ergänzen
3. **Beziehungen & Kardinalität** einzeichnen
4. **n:m auflösen** -- Zwischentabelle einziehen

> Auf den nächsten vier Folien je ein Schritt -- gross genug zum Mitzeichnen.

---

# Schritt 1 -- Entitäten finden

![](21b_erd_schritt1.png){width=82%}

- Substantive im Sachverhalt → je **eine Entität**: *Kunde* gibt *Bestellungen* auf, eine Bestellung enthält *Produkte*.
- Noch **keine** Attribute, **keine** Linien -- erst die Dinge sammeln.

---

# Schritt 2 -- Attribute & Primärschlüssel

![](21b_erd_schritt2.png){width=82%}

- Was weiß man über jedes Ding? → **Attribute** in das Kästchen.
- Eine Spalte (oder Kombination) identifiziert jede Zeile eindeutig → **Primärschlüssel**, im Diagramm **unterstrichen**.

::: exercisebox
**✎ Selbst überlegen** -- Notebook 21, Übung 1.1: für „Bücher" eine Entität mit Attributen und PK entwerfen.
:::

---

# Schritt 3 -- Beziehungen & Kardinalität

![](21b_erd_schritt3.png){width=82%}

- Welche Entitäten hängen zusammen? **Linie** ziehen, an **beide Enden** die Kardinalität (Krähenfuß).
- `kunde` 1:n `bestellung` ist klar -- der FK `kunde_id` wandert auf die „n"-Seite. `bestellung`/`produkt` ist **n:m** und noch offen.

---

# Schritt 4 -- n:m auflösen: die Zwischentabelle

Eine **Zwischentabelle** mit **zwei Fremdschlüsseln** löst *n:m* in *zwei 1:n*-Beziehungen auf -- mit Platz für Zusatzdaten (`anzahl`, …).

![](21b_erd_zwischentabelle.png){width=58%}

::: exercisebox
**✎ Selbst überlegen** -- Notebook 21, Übung 2.1 + Abschlussübung Aufg. 2 (Shop / Mitarbeiter–Projekte).
:::

---

# Das fertige Veggie-Soles-Modell

![](21b_erd_veggiesoles.png){width=92%}

---

# Das Modell lesen

- **`kunde` 1:n `bestellung`** -- eine Kundin, viele Bestellungen; FK `kunde_id` steht auf der „n"-Seite (in `bestellung`).
- **`bestellung` 1:1 `rechnung`** -- genau eine Rechnung pro Bestellung; FK `bestell_id` in `rechnung` (+ `UNIQUE`).
- **`bestellung` n:m `produkt`** -- aufgelöst über `bestellposition` (zwei FKs, dazu das Attribut `anzahl`).
- Jede Tabelle hat **genau einen PK**; jeder **FK** zeigt auf den PK genau einer anderen Tabelle.

::: demobox
**▶ Live-Demo** -- `01_erd_als_python_modell.py` (das Modell als Listen von Dicts)
:::

---

# Vom ER-Diagramm zur `CREATE TABLE`

| Im ERD | Wird in SQL zu |
|---|---|
| Entität | `CREATE TABLE entitaet (...)` |
| Attribut | Spalte mit Datentyp |
| Schlüsselattribut | `... PRIMARY KEY` |
| 1:n-Beziehung | FK-Spalte auf der „n"-Seite + `FOREIGN KEY ... REFERENCES ...` |
| 1:1-Beziehung | FK + `UNIQUE` auf der FK-Spalte |
| n:m-Beziehung | eigene Tabelle mit zwei FKs (oft zusammengesetzter PK) |

```sql
CREATE TABLE bestellung (
    bestell_id INTEGER PRIMARY KEY,
    kunde_id   INTEGER,
    datum      DATE,
    FOREIGN KEY (kunde_id) REFERENCES kunde(kunde_id)
);
```

---

# Häufige Modellierungsfehler

- **Wiederholgruppen** als Spalten: `produkt1, produkt2, produkt3` -- klarer Fall für eine eigene Tabelle.
- **n:m mit FK auf beiden Seiten** statt Zwischentabelle -- funktioniert nicht.
- **Kein Primärschlüssel** -- dann lässt sich eine Zeile nicht eindeutig ansprechen.
- **Mehrere Werte in einer Zelle** (`"vegan, recycled"`) -- besser eigene Tabelle oder Beziehung.
- **Sprechende Schlüssel** (E-Mail als PK) -- ändert sich irgendwann; lieber künstliche `…_id`.
- **Beziehung vergessen** -- die Rechnung „hängt in der Luft", weil `bestell_id` fehlt.

> Faustregel: Steht dieselbe Information an zwei Stellen, fehlt vermutlich eine Tabelle oder eine Beziehung.

---

# Cheat Card -- ER-Diagramme

| Symbol / Begriff | Bedeutung |
|---|---|
| Rechteck | Entität → Tabelle |
| Oval / Zeile im Kästchen | Attribut → Spalte |
| unterstrichen / `(PK)` | Schlüsselattribut → Primärschlüssel |
| `(FK)` | Fremdschlüssel → Verweis auf einen PK |
| Raute / Verbindungslinie | Beziehung |
| `——\|\|` / `——o<` | „genau eins" / „null oder viele" |
| 1:1 / 1:n / n:m | Beziehungstyp -- n:m → Zwischentabelle |

> **Vier Schritte**: Entitäten → Attribute+PK → Beziehungen+Kardinalität → n:m auflösen.

---

# Ausblick: Notebook 22 -- SQLite

Jetzt bauen wir das Modell wirklich:

```sql
CREATE TABLE kunde (
    kunde_id INTEGER PRIMARY KEY,
    name     TEXT NOT NULL,
    email    TEXT
);
INSERT INTO kunde (name, email) VALUES ('Anna Müller', 'anna@example.de');
SELECT name FROM kunde WHERE email IS NOT NULL;
```

- mit Python und dem `sqlite3`-Modul -- ohne Server, alles in einer Datei
- `CREATE TABLE`, `INSERT`, `SELECT` -- und sichere parametrisierte Abfragen

---

# Heute gelernt

✓ Warum man Datenmodelle erst zeichnet  
✓ Bausteine: Entität, Attribut, Beziehung  
✓ Schlüsselattribute (PK) und Fremdschlüssel im ERD  
✓ Kardinalität in Krähenfuß-Notation  
✓ ERD in vier Schritten entworfen  
✓ n:m über eine Zwischentabelle aufgelöst  
✓ ERD → `CREATE TABLE` übersetzt  

::: exercisebox
**✎ Zur Vertiefung im Notebook 21:**

- Übungen 1.1 & 2.1 -- Entität entwerfen, Beziehungen modellieren
- Abschlussübungen Aufg. 2 & 3: n:m-Schema (Mitarbeiter–Projekte) und vollständiges Schema für ein Ticketsystem
:::
