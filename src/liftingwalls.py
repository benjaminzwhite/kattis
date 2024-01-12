# Lifting Walls
# https://open.kattis.com/problems/walls
# TAGS: brute force
# CP4: 3.2g, Try All Answers
# NOTES:
"""
- linked on p152 of Sannemo PDF - Section on Brute Force

---

I got Time Limit Exceeded on first submission (on final test case) using naive brute force.

I figured it might require reducing the number of combinations tried, so I filter the cranes in the inputs:

Rather than include all of them (e.g. up to n=30) I pre-screen them during the input phase, by checking
that the crane HAS AT LEAST ONE OF THE 4 CENTRE POINTS WITHIN ITS RANGE - otherwise it is useless and will
never be part of any valid solution, but will combinatorially explode the number of combos to check.

This simple change passed the TLE to AC.
"""
from itertools import combinations

def is_within_radius(point, crane, radius):
    xp, yp = point
    xc, yc = crane
    return (xp - xc)**2 + (yp - yc)**2 <= radius**2

l, w, n, radius = map(int, input().split())

CENTRES = [(0, w/2), (0, -w/2), (l/2, 0), (-l/2, 0)]

cranes = []
for _ in range(n):
    x, y = map(int, input().split())
    crane = (x, y)
    if any(is_within_radius(centre, crane, radius) for centre in CENTRES):
        cranes.append((x, y))

found = False
# Iterate from 1,2... n so that once you find a valid solution, it is guaranteed to
# have the minimum possible number of cranes used.
for num_cranes in range(1, n+1):
    for crane_combo in combinations(cranes, num_cranes):
        flg = True
        for centre in CENTRES:
            if not any(is_within_radius(centre, crane, radius) for crane in crane_combo):
                flg = False
                break
        if flg:
            print(num_cranes)
            found = True
            break
    if found:
        break

if not found:
    print("Impossible")