#!/usr/bin/python3
"""
append_write - function that appends a string at the end of a text file(utf-8)

Args:
     filename (str): filename to append string to
     text (str): the string to append to the file

Returns:
    The number of characters added
"""


def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8") as myfile:
        return myfile.write(text)
