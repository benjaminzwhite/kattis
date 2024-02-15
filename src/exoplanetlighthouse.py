# Exoplanet Lighthouse
# https://open.kattis.com/problems/exoplanetlighthouse
# TAGS: geometry
# CP4: 7.2e, Triangles + Circles
# NOTES:
from math import acos

t = int(input())

# consider angle alpha formed by r to the tangent point and r+h1 
# and angle beta formed by r to the tangent point and r+h2
for _ in range(t):
    r, h1, h2 = map(float, input().split())
    r *= 1000 # convert r to meters, avoid division on h1 and h2
    angle = acos(r / (h1 + r)) + acos(r / (h2 + r)) # alpha + beta defined above
    res = r * angle
    print(res / 1000) # convert to km