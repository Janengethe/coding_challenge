#!/usr/bin/env python3
"""
encryption
"""
from math import floor, ceil
from math import sqrt



def get_grid(number: int) -> tuple:
    """get grid"""
    root = sqrt(number)
    
    x = int(root//1)
    y = ceil(root)
    
    while x*y < number:
        if x <= y:
            x += 1
        else:
            y += 1
        
    return (x, y)

def encryption(string: str) -> str:
    """
    The function is expected to return a STRING.
    The function accepts STRING s as parameter.
    """
    string = string.strip().replace(' ', '')
    str_len = len(string)
    
    x, y = get_grid(str_len)
    grid = [ [ '' for i in range(x) ] for _j in range(y) ]
    
    count = 0
    x_ind = 0
    y_ind = 0
    for ind in range(str_len):
        if count / y == 1 and count % y == 0:
            count = 0
            y_ind += 1
            x_ind = 0
            
        grid[x_ind][y_ind] = string[ind]
        count += 1
        x_ind += 1
        
    
    out = ''
    for _i in range(y):
        for _j in range(x):
            out += grid[_i][_j]
        out += ' '
    return out

if __name__ == '__main__':
    string = "My name is None"
    print(encryption(string))