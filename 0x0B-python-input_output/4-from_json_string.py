#!/usr/bin/python3
""" deserializes a string to a json"""

import json


def from_json_string(my_str):
    """turn a string to json obj

    Args:
        my_str (string): string to parse

    Returns:
        object: json object
    """
    return json.loads(my_str)
