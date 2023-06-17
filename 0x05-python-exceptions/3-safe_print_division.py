#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        global quotient
        quotient = a / b
    except ZeroDivisionError:
        quotient = None
    finally:
        print(f"Inside result: {quotient}")
        return (quotient)
