import random  # Damit der Computer zufällige Lottozahlen ziehen kann.


class FalscheZahlFehler(Exception):
    """Eigener Fehler, wenn eine Lottozahl nicht erlaubt ist."""

    pass


class Spieler:
    """Diese Klasse speichert den Namen und die Zahlen vom Spieler."""

    def __init__(self, name):
        """Ein neuer Spieler bekommt einen Namen und eine leere Zahlenliste."""
        self.name = name
        self.zahlen = []

    def zahlen_eingeben(self):
        """Der Spieler gibt 6 verschiedene Zahlen von 1 bis 49 ein."""
        print(self.name + ", bitte gib 6 verschiedene Zahlen von 1 bis 49 ein.")

        while len(self.zahlen) < 6:
            try:
                zahl = int(input("Zahl eingeben: "))
                self.zahl_pruefen(zahl)
                self.zahlen.append(zahl)
                print("Gespeicherte Zahlen:", self.zahlen)

            except ValueError:
                print("Bitte nur ganze Zahlen eingeben.")

            except FalscheZahlFehler as fehler:
                print(fehler)

    def zahl_pruefen(self, zahl):
        """Diese Methode prüft, ob eine Zahl erlaubt ist."""
        if zahl < 1 or zahl > 49:
            raise FalscheZahlFehler("Die Zahl muss zwischen 1 und 49 sein.")

        if zahl in self.zahlen:
            raise FalscheZahlFehler("Diese Zahl hast du schon eingegeben.")


class Ziehung:
    """Diese Klasse zieht die Lottozahlen vom Computer."""

    def __init__(self):
        """Am Anfang hat die Ziehung noch keine Zahlen."""
        self.zahlen = []

    def zahlen_ziehen(self):
        """Der Computer zieht 6 verschiedene Zahlen von 1 bis 49."""
        while len(self.zahlen) < 6:
            zahl = random.randint(1, 49)

            if zahl not in self.zahlen:
                self.zahlen.append(zahl)


class Auswertung:
    """Diese Klasse vergleicht Spielerzahlen und Lottozahlen."""

    def __init__(self):
        """Am Anfang gibt es noch keine Treffer."""
        self.treffer = []

    def treffer_suchen(self, spieler_zahlen, lotto_zahlen):
        """Hier wird geprüft, welche Spielerzahlen auch Lottozahlen sind."""
        self.treffer = []

        for zahl in spieler_zahlen:
            if zahl in lotto_zahlen:
                self.treffer.append(zahl)

    def bewertung_erstellen(self):
        """Aus der Anzahl der Treffer wird ein Ergebnistext gemacht."""
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


class LottoSpiel:
    """Diese Klasse steuert das ganze Lottospiel."""

    def __init__(self, spieler):
        """Das Spiel bekommt einen Spieler, eine Ziehung und eine Auswertung."""
        self.spieler = spieler
        self.ziehung = Ziehung()
        self.auswertung = Auswertung()

    def spiel_starten(self):
        """Diese Methode startet alle Schritte in der richtigen Reihenfolge."""
        self.spieler.zahlen_eingeben()
        self.ziehung.zahlen_ziehen()
        self.auswertung.treffer_suchen(self.spieler.zahlen, self.ziehung.zahlen)
        self.ergebnis_anzeigen()

    def ergebnis_anzeigen(self):
        """Am Ende werden alle wichtigen Informationen angezeigt."""
        print()
        print("Spieler:", self.spieler.name)
        print("Deine Zahlen:", self.spieler.zahlen)
        print("Lottozahlen:", self.ziehung.zahlen)
        print("Treffer:", self.auswertung.treffer)
        print("Anzahl Treffer:", len(self.auswertung.treffer))
        print(self.auswertung.bewertung_erstellen())


spieler = Spieler("Daniel")
spiel = LottoSpiel(spieler)
spiel.spiel_starten()