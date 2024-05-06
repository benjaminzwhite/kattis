# Highest Hill
# https://open.kattis.com/problems/highesthill
# TAGS: array, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
Nice exercise.

Subtle bug/possible error:

My first version was with "if x >= prev:" but this doesn't handle cases where you have plateaus
e.g. will produce 1 for this input instead of the correct answer 6:

xs = list(map(int, "1 2 3 10 10 11 10 10 5".split()))  <--- because it will process the 10,11,10 peak 

-> The simple way to handle it is to just IGNORE cases where x == prev (since it doesn't affect anything in the calculations)
   and only update when x strictly > prev, or x strictly < prev with an ELIF statement.
"""
N = int(input())
xs = list(map(int, input().split()))

max_height = 0

climbing = False
left_min = None
peak = None

for prev, x in zip(xs, xs[1:]):
    if x > prev:
        if climbing:
            peak = x
        else:
            climbing = True
            left_min = prev
            peak = x
    elif x < prev:
        climbing = False
        if left_min is not None:
            max_height = max(max_height, min(peak - left_min, peak - x))

print(max_height)