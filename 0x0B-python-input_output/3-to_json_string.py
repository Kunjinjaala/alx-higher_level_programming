#!/usr/bin/python3
"""Returns the JSON representation of an object (string)."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    json_str = json.dumps(my_obj)
    return json_str
