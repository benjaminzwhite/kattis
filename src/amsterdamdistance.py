# Amsterdam Distance
# https://open.kattis.com/problems/amsterdamdistance
# TAGS: geometry, logic
# CP4: 7.2c, Circles
# NOTES:
"""
Need to notice that you have a 2nd possibility (illustrated in 2nd test case):
you can go to centre of semicircle along a radius and back up along a radius (this may work out to be shorter)
"""
from math import pi

M, N, R = map(float, input().split())
x, y, X, Y = map(int, input().split())

path1 = R * abs(y - Y) / N + (pi * R * min(y, Y) / N) * (abs(x - X) / M)

# can go to centre and out again
path2 = R * y / N + R * Y / N

print(min(path1, path2))