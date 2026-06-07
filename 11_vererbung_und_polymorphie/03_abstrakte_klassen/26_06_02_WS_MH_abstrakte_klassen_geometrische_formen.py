from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Basisklasse fuer alle geometrischen Formen."""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    """Ein Rechteck hat eine Breite und eine Hoehe."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Ein Kreis hat einen Radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    """Ein Dreieck hat drei Seiten und eine Hoehe."""

    def __init__(self, side_a, side_b, side_c, height_a):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.height_a = height_a

    def area(self):
        return self.side_a * self.height_a / 2

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


class Drawing:
    """Eine Zeichnung sammelt mehrere Formen in einer Liste."""

    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def total_area(self):
        total = 0
        for shape in self.shapes:
            total = total + shape.area()
        return total

    def total_perimeter(self):
        total = 0
        for shape in self.shapes:
            total = total + shape.perimeter()
        return total


rectangle1 = Rectangle(5, 3)
circle1 = Circle(4)
triangle1 = Triangle(6, 5, 5, 4)

print("Rechteck Flaeche:", rectangle1.area())
print("Rechteck Umfang:", rectangle1.perimeter())
print("Kreis Flaeche:", round(circle1.area(), 2))
print("Kreis Umfang:", round(circle1.perimeter(), 2))
print("Dreieck Flaeche:", triangle1.area())
print("Dreieck Umfang:", triangle1.perimeter())

drawing = Drawing()
drawing.add_shape(rectangle1)
drawing.add_shape(circle1)
drawing.add_shape(triangle1)

print("Gesamtflaeche:", round(drawing.total_area(), 2))
print("Gesamtumfang:", round(drawing.total_perimeter(), 2))

assert rectangle1.area() == 15
assert rectangle1.perimeter() == 16
assert round(circle1.area(), 2) == 50.27
assert round(circle1.perimeter(), 2) == 25.13
assert triangle1.area() == 12
assert triangle1.perimeter() == 16
assert round(drawing.total_area(), 2) == 77.27
assert round(drawing.total_perimeter(), 2) == 57.13

print("Alle Tests sind erfolgreich.")