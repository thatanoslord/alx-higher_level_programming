#!/usr/bin/python3

"""MyList Class Implementation
    """


class MyList(list):
    """MyList class a subclass of list
    """

    def __init__(self):
        """Object constructor"""
        super().__init__()

    def print_sorted(self):
        """Print a sorted list"""

        print(sorted(self))
