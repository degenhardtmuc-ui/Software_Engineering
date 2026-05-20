# Workshop: Einkaufsliste
# Datei: 05_workshop_einkaufsliste_teil_1.py

# Aufgabe 1:
# Definieren Sie zwei Variablen.
# Beide Variablen sollen jeweils eine Liste mit den Strings "Tee" und "Kaffee" enthalten.

meine_einkaufsliste = ["Tee", "Kaffee"]
eine_andere_einkaufsliste = ["Tee", "Kaffee"]


# Aufgabe 2:
# Definieren Sie eine Funktion drucke_einkaufsliste(einkaufsliste).
# Die Funktion bekommt eine Einkaufsliste als Argument.
# Danach gibt sie zuerst die Überschrift "Einkaufsliste:" aus.
# Danach gibt sie jedes Produkt aus der Liste einzeln untereinander aus.

def drucke_einkaufsliste(einkaufsliste):
    print("Einkaufsliste:")
    for produkt in einkaufsliste:
        print(produkt)


# Aufgabe 3:
# Testen Sie die Funktion mit beiden Einkaufslisten.
# Dafür rufen wir die Funktion einmal mit meine_einkaufsliste auf.
# Danach rufen wir die Funktion einmal mit eine_andere_einkaufsliste auf.

drucke_einkaufsliste(meine_einkaufsliste)
drucke_einkaufsliste(eine_andere_einkaufsliste)


# Aufgabe 4:
# Definieren Sie eine Funktion kaufe(produkt, einkaufsliste).
# Die Funktion bekommt ein produkt und eine einkaufsliste als Argumente.
# Mit append() wird das produkt am Ende der einkaufsliste hinzugefügt.

def kaufe(produkt, einkaufsliste):
    einkaufsliste.append(produkt)