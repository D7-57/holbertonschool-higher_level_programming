#!/usr/bin/python3
"""Module that defines a function to read and print a file content."""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its content to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
