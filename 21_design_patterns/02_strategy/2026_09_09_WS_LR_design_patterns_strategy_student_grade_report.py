from abc import ABC, abstractmethod


class ReportStrategy(ABC):
    """Schnittstelle für verschiedene Report-Strategien."""

    @abstractmethod
    def generate(self) -> None:
        """Erzeugt den jeweiligen Report."""
        pass


class StudentReportStrategy(ReportStrategy):
    """Erzeugt einen Report für einen Studenten."""

    def generate(self) -> None:
        """Erstellt den Student-Report."""
        print("Student-Report wird erstellt.")


class CourseReportStrategy(ReportStrategy):
    """Erzeugt einen Report für einen Kurs."""

    def generate(self) -> None:
        """Erstellt den Course-Report."""
        print("Course-Report wird erstellt.")


class SummaryReportStrategy(ReportStrategy):
    """Erzeugt einen zusammenfassenden Report."""

    def generate(self) -> None:
        """Erstellt den Summary-Report."""
        print("Summary-Report wird erstellt.")


class ReportGenerator:
    """Erzeugt Reports mit einer austauschbaren Strategie."""

    def __init__(self, strategy: ReportStrategy):
        """Erstellt den Generator mit einer Report-Strategie."""
        self.strategy = strategy

    def set_strategy(self, strategy: ReportStrategy) -> None:
        """Wechselt die aktuelle Report-Strategie."""
        self.strategy = strategy

    def generate_report(self) -> None:
        """Führt die aktuell ausgewählte Report-Strategie aus."""
        self.strategy.generate()


# Anwendung
generator = ReportGenerator(StudentReportStrategy())
generator.generate_report()

generator.set_strategy(CourseReportStrategy())
generator.generate_report()

generator.set_strategy(SummaryReportStrategy())
generator.generate_report()

# In meinem Student Grade Tracker könnte ich Student-, Course- und Summary-Report als unterschiedliche Strategien implementieren. 
# Der ReportGenerator muss dann nicht wissen, wie der jeweilige Report erzeugt wird.“