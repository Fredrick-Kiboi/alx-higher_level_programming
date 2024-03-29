#!/usr/bin/python3
"""
to_json_string - function that returns the JSON
representation of an object(string)

Args:
    my_obj (string): the object to return the JSON rep of

Returns:
    None
"""


import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object
    """
    return json.dumps(my_obj)
