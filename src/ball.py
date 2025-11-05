# Ball
# https://open.kattis.com/problems/ball
# TAGS: logic, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
Output needs to be sorted, so make sure you convert to int rather than sorting as strings (gives WA).
"""
from collections import defaultdict

n = int(input())

d = defaultdict(int)

xs = []
for _ in range(n // 2 + 1):
    a, b = input().split()
    d[a] += 1
    d[b] += 1
    xs.append((a, b))

for a, b in xs:
    if d[a] == 2 and d[b] == 2:
        print(*sorted(map(int, [a, b])))
        break