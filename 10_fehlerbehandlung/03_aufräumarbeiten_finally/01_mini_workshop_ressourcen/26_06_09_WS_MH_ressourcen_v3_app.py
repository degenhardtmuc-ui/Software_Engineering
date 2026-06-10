from database import Database
from processing import process_data


def our_great_app_wrong():
    """Old version: this version does not close the database safely."""

    print("Phase 3: Wrong version")

    db = Database()

    db.connect()

    process_data(db)

    # This line is not reached if process_data() raises an error.
    db.disconnect()


def our_great_app_fixed():
    """Fixed version: this version always closes the database."""

    print("Phase 4: Fixed version")

    db = Database()

    try:
        db.connect()
        process_data(db)

    except RuntimeError as error:
        print(f"Error was handled: {error}")

    finally:
        db.disconnect()

    print(f"Database connected after app: {db.connected}")

    return db


def test_connection_is_closed():
    """Test if the database connection is really closed."""

    print("Phase 5: Test if database is closed")

    db = our_great_app_fixed()

    assert db.connected is False

    print("Test passed: database was closed.")


if __name__ == "__main__":
    # You can test the wrong version by removing the # in the next line.
    # our_great_app_wrong()

    # This is the final correct test:
    test_connection_is_closed()