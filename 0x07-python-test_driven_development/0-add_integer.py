#!/usr/bin/python3
"""module for add_integer"""


def add_integer(a, b=98):
    """function to add two integers.

    Args:
        a = first integer
        b = second integer

    Raises:
        TyprError: if a or b is not int or float
    Returns:
        sum of two integers
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
