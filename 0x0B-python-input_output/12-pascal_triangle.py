#!/usr/bin/python3
"""module for Pascal's Triangle"""


def pascal_triangle(n):
    """returns a list of lists of int representing Pascal’s triangle of n"""
    if n <= 0:
        return []
    triangle = [[1]]
    while len(triangle) is not n:
        t = triangle[-1]
        temp = [1]
        for i in range(len(t) - 1):
            temp.append(t[i] + t[i + 1])
        tmp.append(1)
        triangle.append(temp)
    return triangle
