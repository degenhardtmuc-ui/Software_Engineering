class LottoSpiel:
    """Diese Klasse steuert das ganze Lottospiel."""

    def __init__(self, spieler):
        """Das Spiel bekommt einen Spieler, eine Ziehung und eine Auswertung."""
        self.spieler = spieler
        self.ziehung = Ziehung()
        self.auswertung = Auswertung()