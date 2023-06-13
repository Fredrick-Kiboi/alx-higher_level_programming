#!/usr/bin/python3

"""
read_file - function that reads a text file (UTF-8) and prints to stdout

Args:
    filename (str): the file to read from

Returns:
    None
"""

def read_file(filename=""):
    with open(filename, mode="r", encoding="utf-8") as myfile:
        print(myfile.read())
