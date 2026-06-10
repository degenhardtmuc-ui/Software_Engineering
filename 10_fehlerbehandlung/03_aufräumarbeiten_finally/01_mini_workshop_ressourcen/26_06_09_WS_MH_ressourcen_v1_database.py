class Database:
    """Small fake database class for the mini workshop."""

    def __init__(self):
        """Create a new database object."""
        self.id = f"db-{id(self) % 100}"
        self.connected = False

    def connect(self):
        """Open the fake database connection."""
        print(f"Connecting to database {self.id}.")
        self.connected = True

    def disconnect(self):
        """Close the fake database connection."""
        print(f"Disconnecting from database {self.id}.")
        self.connected = False

    def read_data(self):
        """Read data from the database."""
        if self.connected:
            print(f"Reading data from database {self.id}.")
        else:
            raise RuntimeError("Not connected to database.")


if __name__ == "__main__":
    print("Phase 1: Test database class")

    db = Database()

    print(f"Start connected: {db.connected}")

    db.connect()
    db.read_data()
    db.disconnect()

    print(f"End connected: {db.connected}")