#!/usr/bin/python3
"""Pascal Triangle Module"""


def pascal_triangle(n):
    """Pascal triangle implementation"""

    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) < n:
        lastRow = triangle[-1]
        curr = [1]

        for i in range(len(lastRow)-1):
            curr.append(lastRow[i] + lastRow[i+1])
        curr.append(1)

        triangle.append(curr)
    return triangle
