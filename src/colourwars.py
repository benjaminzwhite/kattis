# Colour Wars
# https://open.kattis.com/problems/colourwars
# TAGS: logic, proof, nice
# CP4: 3.4e, Non Classical, Easier
# NOTES:
"""
Nice little puzzle: hard to explain the reasoning in writing but see below in code.

The idea that unlocks the solution is:
"If M is the real number of people who voted for the color, then up to M people can REPORT M-1 as their other-people-voted-score"
"""
from collections import Counter
from math import ceil

N = int(input())

xs = list(map(int, input().split())) # update: don't need list() only iterate once

# logic:
# Try to assign as many same votes to the same self-consistent hypothesis e.g.
# 1 1 2; assume 1 and 1 are referring to eachother so they account for 2 real people
# 100 100 100 <-- say out loud "This is consistent with 101 people voting 101, so 101 people REPORTING 100"
# in general if M is the real number of people who voted for the color, then up to M people can REPORT M-1 as their "other-people-voted-score"
# so for each value of M-1 that you find in the xs, assume that the above is the case -> ceil v/k+1 
c = Counter(xs)

res = 0
for k, v in c.items():
    res += (k + 1) * ceil(v / (k + 1))

print(res)