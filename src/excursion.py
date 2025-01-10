# Kindergarten Excursion
# https://open.kattis.com/problems/excursion
# TAGS: array, logic
# CP4: 2.2g, Special Sorting
# NOTES:
"""
The "obvious" way is to do some kind of swap-sorting, but if you think a bit there is a linear solution:

There are only 3 types of chars: pretend that the 1's are "inert" and are either hoppped over by 0's (which must hop over 2's also)
or are hopped over by 2's going rightwards also.
"""
s = input()

d = {'0':0, '1':0, '2':0} # this d is a counter really, stores count of how many of each char we have see as we iterate through s

res = 0
for c in s:
    if c == '0':
        res += d['1'] + d['2'] # say that 0 must hop leftwards over all 1's and 2's seen so far
    elif c == '1':
        res += d['2'] # say that 1 will be hopped over rightwards by all 2's seen so far
    d[c] += 1

print(res)