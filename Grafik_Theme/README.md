# INFO1-Grafik-Theme

Ein einheitlicher Stil für Infografiken, Abläufe und Architekturen in den
Folien und Notebooks. Übersicht auf einem Blatt: [`beispiele/stilblatt.png`](beispiele/stilblatt.png),
Vergleich auf einer echten Folie: [`beispiele/vorher_nachher_folie07.png`](beispiele/vorher_nachher_folie07.png).

| Datei | Zweck |
|---|---|
| `info1_theme.py` | Farben, Schrift und Bausteine (`Leinwand`) |
| `info1.mplstyle` | derselbe Stil für Datendiagramme aus Pandas/Matplotlib |
| `beispiele.py` | sechs Beispielgrafiken, erzeugt `beispiele/*.pdf` und `*.png` |

Voraussetzung ist nur `matplotlib`. DejaVu Sans (die Folienschrift) liefert
matplotlib mit.

## Schnellstart

```python
from info1_theme import Leinwand

lw = Leinwand(140, 44)                      # mm im Folienmaßstab
a = lw.karte(2, 6, 56, 28, "Aufrufstelle (global)", rolle="daten",
             code=["brutto = netto_zu_brutto(89.95)"])
b = lw.karte(96, 6, 42, 28, "Funktion (lokal)", rolle="ablauf",
             code=["netto = 89.95", "return netto * 1.19"])
lw.pfeil(a.rechts(0.32), b.links(0.32), "Argument 89.95", nummer=1)
lw.speichern("07_funktionen_aufruf")        # .pdf für Folien, .png für Notebooks
```

In die Folie **in Entwurfsbreite** einbinden, damit die Schriftgrößen stimmen:
`\includegraphics[width=140mm]{07_funktionen_aufruf.pdf}` (Folie = 160 × 90 mm).
`Leinwand(..., raster=True)` blendet beim Entwerfen ein 10-mm-Raster ein.
Ragt Text über eine Karte hinaus, gibt das Theme eine Warnung aus.

## Die sechs Regeln

1. **Eine Farbe, eine Bedeutung – im ganzen Kurs.** Farbe kodiert die Rolle
   eines Elements, nie Dekoration oder Reihenfolge.

   | Rolle | Farbe | steht für |
   |---|---|---|
   | `daten` | Blau `#2A78D6` | Werte, Objekte, Tabellen |
   | `ablauf` | Orange `#D96C0A` | Anweisung, Kontrollfluss, „jetzt aktiv" |
   | `ergebnis` | Grün `#0F9972` | Rückgabe, Ausgabe, dauerhaft Gespeichertes |
   | `aussen` | Magenta `#B0408F` | Mensch, Eingabe, fremde Systeme |
   | `neutral` | Grau `#6B7B7E` | Kontext ohne eigene Bedeutung |
   | `fehler` | Rot `#C8372D` | nur als Status, immer mit Symbol und Wort |

2. **Text ist immer dunkel auf hell.** Beschriftungen stehen in Tinte
   `#23373B` (die Farbe der Folien-Kopfzeile), nie in der Rollenfarbe.
3. **Nichts unter 7 pt.** Fließtext 8 pt, Code 7,5 pt, Nebentext 7 pt.
4. **Ein Fokus pro Bild.** Was gerade besprochen wird, bekommt den orangen
   Ring oder den orangen Pfeil – höchstens ein Element.
5. **Schritte tragen Nummern.** Dunkle Marke mit weißer Ziffer; komplexe
   Abläufe werden schrittweise aufgebaut (siehe unten).
6. **Lesefluss von links nach rechts, höchstens etwa neun Elemente.** Mehr
   Inhalt wird auf mehrere Bilder verteilt.

Flussdiagramme behalten die Normsymbole nach DIN 66001, die Notebook 13a
lehrt (`knoten(form="start" | "aktion" | "entscheidung" | "ein_aus")`).

## Schrittweiser Aufbau

Jedes Element nimmt `ab=k` und erscheint erst ab Schritt `k`. Die Positionen
bleiben fest, das Bild springt also nicht.

```python
def zeichne(schritt):
    lw = Leinwand(140, 44, schritt=schritt)
    ...
    lw.pfeil(a, b, "Argument", nummer=1, ab=2, fokus=lw.jetzt(2))
    return lw

aufbau(zeichne, "07_aufruf", schritte=3)    # 07_aufruf_1.pdf ... _3.pdf
```

In Beamer: `\includegraphics<1>{07_aufruf_1}\includegraphics<2>{07_aufruf_2}...`

## Animationen mit Manim (Probe)

`manim_probe.py` zeigt denselben Funktionsaufruf als Animation mit Manim, der
Bibliothek hinter den 3Blue1Brown-Videos (Community-Ausgabe 0.22). Ergebnis:
[`beispiele/manim_funktionsaufruf.mp4`](beispiele/manim_funktionsaufruf.mp4),
zum Vergleich auf dunklem Grund
[`beispiele/manim_funktionsaufruf_dunkel.mp4`](beispiele/manim_funktionsaufruf_dunkel.mp4).

Manim lohnt sich, wo Bewegung selbst die Erklärung ist (ein Wert wandert,
eine Liste wird sortiert). Für Standbilder bleibt `info1_theme.py` einfacher:
Manim braucht Pango und Cairo als Systempakete und für Formelsatz zusätzlich
LaTeX; die dunkle Variante ist nicht auf Farbfehlsichtigkeit geprüft.

## Bausteine

| Methode | Wofür |
|---|---|
| `karte` | Baustein mit Titel, Text- und Codezeilen |
| `knoten` | Flussdiagramm-Symbol |
| `gruppe` | gestrichelte Systemgrenze um mehrere Bausteine |
| `pfeil` | gerade, gewinkelt (`form="hv"/"vh"`) oder über Wegpunkte (`ueber=`) |
| `marke` | Schrittnummer |
| `zellen` | Liste / Speicherzellen mit Index |
| `status` | ✓ / ✗ mit Wort |
| `legende`, `text`, `titel` | Beschriftung |

`titel()` nur verwenden, wenn die Grafik ohne Folientitel steht – sonst
steht dieselbe Information doppelt da.

## Begründung und Belege

**Was von 3Blue1Brown übernommen ist – und was nicht.** Übernommen sind drei
Prinzipien: Farbe bleibt an einer Bedeutung haften, es gibt genau einen
Blickfang pro Bild, und Komplexes entsteht schrittweise. Nicht übernommen
ist der dunkle Hintergrund. Diese Einordnung von 3Blue1Brown beruht auf
eigener Anschauung der Videos, nicht auf Literatur.

| Entscheidung | Beleg | Einschränkung |
|---|---|---|
| Heller Grund, dunkle Schrift | Lesbarkeit ist bei dunkler Schrift auf hellem Grund besser, besonders bei kleiner Schrift [1][2] | Der Vorteil geht auf die höhere Leuchtdichte zurück, nicht auf die Polarität an sich [3]; getestet wurde an Bildschirmen, nicht am Beamer |
| Vier Rollenfarben, geprüft auf Farbfehlsichtigkeit | Rot-Grün-Kontraste und ungeprüfte Paletten schließen Betrachter aus [4]; die Palette folgt dem Vorgehen von [5] (Mindestabstand auch unter simulierter Fehlsichtigkeit) | [5] ist ein Preprint ohne Peer-Review |
| Farbe nie als einziger Träger (Form, Symbol, Wort zusätzlich) | Redundante Farbe-Form-Kodierung verbessert die Unterscheidung [6]; Richtlinien verengen sich sonst auf Kontrastwerte [7] | [6] untersucht Streudiagramme, nicht Architekturdiagramme |
| Eine Bedeutung je Symbol, wenige Symbolarten, Text ergänzt Grafik | Prinzipien „semiotic clarity", „graphic economy", „dual coding" [8] | [8] ist eine Designtheorie; sie wird oft unkritisch und ohne Nachweis angewandt [9] |
| Begrenzte Elementzahl, sauberes Layout | Zu viele (und zu wenige) Elemente senken die Verständlichkeit von Komponentendiagrammen [10]; Layoutqualität wirkt messbar auf die kognitive Last [11] | [10] nennt nur grobe Schwellen – „etwa neun" ist eine Faustregel von mir, kein Messwert |
| Lesefluss waagerecht | Waagerechte Layouts waren in einer Blickbewegungsstudie weniger anstrengend [12] | 21 Teilnehmende; frühere Studien fanden keinen signifikanten Richtungseffekt (in [12] berichtet) |
| Ein Fokus, Nummern, schrittweiser Aufbau | Signaling und Segmentierung verbessern das Lernen, stärker bei dozentengetaktetem Material [13][14] | überwiegend kurze Laborstudien |
| Konsistente Regeln als Leitfaden | 22 Praxisleitlinien für kognitiv wirksame Diagramme [15]; frühe Lesbarkeitsregeln für Architekturdiagramme [16] | [16] stammt von 2002 und ist nicht mehr aktuell |

Ohne Literaturbeleg, rein gestalterisch gewählt: Eckenradius, Linienstärken,
die konkreten Farbtöne innerhalb der geprüften Grenzen und die Zuordnung der
Farben zu den Rollen.

### Messwerte der Palette

- Linien gegen Folienhintergrund: 3,3 bis 5,1 : 1 (Mindestwert 3 : 1).
- Tinte auf allen Flächen: über 10 : 1; Nebentext: über 4,6 : 1.
- Die vier Rollenfarben bleiben in jeder Paarung unterscheidbar, auch bei
  simulierter Rot- und Grünschwäche (kleinster Abstand ΔE 8,1 in OKLab bei
  Deuteranopie, Zielwert 8; Simulation nach Machado et al. 2009).
- Rot ist darin nicht enthalten und deshalb nur mit Symbol und Wort erlaubt.

`python info1_theme.py` rechnet die Kontraste nach.

### Quellen

1. Piepenbrock, Mayr & Buchner (2013): [Positive Display Polarity Is Particularly Advantageous for Small Character Sizes](https://consensus.app/papers/details/w:48fdf521-5105-4b9e-b1e1-790f73678555/?utm_source=claude_desktop). Human Factors.
2. Buchner & Baumgartner (2007): [Text – background polarity affects performance irrespective of ambient illumination and colour contrast](https://consensus.app/papers/details/w:091b9f63-90f9-435c-a880-9e5779cc7d7b/?utm_source=claude_desktop). Ergonomics.
3. Buchner, Mayr & Brandt (2009): [The advantage of positive text-background polarity is due to high display luminance](https://consensus.app/papers/details/w:b62a5d16-6b5f-4a1c-a7af-34f1a1df8089/?utm_source=claude_desktop). Ergonomics.
4. Crameri, Shephard & Heron (2020): [The misuse of colour in science communication](https://consensus.app/papers/details/w:d84a7678-fd21-41fe-997e-6a1344005e32/?utm_source=claude_desktop). Nature Communications.
5. Petroff (2021): [Accessible Color Sequences for Data Visualization](https://consensus.app/papers/details/w:2b8d0738-4df8-4663-bd1b-81c452883952/?utm_source=claude_desktop). arXiv, Preprint.
6. Tseng, Wang et al. (2026): [Redundant is Not Redundant: Automating Efficient Categorical Palettes Design Unifying Color & Shape Encodings with CatPAW](https://consensus.app/papers/details/w:82699853-147a-4f93-ac69-15a37d4829da/?utm_source=claude_desktop). CHI.
7. Geddes, Eggertson et al. (2025): [Designing for Colour Vision Deficiency: A Scoping Review of Resources That Support Designers in Choosing Accessible Colours](https://consensus.app/papers/details/w:9e99db89-09ec-4934-b2db-d0c1ff351aa9/?utm_source=claude_desktop). ASSETS.
8. Moody (2009): [The "Physics" of Notations: Toward a Scientific Basis for Constructing Visual Notations in Software Engineering](https://consensus.app/papers/details/w:08285717-5edc-4acc-9fd9-17afdf64a098/?utm_source=claude_desktop). IEEE Transactions on Software Engineering.
9. van der Linden & Hadar (2018): [A Systematic Literature Review of Applications of the Physics of Notations](https://consensus.app/papers/details/w:c1692e4a-989f-4573-a09b-68c7ccf134c0/?utm_source=claude_desktop). IEEE Transactions on Software Engineering.
10. Stevanetic, Javed & Zdun (2014): [Empirical evaluation of the understandability of architectural component diagrams](https://consensus.app/papers/details/w:75e9ec1e-05f5-4874-a057-d3aa42cd06f5/?utm_source=claude_desktop). WICSA Companion.
11. Störrle (2011): [On the impact of layout quality to understanding UML diagrams](https://consensus.app/papers/details/w:bd4ee366-a333-4c27-9103-b7cf103183f4/?utm_source=claude_desktop). IEEE VL/HCC.
12. Lübke, Ahrens & Schneider (2021): [Influence of diagram layout and scrolling on understandability of BPMN processes](https://consensus.app/papers/details/w:3613974b-ed80-4795-a002-6aa219b1dfa8/?utm_source=claude_desktop). Information Technology and Management.
13. Noetel et al. (2021): [Multimedia Design for Learning: An Overview of Reviews With Meta-Meta-Analysis](https://consensus.app/papers/details/w:417099fa-96af-43ff-9bbc-3515893de32c/?utm_source=claude_desktop). Review of Educational Research.
14. Alpizar, Adesope & Wong (2020): [A meta-analysis of signaling principle in multimedia learning environments](https://consensus.app/papers/details/w:e99d2937-1135-4be9-b0a5-0a5c64d49526/?utm_source=claude_desktop). Educational Technology Research and Development.
15. Malinova & Mendling (2021): [Cognitive Diagram Understanding and Task Performance in Systems Analysis and Design](https://consensus.app/papers/details/w:c51c8464-97e6-4a7d-a4fa-ac8cf3c7ed9d/?utm_source=claude_desktop). MIS Quarterly.
16. Koning, Dormann & van Vliet (2002): [Practical guidelines for the readability of IT-architecture diagrams](https://consensus.app/papers/details/w:934b349a-4fb1-4686-ac8a-7666c17ea6d9/?utm_source=claude_desktop). ACM SIGDOC.
