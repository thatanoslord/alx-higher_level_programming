#!/usr/bin/python3
""" load from file"""

import json


def load_from_json_file(filename):
    """load json from file

    Args:
        filename (str): file name

    Returns:
        obj: json
    """
    with open(filename) as f:
        return json.load(f)
