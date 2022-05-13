#!/usr/bin/env python3
"""
time in words
"""
from math import floor, ceil
from math import sqrt



def timeInWords(h: int, m: int) -> str:
    """Returns time in words"""
    n = [
        "zero", 
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "quarter",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "twenty one",
        "twenty two",
        "twenty three",
        "twenty four",
        "twenty five",
        "twenty six",
        "twenty seven",
        "twenty eight",
        "twenty nine",
        "half"
    ]
    m = int(m)
    h = int(h)
    if not m:
        return "%s o' clock" % n[h]
    if m>30: 
        m = 60 - m
        w = "to"
        h = (h+1)%12 or 12
    else:
        w = "past"
    o = " minutes"
    if m==1:
        o = " minute"
    elif not m%15:
        o = ""
    m = n[m]
    h = n[h]
    
    return "%s%s %s %s"%(m,o,w,h)

if __name__ == '__main__':
    h = 10
    m = 13
    print(timeInWords(h, m))