# Informatik 1 — HTW Berlin · Wirtschaftsingenieurwesen

Lehrmaterialien für die Vorlesung **Informatik 1** im 1. Semester
des Studiengangs Wirtschaftsingenieurwesen (WIW) an der
[HTW Berlin](https://www.htw-berlin.de). Alle Inhalte sind in deutscher
Sprache, didaktisch auf den WIW-Kontext zugeschnitten und unter
**CC BY-SA 4.0** offen lizenziert.

> **Doppelte Zielgruppe**
> 1. **Studierende** — als Quelle für Vorlesungsbegleitung, Übung und Selbststudium
> 2. **Dozent:innen** — als Vorlage und Baukasten für eigene Programmiereinführungen

---

## Inhalt & Aufbau

26 Jupyter-Notebooks führen vom Einstieg bis zu SQL-Abfragen, in fünf
Phasen organisiert. Die vollständige Themenprogression — inklusive
Notebook-Reihenfolge und einer Tabelle, welche Python-Konzepte bis zu
welchem Notebook eingeführt sind — steht in
[`docs/curriculum.md`](docs/curriculum.md).

Phasen-Kurzüberblick:

1. **Python-Grundlagen** (NB 01–06)
2. **Kontrollfluss** (NB 07–11)
3. **Algorithmen** (NB 12–15)
4. **Datenanalyse** (NB 16–19)
5. **Datenbanken** (NB 20–23)

Ergänzend gibt es Übungsblätter, Cheat Sheets und Beamer-Folien als
PDF-Bauplan.

---

## Für Studierende

### Schnellstart

```bash
git clone https://github.com/dozwa/HTW_WIW_INFO1.git
cd HTW_WIW_INFO1
jupyter lab Notebooks/
```

Die Notebooks sind self-contained: Theorie, Beispielcode und Übungen
sind in einem Dokument verschmolzen. Lösungen liegen aufklappbar in
`<details>`-Blöcken — erst selbst probieren, dann nachsehen.

### Was Sie brauchen

- Python 3.11+
- `pip install pandas matplotlib seaborn jupyterlab`
- (für Datenbank-Notebooks: `sqlite3` ist Teil der Python-Standardbibliothek)

---

## Für Dozent:innen — als Vorlage nutzen

Das Repository ist bewusst so gebaut, dass es als **Baukasten für
eigene Vorlesungen** dient. Sie können den gesamten Kurs forken oder
einzelne Bausteine übernehmen — die Lizenz erlaubt freie Anpassung,
sofern Sie die Quelle nennen und Ihre Änderungen ebenfalls unter
CC BY-SA 4.0 weitergeben.

### Was Sie hier finden — und wiederverwenden können

- **26 Notebooks** als didaktisch durchgegliederte Lerneinheiten
  (Willkommen → Lernziele → Kernkonzepte → Übungen → Musterlösungen)
- **Markdown-Quelltexte** unter [`Notebooks_src/`](Notebooks_src/) für
  einfache Bearbeitung statt JSON-Wrangling (siehe Workflow unten)
- **Übungsblätter** in [`Uebungen_src/`](Uebungen_src/) mit fertigen Pandoc-LaTeX-Headern
- **Cheat Sheets** in [`Cheat_Sheets_src/`](Cheat_Sheets_src/) (Pandas, SQLite)
- **Beamer-Foliensätze** in [`Praesentationen_src/`](Praesentationen_src/) — pro Foliensatz ein eigener Ordner mit `slides.md` und nummerierten Live-Demo-Beispielen (`01_*.py`, `02_*.py`)
- **Story-Welt** in [`docs/story.md`](docs/story.md) — durchgehender Erzählfaden („Veggie Soles" Online-Shop), an dem sich Beispiele in Notebooks, Folien und Demo-Code orientieren
- **Grafik-Generatoren** in [`Grafiken_src/`](Grafiken_src/) — matplotlib-Skripte,
  die alle Diagramme reproduzierbar erzeugen
- **Makefile** als zentrale Build-Pipeline (PDFs + Notebooks + Grafiken)

### Anpassung an Ihren Studiengang

Die didaktische Struktur ist auf **Wirtschaftsingenieurwesen**
optimiert (Praxisszenarien aus Produktion, E-Commerce, Finanzen,
Verwaltung). Für andere Zielgruppen lassen sich die Beispiele
gezielt austauschen — die kanonische Notebook-Struktur ist in
[`docs/notebook_struktur.md`](docs/notebook_struktur.md)
dokumentiert und enthält Richtwerte für Zellenanzahl,
Markdown/Code-Verhältnis und Übungsdichte.

### Fork-Hinweise

1. Repository forken oder als Template verwenden
2. `LICENSE` beibehalten; Ihre eigene Namensnennung im Header
   ergänzen (CC BY-SA 4.0 verlangt Quellenangabe)
3. Inhalte in den `*_src/`-Verzeichnissen anpassen, dann
   `make all` zum Regenerieren aller Outputs
4. Eigene Übungen/Cheat Sheets/Folien im jeweiligen `*_src/`-Verzeichnis
   anlegen — Pandoc baut PDFs ohne weitere Konfiguration

---

## Verzeichnisstruktur

Quellen (`*_src/`) und generierte Outputs sind durchgängig getrennt.
Beides ist im Repo, sodass Studierende die fertigen PDFs und Notebooks
direkt ohne Build-Toolchain nutzen können.

```
HTW_WIW_INFO1/
├── Notebooks_src/          MyST-Markdown-Quellen     →  Notebooks/*.ipynb
├── Notebooks/              Jupyter-Notebooks (Output für Studierende)
├── Uebungen_src/           Übungsblatt-Quellen       →  Uebungen/*.pdf
├── Uebungen/               Übungsblätter als PDF
├── Cheat_Sheets_src/       Cheat-Sheet-Quellen       →  Cheat_Sheets/*.pdf
├── Cheat_Sheets/           Cheat Sheets als PDF
├── Praesentationen_src/    Foliensatz-Ordner (slides.md + .py)  →  Praesentationen/*.pdf
├── Praesentationen/        Beamer-Folien als PDF
├── Grafiken_src/           matplotlib-Skripte        →  Grafiken/*.png
├── Grafiken/               Generierte PNG-Diagramme
├── docs/                   Didaktische Spezifikation + Story-Welt
├── Makefile                Build-Pipeline für alle Outputs
├── README.md               Dieses Dokument
└── LICENSE                 CC BY-SA 4.0
```

---

## Build-Pipeline

Alle Outputs (PDFs, Notebooks, Grafiken) werden zentral über das
`Makefile` reproduzierbar erzeugt.

| Befehl | Was passiert |
|--------|--------------|
| `make all` | Grafiken + alle PDFs bauen |
| `make uebungen` | Alle Übungsblätter als PDF |
| `make cheatsheets` | Alle Cheat Sheets als PDF |
| `make beamer` | Alle Beamer-Foliensätze als PDF |
| `make grafiken` | Alle `Grafiken_src/generate_*.py`-Skripte ausführen |
| `make notebooks` | Notebooks aus `Notebooks_src/*.md` regenerieren |
| `make uebung-03` | Eine einzelne Übung (Treffer auf Nummer im Dateinamen) |
| `make notebook-11` | Ein einzelnes Notebook (Treffer auf Nummer) |
| `make clean` | Alle generierten PDFs löschen |

### Voraussetzungen

- **Pandoc** + **XeLaTeX** für PDF-Generierung
  (`brew install pandoc; brew install --cask mactex` auf macOS)
- **Python 3.11+** mit `matplotlib`, `seaborn`, `pandas`
- **jupytext** als CLI für Notebook-Generierung
  (`brew install pipx && pipx install jupytext`)

---

## Notebook-Source-Workflow

Notebooks werden nicht als JSON gepflegt, sondern aus
[MyST-Markdown](https://myst-parser.readthedocs.io/) generiert. Vorteil:
diff-freundlich, einfach editierbar, reproduzierbar.

```bash
# 1. Markdown-Quelle bearbeiten
$EDITOR Notebooks_src/11_Fehlerbehandlung.md

# 2. Notebook regenerieren
make notebook-11

# 3. In JupyterLab öffnen, "Run All" für frische Outputs
jupyter lab Notebooks/11_Fehlerbehandlung.ipynb
```

Die Markdown-Quelle nutzt die MyST-Syntax mit expliziten
`{code-cell}`-Direktiven für ausführbare Zellen. Plain ` ```python `-Blöcke
in Markdown (z. B. innerhalb `<details>`-Lösungsboxen) bleiben Markdown
und werden nicht versehentlich zu Code-Zellen.

---

## Folien-Workflow

Foliensätze sind themen-spezifisch und liegen in
[`Praesentationen_src/`](Praesentationen_src/). Pro Foliensatz ein
Ordner — die Markdown-Quelle heißt immer `slides.md`, daneben können
nummerierte Python-Dateien für Live-Demos liegen:

```
Praesentationen_src/
  E1_Einfuehrung/                      ← Einleitungs-Foliensätze (E1–E3)
    slides.md                            haben kein Notebook-Pendant
  07_Funktionen/                       ← Themen-Foliensätze
    slides.md                            folgen der Notebook-Numerierung
    01_einfache_funktion.py              und referenzieren ihre Beispiele
    02_versand_berechnen.py              direkt aus dem Foliensatz
```

Bauen mit `make folien-07` (oder `make folien-E1` etc.). Das fertige
PDF landet als `Praesentationen/<Ordnername>.pdf`.

Themen-Foliensätze sind **bewusst keine 1:1-Kopie der Notebooks**:
sie sind knapper, visueller, konzentrieren sich auf Stichpunkte und
Grafiken. Beispiele dürfen vom Notebook abweichen — Konsistenz ergibt
sich über die gemeinsame Story-Welt aus [`docs/story.md`](docs/story.md).

---

## Lizenz

Dieses Werk ist lizenziert unter
**[Creative Commons Namensnennung – Weitergabe unter gleichen Bedingungen 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.de)**.

Sie dürfen die Materialien frei nutzen, verändern und weitergeben —
auch kommerziell. Bedingungen sind die Namensnennung und die
Weitergabe abgeleiteter Werke unter derselben Lizenz. Den vollständigen
Lizenztext finden Sie in der Datei [`LICENSE`](LICENSE).

---

## Autor & Kontakt

**Dorian Zwanzig**
HTW Berlin · Fachbereich Wirtschaftswissenschaften I
[github.com/dozwa](https://github.com/dozwa)

Korrekturvorschläge, Fragen oder Verbesserungsideen sind willkommen —
gerne als Issue oder Pull Request.
