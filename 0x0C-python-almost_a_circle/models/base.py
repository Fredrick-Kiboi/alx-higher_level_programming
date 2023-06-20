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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        json_str = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs])
        with open(filename, "w") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation of json_string"""
        if json_string is None or json_string == "":
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all the attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy Square instance
        dummy.update(**dictionary)  # alling update with **dictionary as kwargs
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances loaded from a file"""
        filename = cls.__name__ + ".json"  # Generating filename based on class
        try:
            with open(filename, "r", encoding="utf-8") as file:
                json_string = file.read()  # Read file contents
                # Convert JSON string to dict
                dictionaries = Base.from_json_string(json_string)
                instances = []  # List to store the instances
                for dictionary in dictionaries:
                    # Create an instance using the dictionary
                    instance = cls.create(**dictionary)
                    instances.append(instance)  # Add the instance to the list
                return instances
        except FileNotFoundError:
            return []  # Return an empty list if the file doesn't exist
