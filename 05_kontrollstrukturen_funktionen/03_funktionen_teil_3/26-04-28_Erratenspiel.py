import random

computer_zahl = random.randint(1, 10)# Der Computer denkt sich eine Zahl zwischen 1 und 10 aus

user_zahl = int(input("Gib mir eine Zahl zwischen 1 und 10: ")) # Der Benutzer gibt eine Zahl ein

if user_zahl == computer_zahl:
    print("Hurraaaa! Du hast die Zahl richtig eingegeben.")
else:
    print("Oh jeah, Du hast leider eine falsche Zahl eingegeben.")
    print("Die richtige Zahl wäre:", computer_zahl)
    