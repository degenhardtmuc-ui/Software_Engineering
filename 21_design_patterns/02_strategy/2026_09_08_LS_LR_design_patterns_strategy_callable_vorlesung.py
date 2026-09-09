from abc import ABC, abstractmethod


class Vorlesung(ABC):
    """Schnittstelle für verschiedene Vorlesungen."""

    @abstractmethod
    def besuchen(self) -> None:
        """Besucht die jeweilige Vorlesung."""
        pass


class PythonVorlesung(Vorlesung):
    """Konkrete Strategie für eine Python-Vorlesung."""

    def besuchen(self) -> None:
        """Besucht die Python-Vorlesung."""
        print("Besuche Python-Vorlesung.")


class JavaVorlesung(Vorlesung):
    """Konkrete Strategie für eine Java-Vorlesung."""

    def besuchen(self) -> None:
        """Besucht die Java-Vorlesung."""
        print("Besuche Java-Vorlesung.")


class Student:
    """Student mit einer austauschbaren Vorlesungsstrategie."""

    def __init__(self, name: str):
        """Erstellt einen Studenten."""
        self.name = name
        self.vorlesung = None

    def set_vorlesung(self, vorlesung: Vorlesung) -> None:
        """Legt fest, welche Vorlesung besucht wird."""
        self.vorlesung = vorlesung

    def besuche_vorlesung(self) -> None:
        """Besucht die aktuell ausgewählte Vorlesung."""
        if self.vorlesung:
            self.vorlesung.besuchen()


# Anwendung
student = Student("Daniel")

student.set_vorlesung(PythonVorlesung())
student.besuche_vorlesung()

student.set_vorlesung(JavaVorlesung())
student.besuche_vorlesung()