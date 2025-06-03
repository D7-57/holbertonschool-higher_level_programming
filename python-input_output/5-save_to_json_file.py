#!/usr/bin/python3
"""a function that's Saves any python obj as JSON on a file"""
import json


def save_to_json_file(my_obj, filename):
    """a function that saves the JSON equivelannce to a pytohn obj on file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
