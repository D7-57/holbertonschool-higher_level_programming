#!/usr/bin/python3
"""a function thats allow us to choose a file path and print the content"""


def read_file(filename=""):
    """function take one argument the file path and print the content """
        with open(filename) as f:
        contetn = f.read()
        print(contetn)
        f.seek(0)
