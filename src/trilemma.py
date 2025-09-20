# Triangle Trilemma
# https://open.kattis.com/problems/trilemma
# TAGS: mathematics, geometry
# CP4: 7.2e, Triangles + Circles
# NOTES:
"""
Mainly input/output stuff. 

Just using EPS for comparison since might be testcases close to e.g. 90 degrees etc.

Use law of cosines to get the angles f, g, h of the triangle also.
"""
from math import acos, pi

EPS = 1e-6

# distance
def D(x, y, X, Y):
	return abs(x - X + (y - Y) * 1j)

# angles
def A(a, b, c):
	return acos((b * b + c * c - a * a) / (2 * b * c))

# --- Queries ---
N = int(input())
for testcase in range(1, N + 1):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())

    a = D(x1, y1, x2, y2)
    b = D(x1, y1, x3, y3)
    c = D(x2, y2, x3, y3)

    a, b, c = sorted([a, b, c])

    if a < EPS or a + b < c + EPS:
        print(f"Case #{testcase}: not a triangle")
    else:
        f = A(a, b, c)
        g = A(b, a, c)
        h = A(c, a, b)

        f, g, h = sorted([f, g, h])

        angle = "right"
        if 2 * h > pi + EPS:
            angle = "obtuse"
        if 2 * h < pi - EPS:
            angle = "acute"

        categ = "scalene"
        if abs(a - b) < EPS or abs(b - c) < EPS:
            categ = "isosceles"

        print(f"Case #{testcase}: {categ} {angle} triangle")