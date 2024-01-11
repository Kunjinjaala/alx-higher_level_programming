#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1.py import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operators = {"+": addition, "-": subtraction, "*": multiplication, "/": division}
    for operator in operators:
        if operator not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    
    a = int(a)
    b = int(b)
    print("{} {} {} = {}".format(a, operator, b, 

