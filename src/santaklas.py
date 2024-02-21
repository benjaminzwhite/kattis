# Santa Klas
# https://open.kattis.com/problems/santaklas
# TAGS: mathematics, geometry
# CP4: 7.2d, Triangles (Trig)
# NOTES:
"""
Divide the height by the vertical velocity componenent to get the fall time
"""
from math import pi, radians, sin

h, v = map(int, input().split())

if 0 <= v <= 180:
    print("safe")
else:
    a = v - 180
    res = h / sin(radians(a))
    print(int(res))