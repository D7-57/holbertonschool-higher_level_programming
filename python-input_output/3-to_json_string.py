#!/usr/bin/python3
"""a function that's convert any python ogject to JSON string"""
import json


def to_json_string(my_obj):
    """a function that returns the string equivelant to a python object"""
    return json.dumps(my_obj)
