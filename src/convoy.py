# Convoy
# https://open.kattis.com/problems/convoy
# TAGS: binary search, improve
# CP4: 0, Not In List Yet
# NOTES:
"""
TODO: IMPROVE: solved with binary search but it feels like there might be an analytic solution

---

Implementation notes:

For the part in the binary search "for x is xs[:k]" note that Python gracefully handles case where k > n.
Otherwise would have to take K = min(k, n) for any other approach/language.
"""
n, k = map(int, input().split())

xs = []
for _ in range(n):
    xs.append(int(input()))

xs = sorted(xs)

lo, hi = 1, 20_000 * 1_000_000 + 10 # log2(hi) is 35
while lo < hi:
    mid = (lo + hi) // 2

    passengers_moved = 0
    for x in xs[:k]: # use the k fastest drivers where k is num cars
        if x > mid: # if time taken by this driver to make 1 single trip is > total time allowed, skip it. Since xs sorted, then all subsequent are >= x also, so can skip rest also.
            break
        passengers_moved += 5 + 4 * ((mid - x) // (2 * x)) # first trip "moves" the driver and 4 passengers i.e. 5 people. Then any remaining time i.e. (mid - x) can be used to move 4 additional NEW people, which takes a time interval of 2*x each

    if passengers_moved >= n:
        hi = mid
    else:
        lo = mid + 1

print(lo)