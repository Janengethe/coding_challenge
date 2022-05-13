#!/usr/bin/env python3
"""
Given an array of integers, find the sum of its elements.
For example, if the array arr = [1,2,3], 1+2+3 = 6 , so return 6.
"""


def simpleArraySum(ar: list) -> int:
    """returns the sum of the array elements as an integer"""
    return sum(ar)

if __name__ == '__main__':
    ar = [3, 4, 5]
    print(simpleArraySum(ar))