import os

pfad = "tagesreport_demo.txt"

file = open(pfad, "w")
file.write("Veggie Soles -- Reporting\nWas wir so auf Lager haben\n")
file.write("Eco-Sneaker 89.95 EUR\n")
file.write("Hemp-High   109.00 EUR\n")
file.write("Bambus-Boot 135.50")
file.close()

file = open(pfad, "r")
print("--- file-Inhalt ---")

inhalt = file.readlines()
print(inhalt)

n = 1
for line in inhalt:
    print("Zeile ", n, ": ", line, end="")
    n += 1

file.close()

os.remove(pfad)
print("file gelöscht")