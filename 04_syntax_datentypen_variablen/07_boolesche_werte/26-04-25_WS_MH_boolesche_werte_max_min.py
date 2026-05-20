Boolesche Werte – Mini-Workshop: Vergleiche

Thema:
- boolesche Werte: True oder False
- Vergleiche mit >
- Maximum und Minimum mit max() und min()
- Teilbarkeit ohne Rest mit dem Modulo-Operator %

Hinweis:
In Python bedeutet ** "hoch".
Beispiel:
2 ** 3 bedeutet 2 hoch 3, also 8.
"""


# ============================================================
# Aufgabe 1
# ============================================================
# Gegeben sind folgende Variablen:

var1 = 2 ** 2 ** 4
# Wichtig:
# Python wertet mehrere Potenzen von rechts nach links aus.
# Das bedeutet:
# 2 ** 2 ** 4
# ist dasselbe wie:
# 2 ** (2 ** 4)
# also:
# 2 ** 16 = 65536

var2 = 3 ** 12
# 3 hoch 12 = 531441

var3 = 100 * 200 * 300
# 100 mal 200 mal 300 = 6000000

var4 = 4 * 3 ** 2
# Wichtig:
# Potenzrechnung kommt vor Multiplikation.
# Also zuerst:
# 3 ** 2 = 9
# Dann:
# 4 * 9 = 36


# Aufgabe:
# Ist das Maximum von var1 und var2 größer als das Minimum von var3 und var4?

# Wichtig:
# In Python bedeutet ** "hoch".
# Python rechnet Potenzen von rechts nach links:
# 2**2**4 bedeutet also: 2 ** (2 ** 4)
# und NICHT: (2 ** 2) ** 4

# Variablen aus der Aufgabe
var1 = 2**2**4
var2 = 3**12
var3 = 100 * 200 * 300
var4 = 4**3**2

# Rechenweg als einzelne Zwischenschritte
print("Rechenweg:")
print("var1 = 2**2**4 = 2 ** (2 ** 4) = 2 ** 16 =", var1)
print("var2 = 3**12 =", var2)
print("var3 = 100 * 200 * 300 =", var3)
print("var4 = 4**3**2 = 4 ** (3 ** 2) = 4 ** 9 =", var4)

print()

# Maximum von var1 und var2
maximum_var1_var2 = max(var1, var2)

# Minimum von var3 und var4
minimum_var3_var4 = min(var3, var4)

print("Vergleich:")
print("Maximum von var1 und var2:", maximum_var1_var2)
print("Minimum von var3 und var4:", minimum_var3_var4)

print()

# Gesuchte boolesche Aussage
ergebnis = maximum_var1_var2 > minimum_var3_var4

print("Ist das Maximum von var1 und var2 größer als das Minimum von var3 und var4?")
print(ergebnis)
