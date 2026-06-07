import datetime


class Person:
    """This class saves one person."""

    def __init__(self, first_name, last_name, birth_date):
        self._first_name = first_name
        self._last_name = last_name
        self.birth_date = birth_date

    @property
    def first_name(self):
        """Return the first name."""
        return self._first_name

    @first_name.setter
    def first_name(self, new_first_name):
        self._first_name = new_first_name

    @property
    def last_name(self):
        """Return the last name."""
        return self._last_name

    @last_name.setter
    def last_name(self, new_last_name):
        self._last_name = new_last_name

    @property
    def age(self):
        """Return the age in full years."""
        today = datetime.date.today()
        difference = today - self.birth_date
        age_in_days = difference.days
        age_in_years = age_in_days // 365
        return age_in_years

    @property
    def full_name(self):
        """Return first name and last name together."""
        return self.first_name + " " + self.last_name

    @full_name.setter
    def full_name(self, new_full_name):
        name_parts = new_full_name.split(" ")
        self.first_name = name_parts[0]
        self.last_name = name_parts[1]

    def __repr__(self):
        return (
            f"Person(first_name='{self.first_name}', "
            f"last_name='{self.last_name}', "
            f"birth_date={self.birth_date})"
        )


# Small test area
person = Person("Anna", "Muster", datetime.date(2000, 5, 20))

print(person.first_name)
print(person.last_name)
print(person.full_name)
print(person.age)

person.full_name = "Max Beispiel"

print(person.first_name)
print(person.last_name)
print(person.full_name)
print(person)