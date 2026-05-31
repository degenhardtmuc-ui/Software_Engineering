import math


class Form:
    """Base class for all geometric forms."""

    def __init__(self, farbe):
        """Create a form with a color."""
        self.farbe = farbe

    def flaeche(self):
        """Return the area of the form."""
        raise NotImplementedError("Die Fläche hängt von der konkreten Form ab.")

    def umfang(self):
        """Return the perimeter of the form."""
        raise NotImplementedError("Der Umfang hängt von der konkreten Form ab.")

    def beschreibung(self):
        """Return a short text about the form."""
        return f"Form mit der Farbe {self.farbe}"


class Rechteck(Form):
    """Rectangle class: has color, width and height."""

    def __init__(self, farbe, breite, hoehe):
        """Create a rectangle with color, width and height."""
        super().__init__(farbe)
        self.breite = breite
        self.hoehe = hoehe

    def flaeche(self):
        """Return the area of the rectangle."""
        return self.breite * self.hoehe

    def umfang(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.breite + self.hoehe)

    def beschreibung(self):
        """Return a detailed text about the rectangle."""
        return (
            f"Rechteck mit der Farbe {self.farbe}, "
            f"Breite {self.breite} und Höhe {self.hoehe}"
        )

    def __repr__(self):
        """Return a readable representation of the rectangle."""
        return f"Rechteck('{self.farbe}', {self.breite}, {self.hoehe})"


class Kreis(Form):
    """Circle class: has color and radius."""

    def __init__(self, farbe, radius):
        """Create a circle with color and radius."""
        super().__init__(farbe)
        self.radius = radius

    def flaeche(self):
        """Return the area of the circle."""
        return math.pi * self.radius ** 2

    def umfang(self):
        """Return the perimeter/circumference of the circle."""
        return 2 * math.pi * self.radius

    def beschreibung(self):
        """Return a detailed text about the circle."""
        return f"Kreis mit der Farbe {self.farbe} und Radius {self.radius}"

    def __repr__(self):
        """Return a readable representation of the circle."""
        return f"Kreis('{self.farbe}', {self.radius})"


rechteck = Rechteck("blau", 5.0, 3.0)
kreis = Kreis("rot", 2.0)

print(rechteck.beschreibung())
print("Fläche Rechteck:", rechteck.flaeche())
print("Umfang Rechteck:", rechteck.umfang())
print("repr Rechteck:", repr(rechteck))

print()

print(kreis.beschreibung())
print("Fläche Kreis:", kreis.flaeche())
print("Umfang Kreis:", kreis.umfang())
print("repr Kreis:", repr(kreis))