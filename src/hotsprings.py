# Hot Springs
# https://open.kattis.com/problems/hotsprings
# TAGS: greedy, sorting
# CP4: 3.4b, Involving Sorting, E
# NOTES:
"""
Slight confusion in problem statement:

In statement it says temperature differences must be INCREASING but in
reality it wants NON-DECREASING (see the <= symbol in the equation given)

SO e.g. 7 7 7 7 IS a valid answer.

---

Solution is to place alternating largest/smallest in a zig zag - the difference between peaks
and valleys is then non-decreasing.

If you prove this to yourself, I think therefore THERE IS NEVER AN "impossible" - you
can always use this greedy algorithm; so the check below for the "impossibe" is not needed.
"""
n = int(input())
xs = sorted(map(int, input().split()))

res = []
l, r = 0, len(xs) - 1
while l <= r:
    res.append(xs[r])
    if l != r:
        res.append(xs[l])
    l += 1
    r -= 1
res = res[::-1]

# I think you can delete this check step
flg = True
prev_diff = -1
for a, b in zip(res, res[1:]):
    d = abs(b - a)
    if d < prev_diff:
        flg = False
        break
    prev_diff = d

if flg:
    print(*res)
else:
    print("impossible")