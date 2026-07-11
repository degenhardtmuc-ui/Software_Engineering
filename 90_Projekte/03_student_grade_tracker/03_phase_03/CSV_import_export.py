# Phase 3B: CSV export and import for grades
    

    def export_grades_to_csv(self, file_path: str) -> None:
        """Exports all grades as a simple CSV file."""
        path = Path(file_path)

        lines = ["student_id,course_id,score,date"]

        for grade in self.grades:
            line = (
                f"{grade.student.student_id},"
                f"{grade.course.course_id},"
                f"{grade.score},"
                f"{grade.date}"
            )

            lines.append(line)

        csv_text = "\n".join(lines)
        path.write_text(csv_text, encoding="utf-8")

    def import_grades_from_csv(self, file_path: str) -> dict:
        """Imports grades from a CSV file and returns an import report."""
        path = Path(file_path)
        lines = path.read_text(encoding="utf-8").splitlines()

        report = {
            "imported": 0,
            "skipped": 0,
            "errors": [],
        }

        pattern = re.compile(
            r"^([^,]+),([^,]+),([0-9]+(?:\.[0-9]+)?),(\d{4}-\d{2}-\d{2})$"
        )

        for line_number, line in enumerate(lines, start=1):
            if line_number == 1 and line == "student_id,course_id,score,date":
                continue

            match = pattern.match(line)

            if not match:
                report["skipped"] = report["skipped"] + 1
                report["errors"].append(f"Line {line_number}: invalid format")
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

                report["imported"] = report["imported"] + 1

            except ValueError as error:
                report["skipped"] = report["skipped"] + 1
                report["errors"].append(f"Line {line_number}: {error}")

        return report