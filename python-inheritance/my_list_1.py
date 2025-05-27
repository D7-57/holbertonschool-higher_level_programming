#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list
and adds a method to print the list sorted in ascending order.
"""


class MyList(list):
    """
    A subclass of list that includes a method to print
    the list in sorted order without modifying the original list.
    """
    def print_sorted(self):
        """
        Prints a sorted version of the list without changing the original.
        """
        print(sorted(self))
