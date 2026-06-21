def zahlen_eingeben(self):
        """Der Spieler gibt 6 verschiedene Zahlen von 1 bis 49 ein."""
        print(self.name + ", bitte gib 6 verschiedene Zahlen von 1 bis 49 ein.")

        while len(self.zahlen) < 6:
            try:
                zahl = int(input("Zahl eingeben: "))
                self.zahl_pruefen(zahl)
                self.zahlen.append(zahl)
                print("Gespeicherte Zahlen:", self.zahlen)

            except ValueError:
                print("Bitte nur ganze Zahlen eingeben.")

            except FalscheZahlFehler as fehler:
                print(fehler)