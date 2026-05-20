gehalt = int(input("Wie hoch ist dein Gehalt in Euro? "))

if gehalt > 60000:
    print("Mitgliedschaft ist 300€")
elif gehalt >= 50000:
    print("Mitgliedschaft ist 250€")
elif gehalt >= 40000:
    print("Mitgliedschaft ist 200€")
elif gehalt >= 30000:
    print("Mitgliedschaft ist 150€")
elif gehalt >= 20000:
    print("Mitgliedschaft ist 100€")
elif gehalt >= 15000:
    print("Mitgliedschaft ist 50€")
else:
    print("Für Sie ist das nun kostenfrei!")




# Mit input() frage ich das Gehalt ab. 
# Da input() zuerst Text liefert, wandle ich es mit int() in eine Zahl um. 
# Danach soll Python die Bedingungen von oben nach unten prüfen 
# Sobald eine Bedingung stimmt, wird der passende Beitrag ausgegeben und die restlichen elif-Fälle werden übersprungen.
# Deshalb beginne ich oben mit dem höchsten Gehalt und gehen dann Schritt für Schritt nach unten