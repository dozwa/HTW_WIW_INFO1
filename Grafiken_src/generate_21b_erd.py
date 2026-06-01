"""Erzeugt die ER-Diagramme fuer Foliensatz 21b (ERD-Vertiefung) mit Graphviz (`dot`).

Erzeugt:
  Grafiken/21b_erd_veggiesoles.png        -- vollstaendiges Veggie-Soles-Datenmodell
  Grafiken/21b_erd_schritt1.png ... 3.png -- die ersten drei Aufbau-Schritte einzeln (gross)
  Grafiken/21b_erd_zwischentabelle.png    -- Schritt 4: n:m mit Zwischentabelle aufgeloest
  Grafiken/21b_erd_schluesselattribut.png -- PK + FK an einem kleinen Beispiel

Benoetigt das Graphviz-CLI:  brew install graphviz
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from erd_dot_helpers import (table_node, plain_entity, edge, column, render,
                             ONE, ZERO_MANY)

# --- Tabellen-Definitionen des Veggie-Soles-Modells --------------------------
KUNDE = table_node("kunde", "kunde", [
    column("kunde_id", "pk"),
    column("name", "attr"),
    column("email", "attr"),
    column("newsletter", "attr"),
])
BESTELLUNG = table_node("bestellung", "bestellung", [
    column("bestell_id", "pk"),
    column("kunde_id", "fk"),
    column("datum", "attr"),
])
RECHNUNG = table_node("rechnung", "rechnung", [
    column("rechnung_id", "pk"),
    column("bestell_id", "fk"),
    column("betrag", "attr"),
])
BESTELLPOSITION = table_node("bestellposition", "bestellposition", [
    column("position_id", "pk"),
    column("bestell_id", "fk"),
    column("produkt_id", "fk"),
    column("anzahl", "attr"),
])
PRODUKT = table_node("produkt", "produkt", [
    column("produkt_id", "pk"),
    column("name", "attr"),
    column("preis", "attr"),
])


def voll():
    body = "\n".join([
        KUNDE, BESTELLUNG, RECHNUNG, BESTELLPOSITION, PRODUKT,
        edge("kunde", "bestellung", "kunde_id", "kunde_id", ONE, ZERO_MANY, label="gibt auf"),
        edge("bestellung", "rechnung", "bestell_id", "bestell_id", ONE, ONE, label="hat"),
        edge("bestellung", "bestellposition", "bestell_id", "bestell_id", ONE, ZERO_MANY, label="enthält"),
        edge("produkt", "bestellposition", "produkt_id", "produkt_id", ONE, ZERO_MANY, label="steht in"),
    ])
    render(body, "21b_erd_veggiesoles.png", rankdir="LR", nodesep="0.6", ranksep="1.1")


def schritt1():
    body = "\n".join([
        plain_entity("kunde", "kunde"),
        plain_entity("bestellung", "bestellung"),
        plain_entity("produkt", "produkt"),
        '  kunde -> bestellung [style=invis];',
        '  bestellung -> produkt [style=invis];',
    ])
    render(body, "21b_erd_schritt1.png", rankdir="LR", ranksep="1.4")


def schritt2():
    # Schritt 2: nur Attribute + PK -- noch keine Fremdschluessel (die kommen mit den Beziehungen)
    kunde = table_node("kunde", "kunde", [
        column("kunde_id", "pk"), column("name", "attr"), column("email", "attr"),
        column("newsletter", "attr")])
    bestellung = table_node("bestellung", "bestellung", [
        column("bestell_id", "pk"), column("datum", "attr")])
    produkt = table_node("produkt", "produkt", [
        column("produkt_id", "pk"), column("name", "attr"), column("preis", "attr")])
    body = "\n".join([kunde, bestellung, produkt,
                      '  kunde -> bestellung [style=invis];',
                      '  bestellung -> produkt [style=invis];'])
    render(body, "21b_erd_schritt2.png", rankdir="LR", ranksep="1.2")


def schritt3():
    k = table_node("kunde", "kunde", [column("kunde_id", "pk"), column("name", "attr")])
    b = table_node("bestellung", "bestellung", [column("bestell_id", "pk"), column("kunde_id", "fk")])
    p = table_node("produkt", "produkt", [column("produkt_id", "pk"), column("name", "attr")])
    body = "\n".join([
        k, b, p,
        edge("kunde", "bestellung", "kunde_id", "kunde_id", ONE, ZERO_MANY, label="gibt auf"),
        # n:m noch offen: gestrichelte Linie ohne Endsymbole, mit Fragezeichen
        edge("bestellung", "produkt", tail="none", head="none", label="n : m  ?",
             style="dashed", color="#c0392b", label_color="#c0392b"),
    ])
    render(body, "21b_erd_schritt3.png", rankdir="LR", nodesep="0.6", ranksep="1.1")


def schluesselattribut():
    k = table_node("kunde", "kunde", [
        column("kunde_id", "pk"), column("name", "attr"), column("email", "attr")])
    b = table_node("bestellung", "bestellung", [
        column("bestell_id", "pk"), column("kunde_id", "fk"), column("datum", "attr")])
    body = "\n".join([
        k, b,
        edge("kunde", "bestellung", "kunde_id", "kunde_id", ONE, ZERO_MANY, label="verweist auf"),
    ])
    render(body, "21b_erd_schluesselattribut.png", rankdir="LR", ranksep="1.4",
           graph_label="Primärschlüssel (PK): identifiziert jede Zeile  ·  Fremdschlüssel (FK): zeigt auf einen PK")


def zwischentabelle():
    b = table_node("bestellung", "bestellung", [column("bestell_id", "pk"), column("kunde_id", "fk")])
    p = table_node("produkt", "produkt", [column("produkt_id", "pk"), column("name", "attr")])
    bp = table_node("bestellposition", "bestellposition", [
        column("position_id", "pk"),
        column("bestell_id", "fk"),
        column("produkt_id", "fk"),
        column("anzahl", "attr", note='<FONT POINT-SIZE="9" COLOR="#888888">(eigenes Attribut der Beziehung)</FONT>'),
    ], title_bg="#7a3b9c")
    body = "\n".join([
        b, p, bp,
        edge("bestellung", "bestellposition", "bestell_id", "bestell_id", ONE, ZERO_MANY, label="1 : n"),
        edge("produkt", "bestellposition", "produkt_id", "produkt_id", ONE, ZERO_MANY, label="1 : n"),
    ])
    render(body, "21b_erd_zwischentabelle.png", rankdir="LR", nodesep="0.45", ranksep="1.1")


if __name__ == "__main__":
    voll()
    schritt1()
    schritt2()
    schritt3()
    zwischentabelle()       # = Schritt 4 (n:m aufgeloest)
    schluesselattribut()
