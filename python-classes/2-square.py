#!/usr/bin/python3
"""Defines a class Square with a private size attribute."""

class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initializes the square with a private size.
        
        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        """check if size is greater than 0 else throw an exception """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
