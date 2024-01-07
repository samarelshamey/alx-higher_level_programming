#!/usr/bin/python3
"""module for print_square"""


def print_square(size):
    """print square

    Args:
        size: is the size length of the square

    Raises:
        TypeError: if size is not int
        ValueError: if size is less than zero
        TypeError: if size is a float and is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    print((("#" * size + "\n") * size), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
