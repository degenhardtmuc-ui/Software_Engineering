# if elif else
# else nie alleine stehen kann

# if -> immer der start


# elif -> möglich aber nicht verfplichtend


# else -> schließt ab, möglich aber wenn dann IMMER am Ende




 


#def get_user_nr(zahl):

"""

nimmt Zahl des Nutzers engegen

"""

ergebnis = "Die Zahl ist: " + str(zahl)

return ergebnis

eingabe = input("Bitte gebe die Zahl ein: ")

print(get_user_nr(eingabe))

 

def get_computer_nr():

import random

zahl = random.randint(1, 10)

return "generierte Zahl ist: " + str(zahl)

print(get_computer_nr())

 

user_zahl = get_user_nr

computer_zahl = get_computer_nr

if user_zahl == computer_zahl:

print ("richtig ,der computer hat:" + str(computer_zahl))

else:

print ("falsch, der computer hat:" + str(computer_zahl))



get_user_nr -> return

print(get_user_nr(eingabe))


print(f"Die Zahl ist: {zahl}")




return "generierte Zahl ist: " + str(zahl)

if user_zahl == computer_zahl:

user_zahl = get_user_nr

ergebnis = "Die Zahl ist: " + str(zahl)

if 'Die Zahl ist: 2' == 'generierte Zahl ist: 3':


def get_nr():

number = input(...)

print('Zahl eingegeben:' + number)

return number



Бандус Леонид left
Peter Lang
16:54
PL








