#!/usr/bin/python3
""" Matrices Multiplication with numpy"""

from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    """Matrix Multiplication with numpy

    Args:
        m_a (list of lists of int or float): first matrix
        m_b (list of lists of int or float): second matrix

    Returns:
        list of lists: output of multiplication
    """

    return matmul(m_a, m_b)
