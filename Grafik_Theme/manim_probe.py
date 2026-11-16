"""Probe: der Funktionsaufruf aus Foliensatz 07 als Manim-Animation.

Manim ist die Animationsbibliothek hinter den 3Blue1Brown-Videos (hier die
Community-Ausgabe). Die Szene nutzt dieselben Farben und Rollen wie
info1_theme.py.

    pip install manim                       # braucht Pango/Cairo als Systempakete
    manim -qh manim_probe.py Funktionsaufruf
    DUNKEL=1 manim -qh manim_probe.py Funktionsaufruf    # Tafel-Variante
"""

import os

from manim import (DOWN, LEFT, RIGHT, UP, Arrow, Circle, Create, FadeIn, FadeOut,
                   GrowArrow, Indicate, ReplacementTransform, RoundedRectangle,
                   Scene, Text, VGroup, Write, config)

DUNKEL = os.environ.get("DUNKEL") == "1"

if DUNKEL:   # nur zum Vergleich - die Palette ist für dunklen Grund nicht geprüft
    GRUND, TINTE, NEBEN = "#23373B", "#F2F5F5", "#A9B8BA"
    BLAU, ORANGE, GRUEN = ("#5B9BE8", "#2F4D61"), ("#E58530", "#4E4839"), ("#22B089", "#23524C")
else:        # Werte aus info1_theme.py
    GRUND, TINTE, NEBEN = "#FAFAFA", "#23373B", "#5A6B6E"
    BLAU, ORANGE, GRUEN = ("#2A78D6", "#E3EDFA"), ("#D96C0A", "#FAECDF"), ("#0F9972", "#E0F2ED")

config.background_color = GRUND
SANS, MONO = "DejaVu Sans", "DejaVu Sans Mono"


def karte(breite, hoehe, titel, rolle):
    linie, flaeche = rolle
    rahmen = RoundedRectangle(width=breite, height=hoehe, corner_radius=0.16,
                              stroke_color=linie, stroke_width=3,
                              fill_color=flaeche, fill_opacity=1)
    kopf = Text(titel, font=SANS, weight="BOLD", font_size=26, color=TINTE)
    kopf.move_to(rahmen.get_corner(UP + LEFT) + 0.3 * DOWN + 0.3 * RIGHT, aligned_edge=UP + LEFT)
    return VGroup(rahmen, kopf)


def code(zeile, **kw):
    return Text(zeile, font=MONO, font_size=23, color=TINTE, **kw)


def marke(n):
    kreis = Circle(radius=0.2, stroke_width=0, fill_color=TINTE, fill_opacity=1)
    ziffer = Text(str(n), font=SANS, weight="BOLD", font_size=20, color=GRUND)
    return VGroup(kreis, ziffer)


class Funktionsaufruf(Scene):
    def construct(self):
        aufruf = karte(6.9, 3.0, "Aufrufstelle (global)", BLAU).to_edge(LEFT, buff=0.4)
        rumpf = karte(4.6, 3.0, "Funktion (lokal)", ORANGE).to_edge(RIGHT, buff=0.4)

        def unter(k, text, zeile):
            t = code(text)
            t.next_to(k[1], DOWN, buff=0.3 + 0.48 * zeile, aligned_edge=LEFT)
            return t

        z_aufruf = unter(aufruf, "brutto = netto_zu_brutto(89.95)", 0)
        argument = z_aufruf[-6:-1]                      # die Glyphen von 89.95
        z_netto = unter(rumpf, "netto = ", 0)
        z_return = unter(rumpf, "return netto * 1.19", 1)

        # 1 - Ausgangslage: nur die Aufrufstelle
        self.play(Create(aufruf[0]), Write(aufruf[1]), run_time=0.8)
        self.play(Write(z_aufruf), run_time=0.9)
        self.wait(0.4)

        # 2 - der Aufruf erzeugt eine eigene kleine Welt
        hin = Arrow(aufruf[0].get_right() + 0.5 * UP, rumpf[0].get_left() + 0.5 * UP,
                    buff=0.08, color=ORANGE[0], stroke_width=5)
        m1 = marke(1).next_to(hin, UP, buff=0.12)
        self.play(FadeIn(rumpf), GrowArrow(hin), FadeIn(m1), run_time=0.8)

        # der Wert wandert sichtbar hinüber und wird an den Parameter gebunden
        wert = argument.copy().set_color(ORANGE[0])
        ziel = code("89.95").next_to(z_netto, RIGHT, buff=0.14, aligned_edge=DOWN)
        self.play(Indicate(argument, color=ORANGE[0], scale_factor=1.25), run_time=0.6)
        self.play(FadeIn(z_netto), wert.animate.move_to(ziel), run_time=1.2)
        self.play(wert.animate.set_color(TINTE), run_time=0.3)
        self.play(Write(z_return), run_time=0.8)
        self.wait(0.4)

        # 3 - return schickt genau einen Wert zurück
        ergebnis = code("107.0405", weight="BOLD").set_color(GRUEN[0])
        ergebnis.move_to(z_return[-9:])
        self.play(Indicate(z_return[-9:], color=GRUEN[0], scale_factor=1.15), run_time=0.6)
        zurueck = Arrow(rumpf[0].get_left() + 0.75 * DOWN, aufruf[0].get_right() + 0.75 * DOWN,
                        buff=0.08, color=GRUEN[0], stroke_width=5)
        m2 = marke(2).next_to(zurueck, DOWN, buff=0.12)
        z_brutto = code("brutto → ").next_to(z_aufruf, DOWN, buff=0.75, aligned_edge=LEFT)
        ablage = code("107.0405").next_to(z_brutto, RIGHT, buff=0.14, aligned_edge=DOWN)
        self.play(GrowArrow(zurueck), FadeIn(m2), FadeIn(ergebnis), run_time=0.8)
        self.play(FadeIn(z_brutto), ergebnis.animate.move_to(ablage), run_time=1.2)
        self.play(ReplacementTransform(ergebnis, ablage), run_time=0.3)

        # danach wird die lokale Welt abgeräumt
        notiz = Text("lokale Namen werden gelöscht", font=SANS, font_size=20, color=NEBEN)
        notiz.next_to(rumpf, DOWN, buff=0.25)
        lokal = VGroup(rumpf, z_netto, wert, z_return)
        self.play(lokal.animate.set_opacity(0.25), FadeIn(notiz),
                  FadeOut(hin), FadeOut(m1), run_time=0.9)
        self.wait(1.5)
