# Course Scheduling
# https://open.kattis.com/problems/coursescheduling
# TAGS: dict
# CP4: 2.3g, Balanced BST (set)
# NOTES:
from collections import defaultdict

n = int(input())

d = defaultdict(set)

for _ in range(n):
    fst, snd, course = input().split()
    d[course].add((fst, snd))

for k, v in sorted(d.items()):
    print(k, len(v))