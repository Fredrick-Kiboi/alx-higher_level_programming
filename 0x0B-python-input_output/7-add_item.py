#!/usr/bin/python3
"""Module to load and save"""
import sys
from typing import List
import json


def save_to_json_file(my_obj: List[str], filename: str) -> None:
    """Saves a Python object to a JSON file"""
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename: str) -> List[str]:
    """Loads a Python object from a JSON file"""
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)


if __name__ == "__main__":
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
