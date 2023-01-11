#!/usr/bin/python3
""" Module that defines the write function"""


def write_file(filename="", text=""):
    """ Function that writes string to a text file.
    args:
        filename: file to write on
        text: string to be written in the file.
    return:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
