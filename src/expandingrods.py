# Expanding Rods
# https://open.kattis.com/problems/expandingrods
# TAGS: mathematics, geometry, binary search
# CP4: 8.7a, BSTA+Other, Easier
# NOTES:
"""
Hard to explain with ASCII drawing:

Just draw the geometry and then binary search on the displacement such that the resultant radius of the circle
leads to the correct circular segment length `Lprime`.

---

"The input is such that the displacement of the center of any rod is at most one half of the original rod length."
-> set hi = L/2 in the binary search

(I got Run Time Error when I tried with L as the hi, I'm guessing because
there is a testcase where you'd be taking asin of something leading to 0's or whatever)
"""
from math import asin

while True:
    L, n, C = map(float, input().split())
    if L < 0:
        break       
    
    lo, hi = 0, L / 2

    Lprime = L + n * C * L

    half_L = L / 2

    for _ in range(100):
        displacement = (lo + hi) / 2

        radius = (displacement * displacement + half_L * half_L) / (2 * displacement)

        half_angle = asin(half_L / radius)

        guess_length = 2 * half_angle * radius
        if guess_length > Lprime:
            hi = displacement
        else:
            lo = displacement

    print(lo)