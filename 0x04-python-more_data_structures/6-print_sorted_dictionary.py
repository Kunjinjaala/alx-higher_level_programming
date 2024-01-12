#!/usr/bin/python3


def print_sorted_dictionary(my_dict):
    ordered_keys = sorted(my_dict.keys())
    for key in ordered_keys:
        print("{}: {}".format(key, my_dict[key]))
