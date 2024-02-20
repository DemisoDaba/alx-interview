#!/usr/bin/python3
"""0-rotate_2d_matrix.py"""


def rotate_2d_matrix(matrix):
    n = len(matrix)

    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            top = matrix[first][i]
            matrix[first][i] = matrix[last - i + first][first]
            matrix[last - i + first][first] = matrix[last][last - i + first]
            matrix[last][last - i + first] = matrix[i][last]
            matrix[i][last] = top
