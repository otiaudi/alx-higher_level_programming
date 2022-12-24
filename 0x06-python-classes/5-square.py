#!/bin/python3
"""Class blue print"""


class Square:
    """class to create objects"""
    def __init__(self, size=0):
        """Method to initialize the size variable.
        args:
            size (int): size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Method to retrieve instance variable size"""
        return self.__size

    @size.setter
    def size(self, value):
        """method to set instance variable"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    def area(self): 
        """Method that returns the area of a square"""
        return (self.__size * self.__size)
    
    def my_print(self):
        """Method that print the square of with the character '#'"""
        if not self.__size :
            print()
            print("--")
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end='')
                print()

