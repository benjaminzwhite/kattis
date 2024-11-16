# Room Painting
# https://open.kattis.com/problems/roompainting
# TAGS: binary search
# CP4: 3.3a, Binary Search
# NOTES:
"""
Basically binary search - need the next biggest paint can that is >= the target amount x; then sum the "excesses"
"""
from bisect import bisect_left

n, m = map(int, input().split())

paint_cans = []
for _ in range(n):
    paint_cans.append(int(input()))

paint_cans = sorted(paint_cans)
res = 0

for _ in range(m):
    x = int(input())
    i = bisect_left(paint_cans, x)
    res += paint_cans[i] - x
    
print(res)