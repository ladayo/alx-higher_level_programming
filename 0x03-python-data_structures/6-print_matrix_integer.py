#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for out_matrix in matrix:
            for i in out_matrix:
                if i == out_matrix[len(out_matrix) - 1]:
                    print("{:d}".format(i), end='')
                else:
                    print("{:d}".format(i), end=' ')
            print()
