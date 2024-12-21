# Goofy Geometry
# https://open.kattis.com/problems/goofy
# TAGS: mathematics, geometry
# CP4: 0, Not In List Yet
# NOTES:
"""
Just formula/geometry - testcases that are misleading: all are ints but real tests use floats

I used: https://en.wikipedia.org/wiki/Tangent_lines_to_circles#With_analytic_geometry

CARE! Implementation note:
Formula involves dividing by (x0 - curr_x) so have to handle division by 0 case.
This corresponds to vertical line through the 2 points:
x = constant ie. ax+by=c -> b==0, a==1, c==x0 to give: x=x0
"""
N = int(input())
for _ in range(N):
    x0, y0 = map(float, input().split())

    dsq = x0 * x0 + y0 * y0

    x1 = x0 / dsq + (((dsq - 1)**0.5) / (dsq)) * (-y0)
    y1 = y0 / dsq + (((dsq - 1)**0.5) / (dsq)) * (x0)

    x2 = x0 / dsq - (((dsq - 1)**0.5) / (dsq)) * (-y0)
    y2 = y0 / dsq - (((dsq - 1)**0.5) / (dsq)) * (x0)

    b1, b2 = 1, 1
    # first line:
    if x0 == x1:
        b1 = 0
        m1 = -1
        c1 = x0
    else:
        m1 = (y0 - y1) / (x0 - x1)
        c1 = y0 - m1 * x0

    # second line:
    if x0 == x2:
        b2 = 0
        m2 = -1
        c2 = x0
    else:
        m2 = (y0 - y2) / (x0 - x2)
        c2 = y0 - m2 * x0

    #res = (-m1,b1,c1,-m2,b2,c2) # -m to correspond to his format of the eqn a*x + b*y = c -> I currently have y = mx +c so -mx+y=c --> a == -m, b == 1, c == c
    print("({},{},{},{},{},{})".format(-m1, b1, c1, -m2, b2, c2))