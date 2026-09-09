import pytest

from notenverwaltung.course import Course
from notenverwaltung.grade import Grade
from notenverwaltung.student import Student


@pytest.fixture
def sample_student():
    """Create a reusable sample student."""

    return Student(
        "S123",
        "Jane",
        "Doe",
        "jane.doe@example.com",
    )


@pytest.fixture
def default_course():
    """Create a course with the default 100-point scale."""

    return Course(
        "CS101",
        "Intro to CS",
        max_grade=100.0,
        passing_grade=50.0,
    )


@pytest.fixture
def custom_course():
    """Create a course with a custom 6-point scale."""

    return Course(
        "MATH201",
        "Calculus",
        max_grade=6.0,
        passing_grade=4.0,
    )


def test_valid_grade_creation(
    sample_student,
    default_course,
):
    """Test creating a valid grade."""

    grade = Grade(
        sample_student,
        default_course,
        score=85.0,
        date="2026-07-05",
    )

    assert grade.score == 85.0
    assert grade.notes == ""


def test_score_validation_boundaries(
    sample_student,
    default_course,
):
    """Test scores below zero and above the maximum."""

    with pytest.raises(ValueError):
        Grade(
            sample_student,
            default_course,
            score=-1.0,
            date="2026-07-05",
        )

    with pytest.raises(ValueError):
        Grade(
            sample_student,
            default_course,
            score=101.0,
            date="2026-07-05",
        )


def test_invalid_date_format_raises_error(
    sample_student,
    default_course,
):
    """Test that an invalid date format is rejected."""

    with pytest.raises(ValueError):
        Grade(
            sample_student,
            default_course,
            score=80.0,
            date="05-07-2026",
        )


def test_properties_with_default_course(
    sample_student,
    default_course,
):
    """Test calculated properties using the default scale."""

    grade = Grade(
        sample_student,
        default_course,
        score=92.5,
        date="2026-07-05",
    )

    assert grade.is_passing is True
    assert grade.percentage == 92.5
    assert grade.letter_grade == "A"


def test_failing_grade(
    sample_student,
    default_course,
):
    """Test a grade below the passing limit."""

    grade = Grade(
        sample_student,
        default_course,
        score=49.9,
        date="2026-07-05",
    )

    assert grade.is_passing is False
    assert grade.letter_grade == "F"


def test_properties_with_custom_course(
    sample_student,
    custom_course,
):
    """Test properties using a custom grading scale."""

    grade = Grade(
        sample_student,
        custom_course,
        score=4.5,
        date="2026-07-05",
    )

    assert grade.is_passing is True
    assert grade.percentage == 75.0
    assert grade.letter_grade == "C"


def test_readable_grade_text(
    sample_student,
    default_course,
):
    """Test the readable grade representation."""

    grade = Grade(
        sample_student,
        default_course,
        score=85.0,
        date="2026-07-05",
    )

    expected = (
        "Grade: Jane Doe | Intro to CS | "
        "Score: 85.0/100.0 (B) | PASSED"
    )

    assert str(grade) == expected