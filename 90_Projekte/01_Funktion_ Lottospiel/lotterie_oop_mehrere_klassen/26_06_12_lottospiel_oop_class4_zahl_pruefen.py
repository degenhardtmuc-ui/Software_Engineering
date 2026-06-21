def zahl_pruefen(self, zahl):
        """Diese Methode prüft, ob eine Zahl erlaubt ist."""
        if zahl < 1 or zahl > 49:
            raise FalscheZahlFehler("Die Zahl muss zwischen 1 und 49 sein.")

        if zahl in self.zahlen:
            raise FalscheZahlFehler("Diese Zahl hast du schon eingegeben.")