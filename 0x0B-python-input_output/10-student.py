#!/usr/bin/python3
"""module for class student"""


class Student:
    """class for student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        if not isinstance(attrs, list):
            return self.__dict__
        diction = dict()
        for attr in attrs:
            if not isinstance(attr, str):
                return self.__dict__
            if attr in self.__dict__:
                diction[attr] = self.__dict__[attr]
        return diction
