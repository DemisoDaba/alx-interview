#!/usr/bin/python3
"""0-making_change.py"""

def makeChange(coins, total):
    if total < 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0

    for coin in coins:
        if coin <= total:
            num_coins += total // coin
            total %= coin

    return num_coins if total == 0 else -1
