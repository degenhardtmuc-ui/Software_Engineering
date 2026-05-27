import random


def spieler_gibt_zahlen():
    spielerzahlen = []

    while len(spielerzahlen) < 6:
        zahl = int(input("Gib eine Zahl zwischen 1 und 49 ein: "))

        if zahl < 1 or zahl > 49:
            print("Die Zahl muss zwischen 1 und 49 sein.")

        elif zahl in spielerzahlen:
            print("Diese Zahl hast du schon eingegeben.")

        else:
            spielerzahlen.append(zahl)

    return spielerzahlen


def computer_generiert_zahlen():
    computerzahlen = []

    while len(computerzahlen) < 6:
        zahl = random.randint(1, 49)

        if zahl not in computerzahlen:
            computerzahlen.append(zahl)

    return computerzahlen


def gemeinsame_zahlen_finden(spielerzahlen, computerzahlen):
    gemeinsame_zahlen = []

    for zahl in spielerzahlen:
        if zahl in computerzahlen:
            gemeinsame_zahlen.append(zahl)

    return gemeinsame_zahlen


def ergebnis_auswerten(gemeinsame_zahlen):
    anzahl_richtige = len(gemeinsame_zahlen)

    if anzahl_richtige < 3:
        return []

    elif anzahl_richtige == 3:
        return [3, 100]

    elif anzahl_richtige == 4:
        return [4, 1000]

    elif anzahl_richtige == 5:
        return [5, 10000]

    else:
        return [6, 100000]


def lotto_spiel_starten():
    spielerzahlen = spieler_gibt_zahlen()

    computerzahlen = computer_generiert_zahlen()

    gemeinsame_zahlen = gemeinsame_zahlen_finden(spielerzahlen, computerzahlen)

    ergebnis = ergebnis_auswerten(gemeinsame_zahlen)

    print()
    print("Deine Zahlen:", spielerzahlen)
    print("Computerzahlen:", computerzahlen)
    print("Gemeinsame Zahlen:", gemeinsame_zahlen)
    print("Ergebnis:", ergebnis)


lotto_spiel_starten()
