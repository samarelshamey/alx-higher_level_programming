#!/usr/bin/python3
"""module for square"""


class Square:
    """define a square"""

    def __init__(self, size=0):
        """Construct/

        Args:
            size: square side length
        """
        self.size = size

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
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """return square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """print a square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
