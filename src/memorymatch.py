# Memory Match
# https://open.kattis.com/problems/memorymatch
# TAGS: dict
# CP4: 1.6a, Game (Card)
# NOTES:
"""
n.b. the last extra condition: elif (len(avail_indices) == 2 and unpaired == 0):

If you have 2 unused indices at the end, and 0 unpaired cards leftover, then the 2 unused indices must be 2 cards of the same type
so in this edge case, you can guess 1 more pair (the pair hiding behind these 2 unused indices is the last remaining pair in the game)
"""
from collections import defaultdict

N = int(input())
K = int(input())

d = defaultdict(set)
avail_indices = set(map(str, range(1, N + 1)))

for _ in range(K):
    i, j, c1, c2 = input().split()
    avail_indices.discard(i)
    avail_indices.discard(j)
    if c1 == c2:
        if c1 in d:
            del d[c1]
    else:
        d[c1].add(i)
        d[c2].add(j)

paired, unpaired = 0, 0
for k, v in d.items():
    if len(v) == 2:
        paired += 1
    elif len(v) == 1:
        unpaired += 1

res = paired
if (len(avail_indices) == unpaired):
    res += unpaired
elif (len(avail_indices) == 2 and unpaired == 0):
    res += 1

print(res)