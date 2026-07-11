def course_pass_rate(self, course_id: str) -> float:
        """Returns the percentage of passing grades for one course."""
        grades = self.get_course_grades(course_id)

        if not grades:
            raise ValueError(f"No grades recorded for course {course_id}.")

        passing_grades = 0

        for grade in grades:
            if grade.is_passing:
                passing_grades = passing_grades + 1

        return passing_grades / len(grades) * 100