# Triangle Drama
# https://open.kattis.com/problems/triangledrama
# TAGS: brute force
# CP4: 3.2c, Three+ Nested Loops, E
# NOTES:
"""
Be careful with 1 based indexing at the output O_o
"""
from itertools import combinations

N = int(input())

xs = []
for _ in range(N):
    xs.append(list(map(int, input().split())))

best = -1
res = []
for i, j, k in combinations(range(N), 3):
    drama = xs[i][j] * xs[j][k] * xs[k][i]
    if drama > best:
        res = [(i, j, k)]
        best = drama
    elif drama == best:
        res.append((i, j, k))

res = sorted(res) # in tie break it wants smallest i then j then k so sorted order basically

print(*(x + 1 for x in res[0])) # it wants 1 based indexing