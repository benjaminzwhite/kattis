# Greedy Polygons
# https://open.kattis.com/problems/greedypolygons
# TAGS: geometry
# CP4: 7.2e, Triangles + Circles
# NOTES:
"""
https://en.wikipedia.org/wiki/Regular_polygon#Area
Using the expression: 1/4 * n * l**2 * cotan(pi / n), since we have n and l already.

---

Explanation of added_area:

You add n copies of a rectangle of size l * d, times * g for g "grabs", 
then the rounded bits add up to 1 full circle of area pi d**2, again * g for g grabs
"""
from math import pi, tan

N = int(input())

for _ in range(N):
    n, l, d, g = map(int, input().split())
    
    original_area = 0.25 * n * l * l / tan(pi / n)
    
    added_area = (n * l * d * g) + (pi * g * g * d * d)

    print(original_area + added_area)