def rate_zahl_mit_hinweis():
    """Ask the user for a number and give small hints."""
    loesung = 10
    tipp = 0

    while tipp != loesung:
        tipp = int(input("Rate die Zahl: "))

        if tipp < loesung:
            print("Die gesuchte Zahl ist größer.")

        elif tipp > loesung:
            print("Die gesuchte Zahl ist kleiner.")

    print("Richtig! Du hast die Zahl erraten.")


rate_zahl_mit_hinweis()