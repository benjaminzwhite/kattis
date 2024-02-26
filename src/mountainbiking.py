# Mountain Biking
# https://open.kattis.com/problems/mountainbiking
# TAGS: mathematics, physics
# CP4: 7.2d, Triangles (Trig)
# NOTES:
"""
I'm confused because problem statement physically doesn't make sense to me:
(you are adding velocities linearly like this despite changing horiz/vertical component) !?? 

I just reverse engineered from the first test case to see if the formula it was using
matched something like: v2**2 = v1**2 + 2*acceleration*distance and it does O_o
"""
from math import cos, radians, sqrt

N, g = input().split()
N = int(N)
g = float(g)

xs = []
for _ in range(N):
    d, theta = map(int, input().split())
    xs.append((d, theta))

for start_segment in range(N):
    vsq = sum(2 * g * d * cos(radians(theta)) for d, theta in xs[start_segment:])
    print(sqrt(vsq))