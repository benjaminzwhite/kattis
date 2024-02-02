# Ornaments
# https://open.kattis.com/problems/ornaments
# TAGS: mathematics, geometry
# CP4: 7.2c, Circles
# NOTES:
"""
No ASCII drawing, I'll call:
- A the attachment point,
- C the centre of circle,
- T the tangent point on the circle of the line drawn from A

CARE! some decimal formatting required also.
"""
from math import pi, asin

while True:
    r, h, s = map(int, input().split())
    if (r, h, s) == (0, 0, 0):
        break

    straight_lines = 2 * (h**2 - r**2)**0.5

    beta = asin(r / h) # angle TAC where T is tangent A is attachment and C is centre
    alpha = pi / 2 - beta # angle TCA where T is tangent C is centre and A is attachment

    round_part = (2 * pi - 2 * alpha) * r

    res = straight_lines + round_part
    res = round(res * (1 + (s * 0.01)), 2)

    print("{:.2f}".format(res)) # format 2 decimal places e.g. 10 -> 10.00 O_o