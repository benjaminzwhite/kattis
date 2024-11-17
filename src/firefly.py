# Firefly
# https://open.kattis.com/problems/firefly
# TAGS: binary search
# CP4: 3.3a, Binary Search
# NOTES:
"""
For a given height, you will hit a given set of mites+tites REGARDLESS OF THEIR ORIGINAL ORDER, so sort them
then find how many are >= each height value from 1 to H by doing binary search for that height.

The index of where height fits into the sorted list will tell you how many are < height and how many are >= height
"""
from bisect import bisect_left

N, H = map(int, input().split())

mites, tites = [], []

for i in range(N):
    if i % 2 == 0:
        mites.append(int(input()))
    else:
        tites.append(int(input()))

mites = sorted(mites)
tites = sorted(tites)

min_collisions = float('inf')
cnt = 0

for h in range(1, H + 1):
    i_m = bisect_left(mites, h)
    i_t = bisect_left(tites, H - h + 1)
    curr_collisions = (len(mites) - i_m) + (len(tites) - i_t) 
    
    if curr_collisions < min_collisions:
        min_collisions = curr_collisions
        cnt = 1
    elif curr_collisions == min_collisions:
        cnt += 1

print(min_collisions, cnt)