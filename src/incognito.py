# Incognito
# https://open.kattis.com/problems/incognito
# TAGS: mathematics, combinatorics
# CP4: 5.4e, Others, Harder
# NOTES:
"""
Just apply the product rule from combinatorics.

The final result gets -1 because we can't have the option corresponding to where we pick NO items from ALL categories.
"""
from collections import defaultdict

T = int(input())

for _ in range(T):
    n = int(input())
    d = defaultdict(set)
    for _ in range(n):
        x, category = input().split()
        d[category].add(x)

    res = 1
    for v in d.values():
        res *= len(v) + 1

    print(res - 1) # -1 because we can't have the option corresponding to where we pick NO items from ALL categories.