def generate_pass_chart() -> pd.DataFrame:
    """Generate pass and fail statistics from the SQLite database."""

    if not DATABASE_PATH.exists():
        return pd.DataFrame(
            {
                "Status": [],
                "Anzahl": [],
            }
        )

    with sqlite3.connect(DATABASE_PATH) as connection:
        result = connection.execute(
            """
            SELECT
                SUM(
                    CASE
                        WHEN g.score >= c.passing_grade
                        THEN 1
                        ELSE 0
                    END
                ),
                SUM(
                    CASE
                        WHEN g.score < c.passing_grade
                        THEN 1
                        ELSE 0
                    END
                )
            FROM grades AS g
            JOIN courses AS c
                ON g.course_id = c.course_id
            """
        ).fetchone()

    passed_count = result[0] or 0
    failed_count = result[1] or 0

    return pd.DataFrame(
        {
            "Status": [
                "Bestanden",
                "Nicht bestanden",
            ],
            "Anzahl": [
                passed_count,
                failed_count,
            ],
        }
    )