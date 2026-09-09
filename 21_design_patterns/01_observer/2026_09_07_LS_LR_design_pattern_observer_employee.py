class Employee:

 

  def __init__(self, name: str, employee_id: int | str):

    self.name = name

    self.id = employee_id

 

  def calculate_pay(self) -> None:

    print(f"CalculatePay für {self.name} (ID: {self.id})...")

 

  def report_hours(self) -> None:

    print(f"ReportHours für {self.name} (ID: {self.id})...")

 

  def print_report(self) -> None:

    print(f"PrintReport für {self.name} (ID: {self.id})...")



=====

employee = Employee("Max Mustermann", 42) employee.calculate_pay() employee.report_hours() employee.print_report()

=====

Gott Klassen

=====================================================================

# high cohesion
# SRP Single Responisibility 
# SRP trennt Verantwortlichkeiten. 
# High Cohesion hält zusammengehörige Dinge zusammen. 
# Low Coupling reduziert unnötige Abhängigkeiten.



from dataclasses import dataclass


@dataclass
class Employee:
    # Verantwortung: Mitarbeiterdaten
    name: str
    id: int


class PayCalculator:
    # Verantwortung: Gehaltsberechnung
    def calculate_pay(self, employee: Employee) -> None:
        print(f"CalculatePay für {employee.name}")


class TimeTracker:
    # Verantwortung: Zeiterfassung
    def report_hours(self, employee: Employee) -> None:
        print(f"ReportHours für {employee.name}")


class EmployeeReporter:
    # Verantwortung: Berichterstellung
    def print_report(self, employee: Employee) -> None:
        print(f"PrintReport für {employee.name}")

# Vorher:

# Employee
# ├── Mitarbeiterdaten
# ├── calculatePay()
# ├── reportHours()
# └── printReport()

# Eine Klasse → mehrere Verantwortlichkeiten → SRP verletzt.

# Nachher:

# Employee          → Mitarbeiterdaten
# PayCalculator     → Gehaltsberechnung
# TimeTracker       → Zeiterfassung
# EmployeeReporter  → Reporting

# Jede Klasse hat einen klaren Aufgabenbereich → hohe Kohäsion → SRP erfüllt!

========================================================================

# Die erste Lösung

from abc import ABC, abstractmethod

from dataclasses import dataclass

 

 

# 1. Pure Data Entity

@dataclass

class Employee:

  name: str

  id: int | str

 

 

# 2. Interfaces (Abstraktionen)

class IPayCalculator(ABC):

 

  @abstractmethod

  def calculate_pay(self, employee: Employee) -> None:

    pass

 

 

class ITimeTracker(ABC):

 

  @abstractmethod

  def report_hours(self, employee: Employee) -> None:

    pass

 

 

class IEmployeeReporter(ABC):

 

  @abstractmethod

  def print_report(self, employee: Employee) -> None:

    pass

 

 

# 3. Konkrete Implementierungen

class StandardPayCalculator(IPayCalculator):

 

  def calculate_pay(self, employee: Employee) -> None:

    print(f"CalculatePay für {employee.name} (ID: {employee.id})...")

 

 

class StandardTimeTracker(ITimeTracker):

 

  def report_hours(self, employee: Employee) -> None:

    print(f"ReportHours für {employee.name} (ID: {employee.id})...")

class StandardEmployeeReporter(IEmployeeReporter):

 

  def print_report(self, employee: Employee) -> None:

    print(f"PrintReport für {employee.name} (ID: {employee.id})...")

 

# Anwendungsbeispiel mit Dependency Injection:

if __name__ == "__main__":

  emp = Employee(name="Max Mustermann", id=42)

 

  # Auswechselbare Implementierungen gegen Interfaces

  pay_service: IPayCalculator = StandardPayCalculator()

  time_service: ITimeTracker = StandardTimeTracker()

  report_service: IEmployeeReporter = StandardEmployeeReporter()

 

  pay_service.calculate_pay(emp)

  time_service.report_hours(emp)

  report_service.print_report(emp)







========================================================================

Ultimative Lösung

==============

from abc import ABC, abstractmethod

from dataclasses import dataclass

 

 

# 1. Pure Data Entity (entspricht 'Book')

@dataclass

class Employee:

  name: str

  id: int | str

 

 

# 2. Interfaces (entspricht 'BookDAO' & 'BookPrinter')

class EmployeePayCalculator(ABC):

 

  @abstractmethod

  def calculate_pay(self) -> None:

    pass

 

 

class EmployeeTimeTracker(ABC):

 

  @abstractmethod

  def report_hours(self) -> None:

    pass

 

 

class EmployeeReporter(ABC):

 

  @abstractmethod

  def print_report(self) -> None:

    pass

 # 3. Konkrete Klassen (entspricht 'SQLBookDAO' & 'ColorBookPrinter')

class StandardPayCalculator(EmployeePayCalculator):

 

  def __init__(self, employee: Employee):

    self._employee = employee  # entspr. -book : Book

 

  def calculate_pay(self) -> None:

    print(

        f"CalculatePay für {self._employee.name} (ID: {self._employee.id})..."

    )

 

class StandardTimeTracker(EmployeeTimeTracker):

 

  def __init__(self, employee: Employee):

    self._employee = employee  # entspr. -book : Book

 

  def report_hours(self) -> None:

    print(

        f"ReportHours für {self._employee.name} (ID: {self._employee.id})..."

    )

 

class StandardEmployeeReporter(EmployeeReporter):

 

  def __init__(self, employee: Employee):

    self._employee = employee  # entspr. -book : Book

 

  def print_report(self) -> None:

    print(

        f"PrintReport für {self._employee.name} (ID: {self._employee.id})..."

    )

# Anwendungsbeispiel:

if __name__ == "__main__":

  emp = Employee(name="Max Mustermann", id=42)

 

  # Instanziierung analog zu Bild 2 (Service hält Referenz auf die Entität)

  pay_service: EmployeePayCalculator = StandardPayCalculator(emp)

  time_service: EmployeeTimeTracker = StandardTimeTracker(emp)

  report_service: EmployeeReporter = StandardEmployeeReporter(emp)

 

  pay_service.calculate_pay()

  time_service.report_hours()

  report_service.print_report()



===================================================================================


class SkillObserver:
    """Beobachtet Änderungen an den Skills eines Mitarbeiters."""

    def update(self, employee) -> None:
        """Zeigt die aktuellen Skills des Mitarbeiters an."""
        print(f"{employee.name}: {employee.skills}")


class Employee:
    """Repräsentiert einen Mitarbeiter mit verschiedenen Skills."""

    def __init__(self, name: str):
        """Erstellt einen Mitarbeiter ohne Skills und Beobachter."""
        self.name = name
        self.skills = []
        self.observers = []

    def attach(self, observer) -> None:
        """Meldet einen Beobachter an."""
        self.observers.append(observer)

    def detach(self, observer) -> None:
        """Meldet einen Beobachter ab."""
        self.observers.remove(observer)

    def notify(self) -> None:
        """Informiert alle Beobachter über eine Änderung."""
        for observer in self.observers:
            observer.update(self)

    def add_skill(self, skill: str) -> None:
        """Fügt einen Skill hinzu und informiert die Beobachter."""
        self.skills.append(skill)
        self.notify()


# Anwendung
employee = Employee("Daniel")
observer = SkillObserver()

employee.attach(observer)

employee.add_skill("Python")
employee.add_skill("SQL")

===================================================================

add_skill("Python")
       ↓
    notify()
       ↓
    update()
       ↓
Observer reagiert


====================================================================
# Observer – nur bei mindestens 75 % Skill-Match
    
class SkillMatchObserver:
    """Wird bei einem ausreichenden Skill-Match informiert."""

    def update(self, employee, percentage: float) -> None:
        """Zeigt den erreichten Skill-Match an."""
        print(
            f"{employee.name} erreicht "
            f"{percentage:.0f} % Skill-Match."
        )


class Employee:
    """Repräsentiert einen Mitarbeiter mit seinen Skills."""

    def __init__(self, name: str, skills: list[str]):
        """Erstellt einen Mitarbeiter mit vorhandenen Skills."""
        self.name = name
        self.skills = set(skills)
        self.observers = []

    def attach(self, observer) -> None:
        """Meldet einen Beobachter an."""
        self.observers.append(observer)

    def notify(self, percentage: float) -> None:
        """Informiert alle angemeldeten Beobachter."""
        for observer in self.observers:
            observer.update(self, percentage)

    def check_match(self, required_skills: list[str]) -> None:
        """Prüft, wie viele geforderte Skills vorhanden sind."""
        required = set(required_skills)

        if not required:
            return

        matches = self.skills & required
        percentage = len(matches) / len(required) * 100

        if percentage >= 75:
            self.notify(percentage)


# Anwendung
employee = Employee(
    "Daniel",
    ["Python", "SQL", "Git"]
)

observer = SkillMatchObserver()
employee.attach(observer)

required = [
    "Python",
    "SQL",
    "Git",
    "Docker"
]

employee.check_match(required)