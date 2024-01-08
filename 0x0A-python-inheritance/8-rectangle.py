#!/usr/bin/python3
"""module for Rectangle"""


class Rectangle(BaseGeometry):
    """rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.height = height
        self.width = width
