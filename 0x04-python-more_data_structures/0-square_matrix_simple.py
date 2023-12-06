#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return (list(map(lambda doubles: list(map(lambda a: a**2, doubles)), matrix)))
