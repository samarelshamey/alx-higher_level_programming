#!/usr/bin/python3
"""module for BaseGeometry."""


class BaseGeometry:
    """class for basegeometry"""

    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value

        Args:
            name: string
            value: integer
        Raises:
            TypeError: if value is not integer
            ValueError: if value is <= zero
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
