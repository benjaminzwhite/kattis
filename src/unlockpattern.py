# Unlock Pattern
# https://open.kattis.com/problems/unlockpattern
# TAGS: grid, geometry
# CP4: 7.2b, Lines
# NOTES:
"""
Reading comprehension:
You get a 3x3 grid which represents the actual gliding pattern (so e.g 1 is where you first place your finger etc)

Implementation:
- Enumerate rows and cols of 3x3 pattern and assign (r,c) to each of the integers 1->9 (keypad buttons)
- Then for n in range 1 to 8 (NOT 9) you incremement the total distance by the distance from n to n+1 (hence max is from n=8 to n=9)
- You find this distance by looking up the previously processed (r,c) for n and for n+1 - here added them to path {} dict.
"""
def dist(p1, p2):
    return (abs(p1[0] - p2[0])**2 + abs(p1[1] - p2[1])**2)**0.5 # don't need abs(), realized after submit O_o

path = {}

for r in range(3):
    line = input()
    for c, x in enumerate(line.split()):
        path[int(x)] = (r, c)

res = 0

for n in range(1, 8 + 1): # range up to n=8 since we will then add distance from button n = 8 to n = 9 which is the last keypress in all cases
    res += dist(path[n], path[n + 1])

print(res)