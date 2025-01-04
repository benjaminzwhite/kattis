# Pie
# https://open.kattis.com/problems/pie
# TAGS: binary search
# CP4: 8.7a, BSTA+Other, Easier
# NOTES:
"""
Standard binary search; but careful: you need to compare pieces >= F+1 since there are F friends, plus you, so F+1 people
"""
from math import pi, floor

T = int(input())
for _ in range(T):
    N, F = map(int, input().split())

    pies = list(map(int, input().split()))

    lo = 0
    hi = 1e9
    EPS = 1e-6
    while hi - lo > EPS:
        mid = (hi + lo) / 2

        pieces = 0

        for radius in pies:
            vol = pi * radius * radius
            poss_pieces = floor(vol / mid)
            pieces += poss_pieces

        if pieces >= (F + 1):
            lo = mid
        else:
            hi = mid

    print(lo)