class Spieler:
    """Diese Klasse speichert den Namen und die Zahlen vom Spieler."""

    def __init__(self, name):
        """Ein neuer Spieler bekommt einen Namen und eine leere Zahlenliste."""
        self.name = name
        self.zahlen = []