# Veggie Soles — Online-Shop für vegane Turnschuhe

Die durchgehende Erzählwelt für Beispiele in Notebooks, Foliensätzen
und Live-Demo-Code. Sorgt dafür, dass Studierende über das Semester
hinweg dieselben Produkte, Kund:innen und Datensätze wiedersehen —
und Konzepte (Variablen, Listen, Dictionaries, DataFrames, SQL-Tabellen)
auf vertraute Inhalte mappen können.

## Stammprodukte

| Produkt | Preis | Beschreibung |
|---|---|---|
| Eco-Sneaker | 89.95 € | Klassischer Low-Cut, recyceltes Polyester |
| Hemp-High | 109.00 € | Knöchelhoch, Obermaterial aus Hanf |
| Bambus-Boot | 135.50 € | Winterfest, Bambusfaser-Innenfutter |

## Stamm-Kund:innen

| Name | E-Mail | Notiz |
|---|---|---|
| Anna Müller | anna@example.de | Stammkundin, kauft regelmäßig Eco-Sneaker |
| Max Schmidt | max@example.de | Erste Bestellung, Hemp-High |

## Konventionen

- **Geldbeträge** in Euro (`89.95`, nicht `89,95`) — Float, kein String
- **E-Mail-Adressen** auf `@example.de` (RFC-konformer Reserved Domain)
- **IDs** beginnen bei 1 (Produkt-IDs, Bestell-IDs)

## Wachstum

Diese Welt wächst organisch. Wenn ein Notebook/Foliensatz neue
Personen, Produkte, Datensätze oder Geschäftslogik braucht, werden
sie hier ergänzt — bevor sie in den Lehrmaterialien auftauchen.
So bleibt die Welt konsistent und Konflikte (zwei Kund:innen mit
demselben Namen, zwei Produkte mit derselben ID) werden früh sichtbar.

## Datensätze

Wenn Datensätze für Pandas/SQLite-Übungen entstehen, landen sie
unter `Beispiele/_data/` (geplant ab Phase 4 der Lerninhalte).
