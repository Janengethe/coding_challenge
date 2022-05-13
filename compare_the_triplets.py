#!/usr/bin/env python3
"""
The function is expected to return an INTEGER_ARRAY.
The function accepts following parameters:
1. INTEGER_ARRAY a
2. INTEGER_ARRAY b
"""


def compareTriplets(a: list, b: list) -> list:
    """returns a list of the difference in arrays"""
    pointa=0
    pointb=0
    ar = []
    for i in range(3):
        if a[i]>b[i]:
            pointa+=1
            
        if a[i]<b[i]:
            pointb+=1
    ar.insert(0,pointa)
    ar.insert(1,pointb)        
    return(ar)

if __name__ == '__main__':
    ar = [3, 4, 5]
    arr = [8, 1, 3]
    print(compareTriplets(ar, arr))