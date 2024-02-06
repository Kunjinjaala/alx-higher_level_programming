#!/usr/bin/python3
"""A class chcking function."""


def is_kind_of_class(obj, a_class):
    """
    Returns True or False if the object is an instance of a class
    that inherited from the specified class; otherwise False.
    """
    return isinstance(obj, a_class)
