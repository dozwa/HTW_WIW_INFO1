---
title: "Pandas Visualisierungen Cheat Sheet"
geometry: margin=1.5cm
fontsize: 10pt
header-includes:
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhead[L]{Pandas Visualisierungen Cheat Sheet}
  - \fancyhead[R]{Informatik 1}
  - \fancyfoot[C]{\thepage}
  - \usepackage{listings}
  - \usepackage{xcolor}
  - \lstset{basicstyle=\ttfamily\small, breaklines=true, frame=single, backgroundcolor=\color{gray!10}, aboveskip=4pt, belowskip=4pt}
  - \setlength{\parskip}{2pt}
  - \setlength{\parindent}{0pt}
  - \renewcommand{\arraystretch}{1.1}
---

# Import und Setup

\begin{lstlisting}[language=Python]
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datei.csv')           # CSV laden
df = pd.read_csv('datei.csv', sep=';')  # mit Semikolon
df = pd.read_csv('datei.csv', encoding='utf-8')  # UTF-8 Encoding
\end{lstlisting}

# Grundsyntax

\begin{lstlisting}[language=Python]
df.plot(kind='plottyp', parameter)   # Plot erstellen
plt.show()                            # Plot anzeigen (IMMER!)
\end{lstlisting}

**Wichtig**: `plt.show()` muss IMMER am Ende stehen, sonst wird nichts angezeigt!

# Plot-Typen

| Typ | Syntax | Verwendung |
|-----|--------|------------|
| `line` | `df.plot()` oder `df.plot(kind='line')` | Zeitreihen, Trends, kontinuierliche Daten |
| `bar` | `df.plot(kind='bar')` | Kategorienvergleich (vertikale Balken) |
| `barh` | `df.plot(kind='barh')` | Kategorienvergleich (horizontale Balken) |
| `hist` | `df.plot(kind='hist')` | Verteilung von Werten, Haeufigkeiten |
| `scatter` | `df.plot(kind='scatter')` | Korrelation zwischen zwei Variablen |

# Spaltenauswahl

\begin{lstlisting}[language=Python]
df['spalte'].plot()                  # Einzelne Spalte
df[['sp1', 'sp2']].plot()           # Mehrere Spalten (doppelte Klammern!)
df.plot(x='spalte1', y='spalte2')   # Explizite x/y-Achsen
\end{lstlisting}

**Haeufiger Fehler**: `df['sp1', 'sp2']` funktioniert NICHT! → `df[['sp1', 'sp2']]`

# Universelle Parameter

Diese Parameter funktionieren bei allen Plot-Typen:

| Parameter | Beschreibung | Beispiel |
|-----------|--------------|----------|
| `title` | Titel ueber dem Plot | `title='Umsatz 2024'` |
| `xlabel` | Beschriftung x-Achse | `xlabel='Monat'` |
| `ylabel` | Beschriftung y-Achse | `ylabel='Euro'` |
| `color` | Farbe | `color='green'` |
| `figsize` | Groesse (Breite, Hoehe) | `figsize=(10, 5)` |
| `legend` | Legende anzeigen | `legend=True` / `False` |
| `grid` | Gitternetz anzeigen | `grid=True` |
| `alpha` | Transparenz (0-1) | `alpha=0.7` |
| `rot` | Rotation der Beschriftung | `rot=45` |

# Spezielle Parameter nach Plot-Typ

**Line Plot**:

\begin{lstlisting}[language=Python]
df['Umsatz'].plot(marker='o', linestyle='--')
\end{lstlisting}

- `marker`: Markierung an Datenpunkten (`'o'`, `'x'`, `'s'`, etc.)
- `linestyle`: Linienstil (`'-'`, `'--'`, `'-.'`, `':'`)

**Bar / Barh Plot**:

\begin{lstlisting}[language=Python]
df.plot(kind='bar', x='Kategorie', y='Wert')
\end{lstlisting}

- `x`: Spalte fuer Kategorien (bei `barh` erforderlich)
- `y`: Spalte fuer Werte (bei `barh` erforderlich)

**Histogram**:

\begin{lstlisting}[language=Python]
df['Note'].plot(kind='hist', bins=10)
\end{lstlisting}

- `bins`: Anzahl der Intervalle/Balken

**Scatter Plot**:

\begin{lstlisting}[language=Python]
df.plot(kind='scatter', x='Lernzeit', y='Punkte')
\end{lstlisting}

- `x`: Spalte fuer x-Achse (**ERFORDERLICH**)
- `y`: Spalte fuer y-Achse (**ERFORDERLICH**)

# Komplette Beispiele

**Line Plot - Einzelne Spalte**:

\begin{lstlisting}[language=Python]
df['Umsatz'].plot(
    title='Monatlicher Umsatz',
    xlabel='Monat',
    ylabel='Euro',
    color='green',
    grid=True
)
plt.show()
\end{lstlisting}

**Line Plot - Mehrere Spalten**:

\begin{lstlisting}[language=Python]
df[['Umsatz', 'Kosten']].plot(
    title='Umsatz vs. Kosten',
    figsize=(10, 5),
    grid=True
)
plt.show()
\end{lstlisting}

**Bar Plot - Kategorien**:

\begin{lstlisting}[language=Python]
df.plot(
    kind='bar',
    x='Produkt',
    y='Verkauft',
    title='Verkaeufe nach Produkt',
    color='steelblue',
    legend=False
)
plt.show()
\end{lstlisting}

**Histogram - Verteilung**:

\begin{lstlisting}[language=Python]
df['Alter'].plot(
    kind='hist',
    bins=10,
    title='Altersverteilung',
    xlabel='Alter',
    ylabel='Anzahl Personen'
)
plt.show()
\end{lstlisting}

**Scatter Plot - Korrelation**:

\begin{lstlisting}[language=Python]
df.plot(
    kind='scatter',
    x='Lernstunden',
    y='Note',
    title='Lernzeit vs. Note',
    xlabel='Wochenstunden',
    ylabel='Note',
    figsize=(8, 6)
)
plt.show()
\end{lstlisting}

# Wichtige Regeln

1. **IMMER** `plt.show()` am Ende aufrufen
2. **Doppelte Klammern** bei mehreren Spalten: `df[['sp1', 'sp2']]`
3. **Scatter-Plot**: `x=` und `y=` sind PFLICHT
4. **Achsenbeschriftungen**: Immer `title`, `xlabel`, `ylabel` angeben
5. **Kategorische x-Achse**: Parameter `x='spaltenname'` verwenden
6. **CSV-Probleme**: `sep=';'` und `encoding='utf-8'` probieren

# Haeufige Fehler

| Problem | Loesung |
|---------|---------|
| Plot wird nicht angezeigt | `plt.show()` nicht vergessen! |
| Mehrere Spalten nicht geplottet | `df[['sp1', 'sp2']]` (doppelte Klammern) |
| Scatter-Plot funktioniert nicht | Beide Parameter `x=` und `y=` angeben |
| Kategorische x-Achse wird ignoriert | `x='spaltenname'` Parameter verwenden |
| CSV-Datei nicht gefunden | Pfad pruefen, `try-except` verwenden |
| Umlaute falsch dargestellt | `encoding='utf-8'` beim Laden angeben |
| Semikolon-CSV nicht geladen | `sep=';'` Parameter verwenden |
