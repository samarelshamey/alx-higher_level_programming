#!/usr/bin/python3
"""module for inherits_from"""


def inherits_from(obj, a_class):
    """check if the object is an instance of a class that inherited

    Args:
        obj: object
        a_class: class

    Return:
        true or false
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
