class Student:
    """Repräsentiert einen Studenten mit Name und Studienfach."""

    def __init__(
        self,
        name: str | None,
        studienfach: str | None
    ):
        """Erstellt einen Studenten.

        Name und Studienfach dürfen auch None sein.
        """
        self.name = name
        self.studienfach = studienfach

    def print_info(self) -> None:
        """Gibt Name und Studienfach sicher aus.

        Falls ein Wert None ist, wird stattdessen
        'Nicht angegeben' ausgegeben.
        """
        name_text = (
            self.name
            if self.name is not None
            else "Nicht angegeben"
        )

        fach_text = (
            self.studienfach
            if self.studienfach is not None
            else "Nicht angegeben"
        )

        print(f"Name: {name_text}")
        print(f"Studienfach: {fach_text}")


# ---------------------------------
# Fall 1: Student selbst ist None
# ---------------------------------

student1: Student | None = None

if student1 is not None:
    student1.print_info()
else:
    print("Kein Student vorhanden.")


# ---------------------------------
# Fall 2: Student existiert,
# Studienfach ist aber None
# ---------------------------------

student2 = Student(
    name="Anna",
    studienfach=None
)

student2.print_info()

==================================================
# Die Ausgabe für student2 wäre:

# Name: Anna
# Studienfach: Nicht angegeben
# Ganz einfach erklärt

# Es gibt hier zwei unterschiedliche Fälle:

# 1. student = None
#    ↓
#   Es existiert überhaupt kein Student.


# 2. Student("Anna", None)
#   ↓
#   Student existiert,
#   aber das Studienfach fehlt.

# Die Schreibweise

# student: Student | None

# bedeutet:

# „Hier kann entweder ein Student oder None stehen.“

# Und:

# if student is not None:

# bedeutet:

# „Führe den folgenden Code nur aus, wenn tatsächlich ein Student vorhanden ist.“

# Das ist in Python die natürliche Entsprechung zu dem Optional-Gedanken, den Laith gerade anhand von Java erklärt.