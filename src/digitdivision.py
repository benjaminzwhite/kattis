# Digit Division
# https://open.kattis.com/problems/digitdivision
# TAGS: mathematics, combinatorics, nice
# CP4: 8.7h, Mathematics+Other
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/digitdivision.md
"""
BIGMOD = 10**9 + 7

_, d = map(int, input().split())
s = input()

cnt = 0
prefix = 0
for c in map(int, s):
    prefix = prefix * 10 + c # to avoid recounting divisibilty, just *= 10 and shift digits leftwards each iteration
    prefix %= d # avoid TLE due to huge numbers: take the % of prefix each step to keep value small
    if prefix == 0:
        cnt += 1

# These are the extra checks described in the Implementation notes above
# Without these, you will get WA on some testcases - consider for example something like s=888881 with d=2
# -> without this check, my above answer would produce res = 16, when in fact res should be 0.
if prefix % d == 0 and cnt > 0:
    res = pow(2, cnt - 1, BIGMOD)
else:
    res = 0

print(res)