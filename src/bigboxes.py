# Big Boxes
# https://open.kattis.com/problems/bigboxes
# TAGS: binary search, greedy
# CP4: 8.7a, BSTA+Other, Easier
# NOTES:
"""
Binary search - guess a value for the min weight of all boxes, then for each such guess (variable:'mid' in the below binary search)
you greedily move left to right through xs, trying to pack k boxes each up to max_weight = mid

If you can fit all the xs values into <= k boxes of max_weight = mid, then binary search again with mid as UPPER RANGE,
if not then the check_condition is invalid so move mid as LOWER RANGE

---

Implementation notes:

I thought that you might need to be clever about re-calculating this over and over and use a 1d range sum approach
(i.e. accumulate the x's once and use left/right ranges) but my Python solution runs in < .1 secs so no problem for these testcases
"""
n, k = map(int, input().split())
xs = list(map(int, input().split()))

def check(xs, k, target):
    # TODO: improve to range sum approach if TLE
    curr_sum = 0
    boxes_used = 1
    for x in xs:
        if (tmp := curr_sum + x) <= target:
            curr_sum = tmp
        elif x > target:
            return False
        else:
            boxes_used += 1
            if boxes_used > k:
                return False
            curr_sum = x
    
    return boxes_used <= k

lo, hi = 1, n * (10**4) + 10
while lo < hi:
    mid = (lo + hi) // 2

    if check(xs, k, mid):
        hi = mid
    else:
        lo = mid + 1

print(lo)