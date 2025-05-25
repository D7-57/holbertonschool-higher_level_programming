#!/usr/bin/python3
"""Defines an empty class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initializes the square with a private size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
