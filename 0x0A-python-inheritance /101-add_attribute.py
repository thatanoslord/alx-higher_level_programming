#!/usr/bin/python3
"""Add attribute module
    """


def add_attribute(obj, att, value):
    """Function to check whether an attribute exists and add it

    Args:
        obj (object): object
        att (string): attribute to add
        value (any): value of the object

    Raises:
        TypeError: if the attribute already exists
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
