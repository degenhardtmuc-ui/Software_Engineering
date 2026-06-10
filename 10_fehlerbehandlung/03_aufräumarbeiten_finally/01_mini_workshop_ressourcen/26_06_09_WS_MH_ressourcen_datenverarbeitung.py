from datenbank import Database


def process_data(db: Database):
    """Verarbeitet Daten aus der Datenbank."""

    print(f"Verarbeite Daten mit Datenbank {db.id}.")

    db.read_data()

    # Diese Zeile simuliert eine spätere Änderung in der Funktion.
    # Dadurch kann process_data() jetzt plötzlich mit einem Fehler abbrechen.
    raise RuntimeError("Beim Verarbeiten der Daten ist ein Fehler passiert.")


if __name__ == "__main__":
    print("Phase 2: Datenverarbeitung einzeln testen")

    db = Database()

    try:
        db.connect()
        process_data(db)

    except RuntimeError as fehler:
        print(f"Fehler im Test abgefangen: {fehler}")

    finally:
        db.disconnect()

    print(f"Am Ende verbunden: {db.connected}")