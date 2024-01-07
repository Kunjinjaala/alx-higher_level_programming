#!/usr/bin/python3

for alphabet in range(ord('z'), ord('a') - 1, -1):
    if alphabet % 2 == 0:
        upper_f = 0
    else:
        upper_f = 32
    print((chr(alphabet - upper_f)), end='')
