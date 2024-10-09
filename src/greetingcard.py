# Greeting Card
# https://open.kattis.com/problems/greetingcard
# TAGS: set, precompute
# CP4: 2.3d, Hash Table (set)
# NOTES:
"""
Noticed when precomputing the integer solutions : only a few possible solutions for 
the dx,dy from a given x,y that lead to integer length DELTA distance between the 2 points
so precompute them then use MOVES to account for +/- x and y directions
"""
DELTA = 2018

# Find all integer solutions x**2+y**2 = DELTA**2
#for x in range(DELTA + 1):
#   for y in range(DELTA, x, -1):
#       if x*x + y*y == DELTA*DELTA:
#           print(x,y)
# Only solutions (in positive quadrant) are
# (0, 2018) and (1118, 1680) so consider all +/- x and +/y variants

VALS = (-2018, -1680, -1118, 0, 1118, 1680, 2018)
MOVES = [(dx, dy) for dx in VALS for dy in VALS if (dx * dx + dy * dy == DELTA * DELTA)]

seen = set()
cnt = 0

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    for (dx, dy) in MOVES:
        if (x + dx, y + dy) in seen:
            cnt += 1
    seen.add((x, y))
    
print(cnt)