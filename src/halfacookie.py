# Half a Cookie
# https://open.kattis.com/problems/halfacookie
# TAGS: mathematics, geometry
# CP4: 7.2c, Circles
# NOTES:
"""
Can simplify a lot and avoid floating point comparisons, but below is based on the pen and paper approach.
"""
import sys

from math import sin, acos, sqrt, pi

for line in sys.stdin:
    r, x, y = map(float, line.split())

    h = sqrt(x * x + y * y)

    if h >= r:
        print("miss")

    else:
        # theta is opening angle to form the chord
        theta = 2 * acos(h / r)

        # total area is made up of 2 components: 
        # 1/ area of the triangle of height h and basewidth = w = 2*r*sin(theta/2)
        #    -> simplifies to 1/2 * h * w = h * r * sin(theta/2)
        triangle_area = h * r * sin(theta / 2)

        # 2/ area of the "big pie" formed by the complement angle to theta
        #    -> theta is opening angle, use the complement to get area of the pie-shaped part 
        complementary_angle = 2 * pi - theta

        pie_area = (complementary_angle / (2 * pi)) * pi * r * r

        first_piece = triangle_area + pie_area
        second_piece = pi * r * r - first_piece

        # wants largest first so say first_piece is largest WLOG
        if second_piece > first_piece:
            first_piece, second_piece = second_piece, first_piece
        print(first_piece, second_piece)
