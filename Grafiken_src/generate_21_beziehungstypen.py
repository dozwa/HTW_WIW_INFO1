"""Erzeugt die Uebersicht der drei Beziehungstypen (1:1, 1:n, n:m) fuer Foliensatz 21.

Jeder Beziehungstyp wird einzeln mit Graphviz (`dot`) gezeichnet -- links ein farbiger
Markierungs-Knoten ("1 : 1" usw.), daneben die Mini-Beziehung als Kaesten mit
Kraehenfuss-Endsymbolen. Die drei Bilder werden anschliessend mit Pillow untereinander
gesetzt (linksbuendig, damit die Marker uebereinanderstehen) -- so bleibt jedes Diagramm
gross und der Block hat ein folientaugliches Seitenverhaeltnis.

Erzeugt:
  Grafiken/21_beziehungstypen.png
      1:1   bestellung — rechnung
      1:n   kunde — bestellung
      n:m   bestellung — produkt   (aufgeloest ueber bestellposition)

Bewusst ohne Spaltenlisten -- es geht hier nur um die *Form* der Beziehung; die
ausfuehrliche Tabellensicht steht in Foliensatz 21b.

Benoetigt das Graphviz-CLI:  brew install graphviz
"""
import os
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from erd_dot_helpers import (plain_entity, edge, _require_dot,
                             ONE, MANY, BLAU, ATTR_GRAU, FONT)

GRAFIKEN_DIR = "Grafiken"
JOIN_FILL = "#ead7f2"      # Zwischentabelle hervorheben
MARKER_FILL = "#eef3f8"


def _marker(node_id, typ, beschreibung):
    label = (f'<<FONT POINT-SIZE="20" COLOR="{BLAU}"><B>{typ}</B></FONT>'
             f'<BR/><BR/><FONT POINT-SIZE="11" COLOR="{ATTR_GRAU}">{beschreibung}</FONT>>')
    return (f'  {node_id} [shape=box, style="rounded,filled", fillcolor="{MARKER_FILL}", '
            f'color="{BLAU}", penwidth=1.4, margin="0.28,0.20", label={label}];')


def _component_dot(typ, beschreibung, entity_defs, edge_defs, first_entity):
    parts = [_marker("m", typ, beschreibung)]
    parts += entity_defs
    parts.append(f"  m -> {first_entity} [style=invis];")
    parts += edge_defs
    body = "\n".join(parts)
    return ("digraph G {\n"
            "  graph [bgcolor=white, rankdir=LR, nodesep=0.4, ranksep=0.85, "
            f'fontname="{FONT}", splines=spline, margin="0.12,0.12"];\n'
            f'  node [shape=plaintext, fontname="{FONT}", fontsize=12];\n'
            f'  edge [fontname="{FONT}"];\n'
            f"{body}\n}}\n")


def _specs():
    return [
        # 1:1  -- jede Bestellung hat genau eine Rechnung
        ("1 : 1", "jede Bestellung hat genau eine Rechnung",
         [plain_entity("b", "bestellung"), plain_entity("r", "rechnung")],
         [edge("b", "r", tail=ONE, head=ONE, label="hat")], "b"),
        # 1:n  -- ein Kunde, viele Bestellungen; FK auf der "n"-Seite
        ("1 : n", "ein Kunde, viele Bestellungen &#8212; FK auf der &#8222;n&#8220;-Seite",
         [plain_entity("k", "kunde"), plain_entity("b", "bestellung")],
         [edge("k", "b", tail=ONE, head=MANY, label="gibt auf")], "k"),
        # n:m  -- aufgeloest ueber die Zwischentabelle bestellposition (zwei FKs)
        ("n : m", "aufgel&#246;st &#252;ber bestellposition (zwei FKs)",
         [plain_entity("b", "bestellung"),
          plain_entity("p", "bestellposition", fill=JOIN_FILL),
          plain_entity("pr", "produkt")],
         [edge("b", "p", tail=ONE, head=MANY, label="1 : n"),
          edge("p", "pr", tail=MANY, head=ONE, label="n : 1")], "b"),
    ]


def _render_png(dot_src):
    with tempfile.NamedTemporaryFile("w", suffix=".dot", delete=False) as fh:
        fh.write(dot_src)
        dot_path = fh.name
    png_path = dot_path + ".png"
    try:
        subprocess.run(["dot", "-Tpng", "-Gdpi=200", dot_path, "-o", png_path], check=True)
    finally:
        os.unlink(dot_path)
    return png_path


def generate():
    _require_dot()
    tmp_pngs = []
    try:
        for spec in _specs():
            tmp_pngs.append(_render_png(_component_dot(*spec)))
        imgs = [Image.open(p).convert("RGBA") for p in tmp_pngs]
        pad, gap = 26, 38
        max_w = max(im.width for im in imgs)
        total_h = sum(im.height for im in imgs) + gap * (len(imgs) - 1) + 2 * pad
        canvas = Image.new("RGBA", (max_w + 2 * pad, total_h), (255, 255, 255, 255))
        draw = ImageDraw.Draw(canvas)
        y = pad
        for i, im in enumerate(imgs):
            if i > 0:
                ly = y - gap // 2
                draw.line([(pad, ly), (max_w + pad, ly)], fill=(210, 220, 230, 255), width=2)
            canvas.paste(im, (pad, y), im)
            y += im.height + gap
        out = os.path.join(GRAFIKEN_DIR, "21_beziehungstypen.png")
        canvas.convert("RGB").save(out)
    finally:
        for p in tmp_pngs:
            try:
                os.unlink(p)
            except OSError:
                pass
    print(f"→ geschrieben: {out}")


if __name__ == "__main__":
    generate()
