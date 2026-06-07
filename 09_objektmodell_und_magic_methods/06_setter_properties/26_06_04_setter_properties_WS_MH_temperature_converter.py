class Temperature:
    """A small class to save and convert a temperature.

    The class always saves the value inside in Celsius.
    The user can read or change Celsius, Fahrenheit, and Kelvin.
    """

    def __init__(self, value, unit):
        """Create a new Temperature object.

        value: the temperature number
        unit: 'C', 'F', or 'K'
        """
        self._celsius = 0.0
        unit = unit.upper()

        if unit == "C":
            self.celsius = value
        elif unit == "F":
            self.fahrenheit = value
        elif unit == "K":
            self.kelvin = value
        else:
            raise ValueError("Unit must be 'C', 'F', or 'K'.")

    @property
    def celsius(self):
        """Return the temperature in Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Save the temperature as Celsius."""
        self._celsius = float(value)

    @property
    def fahrenheit(self):
        """Return the temperature in Fahrenheit."""
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Save a Fahrenheit value as Celsius inside the object."""
        self._celsius = (float(value) - 32) * 5 / 9

    @property
    def kelvin(self):
        """Return the temperature in Kelvin."""
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value):
        """Save a Kelvin value as Celsius inside the object."""
        self._celsius = float(value) - 273.15

    def __repr__(self):
        """Return a simple text for printing and debugging."""
        return f"Temperature({self._celsius:.2f}, 'C')"


# Small test area
# You can run this part to see if the class works.
t = Temperature(100, "C")
print(t)
print(t.fahrenheit)
print(t.kelvin)

t.fahrenheit = 32
print(t.celsius)

t.kelvin = 273.15
print(t.celsius)




assert t.celsius == 0.0

t = Temperature(100, "C")
assert t.fahrenheit == 212.0
assert t.kelvin == 373.15

t = Temperature(32, "F")
assert t.celsius == 0.0

t = Temperature(273.15, "K")
assert t.celsius == 0.0

print("All tests passed.")