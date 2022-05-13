#!/usr/bin/env python3
"""
the grid search
"""
import re



def gridSearch(G: str, P: str) -> str:
    l = len(P)
    m = len(P[0])
    for x,y in enumerate(G):
        for i in ((m.start(0)) for m in re.finditer("(?=%s)"%P[0], y)):
            for a in range(1,l):
                if G[a+x][i:i+m]!=P[a]:
                    break
            else:
                return "YES"
      
    return "NO"

if __name__ == '__main__':
    g = "876543"
    p = "65"
    h = "11"
    print(gridSearch(g, p))
    print(gridSearch(g, h))