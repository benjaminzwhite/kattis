# Costume Contest
# https://open.kattis.com/problems/costumecontest
# TAGS: array
# CP4: 2.3e, Hash Table (map), E
# NOTES:
from collections import Counter

n = int(input())

xs = [input() for _ in range(n)]

c = Counter(xs)
best = min(c.values())
res = sorted(x for x in set(xs) if c[x] == best)

for x in res:
    print(x)