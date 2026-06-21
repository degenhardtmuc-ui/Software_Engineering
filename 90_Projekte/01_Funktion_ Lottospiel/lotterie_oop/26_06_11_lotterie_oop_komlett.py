import random  # Damit der Computer zufällige Zahlen ziehen kann.


class Lotterie:
    """Eine einfache Klasse für ein Lottospiel."""

    def __init__(self):
        """Hier werden die Listen für ein neues Spiel vorbereitet."""
        # self bedeutet: Diese Liste gehört zu diesem Spiel.
        self.spieler_zahlen = []
        self.lotto_zahlen = []
        self.treffer = []

    def spieler_zahlen_eingeben(self):
        """Der Spieler gibt 6 verschiedene Zahlen von 1 bis 49 ein."""
        print("Bitte gib 6 verschiedene Zahlen von 1 bis 49 ein.")

        while len(self.spieler_zahlen) < 6:
            zahl = int(input("Zahl eingeben: "))

            if zahl < 1 or zahl > 49:
                print("Die Zahl muss zwischen 1 und 49 sein.")

            elif zahl in self.spieler_zahlen:
                print("Diese Zahl hast du schon eingegeben.")

            else:
                self.spieler_zahlen.append(zahl)
                print("Gespeicherte Zahlen:", self.spieler_zahlen)

    def lotto_zahlen_ziehen(self):
        """Der Computer zieht 6 verschiedene Lottozahlen."""
        while len(self.lotto_zahlen) < 6:
            zahl = random.randint(1, 49)

            if zahl not in self.lotto_zahlen:
                self.lotto_zahlen.append(zahl)

    def treffer_suchen(self):
        """Die Spielerzahlen werden mit den Lottozahlen verglichen."""
        for zahl in self.spieler_zahlen:
            if zahl in self.lotto_zahlen:
                self.treffer.append(zahl)

    def bewertung_erstellen(self):
        """Die Anzahl der Treffer wird in einen Text umgewandelt."""
        anzahl_treffer = len(self.treffer)

        if anzahl_treffer == 6:
            return "6 Richtige - Jackpot!"

        elif anzahl_treffer == 5:
            return "5 Richtige - sehr guter Gewinn!"

        elif anzahl_treffer == 4:
            return "4 Richtige - kleiner Gewinn!"

        elif anzahl_treffer == 3:
            return "3 Richtige - du hast gewonnen!"

        else:
            return "Weniger als 3 Richtige - leider nicht gewonnen."

    def ergebnis_anzeigen(self):
        """Alle wichtigen Ergebnisse werden am Ende angezeigt."""
        print()
        print("Deine Zahlen:", self.spieler_zahlen)
        print("Lottozahlen:", self.lotto_zahlen)
        print("Treffer:", self.treffer)
        print("Anzahl Treffer:", len(self.treffer))
        print(self.bewertung_erstellen())

    def spiel_starten(self):
        """Diese Methode startet das ganze Spiel in der richtigen Reihenfolge."""
        self.spieler_zahlen_eingeben()
        self.lotto_zahlen_ziehen()
        self.treffer_suchen()
        self.ergebnis_anzeigen()


mein_spiel = Lotterie()
mein_spiel.spiel_starten()