#!/usr/bin/python3
"""
This is the first class Base
"""
import json


class Base:
    """
    Class called base
    """
    __nb_objects = 0  # Class attribute to keep track of the number of objects

    def __init__(self, id=None):
        "Initializing class attributes"
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string rep. of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
