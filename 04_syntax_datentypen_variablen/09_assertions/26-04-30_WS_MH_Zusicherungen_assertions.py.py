# 09 Zusicherungen / Assertions
# Mini-Workshop
#
# Datei: 09_zusicherungen_assertions.py
#
# Hinweis für VS Code:
# 1. Lege im passenden Kursordner eine neue Datei an.
# 2. Nenne sie: 09_zusicherungen_assertions.py
# 3. Kopiere diesen ganzen Code hinein.
# 4. Speichere mit Cmd + S auf dem Mac oder Strg + S auf Windows.
# 5. Starte die Datei im Terminal mit:
#    python 09_zusicherungen_assertions.py
#
# Hinweis für das Jupyter Notebook:
# Wenn die Variablen my_int und my_float schon in einer vorherigen Zelle gegeben sind,
# brauchst du im Notebook nur die drei assert-Zeilen aus dem Abschnitt "Notebook-Lösung".


print("09 Zusicherungen / Assertions")
print("=" * 55)


# ------------------------------------------------------------
# 1. Gegebene Werte aus der Aufgabe
# ------------------------------------------------------------
# In der Aufgabe sind diese zwei Anweisungen gegeben:

my_int = 1
my_float = 1.0

print()
print("Gegebene Werte:")
print("-" * 55)
print("my_int   =", my_int, "  Datentyp:", type(my_int))
print("my_float =", my_float, "Datentyp:", type(my_float))


# ------------------------------------------------------------
# 2. Was ist eine Assertion?
# ------------------------------------------------------------
# Eine Assertion ist eine Zusicherung / Prüfung.
#
# Schreibweise:
# assert BEDINGUNG
#
# Wenn die Bedingung True ist:
#     Es passiert nichts. Das Programm läuft weiter.
#
# Wenn die Bedingung False ist:
#     Python stoppt und zeigt einen AssertionError.
#
# Das ist praktisch, um im Code zu prüfen:
# "Ich bin mir sicher, dass diese Bedingung stimmen muss."


print()
print("Was macht assert?")
print("-" * 55)
print("assert prüft eine Bedingung.")
print("Ist die Bedingung True, läuft das Programm weiter.")
print("Ist die Bedingung False, entsteht ein AssertionError.")


# ------------------------------------------------------------
# 3. Eigenschaft 1: my_int == 1
# ------------------------------------------------------------
# Aufgabe:
# Schreibe eine Assertion, die die Eigenschaft oder ihre Negation zusichert.
#
# Eigenschaft:
# my_int == 1
#
# Rechenweg:
# my_int hat den Wert 1.
# 1 == 1 ergibt True.
#
# Deshalb können wir die Eigenschaft direkt zusichern:

eigenschaft_1 = my_int == 1

print()
print("Eigenschaft 1: my_int == 1")
print("-" * 55)
print("Rechenweg:")
print("my_int =", my_int)
print("my_int == 1 ergibt:", eigenschaft_1)

# Assertion:
assert my_int == 1

print("Assertion 1 erfolgreich: assert my_int == 1")


# ------------------------------------------------------------
# 4. Eigenschaft 2: my_float == my_int
# ------------------------------------------------------------
# Eigenschaft:
# my_float == my_int
#
# Rechenweg:
# my_float hat den Wert 1.0.
# my_int hat den Wert 1.
#
# In Python gilt:
# 1.0 == 1 ergibt True.
#
# Warum?
# Obwohl die Datentypen verschieden sind:
# 1.0 ist float
# 1 ist int
#
# sind die Werte mathematisch gleich.
#
# Deshalb können wir die Eigenschaft direkt zusichern:

eigenschaft_2 = my_float == my_int

print()
print("Eigenschaft 2: my_float == my_int")
print("-" * 55)
print("Rechenweg:")
print("my_float =", my_float, "Datentyp:", type(my_float))
print("my_int   =", my_int, "Datentyp:", type(my_int))
print("my_float == my_int ergibt:", eigenschaft_2)

# Assertion:
assert my_float == my_int

print("Assertion 2 erfolgreich: assert my_float == my_int")


# ------------------------------------------------------------
# 5. Eigenschaft 3: my_float == "1.0"
# ------------------------------------------------------------
# Eigenschaft:
# my_float == "1.0"
#
# Rechenweg:
# my_float hat den Wert 1.0 und ist eine Zahl vom Typ float.
# "1.0" steht in Anführungszeichen und ist deshalb Text vom Typ string.
#
# Wichtig:
# 1.0   ist eine Zahl
# "1.0" ist ein Text
#
# Deshalb ist diese Aussage falsch:
# my_float == "1.0" ergibt False.
#
# Die Aufgabe sagt:
# Schreibe eine Assertion, die entweder die Eigenschaft
# ODER ihre Negation zusichert und keinen Fehler auslöst.
#
# Weil die Eigenschaft falsch ist, nehmen wir die Negation:
# my_float != "1.0"
#
# != bedeutet: ist ungleich / ist nicht gleich

eigenschaft_3 = my_float == "1.0"
negation_3 = my_float != "1.0"

print()
print('Eigenschaft 3: my_float == "1.0"')
print("-" * 55)
print("Rechenweg:")
print("my_float =", my_float, "Datentyp:", type(my_float))
print('"1.0"    =', "1.0", "Datentyp:", type("1.0"))
print('my_float == "1.0" ergibt:', eigenschaft_3)
print('my_float != "1.0" ergibt:', negation_3)

# Assertion:
assert my_float != "1.0"

print('Assertion 3 erfolgreich: assert my_float != "1.0"')


# ------------------------------------------------------------
# 6. Datentabelle
# ------------------------------------------------------------
# Diese Tabelle zeigt alle Eigenschaften, Ergebnisse und korrekten Assertions.

print()
print("=" * 55)
print("Datentabelle:")
print("-" * 55)

print(f"{'Eigenschaft':<25} {'Ergebnis':<10} {'Korrekte Assertion'}")
print("-" * 80)
print(f"{'my_int == 1':<25} {str(eigenschaft_1):<10} {'assert my_int == 1'}")
print(f"{'my_float == my_int':<25} {str(eigenschaft_2):<10} {'assert my_float == my_int'}")
print(f"{'my_float == "1.0"':<25} {str(eigenschaft_3):<10} {'assert my_float != "1.0"'}")


# ------------------------------------------------------------
# 7. Notebook-Lösung
# ------------------------------------------------------------
# Wenn du NUR die Lösung in das Notebook-Feld übertragen möchtest,
# schreibe diese drei Zeilen:
#
# assert my_int == 1
# assert my_float == my_int
# assert my_float != "1.0"
#
# Wichtig:
# Die vorherige Zelle mit
# my_int = 1
# my_float = 1.0
# muss bereits ausgeführt worden sein.


print()
print("=" * 55)
print("Notebook-Lösung zum Kopieren:")
print("-" * 55)
print("assert my_int == 1")
print("assert my_float == my_int")
print('assert my_float != "1.0"')


# ------------------------------------------------------------
# 8. Merktabelle
# ------------------------------------------------------------

print()
print("=" * 55)
print("Merktabelle:")
print("-" * 55)
print(f"{'Zeichen / Begriff':<20} {'Bedeutung'}")
print("-" * 55)
print(f"{'assert':<20} {'Zusicherung / Prüfung'}")
print(f"{'==':<20} {'ist gleich?'}")
print(f"{'!=':<20} {'ist ungleich / nicht gleich?'}")
print(f"{'int':<20} {'ganze Zahl, zum Beispiel 1'}")
print(f"{'float':<20} {'Kommazahl, zum Beispiel 1.0'}")
print(f"{'str / string':<20} {'Text, zum Beispiel "1.0"'}")


# ------------------------------------------------------------
# 9. Endmeldung
# ------------------------------------------------------------

print()
print("=" * 55)
print("Alle Assertions wurden erfolgreich geprüft.")
print("Es wurde kein Fehler ausgelöst.")
