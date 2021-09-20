#!/usr/bin/python3

"""A function that prints a matrix of integers"""


def print_matrix_integer(matrix=[[]]):
    for index in range(len(matrix)):
        for i in range(len(matrix[index])):
            if i != 0:
                print(" ", end='')
            print("{:d}".format(matrix[index][i]), end='')
        print()
