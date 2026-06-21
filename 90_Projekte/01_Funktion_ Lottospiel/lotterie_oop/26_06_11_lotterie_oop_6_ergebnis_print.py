def ergebnis_anzeigen(self):
        """Alle wichtigen Ergebnisse werden am Ende angezeigt."""
        print()
        print("Deine Zahlen:", self.spieler_zahlen)
        print("Lottozahlen:", self.lotto_zahlen)
        print("Treffer:", self.treffer)
        print("Anzahl Treffer:", len(self.treffer))
        print(self.bewertung_erstellen())