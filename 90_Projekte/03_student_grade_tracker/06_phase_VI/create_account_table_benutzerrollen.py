def _create_account_table(
    connection: sqlite3.Connection,
) -> None:
    """Lege die Tabelle für Zugangsdaten und Benutzerrollen an."""

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS student_accounts (
            student_id TEXT PRIMARY KEY,
            password_salt TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'student',
            FOREIGN KEY (student_id)
                REFERENCES students(student_id)
                ON DELETE CASCADE
        )
        """
    )

    columns = {
        row[1]
        for row in connection.execute(
            "PRAGMA table_info(student_accounts)"
        )
    }

    if "role" not in columns:
        connection.execute(
            """
            ALTER TABLE student_accounts
            ADD COLUMN role TEXT NOT NULL DEFAULT 'student'
            """
        )