#!/usr/bin/python3
"""
0-making_change.py
"""


def makeChange(coins, amount):
    if amount == 0:
        return 0
    amounts = [float("inf")] * (amount + 1)
    amounts[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            amounts[i] = min(amounts[i], amounts[i - coin] + 1)
    if amounts[amount] != float("inf"):
        return amounts[amount]
    else:
        return -1
