# Informatik 1 — HTW Berlin · Wirtschaftsingenieurwesen

Lehrmaterialien für die Vorlesung **Informatik 1** im 1. Semester des
Studiengangs Wirtschaftsingenieurwesen (WIW) an der
[HTW Berlin](https://www.htw-berlin.de). Alle Inhalte sind in deutscher
Sprache, didaktisch auf den WIW-Kontext zugeschnitten und unter
**CC BY-SA 4.0** offen lizenziert.

Dieses Repository ist für **Studierende** gedacht: Es enthält die fertigen
Lernmaterialien zum direkten Verwenden — ohne Build-Werkzeuge, ohne
Generierungs-Schritte.

---

## Inhalt & Aufbau

26 Jupyter-Notebooks führen vom Einstieg bis zu SQL-Abfragen, in fünf
Phasen organisiert:

1. **Python-Grundlagen** (NB 01–06)
2. **Kontrollfluss** (NB 07–11)
3. **Algorithmen** (NB 12–15)
4. **Datenanalyse** (NB 16–19)
5. **Datenbanken** (NB 20–23)

Ergänzend gibt es **Übungsblätter**, **Cheat Sheets** und **Vorlesungsfolien**
als PDF.

---

## Schnellstart

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
- (für die Datenbank-Notebooks: `sqlite3` ist Teil der Python-Standardbibliothek)

---

## Verzeichnisstruktur

```
HTW_WIW_INFO1/
├── Notebooks/         Jupyter-Notebooks (.ipynb) — das Herzstück
├── Uebungen/          Übungsblätter als PDF
├── Cheat_Sheets/      Cheat Sheets als PDF (Pandas, SQLite)
├── Praesentationen/   Vorlesungsfolien als PDF
├── Grafiken/          Diagramme (PNG), in Notebooks und Folien eingebettet
├── README.md          Dieses Dokument
└── LICENSE            CC BY-SA 4.0
```

---

## Für Lehrende

Dieses Repository enthält bewusst nur die fertigen Materialien. Die
Quelldateien und die Build-Pipeline (Markdown-Quellen, Generatoren,
Makefile, didaktische Spezifikationen) sind hier nicht enthalten.

Wenn Sie die Materialien als Baukasten für eine eigene
Programmiereinführung nutzen möchten, stelle ich Ihnen die Basisdateien
gerne bereit — die Lizenz (CC BY-SA 4.0) erlaubt freie Anpassung und
Weitergabe unter Namensnennung. Melden Sie sich einfach
([Kontakt](mailto:kontakt@dorianzwanzig.de)).

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
HTW Berlin - HWR Berlin - HNE Eberswalde
[github.com/dozwa](https://github.com/dozwa)

Korrekturvorschläge, Fragen oder Verbesserungsideen sind willkommen —
gerne als Issue oder Pull Request.
