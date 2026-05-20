# Mini-Workshop: Code Cleanup
# Aufgabe:
# Der ursprüngliche Code hatte ungültige bzw. unsaubere Variablennamen.
# In Python verwendet man normalerweise "snake_case":
# kleine Buchstaben und Wörter werden mit Unterstrichen verbunden.

# Anzahl der Teilnehmer
anzahl_der_teilnehmer = 10

# Preisgeld für den 1. und 2. Platz
# Wichtig:
# Variablennamen dürfen NICHT mit einer Zahl anfangen.
# Deshalb ist "1terPlatz" falsch.
# Besser: "preisgeld_platz_1"
preisgeld_platz_1 = 500
preisgeld_platz_2 = 250

# Gesamtes Preisgeld
# "GesamtesPreisgeld" funktioniert zwar technisch,
# entspricht aber nicht der üblichen Python-Schreibweise.
# Besser ist snake_case:
gesamtes_preisgeld = 1000

# Summe der Preisgelder für die ersten beiden Plätze
summe_preisgelder_platz_1_und_2 = preisgeld_platz_1 + preisgeld_platz_2

# Übriges Preisgeld nach Platz 1 und Platz 2
restliches_preisgeld = gesamtes_preisgeld - summe_preisgelder_platz_1_und_2

# Ausgabe zur Kontrolle
print("Anzahl der Teilnehmer:", anzahl_der_teilnehmer)
print("Preisgeld 1. Platz:", preisgeld_platz_1, "Euro")
print("Preisgeld 2. Platz:", preisgeld_platz_2, "Euro")
print("Gesamtes Preisgeld:", gesamtes_preisgeld, "Euro")
print("Summe Platz 1 und 2:", summe_preisgelder_platz_1_und_2, "Euro")
print("Restliches Preisgeld:", restliches_preisgeld, "Euro")

