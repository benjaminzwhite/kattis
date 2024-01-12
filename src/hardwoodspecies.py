# Hardwood Species
# https://open.kattis.com/problems/hardwoodspecies
# TAGS: basic
# CP4: 2.3h, Balanced BST (map)
# NOTES:
from sys import stdin
from collections import Counter

trees = [tree for tree in stdin]

c = Counter(trees)

for k, v in sorted(c.items()):
    print(f"{k} {100 * c[k] / len(trees)}")