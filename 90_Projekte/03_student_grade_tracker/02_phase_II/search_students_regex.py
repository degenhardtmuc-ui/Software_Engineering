def search_students(self, query: str) -> list[Student]:
        """Searches students by first name, last name or email using regex."""
        pattern = re.compile(query, re.IGNORECASE)

        return [
            student
            for student in self.students.values()
            if pattern.search(student.first_name)
            or pattern.search(student.last_name)
            or pattern.search(student.email)
            or pattern.search(student.full_name)]