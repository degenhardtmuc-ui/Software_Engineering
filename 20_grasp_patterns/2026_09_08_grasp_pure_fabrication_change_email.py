class User:
    """Repräsentiert einen Benutzer und enthält nur Fachlogik."""

    def __init__(self, user_id: int, name: str, email: str):
        """Erstellt einen Benutzer."""
        self.user_id = user_id
        self.name = name
        self.email = email

    def change_email(self, new_email: str) -> None:
        """Ändert die E-Mail-Adresse des Benutzers."""
        self.email = new_email


class UserRepository:
    """Technische Hilfsklasse für die Speicherung von Benutzern."""

    def save(self, user: User) -> None:
        """Speichert einen Benutzer in der Datenbank."""
        print(
            f"Speichere {user.name} "
            f"mit E-Mail {user.email}."
        )


# Anwendung
user = User(
    1,
    "Alice",
    "alice@example.com"
)

user.change_email("alice@newdomain.com")

repository = UserRepository()
repository.save(user)



# Warum ist UserRepository Pure Fabrication?

# Weil wir diese technische Klasse bewusst „erfinden“, damit User nicht selbst Datenbanklogik übernehmen muss.

# Dadurch bekommen wir:

# High Cohesion + Low Coupling + bessere Trennung der Verantwortlichkeiten.