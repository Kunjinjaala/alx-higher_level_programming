#!/usr/bin/python3
"""A Python class-to-JSON function."""


def class_to_json(obj):
    return obj.__dict__
