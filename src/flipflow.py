# Flip Flow
# https://open.kattis.com/problems/flipflow
# TAGS: logic, array, nice
# CP4: 1.4i, Still Easy
# NOTES:
"""
Nice little exercise:

Need to be careful with all the conditions between the states - used more detailed variable names below to be clearer.

CARE! Input variables are a bit confusing - read the problem statement carefully:
t is the time "at the end" from which point you are then measuring how much MORE time until it runs out O_o
"""
t, s, n = map(int, input().split())
xs = list(map(int, input().split()))

prev_x = xs[0] # initialise with xs[0] so first step of loop corresponds to 0 sand change, just flipping lower <-> upper.
lower, upper = s, 0

for x in xs:
    time = x - prev_x
    delta_sand = min(upper, time)
    upper = max(0, upper - delta_sand)
    lower = min(s, lower + delta_sand)
    upper, lower = lower, upper
    prev_x = x

res = max(0, upper - (t - xs[-1]))

print(res)