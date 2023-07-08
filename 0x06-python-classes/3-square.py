#!/usr/bin/python3
"""
A class Square
"""


class Square:
    """
    A class square that defines a square by:
    - Private instance attribute : size
    - Instantiation with optional size: def __init__(self, size=0):
    - size must be an integer, otherwise raise a TypeError
    - if size is less than 0, raise a ValueError
    """

    def __init__(self, size=0):
        """
        Initialization function
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns the current square area
        """
        return self.__size * self.__size
