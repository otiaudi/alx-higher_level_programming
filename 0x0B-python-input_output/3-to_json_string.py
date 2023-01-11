#!/usr/bin/python3
"""Module that contains a function that converts string to JSON"""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object.
    args:
        my_obj: The none JSON file to be converted
    return:
        returns a JSON file.
    """
    return json.dumps(my_obj)
