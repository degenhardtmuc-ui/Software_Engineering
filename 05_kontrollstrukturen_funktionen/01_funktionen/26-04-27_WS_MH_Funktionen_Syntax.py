# Funktion 1: addiere zwei Zahlen
def addiere(a, b):
    return a + b
    
print(addiere(5, 3))           # 8


# Funktion 2: subtrahiere zwei Zahlen
def subtrahiere(a, b):
    return a - b
    
print(subtrahiere(5, 3))       # 2


# Funktion 3: multipliziere zwei Zahlen
def multipliziere(a, b):
    return a * b

print(multipliziere(5, 3))     # 15


# Funktion 4: dividiere zwei Zahlen
def dividiere(a, b):
    if b != 0:
        return a / b
    else:
        return "Fehler: Division durch 0"
        
print(dividiere(5, 3))     # 1.666...

# Funktion 5: gibt den Rest einer Division zurück (Modulo)
def rest(a, b):
    if b != 0:
        return a % b
    else:
        return "Fehler: Division durch 0"

print(rest(5, 3))          # 2

        

print(addiere(5, 3))        # 8
print(subtrahiere(5, 3))   # 2
print(multipliziere(5, 3)) # 15
print(dividiere(5, 3))     # 1.666...
print(rest(5, 3))          # 2