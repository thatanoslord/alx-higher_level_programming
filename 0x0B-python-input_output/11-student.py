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

    def to_json(self, attrs=None):
        """Turns object to a json

        Returns:
            dict: a json representation of each key and value
        """
        if (type(attrs) is list and all(type(a) is str for a in attrs)):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__

    def reload_from_json(self, json: dict):
        """ Updates an instance values from json"""
        for key, val in json.items():
            setattr(self, key, val)
