# Platforme
# https://open.kattis.com/problems/platforme
# TAGS: array, sorting, intervals
# CP4: 7.2b, Lines
# NOTES:
"""
A bit frustrating/badly explained: after first submission (brute force for all intervals) failed I guessed that the description which
EXPLICITLY SAYS "no two intervals will overlap" was in fact talking about __ ___ horizontal
(which seems obvious otherwise the 2 platforms would be 1 platform)

I thought it was ruling out the case of e.g. a hi,mid,lo platform such that the mid platform "blocks access" to the lo for the hi platform
BUT IT SEEMS THAT THIS IS ALLOWED, so you have to sort by height or at least account for "line of sight"

So after that I made a bunch of submissions adjusting edge cases to see which one is intended (basically a lot of < vs <= etc.)

=> IN THE END NOTE THAT l_ <= left < r_ and h_ < height
Here when check the ranges you need to make sure STRICT INEQUALITY is on ONE SIDE only depending on
if you're treating the left or right side; this is because the pillars are "within" the length of the interval so e.g. 
think of a test case with 2 platforms 1_3 and 3_10 then first cant sit on top of 2nd etc.

Just use tests with 2_x x_21413 type cases and same heights etc. if you want to review
"""
n = int(input())

xs = []
for _ in range(n):
    height, left, right = map(int, input().split())
    xs.append((height, left, right))

xs = sorted(xs, reverse=True) # sort by descending height (t[0] is height already)

total = 0
for i, (height, left, right) in enumerate(xs):
    left_res, right_res = height, height
    LF, RF = 1, 1 # flags for if we have touched a lower platform yet (if so cant touch any lower than that)
    for (h_, l_, r_) in xs[i + 1:]:
        if l_ <= left < r_ and h_ < height and LF:
            left_res = height - h_
            LF = 0
        if l_ < right <= r_ and h_ < height and RF:
            right_res = height - h_
            RF = 0
    total += left_res + right_res

print(total)