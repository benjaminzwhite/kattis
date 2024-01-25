# Speeding
# https://open.kattis.com/problems/speeding
# TAGS: basic
# CP4: 1.4e, Control Flow
# NOTES:
"""
Initialize "previous" values of T,D to e.g. -1, 0:
-1 is so that we avoid 0 division error on first "real" input which is always 0, 0
"""
n = int(input())

T, D = -1, 0
res = 0
for _ in range(n):
    t, d = map(int, input().split())
    res = max(res, (d - D) // (t - T))
    T, D = t, d

print(res)