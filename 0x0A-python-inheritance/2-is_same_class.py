#!/usr/bin/python3
"""module for is_same_class"""


def is_same_class(obj, a_class):
    """checks if the object is exactly an instance of the specified class

    Args:
        obj: object
        a_class: class

    Returns:
        True: if the object is exactly an instance of the specified class
        False: if the object isn't exactly an instance of the specified class
    """
    if isinstance(obj, class):
        return True
    else:
        return False
