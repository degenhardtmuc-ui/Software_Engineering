def treffer_suchen(self):
        """Die Spielerzahlen werden mit den Lottozahlen verglichen."""
        for zahl in self.spieler_zahlen:
            if zahl in self.lotto_zahlen:
                self.treffer.append(zahl)