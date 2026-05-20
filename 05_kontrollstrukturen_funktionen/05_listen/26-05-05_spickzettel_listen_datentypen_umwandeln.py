# Datentypen umwandeln in Python
# Das nennt man auch Casting.

# 1. String in Liste umwandeln
text = "rgb"
liste = list(text)
print(liste)  # ['r', 'g', 'b']


# 2. String in Integer umwandeln
text_zahl = "123"
ganze_zahl = int(text_zahl)
print(ganze_zahl)  # 123


# 3. String in Float umwandeln
text_kommazahl = "3.14"
kommazahl = float(text_kommazahl)
print(kommazahl)  # 3.14


# 4. Integer in String umwandeln
alter = 30
alter_als_text = str(alter)
print(alter_als_text)  # "30"


# 5. Integer in Float umwandeln
zahl = 5
zahl_als_float = float(zahl)
print(zahl_als_float)  # 5.0


# 6. Float in Integer umwandeln
andere_zahl = 5.9
ohne_nachkommastellen = int(andere_zahl)
print(ohne_nachkommastellen)  # 5


# 7. Liste in Tuple umwandeln
farben_liste = ["r", "g", "b"]
farben_tuple = tuple(farben_liste)
print(farben_tuple)  # ('r', 'g', 'b')


# 8. Tuple in Liste umwandeln
neue_liste = list(farben_tuple)
print(neue_liste)  # ['r', 'g', 'b']


# 9. Liste in Set umwandeln
farben_mit_doppelungen = ["r", "g", "b", "r"]
farben_ohne_doppelungen = set(farben_mit_doppelungen)
print(farben_ohne_doppelungen)  # {'r', 'g', 'b'}


# 10. Werte in Boolean umwandeln
print(bool(1))       # True
print(bool(0))       # False
print(bool("Hallo")) # True
print(bool(""))      # False