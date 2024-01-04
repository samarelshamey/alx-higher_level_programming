#!/usr/bin/python3
"""module for a rectangle"""


class Rectangle:
    """define a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Construct/

        Args:
            width: rectangel width
            height: rectangle height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """property for the width

        Raise:
            TypeError: if width is not integer
            ValueError: if widtsh is less than zero
        """
        return self.__width

    @width.setter
    def width(self, value):
        """define width value"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """property for height

        Raise:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        """
        return self.__height

    @height.setter
    def height(self, value):
        """define height value"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """return rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """return string representative of a rectangle"""
        rectangle_str = ""
        if self.__width != 0 and self.__height != 0:
            rectangle_str += "\n".join("#" * self.width
                                       for _ in range(self.height))
        return rectangle_str

    def __repr__(self):
        """return string rep of rectangle for production"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """print a message for deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
