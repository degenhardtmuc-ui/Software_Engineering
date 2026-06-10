"""
Workshop: Assertions mit try/except

Dieses Programm fragt eine E-Mail-Adresse ab.
Es zeigt assert und fängt den Fehler freundlich ab.
"""

valid_mail_addresses = [
    "anna@example.com",
    "max@example.com",
    "daniel@example.com",
]

try:
    mail_adresse = input("Bitte E-Mail-Adresse eingeben: ")

    assert mail_adresse in valid_mail_addresses, "Diese E-Mail-Adresse ist nicht erlaubt."

    print(f"Gültige E-Mail-Adresse: {mail_adresse}")

except AssertionError:
    print("Bitte gib eine gültige E-Mail-Adresse ein.")


# Merksatz zu assert
# assert Bedingung, Fehlermeldung (links  = Prüfung / Bedingung, rechts = Fehlermeldung)
# assert mail_adresse in valid_mail_addresses, "Diese E-Mail-Adresse ist nicht erlaubt."
# Bedeutet:
# Ich behaupte: Die E-Mail-Adresse steht in der erlaubten Liste.
# Wenn das nicht stimmt, soll diese Fehlermeldung benutzt werden.
# Das Komma trennt also:
# links  = Prüfung / Bedingung
# rechts = Fehlermeldung
# Mit assert prüfe ich eine Behauptung im Code. 
# Wenn die Behauptung falsch ist, entsteht ein AssertionError. 
# Mit try und except kann ich diesen Fehler abfangen, damit kein roter Traceback angezeigt wird. 