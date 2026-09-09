def search_courses(self, query: str) -> list[Course]:
    """Searches courses by course name."""
    query = query.lower()
    results = []

    for course in self.courses.values():
        if query in course.name.lower():
            results.append(course)

    return results