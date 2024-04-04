# Grazed Grains
# https://open.kattis.com/problems/grazedgrains
# TAGS: mathematics, geometry, probability, monte carlo, nice, improve
# CP4: 3.3c, Ternary Search & Others
# NOTES:
"""
TODO: IMPROVE: think about solution for larger test cases and general approach (maybe numerical integration ?)

---

Really nice exercise, lots of possible ways of solving:

Since you have 1/10 relative error I just did a sampling approach:
overlay a grid and count how many grid points land inside any circle 
-> then divide by total grid point area to get total area occupied by circles

---

You could do this sampling approach Randomly also, randomly generate points and count how many land inside any circle
(Buffon's Needle kind of approach)
-> I made a random version but it wasn't much faster than this once you adjusted to get sufficient resolution
(have to generate lots of random numbers x and y * 100_000 or so to get resolution)
"""
# x,y from 0,0 to 10,10; and r max = 10 -> so create a sampling square grid from x=-10 to x = 20, y= -10 to y=20 will contain all circles
RANGE_START = -10
RANGE_END = 20
SCALE_MULTIPLIER = 10 # adjustable until get 1/10 relative error: determines sampling resolution at which we check the X,Y points in our grid
num_sample_points = (SCALE_MULTIPLIER * (RANGE_END - RANGE_START)) ** 2

n = int(input())
circles = []
for _ in range(n):
    x, y, r = map(int, input().split())
    circles.append((x, y, r))

cnt_hits = 0
for X in range(RANGE_START * SCALE_MULTIPLIER, RANGE_END * SCALE_MULTIPLIER + 1):
    for Y in range(RANGE_START * SCALE_MULTIPLIER, RANGE_END * SCALE_MULTIPLIER + 1):
        curr_x = X / SCALE_MULTIPLIER # should probably avoid floats but below (x-curr_x)**2 + ... expression is clearer when you compute like this (precision is OK numerically it seems)
        curr_y = Y / SCALE_MULTIPLIER
        hit = 0
        for x, y, r in circles:
            if (x - curr_x)**2 + (y - curr_y)**2 <= r * r:
                hit = 1
                break
        cnt_hits += hit

res = (cnt_hits / num_sample_points) * (RANGE_END - RANGE_START)**2

print(res)