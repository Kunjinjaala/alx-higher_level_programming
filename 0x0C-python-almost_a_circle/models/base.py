#!/usr/bin/python3
"""A Python class named Base"""


class Base:
    """A representation of the base for all other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

