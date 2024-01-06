#!/usr/bin/python3

lower_ascii = ord('a')

for i in range(26):
    print_chr = chr(lower_ascii + i)
    if print_chr != 'e' and print_chr != 'q':
        print(print_chr, end='')

print()
