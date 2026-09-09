def login_from_form(
    student_id: str,
    password: str,
) -> str:
    """Verbinde das Anmeldeformular mit der Passwortprüfung."""

    return login_student(
        DATABASE_PATH,
        student_id,
        password,
    )

================================================================

def login_from_form(
    student_id: str,
    password: str,
):
    """Prüfe die Anmeldung und erzeuge eine Benutzersitzung."""

    login_message = login_student(
        DATABASE_PATH,
        student_id,
        password,
    )

    if not login_message.startswith("Anmeldung erfolgreich."):
        return login_message, "", ""

    student_id = student_id.strip().upper()

    with sqlite3.connect(DATABASE_PATH) as connection:
        account = connection.execute(
            """
            SELECT role
            FROM student_accounts
            WHERE student_id = ?
            """,
            (student_id,),
        ).fetchone()

    if account is None:
        return "Benutzerkonto nicht gefunden.", "", ""

    role = account[0]

    return login_message, student_id, role

=========================
# Anmeldemeldung + Student-ID + Rolle