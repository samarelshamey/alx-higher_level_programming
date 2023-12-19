#!/usr/bin/python3
"""module for square"""


class Square:
    """define a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Construct/

        Args:
            size: square side length
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """property for the positionof square"""
        return self.__position

    @position.setter
    def position(self, value):
        """define position value"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                any(n < 0 for n in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """return square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """print a square"""
        if self.__size == 0:
            print()
            return
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        """define print() square"""
        if self.__size != 0:
            [print("") for n in range(0, self.__position[1])]
        for n in range(0, self.__size):
            [print(" ", end="") for i in range(0, self._position[0])]
            [print("#", end=="") for j in range(0, self.__size)]
        if n != self.__size - 1:
            print("")
            return ("")
