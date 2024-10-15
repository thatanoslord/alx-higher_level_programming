#!/usr/bin/python3

""" append_write module """


def append_write(filename="", text=""):
    """append_write

    Args:
        filename (str, optional): name of the file. Defaults to "".
        text (str, optional): text content to append. Defaults to "".

    Returns:
        _type_: _description_
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
