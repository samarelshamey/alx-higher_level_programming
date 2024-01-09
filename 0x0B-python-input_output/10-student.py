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
        try:
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        dictionary = dict()
        for k, v in self.__dict__.items():
            if k in attrs:
                dictionary(k) = v
        return dictionary
