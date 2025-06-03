#!/usr/bin/python3
"""a function that's Reads any JSON and return python obj"""
import json


def load_from_json_file(filename):
    """a function that reads the JSON file and return python obj"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
