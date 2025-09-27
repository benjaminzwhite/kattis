# Reconnaissance
# https://open.kattis.com/problems/reconnaissance
# TAGS: ternary search
# CP4: 3.3c, Ternary Search & Others
# NOTES:
"""
Still not super clear on how to fix the starting values of hi/lo, and also the number
of iterations to perform the "ternary range reduction". Here I found 100 works to get AC
but I need to re-read how to fix this programatically if there is a best practice.
"""
n = int(input())

xs = []
for _ in range(n):
    pos, vel = map(int, input().split())
    xs.append((pos, vel))

def leftmost_position(xs, time_t):
    res = float('inf')
    for pos, vel in xs:
        # x = x0 + v*t
        res = min(res, pos + vel * time_t)
    return res

def rightmost_position(xs, time_t):
    res = -float('inf')
    for pos, vel in xs:
        # x = x0 + v*t
        res = max(res, pos + vel * time_t)
    return res

# TODO: how to fix the "hi" and the "num_iterations" programatically?
lo = 0 # we start at t=0 and can only go "forward" in time, this is fixed by problem statement
hi = 9e9 # here I'm not sure what to put based on problem statement? I just picked a big value

# here for num_iterations I picked 100 but TODO: what is the best practice to find this value
for _ in range(100):
    delta = (hi - lo) / 3
    t1 = lo + delta
    t2 = hi - delta

    range_at_t1 = rightmost_position(xs, t1) - leftmost_position(xs, t1)
    range_at_t2 = rightmost_position(xs, t2) - leftmost_position(xs, t2)

    if range_at_t1 < range_at_t2:
        hi = t2
    else:
        lo = t1

print(range_at_t1)