def top_students(self, n: int = 5) -> list[tuple[Student, float]]:
        """Returns the top N students by average percentage."""
        averages = []

        for student_id, student in self.students.items():
            student_grades = self.get_student_grades(student_id)

            if student_grades:
                average = self.student_average(student_id)
                averages.append((student, average))

        averages.sort(key=lambda item: item[1], reverse=True)

        return averages[:n]