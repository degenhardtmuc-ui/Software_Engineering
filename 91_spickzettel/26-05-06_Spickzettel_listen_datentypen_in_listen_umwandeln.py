# Datentypen in Listen umwandeln
# Dafür benutzt man meistens list()
# Wichtig: list() funktioniert nur bei Dingen,
# die Python Element für Element durchgehen kann.


# 1. String in Liste umwandeln
text = "rgb"
liste_aus_text = list(text)

print(liste_aus_text)  # ['r', 'g', 'b']


# 2. Tuple in Liste umwandeln
farben_tuple = ("r", "g", "b")
liste_aus_tuple = list(farben_tuple)

print(liste_aus_tuple)  # ['r', 'g', 'b']


# 3. Set in Liste umwandeln
farben_set = {"r", "g", "b"}
liste_aus_set = list(farben_set)

print(liste_aus_set)  # Reihenfolge kann unterschiedlich sein


# 4. range in Liste umwandeln
zahlen = range(5)
liste_aus_range = list(zahlen)

print(liste_aus_range)  # [0, 1, 2, 3, 4]


# 5. Text mit mehreren Wörtern in Liste umwandeln
satz = "rot grün blau"
woerter_liste = satz.split()

print(woerter_liste)  # ['rot', 'grün', 'blau']


# 6. Eine einzelne Zahl in eine Liste packen
zahl = 5
liste_mit_einer_zahl = [zahl]

print(liste_mit_einer_zahl)  # [5]


# Wichtig:
# list(5) würde NICHT funktionieren,
# weil eine einzelne Zahl nicht Element für Element durchlaufen werden kann.

# Merke:
# list() = aus mehreren einzelnen Bestandteilen eine Liste machen
# []     = selbst eine Liste bauen
# split() = Text in Wörter aufteilen und daraus eine Liste machen