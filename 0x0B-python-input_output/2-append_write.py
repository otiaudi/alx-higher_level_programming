#!/usr/bin/python3
"""Module with the function that appends a string to a file"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of the file
    args:
        filename: name of the file to write on.
        text: text to write on the file
    Return:
        Number of characters written on the file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
