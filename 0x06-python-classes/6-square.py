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
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialization function
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Gets what the value of the attribute is"""
        return self.__size

    @size.setter
    def size(self, size):
        """Sets the value of the attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """Gets the value of the attribute"""
        return self.__position

    @position.setter
    def position(self, position):
        """Sets the value of the attribute"""
        if not isinstance(position, tuple) or len(position) != 2 or \
                not all(isinstance(num, int) and num >= 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """
        Returns the current square area
        """
        return self.__size * self.__size

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print("\n", end="")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
