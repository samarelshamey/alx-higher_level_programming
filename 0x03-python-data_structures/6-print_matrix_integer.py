#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for line in matrix:
        if len(line) == 0:
            print()
        for n in range(len(line)):
            print("{:d}".format(line[n]),
                    end="\n" if n is len(line) - 1 else " ")
