# Mini-Workshop: Funktion print_all(items: list)

# Die Funktion bekommt eine Liste als Argument.
# items ist der Name der Liste, die an die Funktion übergeben wird.
# Mit der for-Schleife gehen wir jedes Element der Liste einzeln durch.
# Jedes Element wird mit print() in einer eigenen Zeile ausgegeben.
def print_all(items: list):
    # Die for-Schleife geht jedes Element in items einzeln durch.
    for item in items:
        # Jedes Element wird einzeln auf dem Bildschirm ausgegeben.
        print(item)
print_all([1, 2, 3])

# Test 2:
# Hier übergeben wir den String "abc".
# Ein String besteht aus einzelnen Zeichen.
# Deshalb wird jedes Zeichen einzeln ausgegeben.
# Erwartete Ausgabe:
# a
# b
# c

print_all("abc")