# Prinova
# https://open.kattis.com/problems/prinova
# TAGS: array, sorting
# CP4: 3.2g, Try All Answers
# NOTES:
"""
N is small but the values are large so can't just try entire range (l, r)

So, try to guess the middle range of (l, r) UNLESS THAT VALUE IS UNAVAILABLE DUE TO BEING < A or > B
in which case, update it to be A or B (accordingly) and then compute the curr_distance with this value

---

Note: left stuff like A % 2 == 0 to be clear about what it being checked; can simplify code a lot.
"""
N = int(input())
xs = sorted(map(int, input().split()))
A, B = map(int, input().split())

# set A,B to be odd from now on, avoids checking repeatedly later
if A % 2 == 0:
	A += 1
if B % 2 == 0:
	B -= 1

res = None
best = 0
for l, r in zip(xs, xs[1:]):
    mid = (l + r) // 2
    if mid % 2 == 0:
        mid += 1
    if (A <= mid <= B):
        curr_dist = r - mid
    elif mid > B:
        curr_dist = B - l
        mid = B
    else:
        curr_dist = r - A
        mid = A
    if curr_dist > best:
        best = curr_dist
        res = mid

if A < xs[0]:
    dist = xs[0] - A
    if dist > best:
        best = dist
        res = A

if B > xs[-1]:
    dist = B - xs[-1]
    if dist > best:
        best = dist
        res = B

print(res)