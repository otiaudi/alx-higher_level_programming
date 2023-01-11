#!/usr/bin/python3
""" Module that contains a function that reads a file """


def read_file(filename=""):
    """ function that reads a text file (UTF8) and prints it to stdout.
    args:
        filename: Name of the file that is to be accessed
    """

    with open(filename, "r", encoding="utf - 8") as file1:
        read_file = file1.read()
        print(read_file, end="")
