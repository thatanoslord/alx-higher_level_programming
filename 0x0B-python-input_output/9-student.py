#!/usr/bin/python3
""" Student Module"""


class Student:
    """Student Class
    """

    def __init__(self, first_name, last_name, age):
        """Instantiation

        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Turns object to a json

        Returns:
            dict: a json representation of each key and value
        """
        return self.__dict__
