#!/usr/bin/python3
"""Defines a text-indentation function."""



def text_indentation(text):
    """
    Prints the text with two new lines after each '.', '?', and ':' character.

    Args:
    - text (str): The input text.

    Raises:
    - TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    _chars = ['.', '?', ':']
    lines = text.splitlines()  # Split text into lines

    for line in lines:
        for char in line:
            print(char, end="")
            if char in _chars:
                print("\n", end="")
                print("\n", end="")
