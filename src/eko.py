# Eko
# https://open.kattis.com/problems/eko
# TAGS: array, sorting
# CP4: 8.7j, Other+DP 1D RSQ/RMQ
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/eko.md
"""
from math import ceil

N, needed = map(int, input().split())

xs = map(int, input().split())

xs = sorted(xs, reverse=True)
xs.append(-float("inf")) # dummy element to trigger processing of last real element in array

cnt = 0 # cnt number of "left" trees processed when iterating over left, right pairs (note: can do with enumerate(...) but this is clearer)
res = xs[0]
for l, r in zip(xs, xs[1:]):
    cnt += 1
    if (l - r) * cnt <= needed:
        needed -= (l - r) * cnt
        res = r
    else:
        res = l - ceil(needed / cnt) # reduce the height just enough so that leftover needed amount is taken care of
        break

print(res)