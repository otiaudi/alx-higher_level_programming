#!/usr/bin/python3
class Square:
    """a class that defines a square by its size
    """
    def __init__(self, size=0):
        """Method to initialize the square object

        args:
            size (int): size is the side of the square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """method to calculate the area of the square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """method to return the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Method to set the size value of the stuare object
        """
        if not isinstance(value, int):   
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
