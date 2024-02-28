#!/usr/bin/python3
"""
0-making_change.py
"""


def makeChange(coins, total):
    """
    Args: coins (list), total (int)
    Returns: fewest coins needed (int)
    """

    if total <= 0:
        return 0

    number_coins = 0
    coins.sort(reverse=True)

    for coin in coins:
        while coin <= total:
            total -= coin
            number_coins += 1

    if total == 0:
        return number_coins
    return -1
