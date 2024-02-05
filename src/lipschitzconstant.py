# Lipschitz Constant
# https://open.kattis.com/problems/lipschitzconstant
# TAGS: mathematics, geometry, logic
# CP4: 3.2i, Math Simulation, Harder
# NOTES:
"""
Draw 3 points in general configuration in x,y plane so they form a triangle, below comments will be much clearer then:

Of the 3 possible lines between pairs of points, the line with greatest gradient will always 
be between "first 2 x-coords" or "last 2 x-coords" and never between "first and third x-coord"
since e.g. if the middle point is above the line connecting first and last point then the line from 1st to 2nd point has > gradient
and if the middle point is below the line connecting first and last point then the line from 2nd point to 3rd point has > gradient

So sort on x coords and consider adjacent points x1,x2 and their associated gradients
-> the max_L value is among the gradients formed by these adjacent pairs
"""
N = int(input())

ts = []
for _ in range(N):
    x, y = map(float, input().split())
    ts.append((x, y))

ts = sorted(ts) # sort on x
L = -float('inf')

for fst, snd in zip(ts, ts[1:]):
    curr_L = abs(snd[1] - fst[1]) / abs(snd[0] - fst[0])
    L = max(L, curr_L)

print(L)