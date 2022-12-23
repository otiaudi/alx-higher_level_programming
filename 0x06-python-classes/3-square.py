#!/usr/bin/python3
"""Class to represent square"""


class Square:
    """Class that defines a suare"""


def __init__(self, size=0):
    """Initializing object variable.

    args:
        size (int): size of the new square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        self.__size = size


def area(self):
    """Function that calculates area of a square
    """
    return (self.__size ** 2)
