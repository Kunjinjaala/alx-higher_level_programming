#!/usr/bin/python3
"""An inherited class-checking function."""


def inherits_from(obj, a_class):
    """
        Checks if obj is an inherited instance of a_class and returns;True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
