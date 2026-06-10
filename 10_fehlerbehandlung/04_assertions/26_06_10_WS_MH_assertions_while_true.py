"""
Workshop: E-Mail-Prüfung mit while

Dieses Programm fragt so lange nach einer E-Mail-Adresse,
bis eine erlaubte Adresse eingegeben wurde.
"""

valid_mail_addresses = [
    "anna@example.com",
    "max@example.com",
    "daniel@example.com",
]

while True:
    mail_adresse = input("Bitte E-Mail-Adresse eingeben: ")

    if mail_adresse in valid_mail_addresses:
        print(f"Gültige E-Mail-Adresse: {mail_adresse}")
        break

    print("Bitte gib eine gültige E-Mail-Adresse ein.")

# Mit while True kann ich den Benutzer so lange neu fragen, bis eine gültige Eingabe kommt
# Mit assert prüfe ich eine Behauptung im Code. 
# Wenn die Behauptung falsch ist, entsteht ein AssertionError. 
# Mit try und except kann ich diesen Fehler abfangen, damit kein roter Traceback angezeigt wird. 