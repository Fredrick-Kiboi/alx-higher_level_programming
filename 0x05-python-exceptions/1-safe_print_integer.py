#!/usr/bin/python3

"""
Function that prints an integer with "{:d}".format()

Prototype: def safe_print_integer(value):

Args:
    value : type to be evaluated if it's an integer

Returns:
     True : if it is an integer
     False : Otherwise
"""


def safe_print_integer(value):
    """
Function that prints an integer with "{:d}".format()

Prototype: def safe_print_integer(value):

Args:
    value : type to be evaluated if it's an integer

Returns:
     True : if it is an integer
     False : Otherwise
"""
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
