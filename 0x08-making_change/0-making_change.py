#!/usr/bin/python3
""" Fewest coins for change"""


def makeChange(coins, total):
    """ fewest number of coins to meet total """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    change = 0

    for coin in coins:
        if total <= 0:
            break
        remainder = total // coin
        change += remainder
        total -= (remainder * coin)

    if total != 0:
        return -1
    return change
