def create_database_gradebook() -> GradeBook:
    """Erzeuge ein GradeBook aus den Daten der SQLite-Datenbank."""
    gradebook = GradeBook()

    with sqlite3.connect(DATABASE_PATH) as connection:
        students = connection.execute(
            """
            SELECT student_id, first_name, last_name, email
            FROM students
            ORDER BY student_id
            """
        ).fetchall()

        courses = connection.execute(
            """
            SELECT course_id, name, max_grade, passing_grade
            FROM courses
            ORDER BY course_id
            """
        ).fetchall()

        grades = connection.execute(
            """
            SELECT student_id, course_id, score, date, notes
            FROM grades
            ORDER BY date
            """
        ).fetchall()

    for student_id, first_name, last_name, email in students:
        gradebook.add_student(
            Student(student_id, first_name, last_name, email)
        )

    for course_id, name, max_grade, passing_grade in courses:
        gradebook.add_course(
            Course(course_id, name, max_grade, passing_grade)
        )

    for student_id, course_id, score, date, notes in grades:
        gradebook.record_grade(
            student_id,
            course_id,
            score,
            date,
            notes or "",
        )

    return gradebook