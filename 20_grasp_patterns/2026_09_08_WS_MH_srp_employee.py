#Schlecht:

class Employee:
    """Beispiel für eine Klasse mit zu vielen Verantwortlichkeiten."""

    def calculate_pay(self):
        """Berechnet das Gehalt."""
        pass

    def report_hours(self):
        """Erfasst Arbeitsstunden."""
        pass

    def print_report(self):
        """Erstellt einen Bericht."""
        pass

# Besser:
from dataclasses import dataclass


@dataclass
class Employee:
    """Speichert ausschließlich die Daten eines Mitarbeiters."""

    name: str
    employee_id: int


class PayCalculator:
    """Ist ausschließlich für die Gehaltsberechnung zuständig."""

    def calculate_pay(self, employee: Employee) -> None:
        """Berechnet das Gehalt eines Mitarbeiters."""
        print(f"Berechne Gehalt für {employee.name}.")


class TimeTracker:
    """Ist ausschließlich für die Zeiterfassung zuständig."""

    def report_hours(self, employee: Employee) -> None:
        """Erfasst die Arbeitszeit eines Mitarbeiters."""
        print(f"Erfasse Arbeitszeit für {employee.name}.")


class EmployeeReporter:
    """Ist ausschließlich für Mitarbeiterberichte zuständig."""

    def print_report(self, employee: Employee) -> None:
        """Erstellt einen Bericht für einen Mitarbeiter."""
        print(f"Erstelle Report für {employee.name}.")


        
# Ganz einfach:

# Employee         → Daten
# PayCalculator    → Gehalt
# TimeTracker      → Zeit
# EmployeeReporter → Bericht

# SRP = eine Klasse hat einen klaren Grund, sich zu ändern.