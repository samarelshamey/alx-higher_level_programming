#!/usr/bin/python3
"""module for square"""


class Square:
    """define a square"""

    def __init__(self, size=0):
        """Construct/

        Args:
            size: square side length
        """
        self.__size = size

    @property
    def size(self):
        """property for the side length

        Raise:
            ValueError: if size is less than 0
            TtpeError: if size is not int
        """
        return self.__size

    @size.setter
    def size(self, value):
        """define size value"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """define square area"""
        return (self.__size * self.__size)
