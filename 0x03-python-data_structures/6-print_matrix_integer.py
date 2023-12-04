#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for n in line:
            print("{:d}".format(n), end=" ")
        print()
