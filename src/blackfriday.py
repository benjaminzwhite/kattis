# Black Friday
# https://open.kattis.com/problems/blackfriday
# TAGS: array
# CP4: 3.2b, Iterative (Two Loops)
# NOTES:
from collections import Counter

n = int(input())

xs = list(map(int, input().split()))

c = Counter(xs)

winner = max((k for k, v in c.items() if v == 1), default=None)

if winner is None:
    print("none")
else:
    print(1 + xs.index(winner)) # 1 based indexing 