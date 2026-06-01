"""Zwei Tabellen, ueber einen Fremdschluessel verbunden -- in reinem Python.

Zeigt: Fremdschluessel = Spalte, die auf den Primaerschluessel einer anderen
       Tabelle zeigt.  Was "referentielle Integritaet" bedeutet -- und was
       passiert, wenn sie fehlt (verwaister Datensatz).
"""

# 1:n -- eine Kundin, viele Bestellungen.
kunde = {
    1: {"name": "Anna Mueller"},
    2: {"name": "Max Schmidt"},
}

bestellung = [
    {"bestell_id": 10, "kunde_id": 1, "betrag": 89.95},
    {"bestell_id": 11, "kunde_id": 1, "betrag": 109.00},
    {"bestell_id": 12, "kunde_id": 2, "betrag": 135.50},
    {"bestell_id": 13, "kunde_id": 99, "betrag": 60.00},   # kunde_id 99 gibt es nicht -> verwaist!
]


def fremdschluessel_pruefen(bestellungen, kunden):
    """Genau das erzwingt ein DBMS automatisch: jeder FK muss auf eine echte Zeile zeigen."""
    fehler = [b for b in bestellungen if b["kunde_id"] not in kunden]
    return fehler


verwaist = fremdschluessel_pruefen(bestellung, kunde)
print("Verwaiste Bestellungen (FK zeigt ins Leere):")
for b in verwaist:
    print("  ", b, "  <- kunde_id existiert nicht!")
print("Ein DBMS mit FOREIGN KEY haette diese Zeile gar nicht erst zugelassen.\n")

# Beziehung "ausnutzen": pro Kundin ihre Bestellungen + Gesamtsumme.
print("Bestelluebersicht je Kundin:")
for kid, daten in kunde.items():
    meine = [b for b in bestellung if b["kunde_id"] == kid]
    summe = sum(b["betrag"] for b in meine)
    print(f"  {daten['name']}: {len(meine)} Bestellung(en), gesamt {summe:.2f} EUR")

# --- Variante zum Live-Einkommentieren: n:m braucht eine Zwischentabelle -------
# produkt = {1: "Eco-Sneaker", 2: "Hemp-High", 3: "Bambus-Boot"}
# bestellposition = [
#     {"bestell_id": 10, "produkt_id": 1, "anzahl": 1},
#     {"bestell_id": 10, "produkt_id": 2, "anzahl": 1},
#     {"bestell_id": 11, "produkt_id": 3, "anzahl": 2},
# ]
# # -> jede Position hat ZWEI Fremdschluessel: einen auf bestellung, einen auf produkt.
