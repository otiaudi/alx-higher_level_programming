#!/usr/bin/python3

"""Square class that defines the square."""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """The method that initializes the square.

        args:
            size (int): The size of a new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
