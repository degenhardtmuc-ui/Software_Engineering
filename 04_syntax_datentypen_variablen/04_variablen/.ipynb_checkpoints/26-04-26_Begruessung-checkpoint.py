def begruesse_person(a, b):
    print("Hallo", a)
    print("Hallo", b)

begruesse_person("Laith", "Barbara") #Die Funktion bekommt zwei Namen als Parameter und gibt für beide eine Begrüßung aus
                                     #Das ist flexibler als feste Strings, weil ich jede Person übergeben kann


def begruessen():
    print("Hallo Laith")
    print("Hallo Barbara")
begruessen()



def begruessen(name):
    print("Hallo", name)

begruessen("Laith")
begruessen("Barbara")