#!/usr/bin/python3
"""
Write a function that deletes a key in a dictionary.

Prototype: def simple_delete(a_dictionary, key=""):
key argument will be always a string
If a key doesn’t exist, the dictionary won’t change
You are not allowed to import any module
"""


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
