# Lotto-Spiel ohne random
# Computer hat 3 feste Tipp-Reihen


def spieler_gibt_zahlen():
    spieler_zahlen = []

    while len(spieler_zahlen) < 6:
        zahl = int(input("Gib eine Zahl zwischen 1 und 49 ein: "))

        if zahl >= 1 and zahl <= 49:
            if zahl not in spieler_zahlen:
                spieler_zahlen.append(zahl)
            else:
                print("Diese Zahl hast du schon eingegeben.")
        else:
            print("Die Zahl muss zwischen 1 und 49 sein.")

    return spieler_zahlen


def computer_generiert_zahlen():
    computer_zahlen = [
        [1, 3, 4, 33, 40, 47],
        [2, 13, 24, 38, 41, 48],
        [3, 7, 12, 22, 44, 45]
    ]

    return computer_zahlen


def gemeinsame_zahlen_finden(spieler_zahlen, computer_zahlen):
    alle_treffer = []

    index = 0

    while index < len(computer_zahlen):
        eine_reihe = computer_zahlen[index]
        treffer = []

        zahl_index = 0

        while zahl_index < len(spieler_zahlen):
            zahl = spieler_zahlen[zahl_index]

            if zahl in eine_reihe:
                treffer.append(zahl)

            zahl_index = zahl_index + 1

        alle_treffer.append(treffer)

        index = index + 1

    return alle_treffer


def ergebnis_auswerten(alle_treffer):
    index = 0

    while index < len(alle_treffer):
        treffer = alle_treffer[index]

        print("Reihe", index + 1, "Treffer:", treffer)

        if len(treffer) > 3:
            print("Gewonnen!")
        else:
            print("Nicht gewonnen.")

        index = index + 1


def lotto_spiel_starten():
    spieler_zahlen = spieler_gibt_zahlen()
    computer_zahlen = computer_generiert_zahlen()
    alle_treffer = gemeinsame_zahlen_finden(spieler_zahlen, computer_zahlen)

    print("Deine Zahlen:", spieler_zahlen)
    print("Computer-Zahlen:", computer_zahlen)

    ergebnis_auswerten(alle_treffer)


lotto_spiel_starten()