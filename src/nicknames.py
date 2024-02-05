# Nicknames
# https://open.kattis.com/problems/nicknames
# TAGS: improve
# CP4: 2.3e, Hash Table (map), E
# NOTES:
"""
TODO: IMPROVE

Not happy with my solution - it's brute force and takes 0.9s (1.0s is TLE).

Probably can get faster using fast input methods, but still want to return and find a better approach.
"""
from collections import defaultdict

d = defaultdict(int)

A = int(input())
for _ in range(A):
    s = input()
    for i in range(1, len(s) + 1):
        d[s[:i]] += 1

B = int(input())
for _ in range(B):
    t = input()
    print(d[t])