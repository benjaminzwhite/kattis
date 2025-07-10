# Cake
# https://open.kattis.com/problems/cake
# TAGS: array, logic, nice
# CP4: 9.cons, Construction
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/cake.md
"""
from collections import defaultdict

R, C, num_points = map(int, input().split())

POINTS = defaultdict(list)
rows = set() # you don't need this actually, noticed after submission
for _ in range(num_points):
    r, c = map(int, input().split())
    rows.add(r)
    POINTS[r].append(c)

rows = sorted(rows)
# DUMMY VALUE R+1 triggers end of zip processing - see the step with bottom_row = max(curr, below-1)  
# the right element in the zip will be below==R+1-1 == R for the last zip pair
rows.append(R + 1)

top_row = 1
for curr, below in zip(rows, rows[1:]):
    bottom_row = max(curr, below - 1)
    cols = sorted(POINTS[curr])
    n = len(cols) # need to know how many points are in this row, as we need to treat the LAST POINT differently (see NOTES)
    left_border = 1
    for i, x in enumerate(cols, 1):
        if i != n:
            # current rectangle is top_row, bottom_row, left_border, x
            # there are still points to the right of this col, so do NOT extend to rightmost edge/border
            print(top_row, left_border, bottom_row, x)
            left_border = x + 1
        else:
            # this is the last point, so need to extend its rectangle to right border i.e. C
            print(top_row, left_border, bottom_row, C)
    top_row = bottom_row + 1

print(0) # this construction always works so always 0