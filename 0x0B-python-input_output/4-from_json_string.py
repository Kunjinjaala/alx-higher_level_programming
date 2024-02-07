#!/usr/bin/python3
"""Returns an object represented by a JSON string."""
import json


def from_json_string(my_str):
    obj = json.loads(my_str)
    return obj
