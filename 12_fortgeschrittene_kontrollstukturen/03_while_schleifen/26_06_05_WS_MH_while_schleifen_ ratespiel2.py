def rate_wort():
    """Ask the user for a word until it is correct."""
    loesung = "python"
    tipp = ""

    while tipp != loesung:
        tipp = input("Rate das Wort: ")

    print("Richtig geraten!")


rate_wort()