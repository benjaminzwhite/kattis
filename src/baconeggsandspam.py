# Bacon, Eggs, and Spam
# https://open.kattis.com/problems/baconeggsandspam
# TAGS: dict
# CP4: 2.3h, Balanced BST (map)
# NOTES:
from collections import defaultdict

while True:
    n = int(input())
    if n == 0:
        break
    d = defaultdict(set)
    for _ in range(n):
        name, *stuff = input().split()
        for k in stuff:
            d[k].add(name)

    for k in sorted(d):
        print(k, *sorted(d[k]))
    print()