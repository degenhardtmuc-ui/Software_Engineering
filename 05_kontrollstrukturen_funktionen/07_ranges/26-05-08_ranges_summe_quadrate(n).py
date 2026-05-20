Aufgabe 2:
# Schreibe sum_squares(n),
# welche die Summe der ersten n Quadratzahlen zurückgibt.
# ---------------------------------------------------------

def sum_squares(n):
    summe = 0

    for zahl in range(1, n + 1):
        summe = summe + zahl ** 2

    return summe


# Test für Aufgabe 2
print("Aufgabe 2: Summe der Quadrate von 1 bis 10")
print(sum_squares(10))