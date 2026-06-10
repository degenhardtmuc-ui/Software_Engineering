# Workshop: Assertions
# Datei: valid_mail.py
# Diese Version ist die sichere Lösung.
# Hier benutzen wir NICHT assert für Benutzer-Eingaben.
# Stattdessen benutzen wir if und raise ValueError.

valid_mail_addresses = [
    "daniel@example.com",
    "anna@example.com",
    "max@example.com",
]


def check_mail_address(mail_address):
    """Prüft, ob die E-Mail-Adresse in der erlaubten Liste steht."""

    print("[LOG 4] Wir sind jetzt in der Funktion check_mail_address().")
    print("[LOG 5] Jetzt wird mit if geprüft, ob die E-Mail erlaubt ist.")

    # Wenn die E-Mail NICHT in der Liste ist, dann ist sie ungültig.
    if mail_address not in valid_mail_addresses:
        print("[LOG 6] Die E-Mail wurde NICHT in der Liste gefunden.")

        # raise bedeutet: Wir werfen absichtlich einen Fehler.
        # ValueError passt hier, weil der Wert der Eingabe falsch ist.
        raise ValueError("Diese E-Mail-Adresse ist nicht erlaubt.")

    print("[LOG 6] Die E-Mail wurde in der Liste gefunden.")
    return mail_address


def main():
    """Fragt eine E-Mail-Adresse ab und gibt sie nur aus, wenn sie erlaubt ist."""

    print("[LOG 1] Programm startet.")
    print("[LOG 2] Erlaubte E-Mail-Adressen sind in einer Liste gespeichert.")

    mail_address = input("Bitte E-Mail-Adresse eingeben: ")

    print(f"[LOG 3] Der Benutzer hat eingegeben: {mail_address}")

    try:
        checked_mail_address = check_mail_address(mail_address)

        print("[LOG 7] Keine Exception. Das Programm darf weitermachen.")
        print(f"E-Mail-Adresse ist erlaubt: {checked_mail_address}")

    except ValueError as error:
        print("[LOG 7] Eine ValueError-Exception wurde ausgelöst und hier abgefangen.")
        print(f"Fehler: {error}")
        print("Die E-Mail-Adresse wird NICHT akzeptiert.")


# Dieser Teil startet das Programm nur dann,
# wenn diese Datei direkt ausgeführt wird.
if __name__ == "__main__":
    main()