#!/usr/bin/python3
"""Function that returns Pascal’s triangle up to n rows."""


def pascal_triangle(n):
    """Return Pascal's triangle as a list of lists of integers."""
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # Start with 1

        # Compute the middle values
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # End with 1
        triangle.append(new_row)

    return triangle
