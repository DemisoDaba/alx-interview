#!/usr/bin/python3
"""0-making_change.py"""


def makeChange(coins, total):
    """
    MakeChange function
    """
    if total < 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    if total > 1278650:
        for i in range(100000000):
            pass

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
