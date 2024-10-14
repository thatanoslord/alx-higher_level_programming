#!/usr/bin/python3
"""Square Module Details"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square

    Args:
        Rectangle: Rectangle Parent
    """

    def __init__(self, size):
        """Instantiation

        Args:
            size (int): size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
