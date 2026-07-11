class GradeBook:
    """Manages students, courses, grades and grade statistics."""

    def __init__(self) -> None:
        """Creates an empty grade book."""
        self.students: dict[str, Student] = {}
        self.courses: dict[str, Course] = {}
        self.grades: list[Grade] = []
    
    def add_student(self, student: Student) -> None:
        """Adds one student to the grade book."""
        if student.student_id in self.students:
            raise ValueError(f"Student with ID {student.student_id} already exists.")

        self.students[student.student_id] = student

    def add_course(self, course: Course) -> None:
        """Adds one course to the grade book."""
        if course.course_id in self.courses:
            raise ValueError(f"Course with ID {course.course_id} already exists.")

        self.courses[course.course_id] = course