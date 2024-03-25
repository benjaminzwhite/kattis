# Johnny Applesack
# https://open.kattis.com/problems/applesack
# TAGS: logic, greedy
# CP4: 3.4e, Non Classical, Easier
# NOTES:
"""
I wrote detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/applesack.md
"""
from math import ceil

n, k = map(int, input().split())

distance = 0
while n > k:
    n -= ceil(n / k) # greedily perform option 2
    distance += 1

distance += n # perform option 1 with leftover apples

# See implementation notes, need to +1 to get number of first toolbooth you encounter where you will run out of apples.
distance += 1

print(distance)