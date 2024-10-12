#!/usr/bin/python3
""" Matrix multiplication module"""


def matrix_mul(m_a, m_b):
    """multiplies matrices"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all(type(num) in [int, float] for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(type(num) in [int, float] for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    b_col_len = len(m_b[0])
    b_row_len = len(m_b)

    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(b_col_len):
            sum = 0

            for k in range(b_row_len):
                sum += m_a[i][k] * m_b[k][j]
            new_row.append(sum)
        result.append(new_row)
    return (result)
