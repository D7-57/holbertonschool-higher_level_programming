#!/usr/bin/python3
"""
This module defines a function that checks if an object
is an instance of a class or a class that inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or a subclass of it.

    Args:
        obj: The object to check.
        a_class: The target class.

    Returns:
        True if obj is an instance or subclass instance of a_class.
    """
    return isinstance(obj, a_class)
