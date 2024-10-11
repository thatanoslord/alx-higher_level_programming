#!/usr/bin/python3
""" matrix divided by a num module"""


def matrix_divided(matrix, div):
    """divides a matrix by a num

    Args:
        matrix (list of lists): matrix
        div (int or float): number to divide by
    """

    if (not isinstance(matrix, list) or matrix == []
            or not all(isinstance(row, list) for row in matrix)
            or not all(type(num) in [int, float]
                       for row in matrix
                       for num in row)):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')

    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if type(div) not in [float, int]:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    return ([list(map(lambda x: round(x/div, 2), row))for row in matrix])
