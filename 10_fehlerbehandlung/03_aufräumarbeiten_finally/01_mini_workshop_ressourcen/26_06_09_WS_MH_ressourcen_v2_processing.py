from database import Database


def process_data(db: Database):
    """Process data from the database."""

    print(f"Processing data with database {db.id}.")

    db.read_data()

    # This is the change from the workshop.
    # Something goes wrong after reading the data.
    raise RuntimeError("Something went wrong while processing the data.")


if __name__ == "__main__":
    print("Phase 2: Test process_data function")

    db = Database()

    try:
        db.connect()
        process_data(db)
    # Die Funktion bricht absichtlich mit einem Fehler ab
    except RuntimeError as error:
        print(f"Error caught for test: {error}") 

    finally:
        db.disconnect()

    print(f"End connected: {db.connected}")