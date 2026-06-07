class Rectangle:
    """A simple rectangle with width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the width."""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width. Negative values are not allowed."""
        if value < 0:
            raise ValueError("Width cannot be negative.")
        self._width = value

    @property
    def height(self):
        """Return the height."""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height. Negative values are not allowed."""
        if value < 0:
            raise ValueError("Height cannot be negative.")
        self._height = value

    @property
    def area(self):
        """Calculate the area of the rectangle."""
        return self._width * self._height

    @property
    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self._width + self._height)

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height}, area={self.area}, perimeter={self.perimeter})"


rectangle = Rectangle(5, 3)

print(rectangle)
print("Area:", rectangle.area)
print("Perimeter:", rectangle.perimeter)

rectangle.width = 10
rectangle.height = 4

print(rectangle)

assert rectangle.width == 10
assert rectangle.height == 4
assert rectangle.area == 40
assert rectangle.perimeter == 28