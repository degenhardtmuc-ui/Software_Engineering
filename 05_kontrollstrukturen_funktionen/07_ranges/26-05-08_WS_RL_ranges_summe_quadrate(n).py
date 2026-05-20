# Mini-Workshop Ranges # Schreibe pring_squares(n), welche die Quadrate der Zahlen von 1 bis n ausgibt. 

# # Schreibe sum_squares(n), welche die Summe der ersten n Quadratzahlen zureuckgibt.



def print_squares(n):
    # Diese Funktion gibt die Quadrate von 1 bis n aus.
    # Beispiel bei n = 5:
    # 1, 4, 9, 16, 25

    for zahl in range(1, n + 1):
        quadrat = zahl ** 2
        print(quadrat)


def sum_squares(n):
    # Diese Funktion berechnet die Summe der ersten n Quadratzahlen.
    # Beispiel bei n = 5:
    # 1² + 2² + 3² + 4² + 5²
    # 1 + 4 + 9 + 16 + 25 = 55

    summe = 0

    for zahl in range(1, n + 1):
        quadrat = zahl ** 2
        summe = summe + quadrat

    return summe


# Testbereich
print("Quadrate von 1 bis 5:")
print_squares(5)

print("Summe der Quadrate von 1 bis 5:")
ergebnis = sum_squares(5)
print(ergebnis)

#Quadrate von 1 bis 5:
#1
#4
#9
#16
#25
# Summe der Quadrate von 1 bis 5:
# 55

    zahl ** 2
    range(1, n + 1)



# Mini-Workshop Ranges
# Datei: mini_workshop_ranges.py


# ---------------------------------------------------------
# Aufgabe 1:
# Schreibe print_squares(n),
# welche die Quadrate der Zahlen von 1 bis n ausgibt.
# ---------------------------------------------------------

def print_squares(n):
    for zahl in range(1, n + 1):
        print(zahl ** 2)


# Test für Aufgabe 1
print("Aufgabe 1: Quadrate von 1 bis 10")
print_squares(10)


# ---------------------------------------------------------
# Aufgabe 2:
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


# ---------------------------------------------------------
# Aufgabe 3:
# Teilnehmerliste ausgeben
# ---------------------------------------------------------

teilnehmer_liste = [
    "Teilnehmer1",
    "Teilnehmer2",
    "Teilnehmer3",
    "Teilnehmer4",
    "Teilnehmer5",
    "Teilnehmer6",
    "Teilnehmer7",
    "Teilnehmer8",
    "Teilnehmer9",
    "Teilnehmer10"
]

print("Aufgabe 3: Teilnehmerliste")

print("Liste hat", len(teilnehmer_liste), "Teilnehmer")

for index in range(len(teilnehmer_liste)):
    print(index + 1, ".", teilnehmer_liste[index])


# ---------------------------------------------------------
# Aufgabe 4:
# Range von 0 bis 100.
# Gib jede Zahl aus, die ein Vielfaches von 5 ist.
# ---------------------------------------------------------

print("Aufgabe 4: Vielfache von 5 von 0 bis 100")

for zahl in range(0, 101):
    if zahl % 5 == 0:
        print(zahl)