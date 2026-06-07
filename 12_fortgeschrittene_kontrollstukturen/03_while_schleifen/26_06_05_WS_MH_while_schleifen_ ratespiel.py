def rate_wort(loesung):
    """Ask the user for a word until the word is correct."""
    tipp = ""

    while tipp != loesung:
        tipp = input("Bitte rate das Wort: ")

    print("Richtig! Du hast das Wort erraten.")


rate_wort("python")