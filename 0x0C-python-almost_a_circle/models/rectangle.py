#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self._validate_int_positive("width", value)
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self._validate_int_positive("height", value)
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self._validate_int_non_negative("x", value)
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self._validate_int_non_negative("y", value)
        self.__y = value

    def _validate_int_positive(self, attr_name, value):
        """Validate if the value is an integer and positive."""
        if not isinstance(value, int):
            raise TypeError(f"{attr_name} must be an integer")
        if value <= 0:
            raise ValueError(f"{attr_name} must be > 0")

    def _validate_int_non_negative(self, attr_name, value):
        """Validate if the value is an integer and non-negative."""
        if not isinstance(value, int):
            raise TypeError(f"{attr_name} must be an integer")
        if value < 0:
            raise ValueError(f"{attr_name} must be >= 0")

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            self._update_from_args(args)
        elif kwargs:
            self._update_from_kwargs(kwargs)

    def _update_from_args(self, args):
        """Update attributes from positional arguments."""
        attributes = ["id", "width", "height", "x", "y"]
        for i, arg in enumerate(args):
            setattr(self, attributes[i], arg)

    def _update_from_kwargs(self, kwargs):
        """Update attributes from keyword arguments."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return
    f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
