#!/usr/bin/python3
""" Rectangle Class Module"""


class Rectangle:
    """Rectangle Class"""

    def __init__(self, width=0, height=0):
        """consturctor

        Args:
            width (int, optional): width. Defaults to 0.
            height (int, optional): height. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter

        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter

        Args:
            value (int): value width

        Raises:
            TypeError: if width is not int
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """height getter

        Returns:
            int: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter

        Args:
            value (int): height

        Raises:
            TypeError: if height is not integer
            ValueError: if height less than 0
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
