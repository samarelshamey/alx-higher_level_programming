#!/usr/bin/python3
'''Module for square'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.size = size
        super().__init__(size, size)

    def area(self):
        return sel.__size * self__size
