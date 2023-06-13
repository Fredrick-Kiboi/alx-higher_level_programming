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
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
