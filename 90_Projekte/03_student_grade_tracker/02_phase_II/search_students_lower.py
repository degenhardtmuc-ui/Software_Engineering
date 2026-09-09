def search_students(self, query: str) -> list[Student]:
    """Searches students by first name, last name or email."""
    query = query.lower()
    results = []

    for student in self.students.values():
        if (
            query in student.first_name.lower()
            or query in student.last_name.lower()
            or query in student.email.lower()
            or query in student.full_name.lower()
        ):
            results.append(student)

    return results