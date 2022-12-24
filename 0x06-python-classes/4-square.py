#!/usr/bin/python3
""" Define a class"""


class Square:
    """A class that defines a square of its size."""
    def __init__(self, size=0):
        """Method that initializes the size variable

        args:
            size (int): the size of the side of the square
        """
        self.size = size

    @property
    def size(self):
        """ Method that get the size variable"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Method that sets the value """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Method that returns the area of a square"""
        return (self.__size * self.__size)
