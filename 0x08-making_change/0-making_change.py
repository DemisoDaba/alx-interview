#!/usr/bin/python3
"""0-making_change.py"""
import sys
def makeChange(coins, total):
    """
    MakeChange function
    """
    if total <= 0:
        return 0

    res = [sys.maxsize for i in range(total + 1)]
    res[0] = 0

    for i in coins:
        for j in range(i, total + 1):

            res[j] = min(res[j], res[j - i] + 1)

    if res[total] == sys.maxsize:
        return -1

    return res[total]
