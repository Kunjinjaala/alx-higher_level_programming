#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    for num in range(1, 4):
        try:
            if num > a:
                raise Exception('Too far')
        except Exception:
            break
        result += (a ** b) / num
    result += b + a
    return (result)

