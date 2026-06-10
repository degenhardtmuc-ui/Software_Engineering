# Workshop: Assertions
# Datei: valid_mail_assert_demo.py
# Diese Version zeigt das Problem mit assert.
# Wichtig:
# assert ist gut zum Testen.
# assert ist aber NICHT gut für echte Benutzer-Eingaben,
# weil assert mit python -O ausgeschaltet werden kann.

valid_mail_addresses = [
    "daniel@example.com",
    "anna@example.com",
    "max@example.com",
]


def main():
    """Fragt eine E-Mail-Adresse ab und prüft sie mit assert."""

    print("[LOG 1] Programm startet.")
    print("[LOG 2] Die erlaubten E-Mail-Adressen sind in einer Liste gespeichert.")

    mail_address = input("Bitte E-Mail-Adresse eingeben: ")

    print(f"[LOG 3] Der Benutzer hat eingegeben: {mail_address}")
    print("[LOG 4] Jetzt prüfen wir mit assert, ob die E-Mail erlaubt ist.")

    # ACHTUNG:
    # assert kann von Python ausgeschaltet werden.
    # Wenn man das Programm mit python -O startet,
    # dann wird diese Prüfung einfach übersprungen.
    assert mail_address in valid_mail_addresses, "Diese E-Mail-Adresse ist nicht erlaubt."

    print("[LOG 5] Die assert-Prüfung wurde bestanden.")
    print(f"E-Mail-Adresse ist erlaubt: {mail_address}")


# Dieser Teil startet das Programm nur dann,
# wenn diese Datei direkt ausgeführt wird.
if __name__ == "__main__":
    main()