# Phase 3A: JSON persistence
    

    def to_dict(self) -> dict:
        """Converts the whole grade book into simple Python data."""
        students_data = []

        for student in self.students.values():
            students_data.append(
                {
                    "student_id": student.student_id,
                    "first_name": student.first_name,
                    "last_name": student.last_name,
                    "email": student.email,
                }
            )

        courses_data = []

        for course in self.courses.values():
            courses_data.append(
                {
                    "course_id": course.course_id,
                    "name": course.name,
                    "max_grade": course.max_grade,
                    "passing_grade": course.passing_grade,
                }
            )

        grades_data = []

        for grade in self.grades:
            grades_data.append(
                {
                    "student_id": grade.student.student_id,
                    "course_id": grade.course.course_id,
                    "score": grade.score,
                    "date": grade.date,
                    "notes": grade.notes,
                }
            )

        return {
            "students": students_data,
            "courses": courses_data,
            "grades": grades_data,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "GradeBook":
        """Creates a GradeBook object from simple Python data."""
        gradebook = cls()

        for student_data in data["students"]:
            student = Student(
                student_id=student_data["student_id"],
                first_name=student_data["first_name"],
                last_name=student_data["last_name"],
                email=student_data["email"],
            )

            gradebook.add_student(student)

        for course_data in data["courses"]:
            course = Course(
                course_id=course_data["course_id"],
                name=course_data["name"],
                max_grade=course_data["max_grade"],
                passing_grade=course_data["passing_grade"],
            )

            gradebook.add_course(course)

        for grade_data in data["grades"]:
            gradebook.record_grade(
                student_id=grade_data["student_id"],
                course_id=grade_data["course_id"],
                score=grade_data["score"],
                date=grade_data["date"],
                notes=grade_data.get("notes", ""),
            )

        return gradebook

    def save_json(self, file_path: str) -> None:
        """Saves the whole grade book as a JSON file."""
        path = Path(file_path)
        data = self.to_dict()

        json_text = json.dumps(data, indent=4)
        path.write_text(json_text, encoding="utf-8")

    @classmethod
    def load_json(cls, file_path: str) -> "GradeBook":
        """Loads a grade book from a JSON file."""
        path = Path(file_path)
        json_text = path.read_text(encoding="utf-8")

        data = json.loads(json_text)

        return cls.from_dict(data)
