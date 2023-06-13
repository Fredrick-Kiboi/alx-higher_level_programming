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
        myfile.write(text)

    with open(filename, mode="r", encoding="utf-8") as myfile:
        line = myfile.read()
        wordList = line.split()
        count = 0
        for words in wordList:
            for char in words:
                count += 1
        return count
