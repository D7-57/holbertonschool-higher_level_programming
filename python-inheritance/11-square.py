#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that defines a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a square with size validation.

        Args:
            size (int): The size of the square (width and height).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """return the str format for class square"""
        return f"[Square] {size}/{size}"
