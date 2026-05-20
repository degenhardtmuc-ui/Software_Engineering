# Mini-Workshop: Operatoren, Vergleiche und Assertions

# Teil 1: Variablen definieren
var1 = 3 ** (3 * 4)
var2 = 4 ** 3 ** 2
var3 = (3 ** 3) ** 3
var4 = (2 ** 3) ** 4

var1 = 3 ** (3 * 4) = 3 ** 12 = 531441
var2 = 3 ** 2 = 9 → 4 ** 9 = 262144 (Reihenfolge beachten!)
var3 =(3 ** 3) ** 3 = 27 ** 3 = 19683
var4 = (2 ** 3) ** 4 = 8 ** 4 = 4096


# Ergebnisse anzeigen
print("var1 =", var1)
print("var2 =", var2)
print("var3 =", var3)
print("var4 =", var4)

# Teilbarkeit prüfen
ergebnis = (var1 % var3 == 0) and (var2 % var4 == 0)



# 1. var1 % var3 531441 % 19683 = 0
# 2. var2 % var4 262144 % 4096 = 0 
# Beide sind teilbar → Gesamt: True

print("Ist var1 durch var3 teilbar UND var2 durch var4 teilbar?")
print(ergebnis)



# Teil 2: Assertions

my_int = 1
my_float = 1.0

assert my_int == 1
assert my_float == my_int
assert my_float != "1.0"

print("Alle Assertions wurden erfolgreich geprüft.")

