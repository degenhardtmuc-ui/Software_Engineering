GradeBook - students: dict[str, Student] # by student_id - courses: dict[str, Course] # by course_id - grades: list[Grade] + add_student(student: Student) -> None + add_course(course: Course) -> None + record_grade(student_id, course_id, score, date, notes) -> Grade + get_student_grades(student_id: str) -> list[Grade] + get_course_grades(course_id: str) -> list[Grade] + student_average(student_id: str) -> float + course_average(course_id: str) -> float + course_pass_rate(course_id: str) -> float + top_students(n: int = 5) -> list[tuple[Student, float]] + students_at_risk(threshold: float = 60.0) -> list[Student]

GradeBook - students: dict[str, Student] # by student_id - courses: dict[str, Course] # by course_id - grades: list[Grade] + add_student(student: Student) -> None + add_course(course: Course) -> None + record_grade(student_id, course_id, score, date, notes) -> Grade + get_student_grades(student_id: str) -> list[Grade] + get_course_grades(course_id: str) -> list[Grade] + student_average(student_id: str) -> float + course_average(course_id: str) -> float + course_pass_rate(course_id: str) -> float + top_students(n: int = 5) -> list[tuple[Student, float]] + students_at_risk(threshold: float = 60.0) -> list[Student] ReportGenerator (ABC) + generate_student_report(student_id: str, gradebook: GradeBook) -> str + generate_course_report(course_id: str, gradebook: GradeBook) -> str + generate_summary_report(gradebook: GradeBook) -> str TextReportGenerator(ReportGenerator) CsvReportGenerator(ReportGenerator)

Phase Plan
Phase 1: Core Data Model with TDD (Days 1–2)

==============================================================================

# grade.py: gesamt_score = 0.0

        for g in noten:

            gesamt_score += g.score

sum(g.score for g in noten)





