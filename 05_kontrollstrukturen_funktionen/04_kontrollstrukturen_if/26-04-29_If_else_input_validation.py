#if value:
 #if-Zweig
#else
 #else-Zweig

#value: Bedingung z.B.Vergleich: 7 > 3: Antwort JA => True, Antwort: Nein => False
#value: Function liefert True oder False
#value: Zahl sein (wenn die Zahl 0:False, sonst True)
#value: str sein (wenn str leer ist: "" dann False, sonst True)

if 0:
    print("value bei if ist True")
    print("Daher wird if-Zweig ausgeführt")
else:
    print("value bei if ist False")
    print("Daher wird else-Zweig ausgeführt")

# or    True False
#True   True True
#False  True False
#

def gib_user_zahl():
    zahl = int(input("Gib mir eine zahl zwischen 1 und 10"))
    if zahl < 1 or zahl > 10: # False or False => False #value = zahl < 1 or zahl > 10
        print("Sie haben:",zahl,"angegeben!")
        print("Ihre Zahl muss bitte zwischen 1 und 10 sein!")
        zahl = None
    else:
        print("Sie haben",zahl, "angegeben"!)
        print("Prima!Ihre Angabe war richtig!")

    return zahl

user_zahl = gib_user_zahl()
#Gib mir eine Zahl zwischen 1 und 10: 7
#Sie haben 7 angegeben
#Prima Ihre Angabe war richtig!

print(user_zahl)
7

     