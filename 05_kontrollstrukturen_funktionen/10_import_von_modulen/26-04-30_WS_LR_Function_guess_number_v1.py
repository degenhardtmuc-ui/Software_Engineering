#1 - Funktion, welche die Benutzerzahl zurück liefert
def get_user_nr():
    pass

#2 - Funktion,welche ein Randomzahl zwischen 1 und 10 generiert
def get_computer_nr():
    pass

#3 - Ergebnis auswerten
def bewerte(user_nr, computer_nr):
    ergebnis = False
    if user_nr == computer_nr: 
        ergebnis = True
        return ergebnis
        
# 4 Spiel starten
def start():
usr_nr = get_user_nr()
computer_nr = get_computer_nr()
bewerte(usr_nr, computer_nr)

Aufgabe!

# Version 2: man hat 3 Versuche

# Version 3: das Spiel endet erst, wenn der Spieler/in die Zahl richtig erraten hat 