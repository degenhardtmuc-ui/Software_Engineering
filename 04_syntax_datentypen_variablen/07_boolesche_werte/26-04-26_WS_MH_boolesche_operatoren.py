# 08 Boolesche Operatoren
# Aufgabe:
# Ist var1 durch var3 teilbar
# und gleichzeitig var2 durch var4 teilbar?

# Beispielwerte zum Testen:
# Diese Werte kannst du später ändern.
var1 = 72
var2 = 20
var3 = 3
var4 = 5

# Teilprüfung 1:
# Ist var1 durch var3 ohne Rest teilbar?
teilbar_1 = var1 % var3 == 0

# Teilprüfung 2:
# Ist var2 durch var4 ohne Rest teilbar?
teilbar_2 = var2 % var4 == 0

# Gesamtergebnis:
# Beide Bedingungen müssen gleichzeitig True sein.
ergebnis = teilbar_1 and teilbar_2

print("08 Boolesche Operatoren")
print("=" * 40)

print("var1 =", var1)
print("var2 =", var2)
print("var3 =", var3)
print("var4 =", var4)

print()
print("Teilprüfung 1:")
print("var1 % var3 == 0")
print(var1, "%", var3, "=", var1 % var3)
print("Ergebnis:", teilbar_1)

print()
print("Teilprüfung 2:")
print("var2 % var4 == 0")
print(var2, "%", var4, "=", var2 % var4)
print("Ergebnis:", teilbar_2)

print()
print("Gesamtergebnis:")
print("(var1 % var3 == 0) and (var2 % var4 == 0)")
print("Ergebnis:", ergebnis)