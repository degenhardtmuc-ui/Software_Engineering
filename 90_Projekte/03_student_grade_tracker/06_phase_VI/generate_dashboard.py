def generate_dashboard() -> str:
    """Generate the dashboard values from the current gradebook."""
    gradebook = create_demo_gradebook()

    student_count = len(gradebook.students)
    course_count = len(gradebook.courses)
    grade_count = len(gradebook.grades)

    if grade_count > 0:
        total_percentage = sum(
            grade.percentage for grade in gradebook.grades
        )
        overall_average = total_percentage / grade_count

        passed_count = sum(
            1 for grade in gradebook.grades if grade.is_passing
        )
        pass_rate = passed_count / grade_count * 100
    else:
        overall_average = 0.0
        pass_rate = 0.0

    return f"""
| Kennzahl | Aktueller Wert |
|---|---:|
| Studenten | {student_count} |
| Kurse | {course_count} |
| Erfasste Noten | {grade_count} |
| Gesamtdurchschnitt | {overall_average:.1f} % |
| Bestehensquote | {pass_rate:.1f} % |
"""