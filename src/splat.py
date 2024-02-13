# Splat
# https://open.kattis.com/problems/splat
# TAGS: geometry, brute force
# CP4: 8.7e, Geometry+CS
# NOTES:
"""
Small input size so "inefficient" approach:
For each query, loop through the entire series of drops in chronological order.
For each drop that "affects" the query point x_,y_, you update the color of the queried point.

---

Implementation note:

The input drops data is given by a VOLUME of paint which spreads to a circle such that
V = pi * r*r so that's how you get the r for each drop - i just get r**2 instead of taking sqrt
and compare that each query point is within dx**2 +dy**2 <= r**2
"""
from math import pi

T = int(input())

for _ in range(T):
    n = int(input())
    drops = []
    for _ in range(n):
        x, y, v, c = input().split()
        rr = float(v) / pi # store r**2 to avoid taking sqrt - will compare to dx**2 + dy**2 directly
        drops.append((float(x), float(y), rr, c))

    m = int(input())
    for _ in range(m):
        color = "white" # SET DEFAULT TO WHITE - if our point has not been covered by any paint will be white
        x_, y_ = map(float, input().split())
        for x, y, rr, c in drops:
            if (x - x_)**2 + (y - y_)**2 <= rr:
                color = c
        print(color)