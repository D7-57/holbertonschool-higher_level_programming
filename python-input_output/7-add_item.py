#!/usr/bin/python3
"""Adds command line arguments to a Python list and saves it to a JSON file."""


import sys
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Try to load existing items or start with an empty list
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Append new command line arguments (skip the script name at index 0)
items.extend(sys.argv[1:])

# Save updated list
save_to_json_file(items, filename)
