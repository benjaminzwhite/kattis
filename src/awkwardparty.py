# Awkward Party
# https://open.kattis.com/problems/awkwardparty
# TAGS: dict
# CP4: 2.3f, Hash Table (map), H
# NOTES:
n = int(input())

xs = map(int, input().split())

d = {}
res = n
for i, x in enumerate(xs):
    if x in d:
        res = min(res, i - d[x])
    d[x] = i

print(res)