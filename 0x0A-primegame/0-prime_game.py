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
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primeCountInRange(n):
    """
    Computes the number of prime numbers in the given range n

    Return: Number of prime number's between 1 and n
    """
    primeCount = 0
    for i in range(2, n + 1):
        if isPrime(i):
            primeCount += 1
    return primeCount


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
    if x != len(nums) or not nums:
        return None
    if any([type(x) != int for x in nums]):
        return None

    for round in range(x):
        if nums[round] <= 0:
            return None
        if primeCountInRange(nums[round]) % 2 == 0:
            benPoints += 1
        else:
            mariaPoints += 1

    if benPoints == 0 and mariaPoints == 0:
        return 'Ben'
    elif benPoints > mariaPoints:
        return 'Ben'
    elif mariaPoints > benPoints:
        return 'Maria'
    return None
