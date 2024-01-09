#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    for items in my_string:
        if items != 'c' and items != 'C':
            new_string += items
    return new_string
