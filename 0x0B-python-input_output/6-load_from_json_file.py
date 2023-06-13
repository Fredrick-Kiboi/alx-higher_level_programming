#!/usr/bin/python3
"""
load_from_json_file - function that creates an Object
from a "JSON file"

Args:
    filename : The "JSON" filename

Returns:
    None
"""


import json


def load_from_json_file(filename):
    """
    creates an Object from a "JSON file"
    """
    with open(filename, 'r') as file:
        json_data = file.read()
        obj = json.loads(json_data)
        return obj
