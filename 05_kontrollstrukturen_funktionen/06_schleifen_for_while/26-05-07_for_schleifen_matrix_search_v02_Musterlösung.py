# Matrix / zweidimensionale Liste
matrix = [
    [5, 17, 33],
    [17, 20, 98],
    [1, 27, 44]
]


def search_v02(zwei_dimensionale_liste, element):
    # Hier speichern wir alle gefundenen Positionen
    fundstellen = []

    # Äußere Schleife:
    # Wir gehen durch die Zeilen der Matrix
    for zeilen_index in range(len(zwei_dimensionale_liste)):

        # aktuelle Zeile holen
        zeile = zwei_dimensionale_liste[zeilen_index]

        # Innere Schleife:
        # Wir gehen durch die Spalten in dieser Zeile
        for spalten_index in range(len(zeile)):

            # Prüfen, ob der aktuelle Wert das gesuchte Element ist
            if zeile[spalten_index] == element:

                # Wenn ja, speichern wir die Position
                fundstellen.append((zeilen_index, spalten_index))

    # Am Ende geben wir zurück:
    # 1. Wie oft wurde das Element gefunden?
    # 2. An welchen Positionen wurde es gefunden?
    return len(fundstellen), fundstellen


# Test
print(search_v02(matrix, 17))
print(search_v02(matrix, 20))

# _________________________________________________________________________
#          Spalte 0   Spalte 1   Spalte 2
# Zeile 0      5         17         33
# Zeile 1     17         20         98
# Zeile 2      1         27         44

# Die erste 17 steht in Zeile 0, Spalte 1.
# Die zweite 17 steht in Zeile 1, Spalte 0.

# => Ergebnis: (2, [(0, 1), (1, 0)])

# Bedeutet: 2 Treffer gefunden.
# Die Treffer sind bei:
# Zeile 0, Spalte 1
# Zeile 1, Spalte 0


# Musterlösung
matrix = [
    [5, 17, 33],
    [17, 20, 98],
    [1, 27, 44]
]


def search_v02(zwei_dimensionale_liste, element):
    ergebnis = []

    zeile_nummer = 0

    for zeile in zwei_dimensionale_liste:
        spalte_nummer = 0

        for wert in zeile:
            if wert == element:
                ergebnis.append((zeile_nummer, spalte_nummer))

            spalte_nummer = spalte_nummer + 1

        zeile_nummer = zeile_nummer + 1

    return len(ergebnis), ergebnis


print(search_v02(matrix, 17))
print(search_v02(matrix, 20))