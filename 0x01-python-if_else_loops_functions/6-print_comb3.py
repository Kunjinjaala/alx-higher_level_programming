#!/usr/bin/python3

for num in range(0,10):
    for num_2 in range(num + 1, 10):
        print(f"{num}{num_2}", end=", " if num !=8 or num_2 != 9 else "\n")
