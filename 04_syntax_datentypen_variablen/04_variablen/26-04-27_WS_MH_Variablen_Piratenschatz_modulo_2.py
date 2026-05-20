# 04_variablen_piraten_modulo.py
# Mini-Workshop: Piraten
# Thema: Variablen, Ganzzahldivision // und Modulo %

# Ausgangssituation:
# Es gibt 7 Piraten und 1 Kapitän.
anzahl_piraten = 7
anzahl_kapitaen = 1

# Insgesamt sind es also 8 Personen.
anzahl_personen = anzahl_piraten + anzahl_kapitaen

# Der Schatz besteht aus 1000 Golddublonen.
schatz = 1000

# // bedeutet Ganzzahldivision.
# Das Ergebnis hat keine Nachkommastellen.
# 1000 // 8 = 125
anteil_pro_person = schatz // anzahl_personen

# % bedeutet Modulo.
# Modulo berechnet den Rest einer Division.
# 1000 % 8 = 0
rest_fuer_kapitaen = schatz % anzahl_personen

# Der Kapitän bekommt seinen normalen Anteil plus den Rest.
kapitaen_bekommt = anteil_pro_person + rest_fuer_kapitaen

print("Ausgangssituation:")
print("Personen insgesamt:", anzahl_personen)
print("Jeder Pirat bekommt:", anteil_pro_person, "Golddublonen")
print("Der Kapitän bekommt extra:", rest_fuer_kapitaen, "Golddublonen")
print("Der Kapitän bekommt insgesamt:", kapitaen_bekommt, "Golddublonen")

print()

# Neue Situation:
# Die Piratenbande nimmt 3 neue Piraten-Lehrlinge auf.
anzahl_piraten = anzahl_piraten + 3

# Weil sich die Anzahl der Piraten geändert hat,
# müssen wir die Gesamtzahl neu berechnen.
anzahl_personen = anzahl_piraten + anzahl_kapitaen

# Auch Anteil, Rest und Kapitäns-Anteil müssen neu berechnet werden.
anteil_pro_person = schatz // anzahl_personen
rest_fuer_kapitaen = schatz % anzahl_personen
kapitaen_bekommt = anteil_pro_person + rest_fuer_kapitaen

print("Nach Aufnahme von 3 Piraten-Lehrlingen:")
print("Personen insgesamt:", anzahl_personen)
print("Jeder Pirat bekommt:", anteil_pro_person, "Golddublonen")
print("Der Kapitän bekommt extra:", rest_fuer_kapitaen, "Golddublonen")
print("Der Kapitän bekommt insgesamt:", kapitaen_bekommt, "Golddublonen")