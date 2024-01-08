#!/usr/bin/python3
"""module for is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """check if obj is an instance of a_class
        or inheritance of a_class
    
    Args:
        obj: object
        a_class: class

    Returns: true of false
    """
    return isinstance(obj, a_class)
