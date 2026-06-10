class Database:
    """A small fake database connection for the workshop."""

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
        """Read data only when the database is connected."""
        if self.connected:
            print(f"Reading data from database {self.id}.")
        else:
            raise RuntimeError("Not connected to database.")


def process_data(db: Database):
    """Process data from the database."""
    print(f"Processing data with database {db.id}.")
    db.read_data()

    # This line simulates the later change in process_data().
    # The important point is: process_data() can now crash.
    raise RuntimeError("Something went wrong while processing the data.")


def our_great_app():
    """Run the app and always close the database connection."""
    db = Database()

    try:
        db.connect()
        process_data(db)

    except Exception as error:
        print(f"An error happened: {error}")

    finally:
        db.disconnect()

    print(f"Database connected after app? {db.connected}")
    assert db.connected is False
    print("Test passed: database was closed.")


our_great_app()

# Das Problem war, dass disconnect() erst nach process_data() kam. 
# Wenn process_data() durch raise einen Fehler wirft, wird disconnect() in der alten Version übersprungen. 
# Deshalb habe ich den riskanten Teil in try gepackt und disconnect() in finally gesetzt. 
# finally wird immer ausgeführt, also wird die Datenbankverbindung sicher freigegeben. 
# Danach teste ich mit assert, dass connected wirklich False ist.