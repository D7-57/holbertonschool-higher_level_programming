#!/usr/bin/python3
"""a function that let the user choose a text and a filepath to write"""


def append_write(filename="", text=""):
    """append a UTF-8 text file and overwrite its content.

    args: filename is the filepath, and text represent the string to write

    returns the number of character to be written
    """
    with open(filename, "a", encoding="utf-8") as f:
        txt = text
        return f.write(txt)
