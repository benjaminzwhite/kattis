# Ocean Monument
# https://open.kattis.com/problems/oceanmonument
# TAGS: mathematics, combinatorics, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/oceanmonument.md
"""
from math import comb

T = int(input())

for _ in range(T):
    g, e = map(int,input().split())

    if e == 0:
        print(1)
    elif g == 0:
        print(comb(2 * (e - 1), (e - 1)) // ((e - 1) + 1))
    else:
        # using capital letters to match the variables in the notes O_o
        E = e
        G = e + g - 1
        
        ALLS = comb(E + G, G)
        BADS = comb(E + G, G - g)
        
        print(ALLS - BADS)