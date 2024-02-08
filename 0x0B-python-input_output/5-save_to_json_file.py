#!/usr/bin/python3
import json
"""Writes an Object to a text file, using a JSON representation"""


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as file:
        json.dump(my_obj, file)