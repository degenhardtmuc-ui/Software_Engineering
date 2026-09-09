from dataclasses import dataclass


@dataclass
class Student:
    """Represents one student in the grade tracker."""

    student_id: str
    first_name: str
    last_name: str
    email: str

    def __post_init__(self) -> None:
        """Validate the student data after initialization."""

        if not self.student_id.strip():
            raise ValueError("student_id must not be empty.")

        if not self.first_name.strip():
            raise ValueError("first_name must not be empty.")

        if not self.last_name.strip():
            raise ValueError("last_name must not be empty.")

        if "@" not in self.email:
            raise ValueError("email must contain '@'.")

    @property
    def full_name(self) -> str:
        """Return the student's first and last name."""

        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        """Return a readable text representation of the student."""

        return (
            f"Student: {self.full_name} "
            f"(ID: {self.student_id}, Email: {self.email})"
        )