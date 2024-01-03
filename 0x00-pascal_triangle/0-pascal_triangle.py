#!/usr/bin/python
"""
This module contains a function to return the pascal triangle of a given size
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n

    Args:
        n (int): size of the triangle

    Returns:
        list: list of lists of integers representing the Pascal's triangle of n
    """
    if n <= 0:
        return []

    pascal = [[1]]
    top_row = [1]

    for i in range(n - 1):
        new_row = []
        for j in range(len(top_row) + 1):
            if j > 0:
                left = top_row[j - 1]
            else:
                left = 0
            if j < len(top_row):
                right = top_row[j]
            else:
                right = 0
            new_row.append(left + right)
        pascal.append(new_row)
        top_row = new_row

    return pascal
