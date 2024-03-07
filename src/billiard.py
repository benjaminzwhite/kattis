# Billiard
# https://open.kattis.com/problems/billiard
# TAGS: geometry
# CP4: 7.2d, Triangles (Trig)
# NOTES:
import sys

from math import atan, degrees, sqrt

for line in sys.stdin:
    a, b, s, m, n = map(int, line.split())
    if s == 0:
        break

    angle = atan((n * b) / (m * a))
    distance = sqrt((n * b)**2 + (m * a)**2)
    velocity = distance / s

    print(f"{degrees(angle):.2f}", f"{velocity:.2f}")