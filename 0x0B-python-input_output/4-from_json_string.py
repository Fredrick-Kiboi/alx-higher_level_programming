#!/usr/bin/python3
"""
from_json_string - function that returns an object (Python dat
structure) represented by a JSON string:

Args:
    my_str : JSON string to convert to an object

Returns:
    Converted object
"""


import json


def from_json_string(my_str):
    """
    returns an object represented by a JSON string
    """
    return json.loads(my_str)
