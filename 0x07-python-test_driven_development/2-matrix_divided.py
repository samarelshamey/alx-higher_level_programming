#!/usr/bin/python3
"""module for matrix_divided"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix.

    Args:
        matrix: list containing int or float
        div: number to divide matrix by

    Raises:
        TypeError: If matrix is not list of lists containing int or float.
        TypeError: If sublists are not all same size.
        TypeError: If div is not int or float.
        ZeroDivisionError: If div is zero.

    Returns:
        a new matrix
    """

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    for line in matrix:
        if not isinstance(line, list) or len(line) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(line) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in line:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(i / div, 2) for i in line] for line in matrix]

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/2-matrix_divided.txt")
