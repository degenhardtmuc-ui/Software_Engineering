import random


# In dieser Liste speichern wir später alle Lottofelder.
alle_felder = []


# 1. Fragen: Wie viele Felder möchte der Spieler ausfüllen?
anzahl_felder = int(input("Wie viele Felder möchtest du ausfüllen? 1 bis 12: "))


# 2. Prüfen, ob die Anzahl der Felder erlaubt ist.
while anzahl_felder < 1 or anzahl_felder > 12:
    print("Bitte nur eine Zahl von 1 bis 12 eingeben.")
    anzahl_felder = int(input("Wie viele Felder möchtest du ausfüllen? 1 bis 12: "))


# 3. Fragen: Möchte der Spieler selber eintragen oder random generieren lassen?
entscheidung = input("Möchtest du selber eintragen oder random generieren? Schreibe s oder r: ")


# 4. Prüfen, ob die Entscheidung erlaubt ist.
while entscheidung != "s" and entscheidung != "r":
    print("Bitte nur s für selber oder r für random eingeben.")
    entscheidung = input("Möchtest du selber eintragen oder random generieren? Schreibe s oder r: ")


# 5. Für jedes gewünschte Feld werden jetzt Lottozahlen erstellt.
for feld_nummer in range(1, anzahl_felder + 1):

    print()
    print("Feld Nummer", feld_nummer)

    # Für jedes neue Feld brauchen wir eine neue leere Liste.
    lottozahlen = []


    # Variante 1: Der Spieler trägt die Lottozahlen selber ein.
    if entscheidung == "s":

        while len(lottozahlen) < 6:
            zahl = int(input("Gib eine Lottozahl zwischen 1 und 49 ein: "))

            if zahl < 1 or zahl > 49:
                print("Die Zahl muss zwischen 1 und 49 sein.")

            elif zahl in lottozahlen:
                print("Diese Zahl hast du schon eingetragen.")

            else:
                lottozahlen.append(zahl)


        # Jetzt wird die Superzahl eingetragen.
        superzahl = int(input("Gib eine Superzahl zwischen 1 und 9 ein: "))

        while superzahl < 1 or superzahl > 9:
            print("Die Superzahl muss zwischen 1 und 9 sein.")
            superzahl = int(input("Gib eine Superzahl zwischen 1 und 9 ein: "))


    # Variante 2: Der Computer generiert die Lottozahlen zufällig.
    else:

        while len(lottozahlen) < 6:
            zahl = random.randint(1, 49)

            if zahl not in lottozahlen:
                lottozahlen.append(zahl)


        # Die Superzahl wird auch zufällig generiert.
        superzahl = random.randint(1, 9)


    # Die Lottozahlen werden sortiert, damit sie schöner aussehen.
    lottozahlen.sort()


    # Ein fertiges Feld besteht aus Lottozahlen und Superzahl.
    feld = [lottozahlen, superzahl]


    # Das fertige Feld wird in der großen Liste gespeichert.
    alle_felder.append(feld)


# 6. Am Ende werden alle gespeicherten Felder angezeigt.
print()
print("Deine gespeicherten Lottofelder:")

for feld_nummer in range(len(alle_felder)):
    print("Feld", feld_nummer + 1, ":", alle_felder[feld_nummer])