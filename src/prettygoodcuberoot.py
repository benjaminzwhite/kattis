# Pretty Good Cube Root
# https://open.kattis.com/problems/prettygoodcuberoot
# TAGS: binary search
# CP4: 8.7a, BSTA+Other, Easier
# NOTES:
import sys

for l in sys.stdin:
    n = int(l)
    
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi) // 2
        if mid ** 3 > n:
            hi = mid
        else:
            lo = mid + 1
    
    res = min(lo, lo - 1, key = lambda x: abs(n - x ** 3))

    print(res)