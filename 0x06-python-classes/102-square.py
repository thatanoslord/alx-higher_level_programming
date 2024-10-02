#!/usr/bin/python3
""" Defining A square class """


class Square:
    """ Square """

    def __init__(self, size=0):
        """initialize square

        Args:
            size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Gets the area of square"""
        return self.__size * self.__size

    @property
    def size(self):
        """getter for size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """ setter for size attribute """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, value) -> bool:
        """Equal"""
        return self.area() == value.area()

    def __ne__(self, value) -> bool:
        """Not Equal"""
        return self.area() != value.area()

    def __lt__(self, value) -> bool:
        """Less than"""
        return self.area() < value.area()

    def __gt__(self, value) -> bool:
        """Greater than"""
        return self.area() > value.area()

    def __le__(self, value) -> bool:
        """less than or equal"""
        return self.area() <= value.area()

    def __ge__(self, value) -> bool:
        """Greater than or equal"""
        return self.area() >= value.area()
