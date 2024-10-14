#!/usr/bin/python3
"""Rectangle class module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """RectangleClass

    Args:
        BaseGeometry: Base Geometry parent class
    """

    def __init__(self, width, height):
        """instantation

        Args:
            width (int): width
            height (int): height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area of rectangle

        Returns:
            int: area
        """
        return self.__width * self.__height

    def __str__(self):
        """printable output of Rectangle class

        Returns:
            string: printable output
        """
        output = "[" + str(self.__class__.__name__) + "] "
        output += str(self.__width) + "/" + str(self.__height)

        return output
