def student_average(self, student_id: str) -> float:
        """Returns the average percentage for one student."""
        grades = self.get_student_grades(student_id)

        if not grades:
            raise ValueError(f"No grades recorded for student {student_id}.")

        total_percentage = sum(grade.percentage for grade in grades)

        return total_percentage / len(grades)