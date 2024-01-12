#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return [replace if search == to_replace else to_replace for to_replace in my_list]

