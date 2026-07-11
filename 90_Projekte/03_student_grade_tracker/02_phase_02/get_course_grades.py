def get_course_grades(self, course_id: str) -> list[Grade]:
        """Returns all grades for one course."""
        if course_id not in self.courses:
            raise ValueError(f"Course with ID {course_id} does not exist.")

        return [grade for grade in self.grades if grade.course.course_id == course_id]