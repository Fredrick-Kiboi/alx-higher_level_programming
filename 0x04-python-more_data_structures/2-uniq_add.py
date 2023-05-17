#!/usr/bin/python3

"""
Function that adds all unique integers in a list
Only once for each integer

Args:A list

Returns: The sum of the unique integers
"""

def uniq_add(my_list=[]):
    result = 0
    for x in set(my_list):
        result += x
    return (result)

