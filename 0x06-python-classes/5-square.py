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

    def my_print(self):
        """ prints a square"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("#" * self.__size)
