# Shopping List
# https://open.kattis.com/problems/shoppinglist
# TAGS: dict, reduce
# CP4: 2.3d, Hash Table (set)
# NOTES:
"""
Did some FUNctional programming for fun O_o
"""
from functools import reduce

n, m = map(int, input().split())

xs = []
for _ in range(n):
    xs.append(input())

res = reduce(lambda acc, x: acc.intersection(x), map(lambda x: set(x.split()), xs))

print(len(res))
for r in sorted(res):
    print(r)