def rate_passwort():
    """Ask the user for a password until it is correct."""
    passwort = "geheim"
    eingabe = ""

    while eingabe != passwort:
        eingabe = input("Bitte Passwort eingeben: ")

    print("Passwort richtig. Zugang erlaubt.")


rate_passwort()