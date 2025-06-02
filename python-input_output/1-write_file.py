#!/usr/bin/python3
"""a function that let the user choose a text and a filepath to write"""


def write_file(filename="", text=""):
    """write a UTF-8 text file and overwrite its content."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
