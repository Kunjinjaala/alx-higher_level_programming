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
