---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
kernelspec:
  display_name: base
  language: python
  name: python3
---

# 15 – Python-Programme: Vom Skript zum strukturierten Programm 🏗️

+++

## Willkommen! 👋

Herzlich willkommen zu Notebook 15! Heute lernen Sie, wie man aus einzelnen Code-Schnipseln ein **richtiges Python-Programm** macht.

Stellen Sie sich den Unterschied zwischen einem Zettelkasten und einem **Bauplan** vor: Bisher haben Sie einzelne Konzepte wie Variablen, Funktionen, Schleifen und Fehlerbehandlung kennengelernt – wie einzelne Zimmer eines Hauses. Heute lernen Sie, wie man einen **Grundriss** zeichnet, der all diese Zimmer zu einem funktionierenden Gebäude zusammenfügt.

In diesem Notebook arbeiten wir mit Jupyter-Zellen, aber wir lernen dabei die Struktur, die Sie für **echte `.py`-Programme** brauchen. Denn in der Praxis schreibt man Python-Programme als `.py`-Dateien – und die brauchen eine klare Struktur.

+++

## Was Sie heute lernen:
- 📐 **Warum Programmstruktur wichtig ist** und was den Unterschied zwischen einem Skript und einem Programm ausmacht
- 🧱 **Wie Sie Programme aus mehreren Funktionen aufbauen** – jede Funktion hat eine Aufgabe
- 🎯 **Was die `main()`-Funktion ist** und wie sie den Programmablauf steuert
- 🔑 **Was `if __name__ == "__main__":` bedeutet** und warum es in jedes Programm gehört
- 📋 **Wie eine ideale `.py`-Datei aufgebaut ist** (Imports → Konstanten → Funktionen → main)
- 💻 **Den Unterschied zwischen Notebook und `.py`-Datei** und wann man was nutzt

## Voraussetzungen 📚
Was Sie bereits können sollten:
- ✅ Variablen und Datentypen verwenden (Notebooks 04–05)
- ✅ Mit Listen und Dictionaries arbeiten (Notebook 06)
- ✅ Eigene Funktionen definieren und aufrufen (Notebook 07)
- ✅ Operatoren anwenden (Notebook 08)
- ✅ Verzweigungen mit if/elif/else schreiben (Notebook 09)
- ✅ Schleifen mit for und while nutzen (Notebook 10)
- ✅ Fehler mit try/except abfangen (Notebook 11)
- ✅ Dateien lesen und schreiben (Notebook 12)

+++

---
## 1️⃣ Vom Skript zum Programm

### Das Problem: Spaghetti-Code

Bisher haben Sie Code oft so geschrieben: Eine Anweisung nach der anderen, alles direkt hintereinander. Das funktioniert für kleine Übungen – aber stellen Sie sich vor, Sie sollen ein **Lagerverwaltungsprogramm** für ein kleines Unternehmen schreiben.

So könnte ein erster Versuch aussehen:

```{code-cell} ipython3
# ❌ So bitte NICHT: Alles lose hintereinander ("Spaghetti-Code")

lager = {
    "Schrauben M8": 150,
    "Muttern M8": 200,
    "Unterlegscheiben M8": 300,
    "Schrauben M10": 75,
    "Dübel 8mm": 500
}

print("=== Lagerverwaltung ===")
print("\nAktueller Bestand:")
for produkt, menge in lager.items():
    print(f"  {produkt}: {menge} Stück")

gesamt = 0
for menge in lager.values():
    gesamt = gesamt + menge
print(f"\nGesamtbestand: {gesamt} Teile")

print("\nArtikel mit niedrigem Bestand (unter 100):")
for produkt, menge in lager.items():
    if menge < 100:
        print(f"  ⚠️ {produkt}: nur noch {menge} Stück!")

neues_produkt = "Bolzen M12"
neue_menge = 50
lager[neues_produkt] = neue_menge
print(f"\n✅ '{neues_produkt}' mit {neue_menge} Stück hinzugefügt.")

print(f"\nAnzahl verschiedener Artikel: {len(lager)}")
```

Dieser Code funktioniert – aber er hat **gravierende Probleme**:

| Problem | Warum ist das schlecht? |
|---------|------------------------|
| Alles auf einer Ebene | Man erkennt nicht sofort, was der Code tut |
| Keine Wiederverwendbarkeit | Will man den Bestand nochmal anzeigen, muss man den Code kopieren |
| Schwer zu testen | Man kann nicht einzelne Teile isoliert prüfen |
| Schwer zu erweitern | Neue Funktionen einzubauen erfordert Umbau des gesamten Codes |
| Nicht importierbar | Andere Programme können diesen Code nicht nutzen |

> 💡 **Faustregel:** Wenn Ihr Skript länger als ~20 Zeilen wird, braucht es Struktur!

+++

### Die Lösung: Strukturiertes Programm

Das gleiche Programm, aber **richtig strukturiert**:

```{code-cell} ipython3
# ✅ So ist es besser: Strukturiert mit Funktionen

def bestand_anzeigen(lager):
    """Zeigt den aktuellen Lagerbestand an."""
    print("\nAktueller Bestand:")
    for produkt, menge in lager.items():
        print(f"  {produkt}: {menge} Stück")


def gesamtbestand_berechnen(lager):
    """Berechnet die Gesamtanzahl aller Teile im Lager."""
    gesamt = 0
    for menge in lager.values():
        gesamt = gesamt + menge
    return gesamt


def niedrigen_bestand_warnen(lager, grenzwert=100):
    """Warnt bei Artikeln unter dem Grenzwert."""
    print(f"\nArtikel mit niedrigem Bestand (unter {grenzwert}):")
    for produkt, menge in lager.items():
        if menge < grenzwert:
            print(f"  ⚠️ {produkt}: nur noch {menge} Stück!")


def produkt_hinzufuegen(lager, name, menge):
    """Fügt ein neues Produkt zum Lager hinzu."""
    lager[name] = menge
    print(f"\n✅ '{name}' mit {menge} Stück hinzugefügt.")


# --- Hauptprogramm ---
lager = {
    "Schrauben M8": 150,
    "Muttern M8": 200,
    "Unterlegscheiben M8": 300,
    "Schrauben M10": 75,
    "Dübel 8mm": 500
}

print("=== Lagerverwaltung ===")
bestand_anzeigen(lager)
print(f"\nGesamtbestand: {gesamtbestand_berechnen(lager)} Teile")
niedrigen_bestand_warnen(lager)
produkt_hinzufuegen(lager, "Bolzen M12", 50)
print(f"\nAnzahl verschiedener Artikel: {len(lager)}")
```

**Was hat sich verbessert?**

- Jede Funktion hat **genau eine Aufgabe** (Single Responsibility)
- Die Funktionsnamen sagen sofort, was passiert
- Man kann jede Funktion **einzeln testen** und **wiederverwenden**
- Das Hauptprogramm ist nur noch 6 Zeilen lang und liest sich wie eine Anleitung

> 🤔 **Reflexionsfrage:** Stellen Sie sich vor, der Chef möchte jetzt auch eine Funktion zum Entfernen von Produkten. Wo ist das einfacher einzubauen – im Spaghetti-Code oder im strukturierten Programm?

+++

### 🏃 Übung 1.1: Unstrukturierten Code erkennen

**Aufgabe:** Schauen Sie sich den folgenden Code an. Identifizieren Sie **drei verschiedene Aufgaben**, die jeweils eine eigene Funktion sein sollten. Schreiben Sie die Funktionsnamen als Kommentare in die Zelle darunter.

```{code-cell} ipython3
# Unstrukturierter Code – welche Funktionen stecken darin?

noten = [1.3, 2.7, 1.0, 3.3, 2.0, 1.7, 4.0, 2.3]

summe = 0
for note in noten:
    summe = summe + note
durchschnitt = summe / len(noten)
print(f"Durchschnitt: {durchschnitt:.2f}")

beste = noten[0]
for note in noten:
    if note < beste:
        beste = note
print(f"Beste Note: {beste}")

bestanden = 0
for note in noten:
    if note <= 4.0:
        bestanden = bestanden + 1
print(f"Bestanden: {bestanden} von {len(noten)}")
```

```{code-cell} ipython3
# Hier Ihre Antwort: Welche drei Funktionen sollte man daraus machen?
# Funktion 1: ...
# Funktion 2: ...
# Funktion 3: ...
```

<details>
<summary>🔍 Lösung anzeigen</summary>

Die drei Aufgaben sind:

1. **`durchschnitt_berechnen(noten)`** – Berechnet den Durchschnitt einer Notenliste
2. **`beste_note_finden(noten)`** – Findet die beste (niedrigste) Note
3. **`bestanden_zaehlen(noten)`** – Zählt, wie viele Noten bestanden sind (≤ 4.0)

Jede Aufgabe ist klar abgrenzbar und sollte eine eigene Funktion sein.
</details>

+++

---
## 2️⃣ Funktionen als Bausteine

### Wiederholung: Funktionen definieren (Kurzreferenz)

Aus Notebook 07 kennen Sie bereits die Grundlagen:

```python
def funktionsname(parameter1, parameter2):
    """Beschreibung der Funktion."""
    # Code der Funktion
    return ergebnis
```

Heute konzentrieren wir uns darauf, wie mehrere Funktionen **zusammenspielen**.

+++

### Prinzip: Jede Funktion hat EINE Aufgabe

Eine gut geschriebene Funktion tut **genau eine Sache**. Wenn Sie beschreiben müssen, was eine Funktion tut, und dabei das Wort **"und"** verwenden – dann sollte es wahrscheinlich zwei Funktionen sein.

| ❌ Schlecht | ✅ Besser |
|-------------|----------|
| `daten_laden_und_verarbeiten()` | `daten_laden()` + `daten_verarbeiten()` |
| `berechne_und_zeige_ergebnis()` | `ergebnis_berechnen()` + `ergebnis_anzeigen()` |
| `eingabe_pruefen_und_speichern()` | `eingabe_pruefen()` + `eingabe_speichern()` |

+++

### Funktionen rufen andere Funktionen auf

In einem echten Programm rufen Funktionen **andere Funktionen** auf. Das ist völlig normal und gewollt! Schauen wir uns das am Lagerverwaltungs-Beispiel an:

```{code-cell} ipython3
def lagerbericht_erstellen(lager):
    """Erstellt einen vollständigen Lagerbericht.
    Ruft dafür mehrere andere Funktionen auf."""
    print("=" * 40)
    print("       LAGERBERICHT")
    print("=" * 40)
    
    # Andere Funktionen aufrufen
    bestand_anzeigen(lager)
    gesamt = gesamtbestand_berechnen(lager)
    print(f"\nGesamtbestand: {gesamt} Teile")
    print(f"Verschiedene Artikel: {len(lager)}")
    niedrigen_bestand_warnen(lager)
    
    print("\n" + "=" * 40)

# Die Funktionen von oben sind noch definiert – wir können sie nutzen!
lager = {
    "Schrauben M8": 150,
    "Muttern M8": 200,
    "Unterlegscheiben M8": 300,
    "Schrauben M10": 75,
    "Dübel 8mm": 500
}

lagerbericht_erstellen(lager)
```

`lagerbericht_erstellen()` muss nicht wissen, **wie** der Bestand angezeigt wird – sie sagt nur: "Zeig den Bestand an!" Die Details stecken in `bestand_anzeigen()`. Das nennt man **Abstraktion**.

+++

### 🏃 Übung 2.1: Programm in Funktionen zerlegen

**Aufgabe:** Schreiben Sie die drei Funktionen aus Übung 1.1 (`durchschnitt_berechnen`, `beste_note_finden`, `bestanden_zaehlen`). Jede Funktion nimmt eine Liste von Noten entgegen und gibt das Ergebnis zurück.

```{code-cell} ipython3
def durchschnitt_berechnen(noten):
    """Berechnet den Durchschnitt einer Notenliste."""
    # Ihr Code hier
    pass


def beste_note_finden(noten):
    """Findet die beste (niedrigste) Note."""
    # Ihr Code hier
    pass


def bestanden_zaehlen(noten):
    """Zählt die Anzahl bestandener Prüfungen (Note <= 4.0)."""
    # Ihr Code hier
    pass


# Test
test_noten = [1.3, 2.7, 1.0, 3.3, 2.0, 1.7, 4.0, 2.3]
print(f"Durchschnitt: {durchschnitt_berechnen(test_noten)}")
print(f"Beste Note: {beste_note_finden(test_noten)}")
print(f"Bestanden: {bestanden_zaehlen(test_noten)} von {len(test_noten)}")
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
def durchschnitt_berechnen(noten):
    """Berechnet den Durchschnitt einer Notenliste."""
    summe = 0
    for note in noten:
        summe = summe + note
    return summe / len(noten)


def beste_note_finden(noten):
    """Findet die beste (niedrigste) Note."""
    beste = noten[0]
    for note in noten:
        if note < beste:
            beste = note
    return beste


def bestanden_zaehlen(noten):
    """Zählt die Anzahl bestandener Prüfungen (Note <= 4.0)."""
    bestanden = 0
    for note in noten:
        if note <= 4.0:
            bestanden = bestanden + 1
    return bestanden
```

**Erklärung:** Jede Funktion hat genau eine Aufgabe, nimmt `noten` als Parameter und gibt mit `return` das Ergebnis zurück – statt es direkt auszugeben. So kann der Aufrufer selbst entscheiden, was er mit dem Ergebnis macht.
</details>

+++

### 🏃 Übung 2.2: Funktionen kombinieren

**Aufgabe:** Schreiben Sie eine Funktion `notenbericht_erstellen(noten)`, die alle drei Funktionen aus Übung 2.1 aufruft und einen formatierten Bericht ausgibt.

```{code-cell} ipython3
def notenbericht_erstellen(noten):
    """Erstellt einen vollständigen Notenbericht."""
    # Ihr Code hier – nutzen Sie die drei Funktionen von oben!
    pass


# Test
test_noten = [1.3, 2.7, 1.0, 3.3, 2.0, 1.7, 4.0, 2.3]
notenbericht_erstellen(test_noten)
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
def notenbericht_erstellen(noten):
    """Erstellt einen vollständigen Notenbericht."""
    print("=== Notenbericht ===")
    print(f"Anzahl Prüfungen: {len(noten)}")
    print(f"Durchschnitt: {durchschnitt_berechnen(noten):.2f}")
    print(f"Beste Note: {beste_note_finden(noten)}")
    print(f"Bestanden: {bestanden_zaehlen(noten)} von {len(noten)}")
```

**Erklärung:** `notenbericht_erstellen()` muss nicht wissen, *wie* der Durchschnitt berechnet wird. Sie ruft einfach die passende Funktion auf. So bleibt jede Funktion kurz und verständlich.
</details>

+++

---
## 3️⃣ Die `main()`-Funktion

### Der Orchesterdirigent

Stellen Sie sich ein Orchester vor: Jedes Instrument (Funktion) kann alleine spielen, aber es braucht einen **Dirigenten**, der bestimmt, wer wann spielt. In einem Python-Programm ist die `main()`-Funktion dieser Dirigent.

Die `main()`-Funktion:
- **Steuert den Ablauf** des Programms
- **Ruft andere Funktionen** in der richtigen Reihenfolge auf
- Enthält **selbst wenig Logik** – die steckt in den Hilfsfunktionen

+++

### Vom losen Code zur `main()`-Funktion

Schauen wir uns die Transformation Schritt für Schritt an.

**Vorher:** Der Hauptablauf steht lose im Skript:

```{code-cell} ipython3
# ❌ Vorher: Loser Code
# (Die Funktionen wären hier schon definiert)

lager = {
    "Schrauben M8": 150,
    "Muttern M8": 200,
    "Schrauben M10": 75
}

print("=== Lagerverwaltung ===")
bestand_anzeigen(lager)
gesamt = gesamtbestand_berechnen(lager)
print(f"Gesamtbestand: {gesamt} Teile")
niedrigen_bestand_warnen(lager)
```

**Nachher:** Der Hauptablauf steckt in `main()`:

```{code-cell} ipython3
# ✅ Nachher: In main() verpackt

def main():
    """Hauptprogramm der Lagerverwaltung."""
    lager = {
        "Schrauben M8": 150,
        "Muttern M8": 200,
        "Schrauben M10": 75
    }
    
    print("=== Lagerverwaltung ===")
    bestand_anzeigen(lager)
    gesamt = gesamtbestand_berechnen(lager)
    print(f"Gesamtbestand: {gesamt} Teile")
    niedrigen_bestand_warnen(lager)

# Aufruf
main()
```

### Was gehört in `main()`, was nicht?

| ✅ Gehört in `main()` | ❌ Gehört NICHT in `main()` |
|-----------------------|-----------------------------|
| Programmablauf steuern | Funktionsdefinitionen |
| Hilfsfunktionen aufrufen | Import-Anweisungen |
| Anfangsdaten bereitstellen | Konstanten-Definitionen |
| Benutzereingaben (wenn nötig) | Komplexe Berechnungslogik |
| Ergebnisse ausgeben | Hilfsfunktionen |

> 💡 **Faustregel:** `main()` sollte sich wie eine **kurze Zusammenfassung** Ihres Programms lesen. Wer `main()` liest, versteht sofort, was das Programm tut – ohne sich um Details kümmern zu müssen.

+++

### 🏃 Übung 3.1: Eine `main()`-Funktion schreiben

**Aufgabe:** Schreiben Sie eine `main()`-Funktion, die die Funktionen aus Übung 2.1 nutzt. Das Programm soll:
1. Eine Liste mit mindestens 5 Noten definieren
2. Einen Notenbericht ausgeben
3. Eine passende Nachricht ausgeben ("Glückwunsch!" bei Durchschnitt ≤ 2.5, sonst "Weiter üben!")

```{code-cell} ipython3
def main():
    """Hauptprogramm für die Notenauswertung."""
    # Ihr Code hier
    pass


# Aufruf
main()
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
def main():
    """Hauptprogramm für die Notenauswertung."""
    noten = [1.3, 2.7, 1.0, 3.3, 2.0, 1.7, 4.0, 2.3]
    
    notenbericht_erstellen(noten)
    
    schnitt = durchschnitt_berechnen(noten)
    if schnitt <= 2.5:
        print("\n🎉 Glückwunsch! Guter Durchschnitt!")
    else:
        print("\n📚 Weiter üben!")
```

**Erklärung:** `main()` orchestriert den Ablauf: Noten definieren, Bericht erstellen, Bewertung ausgeben. Die eigentliche Logik steckt in den Hilfsfunktionen.
</details>

+++

### 🏃 Übung 3.2: Bestehendes Skript refaktorisieren

**Aufgabe:** Der folgende Code ist ein typisches Anfänger-Skript. Refaktorisieren Sie es: Erstellen Sie passende Funktionen und eine `main()`-Funktion.

```{code-cell} ipython3
# Diesen Code in Funktionen + main() umbauen:

# temperatur = float(input("Temperatur in Celsius: "))
# fahrenheit = temperatur * 9/5 + 32
# print(f"{temperatur}°C = {fahrenheit}°F")
# if temperatur < 0:
#     print("Achtung: Frostgefahr!")
# elif temperatur > 35:
#     print("Achtung: Hitzegefahr!")
# else:
#     print("Normale Temperatur.")
```

```{code-cell} ipython3
# Ihre Lösung hier:

def celsius_zu_fahrenheit(celsius):
    # Ihr Code hier
    pass


def temperatur_bewerten(celsius):
    # Ihr Code hier
    pass


def main():
    # Ihr Code hier
    pass


main()
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
def celsius_zu_fahrenheit(celsius):
    """Konvertiert Celsius in Fahrenheit."""
    return celsius * 9/5 + 32


def temperatur_bewerten(celsius):
    """Gibt eine Warnung basierend auf der Temperatur aus."""
    if celsius < 0:
        print("Achtung: Frostgefahr!")
    elif celsius > 35:
        print("Achtung: Hitzegefahr!")
    else:
        print("Normale Temperatur.")


def main():
    """Hauptprogramm: Temperaturumrechnung mit Bewertung."""
    temperatur = float(input("Temperatur in Celsius: "))
    fahrenheit = celsius_zu_fahrenheit(temperatur)
    print(f"{temperatur}°C = {fahrenheit}°F")
    temperatur_bewerten(temperatur)


main()
```

**Erklärung:** Die Konvertierung und die Bewertung sind jetzt eigenständige Funktionen. `main()` liest sich wie ein klarer Ablaufplan: Eingabe → Umrechnung → Ausgabe → Bewertung.
</details>

+++

---
## 4️⃣ Das `if __name__ == "__main__":` Idiom

### Was ist `__name__`?

Python hat eine eingebaute Variable namens `__name__`. Diese Variable sagt dem Programm, **wie es gestartet wurde**:

- Wenn Sie eine Datei **direkt ausführen** (`python mein_programm.py`): `__name__` ist `"__main__"`
- Wenn eine Datei **als Modul importiert** wird (`import mein_programm`): `__name__` ist der Dateiname

Schauen wir uns das an:

```{code-cell} ipython3
# Im Notebook ist __name__ immer "__main__"
print(f"__name__ hat den Wert: {__name__}")
print(f"Typ: {type(__name__)}")
```

### Warum braucht man diese Prüfung?

Stellen Sie sich vor, Sie haben eine Datei `lager_utils.py` mit nützlichen Funktionen. Ein Kollege möchte Ihre Funktionen in seinem Programm nutzen:

```python
# Kollege schreibt in seiner Datei:
import lager_utils
```

**Ohne** `if __name__ == "__main__":` würde beim Import sofort das gesamte Hauptprogramm loslaufen – der Kollege bekommt plötzlich Ausgaben und Eingabeaufforderungen, die er gar nicht wollte!

**Mit** der Prüfung passiert beim Import gar nichts – nur die Funktionsdefinitionen werden geladen.

+++

### Skript vs. Modul

| Eigenschaft | Skript (direkt ausgeführt) | Modul (importiert) |
|------------|---------------------------|--------------------|
| `__name__` | `"__main__"` | Dateiname (z. B. `"lager_utils"`) |
| Zweck | Programm starten | Funktionen bereitstellen |
| Beispiel | `python lagerverwaltung.py` | `import lager_utils` |

Das Schöne an Python: Mit `if __name__ == "__main__":` kann **dieselbe Datei beides sein** – Skript und Modul!

+++

### So sieht es in einer `.py`-Datei aus

Hier ein Beispiel, wie `lager_utils.py` in der Praxis aussehen würde:

```python
# lager_utils.py

def bestand_anzeigen(lager):
    """Zeigt den aktuellen Lagerbestand an."""
    for produkt, menge in lager.items():
        print(f"  {produkt}: {menge} Stück")

def gesamtbestand_berechnen(lager):
    """Berechnet die Gesamtanzahl aller Teile."""
    gesamt = 0
    for menge in lager.values():
        gesamt = gesamt + menge
    return gesamt

def main():
    """Demo: Zeigt die Funktionen in Aktion."""
    demo_lager = {"Schrauben": 100, "Muttern": 200}
    bestand_anzeigen(demo_lager)
    print(f"Gesamt: {gesamtbestand_berechnen(demo_lager)}")

if __name__ == "__main__":
    main()
```

- `python lager_utils.py` → Führt `main()` aus (Demo)
- `import lager_utils` → Lädt nur die Funktionen, `main()` wird **nicht** ausgeführt

+++

### Und im Notebook?

Im Jupyter Notebook ist `__name__` **immer** `"__main__"`, weil jede Zelle als Top-Level-Code ausgeführt wird. Die Prüfung wäre also immer wahr. Deshalb können Sie im Notebook `main()` einfach direkt aufrufen:

```python
# Im Notebook: Direkter Aufruf reicht
main()

# In einer .py-Datei würde hier stehen:
# if __name__ == "__main__":
#     main()
```

> 💡 **Merke:** Im Notebook üben wir die Struktur mit direktem `main()`-Aufruf. Wenn Sie den Code in eine `.py`-Datei übertragen, fügen Sie `if __name__ == "__main__":` hinzu.

+++

### 🏃 Übung 4.1: `__name__` untersuchen

**Aufgabe:** Führen Sie die folgende Zelle aus und beantworten Sie die Frage darunter.

```{code-cell} ipython3
# Was gibt diese Zelle aus?
print(f"Wert von __name__: '{__name__}'")

if __name__ == "__main__":
    print("Diese Datei wird direkt ausgeführt!")
else:
    print("Diese Datei wurde importiert!")
```

> 🤔 **Reflexionsfrage:** Warum erscheint im Notebook immer "direkt ausgeführt"? Was müsste anders sein, damit "importiert" erscheint?

+++

<details>
<summary>🔍 Antwort anzeigen</summary>

Im Jupyter Notebook läuft jede Zelle im Haupt-Kontext, daher ist `__name__` immer `"__main__"`. Damit "importiert" erscheint, müsste der Code in einer separaten `.py`-Datei stehen, die von einer anderen Datei mit `import` geladen wird. Dann wäre `__name__` nicht `"__main__"`, sondern der Dateiname.
</details>

+++

### 🏃 Übung 4.2: Modul-Verhalten simulieren

**Aufgabe:** Der folgende Code simuliert, wie `__name__` funktioniert. Ergänzen Sie die fehlenden Teile.

```{code-cell} ipython3
def demo_berechnung():
    """Eine einfache Demo-Funktion."""
    return 42 * 3


def main():
    """Wird nur bei direkter Ausführung aufgerufen."""
    ergebnis = demo_berechnung()
    print(f"Ergebnis: {ergebnis}")


# Simulation: Was passiert bei direkter Ausführung?
name_simulation = "__main__"  # Direkte Ausführung

if name_simulation == "__main__":
    print("→ Direkte Ausführung erkannt: main() wird aufgerufen")
    main()
else:
    print("→ Import erkannt: main() wird NICHT aufgerufen")

print()

# Simulation: Was passiert beim Import?
name_simulation = "mein_modul"  # Import

if name_simulation == "__main__":
    print("→ Direkte Ausführung erkannt: main() wird aufgerufen")
    main()
else:
    print("→ Import erkannt: main() wird NICHT aufgerufen")
    print("  (Aber demo_berechnung() ist trotzdem verfügbar!)")
    print(f"  Beweis: demo_berechnung() = {demo_berechnung()}")
```

---
## 5️⃣ Die ideale Programmstruktur

### Die 5 Bausteine einer `.py`-Datei

Ein gut strukturiertes Python-Programm besteht aus **fünf Bausteinen** in dieser Reihenfolge:

```
┌─────────────────────────────────┐
│  1. Imports                     │  Was brauche ich?
├─────────────────────────────────┤
│  2. Konstanten                  │  Was ändert sich nie?
├─────────────────────────────────┤
│  3. Hilfsfunktionen             │  Was sind die Einzelschritte?
├─────────────────────────────────┤
│  4. main()-Funktion             │  Was ist der Gesamtablauf?
├─────────────────────────────────┤
│  5. if __name__ == "__main__":  │  Wer startet das Ganze?
│        main()                   │
└─────────────────────────────────┘
```

+++

### Vollständiges Beispiel: Lagerverwaltung

Hier ist unser Lagerverwaltungsprogramm in der **idealen Struktur** – so würde die Datei `lagerverwaltung.py` aussehen.

> 📋 **Hinweis:** Im Notebook schreiben wir alles in eine Zelle, um die Struktur einer `.py`-Datei zu simulieren. In der Praxis wäre das eine einzelne Datei.

```{code-cell} ipython3
# ============================================================
# lagerverwaltung.py – Einfache Lagerverwaltung
# So würde eine vollständige .py-Datei aussehen.
# ============================================================

# --- 1. Imports ---
# (In diesem Beispiel brauchen wir keine Imports)

# --- 2. Konstanten ---
MINDESTBESTAND = 100
PROGRAMMNAME = "Lagerverwaltung v1.0"


# --- 3. Hilfsfunktionen ---
def lager_erstellen():
    """Erstellt ein Beispiel-Lager mit Anfangsbestand."""
    return {
        "Schrauben M8": 150,
        "Muttern M8": 200,
        "Unterlegscheiben M8": 300,
        "Schrauben M10": 75,
        "Dübel 8mm": 500
    }


def bestand_formatiert_anzeigen(lager):
    """Zeigt den Lagerbestand in einer formatierten Tabelle."""
    print(f"\n{'Artikel':<25} {'Menge':>8}")
    print("-" * 35)
    for produkt, menge in lager.items():
        print(f"{produkt:<25} {menge:>8}")


def gesamtmenge_berechnen(lager):
    """Berechnet die Gesamtanzahl aller Teile."""
    gesamt = 0
    for menge in lager.values():
        gesamt = gesamt + menge
    return gesamt


def niedrigbestand_pruefen(lager, grenzwert):
    """Gibt eine Liste der Artikel unter dem Grenzwert zurück."""
    kritische_artikel = []
    for produkt, menge in lager.items():
        if menge < grenzwert:
            kritische_artikel.append((produkt, menge))
    return kritische_artikel


def warnungen_ausgeben(kritische_artikel):
    """Gibt Warnungen für Artikel mit niedrigem Bestand aus."""
    if kritische_artikel:
        print(f"\n⚠️  Artikel unter Mindestbestand ({MINDESTBESTAND}):")
        for produkt, menge in kritische_artikel:
            print(f"  → {produkt}: nur noch {menge} Stück")
    else:
        print("\n✅ Alle Artikel über dem Mindestbestand.")


# --- 4. Hauptfunktion ---
def main():
    """Hauptprogramm: Erstellt Lager und zeigt Bericht."""
    print(f"=== {PROGRAMMNAME} ===")
    
    lager = lager_erstellen()
    bestand_formatiert_anzeigen(lager)
    
    gesamt = gesamtmenge_berechnen(lager)
    print(f"\nGesamtbestand: {gesamt} Teile")
    print(f"Verschiedene Artikel: {len(lager)}")
    
    kritisch = niedrigbestand_pruefen(lager, MINDESTBESTAND)
    warnungen_ausgeben(kritisch)


# --- 5. Einstiegspunkt ---
# In einer .py-Datei: if __name__ == "__main__":
# Im Notebook: Direkter Aufruf
main()
```

> 🤔 **Reflexionsfrage:** Lesen Sie nur die `main()`-Funktion (Zeilen 55–65). Können Sie verstehen, was das Programm tut, **ohne** die Hilfsfunktionen zu lesen? Genau das ist das Ziel guter Programmstruktur!

+++

### Checkliste: Ist mein Programm gut strukturiert?

Prüfen Sie Ihr Programm mit dieser Checkliste:

- [ ] Imports stehen ganz oben
- [ ] Konstanten stehen nach den Imports (GROSSBUCHSTABEN)
- [ ] Jede Funktion hat **eine** klare Aufgabe
- [ ] Jede Funktion hat einen Docstring
- [ ] Funktionen nutzen **Parameter** statt globaler Variablen
- [ ] Es gibt eine `main()`-Funktion
- [ ] `main()` liest sich wie eine Zusammenfassung des Programms
- [ ] Kein loser Code außerhalb von Funktionen (außer Konstanten und Imports)
- [ ] `if __name__ == "__main__":` am Ende (in `.py`-Dateien)

+++

### 🏃 Übung 5.1: Programmstruktur anwenden

**Aufgabe:** Schreiben Sie ein vollständiges, strukturiertes Programm zum Thema **Einkaufsliste**. Das Programm soll:
- Eine Einkaufsliste als Dictionary verwalten (Artikel → Preis)
- Alle Artikel anzeigen
- Den Gesamtpreis berechnen
- Teure Artikel markieren (über einem Grenzwert)

Verwenden Sie die 5-Bausteine-Struktur!

```{code-cell} ipython3
# --- 1. Imports ---
# (keine nötig)

# --- 2. Konstanten ---
# Ihr Code hier

# --- 3. Hilfsfunktionen ---
# Ihr Code hier

# --- 4. Hauptfunktion ---
def main():
    # Ihr Code hier
    pass

# --- 5. Einstiegspunkt ---
main()
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# --- 1. Imports ---
# (keine nötig)

# --- 2. Konstanten ---
PREIS_GRENZWERT = 5.00


# --- 3. Hilfsfunktionen ---
def einkaufsliste_erstellen():
    """Erstellt eine Beispiel-Einkaufsliste."""
    return {
        "Milch": 1.29,
        "Brot": 2.49,
        "Käse": 3.99,
        "Olivenöl": 6.49,
        "Lachs": 8.99
    }


def artikel_anzeigen(einkaufsliste):
    """Zeigt alle Artikel mit Preisen an."""
    print("\nEinkaufsliste:")
    for artikel, preis in einkaufsliste.items():
        print(f"  {artikel}: {preis:.2f} €")


def gesamtpreis_berechnen(einkaufsliste):
    """Berechnet den Gesamtpreis."""
    gesamt = 0
    for preis in einkaufsliste.values():
        gesamt = gesamt + preis
    return gesamt


def teure_artikel_markieren(einkaufsliste, grenzwert):
    """Zeigt Artikel über dem Grenzwert an."""
    print(f"\nArtikel über {grenzwert:.2f} €:")
    for artikel, preis in einkaufsliste.items():
        if preis > grenzwert:
            print(f"  💰 {artikel}: {preis:.2f} €")


# --- 4. Hauptfunktion ---
def main():
    """Hauptprogramm: Einkaufslisten-Verwaltung."""
    print("=== Einkaufsliste ===")
    
    liste = einkaufsliste_erstellen()
    artikel_anzeigen(liste)
    
    gesamt = gesamtpreis_berechnen(liste)
    print(f"\nGesamtpreis: {gesamt:.2f} €")
    
    teure_artikel_markieren(liste, PREIS_GRENZWERT)


# --- 5. Einstiegspunkt ---
main()
```
</details>

+++

---
## 6️⃣ Notebook vs. `.py`-Datei

### Wann nutzt man was?

| Aspekt | Jupyter Notebook | `.py`-Datei |
|--------|------------------|-------------|
| **Ausführung** | Zelle für Zelle, beliebige Reihenfolge | Sequentiell von oben nach unten |
| **Zustand** | Variablen bleiben zwischen Zellen erhalten | Frisch bei jedem Start |
| **`__name__`** | Immer `"__main__"` | `"__main__"` bei direkter Ausführung, sonst Modulname |
| **Ausgabe** | Direkt unter jeder Zelle | Im Terminal |
| **Ideal für** | Lernen, Experimentieren, Datenanalyse | Programme, Tools, importierbare Module |
| **Versionskontrolle** | Schwierig (JSON-Format) | Einfach (reiner Text) |

+++

### So üben wir die `.py`-Struktur im Notebook

Obwohl wir im Notebook arbeiten, können wir die Programmstruktur **trainieren**. Der Workflow:

1. **Im Notebook entwickeln:** Funktionen schreiben und testen
2. **Struktur einhalten:** Imports → Konstanten → Funktionen → main()
3. **main() direkt aufrufen:** Statt `if __name__` schreiben wir einfach `main()`
4. **Für die Praxis:** Wenn der Code fertig ist, alles in eine `.py`-Datei kopieren und `if __name__ == "__main__":` ergänzen

> 💡 **Merke:** Das Notebook ist Ihre Werkbank – die `.py`-Datei ist das fertige Produkt.

+++

### Beispiel: Vom Notebook zur `.py`-Datei

**So sieht es im Notebook aus** (mehrere Zellen):

```{code-cell} ipython3
# Zelle 1: Konstanten
BEGRUESSUNG = "Willkommen zum Quiz!"
ANZAHL_FRAGEN = 3
```

```{code-cell} ipython3
# Zelle 2: Hilfsfunktionen
def frage_stellen(frage, richtige_antwort):
    """Stellt eine Frage und prüft die Antwort."""
    antwort = input(f"{frage} ")
    if antwort.lower() == richtige_antwort.lower():
        print("✅ Richtig!")
        return True
    else:
        print(f"❌ Falsch! Richtig wäre: {richtige_antwort}")
        return False


def ergebnis_anzeigen(punkte, gesamt):
    """Zeigt das Quizergebnis an."""
    prozent = punkte / gesamt * 100
    print(f"\nErgebnis: {punkte}/{gesamt} ({prozent:.0f}%)")
    if prozent >= 70:
        print("🎉 Bestanden!")
    else:
        print("📚 Leider nicht bestanden.")
```

```{code-cell} ipython3
# Zelle 3: main() + Aufruf
def main():
    """Quiz-Hauptprogramm."""
    print(BEGRUESSUNG)
    
    fragen = [
        ("Was ist die Hauptstadt von Deutschland?", "Berlin"),
        ("Wie viele Bundesländer hat Deutschland?", "16"),
        ("In welchem Jahr fiel die Berliner Mauer?", "1989")
    ]
    
    punkte = 0
    for frage, antwort in fragen:
        if frage_stellen(frage, antwort):
            punkte = punkte + 1
    
    ergebnis_anzeigen(punkte, len(fragen))


# Im Notebook: Direkter Aufruf
main()
```

**In einer `.py`-Datei** wäre alles in einer Datei, mit `if __name__` am Ende:

```python
# quiz.py

BEGRUESSUNG = "Willkommen zum Quiz!"
ANZAHL_FRAGEN = 3


def frage_stellen(frage, richtige_antwort):
    """Stellt eine Frage und prüft die Antwort."""
    antwort = input(f"{frage} ")
    if antwort.lower() == richtige_antwort.lower():
        print("✅ Richtig!")
        return True
    else:
        print(f"❌ Falsch! Richtig wäre: {richtige_antwort}")
        return False


def ergebnis_anzeigen(punkte, gesamt):
    """Zeigt das Quizergebnis an."""
    prozent = punkte / gesamt * 100
    print(f"\nErgebnis: {punkte}/{gesamt} ({prozent:.0f}%)")
    if prozent >= 70:
        print("🎉 Bestanden!")
    else:
        print("📚 Leider nicht bestanden.")


def main():
    """Quiz-Hauptprogramm."""
    print(BEGRUESSUNG)
    fragen = [
        ("Was ist die Hauptstadt von Deutschland?", "Berlin"),
        ("Wie viele Bundesländer hat Deutschland?", "16"),
        ("In welchem Jahr fiel die Berliner Mauer?", "1989")
    ]
    punkte = 0
    for frage, antwort in fragen:
        if frage_stellen(frage, antwort):
            punkte = punkte + 1
    ergebnis_anzeigen(punkte, len(fragen))


if __name__ == "__main__":
    main()
```

> 🤔 **Reflexionsfrage:** Was wäre der Vorteil, wenn ein Kollege `import quiz` in seinem eigenen Programm schreiben könnte? Welche Funktion könnte er wiederverwenden?

+++

### 🏃 Übung 6.1: `.py`-Struktur im Notebook simulieren

**Aufgabe:** Schreiben Sie das folgende Programm in der vollständigen `.py`-Struktur – aber im Notebook (also mit direktem `main()`-Aufruf statt `if __name__`). Das Programm soll:
- Eine Konstante `STUNDENLOHN` definieren (z.B. 15.50)
- Eine Funktion `lohn_berechnen(stunden)` → Bruttolohn berechnen
- Eine Funktion `steuer_berechnen(brutto)` → 20% Steuer berechnen
- Eine Funktion `lohnzettel_ausgeben(stunden, brutto, steuer)` → formatierte Ausgabe
- Eine `main()`-Funktion, die alles zusammenführt

```{code-cell} ipython3
# Schreiben Sie hier das vollständige Programm in .py-Struktur:

# --- 1. Imports ---

# --- 2. Konstanten ---

# --- 3. Hilfsfunktionen ---

# --- 4. Hauptfunktion ---

# --- 5. Einstiegspunkt ---
```

<details>
<summary>🔍 Lösung anzeigen</summary>

```python
# --- 1. Imports ---
# (keine nötig)

# --- 2. Konstanten ---
STUNDENLOHN = 15.50
STEUERSATZ = 0.20


# --- 3. Hilfsfunktionen ---
def lohn_berechnen(stunden):
    """Berechnet den Bruttolohn."""
    return stunden * STUNDENLOHN


def steuer_berechnen(brutto):
    """Berechnet die Steuer (20%)."""
    return brutto * STEUERSATZ


def lohnzettel_ausgeben(stunden, brutto, steuer):
    """Gibt einen formatierten Lohnzettel aus."""
    netto = brutto - steuer
    print("=== Lohnzettel ===")
    print(f"Stunden:      {stunden}")
    print(f"Stundenlohn:  {STUNDENLOHN:.2f} €")
    print(f"Bruttolohn:   {brutto:.2f} €")
    print(f"Steuer (20%): {steuer:.2f} €")
    print(f"Nettolohn:    {netto:.2f} €")


# --- 4. Hauptfunktion ---
def main():
    """Hauptprogramm: Lohnberechnung."""
    stunden = 38.5
    brutto = lohn_berechnen(stunden)
    steuer = steuer_berechnen(brutto)
    lohnzettel_ausgeben(stunden, brutto, steuer)


# --- 5. Einstiegspunkt ---
main()
```
</details>

+++

---
## 7️⃣ Häufige Fehler und Best Practices

### ❌ Fehler 1: Code auf Modulebene statt in Funktionen

```{code-cell} ipython3
# ❌ SCHLECHT: Loser Code auf Modulebene
# Bei einem Import würde sofort nach einer Eingabe gefragt!

# name = input("Ihr Name: ")
# print(f"Hallo, {name}!")

# ✅ GUT: In einer Funktion verpackt
def begruessung():
    """Begrüßt den Benutzer."""
    name = input("Ihr Name: ")
    print(f"Hallo, {name}!")

# Nur ausführen, wenn direkt gestartet
# begruessung()  # Im Notebook: Auskommentiert, da input() wartet
```

### ❌ Fehler 2: Globale Variablen statt Parameter

```{code-cell} ipython3
# ❌ SCHLECHT: Globale Variable
ergebnis_global = 0

def addiere_schlecht(a, b):
    global ergebnis_global     # Ändert globale Variable!
    ergebnis_global = a + b

addiere_schlecht(3, 4)
print(f"Schlecht: {ergebnis_global}")


# ✅ GUT: Parameter und Rückgabewert
def addiere_gut(a, b):
    """Addiert zwei Zahlen und gibt das Ergebnis zurück."""
    return a + b

ergebnis = addiere_gut(3, 4)
print(f"Gut: {ergebnis}")
```

### ❌ Fehler 3: Alles in eine riesige Funktion

```{code-cell} ipython3
# ❌ SCHLECHT: Eine Mega-Funktion, die alles macht
def tue_alles():
    lager = {"Schrauben": 50, "Muttern": 200}
    for p, m in lager.items():
        print(f"{p}: {m}")
    gesamt = 0
    for m in lager.values():
        gesamt += m
    print(f"Gesamt: {gesamt}")
    for p, m in lager.items():
        if m < 100:
            print(f"Warnung: {p}")
    # ... und noch 50 weitere Zeilen ...

print("Die Funktion 'tue_alles' ist definiert, aber das ist schlechter Stil!")
print("Besser: Mehrere kleine Funktionen + main() als Dirigent.")
```

### ✅ Best-Practices-Checkliste

| Best Practice | Warum? |
|---------------|--------|
| Jede Funktion hat **eine** Aufgabe | Leichter zu verstehen, testen und wiederverwenden |
| Sprechende Funktionsnamen | `bestand_pruefen()` statt `bp()` oder `funktion3()` |
| Docstrings in jeder Funktion | Beschreibt, was die Funktion tut |
| Parameter statt globaler Variablen | Verhindert Seiteneffekte und macht Code testbar |
| `return` statt `print()` in Berechnungen | Der Aufrufer entscheidet, was mit dem Ergebnis passiert |
| Konstanten in GROSSBUCHSTABEN | Sofort erkennbar, dass der Wert sich nicht ändert |
| `main()` als Einstiegspunkt | Klarer Programmablauf, importierbar |

+++

### 🏃 Übung 7.1: Fehler finden und korrigieren

**Aufgabe:** Der folgende Code enthält **vier** typische Strukturfehler. Finden und korrigieren Sie alle.

```{code-cell} ipython3
# Finden Sie die 4 Fehler und korrigieren Sie den Code!

produkte = ["Laptop", "Maus", "Tastatur"]  # Fehler 1: Globale Variable
rabatt = 0.1  # Fehler 2: Sollte eine Konstante sein

def preis_anzeigen():  # Fehler 3: Keine Parameter!
    for p in produkte:  # Greift auf globale Variable zu
        print(p)

def preis_mit_rabatt(preis):  # Fehler 4: print statt return
    neuer_preis = preis * (1 - rabatt)  # Greift auf globale Variable zu
    print(neuer_preis)

preis_anzeigen()  # Kein main()!
preis_mit_rabatt(100)
```

```{code-cell} ipython3
# Ihre korrigierte Version hier:
```

<details>
<summary>🔍 Lösung anzeigen</summary>

**Die 4 Fehler:**
1. `produkte` ist eine globale Variable statt ein Parameter
2. `rabatt` sollte eine Konstante sein (`RABATT = 0.1`)
3. `preis_anzeigen()` hat keine Parameter, greift auf globale Variable zu
4. `preis_mit_rabatt()` gibt das Ergebnis mit `print` aus statt mit `return`

**Korrigierter Code:**
```python
# --- Konstanten ---
RABATT = 0.1


# --- Hilfsfunktionen ---
def preis_anzeigen(produkte):
    """Zeigt alle Produkte an."""
    for p in produkte:
        print(p)


def preis_mit_rabatt(preis, rabatt):
    """Berechnet den rabattierten Preis."""
    return preis * (1 - rabatt)


# --- Hauptfunktion ---
def main():
    """Hauptprogramm."""
    produkte = ["Laptop", "Maus", "Tastatur"]
    preis_anzeigen(produkte)
    neuer_preis = preis_mit_rabatt(100, RABATT)
    print(f"Preis nach Rabatt: {neuer_preis:.2f} €")


main()
```
</details>

+++

---
## Abschlussübungen

Die folgenden Aufgaben testen Ihr Verständnis der in diesem Notebook erlernten Konzepte. Bearbeiten Sie die Aufgaben selbstständig und vergleichen Sie Ihre Lösung anschließend mit den Musterlösungen am Ende des Notebooks.

### Teil 1: Grundlagen und Verständnis

**Kompetenzstufe**: Anwenden

---

**Aufgabe 1: Taschenrechner strukturieren**

Schreiben Sie einen einfachen Taschenrechner als strukturiertes Programm. Der Taschenrechner soll:
- Zwei Zahlen und eine Operation (+, -, *, /) entgegennehmen
- Die Berechnung durchführen (in einer eigenen Funktion!)
- Das Ergebnis formatiert ausgeben
- Division durch Null abfangen (mit try/except)

Verwenden Sie die 5-Bausteine-Struktur.

```{code-cell} ipython3
# Aufgabe 1: Ihr strukturierter Taschenrechner
```

---

**Aufgabe 2: Notenrechner mit main()**

Schreiben Sie ein strukturiertes Programm, das:
- Eine Liste von Noten entgegennimmt
- Den Durchschnitt berechnet (eigene Funktion)
- Die beste und schlechteste Note findet (eigene Funktionen)
- Eine Bewertung ausgibt: "Sehr gut" (≤ 1.5), "Gut" (≤ 2.5), "Befriedigend" (≤ 3.5), "Ausreichend" (≤ 4.0), "Nicht bestanden" (> 4.0)
- Eine `main()`-Funktion hat, die alles steuert

```{code-cell} ipython3
# Aufgabe 2: Ihr strukturierter Notenrechner
```

---

### Teil 2: Transfer und Problemlösung

**Kompetenzstufe**: Analysieren & Erschaffen

Diese Aufgaben erfordern die Kombination mehrerer Konzepte und eigenständiges Problemlösen.

---

**Aufgabe 3: Vollständiges Lagerprogramm**

Erweitern Sie die Lagerverwaltung aus diesem Notebook zu einem vollständigen Programm. Zusätzlich zu den bestehenden Funktionen soll es:
- Produkte entfernen können
- Den Bestand eines Produkts ändern können (aufstocken/reduzieren)
- Einen sortierten Bericht ausgeben (alphabetisch nach Produktname)
- Alles mit Fehlerbehandlung (z.B. Produkt nicht gefunden)

Schreiben Sie das komplette Programm in der 5-Bausteine-Struktur.

```{code-cell} ipython3
# Aufgabe 3: Erweiterte Lagerverwaltung
```

---

**Aufgabe 4: Skript komplett refaktorisieren**

Der folgende Code funktioniert, ist aber schlecht strukturiert. Refaktorisieren Sie ihn komplett in die 5-Bausteine-Struktur. Ändern Sie dabei nicht die Funktionalität!

```{code-cell} ipython3
# Diesen Code refaktorisieren:

mitarbeiter = [
    {"name": "Müller", "stunden": 40, "stundensatz": 25},
    {"name": "Schmidt", "stunden": 35, "stundensatz": 30},
    {"name": "Weber", "stunden": 42, "stundensatz": 22},
    {"name": "Fischer", "stunden": 38, "stundensatz": 28}
]
ueberstunden_grenze = 40
ueberstunden_zuschlag = 1.5

print("=== Lohnabrechnung ===")
gesamtkosten = 0
for ma in mitarbeiter:
    if ma["stunden"] > ueberstunden_grenze:
        normal = ueberstunden_grenze * ma["stundensatz"]
        ueber = (ma["stunden"] - ueberstunden_grenze) * ma["stundensatz"] * ueberstunden_zuschlag
        lohn = normal + ueber
    else:
        lohn = ma["stunden"] * ma["stundensatz"]
    gesamtkosten = gesamtkosten + lohn
    print(f"{ma['name']}: {lohn:.2f} €")

print(f"\nGesamtkosten: {gesamtkosten:.2f} €")
print(f"Durchschnittslohn: {gesamtkosten / len(mitarbeiter):.2f} €")
```

```{code-cell} ipython3
# Ihre refaktorisierte Version hier:
```

---
## Zusammenfassung 🎓

### Was Sie gelernt haben:

Herzlichen Glückwunsch! Sie können jetzt echte Python-Programme strukturieren.

✅ **Vom Skript zum Programm**: Sie erkennen den Unterschied zwischen losem Code und strukturierten Programmen  
✅ **Funktionen als Bausteine**: Sie zerlegen Programme in kleine, wiederverwendbare Funktionen  
✅ **Die `main()`-Funktion**: Sie nutzen `main()` als Einstiegspunkt und Dirigenten Ihres Programms  
✅ **`if __name__`-Idiom**: Sie verstehen, warum es wichtig ist und wie es funktioniert  
✅ **Die 5 Bausteine**: Sie kennen die ideale Struktur einer `.py`-Datei  
✅ **Notebook vs. `.py`**: Sie wissen, wann man was nutzt und wie man im Notebook übt  
✅ **Best Practices**: Sie vermeiden häufige Anfängerfehler

### Wichtige Konzepte im Überblick:

| Konzept | Syntax / Beispiel | Beschreibung |
|---------|-------------------|-------------|
| Funktion definieren | `def name(param):` | Jede Funktion hat EINE Aufgabe |
| Hauptfunktion | `def main():` | Steuert den Programmablauf |
| Einstiegspunkt | `if __name__ == "__main__":` | Verhindert Ausführung beim Import |
| Konstante | `MAX_WERT = 100` | Unveränderliche Werte in GROSSBUCHSTABEN |
| Docstring | `"""Beschreibung."""` | Dokumentiert, was die Funktion tut |
| Return statt Print | `return ergebnis` | Gibt Werte zurück statt sie auszugeben |

### Die 5 Bausteine einer `.py`-Datei:

```
1. Imports           → Was brauche ich?
2. Konstanten        → Was ändert sich nie?
3. Hilfsfunktionen   → Was sind die Einzelschritte?
4. main()            → Was ist der Gesamtablauf?
5. if __name__       → Wer startet das Ganze?
```

### Ihr Fortschritt:
✅ Start  
✅ Vom Skript zum Programm  
✅ Funktionen als Bausteine  
✅ Die main()-Funktion  
✅ Das if \_\_name\_\_ Idiom  
✅ Die ideale Programmstruktur  
✅ Notebook vs. .py-Datei  
✅ Häufige Fehler & Best Practices  
✅ Fertig!

+++

---
## Musterlösungen

<details>
<summary>🔍 Lösung zu Aufgabe 1 (Taschenrechner)</summary>

```python
# --- Konstanten ---
ERLAUBTE_OPERATIONEN = ["+", "-", "*", "/"]


# --- Hilfsfunktionen ---
def berechnen(zahl1, zahl2, operation):
    """Führt die Berechnung durch und gibt das Ergebnis zurück."""
    if operation == "+":
        return zahl1 + zahl2
    elif operation == "-":
        return zahl1 - zahl2
    elif operation == "*":
        return zahl1 * zahl2
    elif operation == "/":
        if zahl2 == 0:
            print("Fehler: Division durch Null!")
            return None
        return zahl1 / zahl2


def ergebnis_ausgeben(zahl1, zahl2, operation, ergebnis):
    """Gibt das Ergebnis formatiert aus."""
    if ergebnis is not None:
        print(f"{zahl1} {operation} {zahl2} = {ergebnis}")


# --- Hauptfunktion ---
def main():
    """Taschenrechner-Hauptprogramm."""
    print("=== Taschenrechner ===")
    try:
        zahl1 = float(input("Erste Zahl: "))
        operation = input("Operation (+, -, *, /): ")
        zahl2 = float(input("Zweite Zahl: "))
        
        if operation not in ERLAUBTE_OPERATIONEN:
            print(f"Ungültige Operation: {operation}")
            return
        
        ergebnis = berechnen(zahl1, zahl2, operation)
        ergebnis_ausgeben(zahl1, zahl2, operation, ergebnis)
    except ValueError:
        print("Fehler: Bitte geben Sie gültige Zahlen ein.")


main()
```
</details>

<details>
<summary>🔍 Lösung zu Aufgabe 2 (Notenrechner)</summary>

```python
# --- Hilfsfunktionen ---
def durchschnitt(noten):
    """Berechnet den Notendurchschnitt."""
    summe = 0
    for note in noten:
        summe = summe + note
    return summe / len(noten)


def beste_note(noten):
    """Findet die beste (niedrigste) Note."""
    beste = noten[0]
    for note in noten:
        if note < beste:
            beste = note
    return beste


def schlechteste_note(noten):
    """Findet die schlechteste (höchste) Note."""
    schlechteste = noten[0]
    for note in noten:
        if note > schlechteste:
            schlechteste = note
    return schlechteste


def bewertung_ermitteln(schnitt):
    """Gibt die Bewertung basierend auf dem Durchschnitt zurück."""
    if schnitt <= 1.5:
        return "Sehr gut"
    elif schnitt <= 2.5:
        return "Gut"
    elif schnitt <= 3.5:
        return "Befriedigend"
    elif schnitt <= 4.0:
        return "Ausreichend"
    else:
        return "Nicht bestanden"


# --- Hauptfunktion ---
def main():
    """Notenrechner-Hauptprogramm."""
    noten = [1.3, 2.7, 1.0, 3.3, 2.0, 1.7, 4.0, 2.3]
    
    print("=== Notenrechner ===")
    print(f"Noten: {noten}")
    
    schnitt = durchschnitt(noten)
    print(f"Durchschnitt: {schnitt:.2f}")
    print(f"Beste Note: {beste_note(noten)}")
    print(f"Schlechteste Note: {schlechteste_note(noten)}")
    
    bewertung = bewertung_ermitteln(schnitt)
    print(f"Bewertung: {bewertung}")


main()
```
</details>

<details>
<summary>🔍 Lösung zu Aufgabe 3 (Erweiterte Lagerverwaltung)</summary>

```python
# --- Konstanten ---
MINDESTBESTAND = 100
PROGRAMMNAME = "Lagerverwaltung v2.0"


# --- Hilfsfunktionen ---
def lager_erstellen():
    """Erstellt ein Beispiel-Lager."""
    return {
        "Schrauben M8": 150,
        "Muttern M8": 200,
        "Unterlegscheiben M8": 300,
        "Schrauben M10": 75,
        "Dübel 8mm": 500
    }


def bestand_anzeigen(lager):
    """Zeigt den Lagerbestand sortiert an."""
    print(f"\n{'Artikel':<25} {'Menge':>8}")
    print("-" * 35)
    for produkt in sorted(lager.keys()):
        print(f"{produkt:<25} {lager[produkt]:>8}")


def produkt_hinzufuegen(lager, name, menge):
    """Fügt ein Produkt hinzu."""
    lager[name] = menge
    print(f"✅ '{name}' mit {menge} Stück hinzugefügt.")


def produkt_entfernen(lager, name):
    """Entfernt ein Produkt aus dem Lager."""
    if name in lager:
        del lager[name]
        print(f"✅ '{name}' entfernt.")
    else:
        print(f"❌ Fehler: '{name}' nicht im Lager gefunden.")


def bestand_aendern(lager, name, aenderung):
    """Ändert den Bestand eines Produkts."""
    if name not in lager:
        print(f"❌ Fehler: '{name}' nicht im Lager gefunden.")
        return
    neuer_bestand = lager[name] + aenderung
    if neuer_bestand < 0:
        print(f"❌ Fehler: Bestand kann nicht negativ werden.")
        return
    lager[name] = neuer_bestand
    print(f"✅ '{name}': {lager[name] - aenderung} → {neuer_bestand} Stück")


def niedrigbestand_pruefen(lager, grenzwert):
    """Prüft und meldet Artikel unter dem Grenzwert."""
    kritisch = []
    for produkt, menge in lager.items():
        if menge < grenzwert:
            kritisch.append((produkt, menge))
    return kritisch


def gesamtbestand(lager):
    """Berechnet den Gesamtbestand."""
    gesamt = 0
    for menge in lager.values():
        gesamt = gesamt + menge
    return gesamt


# --- Hauptfunktion ---
def main():
    """Hauptprogramm der erweiterten Lagerverwaltung."""
    print(f"=== {PROGRAMMNAME} ===")
    lager = lager_erstellen()
    
    bestand_anzeigen(lager)
    
    produkt_hinzufuegen(lager, "Bolzen M12", 50)
    bestand_aendern(lager, "Schrauben M10", 100)
    produkt_entfernen(lager, "Dübel 8mm")
    produkt_entfernen(lager, "Gibt es nicht")  # Fehlerfall testen
    
    bestand_anzeigen(lager)
    print(f"\nGesamtbestand: {gesamtbestand(lager)} Teile")
    
    kritisch = niedrigbestand_pruefen(lager, MINDESTBESTAND)
    if kritisch:
        print(f"\n⚠️  {len(kritisch)} Artikel unter Mindestbestand:")
        for name, menge in kritisch:
            print(f"  → {name}: {menge}")
    else:
        print("\n✅ Alle Bestände ausreichend.")


main()
```
</details>

<details>
<summary>🔍 Lösung zu Aufgabe 4 (Lohnabrechnung refaktorisiert)</summary>

```python
# --- Konstanten ---
UEBERSTUNDEN_GRENZE = 40
UEBERSTUNDEN_ZUSCHLAG = 1.5


# --- Hilfsfunktionen ---
def mitarbeiter_erstellen():
    """Erstellt die Mitarbeiterliste."""
    return [
        {"name": "Müller", "stunden": 40, "stundensatz": 25},
        {"name": "Schmidt", "stunden": 35, "stundensatz": 30},
        {"name": "Weber", "stunden": 42, "stundensatz": 22},
        {"name": "Fischer", "stunden": 38, "stundensatz": 28}
    ]


def lohn_berechnen(stunden, stundensatz):
    """Berechnet den Lohn inkl. Überstundenzuschlag."""
    if stunden > UEBERSTUNDEN_GRENZE:
        normal = UEBERSTUNDEN_GRENZE * stundensatz
        ueber = (stunden - UEBERSTUNDEN_GRENZE) * stundensatz * UEBERSTUNDEN_ZUSCHLAG
        return normal + ueber
    else:
        return stunden * stundensatz


def lohnzettel_drucken(mitarbeiter, loehne):
    """Gibt die Lohnzettel formatiert aus."""
    print("=== Lohnabrechnung ===")
    for ma, lohn in zip(mitarbeiter, loehne):
        print(f"{ma['name']}: {lohn:.2f} €")


def statistik_ausgeben(loehne):
    """Gibt die Gesamtkosten und den Durchschnitt aus."""
    gesamt = 0
    for lohn in loehne:
        gesamt = gesamt + lohn
    schnitt = gesamt / len(loehne)
    print(f"\nGesamtkosten: {gesamt:.2f} €")
    print(f"Durchschnittslohn: {schnitt:.2f} €")


# --- Hauptfunktion ---
def main():
    """Hauptprogramm: Lohnabrechnung."""
    mitarbeiter = mitarbeiter_erstellen()
    
    loehne = []
    for ma in mitarbeiter:
        lohn = lohn_berechnen(ma["stunden"], ma["stundensatz"])
        loehne.append(lohn)
    
    lohnzettel_drucken(mitarbeiter, loehne)
    statistik_ausgeben(loehne)


main()
```
</details>

+++

---
## Ausblick auf Notebook 16 👀

Im nächsten Notebook lernen Sie **externe Bibliotheken** kennen – insbesondere **Pandas** für die Datenanalyse:

- 📊 **DataFrames**: Tabellarische Daten elegant verarbeiten
- 📈 **Visualisierungen**: Diagramme direkt aus Daten erzeugen
- 📁 **CSV-Dateien**: Echte Datensätze laden und analysieren
- 🔧 **Externe Bibliotheken**: Wie man `import pandas as pd` nutzt

Die Programmstruktur, die Sie heute gelernt haben, wird Ihnen dabei helfen: Auch Datenanalyse-Programme profitieren von `main()` und guter Struktur!

**Bis dahin: Viel Erfolg beim Üben!** 🚀

---

**Glückwunsch! Sie haben Notebook 15 erfolgreich abgeschlossen!** 🎉
