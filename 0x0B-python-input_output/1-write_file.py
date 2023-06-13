#!/usr/bin/python3
"""
write_file - function that writes a string to a text file

Args:
     filename (str): the file to write to
     text (str): the text to write

Returns:
    Number of characters written
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (utf-8)
    """
    with open(filename, mode="w", encoding="utf-8") as myfile:
        return myfile.write(text)
