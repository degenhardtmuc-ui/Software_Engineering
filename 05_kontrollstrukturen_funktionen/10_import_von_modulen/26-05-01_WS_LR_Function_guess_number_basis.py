import random                                           # Python, bitte gib mir das Zufallszahlen-Werkzeug

def get_computer_nr():                                  # Diese Funktion erzeugt die Zahl vom Computer.
    return random.randint(1, 10)

def get_user_nr():
    return int(input("Rate eine Zahl von 1 bis 10: ")) 
def bewerte(usr_nr, computer_nr):
    if usr_nr == computer_nr:
        print("Richtig geraten!")
        return True
    elif usr_nr < computer_nr:
        print("Zu niedrig!")
        return False
    else:
        print("Zu hoch!")
        return False