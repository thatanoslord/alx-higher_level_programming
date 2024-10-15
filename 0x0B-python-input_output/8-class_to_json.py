#!/usr/bin/python3
"""class_to_json module"""


def class_to_json(obj):
    """returns dictionary representation of obj

    Args:
        obj (object): object

    Returns:
        dict: dictionary representation
    """

    return obj.__dict__
