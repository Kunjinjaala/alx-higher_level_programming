#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num_integers = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            num_integers += 1
        except (TypeError, ValueError):
            pass
    print()
    return num_integers
