class User:

    def __init__(self, name: str, email: str):

        self.name = name

        self.email = email

 

    def change_email(self, new_email: str):

        # Fachlogik

        self.email = new_email

 

    def save_to_db((self):

        # Technische Logik vermischt mit Fachobjekt (Schlechte Kohäsion)

        print(f"SQL: INSERT INTO users VALUES ('{self.name}', '{self.email}')")

God Object

=========

# Pure Domänenklasse: Kümmert sich ausschließlich um Fachlogik

class User:

    def __init__(self, user_id: int, name: str, email: str):

        self.user_id = user_id

        self.name = name

        self.email = email

 

    def change_email(self, new_email: str):

        self.email = new_email

 

# Pure Fabrication: Künstliche Hilfsklasse für die Infrastruktur

class UserRepository:

    def save(self, user: User) -> None:

        # Technische Logik ist komplett isoliert

        print(f"SQL: UPDATE users SET email='{user.email}' WHERE id={user.user_id}")

 

# Nutzung

user = User(1, "Alice", "alice@example.com")

user.change_email("alice@newdomain.com")

 

# Die Pure Fabrication führt die Speicherung durch

repo = UserRepository()

repo.save(user)