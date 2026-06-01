"""Erzeugt die ER-Diagramm-Notationsuebersicht fuer Foliensatz 21b mit Graphviz.

Erzeugt:
  Grafiken/21b_erd_notation.png  -- ein kleines Beispiel-ERD (kunde — bestellung) plus
                                    eine Legende: was PK / FK bedeuten und welche
                                    Kraehenfuss-Symbole es gibt.

Benoetigt das Graphviz-CLI:  brew install graphviz
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from erd_dot_helpers import (table_node, column, edge, render, BLAU, FK_ORANGE,
                             PK_GOLD, ATTR_GRAU, ONE, ZERO_MANY)


def _legende_node():
    rows = [
        '<TR><TD COLSPAN="2" BGCOLOR="#555555"><FONT COLOR="white"><B>Legende</B></FONT></TD></TR>',
        f'<TR><TD ALIGN="LEFT"><FONT COLOR="{PK_GOLD}"><B><U>spalte</U></B></FONT> <FONT COLOR="{PK_GOLD}">PK</FONT></TD>'
        '<TD ALIGN="LEFT">Primärschlüssel — eindeutig, nie NULL</TD></TR>',
        f'<TR><TD ALIGN="LEFT"><FONT COLOR="{FK_ORANGE}"><I>spalte</I></FONT> <FONT COLOR="{FK_ORANGE}">FK</FONT></TD>'
        '<TD ALIGN="LEFT">Fremdschlüssel — zeigt auf einen PK</TD></TR>',
        '<TR><TD ALIGN="LEFT"><FONT FACE="monospace">——||</FONT></TD><TD ALIGN="LEFT">genau eins</TD></TR>',
        '<TR><TD ALIGN="LEFT"><FONT FACE="monospace">——o|</FONT></TD><TD ALIGN="LEFT">null oder eins</TD></TR>',
        '<TR><TD ALIGN="LEFT"><FONT FACE="monospace">&gt;|——</FONT></TD><TD ALIGN="LEFT">eins oder viele</TD></TR>',
        '<TR><TD ALIGN="LEFT"><FONT FACE="monospace">&gt;o——</FONT></TD><TD ALIGN="LEFT">null oder viele</TD></TR>',
    ]
    label = ('<\n      <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="6">\n        '
             + "\n        ".join(rows) + "\n      </TABLE>>")
    return f'  legende [shape=plaintext, fontsize=13, label={label}];'


if __name__ == "__main__":
    kunde = table_node("kunde", "kunde", [
        column("kunde_id", "pk"), column("name", "attr"), column("email", "attr")])
    bestellung = table_node("bestellung", "bestellung", [
        column("bestell_id", "pk"), column("kunde_id", "fk"), column("datum", "attr")])
    body = "\n".join([
        kunde, bestellung, _legende_node(),
        edge("kunde", "bestellung", "kunde_id", "kunde_id", ONE, ZERO_MANY, label="gibt auf"),
        '  bestellung -> legende [style=invis];',
    ])
    render(body, "21b_erd_notation.png", rankdir="LR", nodesep="0.7", ranksep="1.0",
           graph_label="ER-Diagramm: ein kleines Beispiel und die Notation")
