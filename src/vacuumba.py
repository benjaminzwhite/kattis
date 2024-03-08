# Vacuumba
# https://open.kattis.com/problems/vacuumba
# TAGS: mathematics, geometry
# CP4: 7.2d, Triangles (Trig)
# NOTES:
"""
I used cmath import for practice, probably much shorter ways to solve
"""
import cmath

from math import radians, pi # there is pi in cmath already O_o

T = int(input())

for _ in range(T):
    n = int(input())

    angle = pi / 2 #originally facing +y direction and at x,y = 0,0 origin
    r = 0
    curr = cmath.rect(r, angle)

    for _ in range(n):
        theta, r = map(float, input().split())
        angle += radians(theta)
        curr += cmath.rect(r, angle)

    print(curr.real, curr.imag)