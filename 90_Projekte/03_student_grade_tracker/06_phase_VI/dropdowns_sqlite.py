def load_student_choices():
    """Lade die Studentenauswahl aus SQLite."""
    with sqlite3.connect(DATABASE_PATH) as connection:
        students = connection.execute(
            """
            SELECT student_id, first_name, last_name
            FROM students
            ORDER BY student_id
            """
        ).fetchall()

    return [
        (f"{student_id} - {first_name} {last_name}", student_id)
        for student_id, first_name, last_name in students
    ]


def load_course_choices():
    """Lade die Kursauswahl aus SQLite."""
    with sqlite3.connect(DATABASE_PATH) as connection:
        courses = connection.execute(
            """
            SELECT course_id, name
            FROM courses
            ORDER BY course_id
            """
        ).fetchall()

    return [
        (f"{course_id} - {name}", course_id)
        for course_id, name in courses
    ]


student_choices = load_student_choices()
course_choices = load_course_choices()