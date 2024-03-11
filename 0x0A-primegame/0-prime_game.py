#!/usr/bin/python3
"""
Module for a function called isWinner
"""


def isPrime(n):
    """
        @params:
            n: number to be checked
        Returns: a boolean indicating whether the number is prime or not
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    if n == 1 or n == 0:
        return False
    return True


def isWinner(x, nums):
    """
        @params:
            x: number of rounds
            nums: list of numbers
        Returns:
            The winner between Maria and Ben
    """

    mariaPoints = 0
    benPoints = 0
    previous = []

    if type(x) != int or type(nums) != list:
        return None
    if x > len(nums) or len(nums) > x or not nums:
        return None
    if any([type(x) != int for x in nums]):
        return None

    for round in range(0, x):
        moves = 0
        while True:
            sets = [x for x in range(1, nums[round] + 1) if x not in previous]
            if not any([isPrime(x) for x in sets]):
                previous = []
                if moves == 0 or moves % 2 == 0:
                    benPoints += 1
                else:
                    mariaPoints += 1
                break
            if any([isPrime(x) for x in sets]):
                n = next(x for x in sets if isPrime(x))
                previous.append(n)
                previous.extend([x for x in sets if x % n == 0 and x != n])
                moves += 1
    if benPoints == 0 and mariaPoints == 0:
        return 'Ben'
    elif benPoints > mariaPoints:
        return 'Ben'
    elif mariaPoints > benPoints:
        return 'Maria'
    return None
