#!/usr/bin/python3
"""Rotate matrix module
"""


def transpose_matrix(matrix, n):
    """ helper fuction to get matrix transpose

    """
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    """helper function that reverses a matrix

    """
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    """This rotates a 2d matrix

    """
    n = len(matrix)

    transpose_matrix(matrix, n)

    reverse_matrix(matrix)

    return matrix
