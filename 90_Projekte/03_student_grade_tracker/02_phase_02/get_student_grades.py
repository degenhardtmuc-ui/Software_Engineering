def get_student_grades(self, student_id: str) -> list[Grade]:
        """Returns all grades for one student."""
        if student_id not in self.students:
            raise ValueError(f"Student with ID {student_id} does not exist.")

        return [grade for grade in self.grades if grade.student.student_id == student_id]