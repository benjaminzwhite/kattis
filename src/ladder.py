# Ladder
# https://open.kattis.com/problems/ladder
# TAGS: geometry, basic
# CP4: 7.2d, Triangles (Trig)
# NOTES:
from math import sin, ceil, radians

h, v = map(int, input().split())

res = ceil(h / sin(radians(v)))

print(res)