#!/usr/bin/python3
"""
Function that prints a dictionary by ordered keys
Key sort is in alphabetical order

Args:
    a dictionary

Returns: 
    a sorted dictionary
"""


def print_sorted_dictionary(a_dictionary):
   [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
