# Meine Matrix
matrix = [
    [5, 17, 33],
    [17, 20, 98],
    [1, 27, 44]
]


def search_v02(zwei_dimensionale_liste, element):
    # In diese Liste schreibe ich alle Stellen rein,
    # an denen ich das gesuchte Element finde.
    ergebnis = []

    # Ich starte bei Zeile 0
    zeile_nummer = 0

    # Ich gehe jede Zeile einzeln durch
    for zeile in zwei_dimensionale_liste:

        # Bei jeder neuen Zeile starte ich wieder bei Spalte 0
        spalte_nummer = 0

        # Jetzt gehe ich jedes Element in dieser Zeile durch
        for wert in zeile:

            # Wenn der Wert gleich dem gesuchten Element ist,
            # merke ich mir die Position.
            if wert == element:
                ergebnis.append((zeile_nummer, spalte_nummer))

            # Danach gehe ich eine Spalte weiter
            spalte_nummer = spalte_nummer + 1

        # Wenn die Zeile fertig ist, gehe ich eine Zeile weiter
        zeile_nummer = zeile_nummer + 1

    # Rückgabe:
    # Wie oft gefunden und wo gefunden
    return len(ergebnis), ergebnis


print(search_v02(matrix, 17))
print(search_v02(matrix, 20))



# Ich habe zuerst eine leere Liste ergebnis gemacht. 
# Dort speichere ich alle Positionen, an denen ich die gesuchte Zahl finde. 
# Dann gehe ich Zeile für Zeile durch die Matrix. 
# In jeder Zeile gehe ich Wert für Wert durch. 
# Wenn der Wert gleich dem gesuchten Element ist, speichere ich die aktuelle Zeilen- und Spaltennummer. 
# Am Ende gebe ich zurück, wie viele Treffer es gibt und wo sie stehen.

# Die äußere Schleife läuft durch die Zeilen.
# Die innere Schleife läuft durch die Werte in der Zeile.
# Wenn der Wert passt, speichere ich die Position.


# Merksatz: matrix[zeile][spalte]. 
# d.h. Erst Zeile auswählen.
#      Dann Spalte auswählen.

# Beispiel: matrix[0][1] = 17