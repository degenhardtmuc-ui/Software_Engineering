import random


class Lotterie:
    """A simple lottery game with random numbers."""

    def __init__(self):
        self.spieler_zahlen = []
        self.lotto_zahlen = []
        self.treffer = []

    def spieler_zahlen_eingeben(self):
        print("Bitte gib 6 verschiedene Zahlen von 1 bis 49 ein.")

        while len(self.spieler_zahlen) < 6:
            zahl_text = input("Zahl eingeben: ")

            if not zahl_text.isdigit():
                print("Bitte nur ganze Zahlen eingeben.")
                continue

            zahl = int(zahl_text)

            if zahl < 1 or zahl > 49:
                print("Die Zahl muss zwischen 1 und 49 liegen.")

            elif zahl in self.spieler_zahlen:
                print("Diese Zahl hast du schon eingegeben.")

            else:
                self.spieler_zahlen.append(zahl)
                print("Deine Zahlen bisher:", self.spieler_zahlen)

        self.spieler_zahlen.sort()

    def lotto_zahlen_ziehen(self):
        self.lotto_zahlen = random.sample(range(1, 50), 6)
        self.lotto_zahlen.sort()

    def treffer_suchen(self):
        for zahl in self.spieler_zahlen:
            if zahl in self.lotto_zahlen:
                self.treffer.append(zahl)

    def ergebnis_anzeigen(self):
        print()
        print("Deine Zahlen:", self.spieler_zahlen)
        print("Lottozahlen:", self.lotto_zahlen)
        print("Treffer:", self.treffer)
        print("Anzahl Treffer:", len(self.treffer))

        if len(self.treffer) == 6:
            print("Jackpot! 6 Richtige!")

        elif len(self.treffer) == 5:
            print("Sehr gut! 5 Richtige!")

        elif len(self.treffer) == 4:
            print("Gut! 4 Richtige!")

        elif len(self.treffer) == 3:
            print("Nicht schlecht! 3 Richtige!")

        else:
            print("Leider kein großer Gewinn.")

    def spiel_starten(self):
        self.spieler_zahlen_eingeben()
        self.lotto_zahlen_ziehen()
        self.treffer_suchen()
        self.ergebnis_anzeigen()


spiel = Lotterie()
spiel.spiel_starten()