def ergebnis_anzeigen(self):
        """Am Ende werden alle wichtigen Informationen angezeigt."""
        print()
        print("Spieler:", self.spieler.name)
        print("Deine Zahlen:", self.spieler.zahlen)
        print("Lottozahlen:", self.ziehung.zahlen)
        print("Treffer:", self.auswertung.treffer)
        print("Anzahl Treffer:", len(self.auswertung.treffer))
        print(self.auswertung.bewertung_erstellen())