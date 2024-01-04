#!/usr/bin/python3
"""module for a rectangle"""


class Rectangle:
    """define a rectangle"""
    def __init__(self, width=0, height=0):
        """Construct/

        Args:
            width: rectangel width
        """
        self.width = width

    @property
    def width(self):
        """property for the width

        raise:
        TypeError: if width is not integer
        ValueError: if widtsh is less than zero
        """
        return self.__width

    @width.setter
    def width(self, value):
        """define width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property for height

        raise:
        TypeError: if height is not an integer
        ValueError: if height is less than zero
        """
        return self.__height

    @height.setter
    def height(self, value):
        """define height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        sel.__height = value
