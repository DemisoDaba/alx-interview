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

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    makeChange = __import__('0-making_change').makeChange

    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
