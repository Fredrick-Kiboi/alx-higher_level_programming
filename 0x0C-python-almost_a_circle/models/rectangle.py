#!/usr/bin/python3
"""First Rectangle"""
from models.base import Base


class Rectangle(Base):
    """A class rectangle that inherits from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = None
        self.__height = None
        self.__x = None
        self.__y = None
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        # Overide string method
        return (
            "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height))

    # Width getter and setter
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    # Height getter and setter
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    # x getter and setter
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    # y getter and setter
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance with the character #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)
