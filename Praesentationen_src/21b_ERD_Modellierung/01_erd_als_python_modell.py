"""Das Veggie-Soles-ER-Diagramm, als Python-Datenmodell nachgebaut.

Jede Entität wird eine Sammlung von Zeilen, jeder Fremdschluessel ein Verweis
ueber eine ID. So sieht man, dass das ERD nicht abstrakt ist -- es ist genau
die Struktur, mit der wir gleich (NB 22/23) per SQL arbeiten.
Verwendet nur Listen/Dicts/Funktionen aus den Notebooks 06/07/10.
"""

# --- Entitäten (jeweils {PK: zeile}) -----------------------------------------
kunde = {
    1: {"name": "Anna Mueller", "email": "anna@example.de"},
    2: {"name": "Max Schmidt",  "email": "max@example.de"},
}
produkt = {
    1: {"name": "Eco-Sneaker", "preis": 89.95},
    2: {"name": "Hemp-High",   "preis": 109.00},
    3: {"name": "Bambus-Boot", "preis": 135.50},
}
# bestellung: FK kunde_id zeigt auf kunde
bestellung = {
    10: {"kunde_id": 1, "datum": "2026-05-03"},
    11: {"kunde_id": 1, "datum": "2026-05-09"},
    12: {"kunde_id": 2, "datum": "2026-05-10"},
}
# bestellposition: loest n:m zwischen bestellung und produkt auf -> ZWEI Fremdschluessel
bestellposition = [
    {"bestell_id": 10, "produkt_id": 1, "anzahl": 1},
    {"bestell_id": 10, "produkt_id": 2, "anzahl": 1},
    {"bestell_id": 11, "produkt_id": 3, "anzahl": 2},
    {"bestell_id": 12, "produkt_id": 1, "anzahl": 3},
]
# rechnung: 1:1 zu bestellung (FK bestell_id, hier auch eindeutig)
rechnung = {
    100: {"bestell_id": 10, "betrag": 198.95},
    101: {"bestell_id": 11, "betrag": 271.00},
    102: {"bestell_id": 12, "betrag": 269.85},
}


def bestellung_report(bestell_id):
    """Navigiert die ganze ERD-Kette: Bestellung -> Kundin, Positionen -> Produkte, Rechnung."""
    b = bestellung[bestell_id]
    kundin = kunde[b["kunde_id"]]                                  # FK auf kunde
    positionen = [p for p in bestellposition if p["bestell_id"] == bestell_id]
    re = next(r for r in rechnung.values() if r["bestell_id"] == bestell_id)  # 1:1

    print(f"Bestellung {bestell_id} vom {b['datum']}  --  {kundin['name']}")
    summe = 0.0
    for p in positionen:
        prod = produkt[p["produkt_id"]]                            # FK auf produkt
        zeile = p["anzahl"] * prod["preis"]
        summe += zeile
        print(f"  {p['anzahl']} x {prod['name']:14s} a {prod['preis']:7.2f} EUR  =  {zeile:8.2f} EUR")
    print(f"  Summe (berechnet): {summe:8.2f} EUR   |   Rechnungsbetrag: {re['betrag']:.2f} EUR")
    print()


for bid in bestellung:
    bestellung_report(bid)

# --- Variante zum Live-Einkommentieren: was ohne die Zwischentabelle fehlt -----
# # Ohne bestellposition koennte eine Bestellung nur EIN Produkt haben (1:n statt n:m).
# # Probier mal, Bestellung 10 (Eco-Sneaker UND Hemp-High) ohne Zwischentabelle abzubilden -- geht nicht sauber.
