#!/usr/bin/env python3
"""
Swaps container with ball of same type
"""


from typing import List


def organizingContainers(container: List[list]) -> str:
    """
    The function is expected to return a STRING.
    the function accepts 2D_INTEGER_ARRAY container as parameter.
    """
    caps = []
    for i in range(len(container)):
        caps.append( sum(container[i]) )
    #print(caps)

    typenums = []
    for i in range(len(container)):
        n = 0
        for j in range(len(container)):
            n += container[j][i]
        typenums.append(n)
    
    if sorted(caps) == sorted(typenums):
        return 'Possible'
    else:
        return 'Impossible'

if __name__ == '__main__':
    container = [[3, 2], [2, 3]]
    containe_r = [[1, 4], [2, 3]]
    print(organizingContainers(container))
    print(organizingContainers(containe_r))