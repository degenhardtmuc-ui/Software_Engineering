# piraten_beute_variablen.py
# Mini-Workshop: Piraten
# Thema: Variablen, Ganzzahldivision (//) und Modulo (%)

# Ausgangssituation:
# Es gibt 7 Piraten und 1 Kapitän.
# Zusammen sind das 8 Personen.
anzahl_piraten = 7
anzahl_kapitaen = 1
anzahl_personen = anzahl_piraten + anzahl_kapitaen

# Der Schatz besteht aus 1000 Golddublonen.
schatz = 1000

# Jeder bekommt zuerst den gleichen Anteil.
# // bedeutet: ganzzahlige Division ohne Nachkommastellen.
# Beispiel: 1000 // 8 = 125
anteil_pro_person = schatz // anzahl_personen

# % bedeutet Modulo.
# Modulo ist der Rest einer Division.
# Beispiel: 1000 % 8 = 0, weil 1000 glatt durch 8 teilbar ist.
rest_fuer_kapitaen = schatz % anzahl_personen

# Der Kapitän bekommt den normalen Anteil plus den Rest.
kapitaen_bekommt = anteil_pro_person + rest_fuer_kapitaen

print("Ausgangssituation:")
print("Personen insgesamt:", anzahl_personen)
print("Jeder Pirat bekommt:", anteil_pro_person, "Golddublonen")
print("Der Kapitän bekommt extra:", rest_fuer_kapitaen, "Golddublonen")
print("Der Kapitän bekommt insgesamt:", kapitaen_bekommt, "Golddublonen")

print()  # Leerzeile für bessere Lesbarkeit

# Neue Situation:
# Die Piratenbande nimmt 3 neue Piraten-Lehrlinge auf.
# Wir verändern die bestehende Variable anzahl_piraten.
anzahl_piraten = anzahl_piraten + 3

# Die Piratenbande nimmt 3 neue Piraten-Lehrlinge auf.
anzahl_piraten = anzahl_piraten + 3

# Wichtig:
# Die Gesamtzahl muss neu berechnet werden,
# weil sich die Anzahl der Piraten verändert hat.
anzahl_personen = anzahl_piraten + anzahl_kapitaen

# Auch der Anteil und der Rest müssen neu berechnet werden.
anteil_pro_person = schatz // anzahl_personen
rest_fuer_kapitaen = schatz % anzahl_personen
kapitaen_bekommt = anteil_pro_person + rest_fuer_kapitaen

print("Nach Aufnahme von 3 Piraten-Lehrlingen:")
print("Personen insgesamt:", anzahl_personen)
print("Jeder Pirat bekommt:", anteil_pro_person, "Golddublonen")
print("Der Kapitän bekommt extra:", rest_fuer_kapitaen, "Golddublonen")
print("Der Kapitän bekommt insgesamt:", kapitaen_bekommt, "Golddublonen")
Nach Aufnahme von 3 Piraten-Lehrlingen:
Personen insgesamt: 11
Jeder Pirat bekommt: 90 Golddublonen
Der Kapitän bekommt extra: 10 Golddublonen
Der Kapitän bekommt insgesamt: 100 Golddublonen