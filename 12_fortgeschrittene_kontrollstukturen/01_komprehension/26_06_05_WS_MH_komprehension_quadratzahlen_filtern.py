# Workshop: Listen-Komprehension
# Thema: Quadratzahlen und Filtern

numbers = [1, 7, 4, 87, 23]

quadratzahlen = [zahl * zahl for zahl in numbers]
print("Quadratzahlen:", quadratzahlen)


def quadriere(zahlen):
    """Return a new list with every number squared."""
    return [zahl * zahl for zahl in zahlen]


print("Quadratzahlen mit Funktion:", quadriere(numbers))

groesser_als_10 = [zahl for zahl in numbers if zahl > 10]
print("Zahlen groesser als 10:", groesser_als_10)

# Kleine Kontrolle fuer mich:
assert quadratzahlen == [1, 49, 16, 7569, 529]
assert quadriere([2, 3, 4]) == [4, 9, 16]
assert groesser_als_10 == [87, 23]

print("Alle Kontrollen sind okay.")