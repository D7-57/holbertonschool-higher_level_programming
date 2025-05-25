#!/usr/bin/python3
"""This module defines a Square class with size access and update."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize the square with a validated size.

        Args:
            size (int): Size of the square. Must be >= 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): New size to assign.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square.

        Returns:
            int: Area computed as size squared.
        """
        return self.__size ** 2
