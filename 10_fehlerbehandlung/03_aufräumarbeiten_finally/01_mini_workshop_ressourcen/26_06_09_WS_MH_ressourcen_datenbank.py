class Database:
    """Einfache Beispiel-Klasse für eine Datenbankverbindung."""

    def __init__(self):
        """Erstellt ein neues Datenbank-Objekt."""
        self.id = f"db-{id(self) % 100}"
        self.connected = False

    def connect(self):
        """Öffnet die Datenbankverbindung."""
        print(f"Verbinde mit Datenbank {self.id}.")
        self.connected = True

    def disconnect(self):
        """Schließt die Datenbankverbindung."""
        print(f"Trenne Verbindung zur Datenbank {self.id}.")
        self.connected = False

    def read_data(self):
        """Liest Daten aus der Datenbank, wenn eine Verbindung besteht."""
        if self.connected:
            print(f"Lese Daten aus Datenbank {self.id}.")
        else:
            raise RuntimeError("Nicht mit der Datenbank verbunden.")


if __name__ == "__main__":
    print("Phase 1: Datenbank-Klasse einzeln testen")

    db = Database()

    print(f"Am Anfang verbunden: {db.connected}")

    db.connect()
    db.read_data()
    db.disconnect()

    print(f"Am Ende verbunden: {db.connected}")