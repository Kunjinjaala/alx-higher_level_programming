#!/usr/bin/python3
"""A function that writes a text file (UTF8) to the stdout"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file."""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
