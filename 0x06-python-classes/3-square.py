#!/usr/bin/python3
"""module for square"""


class Square:
    """define a square"""
    def __init__(self, size=0):
        """Construct/

        Args:
            size: suqare side length
        Raise:
            ValueError: if size less than zero
            TypeError: if size is not an int
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

        def area(self):
            """area of swuare
            returns:
                size of square
            """
            return (self.__size * self.__size)
