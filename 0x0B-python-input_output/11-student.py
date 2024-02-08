#!/usr/bin/python3
"""A class Student"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student."""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {attr: getattr(self, attr) for
                    attr in attrs if hasattr(self, attr)}
        return self.__dict__

        def reload_from_json(self, json):
            """Replace all attributes of the Student."""

        for attr, val in json.items():
            setattr(self, attr, val)
