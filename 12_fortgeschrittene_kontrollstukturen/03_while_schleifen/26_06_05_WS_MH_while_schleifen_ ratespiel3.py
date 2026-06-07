# Grundidee immer:
# while etwas_noch_nicht_richtig_ist:
#    frage nochmal

def rate_zahl():
    """Ask the user for a number until it is correct."""
    loesung = 7
    tipp = 0

    while tipp != loesung:
        tipp = int(input("Rate eine Zahl: "))

    print("Richtig! Die Zahl war 7.")


rate_zahl()    