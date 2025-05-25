#!/usr/bin/python3
"""This module defines a Square class.

It includes size validation and a method to compute area.
"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize the square with a validated size.

        Args:
            size (int): Size of the square. Must be >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square.

        Returns:
            int: The area (size squared).
        """
        return self.__size ** 2
