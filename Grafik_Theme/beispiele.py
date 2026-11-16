"""Beispielgrafiken zum INFO1-Grafik-Theme.  Aufruf:  python beispiele.py"""

from pathlib import Path

from info1_theme import PT, ROLLEN, TINTE, Leinwand, aufbau

AUS = Path(__file__).parent / "beispiele"
AUS.mkdir(exist_ok=True)


def funktionsaufruf(schritt=None):
    """Ablauf mit schrittweisem Aufbau (ersetzt Grafik in Foliensatz 07)."""
    lw = Leinwand(140, 44, schritt=schritt)
    a = lw.karte(2, 6, 56, 28, "Aufrufstelle (global)", rolle="daten",
                 code=["brutto = netto_zu_brutto(89.95)"])
    b = lw.karte(96, 6, 42, 28, "Funktion (lokal)", rolle="ablauf",
                 code=["netto = 89.95", "return netto * 1.19"], ab=2)
    lw.pfeil(a.rechts(0.32), b.links(0.32), "Argument 89.95", nummer=1, ab=2,
             fokus=lw.jetzt(2))
    lw.pfeil(b.links(0.72), a.rechts(0.72), "Wert 107.0405", nummer=2, ab=3,
             rolle="ergebnis", fokus=lw.jetzt(3), versatz=(0, 3.3))
    lw.text(a.x + 2.6, a.y + 20.5, "brutto → 107.0405", art="code", ab=3)
    lw.text(b.x + b.b, 39, "danach werden lokale Namen gelöscht", art="klein",
            ha="right", ab=3)
    return lw


def flussdiagramm():
    """Flussdiagramm in Normsymbolen: größter gemeinsamer Teiler (Euklid)."""
    lw = Leinwand(140, 62)
    k = dict(code=True)
    start = lw.knoten(8, 25, 22, 9, "Start", form="start")
    ein = lw.knoten(36, 25, 24, 9, "a, b", form="ein_aus", rolle="aussen", **k)
    frage = lw.knoten(68, 21, 26, 17, "b ≠ 0 ?", form="entscheidung",
                      rolle="ablauf", **k)
    aus = lw.knoten(102, 25, 22, 9, "a", form="ein_aus", rolle="ergebnis", **k)
    ende = lw.knoten(102, 44, 22, 9, "Ende", form="start")
    rest = lw.knoten(66, 5, 30, 9, "a, b = b, a % b", rolle="daten", **k)
    lw.pfeil(start, ein)
    lw.pfeil(ein, frage)
    lw.pfeil(frage, aus, "nein", versatz=(0, -2.2))
    lw.pfeil(aus, ende)
    lw.pfeil(frage.oben(), rest.unten(), "ja", versatz=(3.2, 0))
    # Rücksprung der Schleife: mündet vor der Raute in den Hauptfluss
    lw.pfeil(rest.links(), (64, 29.2), ueber=[(64, 9.5)])
    lw.legende(8, 57, [("aussen", "Eingabe"), ("ablauf", "Entscheidung"),
                       ("daten", "Anweisung"), ("ergebnis", "Ausgabe")])
    return lw


def von_neumann():
    """Architektur: Gruppe als Systemgrenze, Karten als Bausteine."""
    lw = Leinwand(140, 62)
    ein = lw.karte(3, 16, 26, 14, zeilen=["Eingabe", "Tastatur, Maus"], rolle="aussen")
    aus = lw.karte(111, 16, 26, 14, zeilen=["Ausgabe", "Monitor, Drucker"],
                   rolle="ergebnis")
    cpu = lw.gruppe(40, 3, 60, 33, "Prozessor (CPU)")
    sw = lw.karte(46, 9, 48, 9, zeilen=["Steuerwerk"], rolle="ablauf")
    alu = lw.karte(46, 22, 22, 10, zeilen=["Rechenwerk", "(ALU)"], rolle="ablauf")
    reg = lw.karte(72, 22, 22, 10, zeilen=["Register"], rolle="daten")
    sp = lw.karte(40, 46, 60, 13, zeilen=["Speicher", "Programm + Daten"],
                  rolle="daten")
    lw.pfeil(ein.rechts(), (40, 23))
    lw.pfeil((100, 23), aus.links())
    lw.pfeil((62, 36), (62, 46))
    lw.pfeil((78, 46), (78, 36))
    lw.text(81, 41, "Befehle und Daten\nüber den Bus", art="klein", va="center")
    return lw


def listenindex():
    """Speicherzellen: Liste mit Index, eine Zelle im Fokus."""
    lw = Leinwand(140, 34)
    z = lw.zellen(34, 9, ['"Eco"', '"Hemp"', '"Bambus"', '"Kork"'], b=20, h=9,
                  name="schuhe", index_name="Index", markiert=[2])
    lw.text(z[2].mitte[0], 3, "schuhe[2]", art="code", fett=True, ha="center")
    lw.pfeil((z[2].mitte[0], 6.6), z[2].oben(), fokus=True)
    lw.text(34, 27.5, "Der Index zählt ab 0 – das dritte Element hat Index 2.",
            art="klein")
    return lw


def sql_pipeline():
    """Pipeline: gleiche Bausteine, waagerechter Lesefluss."""
    lw = Leinwand(140, 34)
    stufen = [("FROM", "Tabelle wählen", "daten"), ("WHERE", "Zeilen filtern", "ablauf"),
              ("GROUP BY", "Gruppen bilden", "ablauf"), ("SELECT", "Spalten wählen", "ablauf"),
              ("ORDER BY", "sortieren", "ergebnis")]
    b, luecke = 22.4, 6
    letzte = None
    for i, (wort, tut, rolle) in enumerate(stufen):
        x = 2 + i * (b + luecke)
        box = lw.karte(x, 9, b, 16, rolle=rolle)
        lw.text(x + b / 2, 12.2, wort, art="code", fett=True, ha="center")
        lw.text(x + b / 2, 18.2, tut, art="klein", ha="center", farbe=TINTE)
        lw.marke(x + 2, 9, i + 1)
        if letzte:
            lw.pfeil(letzte, box)
        letzte = box
    lw.text(2, 30, "Ausführungsreihenfolge – nicht die Schreibreihenfolge der Abfrage.",
            art="klein")
    return lw


def stilblatt():
    """Übersicht: Farben, Schrift, Bausteine auf einem Blatt."""
    lw = Leinwand(160, 98)
    lw.titel("INFO1-Grafik-Theme", 5, 4)
    lw.text(5, 14.5, "ROLLENFARBEN – eine Farbe, eine Bedeutung, im ganzen Kurs",
            art="klein", fett=True)
    namen = [("daten", "Daten", "Werte\nObjekte"), ("ablauf", "Ablauf", "Anweisung\njetzt aktiv"),
             ("ergebnis", "Ergebnis", "Rückgabe\nAusgabe"), ("aussen", "Außen", "Mensch\nEingabe"),
             ("neutral", "Neutral", "Kontext"), ("fehler", "Fehler", "nur mit\nSymbol")]
    for i, (rolle, name, wofuer) in enumerate(namen):
        x = 5 + i * 25.4
        lw.karte(x, 19, 23, 17, name, rolle=rolle)
        lw.text(x + 2.6, 26.4, wofuer, art="klein", farbe=TINTE)
        lw.text(x + 2.6, 37.2, ROLLEN[rolle][0], art="klein", code=True)

    lw.text(5, 45, "SCHRIFT – wie auf den Folien",
            art="klein", fett=True)
    y = 50
    for art, probe in [("titel", "Titel 10 pt"), ("kopf", "Kartenkopf 8,5 pt"),
                       ("text", "Fließtext 8 pt"), ("code", "code = 7.5  # pt"),
                       ("klein", "Nebentext 7 pt")]:
        lw.text(5, y, probe, art=art)
        y += PT[art] * 0.3528 * 1.4 + 1.2

    lw.text(58, 45, "BAUSTEINE", art="klein", fett=True)
    a = lw.karte(58, 50, 28, 15, "Karte", ["Titel + Zeilen"], rolle="daten")
    b = lw.karte(124, 50, 31, 15, "Karte im Fokus", code=["x = 42"], rolle="ablauf",
                 fokus=True)
    lw.pfeil(a, b, "Pfeil mit Schritt", nummer=1)
    lw.knoten(58, 71, 18, 8, "Start", form="start")
    lw.knoten(80, 71, 22, 8, "Anweisung")
    lw.knoten(106, 69, 24, 12, "x > 0 ?", form="entscheidung", rolle="ablauf", code=True)
    lw.knoten(134, 71, 21, 8, "Ausgabe", form="ein_aus", rolle="ergebnis")
    lw.zellen(58, 85, [3, 1, 4, 1, 5], b=9, h=7, markiert=[2])
    lw.status(112, 86, "ok", "Test bestanden")
    lw.status(112, 92, "fehler", "NameError")
    return lw


if __name__ == "__main__":
    for name, fn in [("ablauf_flussdiagramm", flussdiagramm),
                     ("architektur_von_neumann", von_neumann),
                     ("speicher_listenindex", listenindex),
                     ("pipeline_sql", sql_pipeline),
                     ("stilblatt", stilblatt),
                     ("ablauf_funktionsaufruf", funktionsaufruf)]:
        fn().speichern(str(AUS / name))
    aufbau(funktionsaufruf, str(AUS / "ablauf_funktionsaufruf"), 3, formate=("pdf",))
    print("fertig:", AUS)
