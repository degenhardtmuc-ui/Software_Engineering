# 07 Ranges - Mini-Workshop
# Aufgabe:
# Schreibe eine Funktion print_squares(n: int),
# die die Quadrate der Zahlen von 1 bis n ausgibt.

def print_squares(n: int):
    # range(1, n + 1) bedeutet:
    # Starte bei 1 und gehe bis n.
    # Das + 1 brauchen wir, weil Python beim Ende STOPPT,
    # bevor es diese Zahl erreicht.
    for zahl in range(1, n + 1):
        # zahl ** 2 bedeutet:
        # Die Zahl wird mit sich selbst malgenommen.
        # Beispiel: 3 ** 2 = 3 * 3 = 9
        quadrat = zahl ** 2

        # Hier wird eine Zeile ausgegeben.
        # f"...{zahl}..." bedeutet:
        # Python setzt den Wert der Variable in den Text ein.
        print(f"{zahl}**2 = {quadrat}")


# Test der Funktion:
print_squares(3)