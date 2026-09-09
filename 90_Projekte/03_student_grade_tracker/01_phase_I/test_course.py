import pytest

from notenverwaltung.course import Course


def test_course_creation_with_default_grades():
    """Test a course with its default grading rules."""

    course = Course(
        "CS101",
        "Intro to Computer Science",
    )

    assert course.course_id == "CS101"
    assert course.name == "Intro to Computer Science"
    assert course.max_grade == 100.0
    assert course.passing_grade == 50.0


def test_course_creation_with_custom_grades():
    """Test a course with custom grading rules."""

    course = Course(
        "MATH201",
        "Calculus",
        max_grade=6.0,
        passing_grade=4.0,
    )

    assert course.max_grade == 6.0
    assert course.passing_grade == 4.0


def test_invalid_max_grade_raises_value_error():
    """Test that invalid maximum grades are rejected."""

    with pytest.raises(ValueError):
        Course(
            "CS101",
            "Intro to CS",
            max_grade=0,
        )

    with pytest.raises(ValueError):
        Course(
            "CS101",
            "Intro to CS",
            max_grade=-10,
        )


def test_invalid_passing_grade_raises_value_error():
    """Test that invalid passing grades are rejected."""

    with pytest.raises(ValueError):
        Course(
            "CS101",
            "Intro to CS",
            max_grade=100,
            passing_grade=0,
        )

    with pytest.raises(ValueError):
        Course(
            "CS101",
            "Intro to CS",
            max_grade=100,
            passing_grade=-5,
        )

    with pytest.raises(ValueError):
        Course(
            "CS101",
            "Intro to CS",
            max_grade=100,
            passing_grade=101,
        )


def test_readable_course_text():
    """Test the readable course representation."""

    course = Course(
        "CS101",
        "Intro to CS",
    )

    assert str(course) == (
        "Course: Intro to CS (CS101) | "
        "Pass/Max: 50.0/100.0"
    )