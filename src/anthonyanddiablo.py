# Anthony and Diablo
# https://open.kattis.com/problems/anthonyanddiablo
# TAGS: basic, geometry
# CP4: 7.2c, Circles
# NOTES:
from math import pi

a, n = map(float, input().split())

if a <= pi * (n / (2 * pi))**2:
    print("Diablo is happy!")
else:
    print("Need more materials!")