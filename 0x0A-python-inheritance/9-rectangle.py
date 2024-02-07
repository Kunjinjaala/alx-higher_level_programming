#!/usr/bin/python3
"""A class Rectangle that inherits BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        Initializes the BaseGeometry instance with width and height.

        Args:
        width (int): The width of the geometry.
        height (int): The height of the geometry.
        """

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """ Returns the string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
