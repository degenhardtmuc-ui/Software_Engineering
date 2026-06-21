class Lotterie:
    """Eine einfache Klasse für ein Lottospiel."""

    def __init__(self):
        """Hier werden die Listen für ein neues Spiel vorbereitet."""
        # self bedeutet: Diese Liste gehört zu diesem Spiel.
        self.spieler_zahlen = []
        self.lotto_zahlen = []
        self.treffer = []