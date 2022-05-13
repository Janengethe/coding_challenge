#!/usr/bin/env python3
"""
diagonal difference
"""


def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    d1 = sum([arr[x][x] for x in range(len(arr))])
    d2 = sum([arr[x][n - 1 - x] for x in range(len(arr))])
    return(abs(d1 - d2))


if __name__ == '__main__':
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]
    print(diagonalDifference(arr))