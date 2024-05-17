#!/usr/bin/python3
""" Prime game Module """

def isWinner(x, nums):
    """checks for the winner"""
    if not nums or x < 1:
        return None
    maximum_num = max(nums)

    num_filter = [True for _ in range(max(maximum_num + 1, 2))]
    for i in range(2, int(pow(maximum_num, 0.5)) + 1):
        if not num_filter[i]:
            continue
        for j in range(i * i, maximum_num + 1, i):
            num_filter[j] = False
    num_filter[0] = num_filter[1] = False
    y = 0
    for i in range(len(num_filter)):
        if num_filter[i]:
            y += 1
        num_filter[i] = y
    player1 = 0
    for x in nums:
        player1 += num_filter[x] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
