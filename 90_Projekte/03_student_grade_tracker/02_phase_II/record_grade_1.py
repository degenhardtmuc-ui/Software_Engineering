def record_grade(self, student_id: str, course_id: str, score: float, date: str, notes: str = "",) -> Grade:
        """Creates and stores one grade for an existing student and course."""
        if student_id not in self.students:
            raise ValueError(f"Student with ID {student_id} does not exist.")

        if course_id not in self.courses:
            raise ValueError(f"Course with ID {course_id} does not exist.")

        student = self.students[student_id]
        course = self.courses[course_id]

        grade = Grade( student=student, course=course, score=score, date=date, notes=notes,)

        self.grades.append(grade)

        return grade