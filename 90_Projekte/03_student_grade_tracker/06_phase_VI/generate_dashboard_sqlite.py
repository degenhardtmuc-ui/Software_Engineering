def generate_dashboard() -> str:
    """Generate dashboard values from the SQLite database."""

    if not DATABASE_PATH.exists():
        return f"Datenbank nicht gefunden: {DATABASE_PATH}"

    with sqlite3.connect(DATABASE_PATH) as connection:
        student_count = connection.execute(
            "SELECT COUNT(*) FROM students"
        ).fetchone()[0]

        course_count = connection.execute(
            "SELECT COUNT(*) FROM courses"
        ).fetchone()[0]

        grade_count = connection.execute(
            "SELECT COUNT(*) FROM grades"
        ).fetchone()[0]

        statistics = connection.execute(
            """
            SELECT
                COALESCE(AVG(g.score / c.max_grade * 100), 0),
                COALESCE(
                    AVG(
                        CASE
                            WHEN g.score >= c.passing_grade
                            THEN 100.0
                            ELSE 0.0
                        END
                    ),
                    0
                )
            FROM grades AS g
            JOIN courses AS c
                ON g.course_id = c.course_id
            """
        ).fetchone()

    overall_average = statistics[0]
    pass_rate = statistics[1]

    return f"""
| Kennzahl | Aktueller Wert |
|---|---:|
| Studenten | {student_count} |
| Kurse | {course_count} |
| Erfasste Noten | {grade_count} |
| Gesamtdurchschnitt | {overall_average:.1f} % |
| Bestehensquote | {pass_rate:.1f} % |
"""