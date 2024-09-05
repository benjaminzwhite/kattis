# Jolly Jumpers
# https://open.kattis.com/problems/jollyjumpers
# TAGS: array
# CP4: 2.2a, 1D Array, Medium
# NOTES:
"""
Note: the n=1 edge case is expecting Jolly rather than Not jolly
"""
from sys import stdin

for line in stdin:
    n, *xs = map(int, line.split())

    seen = set()
    flg = True
    for a, b in zip(xs, xs[1:]):
        delta = abs(a - b)
        if delta == 0 or delta > n - 1 or delta in seen:
            print("Not jolly")
            flg = False
            break
        else:
            seen.add(delta)
    if flg:
        print("Jolly")