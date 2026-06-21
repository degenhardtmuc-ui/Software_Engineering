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