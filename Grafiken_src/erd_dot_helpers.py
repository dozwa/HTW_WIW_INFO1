"""Gemeinsame Helfer fuer die Graphviz-basierten ER-Diagramme der Datenbank-Foliensaetze.

KEIN generate_*-Skript -- wird von den generate_21*_*.py importiert (sie liegen im
selben Ordner und legen diesen Pfad in sys.path) und nicht von `make grafiken` ausgefuehrt.

Erfordert das Graphviz-CLI (`dot`, ggf. `gvpack`/`neato`).  Installation: `brew install graphviz`.

Idee: Tabellen werden als Graphviz-HTML-Label-Knoten gezeichnet
  - farbige Titelzeile (Tabellenname)
  - eine Zeile pro Spalte; Primaerschluessel fett+unterstrichen+gold, Fremdschluessel
    kursiv+orange, gewoehnliche Attribute grau
Beziehungen sind Kanten mit Kraehenfuss-/Kardinalitaets-Endsymbolen.
"""
import os
import shutil
import subprocess
import tempfile

GRAFIKEN_DIR = "Grafiken"

# --- Farbpalette (an die matplotlib-Grafiken angelehnt) ----------------------
BLAU = "#2a5d8f"        # Rahmen, Kanten, Tabellen-Titelzeile
FK_ORANGE = "#e07b3a"   # Fremdschluessel, Kanten-Labels
PK_GOLD = "#b8860b"     # Primaerschluessel
ATTR_GRAU = "#444444"   # gewoehnliche Attribute
NULL_BG = "#f6e6e6"     # hinterlegte Zelle (z. B. NULL-Beispiel)
LIGHT_BG = "#f7fafd"    # leichter Hintergrund fuer Attribut-Zeilen (optional)

FONT = "DejaVu Sans"

# Kraehenfuss-/Kardinalitaets-Endsymbole (Graphviz arrowhead-Specs)
ONE = "teetee"          # genau eins   ||
ZERO_ONE = "teeodot"    # null oder eins  o|
MANY = "crowtee"        # eins oder viele  >|
ZERO_MANY = "crowodot"  # null oder viele  >o
PLAIN_MANY = "crow"     # viele (ohne Zusatz)
NONE = "none"


def _require_dot():
    if shutil.which("dot") is None:
        raise SystemExit(
            "Graphviz wird benoetigt, aber 'dot' wurde nicht gefunden.\n"
            "Installation:  brew install graphviz"
        )


def column(name, role="attr", note=None, port=None, bg=None):
    """Eine Tabellenzeile (<TR>) als HTML-String.

    role: 'pk' (Primaerschluessel), 'fk' (Fremdschluessel), 'pkfk' (beides), 'attr'.
    note: zusaetzlicher HTML-Text rechts vom Spaltennamen (z. B. ein farbiges 'NULL').
    port: Graphviz-Port-Name (Default: der Spaltenname) -- fuer Kanten an diese Zeile.
    bg:   Hintergrundfarbe der Zelle.
    """
    port = port or name
    bgattr = f' BGCOLOR="{bg}"' if bg else ""
    if role == "pk":
        inner = f'<FONT COLOR="{PK_GOLD}"><B><U>{name}</U></B></FONT>&nbsp;&nbsp;<FONT COLOR="{PK_GOLD}">PK</FONT>'
    elif role == "fk":
        inner = f'<FONT COLOR="{FK_ORANGE}"><I>{name}</I></FONT>&nbsp;&nbsp;<FONT COLOR="{FK_ORANGE}">FK</FONT>'
    elif role == "pkfk":
        inner = (f'<FONT COLOR="{PK_GOLD}"><B><U>{name}</U></B></FONT>'
                 f'&nbsp;&nbsp;<FONT COLOR="{PK_GOLD}">PK</FONT> <FONT COLOR="{FK_ORANGE}">FK</FONT>')
    else:
        inner = f'<FONT COLOR="{ATTR_GRAU}">{name}</FONT>'
    if note:
        inner += f'&nbsp;&nbsp;{note}'
    return f'        <TR><TD ALIGN="LEFT" PORT="{port}"{bgattr}>{inner}</TD></TR>'


def table_node(node_id, title, rows, title_bg=BLAU):
    """Gibt eine vollstaendige Graphviz-Knotendefinition fuer eine Tabelle zurueck.

    rows: Liste von HTML-Zeilen (siehe column()). title: angezeigter Tabellenname.
    """
    body = "\n".join(rows)
    label = (
        '<\n      <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="6">\n'
        f'        <TR><TD BGCOLOR="{title_bg}"><FONT COLOR="white"><B>{title}</B></FONT></TD></TR>\n'
        f'{body}\n'
        '      </TABLE>>'
    )
    return f'  {node_id} [label={label}];'


def plain_entity(node_id, title, fill="#dbe6f2"):
    """Eine schlichte Entitaet (Schritt 1 eines ERD-Aufbaus) -- nur ein Kasten mit Namen."""
    return (f'  {node_id} [shape=box, style="rounded,filled", fillcolor="{fill}", '
            f'color="{BLAU}", penwidth=1.6, fontname="{FONT}", fontsize=14, '
            f'height=0.6, label="{title}"];')


def edge(src, dst, src_port=None, dst_port=None, tail=ONE, head=ZERO_MANY,
         label=None, style="solid", color=BLAU, label_color=FK_ORANGE):
    """Eine Beziehungskante mit Kardinalitaets-Endsymbolen.

    tail/head: Endsymbol an Quelle bzw. Ziel (siehe ONE/MANY/... oben).
    """
    s = f"{src}:{src_port}" if src_port else src
    d = f"{dst}:{dst_port}" if dst_port else dst
    attrs = [f'dir=both', f'arrowtail={tail}', f'arrowhead={head}',
             f'color="{color}"', 'penwidth=1.5', f'style={style}']
    if label:
        attrs += [f'label="{label}"', f'fontname="{FONT}"', 'fontsize=12',
                  f'fontcolor="{label_color}"']
    return f'  {s} -> {d} [{", ".join(attrs)}];'


def _wrap(body, rankdir="LR", graph_label=None, **graph_attrs):
    ga = {
        "bgcolor": "white",
        "rankdir": rankdir,
        "nodesep": "0.55",
        "ranksep": "0.9",
        "fontname": FONT,
        "splines": "spline",
    }
    ga.update(graph_attrs)
    if graph_label:
        ga.update({"label": graph_label, "labelloc": "t", "fontsize": "16"})
    head = " ".join(f'{k}="{v}"' for k, v in ga.items())
    return (f"digraph G {{\n  graph [{head}];\n"
            f'  node [shape=plaintext, fontname="{FONT}", fontsize=12];\n'
            f'  edge [fontname="{FONT}"];\n{body}\n}}\n')


def render(body_or_full, out_filename, dpi=200, rankdir="LR", graph_label=None,
           is_full=False, **graph_attrs):
    """Rendert einen Graphen nach Grafiken/<out_filename> mittels `dot`.

    body_or_full: entweder der Rumpf (Knoten/Kanten) -> wird in digraph{} gehuellt,
                  oder bei is_full=True bereits ein vollstaendiges digraph{...}.
    """
    _require_dot()
    src = body_or_full if is_full else _wrap(body_or_full, rankdir=rankdir,
                                             graph_label=graph_label, **graph_attrs)
    out = os.path.join(GRAFIKEN_DIR, out_filename)
    with tempfile.NamedTemporaryFile("w", suffix=".dot", delete=False) as fh:
        fh.write(src)
        dot_path = fh.name
    try:
        subprocess.run(["dot", "-Tpng", f"-Gdpi={dpi}", dot_path, "-o", out], check=True)
    finally:
        os.unlink(dot_path)
    print(f"→ geschrieben: {out}")
    return out


def render_packed(subgraph_bodies, out_filename, columns=3, dpi=200, rankdir="LR"):
    """Mehrere kleine Graphen nebeneinander packen (gvpack) und als ein PNG rendern.

    subgraph_bodies: Liste von (graph_label, body)-Tupeln.
    """
    _require_dot()
    if shutil.which("gvpack") is None or shutil.which("neato") is None:
        raise SystemExit("Fuer gepackte Grafiken werden 'gvpack' und 'neato' benoetigt "
                         "(Teil von Graphviz: brew install graphviz).")
    laid_out = []
    tmpfiles = []
    try:
        for i, (lbl, body) in enumerate(subgraph_bodies):
            src = _wrap(body, rankdir=rankdir, graph_label=lbl)
            with tempfile.NamedTemporaryFile("w", suffix=f"_{i}.dot", delete=False) as fh:
                fh.write(src)
                tmpfiles.append(fh.name)
            # vor-layouten als .dot, damit gvpack/neato -n2 nur noch anordnen muessen
            laid = subprocess.run(["dot", "-Tdot", fh.name], capture_output=True, text=True,
                                  check=True).stdout
            with tempfile.NamedTemporaryFile("w", suffix=f"_{i}_laid.dot", delete=False) as fh2:
                fh2.write(laid)
                tmpfiles.append(fh2.name)
                laid_out.append(fh2.name)
        packed = subprocess.run(["gvpack", f"-array_il{columns}"] + laid_out,
                                capture_output=True, text=True, check=True).stdout
        with tempfile.NamedTemporaryFile("w", suffix="_packed.dot", delete=False) as fh3:
            fh3.write(packed)
            tmpfiles.append(fh3.name)
            packed_path = fh3.name
        out = os.path.join(GRAFIKEN_DIR, out_filename)
        subprocess.run(["neato", "-n2", "-Tpng", f"-Gdpi={dpi}", packed_path, "-o", out],
                       check=True)
    finally:
        for f in tmpfiles:
            try:
                os.unlink(f)
            except OSError:
                pass
    print(f"→ geschrieben: {out}")
    return out
