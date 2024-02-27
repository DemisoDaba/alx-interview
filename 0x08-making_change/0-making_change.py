#!/usr/bin/python3
"""0-making_change.py"""
import math
def makeChange(coins, total):
    """
    MakeChange function
    """
    n = 0
    coins.sort(reverse=True)
    if total < 0:
        return 0

    for coin in coins:
        if total % coin <= total:
            n += math.trunc(total / coin)
            total %= coin

    if total == 0:
        return n

    return -1
