#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for line in matrix:
        for n in line:
            print("{:d}".format(n), end=" ")
        print()
