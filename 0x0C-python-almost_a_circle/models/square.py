#!/usr/bin/python3
"""module for square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """define a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".\
                format(self.id, self.x, self.y, self.width)

    def update_args(self, id=None, size=None, x=None, y=None):
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        if args:
            self.update_args(*args)
        elif kwargs:
            self.update_args(**kwargs)

    def to_dictionary(self):
        return {"id": self.id, "x": self.x,
                "size": self.width, "y": self.y}
