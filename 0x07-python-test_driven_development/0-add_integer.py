#!/usr/bin/python3

""" Integer Addition Function """


def add_integer(a, b=98):
    """ Addition of 2 integers

    Args:
        a (int or float): first number
        b (int or float, optional): second number. Defaults to 98.

    Raises:
        TypeError: If a or b are not float or int

    Returns:
        int: 2 numbers additions
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')

    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    return int(a) + int(b)
