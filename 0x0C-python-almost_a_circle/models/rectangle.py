#!/usr/bin/python3
'''Module for Rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor.'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.error_msg("width", value, False)
        self.__width = value

    @property
    def height(self):
        """rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.error_msg("height", value, False)
        self.__height = value

    @property
    def x(self):
        """x of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.error_msg("x", value)
        self.__x = value

    @property
    def y(self):
        """y of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.error_msg("y", value)
        self.__y = value

    def error_msg(self, name, value, eq=True):
        """method to validate value and raise errors"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """area of rectangle"""
        return self.width * self.height

    def display(self):
        """print str represntation of rectangle"""
        print("\n" * self.y, end="")
        for _ in range(self.__height):
            print(" " * self.x, end="")
            print("#" * self.__width)

    def __str__(self):
        """return str"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".\
                format(self.id, self.x, self.y, self.width, self.height)

    def update_args(self, id=None, width=None, height=None, x=None, y=None):
        """update instance attribute """
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """update instance"""
        if args:
            self.update_args(*args)
        elif kwargs:
            self.update_args(**kwargs)

    def to_dictionary(self):
        """return dictionary"""
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
