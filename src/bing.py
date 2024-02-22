# Bing It On
# https://open.kattis.com/problems/bing
# TAGS: dict, trie, improve
# CP4: 8.7c, Fast DS+Other, Easier
# NOTES:
"""
TODO: IMPROVE

Here I just make a big defaultdict of the frequencies of all possible prefixes.
Revisit this using a Trie for practice.
"""
from collections import defaultdict

d = defaultdict(int)

N = int(input())

for _ in range(N):
    l = input()
    res = d[l]
    print(res)
    for i in range(len(l) + 1):
        d[l[:i]] += 1