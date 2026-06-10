from datenbank import Database
from daten_verarbeitung import process_data


def our_great_app_wrong():
    """Alte Version: Diese Version schließt die Datenbank nicht sicher."""

    print("Phase 3: Falsche Version")

    db = Database()

    db.connect()

    process_data(db)

    # Diese Zeile wird nicht mehr erreicht,
    # wenn process_data() vorher einen Fehler auslöst.
    db.disconnect()


def our_great_app_fixed():
    """Verbesserte Version: Diese Version schließt die Datenbank immer."""

    print("Phase 4: Verbesserte Version")

    db = Database()

    try:
        db.connect()
        process_data(db)

    except RuntimeError as fehler:
        print(f"Der Fehler wurde behandelt: {fehler}")

    finally:
        db.disconnect()

    print(f"Datenbank nach der App noch verbunden: {db.connected}")

    return db


def test_connection_is_closed():
    """Testet, ob die Datenbankverbindung wirklich geschlossen wurde."""

    print("Phase 5: Test, ob die Datenbank geschlossen wurde")

    db = our_great_app_fixed()

    assert db.connected is False

    print("Test bestanden: Die Datenbank wurde geschlossen.")


if __name__ == "__main__":
    # Die falsche Version kann man testen,
    # wenn man in der nächsten Zeile das # entfernt.
    # our_great_app_wrong()

    # Das ist der richtige finale Test:
    test_connection_is_closed()