#!/usr/bin/python3
def square_matrix_simple(matrix: list = []):
    new_matrix = []
    for i in matrix:
        row = list(map(lambda x: x**2, i))
        new_matrix.append(row)
        return new_matrix
