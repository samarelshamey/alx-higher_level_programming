#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in range(len(matrix)):
            for n in range(len(matrix[row])):
                if n != len(matrix[row]) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                print("{:d}".format(matrix[row][n]), end=endspace)
            print()
