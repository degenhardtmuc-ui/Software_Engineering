def course_average(self, course_id: str) -> float:
        """Returns the average score for one course."""
        grades = self.get_course_grades(course_id)

        if not grades:
            raise ValueError(f"No grades recorded for course {course_id}.")

        total_score = sum(grade.score for grade in grades)

        return total_score / len(grades)