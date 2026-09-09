import pytest

from notenverwaltung.student import Student


def test_valid_student_creation():
    """Test creating a valid student."""

    student = Student(
        "S123",
        "Jane",
        "Doe",
        "jane.doe@example.com",
    )

    assert student.student_id == "S123"
    assert student.full_name == "Jane Doe"


def test_readable_student_text():
    """Test the readable student representation."""

    student = Student(
        "S123",
        "Jane",
        "Doe",
        "jane.doe@example.com",
    )

    assert str(student) == (
        "Student: Jane Doe "
        "(ID: S123, Email: jane.doe@example.com)"
    )


def test_empty_student_id_raises_value_error():
    """Test that an empty student ID is rejected."""

    with pytest.raises(ValueError):
        Student(
            "",
            "Jane",
            "Doe",
            "jane.doe@example.com",
        )


def test_empty_first_name_raises_value_error():
    """Test that an empty first name is rejected."""

    with pytest.raises(ValueError):
        Student(
            "S123",
            "",
            "Doe",
            "jane.doe@example.com",
        )


def test_empty_last_name_raises_value_error():
    """Test that an empty last name is rejected."""

    with pytest.raises(ValueError):
        Student(
            "S123",
            "Jane",
            "",
            "jane.doe@example.com",
        )


def test_invalid_email_raises_value_error():
    """Test that an invalid email address is rejected."""

    with pytest.raises(ValueError):
        Student(
            "S123",
            "Jane",
            "Doe",
            "janedoe.example.com",
        )