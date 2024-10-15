#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """reads a file

    Args:
        filename (str, optional): file name. Defaults to "".
    """
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
