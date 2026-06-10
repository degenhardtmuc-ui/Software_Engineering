"""
Workshop: Assertions

Dieses Programm fragt eine E-Mail-Adresse ab.
Nur Adressen aus valid_mail_addresses sind erlaubt.
Bei falschen Eingaben wird immer ein Fehler ausgelöst.
"""

valid_mail_addresses = [
    "anna@example.com",
    "max@example.com",
    "daniel@example.com",
]

mail_adresse = input("Bitte E-Mail-Adresse eingeben: ")

if mail_adresse not in valid_mail_addresses:
    raise ValueError("Diese E-Mail-Adresse ist nicht erlaubt.")

print(f"Gültige E-Mail-Adresse: {mail_adresse}")