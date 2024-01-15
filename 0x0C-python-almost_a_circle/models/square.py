#!/usr/bin/python3
'''module for square class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    """define a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initiate square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size of square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """return  str representation of square"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.width))

    def update_args(self, id=None, size=None, x=None, y=None):
        """update arguments"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """update square"""
        if args:
            self.update_args(*args)
        elif kwargs:
            self.update_args(**kwargs)

    def to_dictionary(self):
        """return dictionary"""
        return {"id": self.id, "x": self.x,
                "size": self.width, "y": self.y}
