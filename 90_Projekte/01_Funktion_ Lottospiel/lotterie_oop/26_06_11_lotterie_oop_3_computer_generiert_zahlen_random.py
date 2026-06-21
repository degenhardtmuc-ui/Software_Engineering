import random  # Damit der Computer zufällige Zahlen ziehen kann.

def lotto_zahlen_ziehen(self):
        """Der Computer zieht 6 verschiedene Lottozahlen."""
        while len(self.lotto_zahlen) < 6:
            zahl = random.randint(1, 49)

            if zahl not in self.lotto_zahlen:
                self.lotto_zahlen.append(zahl)