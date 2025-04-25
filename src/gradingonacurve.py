# Grading on a Curve
# https://open.kattis.com/problems/gradingonacurve
# TAGS: binary search
# CP4: 0, Not In List Yet
# NOTES:
"""
Here is a binary search approach to solving - you can instead solve it analytically in a much smarter way that is fun to find.

Also there is a T variable that is made to seem important but which never gets used?
(Unless there's some intended smart way to use it, or just use it to fix the "hi" value of binary search?)
"""
N, T = map(int, input().split()) # T is unused in binary search??

scores = []
for _ in range(N):
	x = int(input())
	scores.append(x)

res = -1 # init res to -1; says there may be cases where no valid k exists -> IMPLEMENTATION: if so, binary search will never update res.

lo, hi = 1, 10**15 # hi value just set to a very large value
while lo < hi:
    mid = (lo + hi) // 2

    C, B, A = 0, 0, 0
    for score in scores:
        s = score * 100
        if s >= 70 * mid:
            C += 1
            if s >= 80 * mid:
                B += 1
                if s >= 90 * mid:
                    A += 1

    # A/N >= 1/4 [the "at least" in problem statement is INCLUSIVE afaict]
    # B/N >= 1/2
    # C/N >= 3/4
    # avoid floats by rearranging fractions
    if 4 * A >= N and 2 * B >= N and 4 * C >= 3 * N:
        lo = mid + 1
        res = mid
    else:
        hi = mid

print(res)