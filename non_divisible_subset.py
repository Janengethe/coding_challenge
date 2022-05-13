#!/usr/bin/env python3
"""
non divisible subset
"""
import re
from typing import List



def nonDivisibleSubset(k: int, s: List[int]) -> int:
    """Returns the non divisible subset from an array"""
    n = len(s)
    f = [0 for i in range(k)]
    for i in range(n):
        f[s[i] % k] += 1
    if (k % 2 == 0):
        f[k//2] = min(f[k//2], 1)
    res = min(f[0], 1)
    for i in range(1,(k // 2) + 1):
        res += max(f[i], f[k - i])
 
    return res

if __name__ == '__main__':
    k = 3
    s = [1, 2, 3, 4, 5, 6]
    print(nonDivisibleSubset(k, s))