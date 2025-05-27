#!/usr/bin/python3
"""a function that returns the list of available attributes and methods of an object"""


def lookup(obj):
    """a method that return a list of attribute

    Args:
        obj of any type of object

    returns:
        a list of attribute 
    """
    return dir(obj)
