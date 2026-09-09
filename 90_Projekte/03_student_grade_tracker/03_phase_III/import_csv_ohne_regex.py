import csv


def import_grades_from_csv(self, file_path: str) -> dict:
    """Import grades from a CSV file and return an import report."""

    report = {
        "imported": 0,
        "skipped": 0,
        "errors": [],
    }

    try:
        with open(file_path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            for line_number, row in enumerate(reader, start=2):
                try:
                    student_id = row["student_id"]
                    course_id = row["course_id"]
                    score = float(row["score"])
                    date = row["date"]

                    self.record_grade(
                        student_id=student_id,
                        course_id=course_id,
                        score=score,
                        date=date,
                    )

                    report["imported"] += 1

                except (
                    KeyError,
                    TypeError,
                    ValueError,
                    StudentNotFoundError,
                    CourseNotFoundError,
                ) as error:
                    report["skipped"] += 1
                    report["errors"].append(
                        f"Line {line_number}: {error}"
                    )

        return report

    except OSError as error:
        raise PersistenceError(
            f"Could not import grades from CSV file: {file_path}"
        ) from error