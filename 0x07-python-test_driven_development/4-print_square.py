#!/usr/bin/python3
"""print_square module"""


def print_square(size):
    """prints a square

    Raises:
        TypeError: if size is not int
        ValueError: if value < 0
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print('#' * size)
