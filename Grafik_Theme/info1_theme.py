"""INFO1-Grafik-Theme: einheitliche Infografiken, Abläufe und Architekturen.

Alle Maße sind Millimeter im Folienmaßstab (Folie 16:9 = 160 x 90 mm),
Ursprung oben links. Schriftgrößen sind echte Punktgrößen auf der Folie,
solange die Grafik in ihrer Entwurfsbreite eingebunden wird.

    from info1_theme import Leinwand

    lw = Leinwand(140, 50)
    a = lw.karte(5, 5, 50, 30, "Aufrufstelle", rolle="daten", code=["x = f(3)"])
    b = lw.karte(85, 5, 50, 30, "Funktion", rolle="ablauf", code=["return n * 2"])
    lw.pfeil(a, b, "Argument 3", nummer=1)
    lw.speichern("beispiel")            # beispiel.pdf + beispiel.png

Regeln und Begründungen: siehe README.md in diesem Ordner.
"""

import warnings
from dataclasses import dataclass

import matplotlib
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Polygon
from matplotlib.path import Path

# ----------------------------------------------------------------------------
# Tokens
# ----------------------------------------------------------------------------

FLAECHE = "#FAFAFA"   # Folienhintergrund (Metropolis)
TINTE = "#23373B"     # Text, Rahmen, Pfeile (= Farbe der Folien-Kopfzeile)
TINTE_2 = "#5A6B6E"   # Nebentext: Achsen, Indizes, Pfeilbeschriftung
WEISS = "#FFFFFF"

# Rollenfarben: (Linie, Fläche). Text steht immer in Tinte, nie in Rollenfarbe.
ROLLEN = {
    "daten":    ("#2A78D6", "#E3EDFA"),  # Werte, Objekte, Tabellen
    "ablauf":   ("#D96C0A", "#FAECDF"),  # Anweisung, Kontrollfluss, "jetzt aktiv"
    "ergebnis": ("#0F9972", "#E0F2ED"),  # Rückgabe, Ausgabe, dauerhaft gespeichert
    "aussen":   ("#B0408F", "#F5E6F0"),  # Mensch, Eingabe, fremde Systeme
    "neutral":  ("#6B7B7E", "#ECEEEE"),  # Kontext ohne eigene Bedeutung
    "fehler":   ("#C8372D", "#F8E5E4"),  # nur als Status, immer mit Symbol + Wort
}
FOKUS = ROLLEN["ablauf"][0]

PT = {"titel": 10.0, "kopf": 8.5, "text": 8.0, "code": 7.5, "klein": 7.0}
LINIE = 1.2          # pt, Rahmen und Pfeile
RADIUS = 1.6         # mm, Eckenradius der Karten
RAND = 2.6           # mm, Innenabstand der Karten
SCHRIFT = "DejaVu Sans"
SCHRIFT_CODE = "DejaVu Sans Mono"

matplotlib.rcParams.update({
    "font.family": SCHRIFT,
    "pdf.fonttype": 42,
    "svg.fonttype": "none",
    "mathtext.fontset": "dejavusans",
})


def _zeile(pt):
    """Zeilenhöhe in mm für eine Schriftgröße in pt."""
    return pt * 0.3528 * 1.4


@dataclass
class Box:
    """Rechteckiger Platzhalter eines Elements; liefert Ankerpunkte für Pfeile."""
    x: float
    y: float
    b: float
    h: float

    @property
    def mitte(self):
        return (self.x + self.b / 2, self.y + self.h / 2)

    def links(self, anteil=0.5):
        return (self.x, self.y + self.h * anteil)

    def rechts(self, anteil=0.5):
        return (self.x + self.b, self.y + self.h * anteil)

    def oben(self, anteil=0.5):
        return (self.x + self.b * anteil, self.y)

    def unten(self, anteil=0.5):
        return (self.x + self.b * anteil, self.y + self.h)


def _anker(von, nach):
    """Wählt für zwei Boxen die einander zugewandten Seitenmitten."""
    if not isinstance(von, Box) and not isinstance(nach, Box):
        return von, nach
    p = von.mitte if isinstance(von, Box) else von
    q = nach.mitte if isinstance(nach, Box) else nach
    dx, dy = q[0] - p[0], q[1] - p[1]

    def seite(box, richtung_x, richtung_y, waagerecht):
        if waagerecht:
            return box.rechts() if richtung_x > 0 else box.links()
        return box.unten() if richtung_y > 0 else box.oben()

    def frei(box, gegen):
        """Abstand der Boxen entlang x bzw. y (negativ = Überlappung)."""
        if not isinstance(gegen, Box):
            return abs(dx), abs(dy)
        gx = max(gegen.x - (box.x + box.b), box.x - (gegen.x + gegen.b))
        gy = max(gegen.y - (box.y + box.h), box.y - (gegen.y + gegen.h))
        return gx, gy

    if isinstance(von, Box) and isinstance(nach, Box):
        gx, gy = frei(von, nach)
        waagerecht = gx >= gy
    else:
        waagerecht = abs(dx) >= abs(dy)
    a = seite(von, dx, dy, waagerecht) if isinstance(von, Box) else von
    z = seite(nach, -dx, -dy, waagerecht) if isinstance(nach, Box) else nach
    return a, z


class Leinwand:
    """Zeichenfläche in mm. `schritt=k` zeigt nur Elemente mit `ab <= k`
    (für schrittweisen Aufbau als Beamer-Overlays)."""

    def __init__(self, breite=140, hoehe=60, schritt=None, raster=False):
        self.breite, self.hoehe, self.schritt = breite, hoehe, schritt
        self.fig = plt.figure(figsize=(breite / 25.4, hoehe / 25.4))
        self.fig.patch.set_facecolor(FLAECHE)
        self.ax = self.fig.add_axes([0, 0, 1, 1])
        self.ax.set_xlim(0, breite)
        self.ax.set_ylim(hoehe, 0)
        self.ax.set_aspect("equal")
        self.ax.axis("off")
        if raster:  # Entwurfshilfe: 10-mm-Raster
            for v in range(0, int(breite) + 1, 10):
                self.ax.axvline(v, color="#DDDDDD", lw=0.4, zorder=0)
                self.ax.text(v + 0.5, 2.5, str(v), fontsize=5, color="#AAAAAA")
            for v in range(0, int(hoehe) + 1, 10):
                self.ax.axhline(v, color="#DDDDDD", lw=0.4, zorder=0)
                self.ax.text(0.5, v - 0.5, str(v), fontsize=5, color="#AAAAAA")

    # -- Helfer -------------------------------------------------------------

    def _da(self, ab):
        return self.schritt is None or ab <= self.schritt

    def jetzt(self, k):
        """True, wenn gerade Schritt k aufgebaut wird (für `fokus=`)."""
        return self.schritt == k

    def _text(self, x, y, s, pt=PT["text"], fett=False, kursiv=False, code=False,
              farbe=TINTE, ha="left", va="top", hof=False, z=5):
        t = self.ax.text(
            x, y, s, fontsize=pt, color=farbe, ha=ha, va=va, zorder=z,
            family=SCHRIFT_CODE if code else SCHRIFT,
            weight="bold" if fett else "normal",
            style="italic" if kursiv else "normal",
            linespacing=1.4,
        )
        if hof:  # heller Hof: bleibt lesbar, wenn eine Linie dahinter liegt
            t.set_path_effects([pe.withStroke(linewidth=2.6, foreground=FLAECHE)])
        return t

    def _breite(self, t):
        """Gemessene Breite eines Textobjekts in mm."""
        kasten = t.get_window_extent(self.fig.canvas.get_renderer())
        return kasten.width / self.fig.dpi * 25.4

    def _passt(self, t, platz):
        if self._breite(t) > platz + 0.2:
            warnings.warn(f"Text ragt über das Element hinaus: {t.get_text()!r} "
                          f"({self._breite(t):.0f} mm bei {platz:.0f} mm Platz)",
                          stacklevel=4)

    def _fokusrahmen(self, x, y, b, h, radius):
        d = 0.8
        self.ax.add_patch(FancyBboxPatch(
            (x - d, y - d), b + 2 * d, h + 2 * d,
            boxstyle=f"round,pad=0,rounding_size={radius + d}",
            fc="none", ec=FOKUS, lw=2.2, zorder=4))

    # -- Elemente -----------------------------------------------------------

    def text(self, x, y, s, art="text", ab=1, **kw):
        """Freier Text. art: titel | kopf | text | klein | code."""
        if not self._da(ab):
            return
        kw.setdefault("fett", art in ("titel", "kopf"))
        kw.setdefault("code", art == "code")
        if art == "klein":
            kw.setdefault("farbe", TINTE_2)
        self._text(x, y, s, pt=PT[art], **kw)

    def titel(self, s, x=0, y=0):
        """Grafiktitel mit orangem Strich. Nur nutzen, wenn die Grafik ohne
        Folientitel steht (Notebook, Handout) - sonst doppelt es sich."""
        self._text(x, y, s, pt=PT["titel"], fett=True)
        yy = y + _zeile(PT["titel"]) + 0.6
        self.ax.plot([x, x + 12], [yy, yy], color=FOKUS, lw=2.0,
                     solid_capstyle="butt", zorder=5)

    def karte(self, x, y, b, h, titel=None, zeilen=(), code=(), rolle="neutral",
              ab=1, fokus=False):
        """Abgerundete Karte: Titel (fett), Textzeilen, Codezeilen.
        Ohne Titel wird der Inhalt mittig gesetzt."""
        box = Box(x, y, b, h)
        if not self._da(ab):
            return box
        linie, flaeche = ROLLEN[rolle]
        self.ax.add_patch(FancyBboxPatch(
            (x, y), b, h, boxstyle=f"round,pad=0,rounding_size={RADIUS}",
            fc=flaeche, ec=linie, lw=LINIE, zorder=2))
        if fokus:
            self._fokusrahmen(x, y, b, h, RADIUS)
        inhalt = [(z, False) for z in zeilen] + [(c, True) for c in code]
        if titel is None:
            hoehe = sum(_zeile(PT["code"] if c else PT["text"]) for _, c in inhalt)
            cy = y + h / 2 - hoehe / 2
            for s, c in inhalt:
                pt = PT["code"] if c else PT["text"]
                self._passt(self._text(x + b / 2, cy, s, pt=pt, code=c, ha="center"),
                            b - 2)
                cy += _zeile(pt)
            return box
        platz = b - 2 * RAND
        self._passt(self._text(x + RAND, y + RAND, titel, pt=PT["kopf"], fett=True), platz)
        cy = y + RAND + _zeile(PT["kopf"]) + 0.8
        for s, c in inhalt:
            pt = PT["code"] if c else PT["text"]
            self._passt(self._text(x + RAND, cy, s, pt=pt, code=c), platz)
            cy += _zeile(pt)
        return box

    def knoten(self, x, y, b, h, text, form="aktion", rolle="neutral", ab=1,
               fokus=False, code=False):
        """Flussdiagramm-Symbol (Formen nach DIN 66001):
        start (Grenzstelle) | aktion | entscheidung | ein_aus."""
        box = Box(x, y, b, h)
        if not self._da(ab):
            return box
        linie, flaeche = ROLLEN[rolle]
        stil = dict(fc=flaeche, ec=linie, lw=LINIE, zorder=2, joinstyle="round")
        if form == "start":
            self.ax.add_patch(FancyBboxPatch(
                (x, y), b, h, boxstyle=f"round,pad=0,rounding_size={h / 2}", **stil))
        elif form == "entscheidung":
            self.ax.add_patch(Polygon(
                [(x + b / 2, y), (x + b, y + h / 2), (x + b / 2, y + h), (x, y + h / 2)],
                **stil))
        elif form == "ein_aus":
            s = min(3.0, b / 6)
            self.ax.add_patch(Polygon(
                [(x + s, y), (x + b, y), (x + b - s, y + h), (x, y + h)], **stil))
            box = Box(x + s / 2, y, b - s, h)  # Anker auf den schrägen Kanten
        else:
            self.ax.add_patch(FancyBboxPatch(
                (x, y), b, h, boxstyle="round,pad=0,rounding_size=0.6", **stil))
        if fokus:
            self._fokusrahmen(x, y, b, h, h / 2 if form == "start" else 0.6)
        t = self._text(x + b / 2, y + h / 2, text, pt=PT["code"] if code else PT["text"],
                       code=code, ha="center", va="center")
        self._passt(t, b * (0.62 if form == "entscheidung" else 1) - 2)
        return box

    def gruppe(self, x, y, b, h, titel, ab=1):
        """Gestrichelter Rahmen um zusammengehörige Elemente (Systemgrenze)."""
        box = Box(x, y, b, h)
        if not self._da(ab):
            return box
        self.ax.add_patch(FancyBboxPatch(
            (x, y), b, h, boxstyle=f"round,pad=0,rounding_size={RADIUS}",
            fc="none", ec=TINTE_2, lw=0.9, ls=(0, (4, 3)), zorder=1))
        self._text(x + RAND, y + 1.8, titel.upper(), pt=PT["klein"], fett=True,
                   farbe=TINTE_2)
        return box

    def marke(self, x, y, n, ab=1, fokus=False):
        """Schrittnummer: dunkler Kreis mit weißer Ziffer."""
        if not self._da(ab):
            return
        if fokus:
            self.ax.add_patch(Circle((x, y), 2.9, fc=FLAECHE, ec=FOKUS, lw=1.8, zorder=6))
        self.ax.add_patch(Circle((x, y), 2.2, fc=TINTE, ec="none", zorder=7))
        self._text(x, y + 0.05, str(n), pt=PT["code"], fett=True, farbe=WEISS,
                   ha="center", va="center_baseline", z=8)

    def pfeil(self, von, nach, text=None, rolle=None, form="gerade", nummer=None,
              gestrichelt=False, ab=1, fokus=False, text_bei=0.5, versatz=(0, -3.1),
              ueber=()):
        """Pfeil zwischen Punkten oder Boxen.
        form: gerade | hv (erst waagerecht) | vh (erst senkrecht);
        ueber=[(x, y), ...] führt den Pfeil über eigene Wegpunkte.
        rolle=None zeichnet in Tinte; fokus=True in Orange und kräftiger.
        Die Beschriftung sitzt mittig auf dem längsten Teilstück, um `versatz`
        verschoben; eine `nummer` steht als Marke davor."""
        if not self._da(ab):
            return
        a, z = _anker(von, nach)
        if ueber:
            punkte = [a, *ueber, z]
        elif form == "hv":
            punkte = [a, (z[0], a[1]), z]
        elif form == "vh":
            punkte = [a, (a[0], z[1]), z]
        else:
            punkte = [a, z]
        farbe = FOKUS if fokus else (ROLLEN[rolle][0] if rolle else TINTE)
        self.ax.add_patch(FancyArrowPatch(
            path=Path(punkte), arrowstyle="-|>,head_length=0.55,head_width=0.26",
            mutation_scale=10, lw=LINIE + (0.6 if fokus else 0), color=farbe,
            ls=(0, (3, 2.5)) if gestrichelt else "solid", shrinkA=0, shrinkB=0,
            joinstyle="round", capstyle="round", zorder=3))
        if text is None and nummer is None:
            return
        # Beschriftung auf dem längsten Teilstück
        i = max(range(len(punkte) - 1),
                key=lambda k: abs(punkte[k + 1][0] - punkte[k][0])
                + abs(punkte[k + 1][1] - punkte[k][1]))
        (x0, y0), (x1, y1) = punkte[i], punkte[i + 1]
        tx = x0 + (x1 - x0) * text_bei + versatz[0]
        ty = y0 + (y1 - y0) * text_bei + versatz[1]
        if text is None:
            self.marke(tx, ty, nummer, fokus=fokus)
            return
        t = self._text(tx, ty, text, pt=PT["klein"], farbe=TINTE_2, ha="center",
                       va="center", hof=True, z=6)
        if nummer is not None:  # Marke + Text gemeinsam zentrieren
            breite = self._breite(t)
            t.set_x(tx + 2.9)
            self.marke(tx - breite / 2 - 0.9, ty, nummer, fokus=fokus)

    def zellen(self, x, y, werte, b=11, h=8, indizes=True, rolle="daten",
               markiert=(), name=None, index_name=None, ab=1, code=True):
        """Speicherzellen / Listenelemente in einer Reihe, optional mit Index
        darunter und Variablenname davor. Gibt die Boxen der Zellen zurück."""
        boxen = [Box(x + i * b, y, b, h) for i in range(len(werte))]
        if not self._da(ab):
            return boxen
        linie, flaeche = ROLLEN[rolle]
        for i, (w, bx) in enumerate(zip(werte, boxen)):
            aktiv = i in markiert
            self.ax.add_patch(FancyBboxPatch(
                (bx.x, bx.y), b, h, boxstyle="round,pad=0,rounding_size=0.5",
                fc=ROLLEN["ablauf"][1] if aktiv else flaeche,
                ec=FOKUS if aktiv else linie,
                lw=2.2 if aktiv else LINIE, zorder=3 if aktiv else 2))
            self._text(bx.x + b / 2, bx.y + h / 2, str(w), pt=PT["text"], code=code,
                       fett=aktiv, ha="center", va="center")
            if indizes:
                self._text(bx.x + b / 2, bx.y + h + 1.2, str(i), pt=PT["klein"],
                           code=True, farbe=TINTE_2, ha="center")
        if name:
            self._text(x - 2.5, y + h / 2, name, pt=PT["text"], code=True, fett=True,
                       ha="right", va="center")
        if index_name and indizes:
            self._text(x - 2.5, y + h + 1.2, index_name, pt=PT["klein"],
                       farbe=TINTE_2, ha="right")
        return boxen

    def status(self, x, y, art, text, ab=1):
        """Statusmeldung mit Symbol + Wort (nie Farbe allein). art: ok | fehler."""
        if not self._da(ab):
            return
        farbe = ROLLEN["ergebnis" if art == "ok" else "fehler"][0]
        self.ax.add_patch(Circle((x + 1.9, y), 1.9, fc=farbe, ec="none", zorder=6))
        self._text(x + 1.9, y, "✓" if art == "ok" else "✗", pt=PT["klein"],
                   fett=True, farbe=WEISS, ha="center", va="center", z=7)
        self._text(x + 5.2, y, text, pt=PT["text"], va="center")

    def legende(self, x, y, eintraege, abstand=4.0):
        """Waagerechte Legende. eintraege: [(rolle, beschriftung), ...]."""
        for rolle, s in eintraege:
            linie, flaeche = ROLLEN[rolle]
            self.ax.add_patch(FancyBboxPatch(
                (x, y - 1.5), 4.5, 3.0, boxstyle="round,pad=0,rounding_size=0.6",
                fc=flaeche, ec=linie, lw=LINIE, zorder=2))
            t = self._text(x + 6, y, s, pt=PT["klein"], farbe=TINTE_2, va="center")
            x += 6 + self._breite(t) + abstand

    # -- Ausgabe ------------------------------------------------------------

    def speichern(self, pfad, formate=("pdf", "png"), dpi=300):
        """Speichert als PDF (Folien, verlustfrei) und PNG (Notebooks)."""
        for f in formate:
            self.fig.savefig(f"{pfad}.{f}", dpi=dpi, facecolor=FLAECHE)
        plt.close(self.fig)


def aufbau(zeichne, pfad, schritte, **kw):
    """Rendert `zeichne(schritt)` für schritt = 1..schritte und speichert
    pfad_1.pdf, pfad_2.pdf, ... (Beamer: \\includegraphics<k>{pfad_k})."""
    for k in range(1, schritte + 1):
        zeichne(k).speichern(f"{pfad}_{k}", **kw)


# ----------------------------------------------------------------------------
# Selbsttest: Kontraste nach WCAG 2.x
# ----------------------------------------------------------------------------

def _leuchtdichte(hexfarbe):
    kan = [int(hexfarbe[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    lin = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in kan]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def kontrast(a, b):
    la, lb = sorted((_leuchtdichte(a), _leuchtdichte(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


if __name__ == "__main__":
    print(f"{'Rolle':10} {'Linie/Folie':>12} {'Tinte/Fläche':>13} {'Nebentext/Fläche':>17}")
    for name, (linie, flaeche) in ROLLEN.items():
        k1, k2, k3 = kontrast(linie, FLAECHE), kontrast(TINTE, flaeche), kontrast(TINTE_2, flaeche)
        print(f"{name:10} {k1:12.2f} {k2:13.2f} {k3:17.2f}")
        assert k1 >= 3.0, f"{name}: Linie unter 3:1"
        assert k2 >= 7.0 and k3 >= 4.5, f"{name}: Text zu schwach"
    assert kontrast(WEISS, TINTE) >= 7.0
    print("Alle Kontraste erfüllt (Linien >= 3:1, Text >= 4.5:1).")
