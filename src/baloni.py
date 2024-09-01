# Baloni
# https://open.kattis.com/problems/baloni
# TAGS: array, dynamic programming, nice
# CP4: 2.2a, 1D Array, Medium
# NOTES:
"""
Nice exercise:

Traverse array of heights; record for each height the "height - 1" that can be hit with the same arrow

e.g. if xs = [>>>4<<<, 0, 10, 720, >>>3<<<, 0, 0]
then when you encounter x=4, add 4-1 = 3 to the dp{} so that you know you can hit a "later-occuring 3" with an existing arrow.

Then just check for each new x if it appears in dp as a "target height"-> if so, dont need to use another arrow, but 
just update dp (remove this target height, and replace with h-1 again in dp)

For each new x, if that new x does NOT appear in dp, then we will need 1 more arrow and to start from this height
(so we add target height = h - 1) with that new arrow.
"""
from collections import defaultdict

N = int(input())

xs = map(int, input().split())

dp = defaultdict(int)

arrows = 0

for x in xs:
    if x in dp:
        dp[x] -= 1
        if dp[x] == 0: # this is needed to ensure that the "if x in dp" step does not falsely activate when the value dp[x] is in fact == 0 i.e. does not appear any longer in dp{} 
            del dp[x]
        dp[x - 1] += 1
    else:
        arrows += 1
        dp[x - 1] += 1

print(arrows)