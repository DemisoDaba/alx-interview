#!/usr/bin/python3
"""This module defines the function minOperations"""


def minOperations(num_H):
    """This function takes as argument
        num_H: number of H characters that should be printed
        and returns the number of operations to achieve that"""
    if not isinstance(num_H, int) or num_H <= 0:
        return 0
    copy_var = 1
    rep_var = 1
    op_count = 0
    while rep_var < num_H:
        if num_H % rep_var == 0:
            copy_var = rep_var
            rep_var *= 2
            op_count += 2
        else:
            rep_var += copy_var
            op_count += 1
    return op_count
