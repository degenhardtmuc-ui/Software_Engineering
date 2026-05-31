"""
Workshop Aufgabe 1 - Mitarbeiter
This file shows inheritance with Mitarbeiter, Arbeiter and Manager.
"""


class Mitarbeiter:
    """Base class for all employees in the company."""

    def __init__(self, name, personalnummer, grundgehalt):
        """Save the data that every employee has."""
        self.name = name
        self.personalnummer = personalnummer
        self.grundgehalt = grundgehalt

    def gehalt(self):
        """Calculate the basic salary with 13 monthly salaries."""
        return self.grundgehalt * 13 / 12


class Arbeiter(Mitarbeiter):
    """Worker class: a worker also has overtime and an hourly wage."""

    def __init__(self, name, personalnummer, grundgehalt, ueberstunden, stundenlohn):
        """Save basic employee data and the extra worker data."""
        super().__init__(name, personalnummer, grundgehalt)
        self.ueberstunden = ueberstunden
        self.stundenlohn = stundenlohn

    def gehalt(self):
        """Calculate salary: basic salary plus overtime payment."""
        basis_gehalt = super().gehalt()
        ueberstunden_bezahlung = self.ueberstunden * self.stundenlohn
        return basis_gehalt + ueberstunden_bezahlung


class Manager(Mitarbeiter):
    """Manager class: a manager also has a bonus."""

    def __init__(self, name, personalnummer, grundgehalt, bonus):
        """Save basic employee data and the manager bonus."""
        super().__init__(name, personalnummer, grundgehalt)
        self.bonus = bonus

    def gehalt(self):
        """Calculate salary: basic salary plus bonus."""
        basis_gehalt = super().gehalt()
        return basis_gehalt + self.bonus


# Create a worker from the task.
hans = Arbeiter("Hans", 123, 36000.0, 3.5, 40.0)
print("Gehalt Hans:", hans.gehalt(), "Euro")

# Test the worker class.
assert hans.name == "Hans"
assert hans.personalnummer == 123
assert hans.grundgehalt == 36000.0
assert hans.ueberstunden == 3.5
assert hans.stundenlohn == 40.0
assert isinstance(hans, Mitarbeiter)
assert isinstance(hans, Arbeiter)
assert round(hans.gehalt(), 2) == 39140.0

# Create a manager from the task.
sepp = Manager("Sepp", 843, 60000.0, 30000.0)
print("Gehalt Sepp:", sepp.gehalt(), "Euro")

# Test the manager class.
assert sepp.name == "Sepp"
assert sepp.personalnummer == 843
assert sepp.grundgehalt == 60000.0
assert sepp.bonus == 30000.0
assert isinstance(sepp, Mitarbeiter)
assert isinstance(sepp, Manager)
assert round(sepp.gehalt(), 2) == 95000.0

print("Alle Tests erfolgreich.")