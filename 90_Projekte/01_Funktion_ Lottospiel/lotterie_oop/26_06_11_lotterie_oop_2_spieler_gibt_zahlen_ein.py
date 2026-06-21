def spieler_zahlen_eingeben(self):
        """Der Spieler gibt 6 verschiedene Zahlen von 1 bis 49 ein."""
        print("Bitte gib 6 verschiedene Zahlen von 1 bis 49 ein.")

        while len(self.spieler_zahlen) < 6:
            zahl = int(input("Zahl eingeben: "))

            if zahl < 1 or zahl > 49:
                print("Die Zahl muss zwischen 1 und 49 sein.")

            elif zahl in self.spieler_zahlen:
                print("Diese Zahl hast du schon eingegeben.")

            else:
                self.spieler_zahlen.append(zahl)
                print("Gespeicherte Zahlen:", self.spieler_zahlen)