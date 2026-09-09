def import_grades_from_csv(self, file_path: str) -> dict:
    """Import grades from a CSV file and return an import report."""

    report = {
        "imported": 0,
        "skipped": 0,
        "errors": [],
    }

    # =====================================================
    # REGEX-ZEILE
    # =====================================================
    pattern = re.compile(
        r"^([^,]+),([^,]+),([0-9]+(?:\.[0-9]+)?),(\d{4}-\d{2}-\d{2})$"
    )

    try:
        path = Path(file_path)
        lines = path.read_text(encoding="utf-8").splitlines()

        for line_number, line in enumerate(lines[1:], start=2):
            match = pattern.match(line)

            if match is None:
                report["skipped"] += 1
                report["errors"].append(
                    f"Line {line_number}: Invalid CSV format."
                )
                continue

            student_id = match.group(1)
            course_id = match.group(2)
            score = float(match.group(3))
            date = match.group(4)

            try:
                self.record_grade(
                    student_id=student_id,
                    course_id=course_id,
                    score=score,
                    date=date,
                )
                report["imported"] += 1

            except (StudentNotFoundError, CourseNotFoundError, ValueError) as error:
                report["skipped"] += 1
                report["errors"].append(
                    f"Line {line_number}: {error}"
                )

        return report

    except OSError as error:
        raise PersistenceError(
            f"Could not import grades from CSV file: {file_path}"
        ) from error