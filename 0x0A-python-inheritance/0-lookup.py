#!/usr/bin/python3


def lookup(obj):
    """return the attributes of an object

    Args:
        obj: object
    Returns:
        list of attirbute
    """
    return dir(obj)
