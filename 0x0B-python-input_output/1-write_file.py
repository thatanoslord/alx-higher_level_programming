#!/usr/bin/python3
"""write_file module"""


def write_file(filename="", text=""):
    """writes to a file

    Args:
        filename (str, optional): file name. Defaults to "".
        text (str, optional): text to write. Defaults to "".

    Returns:
        int: number of character written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
