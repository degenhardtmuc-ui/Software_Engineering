from dataclasses import dataclass
from datetime import datetime

from notenverwaltung.course import Course
from notenverwaltung.student import Student


@dataclass
class Grade:
    """Connects one student with one course and one score."""

    student: Student
    course: Course
    score: float
    date: str
    notes: str = ""

    def __post_init__(self) -> None:
        """Validate score and date after initialization."""

        if not 0 <= self.score <= self.course.max_grade:
            raise ValueError(
                "score must be between 0 and course.max_grade."
            )

        try:
            datetime.fromisoformat(self.date)
        except ValueError as error:
            raise ValueError(
                "date must use ISO format YYYY-MM-DD."
            ) from error

    @property
    def is_passing(self) -> bool:
        """Return True if the score reaches the passing grade."""

        return self.score >= self.course.passing_grade

    @property
    def percentage(self) -> float:
        """Return the score as a percentage of the maximum grade."""

        return self.score / self.course.max_grade * 100

    @property
    def letter_grade(self) -> str:
        """Return a letter grade based on the percentage."""

        percentage = self.percentage

        if percentage >= 90:
            return "A"

        if percentage >= 80:
            return "B"

        if percentage >= 70:
            return "C"

        if percentage >= 60:
            return "D"

        return "F"

    def __str__(self) -> str:
        """Return a readable text representation of the grade."""

        status = "PASSED" if self.is_passing else "FAILED"

        return (
            f"Grade: {self.student.full_name} | "
            f"{self.course.name} | "
            f"Score: {self.score}/{self.course.max_grade} "
            f"({self.letter_grade}) | {status}"
        )