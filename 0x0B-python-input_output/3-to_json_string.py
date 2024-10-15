#!/usr/bin/python3
""" serializes a json object to a string"""

import json


def to_json_string(my_obj):
    """changes an object to a json string

    Args:
        my_obj (object): object

    Returns:
        string: serialized object
    """
    return json.dumps(my_obj)
