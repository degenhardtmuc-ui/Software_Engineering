def spiel_starten(self):
        """Diese Methode startet das ganze Spiel in der richtigen Reihenfolge."""
        self.spieler_zahlen_eingeben()
        self.lotto_zahlen_ziehen()
        self.treffer_suchen()
        self.ergebnis_anzeigen()


mein_spiel = Lotterie()
mein_spiel.spiel_starten()