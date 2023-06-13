#!/usr/bin/python3
"""
save_to_json_file - function that writes an Object to a text file
using a JSON representation

Args:
    my_obj : the object to write to a text file
    filename : the file to write the object to

Returns:
    None
"""


import json


def save_to_json_file(my_obj, filename):
    """
    writes object to a text file using a JSON representation
    """
    with open(filename, mode = "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
