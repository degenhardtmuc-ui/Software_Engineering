# 03 Zahlen und Mathematik
# Thema: Wurzeln mit dem ** Operator
# Datei: 03_wurzeln_mit_potenzen.py
#
# Diese Datei kannst du direkt in VS Code speichern und ausführen.
#
# Wichtige Regel:
# In Python bedeutet ** "hoch".
#
# Beispiele:
# 4 ** 2 bedeutet: 4 hoch 2
# 4 ** 0.5 bedeutet: Quadratwurzel aus 4
#
# Warum 0.5?
# 0.5 ist dasselbe wie 1/2.
# Eine Zahl hoch 1/2 bedeutet: Quadratwurzel.

print("03 Zahlen und Mathematik - Wurzeln mit **")
print()


# Aufgabe 1:
# Wie berechnet man die Quadratwurzel aus 4?
print("Aufgabe 1: Quadratwurzel aus 4")
print(4 ** 0.5)  # Ergebnis: 2.0
print()


# Aufgabe 2:
# Wie berechnet man die Quadratwurzel aus 9?
print("Aufgabe 2: Quadratwurzel aus 9")
print(9 ** 0.5)  # Ergebnis: 3.0
print()


# Aufgabe 3:
# Wie berechnet man die Quadratwurzel aus 2?
print("Aufgabe 3: Quadratwurzel aus 2")
print(2 ** 0.5)  # Ergebnis ungefähr: 1.4142135623730951
print()


# Aufgabe 4:
# Kontrolle: Wenn man die Wurzel aus 2 wieder quadriert,
# sollte ungefähr wieder 2 herauskommen.
print("Aufgabe 4: Kontrolle")
print((2 ** 0.5) ** 2)  # Ergebnis: 2.0000000000000004
print()


# Erklärung zu Aufgabe 4:
# (2 ** 0.5) berechnet zuerst die Quadratwurzel aus 2.
# Danach wird dieses Ergebnis mit ** 2 wieder quadriert.
#
# Mathematisch sollte genau 2 herauskommen.
# Python zeigt aber manchmal 2.0000000000000004 an.
# Das ist kein echter Rechenfehler, sondern eine kleine Ungenauigkeit
# bei Kommazahlen im Computer.

print("Merkhilfe:")
print("x ** 0.5 bedeutet: Quadratwurzel aus x")
print("x ** 2 bedeutet: x hoch 2")
print("x ** 3 bedeutet: x hoch 3")
