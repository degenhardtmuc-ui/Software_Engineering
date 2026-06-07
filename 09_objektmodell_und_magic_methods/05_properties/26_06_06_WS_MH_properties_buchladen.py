class Book:
    """This class saves simple information about a book."""

    def __init__(self, title, author):
        """Create a new book object."""
        self._title = title
        self._author = author

    @property
    def title(self):
        """Return the title. There is no setter."""
        return self._title

    @property
    def author(self):
        """Return the author. There is no setter."""
        return self._author

    @property
    def citation(self):
        """Return the citation text for the book."""
        return f'"{self.title}" by {self.author}'

    def __repr__(self):
        """Return a readable text for this book object."""
        return f"Book(title='{self.title}', author='{self.author}')"


book = Book("Der kleine Prinz", "Antoine de Saint-Exupéry")
expected_citation = '"Der kleine Prinz" by Antoine de Saint-Exupéry'

print(book)
print(book.citation)

assert book.title == "Der kleine Prinz"
assert book.author == "Antoine de Saint-Exupéry"
assert book.citation == expected_citation

print("All tests worked.")

# This line would cause an error, because title has no setter:
# book.title = "New title"