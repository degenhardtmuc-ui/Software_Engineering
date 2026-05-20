# 07 Boolesche Werte
# Mini-Workshop: Vergleiche
#
# Datei: 07_boolesche_werte_vergleiche.py
#
# Hinweis für VS Code:
# 1. Lege im passenden Kursordner eine neue Datei an.
# 2. Nenne sie: 07_boolesche_werte_vergleiche.py
# 3. Kopiere diesen ganzen Code hinein.
# 4. Speichere mit Cmd + S auf dem Mac oder Strg + S auf Windows.
# 5. Starte die Datei im Terminal mit:
#    python 07_boolesche_werte_vergleiche.py
#
# In Python bekommt man bei Vergleichen immer einen booleschen Wert:
# True  = wahr / stimmt
# False = falsch / stimmt nicht


print("07 Boolesche Werte")
print("Mini-Workshop: Vergleiche")
print("=" * 50)


# ------------------------------------------------------------
# Aufgabe 1:
# Ist 2^16 größer als 32.000 / 2?
# ------------------------------------------------------------

# WICHTIG:
# In Python schreibt man Potenzen mit **.
# 2 ** 16 bedeutet: 2 hoch 16.
#
# WICHTIG:
# 32.000 darf man in Python NICHT für zweiunddreißigtausend schreiben.
# Python würde 32.000 als 32.0 verstehen.
#
# Besser schreibt man:
# 32_000
# Der Unterstrich macht große Zahlen besser lesbar.
# Python rechnet damit ganz normal wie mit 32000.

potenz = 2 ** 16
division = 32_000 / 2
vergleich_1 = potenz > division

print()
print("Aufgabe 1: Ist 2^16 größer als 32.000 / 2?")
print("-" * 50)

print("Datentabelle Aufgabe 1:")
print(f"{'Teilrechnung':<25} {'Python-Schreibweise':<25} {'Ergebnis'}")
print("-" * 70)
print(f"{'2 hoch 16':<25} {'2 ** 16':<25} {potenz}")
print(f"{'32.000 geteilt durch 2':<25} {'32_000 / 2':<25} {division}")
print(f"{'Vergleich':<25} {'2 ** 16 > 32_000 / 2':<25} {vergleich_1}")

print()
print("Rechenweg Aufgabe 1:")
print(f"2 ** 16 = {potenz}")
print(f"32_000 / 2 = {division}")
print(f"{potenz} > {division} ergibt {vergleich_1}")

print()
print("Lösung für das Notebook-Feld Aufgabe 1:")
print("2 ** 16 > 32_000 / 2")


# ------------------------------------------------------------
# Aufgabe 2:
# Ist 72 ohne Rest durch 3 teilbar?
# ------------------------------------------------------------

# Dafür benutzen wir den Modulo-Operator: %
#
# Modulo bedeutet:
# Was bleibt als Rest übrig?
#
# Beispiel:
# 72 % 3 bedeutet:
# Welcher Rest bleibt, wenn ich 72 durch 3 teile?
#
# Wenn der Rest 0 ist, dann ist die Zahl ohne Rest teilbar.
#
# Wichtig:
# =  bedeutet: etwas speichern / zuweisen
# == bedeutet: vergleichen / prüfen
#
# Deshalb schreiben wir:
# 72 % 3 == 0

zahl = 72
teiler = 3
division_2 = zahl / teiler
rest = zahl % teiler
vergleich_2 = rest == 0

print()
print("=" * 50)
print("Aufgabe 2: Ist 72 ohne Rest durch 3 teilbar?")
print("-" * 50)

print("Datentabelle Aufgabe 2:")
print(f"{'Teilrechnung':<25} {'Python-Schreibweise':<25} {'Ergebnis'}")
print("-" * 70)
print(f"{'72 geteilt durch 3':<25} {'72 / 3':<25} {division_2}")
print(f"{'Rest berechnen':<25} {'72 % 3':<25} {rest}")
print(f"{'Rest mit 0 vergleichen':<25} {'72 % 3 == 0':<25} {vergleich_2}")

print()
print("Rechenweg Aufgabe 2:")
print(f"72 / 3 = {division_2}")
print(f"72 % 3 = {rest}")
print("Wenn der Rest 0 ist, ist 72 ohne Rest durch 3 teilbar.")
print(f"{rest} == 0 ergibt {vergleich_2}")

print()
print("Lösung für das Notebook-Feld Aufgabe 2:")
print("72 % 3 == 0")


# ------------------------------------------------------------
# Merktabelle
# ------------------------------------------------------------

print()
print("=" * 50)
print("Merktabelle:")
print("-" * 50)
print(f"{'Idee':<25} {'Python-Zeichen':<20} {'Beispiel'}")
print("-" * 70)
print(f"{'Hochrechnung':<25} {'**':<20} {'2 ** 16'}")
print(f"{'Normale Division':<25} {'/':<20} {'32_000 / 2'}")
print(f"{'Größer als':<25} {'>':<20} {'65536 > 16000'}")
print(f"{'Gleichheit prüfen':<25} {'==':<20} {'72 % 3 == 0'}")
print(f"{'Rest berechnen':<25} {'%':<20} {'72 % 3'}")


# ------------------------------------------------------------
# Kurze Endergebnisse
# ------------------------------------------------------------

print()
print("=" * 50)
print("Kurze Endergebnisse:")
print("Aufgabe 1:", vergleich_1)
print("Aufgabe 2:", vergleich_2)
