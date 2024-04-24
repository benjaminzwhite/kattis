# Cakey McCakeFace
# https://open.kattis.com/problems/cakeymccakeface
# TAGS: dict, brute force, improve
# CP4: 2.3h, Balanced BST (map)
# NOTES:
"""
TODO: IMPROVE: don't really understand this exercise/what it is testing because it's rated 4+ but basically just a brute force.
It has 4_000_000 (N=2000) data points and 4 sec timelimit but I didn't see a cleverer way to do it yet O_o

Maybe you are supposed to use the fact that both inputs are sorted so only search exits that are >= entries
"""
from collections import defaultdict

N = int(input())
M = int(input())

entries = list(map(int, input().split()))
exits = list(map(int, input().split()))

d = defaultdict(int)

for x in entries:
    for y in exits:
        if y < x:
            continue
        d[y - x] += 1

highest_freq = 0
res = 0
for k, v in d.items():
    if v > highest_freq:
        res = k
        highest_freq = v
    elif v == highest_freq:
        res = min(res, k)

print(res)