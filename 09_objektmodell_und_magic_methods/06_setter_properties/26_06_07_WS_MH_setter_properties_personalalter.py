import datetime


class Person:
    """A simple person with first name, last name and birth date."""

    def __init__(self, first_name, last_name, birth_date):
        self._first_name = first_name
        self._last_name = last_name
        self.birth_date = birth_date

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, new_first_name):
        self._first_name = new_first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, new_last_name):
        self._last_name = new_last_name

    @property
    def age(self):
        today = datetime.date.today()
        difference = today - self.birth_date
        return difference.days // 365

    @property
    def full_name(self):
        return self._first_name + " " + self._last_name

    @full_name.setter
    def full_name(self, new_full_name):
        name_parts = new_full_name.split(" ")
        self._first_name = name_parts[0]
        self._last_name = name_parts[1]

    def __repr__(self):
        return (
            f"Person(first_name='{self.first_name}', "
            f"last_name='{self.last_name}', "
            f"birth_date={self.birth_date})"
        )


# Small test area
person = Person("Daniel", "Degenhardt", datetime.date(1981, 1, 1))

print(person.first_name)
print(person.last_name)
print(person.full_name)
print(person.age)

person.full_name = "Max Mustermann"

print(person.first_name)
print(person.last_name)
print(person.full_name)
print(person)