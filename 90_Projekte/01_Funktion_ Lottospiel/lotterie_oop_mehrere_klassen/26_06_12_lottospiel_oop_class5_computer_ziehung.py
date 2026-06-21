class Ziehung:
    """Diese Klasse zieht die Lottozahlen vom Computer."""

    def __init__(self):
        """Am Anfang hat die Ziehung noch keine Zahlen."""
        self.zahlen = []

    def zahlen_ziehen(self):
        """Der Computer zieht 6 verschiedene Zahlen von 1 bis 49."""
        while len(self.zahlen) < 6:
            zahl = random.randint(1, 49)

            if zahl not in self.zahlen:
                self.zahlen.append(zahl)