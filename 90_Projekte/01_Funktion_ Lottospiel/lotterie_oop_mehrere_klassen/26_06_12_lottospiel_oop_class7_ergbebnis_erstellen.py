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