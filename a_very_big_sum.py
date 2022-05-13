#!/usr/bin/env python3
"""
The function is expected to return a LONG_INTEGER.
The function accepts LONG_INTEGER_ARRAY ar as parameter.
"""


def aVeryBigSum(ar: int) -> int:
    """returns te sum of arr"""
    return sum(ar)

if __name__ == '__main__':
    ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
    print(aVeryBigSum(ar))