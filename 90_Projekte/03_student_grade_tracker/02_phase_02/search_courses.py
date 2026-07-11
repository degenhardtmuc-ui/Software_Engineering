def search_courses(self, query: str) -> list[Course]:
        """Searches courses by course name using regex."""
        pattern = re.compile(query, re.IGNORECASE)

        return [course for course in self.courses.values() if pattern.search(course.name)]