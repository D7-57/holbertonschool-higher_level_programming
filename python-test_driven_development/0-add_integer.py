#!/usr/bin/python3
"""
 a function that adds two integers.

The function ensures inputs are integers or floats
"""


def add_integer(a, b=98):
    """
    Adds two numbers after checking they are int or float types.

    Args:
        a The first number (int or float).
        b The second number (int or float, default is 98).

    Returns:
        The sum of a and b.

    Raises:
        TypeError If a or b are not int or float.
        ValueError If a or b infinite.
    """
    import math

    for var, name in [(a, "a"), (b, "b")]:
        if not isinstance(var, (int, float)):
            raise TypeError(f"{name} must be an integer")
        if isinstance(var, float) and (math.isnan(var) or math.isinf(var)):
            raise ValueError(f"{name} must be a finite number")

    return int(a) + int(b)
