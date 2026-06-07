# Workshop: Tupeldatenbank
# Aufgabe: Personen nach Stadt filtern

# Das ist unsere kleine "Datenbank".
# Jede Person ist ein Tupel mit 4 Werten:
# Vorname, Nachname, Geburtsjahr, Stadt

data = [
    ("Max", "Mustermann", 1999, "Musterstadt"),
    ("John", "Doe", 1995, "New York"),
    ("Jane", "Doe", 1996, "New York"),
    ("Erika", "Mustermann", 2002, "Musterstadt"),
    ("Franziska", "Musterfrau", 2001, "Musterstadt"),
    ("Max", "Mustermann", 1972, "Musterstadt"),
    ("Max", "Power", 1972, "Springfield"),
    ("Peter", "Pan", 1953, "Nimmerland"),
]


def filter_city(data, city):
    """Return first name and last name of all people from one city."""

    persons = [
        (first_name, last_name)
        for first_name, last_name, birth_year, person_city in data
        if person_city == city
    ]

    return persons


# Kleine Kontrolle, damit ich direkt sehe, ob es funktioniert.
result = filter_city(data, "Musterstadt")
print(result)