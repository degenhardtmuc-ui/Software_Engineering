def students_at_risk(self, threshold: float = 60.0) -> list[Student]:
        """Returns students whose average percentage is below the threshold."""
        at_risk_students = []

        for student_id, student in self.students.items():
            student_grades = self.get_student_grades(student_id)

            if student_grades:
                average = self.student_average(student_id)

                if average < threshold:
                    at_risk_students.append(student)

        return at_risk_students