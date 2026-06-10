

# try und except

try:
    mail_adresse = input("Bitte E-Mail-Adresse eingeben: ")

    if mail_adresse not in valid_mail_addresses:
        raise ValueError("Diese E-Mail-Adresse ist nicht erlaubt.")

    print(f"Gültige E-Mail-Adresse: {mail_adresse}")

except ValueError:
    print("Bitte gib eine gültige E-Mail-Adresse ein.")

===========================================================================


valid_mail_addresses = [
    "anna@example.com",
    "max@example.com",
    "daniel@example.com",
]

try:
    mail_adresse = input("Bitte E-Mail-Adresse eingeben: ")

    if mail_adresse not in valid_mail_addresses:
        raise ValueError("Diese E-Mail-Adresse ist nicht erlaubt.")

    print(f"Gültige E-Mail-Adresse: {mail_adresse}")

except ValueError:
    print("Bitte gib eine gültige E-Mail-Adresse ein.")
=======================================================================

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

===========================================================================
# raise valueError
valid_mail_addresses = [
    "anna@example.com",
    "max@example.com",
    "daniel@example.com",
]
try:
    mail_adresse = input("Bitte E-Mail-Adresse eingeben: ")

    if mail_adresse not in valid_mail_addresses:
        raise ValueError("Diese E-Mail-Adresse ist nicht erlaubt.")

    print(f"Gültige E-Mail-Adresse: {mail_adresse}")

except ValueError:
    print("Bitte gib eine gültige E-Mail-Adresse ein.")

==================================================================



valid_mail_addresses = [
    "anna@example.com",
    "max@example.com",
    "daniel@example.com",
]

mail_adresse = input("Bitte E-Mail-Adresse eingeben: ")

if mail_adresse not in valid_mail_addresses:
    raise ValueError("Diese E-Mail-Adresse ist nicht erlaubt.")

print(f"Gültige E-Mail-Adresse: {mail_adresse}")


==================================================



valid_mail_addresses = [
    "anna@example.com",
    "max@example.com",
    "daniel@example.com",
]

mail_adresse = input("Bitte E-Mail-Adresse eingeben: ")

assert mail_adresse in valid_mail_addresses, "Diese E-Mail-Adresse ist nicht erlaubt."

print(f"Gültige E-Mail-Adresse: {mail_adresse}")


