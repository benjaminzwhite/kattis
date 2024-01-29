# The Amazing Human Cannonball
# https://open.kattis.com/problems/humancannonball2
# TAGS: basic, geometry
# CP4: 7.2d, Triangles (Trig)
# NOTES:
from math import cos, sin, pi

T = int(input())

for _ in range(T):
    v0, theta, x1, h1, h2 = map(float, input().split())

    g = 9.81

    t = x1 / (v0 * cos(2 * pi * theta / 360)) # should use math.radians

    yt = v0 * t * sin(2 * pi * theta / 360) - ((g * t * t) / 2)

    if yt - 1 >= h1 and yt + 1 <= h2:
        print("Safe")
    else:
        print("Not Safe")