# Antenna Analysis
# https://open.kattis.com/problems/antennaanalysis
# TAGS: array, dynamic programming, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/antennaanalysis.md
"""
n, c = map(int, input().split())

xs = list(map(int, input().split()))

res = [0] # first x value always has score 0 since no previous elements (see testcase)

big, small = xs[0], xs[0] # start the lookbehind for both the "big" and "small" options with the initial values of i=0, x=xs[0]

for x in xs[1:]:
    big = max(big - c, x) # decay the big option, or take the curr x if even bigger
    small = min(small + c, x) # decay the small option, or take the curr x if even smaller
    tmp = max(abs(x - big), abs(x - small))
    res.append(tmp)

print(*res)