#!/usr/bin/python3
"""module that contains the function that returns an object"""
import json


def from_json_string(my_str):
    """a function that returns an object represented by a JSON string
    args:
        my_str: Json string
    return:
         returns an object
    """
    return json.loads(my_str)
