#!/usr/bin/python3
"""
This module defines a function that checks if an object
inherits from a specified class but is not exactly that class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a subclass of a_class.

    Args:
        obj: The object to check.
        a_class: The target base class.

    Returns:
        True if obj inherits from a_class but is not exactly a_class.
    """
    return not (type(obj) is a_class) and isinstance(obj, a_class)
