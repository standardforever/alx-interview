#!/usr/bin/python3
"""Interview question"""


def minOperations(n):
    """find total num of operarion performed"""
    if not isinstance(n, int) or n <= 1:
        return 0
    num = 1
    count = 0
    dup = 0
    while (num < n):
        if (n % num != 0):
            num += dup
            count += 1
        else:
            dup = num
            num += dup
            count += 2
    if num == n:
        return (count)
    return 0
