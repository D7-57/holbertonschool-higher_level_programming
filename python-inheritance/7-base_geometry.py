#!/usr/bin/python3
"""Defines class baseGeometry that raise an error"""


class BaseGeometry:
    """Represents a Geometery."""
    def area(self):
        """calculate the area but nothing implemented yet so throw exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate an integer.

        Args:
            value (int): int to validate.
            name (string): name associated with the int

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
