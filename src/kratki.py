# Kratki
# https://open.kattis.com/problems/kratki
# TAGS: mathematics, combinatorics, proof
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/kratki.md
"""
from math import sqrt 

N, K = map(int, input().split())

if K < sqrt(N):
    print(-1)
else:
    res = []
    for i in range(N // K + 1):
        res.extend(range(min(N, (i + 1) * K), i * K, -1))
    print(*res)