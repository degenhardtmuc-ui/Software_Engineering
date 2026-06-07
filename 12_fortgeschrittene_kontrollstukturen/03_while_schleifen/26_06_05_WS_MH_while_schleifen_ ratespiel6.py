def rate_antwort():
    """Ask the user until the answer is yes."""
    antwort = ""

    while antwort != "ja":
        antwort = input("Willst du Python lernen? ")

    print("Sehr gut, dann legen wir los!")


rate_antwort()


# Ich benutze hier eine while-Schleife, weil der Benutzer unbegrenzt oft raten darf. Die Schleife läuft so lange weiter, bis die Eingabe mit der Lösung übereinstimmt.