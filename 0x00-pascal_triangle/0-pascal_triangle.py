#!/usr/bin/python3

"""A function that creates a pascal triangle
    out of numbers"""


def pascal_triangle(n):
    """Function that creates a pascal triangle, using
        n as the limit for the base."""

    if n <= 0:
        return []

    # Initialize the Pascal's triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        # Generate the next row based on the previous row
        prev_row = triangle[-1]
        next_row = [1]

        for j in range(1, i):
            next_row.append(prev_row[j - 1] + prev_row[j])

        next_row.append(1)
        triangle.append(next_row)

    return triangle
