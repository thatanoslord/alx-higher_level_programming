#!/usr/bin/python3
"""MagicClass"""

import math


class MagicClass:
    """MagicClass"""

    def __init__(self, radius=0):
        """instantiate

        Args:
            radius (int or float, optional): radius. Defaults to 0.

        Raises:
            TypeError: radius must be a number
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """area

        Returns:
            float: area
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """circumference

        Returns:
            float: circumference
        """
        return (2 * math.pi * self.__radius)
