#!/usr/bin/python3
"""This module defines a Square class with position-based printing."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position.

        Args:
            size (int): The size of the square. Must be >= 0.
            position (tuple): Tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position of the square.

        Returns:
            tuple: Tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a valid position tuple.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(v, int) for v in value) or
                not all(v >= 0 for v in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square.

        Returns:
            int: Area computed as size squared.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' and respect the position.

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
            return

        # Print vertical offset (new lines)
        for _ in range(self.__position[1]):
            print()

        # Print each row with horizontal space offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
