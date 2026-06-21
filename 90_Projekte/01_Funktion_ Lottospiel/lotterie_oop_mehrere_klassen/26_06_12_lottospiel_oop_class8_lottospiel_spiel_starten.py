def spiel_starten(self):
        """Diese Methode startet alle Schritte in der richtigen Reihenfolge."""
        self.spieler.zahlen_eingeben()
        self.ziehung.zahlen_ziehen()
        self.auswertung.treffer_suchen(self.spieler.zahlen, self.ziehung.zahlen)
        self.ergebnis_anzeigen()

spieler = Spieler("Daniel")
spiel = LottoSpiel(spieler)
spiel.spiel_starten()