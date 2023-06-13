#!/usr/bin/python3
"""
class_to_json - function that returns the dictionary description
for JSON serialization of an object

Args:
    obj : instance of a class

Returns:
    dictionary desciption
"""


def class_to_json(obj):
    """
    returns the dictionary description
    """
    return obj.__dict__
