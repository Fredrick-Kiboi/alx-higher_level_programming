#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = str(argv[2])

    if operator == "+":
        print("{:d} {} {:d} = {:d}".format(a, operator, b, add(a, b)))
    elif operator == "-":
        print("{:d} {} {:d} = {:d}".format(a, operator, b, sub(a, b)))
    elif operator == "*":
        print("{:d} {} {:d} = {:d}".format(a, operator, b, mul(a, b)))
    elif operator == "/":
        print("{:d} {} {:d} = {:d}".format(a, operator, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)
