#!/usr/bin/python3
"""a function that's convert any JSON string to python object"""
import json


def from_json_string(my_str):
    """a function that returns the python obj equivelant to a JSON str"""
    return json.loads(my_str)
