#!/usr/bin/python3
"""Returns the JSON representation of an object (string)."""


import json


def to_json_string(my_obj):
    json_str = json.dumps(my_obj)
    return json_str
