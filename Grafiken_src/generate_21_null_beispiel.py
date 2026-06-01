"""Erzeugt das NULL-Beispiel fuer Foliensatz 21 mit Graphviz.

Erzeugt:
  Grafiken/21_null_beispiel.png  -- eine kleine kunde-Datentabelle, in der eine Zeile
                                    email = NULL orange hervorgehoben ist, plus ein
                                    Hinweis-Kasten daneben.

Benoetigt das Graphviz-CLI:  brew install graphviz
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from erd_dot_helpers import render, BLAU, FK_ORANGE, ATTR_GRAU, NULL_BG, FONT

# kunde-Datentabelle (eine Zeile pro Datensatz): (kunde_id, name, email-oder-None)
ZEILEN = [
    ("1", "Anna Müller", "anna@example.de"),
    ("2", "Max Schmidt", "max@example.de"),
    ("3", "Lena Weber", None),          # E-Mail noch unbekannt -> NULL
]
SPALTEN = ("kunde_id", "name", "email")


def _kunde_node():
    head = "<TR>" + "".join(
        f'<TD BGCOLOR="{BLAU}"><FONT COLOR="white"><B>{c}</B></FONT></TD>' for c in SPALTEN
    ) + "</TR>"
    trs = [head]
    for kid, name, email in ZEILEN:
        if email is None:
            mailcell = (f'<TD PORT="nullcell" BGCOLOR="{NULL_BG}">'
                        f'<FONT COLOR="{FK_ORANGE}"><B>NULL</B></FONT></TD>')
        else:
            mailcell = f'<TD><FONT COLOR="{ATTR_GRAU}">{email}</FONT></TD>'
        trs.append(f'<TR><TD><FONT COLOR="{ATTR_GRAU}">{kid}</FONT></TD>'
                   f'<TD><FONT COLOR="{ATTR_GRAU}">{name}</FONT></TD>{mailcell}</TR>')
    label = ('<\n      <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="7">\n        '
             + "\n        ".join(trs) + "\n      </TABLE>>")
    return f'  kunde [shape=plaintext, label={label}];'


def _hinweis_node():
    text = ('NULL = hier steht (noch) kein Wert\\l'
            'nicht 0  ·  nicht leerer Text  ·  nicht False\\l'
            'Abfrage:  WHERE email IS NULL\\l'
            'NICHT  WHERE email = NULL  (findet nichts!)\\l')
    return (f'  hinweis [shape=note, style=filled, fillcolor="#fff6e0", color="{FK_ORANGE}", '
            f'fontname="{FONT}", fontsize=11, fontcolor="{ATTR_GRAU}", label="{text}"];')


if __name__ == "__main__":
    body = "\n".join([
        _kunde_node(),
        _hinweis_node(),
        f'  kunde:nullcell -> hinweis [color="{FK_ORANGE}", style=dashed, penwidth=1.4, '
        'arrowhead=vee];',
    ])
    render(body, "21_null_beispiel.png", rankdir="LR", nodesep="0.6", ranksep="0.9")
